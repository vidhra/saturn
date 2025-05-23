# list-typesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-types.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-types.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# list-types

## Description

Returns summary information about extension that have been registered with CloudFormation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListTypes)

`list-types` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `TypeSummaries`

## Synopsis

```
list-types
[--visibility <value>]
[--provisioning-type <value>]
[--deprecated-status <value>]
[--type <value>]
[--filters <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--visibility` (string)

The scope at which the extensions are visible and usable in CloudFormation operations.

Valid values include:

- `PRIVATE` : Extensions that are visible and usable within this account and Region. This includes:
- Private extensions you have registered in this account and Region.
- Public extensions that you have activated in this account and Region.
- `PUBLIC` : Extensions that are publicly visible and available to be activated within any Amazon Web Services account. This includes extensions from Amazon Web Services, in addition to third-party publishers.

The default is `PRIVATE` .

Possible values:

- `PUBLIC`
- `PRIVATE`

`--provisioning-type` (string)

For resource types, the provisioning behavior of the resource type. CloudFormation determines the provisioning type during registration, based on the types of handlers in the schema handler package submitted.

Valid values include:

- `FULLY_MUTABLE` : The resource type includes an update handler to process updates to the type during stack update operations.
- `IMMUTABLE` : The resource type doesnât include an update handler, so the type canât be updated and must instead be replaced during stack update operations.
- `NON_PROVISIONABLE` : The resource type doesnât include create, read, and delete handlers, and therefore canât actually be provisioned.

The default is `FULLY_MUTABLE` .

Possible values:

- `NON_PROVISIONABLE`
- `IMMUTABLE`
- `FULLY_MUTABLE`

`--deprecated-status` (string)

The deprecation status of the extension that you want to get summary information about.

Valid values include:

- `LIVE` : The extension is registered for use in CloudFormation operations.
- `DEPRECATED` : The extension has been deregistered and can no longer be used in CloudFormation operations.

Possible values:

- `LIVE`
- `DEPRECATED`

`--type` (string)

The type of extension.

Possible values:

- `RESOURCE`
- `MODULE`
- `HOOK`

`--filters` (structure)

Filter criteria to use in determining which extensions to return.

Filters must be compatible with `Visibility` to return valid results. For example, specifying `AWS_TYPES` for `Category` and `PRIVATE` for `Visibility` returns an empty list of types, but specifying `PUBLIC` for `Visibility` returns the desired list.

Category -> (string)

The category of extensions to return.

- `REGISTERED` : Private extensions that have been registered for this account and Region.
- `ACTIVATED` : Public extensions that have been activated for this account and Region.
- `THIRD_PARTY` : Extensions available for use from publishers other than Amazon. This includes:
- Private extensions registered in the account.
- Public extensions from publishers other than Amazon, whether activated or not.
- `AWS_TYPES` : Extensions available for use from Amazon.

PublisherId -> (string)

The id of the publisher of the extension.

Extensions published by Amazon arenât assigned a publisher ID. Use the `AWS_TYPES` category to specify a list of types published by Amazon.

TypeNamePrefix -> (string)

A prefix to use as a filter for results.

Shorthand Syntax:

```
Category=string,PublisherId=string,TypeNamePrefix=string
```

JSON Syntax:

```
{
  "Category": "REGISTERED"|"ACTIVATED"|"THIRD_PARTY"|"AWS_TYPES",
  "PublisherId": "string",
  "TypeNamePrefix": "string"
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To list the private resource types in an account**

The following `list-types` example displays a list of the private resource types currently registered in the current AWS account.

```
aws cloudformation list-types
```

Output:

```
{
    "TypeSummaries": [
        {
            "Description": "WordPress blog resource for internal use",
            "LastUpdated": "2019-12-04T18:28:15.059Z",
            "TypeName": "My::WordPress::BlogExample",
            "TypeArn": "arn:aws:cloudformation:us-west-2:123456789012:type/resource/My-WordPress-BlogExample",
            "DefaultVersionId": "00000005",
            "Type": "RESOURCE"
        },
        {
            "Description": "Customized resource derived from AWS::Logs::LogGroup",
            "LastUpdated": "2019-12-04T18:28:15.059Z",
            "TypeName": "My::Logs::LogGroup",
            "TypeArn": "arn:aws:cloudformation:us-west-2:123456789012:type/resource/My-Logs-LogGroup",
            "DefaultVersionId": "00000003",
            "Type": "RESOURCE"
        }
    ]
}
```

For more information, see [Using the CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) in the *AWS CloudFormation Users Guide*.

## Output

TypeSummaries -> (list)

A list of `TypeSummary` structures that contain information about the specified extensions.

(structure)

Contains summary information about the specified CloudFormation extension.

Type -> (string)

The kind of extension.

TypeName -> (string)

The name of the extension.

If you specified a `TypeNameAlias` when you call the [ActivateType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html) API operation in your account and Region, CloudFormation considers that alias as the type name.

DefaultVersionId -> (string)

The ID of the default version of the extension. The default version is used when the extension version isnât specified.

This applies only to private extensions you have registered in your account. For public extensions, both those provided by Amazon and published by third parties, CloudFormation returns `null` . For more information, see [RegisterType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html) .

To set the default version of an extension, use  SetTypeDefaultVersion .

TypeArn -> (string)

The Amazon Resource Name (ARN) of the extension.

LastUpdated -> (timestamp)

When the specified extension version was registered. This applies only to:

- Private extensions you have registered in your account. For more information, see [RegisterType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html) .
- Public extensions you have activated in your account with auto-update specified. For more information, see [ActivateType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html) .

For all other extension types, CloudFormation returns `null` .

Description -> (string)

The description of the extension.

PublisherId -> (string)

The ID of the extension publisher, if the extension is published by a third party. Extensions published by Amazon donât return a publisher ID.

OriginalTypeName -> (string)

For public extensions that have been activated for this account and Region, the type name of the public extension.

If you specified a `TypeNameAlias` when enabling the extension in this account and Region, CloudFormation treats that alias as the extensionâs type name within the account and Region, not the type name of the public extension. For more information, see [Use aliases to refer to extensions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-alias) in the *CloudFormation User Guide* .

PublicVersionNumber -> (string)

For public extensions that have been activated for this account and Region, the version of the public extension to be used for CloudFormation operations in this account and Region.

How you specified `AutoUpdate` when enabling the extension affects whether CloudFormation automatically updates the extension in this account and Region when a new version is released. For more information, see [Automatically use new versions of extensions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-auto) in the *CloudFormation User Guide* .

LatestPublicVersion -> (string)

For public extensions that have been activated for this account and Region, the latest version of the public extension *that is available* . For any extensions other than activated third-party extensions, CloudFormation returns `null` .

How you specified `AutoUpdate` when enabling the extension affects whether CloudFormation automatically updates the extension in this account and Region when a new version is released. For more information, see [Automatically use new versions of extensions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-auto) in the *CloudFormation User Guide* .

PublisherIdentity -> (string)

The service used to verify the publisher identity.

For more information, see [Publishing extensions to make them available for public use](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html) in the *CloudFormation Command Line Interface (CLI) User Guide* .

PublisherName -> (string)

The publisher name, as defined in the public profile for that publisher in the service used to verify the publisher identity.

IsActivated -> (boolean)

Whether the extension is activated for this account and Region.

This applies only to third-party public extensions. Extensions published by Amazon are activated by default.

NextToken -> (string)

If the request doesnât return all the remaining results, `NextToken` is set to a token. To retrieve the next set of results, call this action again and assign that token to the request objectâs `NextToken` parameter. If the request returns all results, `NextToken` is set to `null` .