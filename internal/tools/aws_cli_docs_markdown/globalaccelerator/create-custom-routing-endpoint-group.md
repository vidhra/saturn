# create-custom-routing-endpoint-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-custom-routing-endpoint-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-custom-routing-endpoint-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [globalaccelerator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/index.html#cli-aws-globalaccelerator) ]

# create-custom-routing-endpoint-group

## Description

Create an endpoint group for the specified listener for a custom routing accelerator. An endpoint group is a collection of endpoints in one Amazon Web Services Region.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/CreateCustomRoutingEndpointGroup)

## Synopsis

```
create-custom-routing-endpoint-group
--listener-arn <value>
--endpoint-group-region <value>
--destination-configurations <value>
[--idempotency-token <value>]
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

`--listener-arn` (string)

The Amazon Resource Name (ARN) of the listener for a custom routing endpoint.

`--endpoint-group-region` (string)

The Amazon Web Services Region where the endpoint group is located. A listener can have only one endpoint group in a specific Region.

`--destination-configurations` (list)

Sets the port range and protocol for all endpoints (virtual private cloud subnets) in a custom routing endpoint group to accept client traffic on.

(structure)

For a custom routing accelerator, sets the port range and protocol for all endpoints (virtual private cloud subnets) in an endpoint group to accept client traffic on.

FromPort -> (integer)

The first port, inclusive, in the range of ports for the endpoint group that is associated with a custom routing accelerator.

ToPort -> (integer)

The last port, inclusive, in the range of ports for the endpoint group that is associated with a custom routing accelerator.

Protocols -> (list)

The protocol for the endpoint group that is associated with a custom routing accelerator. The protocol can be either TCP or UDP.

(string)

Shorthand Syntax:

```
FromPort=integer,ToPort=integer,Protocols=string,string ...
```

JSON Syntax:

```
[
  {
    "FromPort": integer,
    "ToPort": integer,
    "Protocols": ["TCP"|"UDP", ...]
  }
  ...
]
```

`--idempotency-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotencyâthat is, the uniquenessâof the request.

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

**To create an endpoint group for a custom routing accelerator**

The following `create-custom-routing-endpoint-group` example creates an endpoint group for a custom routing accelerator.

```
aws globalaccelerator create-custom-routing-endpoint-group \
    --listener-arn arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz \
    --endpoint-group-region us-east-2 \
    --destination-configurations "FromPort=80,ToPort=81,Protocols=TCP,UDP"
```

Output:

```
{
    "EndpointGroup": {
        "EndpointGroupArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz/endpoint-group/4321abcd",
        "EndpointGroupRegion": "us-east-2",
        "DestinationDescriptions": [
            {
                "FromPort": 80,
                "ToPort": 81,
                "Protocols": [
                    "TCP",
                    "UDP"
                ]
            }
        ],
        "EndpointDescriptions": []
    }
}
```

For more information, see [Endpoint groups for custom routing accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoint-groups.html) in the *AWS Global Accelerator Developer Guide*.

## Output

EndpointGroup -> (structure)

The information about the endpoint group created for a custom routing accelerator.

EndpointGroupArn -> (string)

The Amazon Resource Name (ARN) of the endpoint group.

EndpointGroupRegion -> (string)

The Amazon Web Services Region where the endpoint group is located.

DestinationDescriptions -> (list)

For a custom routing accelerator, describes the port range and protocol for all endpoints (virtual private cloud subnets) in an endpoint group to accept client traffic on.

(structure)

For a custom routing accelerator, describes the port range and protocol for all endpoints (virtual private cloud subnets) in an endpoint group to accept client traffic on.

FromPort -> (integer)

The first port, inclusive, in the range of ports for the endpoint group that is associated with a custom routing accelerator.

ToPort -> (integer)

The last port, inclusive, in the range of ports for the endpoint group that is associated with a custom routing accelerator.

Protocols -> (list)

The protocol for the endpoint group that is associated with a custom routing accelerator. The protocol can be either TCP or UDP.

(string)

EndpointDescriptions -> (list)

For a custom routing accelerator, describes the endpoints (virtual private cloud subnets) in an endpoint group to accept client traffic on.

(structure)

A complex type for an endpoint for a custom routing accelerator. Each endpoint group can include one or more endpoints, which are virtual private cloud (VPC) subnets.

EndpointId -> (string)

An ID for the endpoint. For custom routing accelerators, this is the virtual private cloud (VPC) subnet ID.