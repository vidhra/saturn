# get-insight-selectorsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-insight-selectors.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-insight-selectors.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudtrail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/index.html#cli-aws-cloudtrail) ]

# get-insight-selectors

## Description

Describes the settings for the Insights event selectors that you configured for your trail or event data store. `GetInsightSelectors` shows if CloudTrail Insights event logging is enabled on the trail or event data store, and if it is, which Insights types are enabled. If you run `GetInsightSelectors` on a trail or event data store that does not have Insights events enabled, the operation throws the exception `InsightNotEnabledException`

Specify either the `EventDataStore` parameter to get Insights event selectors for an event data store, or the `TrailName` parameter to the get Insights event selectors for a trail. You cannot specify these parameters together.

For more information, see [Working with CloudTrail Insights](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.html) in the *CloudTrail User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/GetInsightSelectors)

## Synopsis

```
get-insight-selectors
[--trail-name <value>]
[--event-data-store <value>]
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

`--trail-name` (string)

Specifies the name of the trail or trail ARN. If you specify a trail name, the string must meet the following requirements:

- Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)
- Start with a letter or number, and end with a letter or number
- Be between 3 and 128 characters
- Have no adjacent periods, underscores or dashes. Names like `my-_namespace` and `my--namespace` are not valid.
- Not be in IP address format (for example, 192.168.5.4)

If you specify a trail ARN, it must be in the format:

`arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`

You cannot use this parameter with the `EventDataStore` parameter.

`--event-data-store` (string)

Specifies the ARN (or ID suffix of the ARN) of the event data store for which you want to get Insights selectors.

You cannot use this parameter with the `TrailName` parameter.

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

TrailARN -> (string)

The Amazon Resource Name (ARN) of a trail for which you want to get Insights selectors.

InsightSelectors -> (list)

A JSON string that contains the Insight types you want to log on a trail or event data store. `ApiErrorRateInsight` and `ApiCallRateInsight` are supported as Insights types.

(structure)

A JSON string that contains a list of Insights types that are logged on a trail or event data store.

InsightType -> (string)

The type of Insights events to log on a trail or event data store. `ApiCallRateInsight` and `ApiErrorRateInsight` are valid Insight types.

The `ApiCallRateInsight` Insights type analyzes write-only management API calls that are aggregated per minute against a baseline API call volume.

The `ApiErrorRateInsight` Insights type analyzes management API calls that result in error codes. The error is shown if the API call is unsuccessful.

EventDataStoreArn -> (string)

The ARN of the source event data store that enabled Insights events.

InsightsDestination -> (string)

The ARN of the destination event data store that logs Insights events.