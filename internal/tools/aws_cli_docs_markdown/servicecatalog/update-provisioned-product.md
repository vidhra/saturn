# update-provisioned-productÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-provisioned-product.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-provisioned-product.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicecatalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/index.html#cli-aws-servicecatalog) ]

# update-provisioned-product

## Description

Requests updates to the configuration of the specified provisioned product.

If there are tags associated with the object, they cannot be updated or added. Depending on the specific updates requested, this operation can update with no interruption, with some interruption, or replace the provisioned product entirely.

You can check the status of this request using  DescribeRecord .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/UpdateProvisionedProduct)

## Synopsis

```
update-provisioned-product
[--accept-language <value>]
[--provisioned-product-name <value>]
[--provisioned-product-id <value>]
[--product-id <value>]
[--product-name <value>]
[--provisioning-artifact-id <value>]
[--provisioning-artifact-name <value>]
[--path-id <value>]
[--path-name <value>]
[--provisioning-parameters <value>]
[--provisioning-preferences <value>]
[--tags <value>]
[--update-token <value>]
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

`--provisioned-product-name` (string)

The name of the provisioned product. You cannot specify both `ProvisionedProductName` and `ProvisionedProductId` .

`--provisioned-product-id` (string)

The identifier of the provisioned product. You must provide the name or ID, but not both.

`--product-id` (string)

The identifier of the product. You must provide the name or ID, but not both.

`--product-name` (string)

The name of the product. You must provide the name or ID, but not both.

`--provisioning-artifact-id` (string)

The identifier of the provisioning artifact.

`--provisioning-artifact-name` (string)

The name of the provisioning artifact. You must provide the name or ID, but not both.

`--path-id` (string)

The path identifier. This value is optional if the product has a default path, and required if the product has more than one path. You must provide the name or ID, but not both.

`--path-name` (string)

The name of the path. You must provide the name or ID, but not both.

`--provisioning-parameters` (list)

The new parameters.

(structure)

The parameter key-value pair used to update a provisioned product.

Key -> (string)

The parameter key.

Value -> (string)

The parameter value.

UsePreviousValue -> (boolean)

If set to true, `Value` is ignored and the previous parameter value is kept.

Shorthand Syntax:

```
Key=string,Value=string,UsePreviousValue=boolean ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string",
    "UsePreviousValue": true|false
  }
  ...
]
```

`--provisioning-preferences` (structure)

An object that contains information about the provisioning preferences for a stack set.

StackSetAccounts -> (list)

One or more Amazon Web Services accounts that will have access to the provisioned product.

Applicable only to a `CFN_STACKSET` provisioned product type.

The Amazon Web Services accounts specified should be within the list of accounts in the `STACKSET` constraint. To get the list of accounts in the `STACKSET` constraint, use the `DescribeProvisioningParameters` operation.

If no values are specified, the default value is all accounts from the `STACKSET` constraint.

(string)

StackSetRegions -> (list)

One or more Amazon Web Services Regions where the provisioned product will be available.

Applicable only to a `CFN_STACKSET` provisioned product type.

The specified Regions should be within the list of Regions from the `STACKSET` constraint. To get the list of Regions in the `STACKSET` constraint, use the `DescribeProvisioningParameters` operation.

If no values are specified, the default value is all Regions from the `STACKSET` constraint.

(string)

StackSetFailureToleranceCount -> (integer)

The number of accounts, per Region, for which this operation can fail before Service Catalog stops the operation in that Region. If the operation is stopped in a Region, Service Catalog doesnât attempt the operation in any subsequent Regions.

Applicable only to a `CFN_STACKSET` provisioned product type.

Conditional: You must specify either `StackSetFailureToleranceCount` or `StackSetFailureTolerancePercentage` , but not both.

The default value is `0` if no value is specified.

StackSetFailureTolerancePercentage -> (integer)

The percentage of accounts, per Region, for which this stack operation can fail before Service Catalog stops the operation in that Region. If the operation is stopped in a Region, Service Catalog doesnât attempt the operation in any subsequent Regions.

When calculating the number of accounts based on the specified percentage, Service Catalog rounds down to the next whole number.

Applicable only to a `CFN_STACKSET` provisioned product type.

Conditional: You must specify either `StackSetFailureToleranceCount` or `StackSetFailureTolerancePercentage` , but not both.

StackSetMaxConcurrencyCount -> (integer)

The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of `StackSetFailureToleranceCount` . `StackSetMaxConcurrentCount` is at most one more than the `StackSetFailureToleranceCount` .

Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.

Applicable only to a `CFN_STACKSET` provisioned product type.

Conditional: You must specify either `StackSetMaxConcurrentCount` or `StackSetMaxConcurrentPercentage` , but not both.

StackSetMaxConcurrencyPercentage -> (integer)

The maximum percentage of accounts in which to perform this operation at one time.

When calculating the number of accounts based on the specified percentage, Service Catalog rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, Service Catalog sets the number as `1` instead.

Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.

Applicable only to a `CFN_STACKSET` provisioned product type.

Conditional: You must specify either `StackSetMaxConcurrentCount` or `StackSetMaxConcurrentPercentage` , but not both.

StackSetOperationType -> (string)

Determines what action Service Catalog performs to a stack set or a stack instance represented by the provisioned product. The default value is `UPDATE` if nothing is specified.

Applicable only to a `CFN_STACKSET` provisioned product type.

CREATE

Creates a new stack instance in the stack set represented by the provisioned product. In this case, only new stack instances are created based on accounts and Regions; if new ProductId or ProvisioningArtifactID are passed, they will be ignored.

UPDATE

Updates the stack set represented by the provisioned product and also its stack instances.

DELETE

Deletes a stack instance in the stack set represented by the provisioned product.

Shorthand Syntax:

```
StackSetAccounts=string,string,StackSetRegions=string,string,StackSetFailureToleranceCount=integer,StackSetFailureTolerancePercentage=integer,StackSetMaxConcurrencyCount=integer,StackSetMaxConcurrencyPercentage=integer,StackSetOperationType=string
```

JSON Syntax:

```
{
  "StackSetAccounts": ["string", ...],
  "StackSetRegions": ["string", ...],
  "StackSetFailureToleranceCount": integer,
  "StackSetFailureTolerancePercentage": integer,
  "StackSetMaxConcurrencyCount": integer,
  "StackSetMaxConcurrencyPercentage": integer,
  "StackSetOperationType": "CREATE"|"UPDATE"|"DELETE"
}
```

`--tags` (list)

One or more tags. Requires the product to have `RESOURCE_UPDATE` constraint with `TagUpdatesOnProvisionedProduct` set to `ALLOWED` to allow tag updates.

(structure)

Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.

Key -> (string)

The tag key.

Value -> (string)

The value for this key.

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

`--update-token` (string)

The idempotency token that uniquely identifies the provisioning update request.

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

Information about the result of the request.

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