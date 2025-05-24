# describe-typeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-type.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-type.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# describe-type

## Description

Returns detailed information about an extension that has been registered.

If you specify a `VersionId` , `DescribeType` returns information about that specific extension version. Otherwise, it returns information about the default extension version.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeType)

## Synopsis

```
describe-type
[--type <value>]
[--type-name <value>]
[--arn <value>]
[--version-id <value>]
[--publisher-id <value>]
[--public-version-number <value>]
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

`--type` (string)

The kind of extension.

Conditional: You must specify either `TypeName` and `Type` , or `Arn` .

Possible values:

- `RESOURCE`
- `MODULE`
- `HOOK`

`--type-name` (string)

The name of the extension.

Conditional: You must specify either `TypeName` and `Type` , or `Arn` .

`--arn` (string)

The Amazon Resource Name (ARN) of the extension.

Conditional: You must specify either `TypeName` and `Type` , or `Arn` .

`--version-id` (string)

The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.

If you specify a `VersionId` , `DescribeType` returns information about that specific extension version. Otherwise, it returns information about the default extension version.

`--publisher-id` (string)

The publisher ID of the extension publisher.

Extensions provided by Amazon Web Services are not assigned a publisher ID.

`--public-version-number` (string)

The version number of a public third-party extension.

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

**To display type information**

The following `describe-type` example displays information for the specified type.

```
aws cloudformation describe-type \
    --type-name My::Logs::LogGroup \
    --type RESOURCE
```

Output:

```
{
    "SourceUrl": "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-logs.git",
    "Description": "Customized resource derived from AWS::Logs::LogGroup",
    "TimeCreated": "2019-12-03T23:29:33.321Z",
    "Visibility": "PRIVATE",
    "TypeName": "My::Logs::LogGroup",
    "LastUpdated": "2019-12-03T23:29:33.321Z",
    "DeprecatedStatus": "LIVE",
    "ProvisioningType": "FULLY_MUTABLE",
    "Type": "RESOURCE",
    "Arn": "arn:aws:cloudformation:us-west-2:123456789012:type/resource/My-Logs-LogGroup/00000001",
    "Schema": "[details omitted]"
}
```

For more information, see [Using the CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) in the *AWS CloudFormation Users Guide*.

## Output

Arn -> (string)

The Amazon Resource Name (ARN) of the extension.

Type -> (string)

The kind of extension.

TypeName -> (string)

The name of the extension.

If the extension is a public third-party type you have activated with a type name alias, CloudFormation returns the type name alias. For more information, see [ActivateType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html) .

DefaultVersionId -> (string)

The ID of the default version of the extension. The default version is used when the extension version isnât specified.

This applies only to private extensions you have registered in your account. For public extensions, both those provided by Amazon Web Services and published by third parties, CloudFormation returns `null` . For more information, see [RegisterType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html) .

To set the default version of an extension, use  SetTypeDefaultVersion .

IsDefaultVersion -> (boolean)

Whether the specified extension version is set as the default version.

This applies only to private extensions you have registered in your account, and extensions published by Amazon Web Services. For public third-party extensions, whether they are activated in your account, CloudFormation returns `null` .

TypeTestsStatus -> (string)

The contract test status of the registered extension version. To return the extension test status of a specific extension version, you must specify `VersionId` .

This applies only to registered private extension versions. CloudFormation doesnât return this information for public extensions, whether they are activated in your account.

- `PASSED` : The extension has passed all its contract tests. An extension must have a test status of `PASSED` before it can be published. For more information, see [Publishing extensions to make them available for public use](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-publish.html) in the *CloudFormation Command Line Interface (CLI) User Guide* .
- `FAILED` : The extension has failed one or more contract tests.
- `IN_PROGRESS` : Contract tests are currently being performed on the extension.
- `NOT_TESTED` : Contract tests havenât been performed on the extension.

TypeTestsStatusDescription -> (string)

The description of the test status. To return the extension test status of a specific extension version, you must specify `VersionId` .

This applies only to registered private extension versions. CloudFormation doesnât return this information for public extensions, whether they are activated in your account.

Description -> (string)

The description of the extension.

Schema -> (string)

The schema that defines the extension.

For more information about extension schemas, see [Resource type schema](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html) in the *CloudFormation Command Line Interface (CLI) User Guide* .

ProvisioningType -> (string)

For resource type extensions, the provisioning behavior of the resource type. CloudFormation determines the provisioning type during registration, based on the types of handlers in the schema handler package submitted.

Valid values include:

- `FULLY_MUTABLE` : The resource type includes an update handler to process updates to the type during stack update operations.
- `IMMUTABLE` : The resource type doesnât include an update handler, so the type canât be updated and must instead be replaced during stack update operations.
- `NON_PROVISIONABLE` : The resource type doesnât include all the following handlers, and therefore canât actually be provisioned.
- create
- read
- delete

DeprecatedStatus -> (string)

The deprecation status of the extension version.

Valid values include:

- `LIVE` : The extension is activated or registered and can be used in CloudFormation operations, dependent on its provisioning behavior and visibility scope.
- `DEPRECATED` : The extension has been deactivated or deregistered and can no longer be used in CloudFormation operations.

For public third-party extensions, CloudFormation returns `null` .

LoggingConfig -> (structure)

Contains logging configuration information for private extensions. This applies only to private extensions you have registered in your account. For public extensions, both those provided by Amazon Web Services and published by third parties, CloudFormation returns `null` . For more information, see [RegisterType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html) .

LogRoleArn -> (string)

The Amazon Resource Name (ARN) of the role that CloudFormation should assume when sending log entries to CloudWatch Logs.

LogGroupName -> (string)

The Amazon CloudWatch Logs group to which CloudFormation sends error logging information when invoking the extensionâs handlers.

RequiredActivatedTypes -> (list)

For extensions that are modules, the public third-party extensions that must be activated in your account in order for the module itself to be activated.

(structure)

For extensions that are modules, a public third-party extension that must be activated in your account in order for the module itself to be activated.

For more information, see [Requirements for activating third-party public modules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/module-versioning.html#requirements-for-modules) in the *CloudFormation User Guide* .

TypeNameAlias -> (string)

An alias assigned to the public extension, in this account and Region. If you specify an alias for the extension, CloudFormation treats the alias as the extension type name within this account and Region. You must use the alias to refer to the extension in your templates, API calls, and CloudFormation console.

OriginalTypeName -> (string)

The type name of the public extension.

If you specified a `TypeNameAlias` when enabling the extension in this account and Region, CloudFormation treats that alias as the extensionâs type name within the account and Region, not the type name of the public extension. For more information, see [Use aliases to refer to extensions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-alias) in the *CloudFormation User Guide* .

PublisherId -> (string)

The publisher ID of the extension publisher.

SupportedMajorVersions -> (list)

A list of the major versions of the extension type that the macro supports.

(integer)

ExecutionRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM execution role used to register the extension. This applies only to private extensions you have registered in your account. For more information, see [RegisterType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html) .

If the registered extension calls any Amazon Web Services APIs, you must create an * [IAM execution role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) * that includes the necessary permissions to call those Amazon Web Services APIs, and provision that execution role in your account. CloudFormation then assumes that execution role to provide your extension with the appropriate credentials.

Visibility -> (string)

The scope at which the extension is visible and usable in CloudFormation operations.

Valid values include:

- `PRIVATE` : The extension is only visible and usable within the account in which it is registered. CloudFormation marks any extensions you register as `PRIVATE` .
- `PUBLIC` : The extension is publicly visible and usable within any Amazon Web Services account.

SourceUrl -> (string)

The URL of the source code for the extension.

DocumentationUrl -> (string)

The URL of a page providing detailed documentation for this extension.

LastUpdated -> (timestamp)

When the specified extension version was registered. This applies only to:

- Private extensions you have registered in your account. For more information, see [RegisterType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html) .
- Public extensions you have activated in your account with auto-update specified. For more information, see [ActivateType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html) .

TimeCreated -> (timestamp)

When the specified private extension version was registered or activated in your account.

ConfigurationSchema -> (string)

A JSON string that represent the current configuration data for the extension in this account and Region.

To set the configuration data for an extension, use [SetTypeConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html) . For more information, see [Edit configuration data for extensions in your account](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-set-configuration.html) in the *CloudFormation User Guide* .

PublisherId -> (string)

The publisher ID of the extension publisher.

This applies only to public third-party extensions. For private registered extensions, and extensions provided by Amazon Web Services, CloudFormation returns `null` .

OriginalTypeName -> (string)

For public extensions that have been activated for this account and Region, the type name of the public extension.

If you specified a `TypeNameAlias` when enabling the extension in this account and Region, CloudFormation treats that alias as the extensionâs type name within the account and Region, not the type name of the public extension. For more information, see [Use aliases to refer to extensions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-alias) in the *CloudFormation User Guide* .

OriginalTypeArn -> (string)

For public extensions that have been activated for this account and Region, the Amazon Resource Name (ARN) of the public extension.

PublicVersionNumber -> (string)

The version number of a public third-party extension.

This applies only if you specify a public extension you have activated in your account, or specify a public extension without specifying a version. For all other extensions, CloudFormation returns `null` .

LatestPublicVersion -> (string)

The latest version of a public extension *that is available* for use.

This only applies if you specify a public extension, and you donât specify a version. For all other requests, CloudFormation returns `null` .

IsActivated -> (boolean)

Whether the extension is activated in the account and Region.

This only applies to public third-party extensions. For all other extensions, CloudFormation returns `null` .

AutoUpdate -> (boolean)

Whether CloudFormation automatically updates the extension in this account and Region when a new *minor* version is published by the extension publisher. Major versions released by the publisher must be manually updated. For more information, see [Automatically use new versions of extensions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-auto) in the *CloudFormation User Guide* .