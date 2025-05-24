# create-hosted-zoneÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-hosted-zone.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-hosted-zone.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html#cli-aws-route53) ]

# create-hosted-zone

## Description

Creates a new public or private hosted zone. You create records in a public hosted zone to define how you want to route traffic on the internet for a domain, such as example.com, and its subdomains (apex.example.com, acme.example.com). You create records in a private hosted zone to define how you want to route traffic for a domain and its subdomains within one or more Amazon Virtual Private Clouds (Amazon VPCs).

### Warning

You canât convert a public hosted zone to a private hosted zone or vice versa. Instead, you must create a new hosted zone with the same name and create new resource record sets.

For more information about charges for hosted zones, see [Amazon Route 53 Pricing](http://aws.amazon.com/route53/pricing/) .

Note the following:

- You canât create a hosted zone for a top-level domain (TLD) such as .com.
- For public hosted zones, Route 53 automatically creates a default SOA record and four NS records for the zone. For more information about SOA and NS records, see [NS and SOA Records that Route 53 Creates for a Hosted Zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/SOA-NSrecords.html) in the *Amazon Route 53 Developer Guide* . If you want to use the same name servers for multiple public hosted zones, you can optionally associate a reusable delegation set with the hosted zone. See the `DelegationSetId` element.
- If your domain is registered with a registrar other than Route 53, you must update the name servers with your registrar to make Route 53 the DNS service for the domain. For more information, see [Migrating DNS Service for an Existing Domain to Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/MigratingDNS.html) in the *Amazon Route 53 Developer Guide* .

When you submit a `CreateHostedZone` request, the initial status of the hosted zone is `PENDING` . For public hosted zones, this means that the NS and SOA records are not yet available on all Route 53 DNS servers. When the NS and SOA records are available, the status of the zone changes to `INSYNC` .

The `CreateHostedZone` request requires the caller to have an `ec2:DescribeVpcs` permission.

### Note

When creating private hosted zones, the Amazon VPC must belong to the same partition where the hosted zone is created. A partition is a group of Amazon Web Services Regions. Each Amazon Web Services account is scoped to one partition.

The following are the supported partitions:

- `aws` - Amazon Web Services Regions
- `aws-cn` - China Regions
- `aws-us-gov` - Amazon Web Services GovCloud (US) Region

For more information, see [Access Management](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/CreateHostedZone)

## Synopsis

```
create-hosted-zone
--name <value>
[--vpc <value>]
--caller-reference <value>
[--hosted-zone-config <value>]
[--delegation-set-id <value>]
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

`--name` (string)

The name of the domain. Specify a fully qualified domain name, for example, *www.example.com* . The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats *www.example.com* (without a trailing dot) and *www.example.com.* (with a trailing dot) as identical.

If youâre creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Route 53, change the name servers for your domain to the set of `NameServers` that `CreateHostedZone` returns in `DelegationSet` .

`--vpc` (structure)

(Private hosted zones only) A complex type that contains information about the Amazon VPC that youâre associating with this hosted zone.

You can specify only one Amazon VPC when you create a private hosted zone. If you are associating a VPC with a hosted zone with this request, the paramaters `VPCId` and `VPCRegion` are also required.

To associate additional Amazon VPCs with the hosted zone, use [AssociateVPCWithHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_AssociateVPCWithHostedZone.html) after you create a hosted zone.

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

`--caller-reference` (string)

A unique string that identifies the request and that allows failed `CreateHostedZone` requests to be retried without the risk of executing the operation twice. You must use a unique `CallerReference` string every time you submit a `CreateHostedZone` request. `CallerReference` can be any unique string, for example, a date/time stamp.

`--hosted-zone-config` (structure)

(Optional) A complex type that contains the following optional values:

- For public and private hosted zones, an optional comment
- For private hosted zones, an optional `PrivateZone` element

If you donât specify a comment or the `PrivateZone` element, omit `HostedZoneConfig` and the other elements.

Comment -> (string)

Any comments that you want to include about the hosted zone.

PrivateZone -> (boolean)

A value that indicates whether this is a private hosted zone.

Note do **not** include `PrivateZone` in this input structure. Its value is returned in the output to the command.

Shorthand Syntax:

```
Comment=string,PrivateZone=boolean
```

JSON Syntax:

```
{
  "Comment": "string",
  "PrivateZone": true|false
}
```

`--delegation-set-id` (string)

If you want to associate a reusable delegation set with this hosted zone, the ID that Amazon Route 53 assigned to the reusable delegation set when you created it. For more information about reusable delegation sets, see [CreateReusableDelegationSet](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateReusableDelegationSet.html) .

If you are using a reusable delegation set to create a public hosted zone for a subdomain, make sure that the parent hosted zone doesnât use one or more of the same name servers. If you have overlapping nameservers, the operation will cause a `ConflictingDomainsExist` error.

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

**To create a hosted zone**

The following `create-hosted-zone` command adds a hosted zone named `example.com` using the caller reference `2014-04-01-18:47`. The optional comment includes a space, so it must be enclosed in quotation marks:

```
aws route53 create-hosted-zone --name example.com --caller-reference 2014-04-01-18:47 --hosted-zone-config Comment="command-line version"
```

For more information, see [Working with Hosted Zones](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/AboutHZWorkingWith.html) in the *Amazon Route 53 Developer Guide*.

## Output

HostedZone -> (structure)

A complex type that contains general information about the hosted zone.

Id -> (string)

The ID that Amazon Route 53 assigned to the hosted zone when you created it.

Name -> (string)

The name of the domain. For public hosted zones, this is the name that you have registered with your DNS registrar.

For information about how to specify characters other than `a-z` , `0-9` , and `-` (hyphen) and how to specify internationalized domain names, see [CreateHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html) .

CallerReference -> (string)

The value that you specified for `CallerReference` when you created the hosted zone.

Config -> (structure)

A complex type that includes the `Comment` and `PrivateZone` elements. If you omitted the `HostedZoneConfig` and `Comment` elements from the request, the `Config` and `Comment` elements donât appear in the response.

Comment -> (string)

Any comments that you want to include about the hosted zone.

PrivateZone -> (boolean)

A value that indicates whether this is a private hosted zone.

ResourceRecordSetCount -> (long)

The number of resource record sets in the hosted zone.

LinkedService -> (structure)

If the hosted zone was created by another service, the service that created the hosted zone. When a hosted zone is created by another service, you canât edit or delete it using Route 53.

ServicePrincipal -> (string)

If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you canât edit or delete it using Amazon Route 53.

Description -> (string)

If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you canât edit or delete it using Amazon Route 53.

ChangeInfo -> (structure)

A complex type that contains information about the `CreateHostedZone` request.

Id -> (string)

This element contains an ID that you use when performing a [GetChange](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html) action to get detailed information about the change.

Status -> (string)

The current state of the request. `PENDING` indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.

SubmittedAt -> (timestamp)

The date and time that the change request was submitted in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601) and Coordinated Universal Time (UTC). For example, the value `2017-03-27T17:48:16.751Z` represents March 27, 2017 at 17:48:16.751 UTC.

Comment -> (string)

A comment you can provide.

DelegationSet -> (structure)

A complex type that describes the name servers for this hosted zone.

Id -> (string)

The ID that Amazon Route 53 assigns to a reusable delegation set.

CallerReference -> (string)

The value that you specified for `CallerReference` when you created the reusable delegation set.

NameServers -> (list)

A complex type that contains a list of the authoritative name servers for a hosted zone or for a reusable delegation set.

(string)

VPC -> (structure)

A complex type that contains information about an Amazon VPC that you associated with this hosted zone.

VPCRegion -> (string)

(Private hosted zones only) The region that an Amazon VPC was created in.

VPCId -> (string)

(Private hosted zones only) The ID of an Amazon VPC.

Location -> (string)

The unique URL representing the new hosted zone.