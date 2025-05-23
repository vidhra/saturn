# infer-icd10-cmÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/infer-icd10-cm.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/infer-icd10-cm.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [comprehendmedical](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/index.html#cli-aws-comprehendmedical) ]

# infer-icd10-cm

## Description

InferICD10CM detects medical conditions as entities listed in a patient record and links those entities to normalized concept identifiers in the ICD-10-CM knowledge base from the Centers for Disease Control. Amazon Comprehend Medical only detects medical entities in English language texts.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/comprehendmedical-2018-10-30/InferICD10CM)

## Synopsis

```
infer-icd10-cm
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

The input text used for analysis.

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

**Example 1: To detect medical condition entities and link to the ICD-10-CM Ontology directly from text**

The following `infer-icd10-cm` example labels the detected medical condition entities and links those entities with codes in the 2019 edition of the International Classification of Diseases Clinical Modification (ICD-10-CM).

```
aws comprehendmedical infer-icd10-cm \
    --text "The patient complains of abdominal pain, has a long-standing history of diabetes treated with Micronase daily."
```

Output:

```
{
    "Entities": [
        {
            "Id": 0,
            "Text": "abdominal pain",
            "Category": "MEDICAL_CONDITION",
            "Type": "DX_NAME",
            "Score": 0.9475538730621338,
            "BeginOffset": 28,
            "EndOffset": 42,
            "Attributes": [],
            "Traits": [
                {
                    "Name": "SYMPTOM",
                    "Score": 0.6724207401275635
                }
            ],
            "ICD10CMConcepts": [
                {
                    "Description": "Unspecified abdominal pain",
                    "Code": "R10.9",
                    "Score": 0.6904221177101135
                },
                {
                    "Description": "Epigastric pain",
                    "Code": "R10.13",
                    "Score": 0.1364113688468933
                },
                {
                    "Description": "Generalized abdominal pain",
                    "Code": "R10.84",
                    "Score": 0.12508003413677216
                },
                {
                    "Description": "Left lower quadrant pain",
                    "Code": "R10.32",
                    "Score": 0.10063883662223816
                },
                {
                    "Description": "Lower abdominal pain, unspecified",
                    "Code": "R10.30",
                    "Score": 0.09933677315711975
                }
            ]
        },
        {
            "Id": 1,
            "Text": "diabetes",
            "Category": "MEDICAL_CONDITION",
            "Type": "DX_NAME",
            "Score": 0.9899052977561951,
            "BeginOffset": 75,
            "EndOffset": 83,
            "Attributes": [],
            "Traits": [
                {
                    "Name": "DIAGNOSIS",
                    "Score": 0.9258432388305664
                }
            ],
            "ICD10CMConcepts": [
                {
                    "Description": "Type 2 diabetes mellitus without complications",
                    "Code": "E11.9",
                    "Score": 0.7158446311950684
                },
                {
                    "Description": "Family history of diabetes mellitus",
                    "Code": "Z83.3",
                    "Score": 0.5704703330993652
                },
                {
                    "Description": "Family history of other endocrine, nutritional and metabolic diseases",
                    "Code": "Z83.49",
                    "Score": 0.19856023788452148
                },
                {
                    "Description": "Type 1 diabetes mellitus with ketoacidosis without coma",
                    "Code": "E10.10",
                    "Score": 0.13285516202449799
                },
                {
                    "Description": "Type 2 diabetes mellitus with hyperglycemia",
                    "Code": "E11.65",
                    "Score": 0.0993388369679451
                }
            ]
        }
    ],
    "ModelVersion": "0.1.0"
}
```

For more information, see [Infer ICD10-CM](https://docs.aws.amazon.com/comprehend/latest/dg/ontology-linking-icd10.html) in the *Amazon Comprehend Medical Developer Guide*.

**Example 2: To detect medical condition entities and link to the ICD-10-CM Ontology from a file pathway**

The following `infer-icd-10-cm` example labels the detected medical condition entities and links those entities with codes in the 2019 edition of the International Classification of Diseases Clinical Modification (ICD-10-CM).

```
aws comprehendmedical infer-icd10-cm \
    --text file://icd10cm.txt
```

Contents of `icd10cm.txt`:

```
{
    "The patient complains of abdominal pain, has a long-standing history of diabetes treated with Micronase daily."
}
```

Output:

```
{
    "Entities": [
        {
            "Id": 0,
            "Text": "abdominal pain",
            "Category": "MEDICAL_CONDITION",
            "Type": "DX_NAME",
            "Score": 0.9475538730621338,
            "BeginOffset": 28,
            "EndOffset": 42,
            "Attributes": [],
            "Traits": [
                {
                    "Name": "SYMPTOM",
                    "Score": 0.6724207401275635
                }
            ],
            "ICD10CMConcepts": [
                {
                    "Description": "Unspecified abdominal pain",
                    "Code": "R10.9",
                    "Score": 0.6904221177101135
                },
                {
                    "Description": "Epigastric pain",
                    "Code": "R10.13",
                    "Score": 0.1364113688468933
                },
                {
                    "Description": "Generalized abdominal pain",
                    "Code": "R10.84",
                    "Score": 0.12508003413677216
                },
                {
                    "Description": "Left lower quadrant pain",
                    "Code": "R10.32",
                    "Score": 0.10063883662223816
                },
                {
                    "Description": "Lower abdominal pain, unspecified",
                    "Code": "R10.30",
                    "Score": 0.09933677315711975
                }
            ]
        },
        {
            "Id": 1,
            "Text": "diabetes",
            "Category": "MEDICAL_CONDITION",
            "Type": "DX_NAME",
            "Score": 0.9899052977561951,
            "BeginOffset": 75,
            "EndOffset": 83,
            "Attributes": [],
            "Traits": [
                {
                    "Name": "DIAGNOSIS",
                    "Score": 0.9258432388305664
                }
            ],
            "ICD10CMConcepts": [
                {
                    "Description": "Type 2 diabetes mellitus without complications",
                    "Code": "E11.9",
                    "Score": 0.7158446311950684
                },
                {
                    "Description": "Family history of diabetes mellitus",
                    "Code": "Z83.3",
                    "Score": 0.5704703330993652
                },
                {
                    "Description": "Family history of other endocrine, nutritional and metabolic diseases",
                    "Code": "Z83.49",
                    "Score": 0.19856023788452148
                },
                {
                    "Description": "Type 1 diabetes mellitus with ketoacidosis without coma",
                    "Code": "E10.10",
                    "Score": 0.13285516202449799
                },
                {
                    "Description": "Type 2 diabetes mellitus with hyperglycemia",
                    "Code": "E11.65",
                    "Score": 0.0993388369679451
                }
            ]
        }
    ],
    "ModelVersion": "0.1.0"
}
```

For more information, see [Infer-ICD10-CM](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontology-icd10.html) in the *Amazon Comprehend Medical Developer Guide*.

## Output

Entities -> (list)

The medical conditions detected in the text linked to ICD-10-CM concepts. If the action is successful, the service sends back an HTTP 200 response, as well as the entities detected.

(structure)

The collection of medical entities extracted from the input text and their associated information. For each entity, the response provides the entity text, the entity category, where the entity text begins and ends, and the level of confidence that Amazon Comprehend Medical has in the detection and analysis. Attributes and traits of the entity are also returned.

Id -> (integer)

The numeric identifier for the entity. This is a monotonically increasing id unique within this response rather than a global unique identifier.

Text -> (string)

The segment of input text that is matched to the detected entity.

Category -> (string)

The category of the entity. InferICD10CM detects entities in the `MEDICAL_CONDITION` category.

Type -> (string)

Describes the specific type of entity with category of entities. InferICD10CM detects entities of the type `DX_NAME` and `TIME_EXPRESSION` .

Score -> (float)

The level of confidence that Amazon Comprehend Medical has in the accuracy of the detection.

BeginOffset -> (integer)

The 0-based character offset in the input text that shows where the entity begins. The offset returns the UTF-8 code point in the string.

EndOffset -> (integer)

The 0-based character offset in the input text that shows where the entity ends. The offset returns the UTF-8 code point in the string.

Attributes -> (list)

The detected attributes that relate to the entity. An extracted segment of the text that is an attribute of an entity, or otherwise related to an entity, such as the nature of a medical condition.

(structure)

The detected attributes that relate to an entity. This includes an extracted segment of the text that is an attribute of an entity, or otherwise related to an entity. InferICD10CM detects the following attributes: `Direction` , `System, Organ or Site` , and `Acuity` .

Type -> (string)

The type of attribute. InferICD10CM detects entities of the type `DX_NAME` .

Score -> (float)

The level of confidence that Amazon Comprehend Medical has that the segment of text is correctly recognized as an attribute.

RelationshipScore -> (float)

The level of confidence that Amazon Comprehend Medical has that this attribute is correctly related to this entity.

Id -> (integer)

The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier.

BeginOffset -> (integer)

The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string.

EndOffset -> (integer)

The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string.

Text -> (string)

The segment of input text which contains the detected attribute.

Traits -> (list)

The contextual information for the attribute. The traits recognized by InferICD10CM are `DIAGNOSIS` , `SIGN` , `SYMPTOM` , and `NEGATION` .

(structure)

Contextual information for the entity. The traits recognized by InferICD10CM are `DIAGNOSIS` , `SIGN` , `SYMPTOM` , and `NEGATION` .

Name -> (string)

Provides a name or contextual description about the trait.

Score -> (float)

The level of confidence that Amazon Comprehend Medical has that the segment of text is correctly recognized as a trait.

Category -> (string)

The category of attribute. Can be either of `DX_NAME` or `TIME_EXPRESSION` .

RelationshipType -> (string)

The type of relationship between the entity and attribute. Type for the relationship can be either of `OVERLAP` or `SYSTEM_ORGAN_SITE` .

Traits -> (list)

Provides Contextual information for the entity. The traits recognized by InferICD10CM are `DIAGNOSIS` , `SIGN` , `SYMPTOM` , and `NEGATION.`

(structure)

Contextual information for the entity. The traits recognized by InferICD10CM are `DIAGNOSIS` , `SIGN` , `SYMPTOM` , and `NEGATION` .

Name -> (string)

Provides a name or contextual description about the trait.

Score -> (float)

The level of confidence that Amazon Comprehend Medical has that the segment of text is correctly recognized as a trait.

ICD10CMConcepts -> (list)

The ICD-10-CM concepts that the entity could refer to, along with a score indicating the likelihood of the match.

(structure)

The ICD-10-CM concepts that the entity could refer to, along with a score indicating the likelihood of the match.

Description -> (string)

The long description of the ICD-10-CM code in the ontology.

Code -> (string)

The ICD-10-CM code that identifies the concept found in the knowledge base from the Centers for Disease Control.

Score -> (float)

The level of confidence that Amazon Comprehend Medical has that the entity is accurately linked to an ICD-10-CM concept.

PaginationToken -> (string)

If the result of the previous request to `InferICD10CM` was truncated, include the `PaginationToken` to fetch the next page of medical condition entities.

ModelVersion -> (string)

The version of the model used to analyze the documents, in the format *n* .*n* .*n* You can use this information to track the model used for a particular batch of documents.