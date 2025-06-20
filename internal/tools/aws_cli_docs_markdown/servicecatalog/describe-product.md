# describe-productÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-product.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-product.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicecatalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/index.html#cli-aws-servicecatalog) ]

# describe-product

## Description

Gets information about the specified product.

### Note

Running this operation with administrator access results in a failure.  DescribeProductAsAdmin should be used instead.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeProduct)

## Synopsis

```
describe-product
[--accept-language <value>]
[--id <value>]
[--name <value>]
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

ProvisioningArtifacts -> (list)

Information about the provisioning artifacts for the specified product.

(structure)

Information about a provisioning artifact. A provisioning artifact is also known as a product version.

Id -> (string)

The identifier of the provisioning artifact.

Name -> (string)

The name of the provisioning artifact.

Description -> (string)

The description of the provisioning artifact.

CreatedTime -> (timestamp)

The UTC time stamp of the creation time.

Guidance -> (string)

Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.

Budgets -> (list)

Information about the associated budgets.

(structure)

Information about a budget.

BudgetName -> (string)

Name of the associated budget.

LaunchPaths -> (list)

Information about the associated launch paths.

(structure)

A launch path object.

Id -> (string)

The identifier of the launch path.

Name -> (string)

The name of the launch path.