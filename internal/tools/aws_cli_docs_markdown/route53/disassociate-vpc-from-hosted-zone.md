# disassociate-vpc-from-hosted-zoneÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/disassociate-vpc-from-hosted-zone.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/disassociate-vpc-from-hosted-zone.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html#cli-aws-route53) ]

# disassociate-vpc-from-hosted-zone

## Description

Disassociates an Amazon Virtual Private Cloud (Amazon VPC) from an Amazon Route 53 private hosted zone. Note the following:

- You canât disassociate the last Amazon VPC from a private hosted zone.
- You canât convert a private hosted zone into a public hosted zone.
- You can submit a `DisassociateVPCFromHostedZone` request using either the account that created the hosted zone or the account that created the Amazon VPC.
- Some services, such as Cloud Map and Amazon Elastic File System (Amazon EFS) automatically create hosted zones and associate VPCs with the hosted zones. A service can create a hosted zone using your account or using its own account. You can disassociate a VPC from a hosted zone only if the service created the hosted zone using your account. When you run [DisassociateVPCFromHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHostedZonesByVPC.html) , if the hosted zone has a value for `OwningAccount` , you can use `DisassociateVPCFromHostedZone` . If the hosted zone has a value for `OwningService` , you canât use `DisassociateVPCFromHostedZone` .

### Note

When revoking access, the hosted zone and the Amazon VPC must belong to the same partition. A partition is a group of Amazon Web Services Regions. Each Amazon Web Services account is scoped to one partition.

The following are the supported partitions:

- `aws` - Amazon Web Services Regions
- `aws-cn` - China Regions
- `aws-us-gov` - Amazon Web Services GovCloud (US) Region

For more information, see [Access Management](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/DisassociateVPCFromHostedZone)

## Synopsis

```
disassociate-vpc-from-hosted-zone
--hosted-zone-id <value>
--vpc <value>
[--comment <value>]
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

`--hosted-zone-id` (string)

The ID of the private hosted zone that you want to disassociate a VPC from.

`--vpc` (structure)

A complex type that contains information about the VPC that youâre disassociating from the specified hosted zone.

VPCRegion -> (string)

(Private hosted zones only) The region that an Amazon VPC was created in.

VPCId -> (string)

(Private hosted zones only) The ID of an Amazon VPC.

Shorthand Syntax:

```
VPCRegion=string,VPCId=string
```

JSON Syntax:

```
{
  "VPCRegion": "us-east-1"|"us-east-2"|"us-west-1"|"us-west-2"|"eu-west-1"|"eu-west-2"|"eu-west-3"|"eu-central-1"|"eu-central-2"|"ap-east-1"|"me-south-1"|"us-gov-west-1"|"us-gov-east-1"|"us-iso-east-1"|"us-iso-west-1"|"us-isob-east-1"|"me-central-1"|"ap-southeast-1"|"ap-southeast-2"|"ap-southeast-3"|"ap-south-1"|"ap-south-2"|"ap-northeast-1"|"ap-northeast-2"|"ap-northeast-3"|"eu-north-1"|"sa-east-1"|"ca-central-1"|"cn-north-1"|"cn-northwest-1"|"af-south-1"|"eu-south-1"|"eu-south-2"|"ap-southeast-4"|"il-central-1"|"ca-west-1"|"ap-southeast-5"|"mx-central-1"|"us-isof-south-1"|"us-isof-east-1"|"ap-southeast-7",
  "VPCId": "string"
}
```

`--comment` (string)

*Optional:* A comment about the disassociation request.

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

ChangeInfo -> (structure)

A complex type that describes the changes made to the specified private hosted zone.

Id -> (string)

This element contains an ID that you use when performing a [GetChange](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html) action to get detailed information about the change.

Status -> (string)

The current state of the request. `PENDING` indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.

SubmittedAt -> (timestamp)

The date and time that the change request was submitted in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601) and Coordinated Universal Time (UTC). For example, the value `2017-03-27T17:48:16.751Z` represents March 27, 2017 at 17:48:16.751 UTC.

Comment -> (string)

A comment you can provide.