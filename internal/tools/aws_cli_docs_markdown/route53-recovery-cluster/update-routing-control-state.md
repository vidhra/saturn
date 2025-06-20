# update-routing-control-stateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53-recovery-cluster/update-routing-control-state.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53-recovery-cluster/update-routing-control-state.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53-recovery-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53-recovery-cluster/index.html#cli-aws-route53-recovery-cluster) ]

# update-routing-control-state

## Description

Set the state of the routing control to reroute traffic. You can set the value to ON or OFF. When the state is ON, traffic flows to a cell. When the state is OFF, traffic does not flow.

With Route 53 ARC, you can add safety rules for routing controls, which are safeguards for routing control state updates that help prevent unexpected outcomes, like fail open traffic routing. However, there are scenarios when you might want to bypass the routing control safeguards that are enforced with safety rules that youâve configured. For example, you might want to fail over quickly for disaster recovery, and one or more safety rules might be unexpectedly preventing you from updating a routing control state to reroute traffic. In a âbreak glassâ scenario like this, you can override one or more safety rules to change a routing control state and fail over your application.

The `SafetyRulesToOverride` property enables you override one or more safety rules and update routing control states. For more information, see [Override safety rules to reroute traffic](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.override-safety-rule.html) in the Amazon Route 53 Application Recovery Controller Developer Guide.

*You must specify Regional endpoints when you work with API cluster operations to get or update routing control states in Route 53 ARC.*

To see a code example for getting a routing control state, including accessing Regional cluster endpoints in sequence, see [API examples](https://docs.aws.amazon.com/r53recovery/latest/dg/service_code_examples_actions.html) in the Amazon Route 53 Application Recovery Controller Developer Guide.

- [Viewing and updating routing control states](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.update.html)
- [Working with routing controls overall](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-recovery-cluster-2019-12-02/UpdateRoutingControlState)

## Synopsis

```
update-routing-control-state
--routing-control-arn <value>
--routing-control-state <value>
[--safety-rules-to-override <value>]
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

`--routing-control-arn` (string)

The Amazon Resource Name (ARN) for the routing control that you want to update the state for.

`--routing-control-state` (string)

The state of the routing control. You can set the value to ON or OFF.

Possible values:

- `On`
- `Off`

`--safety-rules-to-override` (list)

The Amazon Resource Names (ARNs) for the safety rules that you want to override when youâre updating the state of a routing control. You can override one safety rule or multiple safety rules by including one or more ARNs, separated by commas.

For more information, see [Override safety rules to reroute traffic](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.override-safety-rule.html) in the Amazon Route 53 Application Recovery Controller Developer Guide.

(string)

Syntax:

```
"string" "string" ...
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

None