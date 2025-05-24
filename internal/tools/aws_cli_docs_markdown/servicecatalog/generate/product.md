# productÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/generate/product.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/generate/product.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicecatalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/index.html#cli-aws-servicecatalog) . [generate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/generate/index.html#cli-aws-servicecatalog-generate) ]

# product

## Description

Create a new product using a CloudFormation template specified as a local file path

## Synopsis

```
product
--product-name <value>
--product-owner <value>
--product-type <value>
[--product-description <value>]
[--product-distributor <value>]
[--tags Key=key1,Value=value1 Key=key2,Value=value2]
--file-path <value>
--bucket-name <value>
[--support-description <value>]
[--support-email <value>]
--provisioning-artifact-name <value>
--provisioning-artifact-description <value>
--provisioning-artifact-type <value>
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

`--product-name` (string)
The name of the product

`--product-owner` (string)
The owner of the product

`--product-type` (string)
The type of the product to create

`--product-description` (string)
The text description of the product

`--product-distributor` (string)
The distributor of the product

`--tags` (list)
Tags to associate with the new product.(string)

Syntax:

```
"string" "string" ...
```

`--file-path` (string)
A local file path that references the CloudFormation template

`--bucket-name` (string)
Name of the S3 bucket name where the CloudFormation template will be uploaded to

`--support-description` (string)
Support information about the product

`--support-email` (string)
Contact email for product support

`--provisioning-artifact-name` (string)
The name assigned to the provisioning artifact

`--provisioning-artifact-description` (string)
The text description of the provisioning artifact

`--provisioning-artifact-type` (string)
The type of the provisioning artifact

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