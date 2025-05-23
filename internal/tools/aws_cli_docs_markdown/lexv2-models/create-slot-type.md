# create-slot-typeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/create-slot-type.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/create-slot-type.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/index.html#cli-aws-lexv2-models) ]

# create-slot-type

## Description

Creates a custom slot type

To create a custom slot type, specify a name for the slot type and a set of enumeration values, the values that a slot of this type can assume.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/CreateSlotType)

## Synopsis

```
create-slot-type
--slot-type-name <value>
[--description <value>]
[--slot-type-values <value>]
[--value-selection-setting <value>]
[--parent-slot-type-signature <value>]
--bot-id <value>
--bot-version <value>
--locale-id <value>
[--external-source-setting <value>]
[--composite-slot-type-setting <value>]
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

`--slot-type-name` (string)

The name for the slot. A slot type name must be unique within the intent.

`--description` (string)

A description of the slot type. Use the description to help identify the slot type in lists.

`--slot-type-values` (list)

A list of `SlotTypeValue` objects that defines the values that the slot type can take. Each value can have a list of synonyms, additional values that help train the machine learning model about the values that it resolves for a slot.

(structure)

Each slot type can have a set of values. Each `SlotTypeValue` represents a value that the slot type can take.

sampleValue -> (structure)

The value of the slot type entry.

value -> (string)

The value that can be used for a slot type.

synonyms -> (list)

Additional values related to the slot type entry.

(structure)

Defines one of the values for a slot type.

value -> (string)

The value that can be used for a slot type.

Shorthand Syntax:

```
sampleValue={value=string},synonyms=[{value=string},{value=string}] ...
```

JSON Syntax:

```
[
  {
    "sampleValue": {
      "value": "string"
    },
    "synonyms": [
      {
        "value": "string"
      }
      ...
    ]
  }
  ...
]
```

`--value-selection-setting` (structure)

Determines the strategy that Amazon Lex uses to select a value from the list of possible values. The field can be set to one of the following values:

- `ORIGINAL_VALUE` - Returns the value entered by the user, if the user value is similar to the slot value.
- `TOP_RESOLUTION` - If there is a resolution list for the slot, return the first value in the resolution list. If there is no resolution list, return null.

If you donât specify the `valueSelectionSetting` parameter, the default is `ORIGINAL_VALUE` .

resolutionStrategy -> (string)

Determines the slot resolution strategy that Amazon Lex uses to return slot type values. The field can be set to one of the following values:

- `ORIGINAL_VALUE` - Returns the value entered by the user, if the user value is similar to the slot value.
- `TOP_RESOLUTION` - If there is a resolution list for the slot, return the first value in the resolution list as the slot type value. If there is no resolution list, null is returned.

If you donât specify the `valueSelectionStrategy` , the default is `ORIGINAL_VALUE` .

regexFilter -> (structure)

A regular expression used to validate the value of a slot.

pattern -> (string)

A regular expression used to validate the value of a slot.

Use a standard regular expression. Amazon Lex supports the following characters in the regular expression:

- A-Z, a-z
- 0-9
- Unicode characters (ââ u<Unicode>â)

Represent Unicode characters with four digits, for example ââ u0041â or ââ u005Aâ.

The following regular expression operators are not supported:

- Infinite repeaters: [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/create-slot-type.html#id1), +, or {x,} with no upper bound.
- Wild card (.)

advancedRecognitionSetting -> (structure)

Provides settings that enable advanced recognition settings for slot values. You can use this to enable using slot values as a custom vocabulary for recognizing user utterances.

audioRecognitionStrategy -> (string)

Enables using the slot values as a custom vocabulary for recognizing user utterances.

Shorthand Syntax:

```
resolutionStrategy=string,regexFilter={pattern=string},advancedRecognitionSetting={audioRecognitionStrategy=string}
```

JSON Syntax:

```
{
  "resolutionStrategy": "OriginalValue"|"TopResolution"|"Concatenation",
  "regexFilter": {
    "pattern": "string"
  },
  "advancedRecognitionSetting": {
    "audioRecognitionStrategy": "UseSlotValuesAsCustomVocabulary"
  }
}
```

`--parent-slot-type-signature` (string)

The built-in slot type used as a parent of this slot type. When you define a parent slot type, the new slot type has the configuration of the parent slot type.

Only `AMAZON.AlphaNumeric` is supported.

`--bot-id` (string)

The identifier of the bot associated with this slot type.

`--bot-version` (string)

The identifier of the bot version associated with this slot type.

`--locale-id` (string)

The identifier of the language and locale that the slot type will be used in. The string must match one of the supported locales. All of the bots, intents, and slots used by the slot type must have the same locale. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html) .

`--external-source-setting` (structure)

Sets the type of external information used to create the slot type.

grammarSlotTypeSetting -> (structure)

Settings required for a slot type based on a grammar that you provide.

source -> (structure)

The source of the grammar used to create the slot type.

s3BucketName -> (string)

The name of the Amazon S3 bucket that contains the grammar source.

s3ObjectKey -> (string)

The path to the grammar in the Amazon S3 bucket.

kmsKeyArn -> (string)

The KMS key required to decrypt the contents of the grammar, if any.

Shorthand Syntax:

```
grammarSlotTypeSetting={source={s3BucketName=string,s3ObjectKey=string,kmsKeyArn=string}}
```

JSON Syntax:

```
{
  "grammarSlotTypeSetting": {
    "source": {
      "s3BucketName": "string",
      "s3ObjectKey": "string",
      "kmsKeyArn": "string"
    }
  }
}
```

`--composite-slot-type-setting` (structure)

Specifications for a composite slot type.

subSlots -> (list)

Subslots in the composite slot.

(structure)

Subslot type composition.

name -> (string)

Name of a constituent sub slot inside a composite slot.

slotTypeId -> (string)

The unique identifier assigned to a slot type. This refers to either a built-in slot type or the unique slotTypeId of a custom slot type.

Shorthand Syntax:

```
subSlots=[{name=string,slotTypeId=string},{name=string,slotTypeId=string}]
```

JSON Syntax:

```
{
  "subSlots": [
    {
      "name": "string",
      "slotTypeId": "string"
    }
    ...
  ]
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

slotTypeId -> (string)

The unique identifier assigned to the slot type. Use this to identify the slot type in the `UpdateSlotType` and `DeleteSlotType` operations.

slotTypeName -> (string)

The name specified for the slot type.

description -> (string)

The description specified for the slot type.

slotTypeValues -> (list)

The list of values that the slot type can assume.

(structure)

Each slot type can have a set of values. Each `SlotTypeValue` represents a value that the slot type can take.

sampleValue -> (structure)

The value of the slot type entry.

value -> (string)

The value that can be used for a slot type.

synonyms -> (list)

Additional values related to the slot type entry.

(structure)

Defines one of the values for a slot type.

value -> (string)

The value that can be used for a slot type.

valueSelectionSetting -> (structure)

The strategy that Amazon Lex uses to select a value from the list of possible values.

resolutionStrategy -> (string)

Determines the slot resolution strategy that Amazon Lex uses to return slot type values. The field can be set to one of the following values:

- `ORIGINAL_VALUE` - Returns the value entered by the user, if the user value is similar to the slot value.
- `TOP_RESOLUTION` - If there is a resolution list for the slot, return the first value in the resolution list as the slot type value. If there is no resolution list, null is returned.

If you donât specify the `valueSelectionStrategy` , the default is `ORIGINAL_VALUE` .

regexFilter -> (structure)

A regular expression used to validate the value of a slot.

pattern -> (string)

A regular expression used to validate the value of a slot.

Use a standard regular expression. Amazon Lex supports the following characters in the regular expression:

- A-Z, a-z
- 0-9
- Unicode characters (ââ u<Unicode>â)

Represent Unicode characters with four digits, for example ââ u0041â or ââ u005Aâ.

The following regular expression operators are not supported:

- Infinite repeaters: [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/create-slot-type.html#id3), +, or {x,} with no upper bound.
- Wild card (.)

advancedRecognitionSetting -> (structure)

Provides settings that enable advanced recognition settings for slot values. You can use this to enable using slot values as a custom vocabulary for recognizing user utterances.

audioRecognitionStrategy -> (string)

Enables using the slot values as a custom vocabulary for recognizing user utterances.

parentSlotTypeSignature -> (string)

The signature of the base slot type specified for the slot type.

botId -> (string)

The identifier for the bot associated with the slot type.

botVersion -> (string)

The version of the bot associated with the slot type.

localeId -> (string)

The specified language and local specified for the slot type.

creationDateTime -> (timestamp)

A timestamp of the date and time that the slot type was created.

externalSourceSetting -> (structure)

The type of external information used to create the slot type.

grammarSlotTypeSetting -> (structure)

Settings required for a slot type based on a grammar that you provide.

source -> (structure)

The source of the grammar used to create the slot type.

s3BucketName -> (string)

The name of the Amazon S3 bucket that contains the grammar source.

s3ObjectKey -> (string)

The path to the grammar in the Amazon S3 bucket.

kmsKeyArn -> (string)

The KMS key required to decrypt the contents of the grammar, if any.

compositeSlotTypeSetting -> (structure)

Specifications for a composite slot type.

subSlots -> (list)

Subslots in the composite slot.

(structure)

Subslot type composition.

name -> (string)

Name of a constituent sub slot inside a composite slot.

slotTypeId -> (string)

The unique identifier assigned to a slot type. This refers to either a built-in slot type or the unique slotTypeId of a custom slot type.