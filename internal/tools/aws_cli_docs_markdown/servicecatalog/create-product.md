# create-productÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-product.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-product.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicecatalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/index.html#cli-aws-servicecatalog) ]

# create-product

## Description

Creates a product.

A delegated admin is authorized to invoke this command.

The user or role that performs this operation must have the `cloudformation:GetTemplate` IAM policy permission. This policy permission is required when using the `ImportFromPhysicalId` template source in the information data section.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/CreateProduct)

## Synopsis

```
create-product
[--accept-language <value>]
--name <value>
--owner <value>
[--description <value>]
[--distributor <value>]
[--support-description <value>]
[--support-email <value>]
[--support-url <value>]
--product-type <value>
[--tags <value>]
[--provisioning-artifact-parameters <value>]
[--idempotency-token <value>]
[--source-connection <value>]
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

`--name` (string)

The name of the product.

`--owner` (string)

The owner of the product.

`--description` (string)

The description of the product.

`--distributor` (string)

The distributor of the product.

`--support-description` (string)

The support information about the product.

`--support-email` (string)

The contact email for product support.

`--support-url` (string)

The contact URL for product support.

`^https?:\/\//` / is the pattern used to validate SupportUrl.

`--product-type` (string)

The type of product.

Possible values:

- `CLOUD_FORMATION_TEMPLATE`
- `MARKETPLACE`
- `TERRAFORM_OPEN_SOURCE`
- `TERRAFORM_CLOUD`
- `EXTERNAL`

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

`--provisioning-artifact-parameters` (structure)

The configuration of the provisioning artifact.

Name -> (string)

The name of the provisioning artifact (for example, v1 v2beta). No spaces are allowed.

Description -> (string)

The description of the provisioning artifact, including how it differs from the previous provisioning artifact.

Info -> (map)

Specify the template source with one of the following options, but not both. Keys accepted: [ `LoadTemplateFromURL` , `ImportFromPhysicalId` ]

The URL of the CloudFormation template in Amazon S3 or GitHub in JSON format. Specify the URL in JSON format as follows:

`"LoadTemplateFromURL": "https://s3.amazonaws.com/cf-templates-ozkq9d3hgiq2-us-east-1/..."`

`ImportFromPhysicalId` : The physical id of the resource that contains the template. Currently only supports CloudFormation stack arn. Specify the physical id in JSON format as follows: `ImportFromPhysicalId: âarn:aws:cloudformation:[us-east-1]:[accountId]:stack/[StackName]/[resourceId]`

key -> (string)

value -> (string)

Type -> (string)

The type of provisioning artifact.

- `CLOUD_FORMATION_TEMPLATE` - CloudFormation template
- `TERRAFORM_OPEN_SOURCE` - Terraform Open Source configuration file
- `TERRAFORM_CLOUD` - Terraform Cloud configuration file
- `EXTERNAL` - External configuration file

DisableTemplateValidation -> (boolean)

If set to true, Service Catalog stops validating the specified provisioning artifact even if it is invalid.

Service Catalog does not support template validation for the `TERRAFORM_OS` product type.

Shorthand Syntax:

```
Name=string,Description=string,Info={KeyName1=string,KeyName2=string},Type=string,DisableTemplateValidation=boolean
```

JSON Syntax:

```
{
  "Name": "string",
  "Description": "string",
  "Info": {"string": "string"
    ...},
  "Type": "CLOUD_FORMATION_TEMPLATE"|"MARKETPLACE_AMI"|"MARKETPLACE_CAR"|"TERRAFORM_OPEN_SOURCE"|"TERRAFORM_CLOUD"|"EXTERNAL",
  "DisableTemplateValidation": true|false
}
```

`--idempotency-token` (string)

A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.

`--source-connection` (structure)

Specifies connection details for the created product and syncs the product to the connection source artifact. This automatically manages the productâs artifacts based on changes to the source. The `SourceConnection` parameter consists of the following sub-fields.

- `Type`
- `ConnectionParamters`

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

Shorthand Syntax:

```
Type=string,ConnectionParameters={CodeStar={ConnectionArn=string,Repository=string,Branch=string,ArtifactPath=string}}
```

JSON Syntax:

```
{
  "Type": "CODESTAR",
  "ConnectionParameters": {
    "CodeStar": {
      "ConnectionArn": "string",
      "Repository": "string",
      "Branch": "string",
      "ArtifactPath": "string"
    }
  }
}
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a product**

The following `create-product` example creates a product, using a JSON file to pass parameters.

```
aws servicecatalog create-product \
    --cli-input-json file://create-product-input.json
```

Contents of `create-product-input.json`:

```
{
    "AcceptLanguage": "en",
    "Name": "test-product",
    "Owner": "test-owner",
    "Description": "test-description",
    "Distributor": "test-distributor",
    "SupportDescription": "test-support",
    "SupportEmail": "test@amazon.com",
    "SupportUrl": "https://aws.amazon.com",
    "ProductType": "CLOUD_FORMATION_TEMPLATE",
    "Tags": [
        {
            "Key": "region",
            "Value": "us-east-1"
        }
    ],
    "ProvisioningArtifactParameters": {
        "Name": "test-version-name",
        "Description": "test-version-description",
        "Info": {
            "LoadTemplateFromURL": "https://s3-us-west-1.amazonaws.com/cloudformation-templates-us-west-1/my-cfn-template.template"
        },
        "Type": "CLOUD_FORMATION_TEMPLATE"
    }
}
```

Output:

```
{
    "Tags": [
        {
            "Key": "region",
            "Value": "us-east-1"
        }
    ],
    "ProductViewDetail": {
        "CreatedTime": 1576025036.0,
        "ProductARN": "arn:aws:catalog:us-west-2:1234568542028:product/prod-3p5abcdef3oyk",
        "Status": "CREATED",
        "ProductViewSummary": {
            "Type": "CLOUD_FORMATION_TEMPLATE",
            "Distributor": "test-distributor",
            "SupportUrl": "https://aws.amazon.com",
            "SupportEmail": "test@amazon.com",
            "Id": "prodview-abcd42wvx45um",
            "SupportDescription": "test-support",
            "ShortDescription": "test-description",
            "Owner": "test-owner",
            "Name": "test-product2",
            "HasDefaultPath": false,
            "ProductId": "prod-3p5abcdef3oyk"
        }
    },
    "ProvisioningArtifactDetail": {
        "CreatedTime": 1576025036.0,
        "Active": true,
        "Id": "pa-pq3p5lil12a34",
        "Description": "test-version-description",
        "Name": "test-version-name",
        "Type": "CLOUD_FORMATION_TEMPLATE"
    }
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

ProvisioningArtifactDetail -> (structure)

Information about the provisioning artifact.

Id -> (string)

The identifier of the provisioning artifact.

Name -> (string)

The name of the provisioning artifact.

Description -> (string)

The description of the provisioning artifact.

Type -> (string)

The type of provisioning artifact.

- `CLOUD_FORMATION_TEMPLATE` - CloudFormation template
- `TERRAFORM_OPEN_SOURCE` - Terraform Open Source configuration file
- `TERRAFORM_CLOUD` - Terraform Cloud configuration file
- `EXTERNAL` - External configuration file

CreatedTime -> (timestamp)

The UTC time stamp of the creation time.

Active -> (boolean)

Indicates whether the product version is active.

Guidance -> (string)

Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.

SourceRevision -> (string)

Specifies the revision of the external artifact that was used to automatically sync the Service Catalog product and create the provisioning artifact. Service Catalog includes this response parameter as a high level field to the existing `ProvisioningArtifactDetail` type, which is returned as part of the response for `CreateProduct` , `UpdateProduct` , `DescribeProductAsAdmin` , `DescribeProvisioningArtifact` , `ListProvisioningArtifact` , and `UpdateProvisioningArticat` APIs.

This field only exists for Repo-Synced products.

Tags -> (list)

Information about the tags associated with the product.

(structure)

Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.

Key -> (string)

The tag key.

Value -> (string)

The value for this key.