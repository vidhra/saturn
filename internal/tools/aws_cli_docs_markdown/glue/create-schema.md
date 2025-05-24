# create-schemaÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-schema.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-schema.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# create-schema

## Description

Creates a new schema set and registers the schema definition. Returns an error if the schema set already exists without actually registering the version.

When the schema set is created, a version checkpoint will be set to the first version. Compatibility mode âDISABLEDâ restricts any additional schema versions from being added after the first schema version. For all other compatibility modes, validation of compatibility settings will be applied only from the second version onwards when the `RegisterSchemaVersion` API is used.

When this API is called without a `RegistryId` , this will create an entry for a âdefault-registryâ in the registry database tables, if it is not already present.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateSchema)

## Synopsis

```
create-schema
[--registry-id <value>]
--schema-name <value>
--data-format <value>
[--compatibility <value>]
[--description <value>]
[--tags <value>]
[--schema-definition <value>]
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

`--registry-id` (structure)

This is a wrapper shape to contain the registry identity fields. If this is not provided, the default registry will be used. The ARN format for the same will be: `arn:aws:glue:us-east-2:<customer id>:registry/default-registry:random-5-letter-id` .

RegistryName -> (string)

Name of the registry. Used only for lookup. One of `RegistryArn` or `RegistryName` has to be provided.

RegistryArn -> (string)

Arn of the registry to be updated. One of `RegistryArn` or `RegistryName` has to be provided.

Shorthand Syntax:

```
RegistryName=string,RegistryArn=string
```

JSON Syntax:

```
{
  "RegistryName": "string",
  "RegistryArn": "string"
}
```

`--schema-name` (string)

Name of the schema to be created of max length of 255, and may only contain letters, numbers, hyphen, underscore, dollar sign, or hash mark. No whitespace.

`--data-format` (string)

The data format of the schema definition. Currently `AVRO` , `JSON` and `PROTOBUF` are supported.

Possible values:

- `AVRO`
- `JSON`
- `PROTOBUF`

`--compatibility` (string)

The compatibility mode of the schema. The possible values are:

- *NONE* : No compatibility mode applies. You can use this choice in development scenarios or if you do not know the compatibility mode that you want to apply to schemas. Any new version added will be accepted without undergoing a compatibility check.
- *DISABLED* : This compatibility choice prevents versioning for a particular schema. You can use this choice to prevent future versioning of a schema.
- *BACKWARD* : This compatibility choice is recommended as it allows data receivers to read both the current and one previous schema version. This means that for instance, a new schema version cannot drop data fields or change the type of these fields, so they canât be read by readers using the previous version.
- *BACKWARD_ALL* : This compatibility choice allows data receivers to read both the current and all previous schema versions. You can use this choice when you need to delete fields or add optional fields, and check compatibility against all previous schema versions.
- *FORWARD* : This compatibility choice allows data receivers to read both the current and one next schema version, but not necessarily later versions. You can use this choice when you need to add fields or delete optional fields, but only check compatibility against the last schema version.
- *FORWARD_ALL* : This compatibility choice allows data receivers to read written by producers of any new registered schema. You can use this choice when you need to add fields or delete optional fields, and check compatibility against all previous schema versions.
- *FULL* : This compatibility choice allows data receivers to read data written by producers using the previous or next version of the schema, but not necessarily earlier or later versions. You can use this choice when you need to add or remove optional fields, but only check compatibility against the last schema version.
- *FULL_ALL* : This compatibility choice allows data receivers to read data written by producers using all previous schema versions. You can use this choice when you need to add or remove optional fields, and check compatibility against all previous schema versions.

Possible values:

- `NONE`
- `DISABLED`
- `BACKWARD`
- `BACKWARD_ALL`
- `FORWARD`
- `FORWARD_ALL`
- `FULL`
- `FULL_ALL`

`--description` (string)

An optional description of the schema. If description is not provided, there will not be any automatic default value for this.

`--tags` (map)

Amazon Web Services tags that contain a key value pair and may be searched by console, command line, or API. If specified, follows the Amazon Web Services tags-on-create pattern.

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

`--schema-definition` (string)

The schema definition using the `DataFormat` setting for `SchemaName` .

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

RegistryName -> (string)

The name of the registry.

RegistryArn -> (string)

The Amazon Resource Name (ARN) of the registry.

SchemaName -> (string)

The name of the schema.

SchemaArn -> (string)

The Amazon Resource Name (ARN) of the schema.

Description -> (string)

A description of the schema if specified when created.

DataFormat -> (string)

The data format of the schema definition. Currently `AVRO` , `JSON` and `PROTOBUF` are supported.

Compatibility -> (string)

The schema compatibility mode.

SchemaCheckpoint -> (long)

The version number of the checkpoint (the last time the compatibility mode was changed).

LatestSchemaVersion -> (long)

The latest version of the schema associated with the returned schema definition.

NextSchemaVersion -> (long)

The next version of the schema associated with the returned schema definition.

SchemaStatus -> (string)

The status of the schema.

Tags -> (map)

The tags for the schema.

key -> (string)

value -> (string)

SchemaVersionId -> (string)

The unique identifier of the first schema version.

SchemaVersionStatus -> (string)

The status of the first schema version created.