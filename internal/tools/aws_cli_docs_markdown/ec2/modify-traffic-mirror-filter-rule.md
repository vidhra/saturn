# modify-traffic-mirror-filter-ruleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-traffic-mirror-filter-rule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-traffic-mirror-filter-rule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# modify-traffic-mirror-filter-rule

## Description

Modifies the specified Traffic Mirror rule.

`DestinationCidrBlock` and `SourceCidrBlock` must both be an IPv4 range or an IPv6 range.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ModifyTrafficMirrorFilterRule)

## Synopsis

```
modify-traffic-mirror-filter-rule
--traffic-mirror-filter-rule-id <value>
[--traffic-direction <value>]
[--rule-number <value>]
[--rule-action <value>]
[--destination-port-range <value>]
[--source-port-range <value>]
[--protocol <value>]
[--destination-cidr-block <value>]
[--source-cidr-block <value>]
[--description <value>]
[--remove-fields <value>]
[--dry-run | --no-dry-run]
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

`--traffic-mirror-filter-rule-id` (string)

The ID of the Traffic Mirror rule.

`--traffic-direction` (string)

The type of traffic to assign to the rule.

Possible values:

- `ingress`
- `egress`

`--rule-number` (integer)

The number of the Traffic Mirror rule. This number must be unique for each Traffic Mirror rule in a given direction. The rules are processed in ascending order by rule number.

`--rule-action` (string)

The action to assign to the rule.

Possible values:

- `accept`
- `reject`

`--destination-port-range` (structure)

The destination ports that are associated with the Traffic Mirror rule.

FromPort -> (integer)

The first port in the Traffic Mirror port range. This applies to the TCP and UDP protocols.

ToPort -> (integer)

The last port in the Traffic Mirror port range. This applies to the TCP and UDP protocols.

Shorthand Syntax:

```
FromPort=integer,ToPort=integer
```

JSON Syntax:

```
{
  "FromPort": integer,
  "ToPort": integer
}
```

`--source-port-range` (structure)

The port range to assign to the Traffic Mirror rule.

FromPort -> (integer)

The first port in the Traffic Mirror port range. This applies to the TCP and UDP protocols.

ToPort -> (integer)

The last port in the Traffic Mirror port range. This applies to the TCP and UDP protocols.

Shorthand Syntax:

```
FromPort=integer,ToPort=integer
```

JSON Syntax:

```
{
  "FromPort": integer,
  "ToPort": integer
}
```

`--protocol` (integer)

The protocol, for example TCP, to assign to the Traffic Mirror rule.

`--destination-cidr-block` (string)

The destination CIDR block to assign to the Traffic Mirror rule.

`--source-cidr-block` (string)

The source CIDR block to assign to the Traffic Mirror rule.

`--description` (string)

The description to assign to the Traffic Mirror rule.

`--remove-fields` (list)

The properties that you want to remove from the Traffic Mirror filter rule.

When you remove a property from a Traffic Mirror filter rule, the property is set to the default.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  destination-port-range
  source-port-range
  protocol
  description
```

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To modify a traffic mirror filter rule**

The following `modify-traffic-mirror-filter-rule` example modifies the description of the specified traffic mirror filter rule.

```
aws ec2 modify-traffic-mirror-filter-rule \
    --traffic-mirror-filter-rule-id tmfr-0ca76e0e08EXAMPLE \
    --description "TCP Rule"
```

Output:

```
{
    "TrafficMirrorFilterRule": {
        "TrafficMirrorFilterRuleId": "tmfr-0ca76e0e08EXAMPLE",
        "TrafficMirrorFilterId": "tmf-0293f26e86EXAMPLE",
        "TrafficDirection": "ingress",
        "RuleNumber": 100,
        "RuleAction": "accept",
        "Protocol": 6,
        "DestinationCidrBlock": "10.0.0.0/24",
        "SourceCidrBlock": "10.0.0.0/24",
        "Description": "TCP Rule"
    }
}
```

For more information, see [Modify Your Traffic Mirror Filter Rules](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-filter.html#modify-traffic-mirroring-filter-rules) in the *AWS Traffic Mirroring Guide*.

## Output

TrafficMirrorFilterRule -> (structure)

### Note

Tags are not returned for ModifyTrafficMirrorFilterRule.

A Traffic Mirror rule.

TrafficMirrorFilterRuleId -> (string)

The ID of the Traffic Mirror rule.

TrafficMirrorFilterId -> (string)

The ID of the Traffic Mirror filter that the rule is associated with.

TrafficDirection -> (string)

The traffic direction assigned to the Traffic Mirror rule.

RuleNumber -> (integer)

The rule number of the Traffic Mirror rule.

RuleAction -> (string)

The action assigned to the Traffic Mirror rule.

Protocol -> (integer)

The protocol assigned to the Traffic Mirror rule.

DestinationPortRange -> (structure)

The destination port range assigned to the Traffic Mirror rule.

FromPort -> (integer)

The start of the Traffic Mirror port range. This applies to the TCP and UDP protocols.

ToPort -> (integer)

The end of the Traffic Mirror port range. This applies to the TCP and UDP protocols.

SourcePortRange -> (structure)

The source port range assigned to the Traffic Mirror rule.

FromPort -> (integer)

The start of the Traffic Mirror port range. This applies to the TCP and UDP protocols.

ToPort -> (integer)

The end of the Traffic Mirror port range. This applies to the TCP and UDP protocols.

DestinationCidrBlock -> (string)

The destination CIDR block assigned to the Traffic Mirror rule.

SourceCidrBlock -> (string)

The source CIDR block assigned to the Traffic Mirror rule.

Description -> (string)

The description of the Traffic Mirror rule.

Tags -> (list)

Tags on Traffic Mirroring filter rules.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.