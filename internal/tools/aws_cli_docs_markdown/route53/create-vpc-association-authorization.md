# create-vpc-association-authorizationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-vpc-association-authorization.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-vpc-association-authorization.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html#cli-aws-route53) ]

# create-vpc-association-authorization

## Description

Authorizes the Amazon Web Services account that created a specified VPC to submit an `AssociateVPCWithHostedZone` request to associate the VPC with a specified hosted zone that was created by a different account. To submit a `CreateVPCAssociationAuthorization` request, you must use the account that created the hosted zone. After you authorize the association, use the account that created the VPC to submit an `AssociateVPCWithHostedZone` request.

### Note

If you want to associate multiple VPCs that you created by using one account with a hosted zone that you created by using a different account, you must submit one authorization request for each VPC.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/CreateVPCAssociationAuthorization)

## Synopsis

```
create-vpc-association-authorization
--hosted-zone-id <value>
--vpc <value>
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

The ID of the private hosted zone that you want to authorize associating a VPC with.

`--vpc` (structure)

A complex type that contains the VPC ID and region for the VPC that you want to authorize associating with your hosted zone.

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

HostedZoneId -> (string)

The ID of the hosted zone that you authorized associating a VPC with.

VPC -> (structure)

The VPC that you authorized associating with a hosted zone.

VPCRegion -> (string)

(Private hosted zones only) The region that an Amazon VPC was created in.

VPCId -> (string)

(Private hosted zones only) The ID of an Amazon VPC.