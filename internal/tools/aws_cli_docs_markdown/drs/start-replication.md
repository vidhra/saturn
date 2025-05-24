# start-replicationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/drs/start-replication.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/drs/start-replication.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [drs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/drs/index.html#cli-aws-drs) ]

# start-replication

## Description

Starts replication for a stopped Source Server. This action would make the Source Server protected again and restart billing for it.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/drs-2020-02-26/StartReplication)

## Synopsis

```
start-replication
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

`--source-server-id` (string)

The ID of the Source Server to start replication for.

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

sourceServer -> (structure)

The Source Server that this action was targeted on.

agentVersion -> (string)

The version of the DRS agent installed on the source server

arn -> (string)

The ARN of the Source Server.

dataReplicationInfo -> (structure)

The Data Replication Info of the Source Server.

dataReplicationError -> (structure)

Error in data replication.

error -> (string)

Error in data replication.

rawError -> (string)

Error in data replication.

dataReplicationInitiation -> (structure)

Information about whether the data replication has been initiated.

nextAttemptDateTime -> (string)

The date and time of the next attempt to initiate data replication.

startDateTime -> (string)

The date and time of the current attempt to initiate data replication.

steps -> (list)

The steps of the current attempt to initiate data replication.

(structure)

Data replication initiation step.

name -> (string)

The name of the step.

status -> (string)

The status of the step.

dataReplicationState -> (string)

The state of the data replication.

etaDateTime -> (string)

An estimate of when the data replication will be completed.

lagDuration -> (string)

Data replication lag duration.

replicatedDisks -> (list)

The disks that should be replicated.

(structure)

A disk that should be replicated.

backloggedStorageBytes -> (long)

The size of the replication backlog in bytes.

deviceName -> (string)

The name of the device.

replicatedStorageBytes -> (long)

The amount of data replicated so far in bytes.

rescannedStorageBytes -> (long)

The amount of data to be rescanned in bytes.

totalStorageBytes -> (long)

The total amount of data to be replicated in bytes.

volumeStatus -> (string)

The status of the volume.

stagingAvailabilityZone -> (string)

AWS Availability zone into which data is being replicated.

stagingOutpostArn -> (string)

The ARN of the staging Outpost

lastLaunchResult -> (string)

The status of the last recovery launch of this Source Server.

lifeCycle -> (structure)

The lifecycle information of this Source Server.

addedToServiceDateTime -> (string)

The date and time of when the Source Server was added to the service.

elapsedReplicationDuration -> (string)

The amount of time that the Source Server has been replicating for.

firstByteDateTime -> (string)

The date and time of the first byte that was replicated from the Source Server.

lastLaunch -> (structure)

An object containing information regarding the last launch of the Source Server.

initiated -> (structure)

An object containing information regarding the initiation of the last launch of a Source Server.

apiCallDateTime -> (string)

The date and time the last Source Server launch was initiated.

jobID -> (string)

The ID of the Job that was used to last launch the Source Server.

type -> (string)

The Job type that was used to last launch the Source Server.

status -> (string)

Status of Source Serverâs last launch.

lastSeenByServiceDateTime -> (string)

The date and time this Source Server was last seen by the service.

recoveryInstanceId -> (string)

The ID of the Recovery Instance associated with this Source Server.

replicationDirection -> (string)

Replication direction of the Source Server.

reversedDirectionSourceServerArn -> (string)

For EC2-originated Source Servers which have been failed over and then failed back, this value will mean the ARN of the Source Server on the opposite replication direction.

sourceCloudProperties -> (structure)

Source cloud properties of the Source Server.

originAccountID -> (string)

AWS Account ID for an EC2-originated Source Server.

originAvailabilityZone -> (string)

AWS Availability Zone for an EC2-originated Source Server.

originRegion -> (string)

AWS Region for an EC2-originated Source Server.

sourceOutpostArn -> (string)

The ARN of the source Outpost

sourceNetworkID -> (string)

ID of the Source Network which is protecting this Source Serverâs network.

sourceProperties -> (structure)

The source properties of the Source Server.

cpus -> (list)

An array of CPUs.

(structure)

Information about a serverâs CPU.

cores -> (long)

The number of CPU cores.

modelName -> (string)

The model name of the CPU.

disks -> (list)

An array of disks.

(structure)

An object representing a data storage device on a server.

bytes -> (long)

The amount of storage on the disk in bytes.

deviceName -> (string)

The disk or device name.

identificationHints -> (structure)

Hints used to uniquely identify a machine.

awsInstanceID -> (string)

AWS Instance ID identification hint.

fqdn -> (string)

Fully Qualified Domain Name identification hint.

hostname -> (string)

Hostname identification hint.

vmWareUuid -> (string)

vCenter VM path identification hint.

lastUpdatedDateTime -> (string)

The date and time the Source Properties were last updated on.

networkInterfaces -> (list)

An array of network interfaces.

(structure)

Network interface.

ips -> (list)

Network interface IPs.

(string)

isPrimary -> (boolean)

Whether this is the primary network interface.

macAddress -> (string)

The MAC address of the network interface.

os -> (structure)

Operating system.

fullString -> (string)

The long name of the Operating System.

ramBytes -> (long)

The amount of RAM in bytes.

recommendedInstanceType -> (string)

The recommended EC2 instance type that will be used when recovering the Source Server.

supportsNitroInstances -> (boolean)

Are EC2 nitro instance types supported when recovering the Source Server.

sourceServerID -> (string)

The ID of the Source Server.

stagingArea -> (structure)

The staging area of the source server.

errorMessage -> (string)

Shows an error message that occurred when DRS tried to access the staging source server. In this case StagingArea$status will have value EXTENSION_ERROR

stagingAccountID -> (string)

Account ID of the account to which source server belongs. If this source server is extended - shows Account ID of staging source server.

stagingSourceServerArn -> (string)

Arn of the staging source server if this source server is extended

status -> (string)

Status of Source server extension. Possible values: (a) NOT_EXTENDED - This is a source server that is replicating in the current account. (b) EXTENDED - Source server is extended from a staging source server. In this case, the value of stagingSourceServerArn is pointing to the Arn of the source server in the staging account. (c) EXTENSION_ERROR - Some issue occurred when accessing staging source server. In this case, errorMessage field will contain an error message that explains what happened.

tags -> (map)

The tags associated with the Source Server.

key -> (string)

value -> (string)