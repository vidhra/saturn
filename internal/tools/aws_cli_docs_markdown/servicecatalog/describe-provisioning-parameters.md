# describe-provisioning-parametersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-provisioning-parameters.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-provisioning-parameters.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicecatalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/index.html#cli-aws-servicecatalog) ]

# describe-provisioning-parameters

## Description

Gets information about the configuration required to provision the specified product using the specified provisioning artifact.

If the output contains a TagOption key with an empty list of values, there is a TagOption conflict for that key. The end user cannot take action to fix the conflict, and launch is not blocked. In subsequent calls to  ProvisionProduct , do not include conflicted TagOption keys as tags, or this causes the error âParameter validation failed: Missing required parameter in Tags[*N* ]:*Value* â. Tag the provisioned product with the value `sc-tagoption-conflict-portfolioId-productId` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeProvisioningParameters)

## Synopsis

```
describe-provisioning-parameters
[--accept-language <value>]
[--product-id <value>]
[--product-name <value>]
[--provisioning-artifact-id <value>]
[--provisioning-artifact-name <value>]
[--path-id <value>]
[--path-name <value>]
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

The product identifier. You must provide the product name or ID, but not both.

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

ConstraintSummaries -> (list)

Information about the constraints used to provision the product.

(structure)

Summary information about a constraint.

Type -> (string)

The type of constraint.

- `LAUNCH`
- `NOTIFICATION`
- STACKSET
- `TEMPLATE`

Description -> (string)

The description of the constraint.

UsageInstructions -> (list)

Any additional metadata specifically related to the provisioning of the product. For example, see the `Version` field of the CloudFormation template.

(structure)

Additional information provided by the administrator.

Type -> (string)

The usage instruction type for the value.

Value -> (string)

The usage instruction value for this type.

TagOptions -> (list)

Information about the TagOptions associated with the resource.

(structure)

Summary information about a TagOption.

Key -> (string)

The TagOption key.

Values -> (list)

The TagOption value.

(string)

ProvisioningArtifactPreferences -> (structure)

An object that contains information about preferences, such as Regions and accounts, for the provisioning artifact.

StackSetAccounts -> (list)

One or more Amazon Web Services accounts where stack instances are deployed from the stack set. These accounts can be scoped in `ProvisioningPreferences$StackSetAccounts` and `UpdateProvisioningPreferences$StackSetAccounts` .

Applicable only to a `CFN_STACKSET` provisioned product type.

(string)

StackSetRegions -> (list)

One or more Amazon Web Services Regions where stack instances are deployed from the stack set. These Regions can be scoped in `ProvisioningPreferences$StackSetRegions` and `UpdateProvisioningPreferences$StackSetRegions` .

Applicable only to a `CFN_STACKSET` provisioned product type.

(string)

ProvisioningArtifactOutputs -> (list)

The output of the provisioning artifact.

(structure)

Provisioning artifact output.

Key -> (string)

The provisioning artifact output key.

Description -> (string)

Description of the provisioning artifact output key.

ProvisioningArtifactOutputKeys -> (list)

A list of the keys and descriptions of the outputs. These outputs can be referenced from a provisioned product launched from this provisioning artifact.

(structure)

Provisioning artifact output.

Key -> (string)

The provisioning artifact output key.

Description -> (string)

Description of the provisioning artifact output key.