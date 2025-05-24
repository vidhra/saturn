# create-agent-aliasÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent/create-agent-alias.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent/create-agent-alias.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bedrock-agent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent/index.html#cli-aws-bedrock-agent) ]

# create-agent-alias

## Description

Creates an alias of an agent that can be used to deploy the agent.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agent-2023-06-05/CreateAgentAlias)

## Synopsis

```
create-agent-alias
--agent-alias-name <value>
--agent-id <value>
[--client-token <value>]
[--description <value>]
[--routing-configuration <value>]
[--tags <value>]
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

`--agent-alias-name` (string)

The name of the alias.

`--agent-id` (string)

The unique identifier of the agent.

`--client-token` (string)

A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) .

`--description` (string)

A description of the alias of the agent.

`--routing-configuration` (list)

Contains details about the routing configuration of the alias.

(structure)

Contains details about the routing configuration of the alias.

agentVersion -> (string)

The version of the agent with which the alias is associated.

provisionedThroughput -> (string)

Information on the Provisioned Throughput assigned to an agent alias.

Shorthand Syntax:

```
agentVersion=string,provisionedThroughput=string ...
```

JSON Syntax:

```
[
  {
    "agentVersion": "string",
    "provisionedThroughput": "string"
  }
  ...
]
```

`--tags` (map)

Any tags that you want to attach to the alias of the agent.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

agentAlias -> (structure)

Contains details about the alias that was created.

agentAliasArn -> (string)

The Amazon Resource Name (ARN) of the alias of the agent.

agentAliasHistoryEvents -> (list)

Contains details about the history of the alias.

(structure)

Contains details about the history of the alias.

endDate -> (timestamp)

The date that the alias stopped being associated to the version in the `routingConfiguration` object

routingConfiguration -> (list)

Contains details about the version of the agent with which the alias is associated.

(structure)

Contains details about the routing configuration of the alias.

agentVersion -> (string)

The version of the agent with which the alias is associated.

provisionedThroughput -> (string)

Information on the Provisioned Throughput assigned to an agent alias.

startDate -> (timestamp)

The date that the alias began being associated to the version in the `routingConfiguration` object.

agentAliasId -> (string)

The unique identifier of the alias of the agent.

agentAliasName -> (string)

The name of the alias of the agent.

agentAliasStatus -> (string)

The status of the alias of the agent and whether it is ready for use. The following statuses are possible:

- CREATING â The agent alias is being created.
- PREPARED â The agent alias is finished being created or updated and is ready to be invoked.
- FAILED â The agent alias API operation failed.
- UPDATING â The agent alias is being updated.
- DELETING â The agent alias is being deleted.
- DISSOCIATED - The agent alias has no version associated with it.

agentId -> (string)

The unique identifier of the agent.

clientToken -> (string)

A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) .

createdAt -> (timestamp)

The time at which the alias of the agent was created.

description -> (string)

The description of the alias of the agent.

failureReasons -> (list)

Information on the failure of Provisioned Throughput assigned to an agent alias.

(string)

routingConfiguration -> (list)

Contains details about the routing configuration of the alias.

(structure)

Contains details about the routing configuration of the alias.

agentVersion -> (string)

The version of the agent with which the alias is associated.

provisionedThroughput -> (string)

Information on the Provisioned Throughput assigned to an agent alias.

updatedAt -> (timestamp)

The time at which the alias was last updated.