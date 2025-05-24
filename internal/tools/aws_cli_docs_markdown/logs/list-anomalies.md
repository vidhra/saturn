# list-anomaliesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/list-anomalies.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/list-anomalies.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [logs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/index.html#cli-aws-logs) ]

# list-anomalies

## Description

Returns a list of anomalies that log anomaly detectors have found. For details about the structure format of each anomaly object that is returned, see the example in this section.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/ListAnomalies)

`list-anomalies` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `anomalies`

## Synopsis

```
list-anomalies
[--anomaly-detector-arn <value>]
[--suppression-state <value>]
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

`--anomaly-detector-arn` (string)

Use this to optionally limit the results to only the anomalies found by a certain anomaly detector.

`--suppression-state` (string)

You can specify this parameter if you want to the operation to return only anomalies that are currently either suppressed or unsuppressed.

Possible values:

- `SUPPRESSED`
- `UNSUPPRESSED`

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

anomalies -> (list)

An array of structures, where each structure contains information about one anomaly that a log anomaly detector has found.

(structure)

This structure represents one anomaly that has been found by a logs anomaly detector.

For more information about patterns and anomalies, see [CreateLogAnomalyDetector](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogAnomalyDetector.html) .

anomalyId -> (string)

The unique ID that CloudWatch Logs assigned to this anomaly.

patternId -> (string)

The ID of the pattern used to help identify this anomaly.

anomalyDetectorArn -> (string)

The ARN of the anomaly detector that identified this anomaly.

patternString -> (string)

The pattern used to help identify this anomaly, in string format.

patternRegex -> (string)

The pattern used to help identify this anomaly, in regular expression format.

priority -> (string)

The priority level of this anomaly, as determined by CloudWatch Logs. Priority is computed based on log severity labels such as `FATAL` and `ERROR` and the amount of deviation from the baseline. Possible values are `HIGH` , `MEDIUM` , and `LOW` .

firstSeen -> (long)

The date and time when the anomaly detector first saw this anomaly. It is specified as epoch time, which is the number of seconds since `January 1, 1970, 00:00:00 UTC` .

lastSeen -> (long)

The date and time when the anomaly detector most recently saw this anomaly. It is specified as epoch time, which is the number of seconds since `January 1, 1970, 00:00:00 UTC` .

description -> (string)

A human-readable description of the anomaly. This description is generated by CloudWatch Logs.

active -> (boolean)

Specifies whether this anomaly is still ongoing.

state -> (string)

Indicates the current state of this anomaly. If it is still being treated as an anomaly, the value is `Active` . If you have suppressed this anomaly by using the [UpdateAnomaly](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateAnomaly.html) operation, the value is `Suppressed` . If this behavior is now considered to be normal, the value is `Baseline` .

histogram -> (map)

A map showing times when the anomaly detector ran, and the number of occurrences of this anomaly that were detected at each of those runs. The times are specified in epoch time, which is the number of seconds since `January 1, 1970, 00:00:00 UTC` .

key -> (string)

value -> (long)

logSamples -> (list)

An array of sample log event messages that are considered to be part of this anomaly.

(structure)

This structure contains the information for one sample log event that is associated with an anomaly found by a log anomaly detector.

timestamp -> (long)

The time stamp of the log event.

message -> (string)

The message content of the log event.

patternTokens -> (list)

An array of structures where each structure contains information about one token that makes up the pattern.

(structure)

A structure that contains information about one pattern token related to an anomaly.

For more information about patterns and tokens, see [CreateLogAnomalyDetector](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogAnomalyDetector.html) .

dynamicTokenPosition -> (integer)

For a dynamic token, this indicates where in the pattern that this token appears, related to other dynamic tokens. The dynamic token that appears first has a value of `1` , the one that appears second is `2` , and so on.

isDynamic -> (boolean)

Specifies whether this is a dynamic token.

tokenString -> (string)

The string represented by this token. If this is a dynamic token, the value will be `<*>`

enumerations -> (map)

Contains the values found for a dynamic token, and the number of times each value was found.

key -> (string)

value -> (long)

inferredTokenName -> (string)

A name that CloudWatch Logs assigned to this dynamic token to make the pattern more readable. The string part of the `inferredTokenName` gives you a clearer idea of the content of this token. The number part of the `inferredTokenName` shows where in the pattern this token appears, compared to other dynamic tokens. CloudWatch Logs assigns the string part of the name based on analyzing the content of the log events that contain it.

For example, an inferred token name of `IPAddress-3` means that the token represents an IP address, and this token is the third dynamic token in the pattern.

logGroupArnList -> (list)

An array of ARNS of the log groups that contained log events considered to be part of this anomaly.

(string)

suppressed -> (boolean)

Indicates whether this anomaly is currently suppressed. To suppress an anomaly, use [UpdateAnomaly](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateAnomaly.html) .

suppressedDate -> (long)

If the anomaly is suppressed, this indicates when it was suppressed.

suppressedUntil -> (long)

If the anomaly is suppressed, this indicates when the suppression will end. If this value is `0` , the anomaly was suppressed with no expiration, with the `INFINITE` value.

isPatternLevelSuppression -> (boolean)

If this anomaly is suppressed, this field is `true` if the suppression is because the pattern is suppressed. If `false` , then only this particular anomaly is suppressed.

nextToken -> (string)

The token for the next set of items to return. The token expires after 24 hours.