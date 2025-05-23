# describe-service-link-virtual-interfacesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-service-link-virtual-interfaces.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-service-link-virtual-interfaces.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-service-link-virtual-interfaces

## Description

Describes the Outpost service link virtual interfaces.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeServiceLinkVirtualInterfaces)

## Synopsis

```
describe-service-link-virtual-interfaces
[--service-link-virtual-interface-ids <value>]
[--filters <value>]
[--max-results <value>]
[--next-token <value>]
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

`--service-link-virtual-interface-ids` (list)

The IDs of the service link virtual interfaces.

(string)

Syntax:

```
"string" "string" ...
```

`--filters` (list)

The filters to use for narrowing down the request. The following filters are supported:

- `outpost-lag-id` - The ID of the Outpost LAG.
- `outpost-arn` - The Outpost ARN.
- `owner-id` - The ID of the Amazon Web Services account that owns the service link virtual interface.
- `state` - The state of the Outpost LAG.
- `vlan` - The ID of the address pool.
- `service-link-virtual-interface-id` - The ID of the service link virtual interface.
- `local-gateway-virtual-interface-id` - The ID of the local gateway virtual interface.

(structure)

A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.

If you specify multiple filters, the filters are joined with an `AND` , and the request returns only results that match all of the specified filters.

For more information, see [List and filter using the CLI and API](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html#Filtering_Resources_CLI) in the *Amazon EC2 User Guide* .

Name -> (string)

The name of the filter. Filter names are case-sensitive.

Values -> (list)

The filter values. Filter values are case-sensitive. If you specify multiple values for a filter, the values are joined with an `OR` , and the request returns all results that match any of the specified values.

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Values": ["string", ...]
  }
  ...
]
```

`--max-results` (integer)

The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.

`--next-token` (string)

The token for the next page of results.

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

## Output

ServiceLinkVirtualInterfaces -> (list)

Describes the service link virtual interfaces.

(structure)

Describes the service link virtual interfaces that establish connectivity between Amazon Web Services Outpost and on-premises networks.

ServiceLinkVirtualInterfaceId -> (string)

The ID of the service link virtual interface.

ServiceLinkVirtualInterfaceArn -> (string)

The Amazon Resource Number (ARN) for the service link virtual interface.

OutpostId -> (string)

The Outpost ID for the service link virtual interface.

OutpostArn -> (string)

The Outpost Amazon Resource Number (ARN) for the service link virtual interface.

OwnerId -> (string)

The ID of the Amazon Web Services account that owns the service link virtual interface..

LocalAddress -> (string)

The IPv4 address assigned to the local gateway virtual interface on the Outpost side.

PeerAddress -> (string)

The IPv4 peer address for the service link virtual interface.

PeerBgpAsn -> (long)

The ASN for the Border Gateway Protocol (BGP) associated with the service link virtual interface.

Vlan -> (integer)

The virtual local area network for the service link virtual interface.

OutpostLagId -> (string)

The link aggregation group (LAG) ID for the service link virtual interface.

Tags -> (list)

The tags associated with the service link virtual interface.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

ConfigurationState -> (string)

The current state of the service link virtual interface.

NextToken -> (string)

The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.