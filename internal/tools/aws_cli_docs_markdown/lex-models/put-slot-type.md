# put-slot-typeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-slot-type.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-slot-type.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lex-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/index.html#cli-aws-lex-models) ]

# put-slot-type

## Description

Creates a custom slot type or replaces an existing custom slot type.

To create a custom slot type, specify a name for the slot type and a set of enumeration values, which are the values that a slot of this type can assume. For more information, see  how-it-works .

If you specify the name of an existing slot type, the fields in the request replace the existing values in the `$LATEST` version of the slot type. Amazon Lex removes the fields that you donât provide in the request. If you donât specify required fields, Amazon Lex throws an exception. When you update the `$LATEST` version of a slot type, if a bot uses the `$LATEST` version of an intent that contains the slot type, the botâs `status` field is set to `NOT_BUILT` .

This operation requires permissions for the `lex:PutSlotType` action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/PutSlotType)

## Synopsis

```
put-slot-type
--name <value>
[--description <value>]
[--enumeration-values <value>]
[--checksum <value>]
[--value-selection-strategy <value>]
[--create-version | --no-create-version]
[--parent-slot-type-signature <value>]
[--slot-type-configurations <value>]
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

The name of the slot type. The name is *not* case sensitive.

The name canât match a built-in slot type name, or a built-in slot type name with âAMAZON.â removed. For example, because there is a built-in slot type called `AMAZON.DATE` , you canât create a custom slot type called `DATE` .

For a list of built-in slot types, see [Slot Type Reference](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference) in the *Alexa Skills Kit* .

`--description` (string)

A description of the slot type.

`--enumeration-values` (list)

A list of `EnumerationValue` objects that defines the values that the slot type can take. Each value can have a list of `synonyms` , which are additional values that help train the machine learning model about the values that it resolves for a slot.

A regular expression slot type doesnât require enumeration values. All other slot types require a list of enumeration values.

When Amazon Lex resolves a slot value, it generates a resolution list that contains up to five possible values for the slot. If you are using a Lambda function, this resolution list is passed to the function. If you are not using a Lambda function you can choose to return the value that the user entered or the first value in the resolution list as the slot value. The `valueSelectionStrategy` field indicates the option to use.

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

Shorthand Syntax:

```
value=string,synonyms=string,string ...
```

JSON Syntax:

```
[
  {
    "value": "string",
    "synonyms": ["string", ...]
  }
  ...
]
```

`--checksum` (string)

Identifies a specific revision of the `$LATEST` version.

When you create a new slot type, leave the `checksum` field blank. If you specify a checksum you get a `BadRequestException` exception.

When you want to update a slot type, set the `checksum` field to the checksum of the most recent revision of the `$LATEST` version. If you donât specify the `checksum` field, or if the checksum does not match the `$LATEST` version, you get a `PreconditionFailedException` exception.

`--value-selection-strategy` (string)

Determines the slot resolution strategy that Amazon Lex uses to return slot type values. The field can be set to one of the following values:

- `ORIGINAL_VALUE` - Returns the value entered by the user, if the user value is similar to the slot value.
- `TOP_RESOLUTION` - If there is a resolution list for the slot, return the first value in the resolution list as the slot type value. If there is no resolution list, null is returned.

If you donât specify the `valueSelectionStrategy` , the default is `ORIGINAL_VALUE` .

Possible values:

- `ORIGINAL_VALUE`
- `TOP_RESOLUTION`

`--create-version` | `--no-create-version` (boolean)

When set to `true` a new numbered version of the slot type is created. This is the same as calling the `CreateSlotTypeVersion` operation. If you do not specify `createVersion` , the default is `false` .

`--parent-slot-type-signature` (string)

The built-in slot type used as the parent of the slot type. When you define a parent slot type, the new slot type has all of the same configuration as the parent.

Only `AMAZON.AlphaNumeric` is supported.

`--slot-type-configurations` (list)

Configuration information that extends the parent built-in slot type. The configuration is added to the settings for the parent slot type.

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

- Infinite repeaters: [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-slot-type.html#id1), +, or {x,} with no upper bound.
- Wild card (.)

Shorthand Syntax:

```
regexConfiguration={pattern=string} ...
```

JSON Syntax:

```
[
  {
    "regexConfiguration": {
      "pattern": "string"
    }
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

The date that the slot type was updated. When you create a slot type, the creation date and last update date are the same.

createdDate -> (timestamp)

The date that the slot type was created.

version -> (string)

The version of the slot type. For a new slot type, the version is always `$LATEST` .

checksum -> (string)

Checksum of the `$LATEST` version of the slot type.

valueSelectionStrategy -> (string)

The slot resolution strategy that Amazon Lex uses to determine the value of the slot. For more information, see  PutSlotType .

createVersion -> (boolean)

`True` if a new version of the slot type was created. If the `createVersion` field was not specified in the request, the `createVersion` field is set to false in the response.

parentSlotTypeSignature -> (string)

The built-in slot type used as the parent of the slot type.

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

- Infinite repeaters: [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-slot-type.html#id3), +, or {x,} with no upper bound.
- Wild card (.)