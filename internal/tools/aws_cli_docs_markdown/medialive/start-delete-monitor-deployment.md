# start-delete-monitor-deploymentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/start-delete-monitor-deployment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/start-delete-monitor-deployment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [medialive](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/index.html#cli-aws-medialive) ]

# start-delete-monitor-deployment

## Description

Initiates a deployment to delete the monitor of the specified signal map.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/StartDeleteMonitorDeployment)

## Synopsis

```
start-delete-monitor-deployment
--identifier <value>
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

`--identifier` (string)
A signal mapâs identifier. Can be either be its id or current name.

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

Arn -> (string)

A signal mapâs ARN (Amazon Resource Name)

CloudWatchAlarmTemplateGroupIds -> (list)

Placeholder documentation for __listOf__stringMin7Max11PatternAws097

(string)

Placeholder documentation for __stringMin7Max11PatternAws097

CreatedAt -> (timestamp)

Placeholder documentation for __timestampIso8601

Description -> (string)

A resourceâs optional description.

DiscoveryEntryPointArn -> (string)

A top-level supported AWS resource ARN to discovery a signal map from.

ErrorMessage -> (string)

Error message associated with a failed creation or failed update attempt of a signal map.

EventBridgeRuleTemplateGroupIds -> (list)

Placeholder documentation for __listOf__stringMin7Max11PatternAws097

(string)

Placeholder documentation for __stringMin7Max11PatternAws097

FailedMediaResourceMap -> (map)

A map representing an incomplete AWS media workflow as a graph.

key -> (string)

Placeholder documentation for __string

value -> (structure)

An AWS resource used in media workflows.

Destinations -> (list)

Placeholder documentation for __listOfMediaResourceNeighbor

(structure)

A direct source or destination neighbor to an AWS media resource.

Arn -> (string)

The ARN of a resource used in AWS media workflows.

Name -> (string)

The logical name of an AWS media resource.

Name -> (string)

The logical name of an AWS media resource.

Sources -> (list)

Placeholder documentation for __listOfMediaResourceNeighbor

(structure)

A direct source or destination neighbor to an AWS media resource.

Arn -> (string)

The ARN of a resource used in AWS media workflows.

Name -> (string)

The logical name of an AWS media resource.

Id -> (string)

A signal mapâs id.

LastDiscoveredAt -> (timestamp)

Placeholder documentation for __timestampIso8601

LastSuccessfulMonitorDeployment -> (structure)

Represents the latest successful monitor deployment of a signal map.

DetailsUri -> (string)

URI associated with a signal mapâs monitor deployment.

Status -> (string)

A signal mapâs monitor deployment status.

MediaResourceMap -> (map)

A map representing an AWS media workflow as a graph.

key -> (string)

Placeholder documentation for __string

value -> (structure)

An AWS resource used in media workflows.

Destinations -> (list)

Placeholder documentation for __listOfMediaResourceNeighbor

(structure)

A direct source or destination neighbor to an AWS media resource.

Arn -> (string)

The ARN of a resource used in AWS media workflows.

Name -> (string)

The logical name of an AWS media resource.

Name -> (string)

The logical name of an AWS media resource.

Sources -> (list)

Placeholder documentation for __listOfMediaResourceNeighbor

(structure)

A direct source or destination neighbor to an AWS media resource.

Arn -> (string)

The ARN of a resource used in AWS media workflows.

Name -> (string)

The logical name of an AWS media resource.

ModifiedAt -> (timestamp)

Placeholder documentation for __timestampIso8601

MonitorChangesPendingDeployment -> (boolean)

If true, there are pending monitor changes for this signal map that can be deployed.

MonitorDeployment -> (structure)

Represents the latest monitor deployment of a signal map.

DetailsUri -> (string)

URI associated with a signal mapâs monitor deployment.

ErrorMessage -> (string)

Error message associated with a failed monitor deployment of a signal map.

Status -> (string)

A signal mapâs monitor deployment status.

Name -> (string)

A resourceâs name. Names must be unique within the scope of a resource type in a specific region.

Status -> (string)

A signal mapâs current status which is dependent on its lifecycle actions or associated jobs.

Tags -> (map)

Represents the tags associated with a resource.

key -> (string)

Placeholder documentation for __string

value -> (string)

Placeholder documentation for __string