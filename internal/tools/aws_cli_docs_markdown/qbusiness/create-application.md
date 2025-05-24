# create-applicationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/create-application.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/create-application.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qbusiness](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/index.html#cli-aws-qbusiness) ]

# create-application

## Description

Creates an Amazon Q Business application.

### Note

There are new tiers for Amazon Q Business. Not all features in Amazon Q Business Pro are also available in Amazon Q Business Lite. For information on whatâs included in Amazon Q Business Lite and whatâs included in Amazon Q Business Pro, see [Amazon Q Business tiers](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html#user-sub-tiers) . You must use the Amazon Q Business console to assign subscription tiers to users.

An Amazon Q Apps service linked role will be created if itâs absent in the Amazon Web Services account when `QAppsConfiguration` is enabled in the request. For more information, see [Using service-linked roles for Q Apps](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles-qapps.html) .

When you create an application, Amazon Q Business may securely transmit data for processing from your selected Amazon Web Services region, but within your geography. For more information, see [Cross region inference in Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cross-region-inference.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qbusiness-2023-11-27/CreateApplication)

## Synopsis

```
create-application
--display-name <value>
[--role-arn <value>]
[--identity-type <value>]
[--iam-identity-provider-arn <value>]
[--identity-center-instance-arn <value>]
[--client-ids-for-oidc <value>]
[--description <value>]
[--encryption-configuration <value>]
[--tags <value>]
[--client-token <value>]
[--attachments-configuration <value>]
[--q-apps-configuration <value>]
[--personalization-configuration <value>]
[--quick-sight-configuration <value>]
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

`--display-name` (string)

A name for the Amazon Q Business application.

`--role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role with permissions to access your Amazon CloudWatch logs and metrics. If this property is not specified, Amazon Q Business will create a [service linked role (SLR)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles.html#slr-permissions) and use it as the applicationâs role.

`--identity-type` (string)

The authentication type being used by a Amazon Q Business application.

Possible values:

- `AWS_IAM_IDP_SAML`
- `AWS_IAM_IDP_OIDC`
- `AWS_IAM_IDC`
- `AWS_QUICKSIGHT_IDP`
- `ANONYMOUS`

`--iam-identity-provider-arn` (string)

The Amazon Resource Name (ARN) of an identity provider being used by an Amazon Q Business application.

`--identity-center-instance-arn` (string)

The Amazon Resource Name (ARN) of the IAM Identity Center instance you are either creating forâor connecting toâyour Amazon Q Business application.

`--client-ids-for-oidc` (list)

The OIDC client ID for a Amazon Q Business application.

(string)

Syntax:

```
"string" "string" ...
```

`--description` (string)

A description for the Amazon Q Business application.

`--encryption-configuration` (structure)

The identifier of the KMS key that is used to encrypt your data. Amazon Q Business doesnât support asymmetric keys.

kmsKeyId -> (string)

The identifier of the KMS key. Amazon Q Business doesnât support asymmetric keys.

Shorthand Syntax:

```
kmsKeyId=string
```

JSON Syntax:

```
{
  "kmsKeyId": "string"
}
```

`--tags` (list)

A list of key-value pairs that identify or categorize your Amazon Q Business application. You can also use tags to help control access to the application. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.

(structure)

A list of key/value pairs that identify an index, FAQ, or data source. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.

key -> (string)

The key for the tag. Keys are not case sensitive and must be unique for the Amazon Q Business application or data source.

value -> (string)

The value associated with the tag. The value may be an empty string but it canât be null.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
  }
  ...
]
```

`--client-token` (string)

A token that you provide to identify the request to create your Amazon Q Business application.

`--attachments-configuration` (structure)

An option to allow end users to upload files directly during chat.

attachmentsControlMode -> (string)

Status information about whether file upload functionality is activated or deactivated for your end user.

Shorthand Syntax:

```
attachmentsControlMode=string
```

JSON Syntax:

```
{
  "attachmentsControlMode": "ENABLED"|"DISABLED"
}
```

`--q-apps-configuration` (structure)

An option to allow end users to create and use Amazon Q Apps in the web experience.

qAppsControlMode -> (string)

Status information about whether end users can create and use Amazon Q Apps in the web experience.

Shorthand Syntax:

```
qAppsControlMode=string
```

JSON Syntax:

```
{
  "qAppsControlMode": "ENABLED"|"DISABLED"
}
```

`--personalization-configuration` (structure)

Configuration information about chat response personalization. For more information, see [Personalizing chat responses](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/personalizing-chat-responses.html)

personalizationControlMode -> (string)

An option to allow Amazon Q Business to customize chat responses using user specific metadataâspecifically, location and job informationâin your IAM Identity Center instance.

Shorthand Syntax:

```
personalizationControlMode=string
```

JSON Syntax:

```
{
  "personalizationControlMode": "ENABLED"|"DISABLED"
}
```

`--quick-sight-configuration` (structure)

The Amazon QuickSight configuration for an Amazon Q Business application that uses QuickSight for authentication. This configuration is required if your application uses QuickSight as the identity provider. For more information, see [Creating an Amazon QuickSight integrated application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-quicksight-integrated-application.html) .

clientNamespace -> (string)

The Amazon QuickSight namespace that is used as the identity provider. For more information about QuickSight namespaces, see [Namespace operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/namespace-operations.html) .

Shorthand Syntax:

```
clientNamespace=string
```

JSON Syntax:

```
{
  "clientNamespace": "string"
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

## Output

applicationId -> (string)

The identifier of the Amazon Q Business application.

applicationArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Q Business application.