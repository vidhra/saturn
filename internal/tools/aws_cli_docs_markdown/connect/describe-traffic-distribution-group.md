# describe-traffic-distribution-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-traffic-distribution-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-traffic-distribution-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# describe-traffic-distribution-group

## Description

Gets details and status of a traffic distribution group.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/DescribeTrafficDistributionGroup)

## Synopsis

```
describe-traffic-distribution-group
--traffic-distribution-group-id <value>
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

`--traffic-distribution-group-id` (string)

The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region.

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

TrafficDistributionGroup -> (structure)

Information about the traffic distribution group.

Id -> (string)

The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region.

Arn -> (string)

The Amazon Resource Name (ARN) of the traffic distribution group.

Name -> (string)

The name of the traffic distribution group.

Description -> (string)

The description of the traffic distribution group.

InstanceArn -> (string)

The Amazon Resource Name (ARN).

Status -> (string)

The status of the traffic distribution group.

- `CREATION_IN_PROGRESS` means the previous [CreateTrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateTrafficDistributionGroup.html) operation is still in progress and has not yet completed.
- `ACTIVE` means the previous [CreateTrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateTrafficDistributionGroup.html) operation has succeeded.
- `CREATION_FAILED` indicates that the previous [CreateTrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateTrafficDistributionGroup.html) operation has failed.
- `PENDING_DELETION` means the previous [DeleteTrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteTrafficDistributionGroup.html) operation is still in progress and has not yet completed.
- `DELETION_FAILED` means the previous [DeleteTrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteTrafficDistributionGroup.html) operation has failed.
- `UPDATE_IN_PROGRESS` means the previous [UpdateTrafficDistribution](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateTrafficDistribution.html) operation is still in progress and has not yet completed.

Tags -> (map)

The tags used to organize, track, or control access for this resource. For example, { âTagsâ: {âkey1â:âvalue1â, âkey2â:âvalue2â} }.

key -> (string)

value -> (string)

IsDefault -> (boolean)

Whether this is the default traffic distribution group created during instance replication. The default traffic distribution group cannot be deleted by the `DeleteTrafficDistributionGroup` API. The default traffic distribution group is deleted as part of the process for deleting a replica.

### Note

The `SignInConfig` distribution is available only on a default `TrafficDistributionGroup` (see the `IsDefault` parameter in the [TrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_TrafficDistributionGroup.html) data type). If you call `UpdateTrafficDistribution` with a modified `SignInConfig` and a non-default `TrafficDistributionGroup` , an `InvalidRequestException` is returned.