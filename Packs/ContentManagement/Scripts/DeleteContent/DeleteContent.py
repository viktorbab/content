"""Delete Content script, used to keep instances tidy."""
from CommonServerPython import *

from abc import ABC, abstractmethod
from typing import Tuple

SCRIPT_NAME = 'DeleteContent'
ALWAYS_EXCLUDED = ['Base', 'ContentManagement', 'CleanUpContent', 'CommonDashboards', 'CommonScripts', 'CommonReports',
                   'CommonPlaybooks', 'CommonTypes', 'CommonWidgets', 'DemistoRESTAPI', 'FiltersAndTransformers',
                   'DefaultPlaybook', 'DemistoLocking']


class EntityAPI(ABC):
    """Abstract class for APIs of different content entities."""
    name = ''

    @abstractmethod
    def search_specific_id(self, specific_id: str):
        pass

    @abstractmethod
    def search_all(self):
        pass

    @abstractmethod
    def delete_specific_id(self, specific_id: str):
        pass

    @abstractmethod
    def verify_specific_search_response(self, response: Union[dict, str], name: str):
        pass

    @abstractmethod
    def parse_all_entities_response(self, response: Union[dict, str, list]):
        pass


class JobAPI(EntityAPI):
    name = 'Job'

    def search_specific_id(self, specific_id: str):
        return execute_command('demisto-api-post',
                               {'uri': '/jobs/search',
                                'body': {'page': 0, 'size': 1, 'query': f'name:"{specific_id}"'}},
                               fail_on_error=False)

    def search_all(self):
        return execute_command('demisto-api-post',
                               {'uri': '/jobs/search',
                                'body': {'page': 0, 'size': 100}},
                               fail_on_error=False)

    def delete_specific_id(self, specific_id: str):
        return execute_command('demisto-api-delete',
                               {'uri': f'jobs/{specific_id}'},
                               fail_on_error=False)

    def verify_specific_search_response(self, response: Union[dict, str], name: str):
        job_params = {}
        if type(response) is dict:
            search_results = response.get('data')
            if search_results:
                job_params = search_results[0]

        if not job_params or not job_params.get("id"):
            demisto.debug(f'{SCRIPT_NAME} - {self.name} to delete not found. Aborting.')
            return False
        return job_params.get("id")

    def parse_all_entities_response(self, response: Union[dict, str, list]):
        return [entity.get('name', '') for entity in response.get('data', [])] if type(response) is dict else []


class ListAPI(EntityAPI):
    name = 'List'

    def search_specific_id(self, specific_id: str):
        return execute_command('demisto-api-get',
                               {'uri': f'/lists/download/{specific_id}'},
                               fail_on_error=False)

    def search_all(self):
        return execute_command('demisto-api-get',
                               {'uri': '/lists/names'},
                               fail_on_error=False)

    def delete_specific_id(self, specific_id: str):
        return execute_command('demisto-api-post',
                               {'uri': '/lists/delete',
                                'body': {'id': specific_id}},
                               fail_on_error=False)

    def verify_specific_search_response(self, response: Union[dict, str], name: str):
        if response:
            return name
        return False

    def parse_all_entities_response(self, response: Union[dict, str, list]):
        return response


class InstalledPackAPI(EntityAPI):
    name = 'Pack'

    def search_specific_id(self, specific_id: str):
        return execute_command('demisto-api-get',
                               {'uri': f'/contentpacks/installed/{specific_id}'},
                               fail_on_error=False)

    def search_all(self):
        return execute_command('demisto-api-get',
                               {'uri': '/contentpacks/installed-expired'},
                               fail_on_error=False)

    def delete_specific_id(self, specific_id: str):
        return execute_command('demisto-api-delete',
                               {'uri': f'/contentpacks/installed/{specific_id}'},
                               fail_on_error=False)

    def verify_specific_search_response(self, response: Union[dict, str], name: str):

        if type(response) is dict:
            if not response or not response.get("id"):
                demisto.debug(f'{SCRIPT_NAME} - {self.name} to delete not found. Aborting.')
                return False
            return response.get("id")
        return False

    def parse_all_entities_response(self, response: Union[dict, str, list]):
        return [entity.get('id', '') for entity in response] if type(response) is list else []


def search_and_delete_existing_entity(name: str, entity_api: EntityAPI, dry_run: bool = True) -> bool:
    """Searches the machine for previously configured entity_types with the given name.

    Args:
        name (str): The name of the entity to update it's past configurations.

    Returns:
        True if deleted, False otherwise.
    """

    status, res = entity_api.search_specific_id(specific_id=name)

    if not status:
        error_message = f'{SCRIPT_NAME} - Search {entity_api.name} - {res}'
        demisto.debug(error_message)
        return False

    specific_id = entity_api.verify_specific_search_response(res.get('response'), name)

    if not specific_id:
        return False

    if not dry_run:
        status, res = entity_api.delete_specific_id(specific_id=specific_id)
    else:
        status = True
        res = True

    if not status:
        error_message = f'{SCRIPT_NAME} - Delete {entity_api.name} - {res}'
        demisto.debug(error_message)
        return False

    return True


def search_for_all_entities(entity_api: EntityAPI) -> list:
    """Search for all existing entities in xsoar.

    Args:
        entity_api (EntityAPI): The entity api to preform api calls on.

    Returns:
        list of entity ids.
    """
    status, res = entity_api.search_all()

    if not status:
        error_message = f'{SCRIPT_NAME} - Search All {entity_api.name}s - {res}'
        demisto.debug(error_message)
        raise Exception(error_message)

    entity_ids = entity_api.parse_all_entities_response(res.get('response', {}))

    return entity_ids


def get_and_delete_entities(entity_api: EntityAPI, excluded_ids: list = [], included_ids: list = [],
                            dry_run: bool = True) -> Tuple[list, list]:
    """Search and delete entities with provided EntityAPI.

    Args:
        entity_api (EntityAPI): The api object to use for the get and delete api calls.
        excluded_ids (list): List of ids to exclude from deletion.
        included_ids (list): List of ids to include in deletion.
        dry_run (bool): If true, will not really delete anything.

    Returns:
        (list) successfully deleted ids, (list) not deleted ids
    """
    succesfully_deleted = []
    not_deleted = []

    if included_ids and excluded_ids:
        raise ValueError(f'Choose to either include ids or exclude ids for {entity_api.name}.')

    if included_ids:
        for included_id in included_ids:
            if search_and_delete_existing_entity(included_id, entity_api=entity_api, dry_run=dry_run):
                succesfully_deleted.append(included_id)
            else:
                not_deleted.append(included_id)

    else:
        all_entities = search_for_all_entities(entity_api=entity_api)
        if not all_entities:
            return [], []

        for entity_id in all_entities:
            if entity_id not in excluded_ids:
                if search_and_delete_existing_entity(entity_id, entity_api=entity_api, dry_run=dry_run):
                    succesfully_deleted.append(entity_id)
                else:
                    not_deleted.append(entity_id)
            else:
                not_deleted.append(entity_id)

    return succesfully_deleted, not_deleted


def get_deletion_status(excluded: list, included: list, deleted: list, undeleted: list) -> bool:
    if excluded:
        if undeleted == excluded:
            return True
        else:
            for excluded_id in excluded:
                if excluded_id in deleted:
                    return False
            return True

    elif included:
        if set(deleted) == set(included):
            return True
    # Nothing excluded
    elif not undeleted:
        return True
    return False


def handle_content_enitity(entity_api: EntityAPI, args: dict, dry_run: bool, delete_unspecified: bool) -> Tuple[bool, dict, dict]:
    exclude_ids = argToList(args.get(f'exclude_{entity_api.name.lower()}_ids', '[]'))
    include_ids = argToList(args.get(f'include_{entity_api.name.lower()}_ids', '[]'))

    if entity_api.name == 'Pack' and exclude_ids:
        exclude_ids += ALWAYS_EXCLUDED

    deleted_ids: list = []
    undeleted_ids: list = []
    deletion_status = True
    if exclude_ids or include_ids or delete_unspecified:
        deleted_ids, undeleted_ids = get_and_delete_entities(entity_api=entity_api,
                                                             excluded_ids=exclude_ids,
                                                             included_ids=include_ids,
                                                             dry_run=dry_run)

        deletion_status = get_deletion_status(excluded=exclude_ids, included=include_ids,
                                              deleted=deleted_ids, undeleted=undeleted_ids)

    return deletion_status, {entity_api.name: deleted_ids}, {entity_api.name: undeleted_ids}


def get_and_delete_needed_ids(args: dict) -> CommandResults:
    """Search and delete provided ids to delete.

    Args:
        args[exclude_job_ids] (str(list)): List of job ids to exclude. Will delete all the rest of the found ids.
        args[include_job_ids] (str(list)): List of job ids to include. Will only delete these ids if not empty.
        args[exclude_list_ids] (str(list)): List of list ids to exclude. Will delete all the rest of the found ids.
        args[include_list_ids] (str(list)): List of list ids to include. Will only delete these ids if not empty.
        args[exclude_pack_ids] (str(list)): List of pack ids to exclude. Will delete all the rest of the found ids.
        args[include_pack_ids] (str(list)): List of pack ids to include. Will only delete these ids if not empty.
        args[dry_run] (str(bool)): If True, will only collect items for deletion and will not delete them.

    Raise:
        ValueError if both exclude_ids and include_ids are specified.

    Returns:
        CommandResults with the following outputs:
            successfully_deleted: list of content ids gathered for deletion.
            not_deleted: list of content ids gathered not to delete.
            status: Deletion status (Failed/Completed/Dry run, nothing really deleted.)
    """
    dry_run = True if args.get('dry_run', 'true') == 'true' else False
    delete_unspecified = True if args.get('delete_unspecified', 'true') == 'true' else False
    entities_to_delete = [JobAPI(), ListAPI(), InstalledPackAPI()]

    all_deleted: dict = dict()
    all_not_deleted: dict = dict()
    all_deletion_statuses: list = []
    for entity in entities_to_delete:
        entity_deletion_status, deleted, undeleted = handle_content_enitity(entity, args, dry_run, delete_unspecified)
        all_deleted.update(deleted)
        all_not_deleted.update(undeleted)
        all_deletion_statuses.append(entity_deletion_status)

    deletion_status = 'Failed'
    if dry_run:
        deletion_status = 'Dry run, nothing really deleted.'
    else:
        if all(all_deletion_statuses):
            deletion_status = 'Completed'

    return CommandResults(
        outputs_prefix='ConfigurationSetup.Deletion',
        outputs_key_field='name',
        outputs={
            'successfully_deleted': all_deleted,
            'not_deleted': all_not_deleted,
            'status': deletion_status,
        },
    )


def main():
    try:
        return_results(get_and_delete_needed_ids(demisto.args()))

    except Exception as e:
        return_error(f'{SCRIPT_NAME} - Error occurred while deleting contents.\n{e}'
                     f'\n{traceback.format_exc()}')


if __name__ in ('__main__', '__builtin__', 'builtins'):
    main()