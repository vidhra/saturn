# update-provisioned-product-propertiesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-provisioned-product-properties.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-provisioned-product-properties.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicecatalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/index.html#cli-aws-servicecatalog) ]

# update-provisioned-product-properties

## Description

Requests updates to the properties of the specified provisioned product.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/UpdateProvisionedProductProperties)

## Synopsis

```
update-provisioned-product-properties
[--accept-language <value>]
--provisioned-product-id <value>
--provisioned-product-properties <value>
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

`--accept-language` (string)

The language code.

- `jp` - Japanese
- `zh` - Chinese

`--provisioned-product-id` (string)

The identifier of the provisioned product.

`--provisioned-product-properties` (map)

A map that contains the provisioned product properties to be updated.

The `LAUNCH_ROLE` key accepts role ARNs. This key allows an administrator to call `UpdateProvisionedProductProperties` to update the launch role that is associated with a provisioned product. This role is used when an end user calls a provisioning operation such as `UpdateProvisionedProduct` , `TerminateProvisionedProduct` , or `ExecuteProvisionedProductServiceAction` . Only a role ARN is valid. A user ARN is invalid.

The `OWNER` key accepts user ARNs, IAM role ARNs, and STS assumed-role ARNs. The owner is the user that has permission to see, update, terminate, and execute service actions in the provisioned product.

The administrator can change the owner of a provisioned product to another IAM or STS entity within the same account. Both end user owners and administrators can see ownership history of the provisioned product using the `ListRecordHistory` API. The new owner can describe all past records for the provisioned product using the `DescribeRecord` API. The previous owner can no longer use `DescribeRecord` , but can still see the productâs history from when he was an owner using `ListRecordHistory` .

If a provisioned product ownership is assigned to an end user, they can see and perform any action through the API or Service Catalog console such as update, terminate, and execute service actions. If an end user provisions a product and the owner is updated to someone else, they will no longer be able to see or perform any actions through API or the Service Catalog console on that provisioned product.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string

Where valid key names are:
  OWNER
  LAUNCH_ROLE
```

JSON Syntax:

```
{"OWNER"|"LAUNCH_ROLE": "string"
  ...}
```

`--idempotency-token` (string)

The idempotency token that uniquely identifies the provisioning product update request.

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

ProvisionedProductId -> (string)

The provisioned product identifier.

ProvisionedProductProperties -> (map)

A map that contains the properties updated.

key -> (string)

value -> (string)

RecordId -> (string)

The identifier of the record.

Status -> (string)

The status of the request.