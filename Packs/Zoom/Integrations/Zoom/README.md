Use the Zoom integration manage your Zoom users and meetings
This integration was integrated and tested with version 2 of Zoom API

## Configure Zoom on Cortex XSOAR

1. Navigate to **Settings** > **Integrations** > **Servers & Services**.
2. Search for Zoom.
3. Click **Add instance** to create and configure a new integration instance.

    | **Parameter** | **Description** | **Required** |
    | --- | --- | --- |
    | Server URL (e.g. 'https://api.zoom.us/v2/') |  | True |
    | Account ID (OAuth) |  | False |
    | Client ID (OAuth) |  | False |
    | Client Secret (OAuth) |  | False |
    | API Key (JWT-Deprecated) | This authentication method is deprecated | False |
    | API Secret (JWT-Deprecated) | This authentication method is deprecated | False |
    | Use system proxy settings |  | False |
    | Trust any certificate (not secure) |  | False |

4. Click **Test** to validate the URLs, token, and connection.
## Commands
You can execute these commands from the Cortex XSOAR CLI, as part of an automation, or in a playbook.
After you successfully execute a command, a DBot message appears in the War Room with the command details.
### zoom-create-user
***
Create a new user in zoom account


#### Base Command

`zoom-create-user`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| first_name | First name of the new user. | Required | 
| last_name | Last name of the new user. | Required | 
| email | The email of the new user. | Required | 
| user_type | The type of the newly created user.  Note: the old type "pro" in now called "Licensed", and the type "Corporate" is not sopprted in Zoom v2 and above.<br/>. Possible values are: Basic, Licensed, pro, Corporate. Default is Basic. | Optional | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Zoom.User.id | string | The ID of the created user | 
| Zoom.User.first_name | string | First name of the created user | 
| Zoom.User.last_name | string | Last name for the created user | 
| Zoom.User.email | string | Email of the created user | 
| Zoom.User.created_at | date | Created date of the user. Note that this field does not appear in zoom v2 and above. | 
| Zoom.User.type | number | The type of the user | 

#### Command example
```!zoom-create-user email=example@example.com first_name=john last_name=smith user_type=Basic ```
#### Context Example
```json
{
    "Zoom": {
        "User": {
            "email": "example@example.com",
            "first_name": "john",
            "id": "wSQafNLNSJWq_oBzmT7XOw",
            "last_name": "smith",
            "type": 1
        }
    }
}
```

#### Human Readable Output

>User created successfully with ID: wSQafNLNSJWq_oBzmT7XOw

### zoom-create-meeting
***
Create a new zoom meeting (scheduled ,instant, or recurring)


#### Base Command

`zoom-create-meeting`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| type | The type of the meeting. Possible values are: instant, scheduled, recurring meeting with fixed time. Default is Instant. | Required | 
| end_date_time | For recurring meetings only. Select the final date on which the meeting will recur before it is canceled<br/>For example: 2017-11-25T12:00:00Z<br/>. | Optional | 
| end_times | For recurring meetings only.<br/>Select how many times the meeting should recur before it is canceled. <br/>max = 365. Default = 1.<br/>. | Optional | 
| monthly_day | For recurring meetings with Monthly recurrence_type only.<br/>State the day in a month, the meeting should recur. The value range is from 1 to 31. Default = 1.<br/>. | Optional | 
| monthly_week | For recurring meetings with Monthly recurrence_type only.<br/>State the week of the month when the meeting should recur. If you use this field, you must also use the monthly_week_day field to state the day of the week when the meeting should recur. Allowed: -1 (for last week of the month) ┃1┃2┃3┃4<br/>. | Optional | 
| monthly_week_day | For recurring meetings with Monthly recurrence_type only.<br/>State a specific day in a week when the monthly meeting should recur. Allowed: 1┃2┃3┃4┃5┃6┃7<br/>To use this field, you must also use the monthly_week field.<br/>. | Optional | 
| repeat_interval | For recurring meeting with fixed time only.<br/>Define the interval at which the meeting should recur. For instance, if you would like to schedule a meeting that recurs every two months, you must set the value of this field as 2 and the value of the type parameter as Monthly.<br/>For a daily meeting, the maximum is 90 days. For a weekly meeting the maximum is of 12 weeks. For a monthly meeting, there is a maximum of 3 months.<br/>. | Optional | 
| recurrence_type | For recurring meetings  only.<br/>Set the recurrence meeting types.<br/>. Possible values are: Daily, Weekly, Monthly. | Optional | 
| weekly_days | For recurring meetings with a Weekly recurrence_type only.<br/>State a specific day in a week when the weekly meeting should recur. Allowed: 1┃2┃3┃4┃5┃6┃7  Default = 1.<br/>. | Optional | 
| auto-record-meeting | The automatic recording settings. <br/>Note that the Cloud option is available for zoom paid customers only.<br/>. Possible values are: local, cloud, none. Default is none. | Optional | 
| encryption_type | The type of end-to-end (E2EE) encryption, enhanced_encryption or e2ee. Possible values are: enhanced_encryption, e2ee. Default is enhanced_encryption. | Optional | 
| host_video | start meetings with the host video on. Possible values are: true, false. Default is True. | Optional | 
| join_before_host_time | If the value of the join_before_host field is true, this field sets the time that a participant can join before the meeting's host. <br/>You can choose: 5 or 10 (minuts), or 0 for any time.<br/>. Possible values are: 0, 5, 10. | Optional | 
| join_before_host | Whether participants can join the meeting before its host. For scheduled or recurring meetings only. The default value is False. Possible values are: False, True. | Optional | 
| meeting_authentication | If true, only authenticated users can join the meeting. Possible values are: false, true. Default is false. | Optional | 
| user | email address or id of user for meeting. | Required | 
| topic | The topic of the meeting. | Required | 
| waiting_room | This allows the host to control when a participant joins the meeting. The default is False. Possible values are: false, true. | Optional | 
| start-time | Meeting start time. When using a format like “yyyy-MM-ddTHH:mm:ssZ”, always use GMT time. When using a format like “yyyy-MM-ddTHH:mm:ss”, you should use local time and you will need to specify the time zone. Only used for scheduled meetings and recurring meetings with fixed time. | Optional | 
| timezone | Timezone to format start_time. For example, “America/Los_Angeles”. For scheduled meetings only. . | Optional | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Zoom.Meeting.join_url | string | Join url for the meeting | 
| Zoom.Meeting.id | string | Meeting id of the new meeting that is created | 
| Zoom.Meeting.start_url | string | The URL to start the meeting | 
| Zoom.Meeting.uuid | string | Unique meeting ID of the new meeting that is created | 
| Zoom.Meeting.status | string | The status of the meeting | 
| Zoom.Meeting.start_time | Date | The time that the meeting will start at | 
| Zoom.Meeting.host email | string | The email of the host of this meeting | 
| Zoom.Meeting.topic | string | The topic of the meeting | 
| Zoom.Meeting.duration | number | The duratian of the meeting | 
| Zoom.Meeting.created_at | Date | The time that this meeting was created | 
| Zoom.Meeting.type | number | The type of the new meeting, Instant = 1, Scheduled =2,Recurring with fixed time = 8 | 

#### Command example
```!zoom-create-meeting topic=test type=scheduled user=example@example.com start-time=2022-12-29T12:12:12Z ```
#### Context Example
```json
{
    "Zoom": {
        "Meeting": {
            "created_at": "2022-12-29T08:14:39Z",
            "duration": 60,
            "host_email": "example@example.com",
            "host_id": "uJiZN-O7Rp6Jp_995FpZGg",
            "id": 81967809573,
            "join_url": "https://us06web.zoom.us/j/81967809573?pwd=S1NuSEovNWRXSGJNZHRsWDNOSkFkUT09",
            "pre_schedule": false,
            "settings": {
                "allow_multiple_devices": false,
                "alternative_host_update_polls": false,
                "alternative_hosts": "",
                "alternative_hosts_email_notification": true,
                "approval_type": 2,
                "approved_or_denied_countries_or_regions": {
                    "enable": false
                },
                "audio": "both",
                "auto_recording": "none",
                "breakout_room": {
                    "enable": false
                },
                "close_registration": false,
                "cn_meeting": false,
                "device_testing": false,
                "email_notification": true,
                "enable_dedicated_group_chat": false,
                "encryption_type": "enhanced_encryption",
                "enforce_login": false,
                "enforce_login_domains": "",
                "focus_mode": false,
                "global_dial_in_countries": [
                    "US"
                ],
                "global_dial_in_numbers": [
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 6694449171",
                        "type": "toll"
                    },
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 6892781000",
                        "type": "toll"
                    },
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 7193594580",
                        "type": "toll"
                    },
                    {
                        "city": "Denver",
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 7207072699",
                        "type": "toll"
                    },
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 2532050468",
                        "type": "toll"
                    },
                    {
                        "city": "Tacoma",
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 2532158782",
                        "type": "toll"
                    },
                    {
                        "city": "Washington DC",
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 3017158592",
                        "type": "toll"
                    },
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 3052241968",
                        "type": "toll"
                    },
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 3092053325",
                        "type": "toll"
                    },
                    {
                        "city": "Houston",
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 3126266799",
                        "type": "toll"
                    },
                    {
                        "city": "Houston",
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 3462487799",
                        "type": "toll"
                    },
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 3602095623",
                        "type": "toll"
                    },
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 3863475053",
                        "type": "toll"
                    },
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 5074734847",
                        "type": "toll"
                    },
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 5642172000",
                        "type": "toll"
                    },
                    {
                        "city": "New York",
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 6465588656",
                        "type": "toll"
                    },
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 6469313860",
                        "type": "toll"
                    }
                ],
                "host_save_video_order": false,
                "host_video": true,
                "in_meeting": false,
                "jbh_time": 0,
                "join_before_host": false,
                "meeting_authentication": false,
                "mute_upon_entry": false,
                "participant_video": false,
                "private_meeting": false,
                "registrants_confirmation_email": true,
                "registrants_email_notification": true,
                "request_permission_to_unmute_participants": false,
                "show_share_button": false,
                "use_pmi": false,
                "waiting_room": false,
                "watermark": false
            },
            "start_time": "2022-12-29T12:12:12Z",
            "start_url": "https://us06web.zoom.us/s/81967809573?zak=eyJ0eXAiOiJKV1QiLCJzdiI6IjAwMDAwMSIsInptX3NrbSI6InptX28ybSIsImFsZyI6IkhTMjU2In0.eyJhdWQiOiJjbGllbnRzbSIsInVpZCI6InVKaVpOLU83UnA2SnBfOTk1RnBaR2ciLCJpc3MiOiJ3ZWIiLCJzayI6IjczMjU5NTExMTgxNDYyODc0NjciLCJzdHkiOjEwMCwid2NkIjoidXMwNiIsImNsdCI6MCwibW51bSI6IjgxOTY3ODA5NTczIiwiZXhwIjoxNjcyMzA4ODc5LCJpYXQiOjE2NzIzMDE2NzksImFpZCI6ImFlS0QyQkZKUkFTdDFRVlVSV285Q0EiLCJjaWQiOiIifQ.u77iCWCY0KP2oY5wb9ABzudnFUB8TmqgL7qUdo8sXgg",
            "status": "waiting",
            "timezone": "Asia/Jerusalem",
            "topic": "test",
            "type": 2,
            "uuid": "fQbNc0ZUTECrosWSasccxw=="
        }
    }
}
```

#### Human Readable Output

>### Meeting details
>|uuid|id|host_id|host_email|topic|type|status|start_time|duration|timezone|created_at|start_url|join_url|
>|---|---|---|---|---|---|---|---|---|---|---|---|---|
>| fQbNc0ZUTECrosWSasccxw== | 81967809573 | uJiZN-O7Rp6Jp_995FpZGg | example@example.com | test | 2 | waiting | 2022-12-29T12:12:12Z | 60 | Asia/Jerusalem | 2022-12-29T08:14:39Z | https:<span>//</span>us06web.zoom.us/s/81967809573?zak=eyJ0eXAiOiJKV1QiLCJzdiI6IjAwMDAwMSIsInptX3NrbSI6InptX28ybSIsImFsZyI6IkhTMjU2In0.eyJhdWQiOiJjbGllbnRzbSIsInVpZCI6InVKaVpOLU83UnA2SnBfOTk1RnBaR2ciLCJpc3MiOiJ3ZWIiLCJzayI6IjczMjU5NTExMTgxNDYyODc0NjciLCJzdHkiOjEwMCwid2NkIjoidXMwNiIsImNsdCI6MCwibW51bSI6IjgxOTY3ODA5NTczIiwiZXhwIjoxNjcyMzA4ODc5LCJpYXQiOjE2NzIzMDE2NzksImFpZCI6ImFlS0QyQkZKUkFTdDFRVlVSV285Q0EiLCJjaWQiOiIifQ.u77iCWCY0KP2oY5wb9ABzudnFUB8TmqgL7qUdo8sXgg | https:<span>//</span>us06web.zoom.us/j/81967809573?pwd=S1NuSEovNWRXSGJNZHRsWDNOSkFkUT09 |


### zoom-fetch-recording
***
Get meeting record and save as file in the warroom


#### Base Command

`zoom-fetch-recording`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| meeting_id | Meeting id to get the recording. | Required | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| File.SHA256 | Unknown | Attachment's SHA256 | 
| File.SHA1 | Unknown | Attachment's SHA1 | 
| File.MD5 | Unknown | Attachment's MD5 | 
| File.Name | Unknown | Attachment's Name | 
| File.Info | Unknown | Attachment's Info | 
| File.Size | Unknown | Attachment's Size \(In Bytes\) | 
| File.Extension | Unknown | Attachment's Extension | 
| File.Type | Unknown | Attachment's Type | 
| File.EntryID | Unknown | Attachment's EntryID | 
| File.SSDeep | Unknown | Attachment's SSDeep hash | 

### zoom-list-users
***
List the existing users


#### Base Command

`zoom-list-users`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| status | Which status of users to list. Possible values are: active, inactive, pending. Default is active. | Optional | 
| page-size | Number of users to return. Max 300. The default is 30. | Optional | 
| next_page_token | The next page token is used to get the next page. IMPORTENT: You must pass the same page size that you pased at the first call.<br/>. | Optional | 
| page-number | Which page of results to return. The default = 1.<br/>Note: This argument is in a deprecate process by the API. As an alternative use "next_page_token" or "limit".<br/>. | Optional | 
| limit | The total amunt of results to show. | Optional | 
| user_id | A user ID. this is for a singel user. | Optional | 
| role_id | Filter the response by a specific role.<br/>For example: role_id=0 (Owner), role_id=2 (Member)<br/>. | Optional | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Zoom.Metadata.Count | number | Total page count available | 
| Zoom.Metadata.Number | number | Current page number | 
| Zoom.Metadata.Size | number | Number of results in current page | 
| Zoom.Metadata.Total | number | Total number of records | 
| Zoom.User.id | string | ID of the user | 
| Zoom.User.first_name | string | First name of user | 
| Zoom.User.last_name | string | Last name of user | 
| Zoom.User.email | string | Email of user | 
| Zoom.User.type | number | Type of user | 
| Zoom.User.created_at | date | Date when user was created | 
| Zoom.User.dept | string | Department for user | 
| Zoom.User.verified | number | Is the user verified | 
| Zoom.User.last_login_time | date | Last login time of the user | 
| Zoom.User.timezone | string | Default timezone for the user | 
| Zoom.User.pmi | string | PMI of user | 
| Zoom.User.group_ids | string | Groups user belongs to | 

#### Command example
```!zoom-list-users status=pending limit=10 ```
#### Context Example
```json
{
    "Zoom": {
        "Metadata": {
            "Count": 2,
            "Number": 1,
            "Size": 10,
            "Total": 11
        },
        "User": [
            {
                "created_at": "2022-12-29T08:14:44Z",
                "email": "me3s56f1yhlvdqn@demistomockemail.com",
                "id": "",
                "pmi": 0,
                "role_id": "0",
                "status": "pending",
                "type": 1,
                "user_created_at": "2022-12-22T10:19:47Z",
                "verified": 0
            },
            {
                "created_at": "2022-12-29T08:14:44Z",
                "email": "berg@ks.com",
                "id": "",
                "pmi": 0,
                "role_id": "0",
                "status": "pending",
                "type": 1,
                "user_created_at": "2022-12-14T07:37:02Z",
                "verified": 0
            },
            {
                "created_at": "2022-12-29T08:14:44Z",
                "email": "r2e2fxzmphomnc1@demistomockemail.com",
                "id": "",
                "pmi": 0,
                "role_id": "0",
                "status": "pending",
                "type": 1,
                "user_created_at": "2022-12-22T08:04:33Z",
                "verified": 0
            },
            {
                "created_at": "2022-12-29T08:14:44Z",
                "email": "ax0qwkfpctfuz06@demistomockemail.com",
                "id": "",
                "pmi": 0,
                "role_id": "0",
                "status": "pending",
                "type": 1,
                "user_created_at": "2022-12-22T10:19:12Z",
                "verified": 0
            },
            {
                "created_at": "2022-12-29T08:14:44Z",
                "email": "example@example.com",
                "id": "",
                "pmi": 0,
                "role_id": "0",
                "status": "pending",
                "type": 1,
                "user_created_at": "2022-12-22T10:13:30Z",
                "verified": 0
            },
            {
                "created_at": "2022-12-29T08:14:44Z",
                "email": "example@example.com",
                "id": "",
                "pmi": 0,
                "role_id": "0",
                "status": "pending",
                "type": 1,
                "user_created_at": "2022-12-14T07:19:20Z",
                "verified": 0
            },
            {
                "created_at": "2022-12-29T08:14:44Z",
                "email": "qmeb9kypck6utf1@demistomockemail.com",
                "id": "",
                "pmi": 0,
                "role_id": "0",
                "status": "pending",
                "type": 1,
                "user_created_at": "2022-12-22T10:15:41Z",
                "verified": 0
            },
            {
                "created_at": "2022-12-29T08:14:44Z",
                "email": "example@example.com",
                "id": "",
                "pmi": 0,
                "role_id": "0",
                "status": "pending",
                "type": 1,
                "user_created_at": "2022-12-07T07:38:41Z",
                "verified": 0
            },
            {
                "created_at": "2022-12-29T08:14:44Z",
                "email": "example@example.com",
                "id": "",
                "pmi": 0,
                "role_id": "0",
                "status": "pending",
                "type": 1,
                "user_created_at": "2022-12-07T07:39:52Z",
                "verified": 0
            },
            {
                "created_at": "2022-12-29T08:14:44Z",
                "email": "example@example.com",
                "id": "",
                "pmi": 0,
                "role_id": "0",
                "status": "pending",
                "type": 1,
                "user_created_at": "2022-12-07T07:37:11Z",
                "verified": 0
            }
        ]
    }
}
```

#### Human Readable Output

>### Users
>|id|email|type|pmi|verified|created_at|status|role_id|
>|---|---|---|---|---|---|---|---|
>|  | me3s56f1yhlvdqn@demistomockemail.com | 1 | 0 | 0 | 2022-12-29T08:14:44Z | pending | 0 |
>|  | berg@ks.com | 1 | 0 | 0 | 2022-12-29T08:14:44Z | pending | 0 |
>|  | r2e2fxzmphomnc1@demistomockemail.com | 1 | 0 | 0 | 2022-12-29T08:14:44Z | pending | 0 |
>|  | ax0qwkfpctfuz06@demistomockemail.com | 1 | 0 | 0 | 2022-12-29T08:14:44Z | pending | 0 |
>|  | example@example.com | 1 | 0 | 0 | 2022-12-29T08:14:44Z | pending | 0 |
>|  | example@example.com | 1 | 0 | 0 | 2022-12-29T08:14:44Z | pending | 0 |
>|  | qmeb9kypck6utf1@demistomockemail.com | 1 | 0 | 0 | 2022-12-29T08:14:44Z | pending | 0 |
>|  | example@example.com | 1 | 0 | 0 | 2022-12-29T08:14:44Z | pending | 0 |
>|  | example@example.com | 1 | 0 | 0 | 2022-12-29T08:14:44Z | pending | 0 |
>|  | example@example.com | 1 | 0 | 0 | 2022-12-29T08:14:44Z | pending | 0 |
>
>### Metadata
>|total_records|
>|---|
>| 11 |


### zoom-delete-user
***
Delete a user from Zoom


#### Base Command

`zoom-delete-user`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| user_id | The user ID or email to delete. | Required | 
| action | The action to take. Possible values are: disassociate, delete. Default is disassociate. | Optional | 


#### Context Output

There is no context output for this command.
### zoom-meeting-get
***
Get the information of an existing zoom meeting


#### Base Command

`zoom-meeting-get`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| meeting_id | The id of the existing meeting. | Required | 
| occurrence_id | Provide this field to view meeting details of a particular occurrence of the recurring meeting. | Optional | 
| show_previous_occurrences | Set the value of this field to true if you would like to view meeting details of all previous occurrences of a recurring meeting. Possible values are: False, True. Default is True. | Optional | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Zoom.Meeting.join_url | string | Join url for the meeting | 
| Zoom.Meeting.id | string | Meeting id of the new meeting that is created | 
| Zoom.Meeting.start_url | string | The URL to start the meeting | 
| Zoom.Meeting.uuid | string | Unique meeting ID of the new meeting that is created | 
| Zoom.Meeting.status | string | The status of the meeting | 
| Zoom.Meeting.start_time | Date | The time that the meeting will start at | 
| Zoom.Meeting.host email | string | The email of the host of this meeting | 
| Zoom.Meeting.topic | string | The topic of the meeting | 
| Zoom.Meeting.duration | number | The duratian of the meeting | 
| Zoom.Meeting.created_at | Date | The time that this meeting was created | 
| Zoom.Meeting.type | number | The type of the new meeting, Instant = 1, Scheduled =2,Recurring with fixed time = 8 | 

#### Command example
```!zoom-meeting-get meeting_id=85235660275 ```
#### Context Example
```json
{
    "Zoom": {
        "Meeting": {
            "agenda": "",
            "assistant_id": "",
            "created_at": "2022-12-29T07:35:10Z",
            "duration": 60,
            "host_email": "example@example.com",
            "host_id": "uJiZN-O7Rp6Jp_995FpZGg",
            "id": 85235660275,
            "join_url": "https://us06web.zoom.us/j/85235660275?pwd=UWRXdDNyM3JaMnNJZ3pCZ1YyZ3FyUT09",
            "pre_schedule": false,
            "settings": {
                "allow_multiple_devices": false,
                "alternative_host_update_polls": false,
                "alternative_hosts": "",
                "alternative_hosts_email_notification": true,
                "approval_type": 2,
                "approved_or_denied_countries_or_regions": {
                    "enable": false
                },
                "audio": "both",
                "auto_recording": "none",
                "breakout_room": {
                    "enable": false
                },
                "close_registration": false,
                "cn_meeting": false,
                "device_testing": false,
                "email_notification": true,
                "enable_dedicated_group_chat": false,
                "encryption_type": "enhanced_encryption",
                "enforce_login": false,
                "enforce_login_domains": "",
                "focus_mode": false,
                "global_dial_in_countries": [
                    "US"
                ],
                "global_dial_in_numbers": [
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 7193594580",
                        "type": "toll"
                    },
                    {
                        "city": "Denver",
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 7207072699",
                        "type": "toll"
                    },
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 2532050468",
                        "type": "toll"
                    },
                    {
                        "city": "Tacoma",
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 2532158782",
                        "type": "toll"
                    },
                    {
                        "city": "Washington DC",
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 3017158592",
                        "type": "toll"
                    },
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 3052241968",
                        "type": "toll"
                    },
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 3092053325",
                        "type": "toll"
                    },
                    {
                        "city": "Houston",
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 3126266799",
                        "type": "toll"
                    },
                    {
                        "city": "Houston",
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 3462487799",
                        "type": "toll"
                    },
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 3602095623",
                        "type": "toll"
                    },
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 3863475053",
                        "type": "toll"
                    },
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 5074734847",
                        "type": "toll"
                    },
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 5642172000",
                        "type": "toll"
                    },
                    {
                        "city": "New York",
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 6465588656",
                        "type": "toll"
                    },
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 6469313860",
                        "type": "toll"
                    },
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 6694449171",
                        "type": "toll"
                    },
                    {
                        "country": "US",
                        "country_name": "US",
                        "number": "+1 6892781000",
                        "type": "toll"
                    }
                ],
                "host_save_video_order": false,
                "host_video": true,
                "in_meeting": false,
                "jbh_time": 0,
                "join_before_host": false,
                "meeting_authentication": false,
                "mute_upon_entry": false,
                "participant_video": false,
                "private_meeting": false,
                "registrants_confirmation_email": true,
                "registrants_email_notification": true,
                "request_permission_to_unmute_participants": false,
                "show_share_button": false,
                "use_pmi": false,
                "waiting_room": false,
                "watermark": false
            },
            "start_time": "2022-12-29T12:12:12Z",
            "start_url": "https://us06web.zoom.us/s/85235660275?zak=eyJ0eXAiOiJKV1QiLCJzdiI6IjAwMDAwMSIsInptX3NrbSI6InptX28ybSIsImFsZyI6IkhTMjU2In0.eyJhdWQiOiJjbGllbnRzbSIsInVpZCI6InVKaVpOLU83UnA2SnBfOTk1RnBaR2ciLCJpc3MiOiJ3ZWIiLCJzayI6IjczMjU5NTExMTgxNDYyODc0NjciLCJzdHkiOjEwMCwid2NkIjoidXMwNiIsImNsdCI6MCwibW51bSI6Ijg1MjM1NjYwMjc1IiwiZXhwIjoxNjcyMzA4ODg1LCJpYXQiOjE2NzIzMDE2ODUsImFpZCI6ImFlS0QyQkZKUkFTdDFRVlVSV285Q0EiLCJjaWQiOiIifQ.O_0oFbJ4ptJDVhGUSugGT2Uvw7zCzR4M-KUbDr23fJI",
            "status": "waiting",
            "timezone": "Asia/Jerusalem",
            "topic": "test",
            "type": 2,
            "uuid": "987MfVRLQR2UXxYxo9k0rA=="
        }
    }
}
```

#### Human Readable Output

>### Meeting details
>|uuid|id|host_id|host_email|topic|type|status|start_time|duration|timezone|agenda|created_at|start_url|join_url|
>|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
>| 987MfVRLQR2UXxYxo9k0rA== | 85235660275 | uJiZN-O7Rp6Jp_995FpZGg | example@example.com | test | 2 | waiting | 2022-12-29T12:12:12Z | 60 | Asia/Jerusalem |  | 2022-12-29T07:35:10Z | https:<span>//</span>us06web.zoom.us/s/85235660275?zak=eyJ0eXAiOiJKV1QiLCJzdiI6IjAwMDAwMSIsInptX3NrbSI6InptX28ybSIsImFsZyI6IkhTMjU2In0.eyJhdWQiOiJjbGllbnRzbSIsInVpZCI6InVKaVpOLU83UnA2SnBfOTk1RnBaR2ciLCJpc3MiOiJ3ZWIiLCJzayI6IjczMjU5NTExMTgxNDYyODc0NjciLCJzdHkiOjEwMCwid2NkIjoidXMwNiIsImNsdCI6MCwibW51bSI6Ijg1MjM1NjYwMjc1IiwiZXhwIjoxNjcyMzA4ODg1LCJpYXQiOjE2NzIzMDE2ODUsImFpZCI6ImFlS0QyQkZKUkFTdDFRVlVSV285Q0EiLCJjaWQiOiIifQ.O_0oFbJ4ptJDVhGUSugGT2Uvw7zCzR4M-KUbDr23fJI | https:<span>//</span>us06web.zoom.us/j/85235660275?pwd=UWRXdDNyM3JaMnNJZ3pCZ1YyZ3FyUT09 |


### zoom-meeting-list
***
Show all the meetings of a given user. Note: only scheduled and unexpired meetings will appear.



#### Base Command

`zoom-meeting-list`
#### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| user_id | The user ID. | Required | 
| page_size | Number of users to return. Default = 30. Max = 300. | Optional | 
| page_number | Which page of results to return. The default = 1.<br/>Note: This argument is in a deprecate process by the API. As an alternative use "next_page_token" or "limit".<br/>. | Optional | 
| next_page_token | The next page token is used to paginate te the next page. IMPORTENT: You must pass the same page size that you pased at the first call.<br/>. | Optional | 
| limit | The total amunt of results to show. | Optional | 
| type | Filter the results by searching specific types. Possible values are: all, scheduled, live, upcoming, upcoming_meetings, previous_meetings. Default is "scheduled". | Optional | 


#### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Zoom.Metadata.Total | number | Total number of records | 
| Zoom.Meeting.page_size | number | The size of the page returned from the API | 
| Zoom.Meeting.total_records | number | The total records in the API for this request. | 
| Zoom.Meeting.join_url | string | Join url for the meeting | 
| Zoom.Meeting.id | string | Meeting id of the new meeting that is created | 
| Zoom.Meeting.start_url | string | The URL to start the meeting | 
| Zoom.Meeting.uuid | string | Unique meeting ID of the new meeting that is created | 
| Zoom.Meeting.status | string | The status of the meeting | 
| Zoom.Meeting.start_time | Date | The time that the meeting will start at | 
| Zoom.Meeting.host email | string | The email of the host of this meeting | 
| Zoom.Meeting.topic | string | The topic of the meeting | 
| Zoom.Meeting.duration | number | The duratian of the meeting | 
| Zoom.Meeting.created_at | Date | The time that this meeting was created | 
| Zoom.Meeting.type | unknown |  | 

#### Command example
```!zoom-meeting-list user_id=example@example.com type=scheduled limit=7 ```
#### Context Example
```json
{
    "Zoom": {
        "Meeting": {
            "meetings": [
                {
                    "created_at": "2022-12-04T10:41:27Z",
                    "duration": 60,
                    "host_id": "uJiZN-O7Rp6Jp_995FpZGg",
                    "id": 83810397585,
                    "join_url": "https://us06web.zoom.us/j/83810397585?pwd=OGFiZjRYNGhwWkVvMWZzdDBoaXlLdz09",
                    "start_time": "2022-12-10T11:00:00Z",
                    "timezone": "Asia/Jerusalem",
                    "topic": "2",
                    "type": 8,
                    "uuid": "z93Dc6KjSo20Wr3jx+zaYg=="
                },
                {
                    "created_at": "2022-12-06T07:59:02Z",
                    "duration": 60,
                    "host_id": "uJiZN-O7Rp6Jp_995FpZGg",
                    "id": 84540166459,
                    "join_url": "https://us06web.zoom.us/j/84540166459?pwd=ZzdmUEJ5QkZaaUZaaVpFYlBVYnFoUT09",
                    "start_time": "2022-12-12T08:00:00Z",
                    "timezone": "Asia/Jerusalem",
                    "topic": "My recurring Meeting -Dima",
                    "type": 8,
                    "uuid": "4kZQ+Hl2RFOAz0VBPHoCYg=="
                },
                {
                    "created_at": "2022-12-27T21:05:41Z",
                    "duration": 60,
                    "host_id": "uJiZN-O7Rp6Jp_995FpZGg",
                    "id": 89824497327,
                    "join_url": "https://us06web.zoom.us/j/89824497327?pwd=SWpvK0I0L3pQcTNnWlF3b3VDRVhmQT09",
                    "start_time": "2022-12-27T21:05:00Z",
                    "timezone": "Asia/Jerusalem",
                    "topic": "efe",
                    "type": 8,
                    "uuid": "RABXyk81T02D4hA1rgpDgQ=="
                },
                {
                    "created_at": "2022-12-27T21:11:01Z",
                    "duration": 60,
                    "host_id": "uJiZN-O7Rp6Jp_995FpZGg",
                    "id": 83245658341,
                    "join_url": "https://us06web.zoom.us/j/83245658341?pwd=SmNGMHI0R1hndnNlRXRDNkZ2Yms3Zz09",
                    "start_time": "2022-12-27T21:11:00Z",
                    "timezone": "Asia/Jerusalem",
                    "topic": "efe",
                    "type": 8,
                    "uuid": "qOXvlLOoSamJjjFaFgniTA=="
                },
                {
                    "created_at": "2022-12-27T21:25:54Z",
                    "duration": 60,
                    "host_id": "uJiZN-O7Rp6Jp_995FpZGg",
                    "id": 88468901206,
                    "join_url": "https://us06web.zoom.us/j/88468901206?pwd=RXZYQlhVbWJKZ1pLWCtpS3l1MHUxZz09",
                    "start_time": "2022-12-27T21:25:00Z",
                    "timezone": "Asia/Jerusalem",
                    "topic": "efe",
                    "type": 8,
                    "uuid": "yHzCvl4USry+C9LnCwdnwQ=="
                },
                {
                    "created_at": "2022-12-28T06:39:48Z",
                    "duration": 60,
                    "host_id": "uJiZN-O7Rp6Jp_995FpZGg",
                    "id": 87525048161,
                    "join_url": "https://us06web.zoom.us/j/87525048161?pwd=ZXlXdXl0QWlLOFVyV3U0OUxxSlBkdz09",
                    "start_time": "2022-12-28T06:39:00Z",
                    "timezone": "Asia/Jerusalem",
                    "topic": "efe",
                    "type": 8,
                    "uuid": "Sblh/I34S1W+rTKUcojJjw=="
                },
                {
                    "created_at": "2022-12-28T06:42:25Z",
                    "duration": 60,
                    "host_id": "uJiZN-O7Rp6Jp_995FpZGg",
                    "id": 83877839723,
                    "join_url": "https://us06web.zoom.us/j/83877839723?pwd=WU9xNmp5RW5KRDhsZ1RySkY4Zkc4Zz09",
                    "start_time": "2022-12-28T06:42:00Z",
                    "timezone": "Asia/Jerusalem",
                    "topic": "efe",
                    "type": 8,
                    "uuid": "iLXDe4HsR6uMb+x8GyybTA=="
                }
            ],
            "next_page_token": "bd4jK0hwZi3c9w9dIYzID8EbUuFEF2X10G2",
            "page_size": 7,
            "total_records": 77
        },
        "Metadata": {
            "Size": 7,
            "Total": 77
        }
    }
}
```

#### Human Readable Output

>### Meeting list
>|uuid|id|host_id|topic|type|start time|duration|timezone|created_at|join_url|
>|---|---|---|---|---|---|---|---|---|---|
>| z93Dc6KjSo20Wr3jx+zaYg== | 83810397585 | uJiZN-O7Rp6Jp_995FpZGg | 2 | 8 |  | 60 | Asia/Jerusalem | 2022-12-04T10:41:27Z | https:<span>//</span>us06web.zoom.us/j/83810397585?pwd=OGFiZjRYNGhwWkVvMWZzdDBoaXlLdz09 |
>| 4kZQ+Hl2RFOAz0VBPHoCYg== | 84540166459 | uJiZN-O7Rp6Jp_995FpZGg | My recurring Meeting -Dima | 8 |  | 60 | Asia/Jerusalem | 2022-12-06T07:59:02Z | https:<span>//</span>us06web.zoom.us/j/84540166459?pwd=ZzdmUEJ5QkZaaUZaaVpFYlBVYnFoUT09 |
>| RABXyk81T02D4hA1rgpDgQ== | 89824497327 | uJiZN-O7Rp6Jp_995FpZGg | efe | 8 |  | 60 | Asia/Jerusalem | 2022-12-27T21:05:41Z | https:<span>//</span>us06web.zoom.us/j/89824497327?pwd=SWpvK0I0L3pQcTNnWlF3b3VDRVhmQT09 |
>| qOXvlLOoSamJjjFaFgniTA== | 83245658341 | uJiZN-O7Rp6Jp_995FpZGg | efe | 8 |  | 60 | Asia/Jerusalem | 2022-12-27T21:11:01Z | https:<span>//</span>us06web.zoom.us/j/83245658341?pwd=SmNGMHI0R1hndnNlRXRDNkZ2Yms3Zz09 |
>| yHzCvl4USry+C9LnCwdnwQ== | 88468901206 | uJiZN-O7Rp6Jp_995FpZGg | efe | 8 |  | 60 | Asia/Jerusalem | 2022-12-27T21:25:54Z | https:<span>//</span>us06web.zoom.us/j/88468901206?pwd=RXZYQlhVbWJKZ1pLWCtpS3l1MHUxZz09 |
>| Sblh/I34S1W+rTKUcojJjw== | 87525048161 | uJiZN-O7Rp6Jp_995FpZGg | efe | 8 |  | 60 | Asia/Jerusalem | 2022-12-28T06:39:48Z | https:<span>//</span>us06web.zoom.us/j/87525048161?pwd=ZXlXdXl0QWlLOFVyV3U0OUxxSlBkdz09 |
>| iLXDe4HsR6uMb+x8GyybTA== | 83877839723 | uJiZN-O7Rp6Jp_995FpZGg | efe | 8 |  | 60 | Asia/Jerusalem | 2022-12-28T06:42:25Z | https:<span>//</span>us06web.zoom.us/j/83877839723?pwd=WU9xNmp5RW5KRDhsZ1RySkY4Zkc4Zz09 |
>
>### Metadata
>|total_records|
>|---|
>| 77 |

