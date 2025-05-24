# update-slack-channel-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support-app/update-slack-channel-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support-app/update-slack-channel-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [support-app](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support-app/index.html#cli-aws-support-app) ]

# update-slack-channel-configuration

## Description

Updates the configuration for a Slack channel, such as case update notifications.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/support-app-2021-08-20/UpdateSlackChannelConfiguration)

## Synopsis

```
update-slack-channel-configuration
--channel-id <value>
[--channel-name <value>]
[--channel-role-arn <value>]
[--notify-on-add-correspondence-to-case | --no-notify-on-add-correspondence-to-case]
[--notify-on-case-severity <value>]
[--notify-on-create-or-reopen-case | --no-notify-on-create-or-reopen-case]
[--notify-on-resolve-case | --no-notify-on-resolve-case]
--team-id <value>
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

`--channel-id` (string)

The channel ID in Slack. This ID identifies a channel within a Slack workspace.

`--channel-name` (string)

The Slack channel name that you want to update.

`--channel-role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role that you want to use to perform operations on Amazon Web Services. For more information, see [Managing access to the Amazon Web Services Support App](https://docs.aws.amazon.com/awssupport/latest/user/support-app-permissions.html) in the *Amazon Web Services Support User Guide* .

`--notify-on-add-correspondence-to-case` | `--no-notify-on-add-correspondence-to-case` (boolean)

Whether you want to get notified when a support case has a new correspondence.

`--notify-on-case-severity` (string)

The case severity for a support case that you want to receive notifications.

If you specify `high` or `all` , at least one of the following parameters must be `true` :

- `notifyOnAddCorrespondenceToCase`
- `notifyOnCreateOrReopenCase`
- `notifyOnResolveCase`

If you specify `none` , any of the following parameters that you specify in your request must be `false` :

- `notifyOnAddCorrespondenceToCase`
- `notifyOnCreateOrReopenCase`
- `notifyOnResolveCase`

### Note

If you donât specify these parameters in your request, the Amazon Web Services Support App uses the current values by default.

Possible values:

- `none`
- `all`
- `high`

`--notify-on-create-or-reopen-case` | `--no-notify-on-create-or-reopen-case` (boolean)

Whether you want to get notified when a support case is created or reopened.

`--notify-on-resolve-case` | `--no-notify-on-resolve-case` (boolean)

Whether you want to get notified when a support case is resolved.

`--team-id` (string)

The team ID in Slack. This ID uniquely identifies a Slack workspace, such as `T012ABCDEFG` .

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

channelId -> (string)

The channel ID in Slack. This ID identifies a channel within a Slack workspace.

channelName -> (string)

The name of the Slack channel that you configure for the Amazon Web Services Support App.

channelRoleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role that you want to use to perform operations on Amazon Web Services. For more information, see [Managing access to the Amazon Web Services Support App](https://docs.aws.amazon.com/awssupport/latest/user/support-app-permissions.html) in the *Amazon Web Services Support User Guide* .

notifyOnAddCorrespondenceToCase -> (boolean)

Whether you want to get notified when a support case has a new correspondence.

notifyOnCaseSeverity -> (string)

The case severity for a support case that you want to receive notifications.

notifyOnCreateOrReopenCase -> (boolean)

Whether you want to get notified when a support case is created or reopened.

notifyOnResolveCase -> (boolean)

Whether you want to get notified when a support case is resolved.

teamId -> (string)

The team ID in Slack. This ID uniquely identifies a Slack workspace, such as `T012ABCDEFG` .