# update-userÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-user.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-user.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [quicksight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/index.html#cli-aws-quicksight) ]

# update-user

## Description

Updates an Amazon QuickSight user.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/UpdateUser)

## Synopsis

```
update-user
--user-name <value>
--aws-account-id <value>
--namespace <value>
--email <value>
--role <value>
[--custom-permissions-name <value>]
[--unapply-custom-permissions | --no-unapply-custom-permissions]
[--external-login-federation-provider-type <value>]
[--custom-federation-provider-url <value>]
[--external-login-id <value>]
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

`--user-name` (string)

The Amazon QuickSight user name that you want to update.

`--aws-account-id` (string)

The ID for the Amazon Web Services account that the user is in. Currently, you use the ID for the Amazon Web Services account that contains your Amazon QuickSight account.

`--namespace` (string)

The namespace. Currently, you should set this to `default` .

`--email` (string)

The email address of the user that you want to update.

`--role` (string)

The Amazon QuickSight role of the user. The role can be one of the following default security cohorts:

- `READER` : A user who has read-only access to dashboards.
- `AUTHOR` : A user who can create data sources, datasets, analyses, and dashboards.
- `ADMIN` : A user who is an author, who can also manage Amazon QuickSight settings.
- `READER_PRO` : Reader Pro adds Generative BI capabilities to the Reader role. Reader Pros have access to Amazon Q in Amazon QuickSight, can build stories with Amazon Q, and can generate executive summaries from dashboards.
- `AUTHOR_PRO` : Author Pro adds Generative BI capabilities to the Author role. Author Pros can author dashboards with natural language with Amazon Q, build stories with Amazon Q, create Topics for Q&A, and generate executive summaries from dashboards.
- `ADMIN_PRO` : Admin Pros are Author Pros who can also manage Amazon QuickSight administrative settings. Admin Pro users are billed at Author Pro pricing.

The name of the Amazon QuickSight role is invisible to the user except for the console screens dealing with permissions.

Possible values:

- `ADMIN`
- `AUTHOR`
- `READER`
- `RESTRICTED_AUTHOR`
- `RESTRICTED_READER`
- `ADMIN_PRO`
- `AUTHOR_PRO`
- `READER_PRO`

`--custom-permissions-name` (string)

(Enterprise edition only) The name of the custom permissions profile that you want to assign to this user. Customized permissions allows you to control a userâs access by restricting access the following operations:

- Create and update data sources
- Create and update datasets
- Create and update email reports
- Subscribe to email reports

A set of custom permissions includes any combination of these restrictions. Currently, you need to create the profile names for custom permission sets by using the Amazon QuickSight console. Then, you use the `RegisterUser` API operation to assign the named set of permissions to a Amazon QuickSight user.

Amazon QuickSight custom permissions are applied through IAM policies. Therefore, they override the permissions typically granted by assigning Amazon QuickSight users to one of the default security cohorts in Amazon QuickSight (admin, author, reader).

This feature is available only to Amazon QuickSight Enterprise edition subscriptions.

`--unapply-custom-permissions` | `--no-unapply-custom-permissions` (boolean)

A flag that you use to indicate that you want to remove all custom permissions from this user. Using this parameter resets the user to the state it was in before a custom permissions profile was applied. This parameter defaults to NULL and it doesnât accept any other value.

`--external-login-federation-provider-type` (string)

The type of supported external login provider that provides identity to let a user federate into Amazon QuickSight with an associated Identity and Access Management(IAM) role. The type of supported external login provider can be one of the following.

- `COGNITO` : Amazon Cognito. The provider URL is cognito-identity.amazonaws.com. When choosing the `COGNITO` provider type, donât use the âCustomFederationProviderUrlâ parameter which is only needed when the external provider is custom.
- `CUSTOM_OIDC` : Custom OpenID Connect (OIDC) provider. When choosing `CUSTOM_OIDC` type, use the `CustomFederationProviderUrl` parameter to provide the custom OIDC provider URL.
- `NONE` : This clears all the previously saved external login information for a user. Use the `` [DescribeUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeUser.html) `` API operation to check the external login information.

`--custom-federation-provider-url` (string)

The URL of the custom OpenID Connect (OIDC) provider that provides identity to let a user federate into Amazon QuickSight with an associated Identity and Access Management(IAM) role. This parameter should only be used when `ExternalLoginFederationProviderType` parameter is set to `CUSTOM_OIDC` .

`--external-login-id` (string)

The identity ID for a user in the external login provider.

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

User -> (structure)

The Amazon QuickSight user.

Arn -> (string)

The Amazon Resource Name (ARN) for the user.

UserName -> (string)

The userâs user name. This value is required if you are registering a user that will be managed in Amazon QuickSight. In the output, the value for `UserName` is `N/A` when the value for `IdentityType` is `IAM` and the corresponding IAM user is deleted.

Email -> (string)

The userâs email address.

Role -> (string)

The Amazon QuickSight role for the user. The user role can be one of the following:.

- `READER` : A user who has read-only access to dashboards.
- `AUTHOR` : A user who can create data sources, datasets, analyses, and dashboards.
- `ADMIN` : A user who is an author, who can also manage Amazon Amazon QuickSight settings.
- `READER_PRO` : Reader Pro adds Generative BI capabilities to the Reader role. Reader Pros have access to Amazon Q in Amazon QuickSight, can build stories with Amazon Q, and can generate executive summaries from dashboards.
- `AUTHOR_PRO` : Author Pro adds Generative BI capabilities to the Author role. Author Pros can author dashboards with natural language with Amazon Q, build stories with Amazon Q, create Topics for Q&A, and generate executive summaries from dashboards.
- `ADMIN_PRO` : Admin Pros are Author Pros who can also manage Amazon QuickSight administrative settings. Admin Pro users are billed at Author Pro pricing.
- `RESTRICTED_READER` : This role isnât currently available for use.
- `RESTRICTED_AUTHOR` : This role isnât currently available for use.

IdentityType -> (string)

The type of identity authentication used by the user.

Active -> (boolean)

The active status of user. When you create an Amazon QuickSight user thatâs not an IAM user or an Active Directory user, that user is inactive until they sign in and provide a password.

PrincipalId -> (string)

The principal ID of the user.

CustomPermissionsName -> (string)

The custom permissions profile associated with this user.

ExternalLoginFederationProviderType -> (string)

The type of supported external login provider that provides identity to let the user federate into Amazon QuickSight with an associated IAM role. The type can be one of the following.

- `COGNITO` : Amazon Cognito. The provider URL is cognito-identity.amazonaws.com.
- `CUSTOM_OIDC` : Custom OpenID Connect (OIDC) provider.

ExternalLoginFederationProviderUrl -> (string)

The URL of the external login provider.

ExternalLoginId -> (string)

The identity ID for the user in the external login provider.

RequestId -> (string)

The Amazon Web Services request ID for this operation.

Status -> (integer)

The HTTP status of the request.