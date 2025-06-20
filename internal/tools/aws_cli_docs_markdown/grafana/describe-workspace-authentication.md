# describe-workspace-authenticationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/grafana/describe-workspace-authentication.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/grafana/describe-workspace-authentication.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [grafana](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/grafana/index.html#cli-aws-grafana) ]

# describe-workspace-authentication

## Description

Displays information about the authentication methods used in one Amazon Managed Grafana workspace.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/grafana-2020-08-18/DescribeWorkspaceAuthentication)

## Synopsis

```
describe-workspace-authentication
--workspace-id <value>
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

`--workspace-id` (string)

The ID of the workspace to return authentication information about.

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

authentication -> (structure)

A structure containing information about the authentication methods used in the workspace.

awsSso -> (structure)

A structure containing information about how this workspace works with IAM Identity Center.

ssoClientId -> (string)

The ID of the IAM Identity Center-managed application that is created by Amazon Managed Grafana.

providers -> (list)

Specifies whether this workspace uses IAM Identity Center, SAML, or both methods to authenticate users to use the Grafana console in the Amazon Managed Grafana workspace.

(string)

saml -> (structure)

A structure containing information about how this workspace works with SAML, including what attributes within the assertion are to be mapped to user information in the workspace.

configuration -> (structure)

A structure containing details about how this workspace works with SAML.

allowedOrganizations -> (list)

Lists which organizations defined in the SAML assertion are allowed to use the Amazon Managed Grafana workspace. If this is empty, all organizations in the assertion attribute have access.

(string)

assertionAttributes -> (structure)

A structure that defines which attributes in the SAML assertion are to be used to define information about the users authenticated by that IdP to use the workspace.

email -> (string)

The name of the attribute within the SAML assertion to use as the email names for SAML users.

groups -> (string)

The name of the attribute within the SAML assertion to use as the user full âfriendlyâ names for user groups.

login -> (string)

The name of the attribute within the SAML assertion to use as the login names for SAML users.

name -> (string)

The name of the attribute within the SAML assertion to use as the user full âfriendlyâ names for SAML users.

org -> (string)

The name of the attribute within the SAML assertion to use as the user full âfriendlyâ names for the usersâ organizations.

role -> (string)

The name of the attribute within the SAML assertion to use as the user roles.

idpMetadata -> (tagged union structure)

A structure containing the identity provider (IdP) metadata used to integrate the identity provider with this workspace.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `url`, `xml`.

url -> (string)

The URL of the location containing the IdP metadata.

xml -> (string)

The full IdP metadata, in XML format.

loginValidityDuration -> (integer)

How long a sign-on session by a SAML user is valid, before the user has to sign on again.

roleValues -> (structure)

A structure containing arrays that map group names in the SAML assertion to the Grafana `Admin` and `Editor` roles in the workspace.

admin -> (list)

A list of groups from the SAML assertion attribute to grant the Grafana `Admin` role to.

(string)

editor -> (list)

A list of groups from the SAML assertion attribute to grant the Grafana `Editor` role to.

(string)

status -> (string)

Specifies whether the workspaceâs SAML configuration is complete.