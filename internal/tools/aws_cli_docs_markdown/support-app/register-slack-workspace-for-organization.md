# register-slack-workspace-for-organizationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support-app/register-slack-workspace-for-organization.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support-app/register-slack-workspace-for-organization.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [support-app](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support-app/index.html#cli-aws-support-app) ]

# register-slack-workspace-for-organization

## Description

Registers a Slack workspace for your Amazon Web Services account. To call this API, your account must be part of an organization in Organizations.

If youâre the *management account* and you want to register Slack workspaces for your organization, you must complete the following tasks:

- Sign in to the [Amazon Web Services Support Center](https://console.aws.amazon.com/support/app) and authorize the Slack workspaces where you want your organization to have access to. See [Authorize a Slack workspace](https://docs.aws.amazon.com/awssupport/latest/user/authorize-slack-workspace.html) in the *Amazon Web Services Support User Guide* .
- Call the `RegisterSlackWorkspaceForOrganization` API to authorize each Slack workspace for the organization.

After the management account authorizes the Slack workspace, member accounts can call this API to authorize the same Slack workspace for their individual accounts. Member accounts donât need to authorize the Slack workspace manually through the [Amazon Web Services Support Center](https://console.aws.amazon.com/support/app) .

To use the Amazon Web Services Support App, each account must then complete the following tasks:

- Create an Identity and Access Management (IAM) role with the required permission. For more information, see [Managing access to the Amazon Web Services Support App](https://docs.aws.amazon.com/awssupport/latest/user/support-app-permissions.html) .
- Configure a Slack channel to use the Amazon Web Services Support App for support cases for that account. For more information, see [Configuring a Slack channel](https://docs.aws.amazon.com/awssupport/latest/user/add-your-slack-channel.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/support-app-2021-08-20/RegisterSlackWorkspaceForOrganization)

## Synopsis

```
register-slack-workspace-for-organization
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

`--team-id` (string)

The team ID in Slack. This ID uniquely identifies a Slack workspace, such as `T012ABCDEFG` . Specify the Slack workspace that you want to use for your organization.

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

accountType -> (string)

Whether the Amazon Web Services account is a management or member account thatâs part of an organization in Organizations.

teamId -> (string)

The team ID in Slack. This ID uniquely identifies a Slack workspace, such as `T012ABCDEFG` .

teamName -> (string)

The name of the Slack workspace.