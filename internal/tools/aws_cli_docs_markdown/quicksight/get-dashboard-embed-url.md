# get-dashboard-embed-urlÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/get-dashboard-embed-url.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/get-dashboard-embed-url.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [quicksight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/index.html#cli-aws-quicksight) ]

# get-dashboard-embed-url

## Description

Generates a temporary session URL and authorization code(bearer token) that you can use to embed an Amazon QuickSight read-only dashboard in your website or application. Before you use this command, make sure that you have configured the dashboards and permissions.

Currently, you can use `GetDashboardEmbedURL` only from the server, not from the userâs browser. The following rules apply to the generated URL:

- They must be used together.
- They can be used one time only.
- They are valid for 5 minutes after you run this command.
- You are charged only when the URL is used or there is interaction with Amazon QuickSight.
- The resulting user session is valid for 15 minutes (default) up to 10 hours (maximum). You can use the optional `SessionLifetimeInMinutes` parameter to customize session duration.

For more information, see [Embedding Analytics Using GetDashboardEmbedUrl](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-deprecated.html) in the *Amazon QuickSight User Guide* .

For more information about the high-level steps for embedding and for an interactive demo of the ways you can customize embedding, visit the [Amazon QuickSight Developer Portal](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-dev-portal.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/GetDashboardEmbedUrl)

## Synopsis

```
get-dashboard-embed-url
--aws-account-id <value>
--dashboard-id <value>
--identity-type <value>
[--session-lifetime-in-minutes <value>]
[--undo-redo-disabled | --no-undo-redo-disabled]
[--reset-disabled | --no-reset-disabled]
[--state-persistence-enabled | --no-state-persistence-enabled]
[--user-arn <value>]
[--namespace <value>]
[--additional-dashboard-ids <value>]
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

The ID for the Amazon Web Services account that contains the dashboard that youâre embedding.

`--dashboard-id` (string)

The ID for the dashboard, also added to the Identity and Access Management (IAM) policy.

`--identity-type` (string)

The authentication method that the user uses to sign in.

Possible values:

- `IAM`
- `QUICKSIGHT`
- `ANONYMOUS`

`--session-lifetime-in-minutes` (long)

How many minutes the session is valid. The session lifetime must be 15-600 minutes.

`--undo-redo-disabled` | `--no-undo-redo-disabled` (boolean)

Remove the undo/redo button on the embedded dashboard. The default is FALSE, which enables the undo/redo button.

`--reset-disabled` | `--no-reset-disabled` (boolean)

Remove the reset button on the embedded dashboard. The default is FALSE, which enables the reset button.

`--state-persistence-enabled` | `--no-state-persistence-enabled` (boolean)

Adds persistence of state for the user session in an embedded dashboard. Persistence applies to the sheet and the parameter settings. These are control settings that the dashboard subscriber (Amazon QuickSight reader) chooses while viewing the dashboard. If this is set to `TRUE` , the settings are the same when the subscriber reopens the same dashboard URL. The state is stored in Amazon QuickSight, not in a browser cookie. If this is set to FALSE, the state of the user session is not persisted. The default is `FALSE` .

`--user-arn` (string)

The Amazon QuickSight userâs Amazon Resource Name (ARN), for use with `QUICKSIGHT` identity type. You can use this for any Amazon QuickSight users in your account (readers, authors, or admins) authenticated as one of the following:

- Active Directory (AD) users or group members
- Invited nonfederated users
- IAM users and IAM role-based sessions authenticated through Federated Single Sign-On using SAML, OpenID Connect, or IAM federation.

Omit this parameter for users in the third group â IAM users and IAM role-based sessions.

`--namespace` (string)

The Amazon QuickSight namespace that contains the dashboard IDs in this request. If youâre not using a custom namespace, set `Namespace = default` .

`--additional-dashboard-ids` (list)

A list of one or more dashboard IDs that you want anonymous users to have tempporary access to. Currently, the `IdentityType` parameter must be set to `ANONYMOUS` because other identity types authenticate as Amazon QuickSight or IAM users. For example, if you set â`--dashboard-id dash_id1 --dashboard-id dash_id2 dash_id3 identity-type ANONYMOUS` â, the session can access all three dashboards.

(string)

Syntax:

```
"string" "string" ...
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

EmbedUrl -> (string)

A single-use URL that you can put into your server-side webpage to embed your dashboard. This URL is valid for 5 minutes. The API operation provides the URL with an `auth_code` value that enables one (and only one) sign-on to a user session that is valid for 10 hours.

Status -> (integer)

The HTTP status of the request.

RequestId -> (string)

The Amazon Web Services request ID for this operation.