# list-hosted-zones-by-vpcÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-hosted-zones-by-vpc.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-hosted-zones-by-vpc.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html#cli-aws-route53) ]

# list-hosted-zones-by-vpc

## Description

Lists all the private hosted zones that a specified VPC is associated with, regardless of which Amazon Web Services account or Amazon Web Services service owns the hosted zones. The `HostedZoneOwner` structure in the response contains one of the following values:

- An `OwningAccount` element, which contains the account number of either the current Amazon Web Services account or another Amazon Web Services account. Some services, such as Cloud Map, create hosted zones using the current account.
- An `OwningService` element, which identifies the Amazon Web Services service that created and owns the hosted zone. For example, if a hosted zone was created by Amazon Elastic File System (Amazon EFS), the value of `Owner` is `efs.amazonaws.com` .

`ListHostedZonesByVPC` returns the hosted zones associated with the specified VPC and does not reflect the hosted zone associations to VPCs via Route 53 Profiles. To get the associations to a Profile, call the [ListProfileResourceAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ListProfileResourceAssociations.html) API.

### Note

When listing private hosted zones, the hosted zone and the Amazon VPC must belong to the same partition where the hosted zones were created. A partition is a group of Amazon Web Services Regions. Each Amazon Web Services account is scoped to one partition.

The following are the supported partitions:

- `aws` - Amazon Web Services Regions
- `aws-cn` - China Regions
- `aws-us-gov` - Amazon Web Services GovCloud (US) Region

For more information, see [Access Management](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListHostedZonesByVPC)

## Synopsis

```
list-hosted-zones-by-vpc
--vpc-id <value>
--vpc-region <value>
[--max-items <value>]
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

`--vpc-id` (string)

The ID of the Amazon VPC that you want to list hosted zones for.

`--vpc-region` (string)

For the Amazon VPC that you specified for `VPCId` , the Amazon Web Services Region that you created the VPC in.

Possible values:

- `us-east-1`
- `us-east-2`
- `us-west-1`
- `us-west-2`
- `eu-west-1`
- `eu-west-2`
- `eu-west-3`
- `eu-central-1`
- `eu-central-2`
- `ap-east-1`
- `me-south-1`
- `us-gov-west-1`
- `us-gov-east-1`
- `us-iso-east-1`
- `us-iso-west-1`
- `us-isob-east-1`
- `me-central-1`
- `ap-southeast-1`
- `ap-southeast-2`
- `ap-southeast-3`
- `ap-south-1`
- `ap-south-2`
- `ap-northeast-1`
- `ap-northeast-2`
- `ap-northeast-3`
- `eu-north-1`
- `sa-east-1`
- `ca-central-1`
- `cn-north-1`
- `cn-northwest-1`
- `af-south-1`
- `eu-south-1`
- `eu-south-2`
- `ap-southeast-4`
- `il-central-1`
- `ca-west-1`
- `ap-southeast-5`
- `mx-central-1`
- `us-isof-south-1`
- `us-isof-east-1`
- `ap-southeast-7`

`--max-items` (string)

(Optional) The maximum number of hosted zones that you want Amazon Route 53 to return. If the specified VPC is associated with more than `MaxItems` hosted zones, the response includes a `NextToken` element. `NextToken` contains an encrypted token that identifies the first hosted zone that Route 53 will return if you submit another request.

`--next-token` (string)

If the previous response included a `NextToken` element, the specified VPC is associated with more hosted zones. To get more hosted zones, submit another `ListHostedZonesByVPC` request.

For the value of `NextToken` , specify the value of `NextToken` from the previous response.

If the previous response didnât include a `NextToken` element, there are no more hosted zones to get.

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

HostedZoneSummaries -> (list)

A list that contains one `HostedZoneSummary` element for each hosted zone that the specified Amazon VPC is associated with. Each `HostedZoneSummary` element contains the hosted zone name and ID, and information about who owns the hosted zone.

(structure)

In the response to a `ListHostedZonesByVPC` request, the `HostedZoneSummaries` element contains one `HostedZoneSummary` element for each hosted zone that the specified Amazon VPC is associated with. Each `HostedZoneSummary` element contains the hosted zone name and ID, and information about who owns the hosted zone.

HostedZoneId -> (string)

The Route 53 hosted zone ID of a private hosted zone that the specified VPC is associated with.

Name -> (string)

The name of the private hosted zone, such as `example.com` .

Owner -> (structure)

The owner of a private hosted zone that the specified VPC is associated with. The owner can be either an Amazon Web Services account or an Amazon Web Services service.

OwningAccount -> (string)

If the hosted zone was created by an Amazon Web Services account, or was created by an Amazon Web Services service that creates hosted zones using the current account, `OwningAccount` contains the account ID of that account. For example, when you use Cloud Map to create a hosted zone, Cloud Map creates the hosted zone using the current Amazon Web Services account.

OwningService -> (string)

If an Amazon Web Services service uses its own account to create a hosted zone and associate the specified VPC with that hosted zone, `OwningService` contains an abbreviation that identifies the service. For example, if Amazon Elastic File System (Amazon EFS) created a hosted zone and associated a VPC with the hosted zone, the value of `OwningService` is `efs.amazonaws.com` .

MaxItems -> (string)

The value that you specified for `MaxItems` in the most recent `ListHostedZonesByVPC` request.

NextToken -> (string)

The value that you will use for `NextToken` in the next `ListHostedZonesByVPC` request.