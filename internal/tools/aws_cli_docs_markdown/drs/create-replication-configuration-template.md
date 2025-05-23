# create-replication-configuration-templateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/drs/create-replication-configuration-template.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/drs/create-replication-configuration-template.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [drs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/drs/index.html#cli-aws-drs) ]

# create-replication-configuration-template

## Description

Creates a new ReplicationConfigurationTemplate.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/drs-2020-02-26/CreateReplicationConfigurationTemplate)

## Synopsis

```
create-replication-configuration-template
--associate-default-security-group | --no-associate-default-security-group
[--auto-replicate-new-disks | --no-auto-replicate-new-disks]
--bandwidth-throttling <value>
--create-public-ip | --no-create-public-ip
--data-plane-routing <value>
--default-large-staging-disk-type <value>
--ebs-encryption <value>
[--ebs-encryption-key-arn <value>]
--pit-policy <value>
--replication-server-instance-type <value>
--replication-servers-security-groups-ids <value>
--staging-area-subnet-id <value>
--staging-area-tags <value>
[--tags <value>]
--use-dedicated-replication-server | --no-use-dedicated-replication-server
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

`--associate-default-security-group` | `--no-associate-default-security-group` (boolean)

Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration Template.

`--auto-replicate-new-disks` | `--no-auto-replicate-new-disks` (boolean)

Whether to allow the AWS replication agent to automatically replicate newly added disks.

`--bandwidth-throttling` (long)

Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.

`--create-public-ip` | `--no-create-public-ip` (boolean)

Whether to create a Public IP for the Recovery Instance by default.

`--data-plane-routing` (string)

The data plane routing mechanism that will be used for replication.

Possible values:

- `PRIVATE_IP`
- `PUBLIC_IP`

`--default-large-staging-disk-type` (string)

The Staging Disk EBS volume type to be used during replication.

Possible values:

- `GP2`
- `GP3`
- `ST1`
- `AUTO`

`--ebs-encryption` (string)

The type of EBS encryption to be used during replication.

Possible values:

- `DEFAULT`
- `CUSTOM`
- `NONE`

`--ebs-encryption-key-arn` (string)

The ARN of the EBS encryption key to be used during replication.

`--pit-policy` (list)

The Point in time (PIT) policy to manage snapshots taken during replication.

(structure)

A rule in the Point in Time (PIT) policy representing when to take snapshots and how long to retain them for.

enabled -> (boolean)

Whether this rule is enabled or not.

interval -> (integer)

How often, in the chosen units, a snapshot should be taken.

retentionDuration -> (integer)

The duration to retain a snapshot for, in the chosen units.

ruleID -> (long)

The ID of the rule.

units -> (string)

The units used to measure the interval and retentionDuration.

Shorthand Syntax:

```
enabled=boolean,interval=integer,retentionDuration=integer,ruleID=long,units=string ...
```

JSON Syntax:

```
[
  {
    "enabled": true|false,
    "interval": integer,
    "retentionDuration": integer,
    "ruleID": long,
    "units": "MINUTE"|"HOUR"|"DAY"
  }
  ...
]
```

`--replication-server-instance-type` (string)

The instance type to be used for the replication server.

`--replication-servers-security-groups-ids` (list)

The security group IDs that will be used by the replication server.

(string)

Syntax:

```
"string" "string" ...
```

`--staging-area-subnet-id` (string)

The subnet to be used by the replication staging area.

`--staging-area-tags` (map)

A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.

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

`--tags` (map)

A set of tags to be associated with the Replication Configuration Template resource.

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

`--use-dedicated-replication-server` | `--no-use-dedicated-replication-server` (boolean)

Whether to use a dedicated Replication Server in the replication staging area.

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

arn -> (string)

The Replication Configuration Template ARN.

associateDefaultSecurityGroup -> (boolean)

Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration Template.

autoReplicateNewDisks -> (boolean)

Whether to allow the AWS replication agent to automatically replicate newly added disks.

bandwidthThrottling -> (long)

Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.

createPublicIP -> (boolean)

Whether to create a Public IP for the Recovery Instance by default.

dataPlaneRouting -> (string)

The data plane routing mechanism that will be used for replication.

defaultLargeStagingDiskType -> (string)

The Staging Disk EBS volume type to be used during replication.

ebsEncryption -> (string)

The type of EBS encryption to be used during replication.

ebsEncryptionKeyArn -> (string)

The ARN of the EBS encryption key to be used during replication.

pitPolicy -> (list)

The Point in time (PIT) policy to manage snapshots taken during replication.

(structure)

A rule in the Point in Time (PIT) policy representing when to take snapshots and how long to retain them for.

enabled -> (boolean)

Whether this rule is enabled or not.

interval -> (integer)

How often, in the chosen units, a snapshot should be taken.

retentionDuration -> (integer)

The duration to retain a snapshot for, in the chosen units.

ruleID -> (long)

The ID of the rule.

units -> (string)

The units used to measure the interval and retentionDuration.

replicationConfigurationTemplateID -> (string)

The Replication Configuration Template ID.

replicationServerInstanceType -> (string)

The instance type to be used for the replication server.

replicationServersSecurityGroupsIDs -> (list)

The security group IDs that will be used by the replication server.

(string)

stagingAreaSubnetId -> (string)

The subnet to be used by the replication staging area.

stagingAreaTags -> (map)

A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.

key -> (string)

value -> (string)

tags -> (map)

A set of tags to be associated with the Replication Configuration Template resource.

key -> (string)

value -> (string)

useDedicatedReplicationServer -> (boolean)

Whether to use a dedicated Replication Server in the replication staging area.