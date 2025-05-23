# provision-productÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/provision-product.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/provision-product.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicecatalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/index.html#cli-aws-servicecatalog) ]

# provision-product

## Description

Provisions the specified product.

A provisioned product is a resourced instance of a product. For example, provisioning a product thatâs based on an CloudFormation template launches an CloudFormation stack and its underlying resources. You can check the status of this request using  DescribeRecord .

If the request contains a tag key with an empty list of values, thereâs a tag conflict for that key. Donât include conflicted keys as tags, or this will cause the error âParameter validation failed: Missing required parameter in Tags[*N* ]:*Value* â.

### Note

When provisioning a product thatâs been added to a portfolio, you must grant your user, group, or role access to the portfolio. For more information, see [Granting users access](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_users.html) in the *Service Catalog User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ProvisionProduct)

## Synopsis

```
provision-product
[--accept-language <value>]
[--product-id <value>]
[--product-name <value>]
[--provisioning-artifact-id <value>]
[--provisioning-artifact-name <value>]
[--path-id <value>]
[--path-name <value>]
--provisioned-product-name <value>
[--provisioning-parameters <value>]
[--provisioning-preferences <value>]
[--tags <value>]
[--notification-arns <value>]
[--provision-token <value>]
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

The product identifier. You must provide the name or ID, but not both.

`--product-name` (string)

The name of the product. You must provide the name or ID, but not both.

`--provisioning-artifact-id` (string)

The identifier of the provisioning artifact. You must provide the name or ID, but not both.

`--provisioning-artifact-name` (string)

The name of the provisioning artifact. You must provide the name or ID, but not both.

`--path-id` (string)

The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use  ListLaunchPaths . You must provide the name or ID, but not both.

`--path-name` (string)

The name of the path. You must provide the name or ID, but not both.

`--provisioned-product-name` (string)

A user-friendly name for the provisioned product. This value must be unique for the Amazon Web Services account and cannot be updated after the product is provisioned.

`--provisioning-parameters` (list)

Parameters specified by the administrator that are required for provisioning the product.

(structure)

Information about a parameter used to provision a product.

Key -> (string)

The parameter key.

Value -> (string)

The parameter value.

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

`--provisioning-preferences` (structure)

An object that contains information about the provisioning preferences for a stack set.

StackSetAccounts -> (list)

One or more Amazon Web Services accounts where the provisioned product will be available.

Applicable only to a `CFN_STACKSET` provisioned product type.

The specified accounts should be within the list of accounts from the `STACKSET` constraint. To get the list of accounts in the `STACKSET` constraint, use the `DescribeProvisioningParameters` operation.

If no values are specified, the default value is all acounts from the `STACKSET` constraint.

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

Shorthand Syntax:

```
StackSetAccounts=string,string,StackSetRegions=string,string,StackSetFailureToleranceCount=integer,StackSetFailureTolerancePercentage=integer,StackSetMaxConcurrencyCount=integer,StackSetMaxConcurrencyPercentage=integer
```

JSON Syntax:

```
{
  "StackSetAccounts": ["string", ...],
  "StackSetRegions": ["string", ...],
  "StackSetFailureToleranceCount": integer,
  "StackSetFailureTolerancePercentage": integer,
  "StackSetMaxConcurrencyCount": integer,
  "StackSetMaxConcurrencyPercentage": integer
}
```

`--tags` (list)

One or more tags.

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

`--notification-arns` (list)

Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.

(string)

Syntax:

```
"string" "string" ...
```

`--provision-token` (string)

An idempotency token that uniquely identifies the provisioning request.

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

**To provision a product**

The following `provision-product` example provisions the specified product using the specified provisioning artifact.

```
aws servicecatalog provision-product \
    --product-id prod-abcdfz3syn2rg \
    --provisioning-artifact-id pa-abc347pcsccfm \
    --provisioned-product-name "mytestppname3"
```

Output:

```
{
    "RecordDetail": {
        "RecordId": "rec-tfuawdabcdege",
        "CreatedTime": 1577222793.362,
        "ProvisionedProductId": "pp-abcd27bm4mldq",
        "PathId": "lpv2-abcdg3jp6t5k6",
        "RecordErrors": [],
        "ProductId": "prod-abcdfz3syn2rg",
        "UpdatedTime": 1577222793.362,
        "RecordType": "PROVISION_PRODUCT",
        "ProvisionedProductName": "mytestppname3",
        "ProvisioningArtifactId": "pa-pcz347abcdcfm",
        "RecordTags": [],
        "Status": "CREATED",
        "ProvisionedProductType": "CFN_STACK"
    }
}
```

## Output

RecordDetail -> (structure)

Information about the result of provisioning the product.

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