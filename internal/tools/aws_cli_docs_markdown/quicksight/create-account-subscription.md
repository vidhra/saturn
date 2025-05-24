# create-account-subscriptionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-account-subscription.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-account-subscription.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [quicksight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/index.html#cli-aws-quicksight) ]

# create-account-subscription

## Description

Creates an Amazon QuickSight account, or subscribes to Amazon QuickSight Q.

The Amazon Web Services Region for the account is derived from what is configured in the CLI or SDK.

Before you use this operation, make sure that you can connect to an existing Amazon Web Services account. If you donât have an Amazon Web Services account, see [Sign up for Amazon Web Services](https://docs.aws.amazon.com/quicksight/latest/user/setting-up-aws-sign-up.html) in the *Amazon QuickSight User Guide* . The person who signs up for Amazon QuickSight needs to have the correct Identity and Access Management (IAM) permissions. For more information, see [IAM Policy Examples for Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/iam-policy-examples.html) in the *Amazon QuickSight User Guide* .

If your IAM policy includes both the `Subscribe` and `CreateAccountSubscription` actions, make sure that both actions are set to `Allow` . If either action is set to `Deny` , the `Deny` action prevails and your API call fails.

You canât pass an existing IAM role to access other Amazon Web Services services using this API operation. To pass your existing IAM role to Amazon QuickSight, see [Passing IAM roles to Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/security_iam_service-with-iam.html#security-create-iam-role) in the *Amazon QuickSight User Guide* .

You canât set default resource access on the new account from the Amazon QuickSight API. Instead, add default resource access from the Amazon QuickSight console. For more information about setting default resource access to Amazon Web Services services, see [Setting default resource access to Amazon Web Services services](https://docs.aws.amazon.com/quicksight/latest/user/scoping-policies-defaults.html) in the *Amazon QuickSight User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/CreateAccountSubscription)

## Synopsis

```
create-account-subscription
[--edition <value>]
--authentication-method <value>
--aws-account-id <value>
--account-name <value>
--notification-email <value>
[--active-directory-name <value>]
[--realm <value>]
[--directory-id <value>]
[--admin-group <value>]
[--author-group <value>]
[--reader-group <value>]
[--admin-pro-group <value>]
[--author-pro-group <value>]
[--reader-pro-group <value>]
[--first-name <value>]
[--last-name <value>]
[--email-address <value>]
[--contact-number <value>]
[--iam-identity-center-instance-arn <value>]
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

`--edition` (string)

The edition of Amazon QuickSight that you want your account to have. Currently, you can choose from `ENTERPRISE` or `ENTERPRISE_AND_Q` .

If you choose `ENTERPRISE_AND_Q` , the following parameters are required:

- `FirstName`
- `LastName`
- `EmailAddress`
- `ContactNumber`

Possible values:

- `STANDARD`
- `ENTERPRISE`
- `ENTERPRISE_AND_Q`

`--authentication-method` (string)

The method that you want to use to authenticate your Amazon QuickSight account.

If you choose `ACTIVE_DIRECTORY` , provide an `ActiveDirectoryName` and an `AdminGroup` associated with your Active Directory.

If you choose `IAM_IDENTITY_CENTER` , provide an `AdminGroup` associated with your IAM Identity Center account.

Possible values:

- `IAM_AND_QUICKSIGHT`
- `IAM_ONLY`
- `ACTIVE_DIRECTORY`
- `IAM_IDENTITY_CENTER`

`--aws-account-id` (string)

The Amazon Web Services account ID of the account that youâre using to create your Amazon QuickSight account.

`--account-name` (string)

The name of your Amazon QuickSight account. This name is unique over all of Amazon Web Services, and it appears only when users sign in. You canât change `AccountName` value after the Amazon QuickSight account is created.

`--notification-email` (string)

The email address that you want Amazon QuickSight to send notifications to regarding your Amazon QuickSight account or Amazon QuickSight subscription.

`--active-directory-name` (string)

The name of your Active Directory. This field is required if `ACTIVE_DIRECTORY` is the selected authentication method of the new Amazon QuickSight account.

`--realm` (string)

The realm of the Active Directory that is associated with your Amazon QuickSight account. This field is required if `ACTIVE_DIRECTORY` is the selected authentication method of the new Amazon QuickSight account.

`--directory-id` (string)

The ID of the Active Directory that is associated with your Amazon QuickSight account.

`--admin-group` (list)

The admin group associated with your Active Directory or IAM Identity Center account. Either this field or the `AdminProGroup` field is required if `ACTIVE_DIRECTORY` or `IAM_IDENTITY_CENTER` is the selected authentication method of the new Amazon QuickSight account.

For more information about using IAM Identity Center in Amazon QuickSight, see [Using IAM Identity Center with Amazon QuickSight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html) in the Amazon QuickSight User Guide. For more information about using Active Directory in Amazon QuickSight, see [Using Active Directory with Amazon QuickSight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/aws-directory-service.html) in the Amazon QuickSight User Guide.

(string)

Syntax:

```
"string" "string" ...
```

`--author-group` (list)

The author group associated with your Active Directory or IAM Identity Center account.

For more information about using IAM Identity Center in Amazon QuickSight, see [Using IAM Identity Center with Amazon QuickSight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html) in the Amazon QuickSight User Guide. For more information about using Active Directory in Amazon QuickSight, see [Using Active Directory with Amazon QuickSight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/aws-directory-service.html) in the Amazon QuickSight User Guide.

(string)

Syntax:

```
"string" "string" ...
```

`--reader-group` (list)

The reader group associated with your Active Directory or IAM Identity Center account.

For more information about using IAM Identity Center in Amazon QuickSight, see [Using IAM Identity Center with Amazon QuickSight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html) in the Amazon QuickSight User Guide. For more information about using Active Directory in Amazon QuickSight, see [Using Active Directory with Amazon QuickSight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/aws-directory-service.html) in the Amazon QuickSight User Guide.

(string)

Syntax:

```
"string" "string" ...
```

`--admin-pro-group` (list)

The admin pro group associated with your Active Directory or IAM Identity Center account. Either this field or the `AdminGroup` field is required if `ACTIVE_DIRECTORY` or `IAM_IDENTITY_CENTER` is the selected authentication method of the new Amazon QuickSight account.

For more information about using IAM Identity Center in Amazon QuickSight, see [Using IAM Identity Center with Amazon QuickSight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html) in the Amazon QuickSight User Guide. For more information about using Active Directory in Amazon QuickSight, see [Using Active Directory with Amazon QuickSight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/aws-directory-service.html) in the Amazon QuickSight User Guide.

(string)

Syntax:

```
"string" "string" ...
```

`--author-pro-group` (list)

The author pro group associated with your Active Directory or IAM Identity Center account.

For more information about using IAM Identity Center in Amazon QuickSight, see [Using IAM Identity Center with Amazon QuickSight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html) in the Amazon QuickSight User Guide. For more information about using Active Directory in Amazon QuickSight, see [Using Active Directory with Amazon QuickSight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/aws-directory-service.html) in the Amazon QuickSight User Guide.

(string)

Syntax:

```
"string" "string" ...
```

`--reader-pro-group` (list)

The reader pro group associated with your Active Directory or IAM Identity Center account.

For more information about using IAM Identity Center in Amazon QuickSight, see [Using IAM Identity Center with Amazon QuickSight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html) in the Amazon QuickSight User Guide. For more information about using Active Directory in Amazon QuickSight, see [Using Active Directory with Amazon QuickSight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/aws-directory-service.html) in the Amazon QuickSight User Guide.

(string)

Syntax:

```
"string" "string" ...
```

`--first-name` (string)

The first name of the author of the Amazon QuickSight account to use for future communications. This field is required if `ENTERPPRISE_AND_Q` is the selected edition of the new Amazon QuickSight account.

`--last-name` (string)

The last name of the author of the Amazon QuickSight account to use for future communications. This field is required if `ENTERPPRISE_AND_Q` is the selected edition of the new Amazon QuickSight account.

`--email-address` (string)

The email address of the author of the Amazon QuickSight account to use for future communications. This field is required if `ENTERPPRISE_AND_Q` is the selected edition of the new Amazon QuickSight account.

`--contact-number` (string)

A 10-digit phone number for the author of the Amazon QuickSight account to use for future communications. This field is required if `ENTERPPRISE_AND_Q` is the selected edition of the new Amazon QuickSight account.

`--iam-identity-center-instance-arn` (string)

The Amazon Resource Name (ARN) for the IAM Identity Center instance.

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

SignupResponse -> (structure)

A `SignupResponse` object that returns information about a newly created Amazon QuickSight account.

IAMUser -> (boolean)

A Boolean that is `TRUE` if the Amazon QuickSight uses IAM as an authentication method.

userLoginName -> (string)

The user login name for your Amazon QuickSight account.

accountName -> (string)

The name of your Amazon QuickSight account.

directoryType -> (string)

The type of Active Directory that is being used to authenticate the Amazon QuickSight account. Valid values are `SIMPLE_AD` , `AD_CONNECTOR` , and `MICROSOFT_AD` .

Status -> (integer)

The HTTP status of the request.

RequestId -> (string)

The Amazon Web Services request ID for this operation.