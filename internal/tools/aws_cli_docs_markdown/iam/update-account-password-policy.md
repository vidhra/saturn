# update-account-password-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-account-password-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-account-password-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iam](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html#cli-aws-iam) ]

# update-account-password-policy

## Description

Updates the password policy settings for the Amazon Web Services account.

### Note

This operation does not support partial updates. No parameters are required, but if you do not specify a parameter, that parameterâs value reverts to its default value. See the **Request Parameters** section for each parameterâs default value. Also note that some parameters do not allow the default parameter to be explicitly set. Instead, to invoke the default value, do not include that parameter when you invoke the operation.

For more information about using a password policy, see [Managing an IAM password policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingPasswordPolicies.html) in the *IAM User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/UpdateAccountPasswordPolicy)

## Synopsis

```
update-account-password-policy
[--minimum-password-length <value>]
[--require-symbols | --no-require-symbols]
[--require-numbers | --no-require-numbers]
[--require-uppercase-characters | --no-require-uppercase-characters]
[--require-lowercase-characters | --no-require-lowercase-characters]
[--allow-users-to-change-password | --no-allow-users-to-change-password]
[--max-password-age <value>]
[--password-reuse-prevention <value>]
[--hard-expiry | --no-hard-expiry]
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

`--minimum-password-length` (integer)

The minimum number of characters allowed in an IAM user password.

If you do not specify a value for this parameter, then the operation uses the default value of `6` .

`--require-symbols` | `--no-require-symbols` (boolean)

Specifies whether IAM user passwords must contain at least one of the following non-alphanumeric characters:

! @ # $ % ^ & * ( ) _ + - = [ ] { } | â

If you do not specify a value for this parameter, then the operation uses the default value of `false` . The result is that passwords do not require at least one symbol character.

`--require-numbers` | `--no-require-numbers` (boolean)

Specifies whether IAM user passwords must contain at least one numeric character (0 to 9).

If you do not specify a value for this parameter, then the operation uses the default value of `false` . The result is that passwords do not require at least one numeric character.

`--require-uppercase-characters` | `--no-require-uppercase-characters` (boolean)

Specifies whether IAM user passwords must contain at least one uppercase character from the ISO basic Latin alphabet (A to Z).

If you do not specify a value for this parameter, then the operation uses the default value of `false` . The result is that passwords do not require at least one uppercase character.

`--require-lowercase-characters` | `--no-require-lowercase-characters` (boolean)

Specifies whether IAM user passwords must contain at least one lowercase character from the ISO basic Latin alphabet (a to z).

If you do not specify a value for this parameter, then the operation uses the default value of `false` . The result is that passwords do not require at least one lowercase character.

`--allow-users-to-change-password` | `--no-allow-users-to-change-password` (boolean)

Allows all IAM users in your account to use the Amazon Web Services Management Console to change their own passwords. For more information, see [Permitting IAM users to change their own passwords](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_enable-user-change.html) in the *IAM User Guide* .

If you do not specify a value for this parameter, then the operation uses the default value of `false` . The result is that IAM users in the account do not automatically have permissions to change their own password.

`--max-password-age` (integer)

The number of days that an IAM user password is valid.

If you do not specify a value for this parameter, then the operation uses the default value of `0` . The result is that IAM user passwords never expire.

`--password-reuse-prevention` (integer)

Specifies the number of previous passwords that IAM users are prevented from reusing.

If you do not specify a value for this parameter, then the operation uses the default value of `0` . The result is that IAM users are not prevented from reusing previous passwords.

`--hard-expiry` | `--no-hard-expiry` (boolean)

Prevents IAM users who are accessing the account via the Amazon Web Services Management Console from setting a new console password after their password has expired. The IAM user cannot access the console until an administrator resets the password.

If you do not specify a value for this parameter, then the operation uses the default value of `false` . The result is that IAM users can change their passwords after they expire and continue to sign in as the user.

### Note

In the Amazon Web Services Management Console, the custom password policy option **Allow users to change their own password** gives IAM users permissions to `iam:ChangePassword` for only their user and to the `iam:GetAccountPasswordPolicy` action. This option does not attach a permissions policy to each user, rather the permissions are applied at the account-level for all users by IAM. IAM users with `iam:ChangePassword` permission and active access keys can reset their own expired console password using the CLI or API.

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

**To set or change the current account password policy**

The following `update-account-password-policy` command sets the password policy to require a minimum length of eight
characters and to require one or more numbers in the password.

```
aws iam update-account-password-policy \
    --minimum-password-length 8 \
    --require-numbers
```

This command produces no output.

Changes to an accountâs password policy affect any new passwords that are created for IAM users in the account. Password
policy changes do not affect existing passwords.

For more information, see [Setting an account password policy for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html) in the *AWS IAM User Guide*.

## Output

None