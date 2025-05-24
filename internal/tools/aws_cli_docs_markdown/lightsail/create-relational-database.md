# create-relational-databaseÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-relational-database.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-relational-database.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lightsail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html#cli-aws-lightsail) ]

# create-relational-database

## Description

Creates a new database in Amazon Lightsail.

The `create relational database` operation supports tag-based access control via request tags. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateRelationalDatabase)

## Synopsis

```
create-relational-database
--relational-database-name <value>
[--availability-zone <value>]
--relational-database-blueprint-id <value>
--relational-database-bundle-id <value>
--master-database-name <value>
--master-username <value>
[--master-user-password <value>]
[--preferred-backup-window <value>]
[--preferred-maintenance-window <value>]
[--publicly-accessible | --no-publicly-accessible]
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

`--relational-database-name` (string)

The name to use for your new Lightsail database resource.

Constraints:

- Must contain from 2 to 255 alphanumeric characters, or hyphens.
- The first and last character must be a letter or number.

`--availability-zone` (string)

The Availability Zone in which to create your new database. Use the `us-east-2a` case-sensitive format.

You can get a list of Availability Zones by using the `get regions` operation. Be sure to add the `include relational database Availability Zones` parameter to your request.

`--relational-database-blueprint-id` (string)

The blueprint ID for your new database. A blueprint describes the major engine version of a database.

You can get a list of database blueprints IDs by using the `get relational database blueprints` operation.

`--relational-database-bundle-id` (string)

The bundle ID for your new database. A bundle describes the performance specifications for your database.

You can get a list of database bundle IDs by using the `get relational database bundles` operation.

`--master-database-name` (string)

The meaning of this parameter differs according to the database engine you use.

**MySQL**

The name of the database to create when the Lightsail database resource is created. If this parameter isnât specified, no database is created in the database resource.

Constraints:

- Must contain 1 to 64 letters or numbers.
- Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0- 9).
- Canât be a word reserved by the specified database engine. For more information about reserved words in MySQL, see the Keywords and Reserved Words articles for [MySQL 5.6](https://dev.mysql.com/doc/refman/5.6/en/keywords.html) , [MySQL 5.7](https://dev.mysql.com/doc/refman/5.7/en/keywords.html) , and [MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/keywords.html) .

**PostgreSQL**

The name of the database to create when the Lightsail database resource is created. If this parameter isnât specified, a database named `postgres` is created in the database resource.

Constraints:

- Must contain 1 to 63 letters or numbers.
- Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0- 9).
- Canât be a word reserved by the specified database engine. For more information about reserved words in PostgreSQL, see the SQL Key Words articles for [PostgreSQL 9.6](https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html) , [PostgreSQL 10](https://www.postgresql.org/docs/10/sql-keywords-appendix.html) , [PostgreSQL 11](https://www.postgresql.org/docs/11/sql-keywords-appendix.html) , and [PostgreSQL 12](https://www.postgresql.org/docs/12/sql-keywords-appendix.html) .

`--master-username` (string)

The name for the master user.

**MySQL**

Constraints:

- Required for MySQL.
- Must be 1 to 16 letters or numbers. Can contain underscores.
- First character must be a letter.
- Canât be a reserved word for the chosen database engine. For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for [MySQL 5.6](https://dev.mysql.com/doc/refman/5.6/en/keywords.html) , [MySQL 5.7](https://dev.mysql.com/doc/refman/5.7/en/keywords.html) , or [MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/keywords.html) .

**PostgreSQL**

Constraints:

- Required for PostgreSQL.
- Must be 1 to 63 letters or numbers. Can contain underscores.
- First character must be a letter.
- Canât be a reserved word for the chosen database engine. For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for [PostgreSQL 9.6](https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html) , [PostgreSQL 10](https://www.postgresql.org/docs/10/sql-keywords-appendix.html) , [PostgreSQL 11](https://www.postgresql.org/docs/11/sql-keywords-appendix.html) , and [PostgreSQL 12](https://www.postgresql.org/docs/12/sql-keywords-appendix.html) .

`--master-user-password` (string)

The password for the master user. The password can include any printable ASCII character except â/â, âââ, or â@â. It cannot contain spaces.

**MySQL**

Constraints: Must contain from 8 to 41 characters.

**PostgreSQL**

Constraints: Must contain from 8 to 128 characters.

`--preferred-backup-window` (string)

The daily time range during which automated backups are created for your new database if automated backups are enabled.

The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. For more information about the preferred backup window time blocks for each region, see the [Working With Backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupWindow) guide in the Amazon Relational Database Service documentation.

Constraints:

- Must be in the `hh24:mi-hh24:mi` format. Example: `16:00-16:30`
- Specified in Coordinated Universal Time (UTC).
- Must not conflict with the preferred maintenance window.
- Must be at least 30 minutes.

`--preferred-maintenance-window` (string)

The weekly time range during which system maintenance can occur on your new database.

The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.

Constraints:

- Must be in the `ddd:hh24:mi-ddd:hh24:mi` format.
- Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.
- Must be at least 30 minutes.
- Specified in Coordinated Universal Time (UTC).
- Example: `Tue:17:00-Tue:17:30`

`--publicly-accessible` | `--no-publicly-accessible` (boolean)

Specifies the accessibility options for your new database. A value of `true` specifies a database that is available to resources outside of your Lightsail account. A value of `false` specifies a database that is available only to your Lightsail resources in the same region as your database.

`--tags` (list)

The tag keys and optional values to add to the resource during create.

Use the `TagResource` action to tag a resource after itâs created.

(structure)

Describes a tag key and optional value assigned to an Amazon Lightsail resource.

For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

key -> (string)

The key of the tag.

Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value -> (string)

The value of the tag.

Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a managed database**

The following `create-relational-database` example creates a managed database in the specified AWS Region and Availability Zone, using the MySQL 5.6 database engine (mysql_5_6), and the $15 USD standard database bundle (micro_1_0). The managed database is pre-populated a master user name, and is not publicly accessible.

```
aws lightsail create-relational-database \
    --relational-database-name Database-1 \
    --availability-zone us-west-2a \
    --relational-database-blueprint-id mysql_5_6 \
    --relational-database-bundle-id micro_1_0 \
    --master-database-name dbmaster \
    --master-username user \
    --no-publicly-accessible
```

Output:

```
{
    "operations": [
        {
            "id": "b52bedee-73ed-4798-8d2a-9c12df89adcd",
            "resourceName": "Database-1",
            "resourceType": "RelationalDatabase",
            "createdAt": 1569450017.244,
            "location": {
                "availabilityZone": "us-west-2a",
                "regionName": "us-west-2"
            },
            "isTerminal": false,
            "operationType": "CreateRelationalDatabase",
            "status": "Started",
            "statusChangedAt": 1569450018.637
        }
    ]
}
```

## Output

operations -> (list)

An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(structure)

Describes the API operation.

id -> (string)

The ID of the operation.

resourceName -> (string)

The resource name.

resourceType -> (string)

The resource type.

createdAt -> (timestamp)

The timestamp when the operation was initialized (`1479816991.349` ).

location -> (structure)

The Amazon Web Services Region and Availability Zone.

availabilityZone -> (string)

The Availability Zone. Follows the format `us-east-2a` (case-sensitive).

regionName -> (string)

The Amazon Web Services Region name.

isTerminal -> (boolean)

A Boolean value indicating whether the operation is terminal.

operationDetails -> (string)

Details about the operation (`Debian-1GB-Ohio-1` ).

operationType -> (string)

The type of operation.

status -> (string)

The status of the operation.

statusChangedAt -> (timestamp)

The timestamp when the status was changed (`1479816991.349` ).

errorCode -> (string)

The error code.

errorDetails -> (string)

The error details.