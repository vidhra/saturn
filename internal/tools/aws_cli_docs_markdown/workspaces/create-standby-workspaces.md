# create-standby-workspacesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/create-standby-workspaces.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/create-standby-workspaces.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [workspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/index.html#cli-aws-workspaces) ]

# create-standby-workspaces

## Description

Creates a standby WorkSpace in a secondary Region.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/CreateStandbyWorkspaces)

## Synopsis

```
create-standby-workspaces
--primary-region <value>
--standby-workspaces <value>
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

`--primary-region` (string)

The Region of the primary WorkSpace.

`--standby-workspaces` (list)

Information about the standby WorkSpace to be created.

(structure)

Describes a standby WorkSpace.

PrimaryWorkspaceId -> (string)

The identifier of the standby WorkSpace.

VolumeEncryptionKey -> (string)

The volume encryption key of the standby WorkSpace.

DirectoryId -> (string)

The identifier of the directory for the standby WorkSpace.

Tags -> (list)

The tags associated with the standby WorkSpace.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.

DataReplication -> (string)

Indicates whether data replication is enabled, and if enabled, the type of data replication.

Shorthand Syntax:

```
PrimaryWorkspaceId=string,VolumeEncryptionKey=string,DirectoryId=string,Tags=[{Key=string,Value=string},{Key=string,Value=string}],DataReplication=string ...
```

JSON Syntax:

```
[
  {
    "PrimaryWorkspaceId": "string",
    "VolumeEncryptionKey": "string",
    "DirectoryId": "string",
    "Tags": [
      {
        "Key": "string",
        "Value": "string"
      }
      ...
    ],
    "DataReplication": "NO_REPLICATION"|"PRIMARY_AS_SOURCE"
  }
  ...
]
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

FailedStandbyRequests -> (list)

Information about the standby WorkSpace that could not be created.

(structure)

Describes the standby WorkSpace that could not be created.

StandbyWorkspaceRequest -> (structure)

Information about the standby WorkSpace that could not be created.

PrimaryWorkspaceId -> (string)

The identifier of the standby WorkSpace.

VolumeEncryptionKey -> (string)

The volume encryption key of the standby WorkSpace.

DirectoryId -> (string)

The identifier of the directory for the standby WorkSpace.

Tags -> (list)

The tags associated with the standby WorkSpace.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.

DataReplication -> (string)

Indicates whether data replication is enabled, and if enabled, the type of data replication.

ErrorCode -> (string)

The error code that is returned if the standby WorkSpace could not be created.

ErrorMessage -> (string)

The text of the error message that is returned if the standby WorkSpace could not be created.

PendingStandbyRequests -> (list)

Information about the standby WorkSpace that was created.

(structure)

Information about the standby WorkSpace.

UserName -> (string)

Describes the standby WorkSpace that was created.

Because this operation is asynchronous, the identifier returned is not immediately available for use with other operations. For example, if you call [DescribeWorkspaces](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaces.html) before the WorkSpace is created, the information returned can be incomplete.

DirectoryId -> (string)

The identifier of the directory for the standby WorkSpace.

State -> (string)

The operational state of the standby WorkSpace.

WorkspaceId -> (string)

The identifier of the standby WorkSpace.