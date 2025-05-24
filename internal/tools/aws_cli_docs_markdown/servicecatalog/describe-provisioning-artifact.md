# describe-provisioning-artifactÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-provisioning-artifact.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-provisioning-artifact.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicecatalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/index.html#cli-aws-servicecatalog) ]

# describe-provisioning-artifact

## Description

Gets information about the specified provisioning artifact (also known as a version) for the specified product.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeProvisioningArtifact)

## Synopsis

```
describe-provisioning-artifact
[--accept-language <value>]
[--provisioning-artifact-id <value>]
[--product-id <value>]
[--provisioning-artifact-name <value>]
[--product-name <value>]
[--verbose | --no-verbose]
[--include-provisioning-artifact-parameters | --no-include-provisioning-artifact-parameters]
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

`--provisioning-artifact-id` (string)

The identifier of the provisioning artifact.

`--product-id` (string)

The product identifier.

`--provisioning-artifact-name` (string)

The provisioning artifact name.

`--product-name` (string)

The product name.

`--verbose` | `--no-verbose` (boolean)

Indicates whether a verbose level of detail is enabled.

`--include-provisioning-artifact-parameters` | `--no-include-provisioning-artifact-parameters` (boolean)

Indicates if the API call response does or does not include additional details about the provisioning parameters.

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

**To describe a provisioning artifact**

The following `describe-provisioning-artifact` example displays details for the specified provisioning artifact.

```
aws servicecatalog describe-provisioning-artifact \
    --provisioning-artifact-id pa-pcz347abcdcfm \
    --product-id prod-abcdfz3syn2rg
```

Output:

```
{
    "Info": {
        "TemplateUrl": "https://awsdocs.s3.amazonaws.com/servicecatalog/myexampledevelopment-environment.template"
    },
    "ProvisioningArtifactDetail": {
        "Id": "pa-pcz347abcdcfm",
        "Active": true,
        "Type": "CLOUD_FORMATION_TEMPLATE",
        "Description": "updated description",
        "CreatedTime": 1562097906.0,
        "Name": "updated name"
    },
    "Status": "AVAILABLE"
}
```

## Output

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

Info -> (map)

The URL of the CloudFormation template in Amazon S3 or GitHub in JSON format.

key -> (string)

value -> (string)

Status -> (string)

The status of the current request.

ProvisioningArtifactParameters -> (list)

Information about the parameters used to provision the product.

(structure)

Information about a parameter used to provision a product.

ParameterKey -> (string)

The parameter key.

DefaultValue -> (string)

The default value.

ParameterType -> (string)

The parameter type.

IsNoEcho -> (boolean)

If this value is true, the value for this parameter is obfuscated from view when the parameter is retrieved. This parameter is used to hide sensitive information.

Description -> (string)

The description of the parameter.

ParameterConstraints -> (structure)

Constraints that the administrator has put on a parameter.

AllowedValues -> (list)

The values that the administrator has allowed for the parameter.

(string)

AllowedPattern -> (string)

A regular expression that represents the patterns that allow for `String` types. The pattern must match the entire parameter value provided.

ConstraintDescription -> (string)

A string that explains a constraint when the constraint is violated. For example, without a constraint description, a parameter that has an allowed pattern of `[A-Za-z0-9]+` displays the following error message when the user specifies an invalid value:

`Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+`

By adding a constraint description, such as must only contain letters (uppercase and lowercase) and numbers, you can display the following customized error message:

`Malformed input-Parameter MyParameter must only contain uppercase and lowercase letters and numbers.`

MaxLength -> (string)

An integer value that determines the largest number of characters you want to allow for `String` types.

MinLength -> (string)

An integer value that determines the smallest number of characters you want to allow for `String` types.

MaxValue -> (string)

A numeric value that determines the largest numeric value you want to allow for `Number` types.

MinValue -> (string)

A numeric value that determines the smallest numeric value you want to allow for `Number` types.