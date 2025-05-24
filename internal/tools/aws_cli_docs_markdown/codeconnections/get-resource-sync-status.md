# get-resource-sync-statusÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/get-resource-sync-status.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/get-resource-sync-status.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codeconnections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeconnections/index.html#cli-aws-codeconnections) ]

# get-resource-sync-status

## Description

Returns the status of the sync with the Git repository for a specific Amazon Web Services resource.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codeconnections-2023-12-01/GetResourceSyncStatus)

## Synopsis

```
get-resource-sync-status
--resource-name <value>
--sync-type <value>
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

`--resource-name` (string)

The name of the Amazon Web Services resource for the sync status with the Git repository.

`--sync-type` (string)

The sync type for the sync status with the Git repository.

Possible values:

- `CFN_STACK_SYNC`

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

DesiredState -> (structure)

The desired state of the Amazon Web Services resource for the sync status with the Git repository.

Branch -> (string)

The branch name for a specific revision.

Directory -> (string)

The directory, if any, for a specific revision.

OwnerId -> (string)

The owner ID for a specific revision, such as the GitHub owner ID for a GitHub repository.

RepositoryName -> (string)

The repository name for a specific revision.

ProviderType -> (string)

The provider type for a revision, such as GitHub.

Sha -> (string)

The SHA, such as the commit ID, for a specific revision.

LatestSuccessfulSync -> (structure)

The latest successful sync for the sync status with the Git repository.

Events -> (list)

The events related to a resource sync attempt.

(structure)

Information about a resource sync event for the resource associated with a sync configuration.

Event -> (string)

The event for a resource sync event.

ExternalId -> (string)

The ID for a resource sync event.

Time -> (timestamp)

The time that a resource sync event occurred.

Type -> (string)

The type of resource sync event.

InitialRevision -> (structure)

The current state of the resource as defined in the resourceâs `config-file` in the linked repository.

Branch -> (string)

The branch name for a specific revision.

Directory -> (string)

The directory, if any, for a specific revision.

OwnerId -> (string)

The owner ID for a specific revision, such as the GitHub owner ID for a GitHub repository.

RepositoryName -> (string)

The repository name for a specific revision.

ProviderType -> (string)

The provider type for a revision, such as GitHub.

Sha -> (string)

The SHA, such as the commit ID, for a specific revision.

StartedAt -> (timestamp)

The start time for a resource sync attempt.

Status -> (string)

The status for a resource sync attempt. The follow are valid statuses:

- SYNC-INITIATED - A resource sync attempt has been created and will begin soon.
- SYNCING - Syncing has started and work is being done to reconcile state.
- SYNCED - Syncing has completed successfully.
- SYNC_FAILED - A resource sync attempt has failed.

TargetRevision -> (structure)

The desired state of the resource as defined in the resourceâs `config-file` in the linked repository. Git sync attempts to update the resource to this state.

Branch -> (string)

The branch name for a specific revision.

Directory -> (string)

The directory, if any, for a specific revision.

OwnerId -> (string)

The owner ID for a specific revision, such as the GitHub owner ID for a GitHub repository.

RepositoryName -> (string)

The repository name for a specific revision.

ProviderType -> (string)

The provider type for a revision, such as GitHub.

Sha -> (string)

The SHA, such as the commit ID, for a specific revision.

Target -> (string)

The name of the Amazon Web Services resource that is attempted to be synchronized.

LatestSync -> (structure)

The latest sync for the sync status with the Git repository, whether successful or not.

Events -> (list)

The events related to a resource sync attempt.

(structure)

Information about a resource sync event for the resource associated with a sync configuration.

Event -> (string)

The event for a resource sync event.

ExternalId -> (string)

The ID for a resource sync event.

Time -> (timestamp)

The time that a resource sync event occurred.

Type -> (string)

The type of resource sync event.

InitialRevision -> (structure)

The current state of the resource as defined in the resourceâs `config-file` in the linked repository.

Branch -> (string)

The branch name for a specific revision.

Directory -> (string)

The directory, if any, for a specific revision.

OwnerId -> (string)

The owner ID for a specific revision, such as the GitHub owner ID for a GitHub repository.

RepositoryName -> (string)

The repository name for a specific revision.

ProviderType -> (string)

The provider type for a revision, such as GitHub.

Sha -> (string)

The SHA, such as the commit ID, for a specific revision.

StartedAt -> (timestamp)

The start time for a resource sync attempt.

Status -> (string)

The status for a resource sync attempt. The follow are valid statuses:

- SYNC-INITIATED - A resource sync attempt has been created and will begin soon.
- SYNCING - Syncing has started and work is being done to reconcile state.
- SYNCED - Syncing has completed successfully.
- SYNC_FAILED - A resource sync attempt has failed.

TargetRevision -> (structure)

The desired state of the resource as defined in the resourceâs `config-file` in the linked repository. Git sync attempts to update the resource to this state.

Branch -> (string)

The branch name for a specific revision.

Directory -> (string)

The directory, if any, for a specific revision.

OwnerId -> (string)

The owner ID for a specific revision, such as the GitHub owner ID for a GitHub repository.

RepositoryName -> (string)

The repository name for a specific revision.

ProviderType -> (string)

The provider type for a revision, such as GitHub.

Sha -> (string)

The SHA, such as the commit ID, for a specific revision.

Target -> (string)

The name of the Amazon Web Services resource that is attempted to be synchronized.