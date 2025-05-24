# describe-agentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/describe-agent.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/describe-agent.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [datasync](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/index.html#cli-aws-datasync) ]

# describe-agent

## Description

Returns information about an DataSync agent, such as its name, service endpoint type, and status.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/DescribeAgent)

## Synopsis

```
describe-agent
--agent-arn <value>
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

`--agent-arn` (string)

Specifies the Amazon Resource Name (ARN) of the DataSync agent that you want information about.

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

AgentArn -> (string)

The ARN of the agent.

Name -> (string)

The name of the agent.

Status -> (string)

The status of the agent.

- If the status is `ONLINE` , the agent is configured properly and ready to use.
- If the status is `OFFLINE` , the agent has been out of contact with DataSync for five minutes or longer. This can happen for a few reasons. For more information, see [What do I do if my agent is offline?](https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-agents.html#troubleshoot-agent-offline)

LastConnectionTime -> (timestamp)

The last time that the agent was communicating with the DataSync service.

CreationTime -> (timestamp)

The time that the agent was [activated](https://docs.aws.amazon.com/datasync/latest/userguide/activate-agent.html) .

EndpointType -> (string)

The type of [service endpoint](https://docs.aws.amazon.com/datasync/latest/userguide/choose-service-endpoint.html) that your agent is connected to.

PrivateLinkConfig -> (structure)

The network configuration that the agent uses when connecting to a [VPC service endpoint](https://docs.aws.amazon.com/datasync/latest/userguide/choose-service-endpoint.html#choose-service-endpoint-vpc) .

VpcEndpointId -> (string)

Specifies the ID of the VPC endpoint that your agent connects to.

PrivateLinkEndpoint -> (string)

Specifies the VPC endpoint provided by [Amazon Web Services PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html) that your agent connects to.

SubnetArns -> (list)

Specifies the ARN of the subnet where your VPC endpoint is located. You can only specify one ARN.

(string)

SecurityGroupArns -> (list)

Specifies the Amazon Resource Names (ARN) of the security group that provides DataSync access to your VPC endpoint. You can only specify one ARN.

(string)

Platform -> (structure)

The platform-related details about the agent, such as the version number.

Version -> (string)

The version of the DataSync agent.