# describe-verified-access-endpointsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-verified-access-endpoints.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-verified-access-endpoints.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-verified-access-endpoints

## Description

Describes the specified Amazon Web Services Verified Access endpoints.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVerifiedAccessEndpoints)

`describe-verified-access-endpoints` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `VerifiedAccessEndpoints`

## Synopsis

```
describe-verified-access-endpoints
[--verified-access-endpoint-ids <value>]
[--verified-access-instance-id <value>]
[--verified-access-group-id <value>]
[--filters <value>]
[--dry-run | --no-dry-run]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--verified-access-endpoint-ids` (list)

The ID of the Verified Access endpoint.

(string)

Syntax:

```
"string" "string" ...
```

`--verified-access-instance-id` (string)

The ID of the Verified Access instance.

`--verified-access-group-id` (string)

The ID of the Verified Access group.

`--filters` (list)

One or more filters. Filter names and values are case-sensitive.

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

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To describe a Verified Access endpoint**

The following `describe-verified-access-endpoints` example describes the specified Verified Access endpoint.

```
aws ec2 describe-verified-access-endpoints \
    --verified-access-endpoint-ids vae-066fac616d4d546f2
```

Output:

```
{
    "VerifiedAccessEndpoints": [
        {
            "VerifiedAccessInstanceId": "vai-0ce000c0b7643abea",
            "VerifiedAccessGroupId": "vagr-0dbe967baf14b7235",
            "VerifiedAccessEndpointId": "vae-066fac616d4d546f2",
            "ApplicationDomain": "example.com",
            "EndpointType": "network-interface",
            "AttachmentType": "vpc",
            "DomainCertificateArn": "arn:aws:acm:us-east-2:123456789012:certificate/eb065ea0-26f9-4e75-a6ce-0a1a7EXAMPLE",
            "EndpointDomain": "my-ava-app.edge-00c3372d53b1540bb.vai-0ce000c0b7643abea.prod.verified-access.us-east-2.amazonaws.com",
            "SecurityGroupIds": [
                "sg-004915970c4c8f13a"
            ],
            "NetworkInterfaceOptions": {
                "NetworkInterfaceId": "eni-0aec70418c8d87a0f",
                "Protocol": "https",
                "Port": 443
            },
            "Status": {
                "Code": "active"
            },
            "Description": "",
            "CreationTime": "2023-08-25T20:54:43",
            "LastUpdatedTime": "2023-08-25T22:17:26",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "my-va-endpoint"
                }
            ]
        }
    ]
}
```

For more information, see [Verified Access endpoints](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-endpoints.html) in the *AWS Verified Access User Guide*.

## Output

VerifiedAccessEndpoints -> (list)

Details about the Verified Access endpoints.

(structure)

An Amazon Web Services Verified Access endpoint specifies the application that Amazon Web Services Verified Access provides access to. It must be attached to an Amazon Web Services Verified Access group. An Amazon Web Services Verified Access endpoint must also have an attached access policy before you attached it to a group.

VerifiedAccessInstanceId -> (string)

The ID of the Amazon Web Services Verified Access instance.

VerifiedAccessGroupId -> (string)

The ID of the Amazon Web Services Verified Access group.

VerifiedAccessEndpointId -> (string)

The ID of the Amazon Web Services Verified Access endpoint.

ApplicationDomain -> (string)

The DNS name for users to reach your application.

EndpointType -> (string)

The type of Amazon Web Services Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified.

AttachmentType -> (string)

The type of attachment used to provide connectivity between the Amazon Web Services Verified Access endpoint and the application.

DomainCertificateArn -> (string)

The ARN of a public TLS/SSL certificate imported into or created with ACM.

EndpointDomain -> (string)

A DNS name that is generated for the endpoint.

DeviceValidationDomain -> (string)

Returned if endpoint has a device trust provider attached.

SecurityGroupIds -> (list)

The IDs of the security groups for the endpoint.

(string)

LoadBalancerOptions -> (structure)

The load balancer details if creating the Amazon Web Services Verified Access endpoint as `load-balancer` type.

Protocol -> (string)

The IP protocol.

Port -> (integer)

The IP port number.

LoadBalancerArn -> (string)

The ARN of the load balancer.

SubnetIds -> (list)

The IDs of the subnets.

(string)

PortRanges -> (list)

The port ranges.

(structure)

Describes a port range.

FromPort -> (integer)

The start of the port range.

ToPort -> (integer)

The end of the port range.

NetworkInterfaceOptions -> (structure)

The options for network-interface type endpoint.

NetworkInterfaceId -> (string)

The ID of the network interface.

Protocol -> (string)

The IP protocol.

Port -> (integer)

The IP port number.

PortRanges -> (list)

The port ranges.

(structure)

Describes a port range.

FromPort -> (integer)

The start of the port range.

ToPort -> (integer)

The end of the port range.

Status -> (structure)

The endpoint status.

Code -> (string)

The status code of the Verified Access endpoint.

Message -> (string)

The status message of the Verified Access endpoint.

Description -> (string)

A description for the Amazon Web Services Verified Access endpoint.

CreationTime -> (string)

The creation time.

LastUpdatedTime -> (string)

The last updated time.

DeletionTime -> (string)

The deletion time.

Tags -> (list)

The tags.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

SseSpecification -> (structure)

The options in use for server side encryption.

CustomerManagedKeyEnabled -> (boolean)

Indicates whether customer managed KMS keys are in use for server side encryption.

Valid values: `True` | `False`

KmsKeyArn -> (string)

The ARN of the KMS key.

RdsOptions -> (structure)

The options for an RDS endpoint.

Protocol -> (string)

The protocol.

Port -> (integer)

The port.

RdsDbInstanceArn -> (string)

The ARN of the RDS instance.

RdsDbClusterArn -> (string)

The ARN of the DB cluster.

RdsDbProxyArn -> (string)

The ARN of the RDS proxy.

RdsEndpoint -> (string)

The RDS endpoint.

SubnetIds -> (list)

The IDs of the subnets.

(string)

CidrOptions -> (structure)

The options for a CIDR endpoint.

Cidr -> (string)

The CIDR.

PortRanges -> (list)

The port ranges.

(structure)

Describes a port range.

FromPort -> (integer)

The start of the port range.

ToPort -> (integer)

The end of the port range.

Protocol -> (string)

The protocol.

SubnetIds -> (list)

The IDs of the subnets.

(string)

NextToken -> (string)

The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.