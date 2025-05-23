# search-tasksÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/search-tasks.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/search-tasks.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [deadline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/index.html#cli-aws-deadline) ]

# search-tasks

## Description

Searches for tasks.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/deadline-2023-10-12/SearchTasks)

## Synopsis

```
search-tasks
--farm-id <value>
--queue-ids <value>
[--job-id <value>]
[--filter-expressions <value>]
[--sort-expressions <value>]
--item-offset <value>
[--page-size <value>]
[--cli-input-json | --cli-input-yaml]
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

`--farm-id` (string)

The farm ID of the task.

`--queue-ids` (list)

The queue IDs to include in the search.

(string)

Syntax:

```
"string" "string" ...
```

`--job-id` (string)

The job ID for the task search.

`--filter-expressions` (structure)

The filter expression, `AND` or `OR` , to use when searching among a group of search strings in a resource. You can use two groupings per search each within parenthesis `()` .

filters -> (list)

The filters to use for the search.

(tagged union structure)

The type of search filter to apply.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `dateTimeFilter`, `parameterFilter`, `searchTermFilter`, `stringFilter`, `groupFilter`.

dateTimeFilter -> (structure)

Filters based on date and time.

name -> (string)

The name of the date-time field to filter on.

operator -> (string)

The type of comparison to use to filter the results.

dateTime -> (timestamp)

The date and time.

parameterFilter -> (structure)

Filters by parameter.

name -> (string)

The name of the parameter to filter on.

operator -> (string)

The type of comparison to use to filter results.

value -> (string)

The parameterâs value.

searchTermFilter -> (structure)

Filters by a specified search term.

searchTerm -> (string)

The term to search for.

matchType -> (string)

Specifies how Deadline Cloud matches your search term in the results. If you donât specify a `matchType` the default is `FUZZY_MATCH` .

- `FUZZY_MATCH` - Matches if a portion of the search term is found in the result.
- `CONTAINS` - Matches if the exact search term is contained in the result.

stringFilter -> (structure)

Filters by a string.

name -> (string)

The field name to search.

operator -> (string)

The type of comparison to use for this search.

value -> (string)

The string to search for.

groupFilter -> (structure)

Filters by group.

filters -> (list)

The filters to use for the search.

(tagged union structure)

The type of search filter to apply.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `dateTimeFilter`, `parameterFilter`, `searchTermFilter`, `stringFilter`, `groupFilter`.

dateTimeFilter -> (structure)

Filters based on date and time.

name -> (string)

The name of the date-time field to filter on.

operator -> (string)

The type of comparison to use to filter the results.

dateTime -> (timestamp)

The date and time.

parameterFilter -> (structure)

Filters by parameter.

name -> (string)

The name of the parameter to filter on.

operator -> (string)

The type of comparison to use to filter results.

value -> (string)

The parameterâs value.

searchTermFilter -> (structure)

Filters by a specified search term.

searchTerm -> (string)

The term to search for.

matchType -> (string)

Specifies how Deadline Cloud matches your search term in the results. If you donât specify a `matchType` the default is `FUZZY_MATCH` .

- `FUZZY_MATCH` - Matches if a portion of the search term is found in the result.
- `CONTAINS` - Matches if the exact search term is contained in the result.

stringFilter -> (structure)

Filters by a string.

name -> (string)

The field name to search.

operator -> (string)

The type of comparison to use for this search.

value -> (string)

The string to search for.

( â¦ recursive â¦ )

operator -> (string)

The operators to include in the search.

operator -> (string)

The operators to include in the search.

JSON Syntax:

```
{
  "filters": [
    {
      "dateTimeFilter": {
        "name": "string",
        "operator": "EQUAL"|"NOT_EQUAL"|"GREATER_THAN_EQUAL_TO"|"GREATER_THAN"|"LESS_THAN_EQUAL_TO"|"LESS_THAN",
        "dateTime": timestamp
      },
      "parameterFilter": {
        "name": "string",
        "operator": "EQUAL"|"NOT_EQUAL"|"GREATER_THAN_EQUAL_TO"|"GREATER_THAN"|"LESS_THAN_EQUAL_TO"|"LESS_THAN",
        "value": "string"
      },
      "searchTermFilter": {
        "searchTerm": "string",
        "matchType": "FUZZY_MATCH"|"CONTAINS"
      },
      "stringFilter": {
        "name": "string",
        "operator": "EQUAL"|"NOT_EQUAL"|"GREATER_THAN_EQUAL_TO"|"GREATER_THAN"|"LESS_THAN_EQUAL_TO"|"LESS_THAN",
        "value": "string"
      },
      "groupFilter": {
        "filters": [
          {
            "dateTimeFilter": {
              "name": "string",
              "operator": "EQUAL"|"NOT_EQUAL"|"GREATER_THAN_EQUAL_TO"|"GREATER_THAN"|"LESS_THAN_EQUAL_TO"|"LESS_THAN",
              "dateTime": timestamp
            },
            "parameterFilter": {
              "name": "string",
              "operator": "EQUAL"|"NOT_EQUAL"|"GREATER_THAN_EQUAL_TO"|"GREATER_THAN"|"LESS_THAN_EQUAL_TO"|"LESS_THAN",
              "value": "string"
            },
            "searchTermFilter": {
              "searchTerm": "string",
              "matchType": "FUZZY_MATCH"|"CONTAINS"
            },
            "stringFilter": {
              "name": "string",
              "operator": "EQUAL"|"NOT_EQUAL"|"GREATER_THAN_EQUAL_TO"|"GREATER_THAN"|"LESS_THAN_EQUAL_TO"|"LESS_THAN",
              "value": "string"
            },
            "groupFilter": { ... recursive ... }
          }
          ...
        ],
        "operator": "AND"|"OR"
      }
    }
    ...
  ],
  "operator": "AND"|"OR"
}
```

`--sort-expressions` (list)

The search terms for a resource.

(tagged union structure)

The resources to search.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `userJobsFirst`, `fieldSort`, `parameterSort`.

userJobsFirst -> (structure)

Options for sorting a particular userâs jobs first.

userIdentityId -> (string)

The userâs ID.

fieldSort -> (structure)

Options for sorting by a field.

sortOrder -> (string)

The sort order for the field.

name -> (string)

The name of the field.

parameterSort -> (structure)

Options for sorting by a parameter.

sortOrder -> (string)

The sort order for the parameter.

name -> (string)

The parameter name to sort by.

Shorthand Syntax:

```
userJobsFirst={userIdentityId=string},fieldSort={sortOrder=string,name=string},parameterSort={sortOrder=string,name=string} ...
```

JSON Syntax:

```
[
  {
    "userJobsFirst": {
      "userIdentityId": "string"
    },
    "fieldSort": {
      "sortOrder": "ASCENDING"|"DESCENDING",
      "name": "string"
    },
    "parameterSort": {
      "sortOrder": "ASCENDING"|"DESCENDING",
      "name": "string"
    }
  }
  ...
]
```

`--item-offset` (integer)

Defines how far into the scrollable list to start the return of results.

`--page-size` (integer)

Specifies the number of items per page for the resource.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

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

tasks -> (list)

Tasks in the search.

(structure)

The details of a task search.

taskId -> (string)

The task ID.

stepId -> (string)

The step ID.

jobId -> (string)

The job ID.

queueId -> (string)

The queue ID.

runStatus -> (string)

The run status of the task.

targetRunStatus -> (string)

The run status that the task is being updated to.

parameters -> (map)

The parameters to search for.

key -> (string)

value -> (tagged union structure)

The data types for the task parameters.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `int`, `float`, `string`, `path`.

int -> (string)

A signed integer represented as a string.

float -> (string)

A double precision IEEE-754 floating point number represented as a string.

string -> (string)

A UTF-8 string.

path -> (string)

A file system path represented as a string.

failureRetryCount -> (integer)

The number of times that the task failed and was retried.

startedAt -> (timestamp)

The date and time the resource started running.

endedAt -> (timestamp)

The date and time the resource ended running.

nextItemOffset -> (integer)

The next incremental starting point after the defined `itemOffset` .

totalResults -> (integer)

The total number of results in the search.