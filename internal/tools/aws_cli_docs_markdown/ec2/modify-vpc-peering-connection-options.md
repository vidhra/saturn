# modify-vpc-peering-connection-optionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-peering-connection-options.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-peering-connection-options.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# modify-vpc-peering-connection-options

## Description

Modifies the VPC peering connection options on one side of a VPC peering connection.

If the peered VPCs are in the same Amazon Web Services account, you can enable DNS resolution for queries from the local VPC. This ensures that queries from the local VPC resolve to private IP addresses in the peer VPC. This option is not available if the peered VPCs are in different Amazon Web Services accounts or different Regions. For peered VPCs in different Amazon Web Services accounts, each Amazon Web Services account owner must initiate a separate request to modify the peering connection options. For inter-region peering connections, you must use the Region for the requester VPC to modify the requester VPC peering options and the Region for the accepter VPC to modify the accepter VPC peering options. To verify which VPCs are the accepter and the requester for a VPC peering connection, use the  DescribeVpcPeeringConnections command.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ModifyVpcPeeringConnectionOptions)

## Synopsis

```
modify-vpc-peering-connection-options
[--accepter-peering-connection-options <value>]
[--dry-run | --no-dry-run]
[--requester-peering-connection-options <value>]
--vpc-peering-connection-id <value>
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

`--accepter-peering-connection-options` (structure)

The VPC peering connection options for the accepter VPC.

AllowDnsResolutionFromRemoteVpc -> (boolean)

If true, enables a local VPC to resolve public DNS hostnames to private IP addresses when queried from instances in the peer VPC.

AllowEgressFromLocalClassicLinkToRemoteVpc -> (boolean)

Deprecated.

AllowEgressFromLocalVpcToRemoteClassicLink -> (boolean)

Deprecated.

Shorthand Syntax:

```
AllowDnsResolutionFromRemoteVpc=boolean,AllowEgressFromLocalClassicLinkToRemoteVpc=boolean,AllowEgressFromLocalVpcToRemoteClassicLink=boolean
```

JSON Syntax:

```
{
  "AllowDnsResolutionFromRemoteVpc": true|false,
  "AllowEgressFromLocalClassicLinkToRemoteVpc": true|false,
  "AllowEgressFromLocalVpcToRemoteClassicLink": true|false
}
```

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--requester-peering-connection-options` (structure)

The VPC peering connection options for the requester VPC.

AllowDnsResolutionFromRemoteVpc -> (boolean)

If true, enables a local VPC to resolve public DNS hostnames to private IP addresses when queried from instances in the peer VPC.

AllowEgressFromLocalClassicLinkToRemoteVpc -> (boolean)

Deprecated.

AllowEgressFromLocalVpcToRemoteClassicLink -> (boolean)

Deprecated.

Shorthand Syntax:

```
AllowDnsResolutionFromRemoteVpc=boolean,AllowEgressFromLocalClassicLinkToRemoteVpc=boolean,AllowEgressFromLocalVpcToRemoteClassicLink=boolean
```

JSON Syntax:

```
{
  "AllowDnsResolutionFromRemoteVpc": true|false,
  "AllowEgressFromLocalClassicLinkToRemoteVpc": true|false,
  "AllowEgressFromLocalVpcToRemoteClassicLink": true|false
}
```

`--vpc-peering-connection-id` (string)

The ID of the VPC peering connection.

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

**To enable communication over a VPC peering connection from your local ClassicLink connection**

In this example, for peering connection `pcx-aaaabbb`, the owner of the requester VPC modifies the VPC peering connection options to enable a local ClassicLink connection to communicate with the peer VPC.

Command:

```
aws ec2 modify-vpc-peering-connection-options --vpc-peering-connection-id pcx-aaaabbbb --requester-peering-connection-options AllowEgressFromLocalClassicLinkToRemoteVpc=true
```

Output:

```
{
  "RequesterPeeringConnectionOptions": {
      "AllowEgressFromLocalClassicLinkToRemoteVpc": true
  }
}
```

**To enable communication over a VPC peering connection from your local VPC to a remote ClassicLink connection**

In this example, the owner of the accepter VPC modifies the VPC peering connection options to enable the local VPC to communicate with the ClassicLink connection in the peer VPC.

Command:

```
aws ec2 modify-vpc-peering-connection-options --vpc-peering-connection-id pcx-aaaabbbb --accepter-peering-connection-options AllowEgressFromLocalVpcToRemoteClassicLink=true
```

Output:

```
{
  "AccepterPeeringConnectionOptions": {
    "AllowEgressFromLocalVpcToRemoteClassicLink": true
  }
}
```

**To enable DNS resolution support for the VPC peering connection**

In this example, the owner of the requester VPC modifies the VPC peering connection options for `pcx-aaaabbbb` to enable the local VPC to resolve public DNS hostnames to private IP addresses when queried from instances in the peer VPC.

Command:

```
aws ec2 modify-vpc-peering-connection-options --vpc-peering-connection-id pcx-aaaabbbb --requester-peering-connection-options AllowDnsResolutionFromRemoteVpc=true
```

Output:

```
{
  "RequesterPeeringConnectionOptions": {
      "AllowDnsResolutionFromRemoteVpc": true
  }
}
```

## Output

AccepterPeeringConnectionOptions -> (structure)

Information about the VPC peering connection options for the accepter VPC.

AllowDnsResolutionFromRemoteVpc -> (boolean)

If true, the public DNS hostnames of instances in the specified VPC resolve to private IP addresses when queried from instances in the peer VPC.

AllowEgressFromLocalClassicLinkToRemoteVpc -> (boolean)

Deprecated.

AllowEgressFromLocalVpcToRemoteClassicLink -> (boolean)

Deprecated.

RequesterPeeringConnectionOptions -> (structure)

Information about the VPC peering connection options for the requester VPC.

AllowDnsResolutionFromRemoteVpc -> (boolean)

If true, the public DNS hostnames of instances in the specified VPC resolve to private IP addresses when queried from instances in the peer VPC.

AllowEgressFromLocalClassicLinkToRemoteVpc -> (boolean)

Deprecated.

AllowEgressFromLocalVpcToRemoteClassicLink -> (boolean)

Deprecated.