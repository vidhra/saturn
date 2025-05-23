# create-slot-type-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/create-slot-type-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/create-slot-type-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lex-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/index.html#cli-aws-lex-models) ]

# create-slot-type-version

## Description

Creates a new version of a slot type based on the `$LATEST` version of the specified slot type. If the `$LATEST` version of this resource has not changed since the last version that you created, Amazon Lex doesnât create a new version. It returns the last version that you created.

### Note

You can update only the `$LATEST` version of a slot type. You canât update the numbered versions that you create with the `CreateSlotTypeVersion` operation.

When you create a version of a slot type, Amazon Lex sets the version to 1. Subsequent versions increment by 1. For more information, see  versioning-intro .

This operation requires permissions for the `lex:CreateSlotTypeVersion` action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/CreateSlotTypeVersion)

## Synopsis

```
create-slot-type-version
--name <value>
[--checksum <value>]
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

`--name` (string)

The name of the slot type that you want to create a new version for. The name is case sensitive.

`--checksum` (string)

Checksum for the `$LATEST` version of the slot type that you want to publish. If you specify a checksum and the `$LATEST` version of the slot type has a different checksum, Amazon Lex returns a `PreconditionFailedException` exception and doesnât publish the new version. If you donât specify a checksum, Amazon Lex publishes the `$LATEST` version.

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

name -> (string)

The name of the slot type.

description -> (string)

A description of the slot type.

enumerationValues -> (list)

A list of `EnumerationValue` objects that defines the values that the slot type can take.

(structure)

Each slot type can have a set of values. Each enumeration value represents a value the slot type can take.

For example, a pizza ordering bot could have a slot type that specifies the type of crust that the pizza should have. The slot type could include the values

- thick
- thin
- stuffed

value -> (string)

The value of the slot type.

synonyms -> (list)

Additional values related to the slot type value.

(string)

lastUpdatedDate -> (timestamp)

The date that the slot type was updated. When you create a resource, the creation date and last update date are the same.

createdDate -> (timestamp)

The date that the slot type was created.

version -> (string)

The version assigned to the new slot type version.

checksum -> (string)

Checksum of the `$LATEST` version of the slot type.

valueSelectionStrategy -> (string)

The strategy that Amazon Lex uses to determine the value of the slot. For more information, see  PutSlotType .

parentSlotTypeSignature -> (string)

The built-in slot type used a the parent of the slot type.

slotTypeConfigurations -> (list)

Configuration information that extends the parent built-in slot type.

(structure)

Provides configuration information for a slot type.

regexConfiguration -> (structure)

A regular expression used to validate the value of a slot.

pattern -> (string)

A regular expression used to validate the value of a slot.

Use a standard regular expression. Amazon Lex supports the following characters in the regular expression:

- A-Z, a-z
- 0-9
- Unicode characters (âu<Unicode>â)

Represent Unicode characters with four digits, for example âu0041â or âu005Aâ.

The following regular expression operators are not supported:

- Infinite repeaters: [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/create-slot-type-version.html#id1), +, or {x,} with no upper bound.
- Wild card (.)