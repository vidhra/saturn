# modify-migration-projectÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-migration-project.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-migration-project.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/index.html#cli-aws-dms) ]

# modify-migration-project

## Description

Modifies the specified migration project using the provided parameters.

### Note

The migration project must be closed before you can modify it.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/ModifyMigrationProject)

## Synopsis

```
modify-migration-project
--migration-project-identifier <value>
[--migration-project-name <value>]
[--source-data-provider-descriptors <value>]
[--target-data-provider-descriptors <value>]
[--instance-profile-identifier <value>]
[--transformation-rules <value>]
[--description <value>]
[--schema-conversion-application-attributes <value>]
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

`--migration-project-identifier` (string)

The identifier of the migration project. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They canât end with a hyphen, or contain two consecutive hyphens.

`--migration-project-name` (string)

A user-friendly name for the migration project.

`--source-data-provider-descriptors` (list)

Information about the source data provider, including the name, ARN, and Amazon Web Services Secrets Manager parameters.

(structure)

Information about a data provider.

DataProviderIdentifier -> (string)

The name or Amazon Resource Name (ARN) of the data provider.

SecretsManagerSecretId -> (string)

The identifier of the Amazon Web Services Secrets Manager Secret used to store access credentials for the data provider.

SecretsManagerAccessRoleArn -> (string)

The ARN of the role used to access Amazon Web Services Secrets Manager.

Shorthand Syntax:

```
DataProviderIdentifier=string,SecretsManagerSecretId=string,SecretsManagerAccessRoleArn=string ...
```

JSON Syntax:

```
[
  {
    "DataProviderIdentifier": "string",
    "SecretsManagerSecretId": "string",
    "SecretsManagerAccessRoleArn": "string"
  }
  ...
]
```

`--target-data-provider-descriptors` (list)

Information about the target data provider, including the name, ARN, and Amazon Web Services Secrets Manager parameters.

(structure)

Information about a data provider.

DataProviderIdentifier -> (string)

The name or Amazon Resource Name (ARN) of the data provider.

SecretsManagerSecretId -> (string)

The identifier of the Amazon Web Services Secrets Manager Secret used to store access credentials for the data provider.

SecretsManagerAccessRoleArn -> (string)

The ARN of the role used to access Amazon Web Services Secrets Manager.

Shorthand Syntax:

```
DataProviderIdentifier=string,SecretsManagerSecretId=string,SecretsManagerAccessRoleArn=string ...
```

JSON Syntax:

```
[
  {
    "DataProviderIdentifier": "string",
    "SecretsManagerSecretId": "string",
    "SecretsManagerAccessRoleArn": "string"
  }
  ...
]
```

`--instance-profile-identifier` (string)

The name or Amazon Resource Name (ARN) for the instance profile.

`--transformation-rules` (string)

The settings in JSON format for migration rules. Migration rules make it possible for you to change the object names according to the rules that you specify. For example, you can change an object name to lowercase or uppercase, add or remove a prefix or suffix, or rename objects.

`--description` (string)

A user-friendly description of the migration project.

`--schema-conversion-application-attributes` (structure)

The schema conversion application attributes, including the Amazon S3 bucket name and Amazon S3 role ARN.

S3BucketPath -> (string)

The path for the Amazon S3 bucket that the application uses for exporting assessment reports.

S3BucketRoleArn -> (string)

The ARN for the role the application uses to access its Amazon S3 bucket.

Shorthand Syntax:

```
S3BucketPath=string,S3BucketRoleArn=string
```

JSON Syntax:

```
{
  "S3BucketPath": "string",
  "S3BucketRoleArn": "string"
}
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

MigrationProject -> (structure)

The migration project that was modified.

MigrationProjectName -> (string)

The name of the migration project.

MigrationProjectArn -> (string)

The ARN string that uniquely identifies the migration project.

MigrationProjectCreationTime -> (timestamp)

The time when the migration project was created.

SourceDataProviderDescriptors -> (list)

Information about the source data provider, including the name or ARN, and Secrets Manager parameters.

(structure)

Information about a data provider.

SecretsManagerSecretId -> (string)

The identifier of the Amazon Web Services Secrets Manager Secret used to store access credentials for the data provider.

SecretsManagerAccessRoleArn -> (string)

The ARN of the role used to access Amazon Web Services Secrets Manager.

DataProviderName -> (string)

The user-friendly name of the data provider.

DataProviderArn -> (string)

The Amazon Resource Name (ARN) of the data provider.

TargetDataProviderDescriptors -> (list)

Information about the target data provider, including the name or ARN, and Secrets Manager parameters.

(structure)

Information about a data provider.

SecretsManagerSecretId -> (string)

The identifier of the Amazon Web Services Secrets Manager Secret used to store access credentials for the data provider.

SecretsManagerAccessRoleArn -> (string)

The ARN of the role used to access Amazon Web Services Secrets Manager.

DataProviderName -> (string)

The user-friendly name of the data provider.

DataProviderArn -> (string)

The Amazon Resource Name (ARN) of the data provider.

InstanceProfileArn -> (string)

The Amazon Resource Name (ARN) of the instance profile for your migration project.

InstanceProfileName -> (string)

The name of the associated instance profile.

TransformationRules -> (string)

The settings in JSON format for migration rules. Migration rules make it possible for you to change the object names according to the rules that you specify. For example, you can change an object name to lowercase or uppercase, add or remove a prefix or suffix, or rename objects.

Description -> (string)

A user-friendly description of the migration project.

SchemaConversionApplicationAttributes -> (structure)

The schema conversion application attributes, including the Amazon S3 bucket name and Amazon S3 role ARN.

S3BucketPath -> (string)

The path for the Amazon S3 bucket that the application uses for exporting assessment reports.

S3BucketRoleArn -> (string)

The ARN for the role the application uses to access its Amazon S3 bucket.