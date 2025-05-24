# list-crawlsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-crawls.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-crawls.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# list-crawls

## Description

Returns all the crawls of a specified crawler. Returns only the crawls that have occurred since the launch date of the crawler history feature, and only retains up to 12 months of crawls. Older crawls will not be returned.

You may use this API to:

- Retrive all the crawls of a specified crawler.
- Retrieve all the crawls of a specified crawler within a limited count.
- Retrieve all the crawls of a specified crawler in a specific time range.
- Retrieve all the crawls of a specified crawler with a particular state, crawl ID, or DPU hour value.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/ListCrawls)

## Synopsis

```
list-crawls
--crawler-name <value>
[--max-results <value>]
[--filters <value>]
[--next-token <value>]
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

`--crawler-name` (string)

The name of the crawler whose runs you want to retrieve.

`--max-results` (integer)

The maximum number of results to return. The default is 20, and maximum is 100.

`--filters` (list)

Filters the crawls by the criteria you specify in a list of `CrawlsFilter` objects.

(structure)

A list of fields, comparators and value that you can use to filter the crawler runs for a specified crawler.

FieldName -> (string)

A key used to filter the crawler runs for a specified crawler. Valid values for each of the field names are:

- `CRAWL_ID` : A string representing the UUID identifier for a crawl.
- `STATE` : A string representing the state of the crawl.
- `START_TIME` and `END_TIME` : The epoch timestamp in milliseconds.
- `DPU_HOUR` : The number of data processing unit (DPU) hours used for the crawl.

FilterOperator -> (string)

A defined comparator that operates on the value. The available operators are:

- `GT` : Greater than.
- `GE` : Greater than or equal to.
- `LT` : Less than.
- `LE` : Less than or equal to.
- `EQ` : Equal to.
- `NE` : Not equal to.

FieldValue -> (string)

The value provided for comparison on the crawl field.

Shorthand Syntax:

```
FieldName=string,FilterOperator=string,FieldValue=string ...
```

JSON Syntax:

```
[
  {
    "FieldName": "CRAWL_ID"|"STATE"|"START_TIME"|"END_TIME"|"DPU_HOUR",
    "FilterOperator": "GT"|"GE"|"LT"|"LE"|"EQ"|"NE",
    "FieldValue": "string"
  }
  ...
]
```

`--next-token` (string)

A continuation token, if this is a continuation call.

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

Crawls -> (list)

A list of `CrawlerHistory` objects representing the crawl runs that meet your criteria.

(structure)

Contains the information for a run of a crawler.

CrawlId -> (string)

A UUID identifier for each crawl.

State -> (string)

The state of the crawl.

StartTime -> (timestamp)

The date and time on which the crawl started.

EndTime -> (timestamp)

The date and time on which the crawl ended.

Summary -> (string)

A run summary for the specific crawl in JSON. Contains the catalog tables and partitions that were added, updated, or deleted.

ErrorMessage -> (string)

If an error occurred, the error message associated with the crawl.

LogGroup -> (string)

The log group associated with the crawl.

LogStream -> (string)

The log stream associated with the crawl.

MessagePrefix -> (string)

The prefix for a CloudWatch message about this crawl.

DPUHour -> (double)

The number of data processing units (DPU) used in hours for the crawl.

NextToken -> (string)

A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.