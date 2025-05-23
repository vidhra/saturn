# update-clusterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb-elastic/update-cluster.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb-elastic/update-cluster.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [docdb-elastic](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb-elastic/index.html#cli-aws-docdb-elastic) ]

# update-cluster

## Description

Modifies an elastic cluster. This includes updating admin-username/password, upgrading the API version, and setting up a backup window and maintenance window

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/docdb-elastic-2022-11-28/UpdateCluster)

## Synopsis

```
update-cluster
[--admin-user-password <value>]
[--auth-type <value>]
[--backup-retention-period <value>]
[--client-token <value>]
--cluster-arn <value>
[--preferred-backup-window <value>]
[--preferred-maintenance-window <value>]
[--shard-capacity <value>]
[--shard-count <value>]
[--shard-instance-count <value>]
[--subnet-ids <value>]
[--vpc-security-group-ids <value>]
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

`--admin-user-password` (string)

The password associated with the elastic cluster administrator. This password can contain any printable ASCII character except forward slash (/), double quote (â), or the âatâ symbol (@).

*Constraints* : Must contain from 8 to 100 characters.

`--auth-type` (string)

The authentication type used to determine where to fetch the password used for accessing the elastic cluster. Valid types are `PLAIN_TEXT` or `SECRET_ARN` .

Possible values:

- `PLAIN_TEXT`
- `SECRET_ARN`

`--backup-retention-period` (integer)

The number of days for which automatic snapshots are retained.

`--client-token` (string)

The client token for the elastic cluster.

`--cluster-arn` (string)

The ARN identifier of the elastic cluster.

`--preferred-backup-window` (string)

The daily time range during which automated backups are created if automated backups are enabled, as determined by the `backupRetentionPeriod` .

`--preferred-maintenance-window` (string)

The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

*Format* : `ddd:hh24:mi-ddd:hh24:mi`

*Default* : a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week.

*Valid days* : Mon, Tue, Wed, Thu, Fri, Sat, Sun

*Constraints* : Minimum 30-minute window.

`--shard-capacity` (integer)

The number of vCPUs assigned to each elastic cluster shard. Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.

`--shard-count` (integer)

The number of shards assigned to the elastic cluster. Maximum is 32.

`--shard-instance-count` (integer)

The number of replica instances applying to all shards in the elastic cluster. A `shardInstanceCount` value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.

`--subnet-ids` (list)

The Amazon EC2 subnet IDs for the elastic cluster.

(string)

Syntax:

```
"string" "string" ...
```

`--vpc-security-group-ids` (list)

A list of EC2 VPC security groups to associate with the elastic cluster.

(string)

Syntax:

```
"string" "string" ...
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

cluster -> (structure)

Returns information about the updated elastic cluster.

adminUserName -> (string)

The name of the elastic cluster administrator.

authType -> (string)

The authentication type for the elastic cluster.

backupRetentionPeriod -> (integer)

The number of days for which automatic snapshots are retained.

clusterArn -> (string)

The ARN identifier of the elastic cluster.

clusterEndpoint -> (string)

The URL used to connect to the elastic cluster.

clusterName -> (string)

The name of the elastic cluster.

createTime -> (string)

The time when the elastic cluster was created in Universal Coordinated Time (UTC).

kmsKeyId -> (string)

The KMS key identifier to use to encrypt the elastic cluster.

preferredBackupWindow -> (string)

The daily time range during which automated backups are created if automated backups are enabled, as determined by `backupRetentionPeriod` .

preferredMaintenanceWindow -> (string)

The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

*Format* : `ddd:hh24:mi-ddd:hh24:mi`

shardCapacity -> (integer)

The number of vCPUs assigned to each elastic cluster shard. Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.

shardCount -> (integer)

The number of shards assigned to the elastic cluster. Maximum is 32.

shardInstanceCount -> (integer)

The number of replica instances applying to all shards in the cluster. A `shardInstanceCount` value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.

shards -> (list)

The total number of shards in the cluster.

(structure)

The name of the shard.

createTime -> (string)

The time when the shard was created in Universal Coordinated Time (UTC).

shardId -> (string)

The ID of the shard.

status -> (string)

The current status of the shard.

status -> (string)

The status of the elastic cluster.

subnetIds -> (list)

The Amazon EC2 subnet IDs for the elastic cluster.

(string)

vpcSecurityGroupIds -> (list)

A list of EC2 VPC security groups associated with thie elastic cluster.

(string)