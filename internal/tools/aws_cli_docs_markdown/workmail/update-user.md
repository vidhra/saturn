# update-userÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/update-user.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/update-user.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [workmail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/index.html#cli-aws-workmail) ]

# update-user

## Description

Updates data for the user. To have the latest information, it must be preceded by a  DescribeUser call. The dataset in the request should be the one expected when performing another `DescribeUser` call.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/UpdateUser)

## Synopsis

```
update-user
--organization-id <value>
--user-id <value>
[--role <value>]
[--display-name <value>]
[--first-name <value>]
[--last-name <value>]
[--hidden-from-global-address-list | --no-hidden-from-global-address-list]
[--initials <value>]
[--telephone <value>]
[--street <value>]
[--job-title <value>]
[--city <value>]
[--company <value>]
[--zip-code <value>]
[--department <value>]
[--country <value>]
[--office <value>]
[--identity-provider-user-id <value>]
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

`--organization-id` (string)

The identifier for the organization under which the user exists.

`--user-id` (string)

The identifier for the user to be updated.

The identifier can be the *UserId* , *Username* , or *email* . The following identity formats are available:

- User ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234
- Email address: [user@domain.tld](mailto:user%40domain.tld)
- User name: user

`--role` (string)

Updates the user role.

You cannot pass *SYSTEM_USER* or *RESOURCE* .

Possible values:

- `USER`
- `RESOURCE`
- `SYSTEM_USER`
- `REMOTE_USER`

`--display-name` (string)

Updates the display name of the user.

`--first-name` (string)

Updates the userâs first name.

`--last-name` (string)

Updates the userâs last name.

`--hidden-from-global-address-list` | `--no-hidden-from-global-address-list` (boolean)

If enabled, the user is hidden from the global address list.

`--initials` (string)

Updates the userâs initials.

`--telephone` (string)

Updates the userâs contact details.

`--street` (string)

Updates the userâs street address.

`--job-title` (string)

Updates the userâs job title.

`--city` (string)

Updates the userâs city.

`--company` (string)

Updates the userâs company.

`--zip-code` (string)

Updates the userâs zip code.

`--department` (string)

Updates the userâs department.

`--country` (string)

Updates the userâs country.

`--office` (string)

Updates the userâs office.

`--identity-provider-user-id` (string)

User ID from the IAM Identity Center. If this parameter is empty it will be updated automatically when the user logs in for the first time to the mailbox associated with WorkMail.

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

None