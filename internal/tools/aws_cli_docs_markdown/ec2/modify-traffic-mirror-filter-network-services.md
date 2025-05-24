# modify-traffic-mirror-filter-network-servicesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-traffic-mirror-filter-network-services.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-traffic-mirror-filter-network-services.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# modify-traffic-mirror-filter-network-services

## Description

Allows or restricts mirroring network services.

By default, Amazon DNS network services are not eligible for Traffic Mirror. Use `AddNetworkServices` to add network services to a Traffic Mirror filter. When a network service is added to the Traffic Mirror filter, all traffic related to that network service will be mirrored. When you no longer want to mirror network services, use `RemoveNetworkServices` to remove the network services from the Traffic Mirror filter.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ModifyTrafficMirrorFilterNetworkServices)

## Synopsis

```
modify-traffic-mirror-filter-network-services
--traffic-mirror-filter-id <value>
[--add-network-services <value>]
[--remove-network-services <value>]
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

`--traffic-mirror-filter-id` (string)

The ID of the Traffic Mirror filter.

`--add-network-services` (list)

The network service, for example Amazon DNS, that you want to mirror.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  amazon-dns
```

`--remove-network-services` (list)

The network service, for example Amazon DNS, that you no longer want to mirror.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  amazon-dns
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

**To add network services to a Traffic Mirror filter**

The following `modify-traffic-mirror-filter-network-services` example adds the Amazon DNS network services to the specified filter.

```
aws ec2 modify-traffic-mirror-filter-network-services \
    --traffic-mirror-filter-id tmf-04812ff784EXAMPLE \
    --add-network-service amazon-dns
```

Output:

```
{
    "TrafficMirrorFilter": {
        "Tags": [
            {
                "Key": "Name",
                "Value": "Production"
            }
        ],
        "EgressFilterRules": [],
        "NetworkServices": [
            "amazon-dns"
        ],
        "TrafficMirrorFilterId": "tmf-04812ff784EXAMPLE",
        "IngressFilterRules": [
            {
                "SourceCidrBlock": "0.0.0.0/0",
                "RuleNumber": 1,
                "DestinationCidrBlock": "0.0.0.0/0",
                "Description": "TCP Rule",
                "Protocol": 6,
                "TrafficDirection": "ingress",
                "TrafficMirrorFilterId": "tmf-04812ff784EXAMPLE",
                "RuleAction": "accept",
                "TrafficMirrorFilterRuleId": "tmf-04812ff784EXAMPLE"
            }
        ]
    }
}
```

For more information, see [Modify Traffic Mirror Filter Network Services](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-filter.html#modify-traffic-mirroring-filter-network-services) in the *AWS Traffic Mirroring Guide*.

## Output

TrafficMirrorFilter -> (structure)

The Traffic Mirror filter that the network service is associated with.

TrafficMirrorFilterId -> (string)

The ID of the Traffic Mirror filter.

IngressFilterRules -> (list)

Information about the ingress rules that are associated with the Traffic Mirror filter.

(structure)

Describes the Traffic Mirror rule.

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

EgressFilterRules -> (list)

Information about the egress rules that are associated with the Traffic Mirror filter.

(structure)

Describes the Traffic Mirror rule.

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

NetworkServices -> (list)

The network service traffic that is associated with the Traffic Mirror filter.

(string)

Description -> (string)

The description of the Traffic Mirror filter.

Tags -> (list)

The tags assigned to the Traffic Mirror filter.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.