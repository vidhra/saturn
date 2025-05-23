# create-cross-account-attachmentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-cross-account-attachment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-cross-account-attachment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [globalaccelerator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/index.html#cli-aws-globalaccelerator) ]

# create-cross-account-attachment

## Description

Create a cross-account attachment in Global Accelerator. You create a cross-account attachment to specify the *principals* who have permission to work with *resources* in accelerators in their own account. You specify, in the same attachment, the resources that are shared.

A principal can be an Amazon Web Services account number or the Amazon Resource Name (ARN) for an accelerator. For account numbers that are listed as principals, to work with a resource listed in the attachment, you must sign in to an account specified as a principal. Then, you can work with resources that are listed, with any of your accelerators. If an accelerator ARN is listed in the cross-account attachment as a principal, anyone with permission to make updates to the accelerator can work with resources that are listed in the attachment.

Specify each principal and resource separately. To specify two CIDR address pools, list them individually under `Resources` , and so on. For a command line operation, for example, you might use a statement like the following:

`"Resources": [{"Cidr": "169.254.60.0/24"},{"Cidr": "169.254.59.0/24"}]`

For more information, see [Working with cross-account attachments and resources in Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.html) in the *Global Accelerator Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/CreateCrossAccountAttachment)

## Synopsis

```
create-cross-account-attachment
--name <value>
[--principals <value>]
[--resources <value>]
[--idempotency-token <value>]
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

`--name` (string)

The name of the cross-account attachment.

`--principals` (list)

The principals to include in the cross-account attachment. A principal can be an Amazon Web Services account number or the Amazon Resource Name (ARN) for an accelerator.

(string)

Syntax:

```
"string" "string" ...
```

`--resources` (list)

The Amazon Resource Names (ARNs) for the resources to include in the cross-account attachment. A resource can be any supported Amazon Web Services resource type for Global Accelerator or a CIDR range for a bring your own IP address (BYOIP) address pool.

(structure)

A resource is one of the following: the ARN for an Amazon Web Services resource that is supported by Global Accelerator to be added as an endpoint, or a CIDR range that specifies a bring your own IP (BYOIP) address pool.

EndpointId -> (string)

The endpoint ID for the endpoint that is specified as a Amazon Web Services resource.

An endpoint ID for the cross-account feature is the ARN of an Amazon Web Services resource, such as a Network Load Balancer, that Global Accelerator supports as an endpoint for an accelerator.

Cidr -> (string)

An IP address range, in CIDR format, that is specified as resource. The address must be provisioned and advertised in Global Accelerator by following the bring your own IP address (BYOIP) process for Global Accelerator

For more information, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html) in the Global Accelerator Developer Guide.

Region -> (string)

The Amazon Web Services Region where a shared endpoint resource is located.

Shorthand Syntax:

```
EndpointId=string,Cidr=string,Region=string ...
```

JSON Syntax:

```
[
  {
    "EndpointId": "string",
    "Cidr": "string",
    "Region": "string"
  }
  ...
]
```

`--idempotency-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotencyâthat is, the uniquenessâof the request.

`--tags` (list)

Add tags for a cross-account attachment.

For more information, see [Tagging in Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html) in the *Global Accelerator Developer Guide* .

(structure)

A complex type that contains a `Tag` key and `Tag` value.

Key -> (string)

A string that contains a `Tag` key.

Value -> (string)

A string that contains a `Tag` value.

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

CrossAccountAttachment -> (structure)

Information about the cross-account attachment.

AttachmentArn -> (string)

The Amazon Resource Name (ARN) of the cross-account attachment.

Name -> (string)

The name of the cross-account attachment.

Principals -> (list)

The principals included in the cross-account attachment.

(string)

Resources -> (list)

The resources included in the cross-account attachment.

(structure)

A resource is one of the following: the ARN for an Amazon Web Services resource that is supported by Global Accelerator to be added as an endpoint, or a CIDR range that specifies a bring your own IP (BYOIP) address pool.

EndpointId -> (string)

The endpoint ID for the endpoint that is specified as a Amazon Web Services resource.

An endpoint ID for the cross-account feature is the ARN of an Amazon Web Services resource, such as a Network Load Balancer, that Global Accelerator supports as an endpoint for an accelerator.

Cidr -> (string)

An IP address range, in CIDR format, that is specified as resource. The address must be provisioned and advertised in Global Accelerator by following the bring your own IP address (BYOIP) process for Global Accelerator

For more information, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html) in the Global Accelerator Developer Guide.

Region -> (string)

The Amazon Web Services Region where a shared endpoint resource is located.

LastModifiedTime -> (timestamp)

The date and time that the cross-account attachment was last modified.

CreatedTime -> (timestamp)

The date and time that the cross-account attachment was created.