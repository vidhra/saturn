# describe-vpc-endpoint-associationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-endpoint-associations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-endpoint-associations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-vpc-endpoint-associations

## Description

Describes the VPC resources, VPC endpoint services, Amazon Lattice services, or service networks associated with the VPC endpoint.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcEndpointAssociations)

## Synopsis

```
describe-vpc-endpoint-associations
[--dry-run | --no-dry-run]
[--vpc-endpoint-ids <value>]
[--filters <value>]
[--max-results <value>]
[--next-token <value>]
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

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--vpc-endpoint-ids` (list)

The IDs of the VPC endpoints.

(string)

Syntax:

```
"string" "string" ...
```

`--filters` (list)

The filters.

- `vpc-endpoint-id` - The ID of the VPC endpoint.
- `associated-resource-accessibility` - The association state. When the state is `accessible` , it returns `AVAILABLE` . When the state is `inaccessible` , it returns `PENDING` or `FAILED` .
- `association-id` - The ID of the VPC endpoint association.
- `associated-resource-id` - The ID of the associated resource configuration.
- `service-network-arn` - The Amazon Resource Name (ARN) of the associated service network. Only VPC endpoints of type service network will be returned.
- `resource-configuration-group-arn` - The Amazon Resource Name (ARN) of the resource configuration of type GROUP.
- `service-network-resource-association-id` - The ID of the association.

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

The maximum page size.

`--next-token` (string)

The pagination token.

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

**To describe VPC endpoint associations**

The following `describe-vpc-endpoint-associations` example describes your VPC endpoint associations.

```
aws ec2 describe-vpc-endpoint-associations
```

Output:

```
{
    "VpcEndpointAssociations": [
        {
            "Id": "vpce-rsc-asc-0a810ca6ac8866bf9",
            "VpcEndpointId": "vpce-019b90d6f16d4f958",
            "AssociatedResourceAccessibility": "Accessible",
            "DnsEntry": {
                "DnsName": "vpce-019b90d6f16d4f958.rcfg-07129f3acded87625.4232ccc.vpc-lattice-rsc.us-east-2.on.aws",
                "HostedZoneId": "Z03265862FOUNWMZOKUF4"
            },
            "AssociatedResourceArn": "arn:aws:vpc-lattice:us-east-1:123456789012:resourceconfiguration/rcfg-07129f3acded87625"
        }
    ]
}
```

For more information, see [Manage VPC endpoint associations](https://docs.aws.amazon.com/vpc/latest/privatelink/resource-configuration-associations.html#resource-config-manage-ep-association) in the *AWS PrivateLink User Guide*.

## Output

VpcEndpointAssociations -> (list)

Details of the endpoint associations.

(structure)

Describes the VPC resources, VPC endpoint services, Lattice services, or service networks associated with the VPC endpoint.

Id -> (string)

The ID of the VPC endpoint association.

VpcEndpointId -> (string)

The ID of the VPC endpoint.

ServiceNetworkArn -> (string)

The Amazon Resource Name (ARN) of the service network.

ServiceNetworkName -> (string)

The name of the service network.

AssociatedResourceAccessibility -> (string)

The connectivity status of the resources associated to a VPC endpoint. The resource is accessible if the associated resource configuration is `AVAILABLE` , otherwise the resource is inaccessible.

FailureReason -> (string)

A message related to why an VPC endpoint association failed.

FailureCode -> (string)

An error code related to why an VPC endpoint association failed.

DnsEntry -> (structure)

The DNS entry of the VPC endpoint association.

DnsName -> (string)

The DNS name.

HostedZoneId -> (string)

The ID of the private hosted zone.

PrivateDnsEntry -> (structure)

The private DNS entry of the VPC endpoint association.

DnsName -> (string)

The DNS name.

HostedZoneId -> (string)

The ID of the private hosted zone.

AssociatedResourceArn -> (string)

The Amazon Resource Name (ARN) of the associated resource.

ResourceConfigurationGroupArn -> (string)

The Amazon Resource Name (ARN) of the resource configuration group.

Tags -> (list)

The tags to apply to the VPC endpoint association.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

NextToken -> (string)

The pagination token.