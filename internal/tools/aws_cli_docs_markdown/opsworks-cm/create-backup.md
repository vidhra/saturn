# create-backupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/create-backup.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/create-backup.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opsworkscm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworkscm/index.html#cli-aws-opsworkscm) ]

# create-backup

## Description

Creates an application-level backup of a server. While the server is in the `BACKING_UP` state, the server cannot be changed, and no additional backup can be created.

Backups can be created for servers in `RUNNING` , `HEALTHY` , and `UNHEALTHY` states. By default, you can create a maximum of 50 manual backups.

This operation is asynchronous.

A `LimitExceededException` is thrown when the maximum number of manual backups is reached. An `InvalidStateException` is thrown when the server is not in any of the following states: RUNNING, HEALTHY, or UNHEALTHY. A `ResourceNotFoundException` is thrown when the server is not found. A `ValidationException` is thrown when parameters of the request are not valid.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/CreateBackup)

## Synopsis

```
create-backup
--server-name <value>
[--description <value>]
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

`--server-name` (string)

The name of the server that you want to back up.

`--description` (string)

A user-defined description of the backup.

`--tags` (list)

A map that contains tag keys and tag values to attach to an AWS OpsWorks-CM server backup.

- The key cannot be empty.
- The key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: `+ - = . _ : /`
- The value can be a maximum 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: `+ - = . _ : /`
- Leading and trailing white spaces are trimmed from both the key and value.
- A maximum of 50 user-applied tags is allowed for tag-supported AWS OpsWorks-CM resources.

(structure)

A map that contains tag keys and tag values to attach to an AWS OpsWorks for Chef Automate or AWS OpsWorks for Puppet Enterprise server. Leading and trailing white spaces are trimmed from both the key and value. A maximum of 50 user-applied tags is allowed for tag-supported AWS OpsWorks-CM resources.

Key -> (string)

A tag key, such as `Stage` or `Name` . A tag key cannot be empty. The key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: `+ - = . _ : /`

Value -> (string)

An optional tag value, such as `Production` or `test-owcm-server` . The value can be a maximum of 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: `+ - = . _ : /`

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create backups**

The following `create-backup` command starts a manual backup of a Chef Automate server
named `automate-06` in the `us-east-1` region. The command adds a descriptive message to
the backup in the `--description` parameter.

```
aws opsworks-cm create-backup \
    --server-name 'automate-06' \
    --description "state of my infrastructure at launch"
```

The output shows you information similar to the following about the new backup.

Output:

```
{
    "Backups": [
        {
            "BackupArn": "string",
            "BackupId": "automate-06-20160729133847520",
            "BackupType": "MANUAL",
            "CreatedAt": 2016-07-29T13:38:47.520Z,
            "Description": "state of my infrastructure at launch",
            "Engine": "Chef",
            "EngineModel": "Single",
            "EngineVersion": "12",
            "InstanceProfileArn": "arn:aws:iam::1019881987024:instance-profile/automate-06-1010V4UU2WRM2",
            "InstanceType": "m4.large",
            "KeyPair": "",
            "PreferredBackupWindow": "",
            "PreferredMaintenanceWindow": "",
            "S3LogUrl": "https://s3.amazonaws.com/<bucket-name>/automate-06-20160729133847520",
            "SecurityGroupIds": [ "sg-1a24c270" ],
            "ServerName": "automate-06",
            "ServiceRoleArn": "arn:aws:iam::1019881987024:role/aws-opsworks-cm-service-role.1114810729735",
            "Status": "OK",
            "StatusDescription": "",
            "SubnetIds": [ "subnet-49436a18" ],
            "ToolsVersion": "string",
            "UserArn": "arn:aws:iam::1019881987024:user/opsworks-user"
        }
    ],
}
```

For more information, see [Back Up and Restore an AWS OpsWorks for Chef Automate Server](http://docs.aws.amazon.com/opsworks/latest/userguide/opscm-backup-restore.html) in the *AWS OpsWorks User Guide*.

## Output

Backup -> (structure)

Backup created by request.

BackupArn -> (string)

The ARN of the backup.

BackupId -> (string)

The generated ID of the backup. Example: `myServerName-yyyyMMddHHmmssSSS`

BackupType -> (string)

The backup type. Valid values are `automated` or `manual` .

CreatedAt -> (timestamp)

The time stamp when the backup was created in the database. Example: `2016-07-29T13:38:47.520Z`

Description -> (string)

A user-provided description for a manual backup. This field is empty for automated backups.

Engine -> (string)

The engine type that is obtained from the server when the backup is created.

EngineModel -> (string)

The engine model that is obtained from the server when the backup is created.

EngineVersion -> (string)

The engine version that is obtained from the server when the backup is created.

InstanceProfileArn -> (string)

The EC2 instance profile ARN that is obtained from the server when the backup is created. Because this value is stored, you are not required to provide the InstanceProfileArn again if you restore a backup.

InstanceType -> (string)

The instance type that is obtained from the server when the backup is created.

KeyPair -> (string)

The key pair that is obtained from the server when the backup is created.

PreferredBackupWindow -> (string)

The preferred backup period that is obtained from the server when the backup is created.

PreferredMaintenanceWindow -> (string)

The preferred maintenance period that is obtained from the server when the backup is created.

S3DataSize -> (integer)

This field is deprecated and is no longer used.

S3DataUrl -> (string)

This field is deprecated and is no longer used.

S3LogUrl -> (string)

The Amazon S3 URL of the backupâs log file.

SecurityGroupIds -> (list)

The security group IDs that are obtained from the server when the backup is created.

(string)

ServerName -> (string)

The name of the server from which the backup was made.

ServiceRoleArn -> (string)

The service role ARN that is obtained from the server when the backup is created.

Status -> (string)

The status of a backup while in progress.

StatusDescription -> (string)

An informational message about backup status.

SubnetIds -> (list)

The subnet IDs that are obtained from the server when the backup is created.

(string)

ToolsVersion -> (string)

The version of AWS OpsWorks CM-specific tools that is obtained from the server when the backup is created.

UserArn -> (string)

The IAM user ARN of the requester for manual backups. This field is empty for automated backups.