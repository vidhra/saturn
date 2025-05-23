# describe-instanceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-instance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-instance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# describe-instance

## Description

This API is in preview release for Amazon Connect and is subject to change.

Returns the current state of the specified instance identifier. It tracks the instance while it is being created and returns an error status, if applicable.

If an instance is not created successfully, the instance status reason field returns details relevant to the reason. The instance in a failed state is returned only for 24 hours after the CreateInstance API was invoked.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/DescribeInstance)

## Synopsis

```
describe-instance
--instance-id <value>
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

`--instance-id` (string)

The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.

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

Instance -> (structure)

The name of the instance.

Id -> (string)

The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.

Arn -> (string)

The Amazon Resource Name (ARN) of the instance.

IdentityManagementType -> (string)

The identity management type.

InstanceAlias -> (string)

The alias of instance.

CreatedTime -> (timestamp)

When the instance was created.

ServiceRole -> (string)

The service role of the instance.

InstanceStatus -> (string)

The state of the instance.

StatusReason -> (structure)

Relevant details why the instance was not successfully created.

Message -> (string)

The message.

InboundCallsEnabled -> (boolean)

Whether inbound calls are enabled.

OutboundCallsEnabled -> (boolean)

Whether outbound calls are enabled.

InstanceAccessUrl -> (string)

This URL allows contact center users to access the Amazon Connect admin website.

Tags -> (map)

The tags of an instance.

key -> (string)

value -> (string)

ReplicationConfiguration -> (structure)

Status information about the replication process. This field is included only when you are using the [ReplicateInstance](https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicateInstance.html) API to replicate an Amazon Connect instance across Amazon Web Services Regions. For information about replicating Amazon Connect instances, see [Create a replica of your existing Amazon Connect instance](https://docs.aws.amazon.com/connect/latest/adminguide/create-replica-connect-instance.html) in the *Amazon Connect Administrator Guide* .

ReplicationStatusSummaryList -> (list)

A list of replication status summaries. The summaries contain details about the replication of configuration information for Amazon Connect resources, for each Amazon Web Services Region.

(structure)

Status information about the replication process, where you use the [ReplicateInstance](https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicateInstance.html) API to create a replica of your Amazon Connect instance in another Amazon Web Services Region. For more information, see [Set up Amazon Connect Global Resiliency](https://docs.aws.amazon.com/connect/latest/adminguide/setup-connect-global-resiliency.html) in the *Amazon Connect Administrator Guide* .

Region -> (string)

The Amazon Web Services Region. This can be either the source or the replica Region, depending where it appears in the summary list.

ReplicationStatus -> (string)

The state of the replication.

ReplicationStatusReason -> (string)

A description of the replication status. Use this information to resolve any issues that are preventing the successful replication of your Amazon Connect instance to another Region.

SourceRegion -> (string)

The Amazon Web Services Region where the source Amazon Connect instance was created. This is the Region where the [ReplicateInstance](https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicateInstance.html) API was called to start the replication process.

GlobalSignInEndpoint -> (string)

The URL that is used to sign-in to your Amazon Connect instance according to your traffic distribution group configuration. For more information about sign-in and traffic distribution groups, see [Important things to know](https://docs.aws.amazon.com/connect/latest/adminguide/setup-traffic-distribution-groups.html) in the *Create traffic distribution groups* topic in the *Amazon Connect Administrator Guide* .