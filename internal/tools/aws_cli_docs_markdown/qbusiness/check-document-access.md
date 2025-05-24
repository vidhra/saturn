# check-document-accessÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/check-document-access.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/check-document-access.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qbusiness](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/index.html#cli-aws-qbusiness) ]

# check-document-access

## Description

Verifies if a user has access permissions for a specified document and returns the actual ACL attached to the document. Resolves user access on the document via user aliases and groups when verifying user access.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qbusiness-2023-11-27/CheckDocumentAccess)

## Synopsis

```
check-document-access
--application-id <value>
--index-id <value>
--user-id <value>
--document-id <value>
[--data-source-id <value>]
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

`--application-id` (string)

The unique identifier of the application. This is required to identify the specific Amazon Q Business application context for the document access check.

`--index-id` (string)

The unique identifier of the index. Used to locate the correct index within the application where the document is stored.

`--user-id` (string)

The unique identifier of the user. Used to check the access permissions for this specific user against the documentâs ACL.

`--document-id` (string)

The unique identifier of the document. Specifies which documentâs access permissions are being checked.

`--data-source-id` (string)

The unique identifier of the data source. Identifies the specific data source from which the document originates. Should not be used when a document is uploaded directly with BatchPutDocument, as no dataSourceId is available or necessary.

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

userGroups -> (list)

An array of groups the user is part of for the specified data source. Each group has a name and type.

(structure)

Represents a group associated with a given user in the access control system.

name -> (string)

The name of the group associated with the user. This is used to identify the group in access control decisions.

type -> (string)

The type of the associated group. This indicates the scope of the groupâs applicability.

userAliases -> (list)

An array of aliases associated with the user. This includes both global and local aliases, each with a name and type.

(structure)

Represents an associated user in the access control system.

id -> (string)

The unique identifier of the associated user. This is used to identify the user in access control decisions.

type -> (string)

The type of the associated user. This indicates the scope of the userâs association.

hasAccess -> (boolean)

A boolean value indicating whether the specified user has access to the document, either direct access or transitive access via groups and aliases attached to the document.

documentAcl -> (structure)

The Access Control List (ACL) associated with the document. Includes allowlist and denylist conditions that determine user access.

allowlist -> (structure)

The allowlist conditions for the document. Users or groups matching these conditions are granted access to the document.

memberRelation -> (string)

The logical relation between members in the membership rule, determining how multiple conditions are combined.

conditions -> (list)

An array of conditions that define the membership rules. Each condition specifies criteria for users or groups to be included in this membership.

(structure)

Represents a condition in the documentâs ACL, specifying access rules for users and groups.

memberRelation -> (string)

The logical relation between members in the condition, determining how multiple user or group conditions are combined.

users -> (list)

An array of user identifiers that this condition applies to. Users listed here are subject to the access rule defined by this condition.

(structure)

Represents a user in the documentâs ACL, used to define access permissions for individual users.

id -> (string)

The unique identifier of the user in the documentâs ACL. This is used to identify the user when applying access rules.

type -> (string)

The type of the user. This indicates the scope of the userâs applicability in access control.

groups -> (list)

An array of group identifiers that this condition applies to. Groups listed here are subject to the access rule defined by this condition.

(structure)

Represents a group in the documentâs ACL, used to define access permissions for multiple users collectively.

name -> (string)

The name of the group in the documentâs ACL. This is used to identify the group when applying access rules.

type -> (string)

The type of the group. This indicates the scope of the groupâs applicability in access control.

denyList -> (structure)

The denylist conditions for the document. Users or groups matching these conditions are denied access to the document, overriding allowlist permissions.

memberRelation -> (string)

The logical relation between members in the membership rule, determining how multiple conditions are combined.

conditions -> (list)

An array of conditions that define the membership rules. Each condition specifies criteria for users or groups to be included in this membership.

(structure)

Represents a condition in the documentâs ACL, specifying access rules for users and groups.

memberRelation -> (string)

The logical relation between members in the condition, determining how multiple user or group conditions are combined.

users -> (list)

An array of user identifiers that this condition applies to. Users listed here are subject to the access rule defined by this condition.

(structure)

Represents a user in the documentâs ACL, used to define access permissions for individual users.

id -> (string)

The unique identifier of the user in the documentâs ACL. This is used to identify the user when applying access rules.

type -> (string)

The type of the user. This indicates the scope of the userâs applicability in access control.

groups -> (list)

An array of group identifiers that this condition applies to. Groups listed here are subject to the access rule defined by this condition.

(structure)

Represents a group in the documentâs ACL, used to define access permissions for multiple users collectively.

name -> (string)

The name of the group in the documentâs ACL. This is used to identify the group when applying access rules.

type -> (string)

The type of the group. This indicates the scope of the groupâs applicability in access control.