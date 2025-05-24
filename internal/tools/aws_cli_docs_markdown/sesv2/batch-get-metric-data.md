# batch-get-metric-dataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/batch-get-metric-data.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/batch-get-metric-data.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sesv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/index.html#cli-aws-sesv2) ]

# batch-get-metric-data

## Description

Retrieves batches of metric data collected based on your sending activity.

You can execute this operation no more than 16 times per second, and with at most 160 queries from the batches per second (cumulative).

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sesv2-2019-09-27/BatchGetMetricData)

## Synopsis

```
batch-get-metric-data
--queries <value>
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

`--queries` (list)

A list of queries for metrics to be retrieved.

(structure)

Represents a single metric data query to include in a batch.

Id -> (string)

The query identifier.

Namespace -> (string)

The query namespace - e.g. `VDM`

Metric -> (string)

The queried metric. This can be one of the following:

- `SEND` â Emails sent eligible for tracking in the VDM dashboard. This excludes emails sent to the mailbox simulator and emails addressed to more than one recipient.
- `COMPLAINT` â Complaints received for your account. This excludes complaints from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those for emails addressed to more than one recipient
- `PERMANENT_BOUNCE` â Permanent bounces - i.e. feedback received for emails sent to non-existent mailboxes. Excludes bounces from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those for emails addressed to more than one recipient.
- `TRANSIENT_BOUNCE` â Transient bounces - i.e. feedback received for delivery failures excluding issues with non-existent mailboxes. Excludes bounces from the mailbox simulator, and those for emails addressed to more than one recipient.
- `OPEN` â Unique open events for emails including open trackers. Excludes opens for emails addressed to more than one recipient.
- `CLICK` â Unique click events for emails including wrapped links. Excludes clicks for emails addressed to more than one recipient.
- `DELIVERY` â Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator and for emails addressed to more than one recipient.
- `DELIVERY_OPEN` â Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator, for emails addressed to more than one recipient, and emails without open trackers.
- `DELIVERY_CLICK` â Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator, for emails addressed to more than one recipient, and emails without click trackers.
- `DELIVERY_COMPLAINT` â Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator, for emails addressed to more than one recipient, and emails addressed to recipients hosted by ISPs with which Amazon SES does not have a feedback loop agreement.

Dimensions -> (map)

An object that contains mapping between `MetricDimensionName` and `MetricDimensionValue` to filter metrics by.

key -> (string)

The `BatchGetMetricDataQuery` dimension name. This can be one of the following:

- `EMAIL_IDENTITY` â The email identity used when sending messages.
- `CONFIGURATION_SET` â The configuration set used when sending messages (if one was used).
- `ISP` â The recipient ISP (e.g. `Gmail` , `Yahoo` , etc.).

value -> (string)

A list of values associated with the `MetricDimensionName` to filter metrics by. Can either be `*` as a wildcard for all values or a list of up to 10 specific values. If one `Dimension` has the `*` value, other dimensions can only contain one value.

StartDate -> (timestamp)

Represents the start date for the query interval.

EndDate -> (timestamp)

Represents the end date for the query interval.

Shorthand Syntax:

```
Id=string,Namespace=string,Metric=string,Dimensions={KeyName1=string,KeyName2=string},StartDate=timestamp,EndDate=timestamp ...
```

JSON Syntax:

```
[
  {
    "Id": "string",
    "Namespace": "VDM",
    "Metric": "SEND"|"COMPLAINT"|"PERMANENT_BOUNCE"|"TRANSIENT_BOUNCE"|"OPEN"|"CLICK"|"DELIVERY"|"DELIVERY_OPEN"|"DELIVERY_CLICK"|"DELIVERY_COMPLAINT",
    "Dimensions": {"EMAIL_IDENTITY"|"CONFIGURATION_SET"|"ISP": "string"
      ...},
    "StartDate": timestamp,
    "EndDate": timestamp
  }
  ...
]
```

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

Results -> (list)

A list of successfully retrieved `MetricDataResult` .

(structure)

The result of a single metric data query.

Id -> (string)

The query identifier.

Timestamps -> (list)

A list of timestamps for the metric data results.

(timestamp)

Values -> (list)

A list of values (cumulative / sum) for the metric data results.

(long)

Errors -> (list)

A list of `MetricDataError` encountered while processing your metric data batch request.

(structure)

An error corresponding to the unsuccessful processing of a single metric data query.

Id -> (string)

The query identifier.

Code -> (string)

The query error code. Can be one of:

- `INTERNAL_FAILURE` â Amazon SES has failed to process one of the queries.
- `ACCESS_DENIED` â You have insufficient access to retrieve metrics based on the given query.

Message -> (string)

The error message associated with the current query error.