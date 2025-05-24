# detect-entities-v2Â¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/detect-entities-v2.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/detect-entities-v2.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [comprehendmedical](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/index.html#cli-aws-comprehendmedical) ]

# detect-entities-v2

## Description

Inspects the clinical text for a variety of medical entities and returns specific information about them such as entity category, location, and confidence score on that information. Amazon Comprehend Medical only detects medical entities in English language texts.

The `DetectEntitiesV2` operation replaces the  DetectEntities operation. This new action uses a different model for determining the entities in your medical text and changes the way that some entities are returned in the output. You should use the `DetectEntitiesV2` operation in all new applications.

The `DetectEntitiesV2` operation returns the `Acuity` and `Direction` entities as attributes instead of types.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/comprehendmedical-2018-10-30/DetectEntitiesV2)

## Synopsis

```
detect-entities-v2
--text <value>
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

`--text` (string)

A UTF-8 string containing the clinical content being examined for entities.

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

**Example 1: To detect entities directly from text**

The following `detect-entities-v2` example shows the detected entities and labels them according to type, directly from input text.

```
aws comprehendmedical detect-entities-v2 \
    --text "Sleeping trouble on present dosage of Clonidine. Severe rash on face and leg, slightly itchy."
```

Output:

```
{
    "Id": 0,
    "BeginOffset": 38,
    "EndOffset": 47,
    "Score": 0.9942955374717712,
    "Text": "Clonidine",
    "Category": "MEDICATION",
    "Type": "GENERIC_NAME",
    "Traits": []
}
```

For more information, see [Detect Entities Version 2](https://docs.aws.amazon.com/comprehend/latest/dg/extracted-med-info-V2.html) in the *Amazon Comprehend Medical Developer Guide*.

**Example 2: To detect entities from a file path**

The following `detect-entities-v2` example shows the detected entities and labels them according to type from a file path.

```
aws comprehendmedical detect-entities-v2 \
    --text file://medical_entities.txt
```

Contents of `medical_entities.txt`:

```
{
    "Sleeping trouble on present dosage of Clonidine. Severe rash on face and leg, slightly itchy."
}
```

Output:

```
{
    "Id": 0,
    "BeginOffset": 38,
    "EndOffset": 47,
    "Score": 0.9942955374717712,
    "Text": "Clonidine",
    "Category": "MEDICATION",
    "Type": "GENERIC_NAME",
    "Traits": []
}
```

For more information, see [Detect Entities Version 2](https://docs.aws.amazon.com/comprehend-medical/latest/dev/textanalysis-entitiesv2.html) in the *Amazon Comprehend Medical Developer Guide*.

## Output

Entities -> (list)

The collection of medical entities extracted from the input text and their associated information. For each entity, the response provides the entity text, the entity category, where the entity text begins and ends, and the level of confidence in the detection and analysis. Attributes and traits of the entity are also returned.

(structure)

Provides information about an extracted medical entity.

Id -> (integer)

The numeric identifier for the entity. This is a monotonically increasing id unique within this response rather than a global unique identifier.

BeginOffset -> (integer)

The 0-based character offset in the input text that shows where the entity begins. The offset returns the UTF-8 code point in the string.

EndOffset -> (integer)

The 0-based character offset in the input text that shows where the entity ends. The offset returns the UTF-8 code point in the string.

Score -> (float)

The level of confidence that Amazon Comprehend Medical has in the accuracy of the detection.

Text -> (string)

The segment of input text extracted as this entity.

Category -> (string)

The category of the entity.

Type -> (string)

Describes the specific type of entity with category of entities.

Traits -> (list)

Contextual information for the entity.

(structure)

Provides contextual information about the extracted entity.

Name -> (string)

Provides a name or contextual description about the trait.

Score -> (float)

The level of confidence that Amazon Comprehend Medical has in the accuracy of this trait.

Attributes -> (list)

The extracted attributes that relate to this entity.

(structure)

An extracted segment of the text that is an attribute of an entity, or otherwise related to an entity, such as the dosage of a medication taken. It contains information about the attribute such as id, begin and end offset within the input text, and the segment of the input text.

Type -> (string)

The type of attribute.

Score -> (float)

The level of confidence that Amazon Comprehend Medical has that the segment of text is correctly recognized as an attribute.

RelationshipScore -> (float)

The level of confidence that Amazon Comprehend Medical has that this attribute is correctly related to this entity.

RelationshipType -> (string)

The type of relationship between the entity and attribute. Type for the relationship is `OVERLAP` , indicating that the entity occurred at the same time as the `Date_Expression` .

Id -> (integer)

The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier.

BeginOffset -> (integer)

The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string.

EndOffset -> (integer)

The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string.

Text -> (string)

The segment of input text extracted as this attribute.

Category -> (string)

The category of attribute.

Traits -> (list)

Contextual information for this attribute.

(structure)

Provides contextual information about the extracted entity.

Name -> (string)

Provides a name or contextual description about the trait.

Score -> (float)

The level of confidence that Amazon Comprehend Medical has in the accuracy of this trait.

UnmappedAttributes -> (list)

Attributes extracted from the input text that couldnât be related to an entity.

(structure)

An attribute that was extracted, but Amazon Comprehend Medical was unable to relate to an entity.

Type -> (string)

The type of the unmapped attribute, could be one of the following values: âMEDICATIONâ, âMEDICAL_CONDITIONâ, âANATOMYâ, âTEST_AND_TREATMENT_PROCEDUREâ or âPROTECTED_HEALTH_INFORMATIONâ.

Attribute -> (structure)

The specific attribute that has been extracted but not mapped to an entity.

Type -> (string)

The type of attribute.

Score -> (float)

The level of confidence that Amazon Comprehend Medical has that the segment of text is correctly recognized as an attribute.

RelationshipScore -> (float)

The level of confidence that Amazon Comprehend Medical has that this attribute is correctly related to this entity.

RelationshipType -> (string)

The type of relationship between the entity and attribute. Type for the relationship is `OVERLAP` , indicating that the entity occurred at the same time as the `Date_Expression` .

Id -> (integer)

The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier.

BeginOffset -> (integer)

The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string.

EndOffset -> (integer)

The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string.

Text -> (string)

The segment of input text extracted as this attribute.

Category -> (string)

The category of attribute.

Traits -> (list)

Contextual information for this attribute.

(structure)

Provides contextual information about the extracted entity.

Name -> (string)

Provides a name or contextual description about the trait.

Score -> (float)

The level of confidence that Amazon Comprehend Medical has in the accuracy of this trait.

PaginationToken -> (string)

If the result to the `DetectEntitiesV2` operation was truncated, include the `PaginationToken` to fetch the next page of entities.

ModelVersion -> (string)

The version of the model used to analyze the documents. The version number looks like X.X.X. You can use this information to track the model used for a particular batch of documents.