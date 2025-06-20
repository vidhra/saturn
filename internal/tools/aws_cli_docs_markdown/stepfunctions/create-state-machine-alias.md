# create-state-machine-aliasÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/create-state-machine-alias.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/create-state-machine-alias.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [stepfunctions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/index.html#cli-aws-stepfunctions) ]

# create-state-machine-alias

## Description

Creates an [alias](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html) for a state machine that points to one or two [versions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html) of the same state machine. You can set your application to call  StartExecution with an alias and update the version the alias uses without changing the clientâs code.

You can also map an alias to split  StartExecution requests between two versions of a state machine. To do this, add a second `RoutingConfig` object in the `routingConfiguration` parameter. You must also specify the percentage of execution run requests each version should receive in both `RoutingConfig` objects. Step Functions randomly chooses which version runs a given execution based on the percentage you specify.

To create an alias that points to a single version, specify a single `RoutingConfig` object with a `weight` set to 100.

You can create up to 100 aliases for each state machine. You must delete unused aliases using the  DeleteStateMachineAlias API action.

`CreateStateMachineAlias` is an idempotent API. Step Functions bases the idempotency check on the `stateMachineArn` , `description` , `name` , and `routingConfiguration` parameters. Requests that contain the same values for these parameters return a successful idempotent response without creating a duplicate resource.

**Related operations:**

- DescribeStateMachineAlias
- ListStateMachineAliases
- UpdateStateMachineAlias
- DeleteStateMachineAlias

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/CreateStateMachineAlias)

## Synopsis

```
create-state-machine-alias
[--description <value>]
--name <value>
--routing-configuration <value>
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

`--description` (string)

A description for the state machine alias.

`--name` (string)

The name of the state machine alias.

To avoid conflict with version ARNs, donât use an integer in the name of the alias.

`--routing-configuration` (list)

The routing configuration of a state machine alias. The routing configuration shifts execution traffic between two state machine versions. `routingConfiguration` contains an array of `RoutingConfig` objects that specify up to two state machine versions. Step Functions then randomly choses which version to run an execution with based on the weight assigned to each `RoutingConfig` .

(structure)

Contains details about the routing configuration of a state machine alias. In a routing configuration, you define an array of objects that specify up to two state machine versions. You also specify the percentage of traffic to be routed to each version.

stateMachineVersionArn -> (string)

The Amazon Resource Name (ARN) that identifies one or two state machine versions defined in the routing configuration.

If you specify the ARN of a second version, it must belong to the same state machine as the first version.

weight -> (integer)

The percentage of traffic you want to route to a state machine version. The sum of the weights in the routing configuration must be equal to 100.

Shorthand Syntax:

```
stateMachineVersionArn=string,weight=integer ...
```

JSON Syntax:

```
[
  {
    "stateMachineVersionArn": "string",
    "weight": integer
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

stateMachineAliasArn -> (string)

The Amazon Resource Name (ARN) that identifies the created state machine alias.

creationDate -> (timestamp)

The date the state machine alias was created.