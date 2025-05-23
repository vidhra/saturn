# update-appÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/update-app.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/update-app.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/index.html#cli-aws-sms) ]

# update-app

## Description

Updates the specified application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/UpdateApp)

## Synopsis

```
update-app
[--app-id <value>]
[--name <value>]
[--description <value>]
[--role-name <value>]
[--server-groups <value>]
[--tags <value>]
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

`--app-id` (string)

The ID of the application.

`--name` (string)

The new name of the application.

`--description` (string)

The new description of the application.

`--role-name` (string)

The name of the service role in the customerâs account used by Server Migration Service.

`--server-groups` (list)

The server groups in the application to update.

(structure)

Logical grouping of servers.

serverGroupId -> (string)

The ID of a server group.

name -> (string)

The name of a server group.

serverList -> (list)

The servers that belong to a server group.

(structure)

Represents a server.

serverId -> (string)

The ID of the server.

serverType -> (string)

The type of server.

vmServer -> (structure)

Information about the VM server.

vmServerAddress -> (structure)

The VM server location.

vmManagerId -> (string)

The ID of the VM manager.

vmId -> (string)

The ID of the VM.

vmName -> (string)

The name of the VM.

vmManagerName -> (string)

The name of the VM manager.

vmManagerType -> (string)

The type of VM management product.

vmPath -> (string)

The VM folder path in the vCenter Server virtual machine inventory tree.

replicationJobId -> (string)

The ID of the replication job.

replicationJobTerminated -> (boolean)

Indicates whether the replication job is deleted or failed.

JSON Syntax:

```
[
  {
    "serverGroupId": "string",
    "name": "string",
    "serverList": [
      {
        "serverId": "string",
        "serverType": "VIRTUAL_MACHINE",
        "vmServer": {
          "vmServerAddress": {
            "vmManagerId": "string",
            "vmId": "string"
          },
          "vmName": "string",
          "vmManagerName": "string",
          "vmManagerType": "VSPHERE"|"SCVMM"|"HYPERV-MANAGER",
          "vmPath": "string"
        },
        "replicationJobId": "string",
        "replicationJobTerminated": true|false
      }
      ...
    ]
  }
  ...
]
```

`--tags` (list)

The tags to associate with the application.

(structure)

Key/value pair that can be assigned to an application.

key -> (string)

The tag key.

value -> (string)

The tag value.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
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

appSummary -> (structure)

A summary description of the application.

appId -> (string)

The unique ID of the application.

importedAppId -> (string)

The ID of the application.

name -> (string)

The name of the application.

description -> (string)

The description of the application.

status -> (string)

Status of the application.

statusMessage -> (string)

A message related to the status of the application

replicationConfigurationStatus -> (string)

Status of the replication configuration.

replicationStatus -> (string)

The replication status of the application.

replicationStatusMessage -> (string)

A message related to the replication status of the application.

latestReplicationTime -> (timestamp)

The timestamp of the applicationâs most recent successful replication.

launchConfigurationStatus -> (string)

Status of the launch configuration.

launchStatus -> (string)

The launch status of the application.

launchStatusMessage -> (string)

A message related to the launch status of the application.

launchDetails -> (structure)

Details about the latest launch of the application.

latestLaunchTime -> (timestamp)

The latest time that this application was launched successfully.

stackName -> (string)

The name of the latest stack launched for this application.

stackId -> (string)

The ID of the latest stack launched for this application.

creationTime -> (timestamp)

The creation time of the application.

lastModified -> (timestamp)

The last modified time of the application.

roleName -> (string)

The name of the service role in the customerâs account used by Server Migration Service.

totalServerGroups -> (integer)

The number of server groups present in the application.

totalServers -> (integer)

The number of servers present in the application.

serverGroups -> (list)

The updated server groups in the application.

(structure)

Logical grouping of servers.

serverGroupId -> (string)

The ID of a server group.

name -> (string)

The name of a server group.

serverList -> (list)

The servers that belong to a server group.

(structure)

Represents a server.

serverId -> (string)

The ID of the server.

serverType -> (string)

The type of server.

vmServer -> (structure)

Information about the VM server.

vmServerAddress -> (structure)

The VM server location.

vmManagerId -> (string)

The ID of the VM manager.

vmId -> (string)

The ID of the VM.

vmName -> (string)

The name of the VM.

vmManagerName -> (string)

The name of the VM manager.

vmManagerType -> (string)

The type of VM management product.

vmPath -> (string)

The VM folder path in the vCenter Server virtual machine inventory tree.

replicationJobId -> (string)

The ID of the replication job.

replicationJobTerminated -> (boolean)

Indicates whether the replication job is deleted or failed.

tags -> (list)

The tags associated with the application.

(structure)

Key/value pair that can be assigned to an application.

key -> (string)

The tag key.

value -> (string)

The tag value.