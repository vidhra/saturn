# start-service-software-updateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/start-service-software-update.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/start-service-software-update.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opensearch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/index.html#cli-aws-opensearch) ]

# start-service-software-update

## Description

Schedules a service software update for an Amazon OpenSearch Service domain. For more information, see [Service software updates in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opensearch-2021-01-01/StartServiceSoftwareUpdate)

## Synopsis

```
start-service-software-update
--domain-name <value>
[--schedule-at <value>]
[--desired-start-time <value>]
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

`--domain-name` (string)

The name of the domain that you want to update to the latest service software.

`--schedule-at` (string)

When to start the service software update.

- `NOW` - Immediately schedules the update to happen in the current hour if thereâs capacity available.
- `TIMESTAMP` - Lets you specify a custom date and time to apply the update. If you specify this value, you must also provide a value for `DesiredStartTime` .
- `OFF_PEAK_WINDOW` - Marks the update to be picked up during an upcoming off-peak window. Thereâs no guarantee that the update will happen during the next immediate window. Depending on capacity, it might happen in subsequent days.

Default: `NOW` if you donât specify a value for `DesiredStartTime` , and `TIMESTAMP` if you do.

Possible values:

- `NOW`
- `TIMESTAMP`
- `OFF_PEAK_WINDOW`

`--desired-start-time` (long)

The Epoch timestamp when you want the service software update to start. You only need to specify this parameter if you set `ScheduleAt` to `TIMESTAMP` .

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

ServiceSoftwareOptions -> (structure)

The current status of the OpenSearch Service software update.

CurrentVersion -> (string)

The current service software version present on the domain.

NewVersion -> (string)

The new service software version, if one is available.

UpdateAvailable -> (boolean)

True if youâre able to update your service software version. False if you canât update your service software version.

Cancellable -> (boolean)

True if youâre able to cancel your service software version update. False if you canât cancel your service software update.

UpdateStatus -> (string)

The status of your service software update.

Description -> (string)

A description of the service software update status.

AutomatedUpdateDate -> (timestamp)

The timestamp, in Epoch time, until which you can manually request a service software update. After this date, we automatically update your service software.

OptionalDeployment -> (boolean)

True if a service software is never automatically updated. False if a service software is automatically updated after the automated update date.