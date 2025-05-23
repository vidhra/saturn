# search-provisioned-productsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/search-provisioned-products.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/search-provisioned-products.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicecatalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/index.html#cli-aws-servicecatalog) ]

# search-provisioned-products

## Description

Gets information about the provisioned products that meet the specified criteria.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/SearchProvisionedProducts)

## Synopsis

```
search-provisioned-products
[--accept-language <value>]
[--access-level-filter <value>]
[--filters <value>]
[--sort-by <value>]
[--sort-order <value>]
[--page-size <value>]
[--page-token <value>]
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

`--access-level-filter` (structure)

The access level to use to obtain results. The default is `Account` .

Key -> (string)

The access level.

- `Account` - Filter results based on the account.
- `Role` - Filter results based on the federated role of the specified user.
- `User` - Filter results based on the specified user.

Value -> (string)

The user to which the access level applies. The only supported value is `self` .

Shorthand Syntax:

```
Key=string,Value=string
```

JSON Syntax:

```
{
  "Key": "Account"|"Role"|"User",
  "Value": "string"
}
```

`--filters` (map)

The search filters.

When the key is `SearchQuery` , the searchable fields are `arn` , `createdTime` , `id` , `lastRecordId` , `idempotencyToken` , `name` , `physicalId` , `productId` , `provisioningArtifactId` , `type` , `status` , `tags` , `userArn` , `userArnSession` , `lastProvisioningRecordId` , `lastSuccessfulProvisioningRecordId` , `productName` , and `provisioningArtifactName` .

Example: `"SearchQuery":["status:AVAILABLE"]`

key -> (string)

value -> (list)

(string)

Shorthand Syntax:

```
KeyName1=string,string,KeyName2=string,string

Where valid key names are:
  SearchQuery
```

JSON Syntax:

```
{"SearchQuery": ["string", ...]
  ...}
```

`--sort-by` (string)

The sort field. If no value is specified, the results are not sorted. The valid values are `arn` , `id` , `name` , and `lastRecordId` .

`--sort-order` (string)

The sort order. If no value is specified, the results are not sorted.

Possible values:

- `ASCENDING`
- `DESCENDING`

`--page-size` (integer)

The maximum number of items to return with this call.

`--page-token` (string)

The page token for the next set of results. To retrieve the first set of results, use null.

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

**To search provisioned products**

The following `search-provisioned-products` example searches for provisioned products matching the specified product ID, using a JSON file to pass parameters.

```
aws servicecatalog search-provisioned-products \
    --cli-input-json file://search-provisioned-products-input.json
```

Contents of `search-provisioned-products-input.json`:

```
{
    "Filters": {
        "SearchQuery": [
            "prod-tcjvfz3syn2rg"
        ]
    }
}
```

Output:

```
{
    "ProvisionedProducts": [
        {
            "ProvisioningArtifactId": "pa-pcz347abcdcfm",
            "Name": "mytestppname3",
            "CreatedTime": 1577222793.358,
            "Id": "pp-abcd27bm4mldq",
            "Status": "ERROR",
            "UserArn": "arn:aws:iam::123456789012:user/cliuser",
            "StatusMessage": "AmazonCloudFormationException  Parameters: [KeyName] must have values (Service: AmazonCloudFormation; Status Code: 400; Error Code: ValidationError; Request ID: 5528602a-a9ef-427c-825c-f82c31b814f5)",
            "Arn": "arn:aws:servicecatalog:us-west-2:123456789012:stack/mytestppname3/pp-abcd27bm4mldq",
            "Tags": [
                {
                    "Value": "arn:aws:catalog:us-west-2:123456789012:product/prod-abcdfz3syn2rg",
                    "Key": "aws:servicecatalog:productArn"
                },
                {
                    "Value": "arn:aws:iam::123456789012:user/cliuser",
                    "Key": "aws:servicecatalog:provisioningPrincipalArn"
                },
                {
                    "Value": "value-3",
                    "Key": "1234"
                },
                {
                    "Value": "pa-pcz347abcdcfm",
                    "Key": "aws:servicecatalog:provisioningArtifactIdentifier"
                },
                {
                    "Value": "arn:aws:catalog:us-west-2:123456789012:portfolio/port-2s6abcdq5wdh4",
                    "Key": "aws:servicecatalog:portfolioArn"
                },
                {
                    "Value": "arn:aws:servicecatalog:us-west-2:123456789012:stack/mytestppname3/pp-abcd27bm4mldq",
                    "Key": "aws:servicecatalog:provisionedProductArn"
                }
            ],
            "IdempotencyToken": "527c5358-2a1a-4b9e-b1b9-7293b0ddff42",
            "UserArnSession": "arn:aws:iam::123456789012:user/cliuser",
            "Type": "CFN_STACK",
            "LastRecordId": "rec-tfuawdabcdxge",
            "ProductId": "prod-abcdfz3syn2rg"
        }
    ],
    "TotalResultsCount": 1
}
```

## Output

ProvisionedProducts -> (list)

Information about the provisioned products.

(structure)

Information about a provisioned product.

Name -> (string)

The user-friendly name of the provisioned product.

Arn -> (string)

The ARN of the provisioned product.

Type -> (string)

The type of provisioned product. The supported values are `CFN_STACK` , `CFN_STACKSET` , `TERRAFORM_OPEN_SOURCE` , `TERRAFORM_CLOUD` , and `EXTERNAL` .

Id -> (string)

The identifier of the provisioned product.

Status -> (string)

The current status of the provisioned product.

- `AVAILABLE` - Stable state, ready to perform any operation. The most recent operation succeeded and completed.
- `UNDER_CHANGE` - Transitive state. Operations performed might not have valid results. Wait for an `AVAILABLE` status before performing operations.
- `TAINTED` - Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version.
- `ERROR` - An unexpected error occurred. The provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack.
- `PLAN_IN_PROGRESS` - Transitive state. The plan operations were performed to provision a new product, but resources have not yet been created. After reviewing the list of resources to be created, execute the plan. Wait for an `AVAILABLE` status before performing operations.

StatusMessage -> (string)

The current status message of the provisioned product.

CreatedTime -> (timestamp)

The UTC time stamp of the creation time.

IdempotencyToken -> (string)

A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.

LastRecordId -> (string)

The record identifier of the last request performed on this provisioned product.

LastProvisioningRecordId -> (string)

The record identifier of the last request performed on this provisioned product of the following types:

- ProvisionProduct
- UpdateProvisionedProduct
- ExecuteProvisionedProductPlan
- TerminateProvisionedProduct

LastSuccessfulProvisioningRecordId -> (string)

The record identifier of the last successful request performed on this provisioned product of the following types:

- ProvisionProduct
- UpdateProvisionedProduct
- ExecuteProvisionedProductPlan
- TerminateProvisionedProduct

Tags -> (list)

One or more tags.

(structure)

Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.

Key -> (string)

The tag key.

Value -> (string)

The value for this key.

PhysicalId -> (string)

The assigned identifier for the resource, such as an EC2 instance ID or an S3 bucket name.

ProductId -> (string)

The product identifier.

ProductName -> (string)

The name of the product.

ProvisioningArtifactId -> (string)

The identifier of the provisioning artifact.

ProvisioningArtifactName -> (string)

The name of the provisioning artifact.

UserArn -> (string)

The Amazon Resource Name (ARN) of the user.

UserArnSession -> (string)

The ARN of the user in the session. This ARN might contain a session ID.

TotalResultsCount -> (integer)

The number of provisioned products found.

NextPageToken -> (string)

The page token to use to retrieve the next set of results. If there are no additional results, this value is null.