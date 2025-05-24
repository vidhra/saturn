# stop-replicationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgn/stop-replication.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgn/stop-replication.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mgn](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgn/index.html#cli-aws-mgn) ]

# stop-replication

## Description

Stop Replication.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mgn-2020-02-26/StopReplication)

## Synopsis

```
stop-replication
[--account-id <value>]
--source-server-id <value>
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

`--account-id` (string)

Stop Replication Request account ID.

`--source-server-id` (string)

Stop Replication Request source server ID.

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

applicationID -> (string)

Source server application ID.

arn -> (string)

Source server ARN.

connectorAction -> (structure)

Source Server connector action.

connectorArn -> (string)

Source Server connector action connector arn.

credentialsSecretArn -> (string)

Source Server connector action credentials secret arn.

dataReplicationInfo -> (structure)

Source server data replication info.

dataReplicationError -> (structure)

Error in obtaining data replication info.

error -> (string)

Error in data replication.

rawError -> (string)

Error in data replication.

dataReplicationInitiation -> (structure)

Request to query whether data replication has been initiated.

nextAttemptDateTime -> (string)

Request to query next data initiation date and time.

startDateTime -> (string)

Request to query data initiation start date and time.

steps -> (list)

Request to query data initiation steps.

(structure)

Data replication initiation step.

name -> (string)

Request to query data initiation step name.

status -> (string)

Request to query data initiation status.

dataReplicationState -> (string)

Request to query the data replication state.

etaDateTime -> (string)

Request to query the time when data replication will be complete.

lagDuration -> (string)

Request to query data replication lag duration.

lastSnapshotDateTime -> (string)

Request to query data replication last snapshot time.

replicatedDisks -> (list)

Request to query disks replicated.

(structure)

Request to query disks replicated.

backloggedStorageBytes -> (long)

Request to query data replication backlog size in bytes.

deviceName -> (string)

Request to query device name.

replicatedStorageBytes -> (long)

Request to query amount of data replicated in bytes.

rescannedStorageBytes -> (long)

Request to query amount of data rescanned in bytes.

totalStorageBytes -> (long)

Request to query total amount of data replicated in bytes.

fqdnForActionFramework -> (string)

Source server fqdn for action framework.

isArchived -> (boolean)

Source server archived status.

launchedInstance -> (structure)

Source server launched instance.

ec2InstanceID -> (string)

Launched instance EC2 ID.

firstBoot -> (string)

Launched instance first boot.

jobID -> (string)

Launched instance Job ID.

lifeCycle -> (structure)

Source server lifecycle state.

addedToServiceDateTime -> (string)

Lifecycle added to service data and time.

elapsedReplicationDuration -> (string)

Lifecycle elapsed time and duration.

firstByteDateTime -> (string)

Lifecycle replication initiation date and time.

lastCutover -> (structure)

Lifecycle last Cutover.

finalized -> (structure)

Lifecycle Cutover finalized date and time.

apiCallDateTime -> (string)

Lifecycle Cutover finalized date and time.

initiated -> (structure)

Lifecycle last Cutover initiated.

apiCallDateTime -> (string)

jobID -> (string)

Lifecycle last Cutover initiated by Job ID.

reverted -> (structure)

Lifecycle last Cutover reverted.

apiCallDateTime -> (string)

Lifecycle last Cutover reverted API call date time.

lastSeenByServiceDateTime -> (string)

Lifecycle last seen date and time.

lastTest -> (structure)

Lifecycle last Test.

finalized -> (structure)

Lifecycle last Test finalized.

apiCallDateTime -> (string)

Lifecycle Test failed API call date and time.

initiated -> (structure)

Lifecycle last Test initiated.

apiCallDateTime -> (string)

Lifecycle last Test initiated API call date and time.

jobID -> (string)

Lifecycle last Test initiated Job ID.

reverted -> (structure)

Lifecycle last Test reverted.

apiCallDateTime -> (string)

Lifecycle last Test reverted API call date and time.

state -> (string)

Lifecycle state.

replicationType -> (string)

Source server replication type.

sourceProperties -> (structure)

Source server properties.

cpus -> (list)

Source Server CPUs.

(structure)

Source server CPU information.

cores -> (long)

The number of CPU cores on the source server.

modelName -> (string)

The source serverâs CPU model name.

disks -> (list)

Source Server disks.

(structure)

The disk identifier.

bytes -> (long)

The amount of storage on the disk in bytes.

deviceName -> (string)

The disk or device name.

identificationHints -> (structure)

Source server identification hints.

awsInstanceID -> (string)

AWS Instance ID identification hint.

fqdn -> (string)

FQDN address identification hint.

hostname -> (string)

Hostname identification hint.

vmPath -> (string)

vCenter VM path identification hint.

vmWareUuid -> (string)

vmWare UUID identification hint.

lastUpdatedDateTime -> (string)

Source server last update date and time.

networkInterfaces -> (list)

Source server network interfaces.

(structure)

Network interface.

ips -> (list)

Network interface IPs.

(string)

isPrimary -> (boolean)

Network interface primary IP.

macAddress -> (string)

Network interface Mac address.

os -> (structure)

Source server OS.

fullString -> (string)

OS full string.

ramBytes -> (long)

Source server RAM in bytes.

recommendedInstanceType -> (string)

Source server recommended instance type.

sourceServerID -> (string)

Source server ID.

tags -> (map)

Source server Tags.

key -> (string)

value -> (string)

userProvidedID -> (string)

Source server user provided ID.

vcenterClientID -> (string)

Source server vCenter client id.