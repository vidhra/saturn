# create-resource-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/create-resource-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/create-resource-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [vpc-lattice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/index.html#cli-aws-vpc-lattice) ]

# create-resource-configuration

## Description

Creates a resource configuration. A resource configuration defines a specific resource. You can associate a resource configuration with a service network or a VPC endpoint.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/vpc-lattice-2022-11-30/CreateResourceConfiguration)

## Synopsis

```
create-resource-configuration
[--allow-association-to-shareable-service-network | --no-allow-association-to-shareable-service-network]
[--client-token <value>]
--name <value>
[--port-ranges <value>]
[--protocol <value>]
[--resource-configuration-definition <value>]
[--resource-configuration-group-identifier <value>]
[--resource-gateway-identifier <value>]
[--tags <value>]
--type <value>
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

`--allow-association-to-shareable-service-network` | `--no-allow-association-to-shareable-service-network` (boolean)

(SINGLE, GROUP, ARN) Specifies whether the resource configuration can be associated with a sharable service network. The default is false.

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters arenât identical, the retry fails.

`--name` (string)

The name of the resource configuration. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You canât use a hyphen as the first or last character, or immediately after another hyphen.

`--port-ranges` (list)

(SINGLE, GROUP, CHILD) The TCP port ranges that a consumer can use to access a resource configuration (for example: 1-65535). You can separate port ranges using commas (for example: 1,2,22-30).

(string)

Syntax:

```
"string" "string" ...
```

`--protocol` (string)

(SINGLE, GROUP) The protocol accepted by the resource configuration.

Possible values:

- `TCP`

`--resource-configuration-definition` (tagged union structure)

(SINGLE, CHILD, ARN) The resource configuration.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `arnResource`, `dnsResource`, `ipResource`.

arnResource -> (structure)

The Amazon Resource Name (ARN) of the resource.

arn -> (string)

The Amazon Resource Name (ARN) of the resource.

dnsResource -> (structure)

The DNS name of the resource.

domainName -> (string)

The domain name of the resource.

ipAddressType -> (string)

The type of IP address.

ipResource -> (structure)

The IP resource.

ipAddress -> (string)

The IP address of the IP resource.

Shorthand Syntax:

```
arnResource={arn=string},dnsResource={domainName=string,ipAddressType=string},ipResource={ipAddress=string}
```

JSON Syntax:

```
{
  "arnResource": {
    "arn": "string"
  },
  "dnsResource": {
    "domainName": "string",
    "ipAddressType": "IPV4"|"IPV6"|"DUALSTACK"
  },
  "ipResource": {
    "ipAddress": "string"
  }
}
```

`--resource-configuration-group-identifier` (string)

(CHILD) The ID or ARN of the parent resource configuration (type is `GROUP` ). This is used to associate a child resource configuration with a group resource configuration.

`--resource-gateway-identifier` (string)

(SINGLE, GROUP, ARN) The ID or ARN of the resource gateway used to connect to the resource configuration. For a child resource configuration, this value is inherited from the parent resource configuration.

`--tags` (map)

The tags for the resource configuration.

key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 128 Unicode characters. Valid characters are Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @ May not begin with `aws:` .

value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters. Valid characters are Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--type` (string)

The type of resource configuration.

- `SINGLE` - A single resource.
- `GROUP` - A group of resources. You must create a group resource configuration before you create a child resource configuration.
- `CHILD` - A single resource that is part of a group resource configuration.
- `ARN` - An Amazon Web Services resource.

Possible values:

- `GROUP`
- `CHILD`
- `SINGLE`
- `ARN`

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

**To create a resource configuration**

The following `create-resource-configuration` example creates a resource configuration that specifies a single IPv4 address.

```
aws vpc-lattice create-resource-configuration \
    --name my-resource-config \
    --type SINGLE \
    --resource-gateway-identifier rgw-0bba03f3d56060135 \
    --resource-configuration-definition 'ipResource={ipAddress=10.0.14.85}'
```

Output:

```
{
    "allowAssociationToShareableServiceNetwork": true,
    "arn": "arn:aws:vpc-lattice:us-east-1:123456789012:resourceconfiguration/rcfg-07129f3acded87625",
    "id": "rcfg-07129f3acded87625",
    "name": "my-resource-config",
    "portRanges": [
        "1-65535"
    ],
    "protocol": "TCP",
    "resourceConfigurationDefinition": {
        "ipResource": {
            "ipAddress": "10.0.14.85"
        }
    },
    "resourceGatewayId": "rgw-0bba03f3d56060135",
    "status": "ACTIVE",
    "type": "SINGLE"
}
```

For more information, see [Resource configurations for VPC resources](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-configuration.html) in the *Amazon VPC Lattice User Guide*.

## Output

allowAssociationToShareableServiceNetwork -> (boolean)

Specifies whether the resource configuration can be associated with a sharable service network.

arn -> (string)

The Amazon Resource Name (ARN) of the resource configuration.

createdAt -> (timestamp)

The date and time that the resource configuration was created, in ISO-8601 format.

failureReason -> (string)

The reason that the request failed.

id -> (string)

The ID of the resource configuration.

name -> (string)

The name of the resource configuration.

portRanges -> (list)

The port range.

(string)

protocol -> (string)

The protocol.

resourceConfigurationDefinition -> (tagged union structure)

The resource configuration.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `arnResource`, `dnsResource`, `ipResource`.

arnResource -> (structure)

The Amazon Resource Name (ARN) of the resource.

arn -> (string)

The Amazon Resource Name (ARN) of the resource.

dnsResource -> (structure)

The DNS name of the resource.

domainName -> (string)

The domain name of the resource.

ipAddressType -> (string)

The type of IP address.

ipResource -> (structure)

The IP resource.

ipAddress -> (string)

The IP address of the IP resource.

resourceConfigurationGroupId -> (string)

The ID of the parent resource configuration (type is GROUP).

resourceGatewayId -> (string)

The ID of the resource gateway associated with the resource configuration.

status -> (string)

The current status of the resource configuration.

type -> (string)

The type of resource configuration.