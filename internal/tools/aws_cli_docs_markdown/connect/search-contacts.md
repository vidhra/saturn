# search-contactsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/search-contacts.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/search-contacts.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# search-contacts

## Description

Searches contacts in an Amazon Connect instance.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/SearchContacts)

`search-contacts` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Contacts`

## Synopsis

```
search-contacts
--instance-id <value>
--time-range <value>
[--search-criteria <value>]
[--sort <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
[--generate-cli-skeleton <value>]
[--debug]
[--endpoint-url <value>]
[--no-verify-ssl]
[--no-paginate]
[--output <value>]
[--query <value>]
[--profile <value>]
[--region <value>]
[--version <value>]
[--color <value>]
[--no-sign-request]
[--ca-bundle <value>]
[--cli-read-timeout <value>]
[--cli-connect-timeout <value>]
[--cli-binary-format <value>]
[--no-cli-pager]
[--cli-auto-prompt]
[--no-cli-auto-prompt]
```

## Options

`--instance-id` (string)

The identifier of Amazon Connect instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance.

`--time-range` (structure)

Time range that you want to search results.

Type -> (string)

The type of timestamp to search.

StartTime -> (timestamp)

The start time of the time range.

EndTime -> (timestamp)

The end time of the time range.

Shorthand Syntax:

```
Type=string,StartTime=timestamp,EndTime=timestamp
```

JSON Syntax:

```
{
  "Type": "INITIATION_TIMESTAMP"|"SCHEDULED_TIMESTAMP"|"CONNECTED_TO_AGENT_TIMESTAMP"|"DISCONNECT_TIMESTAMP",
  "StartTime": timestamp,
  "EndTime": timestamp
}
```

`--search-criteria` (structure)

The search criteria to be used to return contacts.

AgentIds -> (list)

The identifiers of agents who handled the contacts.

(string)

AgentHierarchyGroups -> (structure)

The agent hierarchy groups of the agent at the time of handling the contact.

L1Ids -> (list)

The identifiers for level 1 hierarchy groups.

(string)

L2Ids -> (list)

The identifiers for level 2 hierarchy groups.

(string)

L3Ids -> (list)

The identifiers for level 3 hierarchy groups.

(string)

L4Ids -> (list)

The identifiers for level 4 hierarchy groups.

(string)

L5Ids -> (list)

The identifiers for level 5 hierarchy groups.

(string)

Channels -> (list)

The list of channels associated with contacts.

(string)

ContactAnalysis -> (structure)

Search criteria based on analysis outputs from Amazon Connect Contact Lens.

Transcript -> (structure)

Search criteria based on transcript analyzed by Amazon Connect Contact Lens.

Criteria -> (list)

The list of search criteria based on Contact Lens conversational analytics transcript.

(structure)

A structure that defines search criteria base on words or phrases, participants in the Contact Lens conversational analytics transcript.

ParticipantRole -> (string)

The participant role in a transcript

SearchText -> (list)

The words or phrases used to search within a transcript.

(string)

MatchType -> (string)

The match type combining search criteria using multiple search texts in a transcript criteria.

MatchType -> (string)

The match type combining search criteria using multiple transcript criteria.

InitiationMethods -> (list)

The list of initiation methods associated with contacts.

(string)

QueueIds -> (list)

The list of queue IDs associated with contacts.

(string)

SearchableContactAttributes -> (structure)

The search criteria based on user-defined contact attributes that have been configured for contact search. For more information, see [Search by custom contact attributes](https://docs.aws.amazon.com/connect/latest/adminguide/search-custom-attributes.html) in the *Amazon Connect Administrator Guide* .

### Warning

To use `SearchableContactAttributes` in a search request, the `GetContactAttributes` action is required to perform an API request. For more information, see [https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonconnect.html#amazonconnect-actions-as-permissions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonconnect.html#amazonconnect-actions-as-permissions) Actions defined by Amazon Connect.

Criteria -> (list)

The list of criteria based on user-defined contact attributes that are configured for contact search.

(structure)

The search criteria based on user-defined contact attribute key and values to search on.

Key -> (string)

The key containing a searchable user-defined contact attribute.

Values -> (list)

The list of values to search for within a user-defined contact attribute.

(string)

MatchType -> (string)

The match type combining search criteria using multiple searchable contact attributes.

SearchableSegmentAttributes -> (structure)

The search criteria based on searchable segment attributes of a contact.

Criteria -> (list)

The list of criteria based on searchable segment attributes.

(structure)

The search criteria based on searchable segment attribute key and values to search on.

Key -> (string)

The key containing a searchable segment attribute.

Values -> (list)

The list of values to search for within a searchable segment attribute.

(string)

MatchType -> (string)

The match type combining search criteria using multiple searchable segment attributes.

JSON Syntax:

```
{
  "AgentIds": ["string", ...],
  "AgentHierarchyGroups": {
    "L1Ids": ["string", ...],
    "L2Ids": ["string", ...],
    "L3Ids": ["string", ...],
    "L4Ids": ["string", ...],
    "L5Ids": ["string", ...]
  },
  "Channels": ["VOICE"|"CHAT"|"TASK"|"EMAIL", ...],
  "ContactAnalysis": {
    "Transcript": {
      "Criteria": [
        {
          "ParticipantRole": "AGENT"|"CUSTOMER"|"SYSTEM"|"CUSTOM_BOT"|"SUPERVISOR",
          "SearchText": ["string", ...],
          "MatchType": "MATCH_ALL"|"MATCH_ANY"
        }
        ...
      ],
      "MatchType": "MATCH_ALL"|"MATCH_ANY"
    }
  },
  "InitiationMethods": ["INBOUND"|"OUTBOUND"|"TRANSFER"|"QUEUE_TRANSFER"|"CALLBACK"|"API"|"DISCONNECT"|"MONITOR"|"EXTERNAL_OUTBOUND"|"WEBRTC_API"|"AGENT_REPLY"|"FLOW", ...],
  "QueueIds": ["string", ...],
  "SearchableContactAttributes": {
    "Criteria": [
      {
        "Key": "string",
        "Values": ["string", ...]
      }
      ...
    ],
    "MatchType": "MATCH_ALL"|"MATCH_ANY"
  },
  "SearchableSegmentAttributes": {
    "Criteria": [
      {
        "Key": "string",
        "Values": ["string", ...]
      }
      ...
    ],
    "MatchType": "MATCH_ALL"|"MATCH_ANY"
  }
}
```

`--sort` (structure)

Specifies a field to sort by and a sort order.

FieldName -> (string)

The name of the field on which to sort.

Order -> (string)

An ascending or descending sort.

Shorthand Syntax:

```
FieldName=string,Order=string
```

JSON Syntax:

```
{
  "FieldName": "INITIATION_TIMESTAMP"|"SCHEDULED_TIMESTAMP"|"CONNECTED_TO_AGENT_TIMESTAMP"|"DISCONNECT_TIMESTAMP"|"INITIATION_METHOD"|"CHANNEL",
  "Order": "ASCENDING"|"DESCENDING"
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--generate-cli-skeleton` (string)
Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value `input`, prints a sample input JSON that can be used as an argument for `--cli-input-json`. Similarly, if provided `yaml-input` it will print a sample input YAML that can be used with `--cli-input-yaml`. If provided with the value `output`, it validates the command inputs and returns a sample output JSON for that command. The generated JSON skeleton is not stable between versions of the AWS CLI and there are no backwards compatibility guarantees in the JSON skeleton generated.

## Global Options

`--debug` (boolean)

Turn on debug logging.

`--endpoint-url` (string)

Override commandâs default URL with the given URL.

`--no-verify-ssl` (boolean)

By default, the AWS CLI uses SSL when communicating with AWS services. For each SSL connection, the AWS CLI will verify SSL certificates. This option overrides the default behavior of verifying SSL certificates.

`--no-paginate` (boolean)

Disable automatic pagination. If automatic pagination is disabled, the AWS CLI will only make one call, for the first page of results.

`--output` (string)

The formatting style for command output.

- json
- text
- table
- yaml
- yaml-stream

`--query` (string)

A JMESPath query to use in filtering the response data.

`--profile` (string)

Use a specific profile from your credential file.

`--region` (string)

The region to use. Overrides config/env settings.

`--version` (string)

Display the version of this tool.

`--color` (string)

Turn on/off color output.

- on
- off
- auto

`--no-sign-request` (boolean)

Do not sign requests. Credentials will not be loaded if this argument is provided.

`--ca-bundle` (string)

The CA certificate bundle to use when verifying SSL certificates. Overrides config/env settings.

`--cli-read-timeout` (int)

The maximum socket read time in seconds. If the value is set to 0, the socket read will be blocking and not timeout. The default value is 60 seconds.

`--cli-connect-timeout` (int)

The maximum socket connect time in seconds. If the value is set to 0, the socket connect will be blocking and not timeout. The default value is 60 seconds.

`--cli-binary-format` (string)

The formatting style to be used for binary blobs. The default format is base64. The base64 format expects binary blobs to be provided as a base64 encoded string. The raw-in-base64-out format preserves compatibility with AWS CLI V1 behavior and binary values must be passed literally. When providing contents from a file that map to a binary blob `fileb://` will always be treated as binary and use the file contents directly regardless of the `cli-binary-format` setting. When using `file://` the file contents will need to properly formatted for the configured `cli-binary-format`.

- base64
- raw-in-base64-out

`--no-cli-pager` (boolean)

Disable cli pager for output.

`--cli-auto-prompt` (boolean)

Automatically prompt for CLI input parameters.

`--no-cli-auto-prompt` (boolean)

Disable automatically prompt for CLI input parameters.

## Output

Contacts -> (list)

Information about the contacts.

(structure)

Information of returned contact.

Arn -> (string)

The Amazon Resource Name (ARN) of the contact.

Id -> (string)

The identifier of the contact summary.

InitialContactId -> (string)

If this contact is related to other contacts, this is the ID of the initial contact.

PreviousContactId -> (string)

If this contact is not the first contact, this is the ID of the previous contact.

InitiationMethod -> (string)

Indicates how the contact was initiated.

Channel -> (string)

How the contact reached your contact center.

QueueInfo -> (structure)

If this contact was queued, this contains information about the queue.

Id -> (string)

The unique identifier for the queue.

EnqueueTimestamp -> (timestamp)

The timestamp when the contact was added to the queue.

AgentInfo -> (structure)

Information about the agent who accepted the contact.

Id -> (string)

The identifier of the agent who accepted the contact.

ConnectedToAgentTimestamp -> (timestamp)

The timestamp when the contact was connected to the agent.

InitiationTimestamp -> (timestamp)

The date and time this contact was initiated, in UTC time. For `INBOUND` , this is when the contact arrived. For `OUTBOUND` , this is when the agent began dialing. For `CALLBACK` , this is when the callback contact was created. For `TRANSFER` and `QUEUE_TRANSFER` , this is when the transfer was initiated. For API, this is when the request arrived. For `EXTERNAL_OUTBOUND` , this is when the agent started dialing the external participant. For `MONITOR` , this is when the supervisor started listening to a contact.

DisconnectTimestamp -> (timestamp)

The timestamp when the customer endpoint disconnected from Amazon Connect.

ScheduledTimestamp -> (timestamp)

The timestamp, in Unix epoch time format, at which to start running the inbound flow.

SegmentAttributes -> (map)

Set of segment attributes for a contact.

key -> (string)

value -> (structure)

The value of a segment attribute. This is structured as a map with a single key-value pair. The key âvalueStringâ indicates that the attribute type is a string, and its corresponding value is the actual string value of the segment attribute.

ValueString -> (string)

The value of a segment attribute represented as a string.

NextToken -> (string)

If there are additional results, this is the token for the next set of results.

TotalCount -> (long)

The total number of contacts which matched your search query.