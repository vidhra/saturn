# infer-snomedctÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/infer-snomedct.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/infer-snomedct.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [comprehendmedical](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/index.html#cli-aws-comprehendmedical) ]

# infer-snomedct

## Description

InferSNOMEDCT detects possible medical concepts as entities and links them to codes from the Systematized Nomenclature of Medicine, Clinical Terms (SNOMED-CT) ontology

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/comprehendmedical-2018-10-30/InferSNOMEDCT)

## Synopsis

```
infer-snomedct
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

The input text to be analyzed using InferSNOMEDCT.

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

**Example: To detect entities and link to the SNOMED CT Ontology directly from text**

The following `infer-snomedct` example shows how to detect medical entities and link them to concepts from the 2021-03 version of the Systematized Nomenclature of Medicine, Clinical Terms (SNOMED CT).

```
aws comprehendmedical infer-snomedct \
    --text "The patient complains of abdominal pain, has a long-standing history of diabetes treated with Micronase daily."
```

Output:

```
{
    "Entities": [
        {
            "Id": 3,
            "BeginOffset": 26,
            "EndOffset": 40,
            "Score": 0.9598260521888733,
            "Text": "abdominal pain",
            "Category": "MEDICAL_CONDITION",
            "Type": "DX_NAME",
            "Traits": [
                {
                    "Name": "SYMPTOM",
                    "Score": 0.6819021701812744
                }
            ]
        },
        {
            "Id": 4,
            "BeginOffset": 73,
            "EndOffset": 81,
            "Score": 0.9905840158462524,
            "Text": "diabetes",
            "Category": "MEDICAL_CONDITION",
            "Type": "DX_NAME",
            "Traits": [
                {
                    "Name": "DIAGNOSIS",
                    "Score": 0.9255214333534241
                }
            ]
        },
        {
            "Id": 1,
            "BeginOffset": 95,
            "EndOffset": 104,
            "Score": 0.6371926665306091,
            "Text": "Micronase",
            "Category": "MEDICATION",
            "Type": "BRAND_NAME",
            "Traits": [],
            "Attributes": [
                {
                    "Type": "FREQUENCY",
                    "Score": 0.9761165380477905,
                    "RelationshipScore": 0.9984188079833984,
                    "RelationshipType": "FREQUENCY",
                    "Id": 2,
                    "BeginOffset": 105,
                    "EndOffset": 110,
                    "Text": "daily",
                    "Category": "MEDICATION",
                    "Traits": []
                }
            ]
        }
    ],
    "UnmappedAttributes": [],
    "ModelVersion": "1.0.0"
}
```

For more information, see [InferSNOMEDCT](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontology-linking-snomed.html) in the *Amazon Comprehend Medical Developer Guide*.

## Output

Entities -> (list)

The collection of medical concept entities extracted from the input text and their associated information. For each entity, the response provides the entity text, the entity category, where the entity text begins and ends, and the level of confidence that Amazon Comprehend Medical has in the detection and analysis. Attributes and traits of the entity are also returned.

(structure)

The collection of medical entities extracted from the input text and their associated information. For each entity, the response provides the entity text, the entity category, where the entity text begins and ends, and the level of confidence that Amazon Comprehend Medical has in the detection and analysis. Attributes and traits of the entity are also returned.

Id -> (integer)

The numeric identifier for the entity. This is a monotonically increasing id unique within this response rather than a global unique identifier.

Text -> (string)

The segment of input text extracted as this entity.

Category -> (string)

The category of the detected entity. Possible categories are MEDICAL_CONDITION, ANATOMY, or TEST_TREATMENT_PROCEDURE.

Type -> (string)

Describes the specific type of entity with category of entities. Possible types include DX_NAME, ACUITY, DIRECTION, SYSTEM_ORGAN_SITE, TEST_NAME, TEST_VALUE, TEST_UNIT, PROCEDURE_NAME, or TREATMENT_NAME.

Score -> (float)

The level of confidence that Amazon Comprehend Medical has in the accuracy of the detected entity.

BeginOffset -> (integer)

The 0-based character offset in the input text that shows where the entity begins. The offset returns the UTF-8 code point in the string.

EndOffset -> (integer)

The 0-based character offset in the input text that shows where the entity ends. The offset returns the UTF-8 code point in the string.

Attributes -> (list)

An extracted segment of the text that is an attribute of an entity, or otherwise related to an entity, such as the dosage of a medication taken.

(structure)

The extracted attributes that relate to an entity. An extracted segment of the text that is an attribute of an entity, or otherwise related to an entity, such as the dosage of a medication taken.

Category -> (string)

The category of the detected attribute. Possible categories include MEDICAL_CONDITION, ANATOMY, and TEST_TREATMENT_PROCEDURE.

Type -> (string)

The type of attribute. Possible types include DX_NAME, ACUITY, DIRECTION, SYSTEM_ORGAN_SITE,TEST_NAME, TEST_VALUE, TEST_UNIT, PROCEDURE_NAME, and TREATMENT_NAME.

Score -> (float)

The level of confidence that Amazon Comprehend Medical has that the segment of text is correctly recognized as an attribute.

RelationshipScore -> (float)

The level of confidence that Amazon Comprehend Medical has that this attribute is correctly related to this entity.

RelationshipType -> (string)

The type of relationship that exists between the entity and the related attribute.

Id -> (integer)

The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier.

BeginOffset -> (integer)

The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string.

EndOffset -> (integer)

The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string.

Text -> (string)

The segment of input text extracted as this attribute.

Traits -> (list)

Contextual information for an attribute. Examples include signs, symptoms, diagnosis, and negation.

(structure)

Contextual information for an entity.

Name -> (string)

The name or contextual description of a detected trait.

Score -> (float)

The level of confidence that Amazon Comprehend Medical has in the accuracy of a detected trait.

SNOMEDCTConcepts -> (list)

The SNOMED-CT concepts specific to an attribute, along with a score indicating the likelihood of the match.

(structure)

The SNOMED-CT concepts that the entity could refer to, along with a score indicating the likelihood of the match.

Description -> (string)

The description of the SNOMED-CT concept.

Code -> (string)

The numeric ID for the SNOMED-CT concept.

Score -> (float)

The level of confidence Amazon Comprehend Medical has that the entity should be linked to the identified SNOMED-CT concept.

Traits -> (list)

Contextual information for the entity.

(structure)

Contextual information for an entity.

Name -> (string)

The name or contextual description of a detected trait.

Score -> (float)

The level of confidence that Amazon Comprehend Medical has in the accuracy of a detected trait.

SNOMEDCTConcepts -> (list)

The SNOMED concepts that the entity could refer to, along with a score indicating the likelihood of the match.

(structure)

The SNOMED-CT concepts that the entity could refer to, along with a score indicating the likelihood of the match.

Description -> (string)

The description of the SNOMED-CT concept.

Code -> (string)

The numeric ID for the SNOMED-CT concept.

Score -> (float)

The level of confidence Amazon Comprehend Medical has that the entity should be linked to the identified SNOMED-CT concept.

PaginationToken -> (string)

If the result of the request is truncated, the pagination token can be used to fetch the next page of entities.

ModelVersion -> (string)

The version of the model used to analyze the documents, in the format n.n.n You can use this information to track the model used for a particular batch of documents.

SNOMEDCTDetails -> (structure)

The details of the SNOMED-CT revision, including the edition, language, and version date.

Edition -> (string)

The edition of SNOMED-CT used. The edition used for the InferSNOMEDCT editions is the US edition.

Language -> (string)

The language used in the SNOMED-CT ontology. All Amazon Comprehend Medical operations are US English (en).

VersionDate -> (string)

The version date of the SNOMED-CT ontology used.

Characters -> (structure)

The number of characters in the input request documentation.

OriginalTextCharacters -> (integer)

The number of characters present in the input text document as processed by Amazon Comprehend Medical.