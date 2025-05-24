# create-custom-db-engine-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-custom-db-engine-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-custom-db-engine-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# create-custom-db-engine-version

## Description

Creates a custom DB engine version (CEV).

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/CreateCustomDBEngineVersion)

## Synopsis

```
create-custom-db-engine-version
--engine <value>
--engine-version <value>
[--database-installation-files-s3-bucket-name <value>]
[--database-installation-files-s3-prefix <value>]
[--image-id <value>]
[--kms-key-id <value>]
[--description <value>]
[--manifest <value>]
[--tags <value>]
[--source-custom-db-engine-version-identifier <value>]
[--use-aws-provided-latest-image | --no-use-aws-provided-latest-image]
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

`--engine` (string)

The database engine. RDS Custom for Oracle supports the following values:

- `custom-oracle-ee`
- `custom-oracle-ee-cdb`
- `custom-oracle-se2`
- `custom-oracle-se2-cdb`

`--engine-version` (string)

The name of your CEV. The name format is 19.*customized_string* . For example, a valid CEV name is `19.my_cev1` . This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of `Engine` and `EngineVersion` is unique per customer per Region.

`--database-installation-files-s3-bucket-name` (string)

The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is `my-custom-installation-files` .

`--database-installation-files-s3-prefix` (string)

The Amazon S3 directory that contains the database installation files for your CEV. For example, a valid bucket name is `123456789012/cev1` . If this setting isnât specified, no prefix is assumed.

`--image-id` (string)

The ID of the Amazon Machine Image (AMI). For RDS Custom for SQL Server, an AMI ID is required to create a CEV. For RDS Custom for Oracle, the default is the most recent AMI available, but you can specify an AMI ID that was used in a different Oracle CEV. Find the AMIs used by your CEVs by calling the [DescribeDBEngineVersions](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBEngineVersions.html) operation.

`--kms-key-id` (string)

The Amazon Web Services KMS key identifier for an encrypted CEV. A symmetric encryption KMS key is required for RDS Custom, but optional for Amazon RDS.

If you have an existing symmetric encryption KMS key in your account, you can use it with RDS Custom. No further action is necessary. If you donât already have a symmetric encryption KMS key in your account, follow the instructions in [Creating a symmetric encryption KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk) in the *Amazon Web Services Key Management Service Developer Guide* .

You can choose the same symmetric encryption key when you create a CEV and a DB instance, or choose different keys.

`--description` (string)

An optional description of your CEV.

`--manifest` (string)

The CEV manifest, which is a JSON document that describes the installation .zip files stored in Amazon S3. Specify the name/value pairs in a file or a quoted string. RDS Custom applies the patches in the order in which they are listed.

The following JSON fields are valid:

MediaImportTemplateVersion

Version of the CEV manifest. The date is in the format `YYYY-MM-DD` .

databaseInstallationFileNames

Ordered list of installation files for the CEV.

opatchFileNames

Ordered list of OPatch installers used for the Oracle DB engine.

psuRuPatchFileNames

The PSU and RU patches for this CEV.

OtherPatchFileNames

The patches that are not in the list of PSU and RU patches. Amazon RDS applies these patches after applying the PSU and RU patches.

For more information, see [Creating the CEV manifest](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.html#custom-cev.preparing.manifest) in the *Amazon RDS User Guide* .

`--tags` (list)

A list of tags.

For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide* .

(structure)

Metadata assigned to an Amazon RDS resource consisting of a key-value pair.

For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide* .

Key -> (string)

A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and canât be prefixed with `aws:` or `rds:` . The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â:â, â/â, â=â, â+â, â-â, â@â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$â).

Value -> (string)

A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and canât be prefixed with `aws:` or `rds:` . The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â:â, â/â, â=â, â+â, â-â, â@â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$â).

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

`--source-custom-db-engine-version-identifier` (string)

The ARN of a CEV to use as a source for creating a new CEV. You can specify a different Amazon Machine Imagine (AMI) by using either `Source` or `UseAwsProvidedLatestImage` . You canât specify a different JSON manifest when you specify `SourceCustomDbEngineVersionIdentifier` .

`--use-aws-provided-latest-image` | `--no-use-aws-provided-latest-image` (boolean)

Specifies whether to use the latest service-provided Amazon Machine Image (AMI) for the CEV. If you specify `UseAwsProvidedLatestImage` , you canât also specify `ImageId` .

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

Engine -> (string)

The name of the database engine.

EngineVersion -> (string)

The version number of the database engine.

DBParameterGroupFamily -> (string)

The name of the DB parameter group family for the database engine.

DBEngineDescription -> (string)

The description of the database engine.

DBEngineVersionDescription -> (string)

The description of the database engine version.

DefaultCharacterSet -> (structure)

The default character set for new instances of this engine version, if the `CharacterSetName` parameter of the CreateDBInstance API isnât specified.

CharacterSetName -> (string)

The name of the character set.

CharacterSetDescription -> (string)

The description of the character set.

Image -> (structure)

The EC2 image

ImageId -> (string)

A value that indicates the ID of the AMI.

Status -> (string)

A value that indicates the status of a custom engine version (CEV).

DBEngineMediaType -> (string)

A value that indicates the source media provider of the AMI based on the usage operation. Applicable for RDS Custom for SQL Server.

SupportedCharacterSets -> (list)

A list of the character sets supported by this engine for the `CharacterSetName` parameter of the `CreateDBInstance` operation.

(structure)

This data type is used as a response element in the action `DescribeDBEngineVersions` .

CharacterSetName -> (string)

The name of the character set.

CharacterSetDescription -> (string)

The description of the character set.

SupportedNcharCharacterSets -> (list)

A list of the character sets supported by the Oracle DB engine for the `NcharCharacterSetName` parameter of the `CreateDBInstance` operation.

(structure)

This data type is used as a response element in the action `DescribeDBEngineVersions` .

CharacterSetName -> (string)

The name of the character set.

CharacterSetDescription -> (string)

The description of the character set.

ValidUpgradeTarget -> (list)

A list of engine versions that this database engine version can be upgraded to.

(structure)

The version of the database engine that a DB instance can be upgraded to.

Engine -> (string)

The name of the upgrade target database engine.

EngineVersion -> (string)

The version number of the upgrade target database engine.

Description -> (string)

The version of the database engine that a DB instance can be upgraded to.

AutoUpgrade -> (boolean)

Indicates whether the target version is applied to any source DB instances that have `AutoMinorVersionUpgrade` set to true.

This parameter is dynamic, and is set by RDS.

IsMajorVersionUpgrade -> (boolean)

Indicates whether upgrading to the target version requires upgrading the major version of the database engine.

SupportedEngineModes -> (list)

A list of the supported DB engine modes for the target engine version.

(string)

SupportsParallelQuery -> (boolean)

Indicates whether you can use Aurora parallel query with the target engine version.

SupportsGlobalDatabases -> (boolean)

Indicates whether you can use Aurora global databases with the target engine version.

SupportsBabelfish -> (boolean)

Indicates whether you can use Babelfish for Aurora PostgreSQL with the target engine version.

SupportsLimitlessDatabase -> (boolean)

Indicates whether the DB engine version supports Aurora Limitless Database.

SupportsLocalWriteForwarding -> (boolean)

Indicates whether the target engine version supports forwarding write operations from reader DB instances to the writer DB instance in the DB cluster. By default, write operations arenât allowed on reader DB instances.

Valid for: Aurora DB clusters only

SupportsIntegrations -> (boolean)

Indicates whether the DB engine version supports zero-ETL integrations with Amazon Redshift.

SupportedTimezones -> (list)

A list of the time zones supported by this engine for the `Timezone` parameter of the `CreateDBInstance` action.

(structure)

A time zone associated with a `DBInstance` or a `DBSnapshot` . This data type is an element in the response to the `DescribeDBInstances` , the `DescribeDBSnapshots` , and the `DescribeDBEngineVersions` actions.

TimezoneName -> (string)

The name of the time zone.

ExportableLogTypes -> (list)

The types of logs that the database engine has available for export to CloudWatch Logs.

(string)

SupportsLogExportsToCloudwatchLogs -> (boolean)

Indicates whether the engine version supports exporting the log types specified by ExportableLogTypes to CloudWatch Logs.

SupportsReadReplica -> (boolean)

Indicates whether the database engine version supports read replicas.

SupportedEngineModes -> (list)

A list of the supported DB engine modes.

(string)

SupportedFeatureNames -> (list)

A list of features supported by the DB engine.

The supported features vary by DB engine and DB engine version.

To determine the supported features for a specific DB engine and DB engine version using the CLI, use the following command:

`aws rds describe-db-engine-versions --engine <engine_name> --engine-version <engine_version>`

For example, to determine the supported features for RDS for PostgreSQL version 13.3 using the CLI, use the following command:

`aws rds describe-db-engine-versions --engine postgres --engine-version 13.3`

The supported features are listed under `SupportedFeatureNames` in the output.

(string)

Status -> (string)

The status of the DB engine version, either `available` or `deprecated` .

SupportsParallelQuery -> (boolean)

Indicates whether you can use Aurora parallel query with a specific DB engine version.

SupportsGlobalDatabases -> (boolean)

Indicates whether you can use Aurora global databases with a specific DB engine version.

MajorEngineVersion -> (string)

The major engine version of the CEV.

DatabaseInstallationFilesS3BucketName -> (string)

The name of the Amazon S3 bucket that contains your database installation files.

DatabaseInstallationFilesS3Prefix -> (string)

The Amazon S3 directory that contains the database installation files. If not specified, then no prefix is assumed.

DBEngineVersionArn -> (string)

The ARN of the custom engine version.

KMSKeyId -> (string)

The Amazon Web Services KMS key identifier for an encrypted CEV. This parameter is required for RDS Custom, but optional for Amazon RDS.

CreateTime -> (timestamp)

The creation time of the DB engine version.

TagList -> (list)

A list of tags.

For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide* .

(structure)

Metadata assigned to an Amazon RDS resource consisting of a key-value pair.

For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide* .

Key -> (string)

A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and canât be prefixed with `aws:` or `rds:` . The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â:â, â/â, â=â, â+â, â-â, â@â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$â).

Value -> (string)

A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and canât be prefixed with `aws:` or `rds:` . The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â:â, â/â, â=â, â+â, â-â, â@â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$â).

SupportsBabelfish -> (boolean)

Indicates whether the engine version supports Babelfish for Aurora PostgreSQL.

CustomDBEngineVersionManifest -> (string)

JSON string that lists the installation files and parameters that RDS Custom uses to create a custom engine version (CEV). RDS Custom applies the patches in the order in which theyâre listed in the manifest. You can set the Oracle home, Oracle base, and UNIX/Linux user and group using the installation parameters. For more information, see [JSON fields in the CEV manifest](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.preparing.html#custom-cev.preparing.manifest.fields) in the *Amazon RDS User Guide* .

SupportsLimitlessDatabase -> (boolean)

Indicates whether the DB engine version supports Aurora Limitless Database.

SupportsCertificateRotationWithoutRestart -> (boolean)

Indicates whether the engine version supports rotating the server certificate without rebooting the DB instance.

SupportedCACertificateIdentifiers -> (list)

A list of the supported CA certificate identifiers.

For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide* .

(string)

SupportsLocalWriteForwarding -> (boolean)

Indicates whether the DB engine version supports forwarding write operations from reader DB instances to the writer DB instance in the DB cluster. By default, write operations arenât allowed on reader DB instances.

Valid for: Aurora DB clusters only

SupportsIntegrations -> (boolean)

Indicates whether the DB engine version supports zero-ETL integrations with Amazon Redshift.

ServerlessV2FeaturesSupport -> (structure)

Specifies any Aurora Serverless v2 properties or limits that differ between Aurora engine versions. You can test the values of this attribute when deciding which Aurora version to use in a new or upgraded DB cluster. You can also retrieve the version of an existing DB cluster and check whether that version supports certain Aurora Serverless v2 features before you attempt to use those features.

MinCapacity -> (double)

If the minimum capacity is 0 ACUs, the engine version supports the automatic pause/resume feature of Aurora Serverless v2.

MaxCapacity -> (double)

Specifies the upper Aurora Serverless v2 capacity limit for a particular engine version. Depending on the engine version, the maximum capacity for an Aurora Serverless v2 cluster might be `256` or `128` .