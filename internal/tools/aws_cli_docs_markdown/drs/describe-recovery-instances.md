# describe-recovery-instancesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/drs/describe-recovery-instances.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/drs/describe-recovery-instances.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [drs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/drs/index.html#cli-aws-drs) ]

# describe-recovery-instances

## Description

Lists all Recovery Instances or multiple Recovery Instances by ID.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/drs-2020-02-26/DescribeRecoveryInstances)

`describe-recovery-instances` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `items`

## Synopsis

```
describe-recovery-instances
[--filters <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--filters` (structure)

A set of filters by which to return Recovery Instances.

recoveryInstanceIDs -> (list)

An array of Recovery Instance IDs that should be returned. An empty array means all Recovery Instances.

(string)

sourceServerIDs -> (list)

An array of Source Server IDs for which associated Recovery Instances should be returned.

(string)

Shorthand Syntax:

```
recoveryInstanceIDs=string,string,sourceServerIDs=string,string
```

JSON Syntax:

```
{
  "recoveryInstanceIDs": ["string", ...],
  "sourceServerIDs": ["string", ...]
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

items -> (list)

An array of Recovery Instances.

(structure)

A Recovery Instance is a replica of a Source Server running on EC2.

agentVersion -> (string)

The version of the DRS agent installed on the recovery instance

arn -> (string)

The ARN of the Recovery Instance.

dataReplicationInfo -> (structure)

The Data Replication Info of the Recovery Instance.

dataReplicationError -> (structure)

Information about Data Replication

error -> (string)

Error in data replication.

rawError -> (string)

Error in data replication.

dataReplicationInitiation -> (structure)

Information about whether the data replication has been initiated.

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

stagingAvailabilityZone -> (string)

AWS Availability zone into which data is being replicated.

stagingOutpostArn -> (string)

The ARN of the staging Outpost

ec2InstanceID -> (string)

The EC2 instance ID of the Recovery Instance.

ec2InstanceState -> (string)

The state of the EC2 instance for this Recovery Instance.

failback -> (structure)

An object representing failback related information of the Recovery Instance.

agentLastSeenByServiceDateTime -> (string)

The date and time the agent on the Recovery Instance was last seen by the service.

elapsedReplicationDuration -> (string)

The amount of time that the Recovery Instance has been replicating for.

failbackClientID -> (string)

The ID of the failback client that this Recovery Instance is associated with.

failbackClientLastSeenByServiceDateTime -> (string)

The date and time that the failback client was last seen by the service.

failbackInitiationTime -> (string)

The date and time that the failback initiation started.

failbackJobID -> (string)

The Job ID of the last failback log for this Recovery Instance.

failbackLaunchType -> (string)

The launch type (Recovery / Drill) of the last launch for the failback replication of this recovery instance.

failbackToOriginalServer -> (boolean)

Whether we are failing back to the original Source Server for this Recovery Instance.

firstByteDateTime -> (string)

The date and time of the first byte that was replicated from the Recovery Instance.

state -> (string)

The state of the failback process that this Recovery Instance is in.

isDrill -> (boolean)

Whether this Recovery Instance was created for a drill or for an actual Recovery event.

jobID -> (string)

The ID of the Job that created the Recovery Instance.

originAvailabilityZone -> (string)

AWS availability zone associated with the recovery instance.

originEnvironment -> (string)

Environment (On Premises / AWS) of the instance that the recovery instance originated from.

pointInTimeSnapshotDateTime -> (string)

The date and time of the Point in Time (PIT) snapshot that this Recovery Instance was launched from.

recoveryInstanceID -> (string)

The ID of the Recovery Instance.

recoveryInstanceProperties -> (structure)

Properties of the Recovery Instance machine.

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

An object representing a block storage device on the Recovery Instance.

bytes -> (long)

The amount of storage on the disk in bytes.

ebsVolumeID -> (string)

The EBS Volume ID of this disk.

internalDeviceName -> (string)

The internal device name of this disk. This is the name that is visible on the machine itself and not from the EC2 console.

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

The date and time the Recovery Instance properties were last updated on.

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

sourceOutpostArn -> (string)

The ARN of the source Outpost

sourceServerID -> (string)

The Source Server ID that this Recovery Instance is associated with.

tags -> (map)

An array of tags that are associated with the Recovery Instance.

key -> (string)

value -> (string)

nextToken -> (string)

The token of the next Recovery Instance to retrieve.