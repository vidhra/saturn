# get-relational-databaseÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lightsail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html#cli-aws-lightsail) ]

# get-relational-database

## Description

Returns information about a specific database in Amazon Lightsail.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRelationalDatabase)

## Synopsis

```
get-relational-database
--relational-database-name <value>
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

`--relational-database-name` (string)

The name of the database that you are looking up.

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

**To get information about a relational database**

The following `get-relational-database` example displays details about the specified relational database.

```
aws lightsail get-relational-database \
    --relational-database-name Database-1
```

Output:

```
{
    "relationalDatabase": {
        "name": "Database-1",
        "arn": "arn:aws:lightsail:us-west-2:111122223333:RelationalDatabase/7ea932b1-b85a-4bd5-9b3e-bEXAMPLE8cc4",
        "supportCode": "6EXAMPLE3362/ls-9EXAMPLE8ad863723b62cc8901a8aa6e794ae0d2",
        "createdAt": 1571259453.795,
        "location": {
            "availabilityZone": "us-west-2a",
            "regionName": "us-west-2"
        },
        "resourceType": "RelationalDatabase",
        "tags": [],
        "relationalDatabaseBlueprintId": "mysql_8_0",
        "relationalDatabaseBundleId": "micro_1_0",
        "masterDatabaseName": "dbmaster",
        "hardware": {
            "cpuCount": 1,
            "diskSizeInGb": 40,
            "ramSizeInGb": 1.0
        },
        "state": "available",
        "backupRetentionEnabled": false,
        "pendingModifiedValues": {},
        "engine": "mysql",
        "engineVersion": "8.0.16",
        "masterUsername": "dbmasteruser",
        "parameterApplyStatus": "in-sync",
        "preferredBackupWindow": "10:01-10:31",
        "preferredMaintenanceWindow": "sat:11:14-sat:11:44",
        "publiclyAccessible": true,
        "masterEndpoint": {
            "port": 3306,
            "address": "ls-9EXAMPLE8ad863723b62ccEXAMPLEa6e794ae0d2.czowadgeezqi.us-west-2.rds.amazonaws.com"
        },
        "pendingMaintenanceActions": []
    }
}
```

## Output

relationalDatabase -> (structure)

An object describing the specified database.

name -> (string)

The unique name of the database resource in Lightsail.

arn -> (string)

The Amazon Resource Name (ARN) of the database.

supportCode -> (string)

The support code for the database. Include this code in your email to support when you have questions about a database in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt -> (timestamp)

The timestamp when the database was created. Formatted in Unix time.

location -> (structure)

The Region name and Availability Zone where the database is located.

availabilityZone -> (string)

The Availability Zone. Follows the format `us-east-2a` (case-sensitive).

regionName -> (string)

The Amazon Web Services Region name.

resourceType -> (string)

The Lightsail resource type for the database (for example, `RelationalDatabase` ).

tags -> (list)

The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

(structure)

Describes a tag key and optional value assigned to an Amazon Lightsail resource.

For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

key -> (string)

The key of the tag.

Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value -> (string)

The value of the tag.

Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

relationalDatabaseBlueprintId -> (string)

The blueprint ID for the database. A blueprint describes the major engine version of a database.

relationalDatabaseBundleId -> (string)

The bundle ID for the database. A bundle describes the performance specifications for your database.

masterDatabaseName -> (string)

The name of the master database created when the Lightsail database resource is created.

hardware -> (structure)

Describes the hardware of the database.

cpuCount -> (integer)

The number of vCPUs for the database.

diskSizeInGb -> (integer)

The size of the disk for the database.

ramSizeInGb -> (float)

The amount of RAM in GB for the database.

state -> (string)

Describes the current state of the database.

secondaryAvailabilityZone -> (string)

Describes the secondary Availability Zone of a high availability database.

The secondary database is used for failover support of a high availability database.

backupRetentionEnabled -> (boolean)

A Boolean value indicating whether automated backup retention is enabled for the database.

pendingModifiedValues -> (structure)

Describes pending database value modifications.

masterUserPassword -> (string)

The password for the master user of the database.

engineVersion -> (string)

The database engine version.

backupRetentionEnabled -> (boolean)

A Boolean value indicating whether automated backup retention is enabled.

engine -> (string)

The database software (for example, `MySQL` ).

engineVersion -> (string)

The database engine version (for example, `5.7.23` ).

latestRestorableTime -> (timestamp)

The latest point in time to which the database can be restored. Formatted in Unix time.

masterUsername -> (string)

The master user name of the database.

parameterApplyStatus -> (string)

The status of parameter updates for the database.

preferredBackupWindow -> (string)

The daily time range during which automated backups are created for the database (for example, `16:00-16:30` ).

preferredMaintenanceWindow -> (string)

The weekly time range during which system maintenance can occur on the database.

In the format `ddd:hh24:mi-ddd:hh24:mi` . For example, `Tue:17:00-Tue:17:30` .

publiclyAccessible -> (boolean)

A Boolean value indicating whether the database is publicly accessible.

masterEndpoint -> (structure)

The master endpoint for the database.

port -> (integer)

Specifies the port that the database is listening on.

address -> (string)

Specifies the DNS address of the database.

pendingMaintenanceActions -> (list)

Describes the pending maintenance actions for the database.

(structure)

Describes a pending database maintenance action.

action -> (string)

The type of pending database maintenance action.

description -> (string)

Additional detail about the pending database maintenance action.

currentApplyDate -> (timestamp)

The effective date of the pending database maintenance action.

caCertificateIdentifier -> (string)

The certificate associated with the database.