# update-provisioning-artifactÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-provisioning-artifact.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-provisioning-artifact.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicecatalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/index.html#cli-aws-servicecatalog) ]

# update-provisioning-artifact

## Description

Updates the specified provisioning artifact (also known as a version) for the specified product.

You cannot update a provisioning artifact for a product that was shared with you.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/UpdateProvisioningArtifact)

## Synopsis

```
update-provisioning-artifact
[--accept-language <value>]
--product-id <value>
--provisioning-artifact-id <value>
[--name <value>]
[--description <value>]
[--active | --no-active]
[--guidance <value>]
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

`--name` (string)

The updated name of the provisioning artifact.

`--description` (string)

The updated description of the provisioning artifact.

`--active` | `--no-active` (boolean)

Indicates whether the product version is active.

Inactive provisioning artifacts are invisible to end users. End users cannot launch or update a provisioned product from an inactive provisioning artifact.

`--guidance` (string)

Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.

The `DEFAULT` value indicates that the product version is active.

The administrator can set the guidance to `DEPRECATED` to inform users that the product version is deprecated. Users are able to make updates to a provisioned product of a deprecated version but cannot launch new provisioned products using a deprecated version.

Possible values:

- `DEFAULT`
- `DEPRECATED`

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

**To update a provisioning artifact**

The following `update-provisioning-artifact` example updates the name and description of the specified provisioning artifact, using a JSON file to pass parameters.

```
aws servicecatalog update-provisioning-artifact \
    --cli-input-json file://update-provisioning-artifact-input.json
```

Contents of `update-provisioning-artifact-input.json`:

```
{
    "ProductId": "prod-abcdfz3syn2rg",
    "ProvisioningArtifactId": "pa-pcz347abcdcfm",
    "Name": "updated name",
    "Description": "updated description"
}
```

Output:

```
{
    "Info": {
        "TemplateUrl": "https://awsdocs.s3.amazonaws.com/servicecatalog/myexampledevelopment-environment.template"
    },
    "Status": "AVAILABLE",
    "ProvisioningArtifactDetail": {
        "Active": true,
        "Description": "updated description",
        "Id": "pa-pcz347abcdcfm",
        "Name": "updated name",
        "Type": "CLOUD_FORMATION_TEMPLATE",
        "CreatedTime": 1562097906.0
    }
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