# create-vpc-ingress-connectionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/create-vpc-ingress-connection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/create-vpc-ingress-connection.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [apprunner](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/index.html#cli-aws-apprunner) ]

# create-vpc-ingress-connection

## Description

Create an App Runner VPC Ingress Connection resource. App Runner requires this resource when you want to associate your App Runner service with an Amazon VPC endpoint.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/apprunner-2020-05-15/CreateVpcIngressConnection)

## Synopsis

```
create-vpc-ingress-connection
--service-arn <value>
--vpc-ingress-connection-name <value>
--ingress-vpc-configuration <value>
[--tags <value>]
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

`--service-arn` (string)

The Amazon Resource Name (ARN) for this App Runner service that is used to create the VPC Ingress Connection resource.

`--vpc-ingress-connection-name` (string)

A name for the VPC Ingress Connection resource. It must be unique across all the active VPC Ingress Connections in your Amazon Web Services account in the Amazon Web Services Region.

`--ingress-vpc-configuration` (structure)

Specifications for the customerâs Amazon VPC and the related Amazon Web Services PrivateLink VPC endpoint that are used to create the VPC Ingress Connection resource.

VpcId -> (string)

The ID of the VPC that is used for the VPC endpoint.

VpcEndpointId -> (string)

The ID of the VPC endpoint that your App Runner service connects to.

Shorthand Syntax:

```
VpcId=string,VpcEndpointId=string
```

JSON Syntax:

```
{
  "VpcId": "string",
  "VpcEndpointId": "string"
}
```

`--tags` (list)

An optional list of metadata items that you can associate with the VPC Ingress Connection resource. A tag is a key-value pair.

(structure)

Describes a tag that is applied to an App Runner resource. A tag is a metadata item consisting of a key-value pair.

Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
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

VpcIngressConnection -> (structure)

A description of the App Runner VPC Ingress Connection resource thatâs created by this request.

VpcIngressConnectionArn -> (string)

The Amazon Resource Name (ARN) of the VPC Ingress Connection.

VpcIngressConnectionName -> (string)

The customer-provided VPC Ingress Connection name.

ServiceArn -> (string)

The Amazon Resource Name (ARN) of the service associated with the VPC Ingress Connection.

Status -> (string)

The current status of the VPC Ingress Connection. The VPC Ingress Connection displays one of the following statuses: `AVAILABLE` , `PENDING_CREATION` , `PENDING_UPDATE` , `PENDING_DELETION` ,``FAILED_CREATION`` , `FAILED_UPDATE` , `FAILED_DELETION` , and `DELETED` ..

AccountId -> (string)

The Account Id you use to create the VPC Ingress Connection resource.

DomainName -> (string)

The domain name associated with the VPC Ingress Connection resource.

IngressVpcConfiguration -> (structure)

Specifications for the customerâs VPC and related PrivateLink VPC endpoint that are used to associate with the VPC Ingress Connection resource.

VpcId -> (string)

The ID of the VPC that is used for the VPC endpoint.

VpcEndpointId -> (string)

The ID of the VPC endpoint that your App Runner service connects to.

CreatedAt -> (timestamp)

The time when the VPC Ingress Connection was created. Itâs in the Unix time stamp format.

- Type: Timestamp
- Required: Yes

DeletedAt -> (timestamp)

The time when the App Runner service was deleted. Itâs in the Unix time stamp format.

- Type: Timestamp
- Required: No