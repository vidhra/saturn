# create-account-customizationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-account-customization.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-account-customization.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [quicksight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/index.html#cli-aws-quicksight) ]

# create-account-customization

## Description

Creates Amazon QuickSight customizations for the current Amazon Web Services Region. Currently, you can add a custom default theme by using the `CreateAccountCustomization` or `UpdateAccountCustomization` API operation. To further customize Amazon QuickSight by removing Amazon QuickSight sample assets and videos for all new users, see [Customizing Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/customizing-quicksight.html) in the *Amazon QuickSight User Guide.*

You can create customizations for your Amazon Web Services account or, if you specify a namespace, for a QuickSight namespace instead. Customizations that apply to a namespace always override customizations that apply to an Amazon Web Services account. To find out which customizations apply, use the `DescribeAccountCustomization` API operation.

Before you use the `CreateAccountCustomization` API operation to add a theme as the namespace default, make sure that you first share the theme with the namespace. If you donât share it with the namespace, the theme isnât visible to your users even if you make it the default theme. To check if the theme is shared, view the current permissions by using the `` [DescribeThemePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeThemePermissions.html) `` API operation. To share the theme, grant permissions by using the `` [UpdateThemePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateThemePermissions.html) `` API operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/CreateAccountCustomization)

## Synopsis

```
create-account-customization
--aws-account-id <value>
[--namespace <value>]
--account-customization <value>
[--tags <value>]
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

`--aws-account-id` (string)

The ID for the Amazon Web Services account that you want to customize Amazon QuickSight for.

`--namespace` (string)

The Amazon QuickSight namespace that you want to add customizations to.

`--account-customization` (structure)

The Amazon QuickSight customizations youâre adding in the current Amazon Web Services Region. You can add these to an Amazon Web Services account and a QuickSight namespace.

For example, you can add a default theme by setting `AccountCustomization` to the midnight theme: `"AccountCustomization": { "DefaultTheme": "arn:aws:quicksight::aws:theme/MIDNIGHT" }` . Or, you can add a custom theme by specifying `"AccountCustomization": { "DefaultTheme": "arn:aws:quicksight:us-west-2:111122223333:theme/bdb844d0-0fe9-4d9d-b520-0fe602d93639" }` .

DefaultTheme -> (string)

The default theme for this Amazon QuickSight subscription.

DefaultEmailCustomizationTemplate -> (string)

The default email customization template.

Shorthand Syntax:

```
DefaultTheme=string,DefaultEmailCustomizationTemplate=string
```

JSON Syntax:

```
{
  "DefaultTheme": "string",
  "DefaultEmailCustomizationTemplate": "string"
}
```

`--tags` (list)

A list of the tags that you want to attach to this resource.

(structure)

The key or keys of the key-value pairs for the resource tag or tags assigned to the resource.

Key -> (string)

Tag key.

Value -> (string)

Tag value.

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

Arn -> (string)

The Amazon Resource Name (ARN) for the customization that you created for this Amazon Web Services account.

AwsAccountId -> (string)

The ID for the Amazon Web Services account that you want to customize Amazon QuickSight for.

Namespace -> (string)

The namespace associated with the customization youâre creating.

AccountCustomization -> (structure)

The Amazon QuickSight customizations youâre adding in the current Amazon Web Services Region.

DefaultTheme -> (string)

The default theme for this Amazon QuickSight subscription.

DefaultEmailCustomizationTemplate -> (string)

The default email customization template.

RequestId -> (string)

The Amazon Web Services request ID for this operation.

Status -> (integer)

The HTTP status of the request.