# start-recoveryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/drs/start-recovery.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/drs/start-recovery.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [drs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/drs/index.html#cli-aws-drs) ]

# start-recovery

## Description

Launches Recovery Instances for the specified Source Servers. For each Source Server you may choose a point in time snapshot to launch from, or use an on demand snapshot.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/drs-2020-02-26/StartRecovery)

## Synopsis

```
start-recovery
[--is-drill | --no-is-drill]
--source-servers <value>
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

`--is-drill` | `--no-is-drill` (boolean)

Whether this Source Server Recovery operation is a drill or not.

`--source-servers` (list)

The Source Servers that we want to start a Recovery Job for.

(structure)

An object representing the Source Server to recover.

recoverySnapshotID -> (string)

The ID of a Recovery Snapshot we want to recover from. Omit this field to launch from the latest data by taking an on-demand snapshot.

sourceServerID -> (string)

The ID of the Source Server you want to recover.

Shorthand Syntax:

```
recoverySnapshotID=string,sourceServerID=string ...
```

JSON Syntax:

```
[
  {
    "recoverySnapshotID": "string",
    "sourceServerID": "string"
  }
  ...
]
```

`--tags` (map)

The tags to be associated with the Recovery Job.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

job -> (structure)

The Recovery Job.

arn -> (string)

The ARN of a Job.

creationDateTime -> (string)

The date and time of when the Job was created.

endDateTime -> (string)

The date and time of when the Job ended.

initiatedBy -> (string)

A string representing who initiated the Job.

jobID -> (string)

The ID of the Job.

participatingResources -> (list)

A list of resources that the Job is acting upon.

(structure)

Represents a resource participating in an asynchronous Job.

launchStatus -> (string)

The launch status of a participating resource.

participatingResourceID -> (tagged union structure)

The ID of a participating resource.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `sourceNetworkID`.

sourceNetworkID -> (string)

Source Network ID.

participatingServers -> (list)

A list of servers that the Job is acting upon.

(structure)

Represents a server participating in an asynchronous Job.

launchActionsStatus -> (structure)

The post-launch action runs of a participating server.

runs -> (list)

List of post launch action status.

(structure)

Launch action run.

action -> (structure)

Action.

actionCode -> (string)

Launch action code.

actionId -> (string)

Launch action Id.

actionVersion -> (string)

Launch action version.

active -> (boolean)

Whether the launch action is active.

category -> (string)

Launch action category.

description -> (string)

Launch action description.

name -> (string)

Launch action name.

optional -> (boolean)

Whether the launch will not be marked as failed if this action fails.

order -> (integer)

Launch action order.

parameters -> (map)

Launch action parameters.

key -> (string)

value -> (structure)

Launch action parameter.

type -> (string)

Type.

value -> (string)

Value.

type -> (string)

Launch action type.

failureReason -> (string)

Failure reason.

runId -> (string)

Run Id.

status -> (string)

Run status.

ssmAgentDiscoveryDatetime -> (string)

Time where the AWS Systems Manager was detected as running on the launched instance.

launchStatus -> (string)

The launch status of a participating server.

recoveryInstanceID -> (string)

The Recovery Instance ID of a participating server.

sourceServerID -> (string)

The Source Server ID of a participating server.

status -> (string)

The status of the Job.

tags -> (map)

A list of tags associated with the Job.

key -> (string)

value -> (string)

type -> (string)

The type of the Job.