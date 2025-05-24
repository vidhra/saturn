# describe-product-as-adminÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-product-as-admin.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-product-as-admin.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicecatalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/index.html#cli-aws-servicecatalog) ]

# describe-product-as-admin

## Description

Gets information about the specified product. This operation is run with administrator access.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeProductAsAdmin)

## Synopsis

```
describe-product-as-admin
[--accept-language <value>]
[--id <value>]
[--name <value>]
[--source-portfolio-id <value>]
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

`--id` (string)

The product identifier.

`--name` (string)

The product name.

`--source-portfolio-id` (string)

The unique identifier of the shared portfolio that the specified product is associated with.

You can provide this parameter to retrieve the shared TagOptions associated with the product. If this parameter is provided and if TagOptions sharing is enabled in the portfolio share, the API returns both local and shared TagOptions associated with the product. Otherwise only local TagOptions will be returned.

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

**To describe a product as an administrator**

The following `describe-product-as-admin` example displays details for the specified product using administrator privileges.

```
aws servicecatalog describe-product-as-admin \
    --id prod-abcdcek6yhbxi
```

Output:

```
{
    "TagOptions": [],
    "ProductViewDetail": {
        "ProductARN": "arn:aws:catalog:us-west-2:687558542028:product/prod-abcdcek6yhbxi",
        "ProductViewSummary": {
            "SupportEmail": "test@amazon.com",
            "Type": "CLOUD_FORMATION_TEMPLATE",
            "Distributor": "test-distributor",
            "ShortDescription": "test-description",
            "Owner": "test-owner",
            "Id": "prodview-wi3l2j4abc6vc",
            "SupportDescription": "test-support",
            "ProductId": "prod-abcdcek6yhbxi",
            "HasDefaultPath": false,
            "Name": "test-product3",
            "SupportUrl": "https://aws.amazon.com"
        },
        "CreatedTime": 1577136715.0,
        "Status": "CREATED"
    },
    "ProvisioningArtifactSummaries": [
        {
            "CreatedTime": 1577136715.0,
            "Description": "test-version-description",
            "ProvisioningArtifactMetadata": {
                "SourceProvisioningArtifactId": "pa-abcdxkkiv5fcm"
            },
            "Name": "test-version-name-3",
            "Id": "pa-abcdxkkiv5fcm"
        }
    ],
    "Tags": [
        {
            "Value": "iad",
            "Key": "region"
        }
    ]
}
```

## Output

ProductViewDetail -> (structure)

Information about the product view.

ProductViewSummary -> (structure)

Summary information about the product view.

Id -> (string)

The product view identifier.

ProductId -> (string)

The product identifier.

Name -> (string)

The name of the product.

Owner -> (string)

The owner of the product. Contact the product administrator for the significance of this value.

ShortDescription -> (string)

Short description of the product.

Type -> (string)

The product type. Contact the product administrator for the significance of this value. If this value is `MARKETPLACE` , the product was created by Amazon Web Services Marketplace.

Distributor -> (string)

The distributor of the product. Contact the product administrator for the significance of this value.

HasDefaultPath -> (boolean)

Indicates whether the product has a default path. If the product does not have a default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is not required, and the output of  ProductViewSummary can be used directly with  DescribeProvisioningParameters .

SupportEmail -> (string)

The email contact information to obtain support for this Product.

SupportDescription -> (string)

The description of the support for this Product.

SupportUrl -> (string)

The URL information to obtain support for this Product.

Status -> (string)

The status of the product.

- `AVAILABLE` - The product is ready for use.
- `CREATING` - Product creation has started; the product is not ready for use.
- `FAILED` - An action failed.

ProductARN -> (string)

The ARN of the product.

CreatedTime -> (timestamp)

The UTC time stamp of the creation time.

SourceConnection -> (structure)

A top level `ProductViewDetail` response containing details about the productâs connection. Service Catalog returns this field for the `CreateProduct` , `UpdateProduct` , `DescribeProductAsAdmin` , and `SearchProductAsAdmin` APIs. This response contains the same fields as the `ConnectionParameters` request, with the addition of the `LastSync` response.

Type -> (string)

The only supported `SourceConnection` type is Codestar.

ConnectionParameters -> (structure)

The connection details based on the connection `Type` .

CodeStar -> (structure)

Provides `ConnectionType` details.

ConnectionArn -> (string)

The CodeStar ARN, which is the connection between Service Catalog and the external repository.

Repository -> (string)

The specific repository where the productâs artifact-to-be-synced resides, formatted as âAccount/Repo.â

Branch -> (string)

The specific branch where the artifact resides.

ArtifactPath -> (string)

The absolute path wehre the artifact resides within the repo and branch, formatted as âfolder/file.json.â

LastSync -> (structure)

Provides details about the productâs connection sync and contains the following sub-fields.

- `LastSyncTime`
- `LastSyncStatus`
- `LastSyncStatusMessage`
- `LastSuccessfulSyncTime`
- `LastSuccessfulSyncProvisioningArtifactID`

LastSyncTime -> (timestamp)

The time of the last attempted sync from the repository to the Service Catalog product.

LastSyncStatus -> (string)

The current status of the sync. Responses include `SUCCEEDED` or `FAILED` .

LastSyncStatusMessage -> (string)

The syncâs status message.

LastSuccessfulSyncTime -> (timestamp)

The time of the latest successful sync from the source repo artifact to the Service Catalog product.

LastSuccessfulSyncProvisioningArtifactId -> (string)

The ProvisioningArtifactID of the ProvisioningArtifact created from the latest successful sync.

ProvisioningArtifactSummaries -> (list)

Information about the provisioning artifacts (also known as versions) for the specified product.

(structure)

Summary information about a provisioning artifact (also known as a version) for a product.

Id -> (string)

The identifier of the provisioning artifact.

Name -> (string)

The name of the provisioning artifact.

Description -> (string)

The description of the provisioning artifact.

CreatedTime -> (timestamp)

The UTC time stamp of the creation time.

ProvisioningArtifactMetadata -> (map)

The metadata for the provisioning artifact. This is used with Amazon Web Services Marketplace products.

key -> (string)

value -> (string)

Tags -> (list)

Information about the tags associated with the product.

(structure)

Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.

Key -> (string)

The tag key.

Value -> (string)

The value for this key.

TagOptions -> (list)

Information about the TagOptions associated with the product.

(structure)

Information about a TagOption.

Key -> (string)

The TagOption key.

Value -> (string)

The TagOption value.

Active -> (boolean)

The TagOption active state.

Id -> (string)

The TagOption identifier.

Owner -> (string)

The Amazon Web Services account Id of the owner account that created the TagOption.

Budgets -> (list)

Information about the associated budgets.

(structure)

Information about a budget.

BudgetName -> (string)

Name of the associated budget.