# import-as-provisioned-productÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/import-as-provisioned-product.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/import-as-provisioned-product.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicecatalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/index.html#cli-aws-servicecatalog) ]

# import-as-provisioned-product

## Description

Requests the import of a resource as an Service Catalog provisioned product that is associated to an Service Catalog product and provisioning artifact. Once imported, all supported governance actions are supported on the provisioned product.

Resource import only supports CloudFormation stack ARNs. CloudFormation StackSets, and non-root nested stacks, are not supported.

The CloudFormation stack must have one of the following statuses to be imported: `CREATE_COMPLETE` , `UPDATE_COMPLETE` , `UPDATE_ROLLBACK_COMPLETE` , `IMPORT_COMPLETE` , and `IMPORT_ROLLBACK_COMPLETE` .

Import of the resource requires that the CloudFormation stack template matches the associated Service Catalog product provisioning artifact.

### Note

When you import an existing CloudFormation stack into a portfolio, Service Catalog does not apply the productâs associated constraints during the import process. Service Catalog applies the constraints after you call `UpdateProvisionedProduct` for the provisioned product.

The user or role that performs this operation must have the `cloudformation:GetTemplate` and `cloudformation:DescribeStacks` IAM policy permissions.

You can only import one provisioned product at a time. The productâs CloudFormation stack must have the `IMPORT_COMPLETE` status before you import another.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ImportAsProvisionedProduct)

## Synopsis

```
import-as-provisioned-product
[--accept-language <value>]
--product-id <value>
--provisioning-artifact-id <value>
--provisioned-product-name <value>
--physical-id <value>
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

`--product-id` (string)

The product identifier.

`--provisioning-artifact-id` (string)

The identifier of the provisioning artifact.

`--provisioned-product-name` (string)

The user-friendly name of the provisioned product. The value must be unique for the Amazon Web Services account. The name cannot be updated after the product is provisioned.

`--physical-id` (string)

The unique identifier of the resource to be imported. It only currently supports CloudFormation stack IDs.

`--idempotency-token` (string)

A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.

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

RecordDetail -> (structure)

Information about a request operation.

RecordId -> (string)

The identifier of the record.

ProvisionedProductName -> (string)

The user-friendly name of the provisioned product.

Status -> (string)

The status of the provisioned product.

- `CREATED` - The request was created but the operation has not started.
- `IN_PROGRESS` - The requested operation is in progress.
- `IN_PROGRESS_IN_ERROR` - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback.
- `SUCCEEDED` - The requested operation has successfully completed.
- `FAILED` - The requested operation has unsuccessfully completed. Investigate using the error messages returned.

CreatedTime -> (timestamp)

The UTC time stamp of the creation time.

UpdatedTime -> (timestamp)

The time when the record was last updated.

ProvisionedProductType -> (string)

The type of provisioned product. The supported values are `CFN_STACK` , `CFN_STACKSET` , `TERRAFORM_OPEN_SOURCE` , `TERRAFORM_CLOUD` , and `EXTERNAL` .

RecordType -> (string)

The record type.

- `PROVISION_PRODUCT`
- `UPDATE_PROVISIONED_PRODUCT`
- `TERMINATE_PROVISIONED_PRODUCT`

ProvisionedProductId -> (string)

The identifier of the provisioned product.

ProductId -> (string)

The product identifier.

ProvisioningArtifactId -> (string)

The identifier of the provisioning artifact.

PathId -> (string)

The path identifier.

RecordErrors -> (list)

The errors that occurred.

(structure)

The error code and description resulting from an operation.

Code -> (string)

The numeric value of the error.

Description -> (string)

The description of the error.

RecordTags -> (list)

One or more tags.

(structure)

Information about a tag, which is a key-value pair.

Key -> (string)

The key for this tag.

Value -> (string)

The value for this tag.

LaunchRoleArn -> (string)

The ARN of the launch role associated with the provisioned product.