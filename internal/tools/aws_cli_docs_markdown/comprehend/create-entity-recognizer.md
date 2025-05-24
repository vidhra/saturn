# create-entity-recognizerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/create-entity-recognizer.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/create-entity-recognizer.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [comprehend](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/index.html#cli-aws-comprehend) ]

# create-entity-recognizer

## Description

Creates an entity recognizer using submitted files. After your `CreateEntityRecognizer` request is submitted, you can check job status using the `DescribeEntityRecognizer` API.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/CreateEntityRecognizer)

## Synopsis

```
create-entity-recognizer
--recognizer-name <value>
[--version-name <value>]
--data-access-role-arn <value>
[--tags <value>]
--input-data-config <value>
[--client-request-token <value>]
--language-code <value>
[--volume-kms-key-id <value>]
[--vpc-config <value>]
[--model-kms-key-id <value>]
[--model-policy <value>]
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

`--recognizer-name` (string)

The name given to the newly created recognizer. Recognizer names can be a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The name must be unique in the account/Region.

`--version-name` (string)

The version name given to the newly created recognizer. Version names can be a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The version name must be unique among all models with the same recognizer name in the account/Region.

`--data-access-role-arn` (string)

The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.

`--tags` (list)

Tags to associate with the entity recognizer. A tag is a key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with âSalesâ as the key might be added to a resource to indicate its use by the sales department.

(structure)

A key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with the key-value pair âDepartmentâ:âSalesâ might be added to a resource to indicate its use by a particular department.

Key -> (string)

The initial part of a key-value pair that forms a tag associated with a given resource. For instance, if you want to show which resources are used by which departments, you might use âDepartmentâ as the key portion of the pair, with multiple possible values such as âsales,â âlegal,â and âadministration.â

Value -> (string)

The second part of a key-value pair that forms a tag associated with a given resource. For instance, if you want to show which resources are used by which departments, you might use âDepartmentâ as the initial (key) portion of the pair, with a value of âsalesâ to indicate the sales department.

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

`--input-data-config` (structure)

Specifies the format and location of the input data. The S3 bucket containing the input data must be located in the same Region as the entity recognizer being created.

DataFormat -> (string)

The format of your training data:

- `COMPREHEND_CSV` : A CSV file that supplements your training documents. The CSV file contains information about the custom entities that your trained model will detect. The required format of the file depends on whether you are providing annotations or an entity list. If you use this value, you must provide your CSV file by using either the `Annotations` or `EntityList` parameters. You must provide your training documents by using the `Documents` parameter.
- `AUGMENTED_MANIFEST` : A labeled dataset that is produced by Amazon SageMaker Ground Truth. This file is in JSON lines format. Each line is a complete JSON object that contains a training document and its labels. Each label annotates a named entity in the training document.  If you use this value, you must provide the `AugmentedManifests` parameter in your request.

If you donât specify a value, Amazon Comprehend uses `COMPREHEND_CSV` as the default.

EntityTypes -> (list)

The entity types in the labeled training data that Amazon Comprehend uses to train the custom entity recognizer. Any entity types that you donât specify are ignored.

A maximum of 25 entity types can be used at one time to train an entity recognizer. Entity types must not contain the following invalid characters: n (line break), \n (escaped line break), r (carriage return), \r (escaped carriage return), t (tab), \t (escaped tab), space, and , (comma).

(structure)

An entity type within a labeled training dataset that Amazon Comprehend uses to train a custom entity recognizer.

Type -> (string)

An entity type within a labeled training dataset that Amazon Comprehend uses to train a custom entity recognizer.

Entity types must not contain the following invalid characters: n (line break), \n (escaped line break, r (carriage return), \r (escaped carriage return), t (tab), \t (escaped tab), and , (comma).

Documents -> (structure)

The S3 location of the folder that contains the training documents for your custom entity recognizer.

This parameter is required if you set `DataFormat` to `COMPREHEND_CSV` .

S3Uri -> (string)

Specifies the Amazon S3 location where the training documents for an entity recognizer are located. The URI must be in the same Region as the API endpoint that you are calling.

TestS3Uri -> (string)

Specifies the Amazon S3 location where the test documents for an entity recognizer are located. The URI must be in the same Amazon Web Services Region as the API endpoint that you are calling.

InputFormat -> (string)

Specifies how the text in an input file should be processed. This is optional, and the default is ONE_DOC_PER_LINE. ONE_DOC_PER_FILE - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. ONE_DOC_PER_LINE - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.

Annotations -> (structure)

The S3 location of the CSV file that annotates your training documents.

S3Uri -> (string)

Specifies the Amazon S3 location where the annotations for an entity recognizer are located. The URI must be in the same Region as the API endpoint that you are calling.

TestS3Uri -> (string)

Specifies the Amazon S3 location where the test annotations for an entity recognizer are located. The URI must be in the same Region as the API endpoint that you are calling.

EntityList -> (structure)

The S3 location of the CSV file that has the entity list for your custom entity recognizer.

S3Uri -> (string)

Specifies the Amazon S3 location where the entity list is located. The URI must be in the same Region as the API endpoint that you are calling.

AugmentedManifests -> (list)

A list of augmented manifest files that provide training data for your custom model. An augmented manifest file is a labeled dataset that is produced by Amazon SageMaker Ground Truth.

This parameter is required if you set `DataFormat` to `AUGMENTED_MANIFEST` .

(structure)

An augmented manifest file that provides training data for your custom model. An augmented manifest file is a labeled dataset that is produced by Amazon SageMaker Ground Truth.

S3Uri -> (string)

The Amazon S3 location of the augmented manifest file.

Split -> (string)

The purpose of the data youâve provided in the augmented manifest. You can either train or test this data. If you donât specify, the default is train.

TRAIN - all of the documents in the manifest will be used for training. If no test documents are provided, Amazon Comprehend will automatically reserve a portion of the training documents for testing.

TEST - all of the documents in the manifest will be used for testing.

AttributeNames -> (list)

The JSON attribute that contains the annotations for your training documents. The number of attribute names that you specify depends on whether your augmented manifest file is the output of a single labeling job or a chained labeling job.

If your file is the output of a single labeling job, specify the LabelAttributeName key that was used when the job was created in Ground Truth.

If your file is the output of a chained labeling job, specify the LabelAttributeName key for one or more jobs in the chain. Each LabelAttributeName key provides the annotations from an individual job.

(string)

AnnotationDataS3Uri -> (string)

The S3 prefix to the annotation files that are referred in the augmented manifest file.

SourceDocumentsS3Uri -> (string)

The S3 prefix to the source files (PDFs) that are referred to in the augmented manifest file.

DocumentType -> (string)

The type of augmented manifest. PlainTextDocument or SemiStructuredDocument. If you donât specify, the default is PlainTextDocument.

- `PLAIN_TEXT_DOCUMENT` A document type that represents any unicode text that is encoded in UTF-8.
- `SEMI_STRUCTURED_DOCUMENT` A document type with positional and structural context, like a PDF. For training with Amazon Comprehend, only PDFs are supported. For inference, Amazon Comprehend support PDFs, DOCX and TXT.

JSON Syntax:

```
{
  "DataFormat": "COMPREHEND_CSV"|"AUGMENTED_MANIFEST",
  "EntityTypes": [
    {
      "Type": "string"
    }
    ...
  ],
  "Documents": {
    "S3Uri": "string",
    "TestS3Uri": "string",
    "InputFormat": "ONE_DOC_PER_FILE"|"ONE_DOC_PER_LINE"
  },
  "Annotations": {
    "S3Uri": "string",
    "TestS3Uri": "string"
  },
  "EntityList": {
    "S3Uri": "string"
  },
  "AugmentedManifests": [
    {
      "S3Uri": "string",
      "Split": "TRAIN"|"TEST",
      "AttributeNames": ["string", ...],
      "AnnotationDataS3Uri": "string",
      "SourceDocumentsS3Uri": "string",
      "DocumentType": "PLAIN_TEXT_DOCUMENT"|"SEMI_STRUCTURED_DOCUMENT"
    }
    ...
  ]
}
```

`--client-request-token` (string)

A unique identifier for the request. If you donât set the client request token, Amazon Comprehend generates one.

`--language-code` (string)

You can specify any of the following languages: English (âenâ), Spanish (âesâ), French (âfrâ), Italian (âitâ), German (âdeâ), or Portuguese (âptâ). If you plan to use this entity recognizer with PDF, Word, or image input files, you must specify English as the language. All training documents must be in the same language.

Possible values:

- `en`
- `es`
- `fr`
- `de`
- `it`
- `pt`
- `ar`
- `hi`
- `ja`
- `ko`
- `zh`
- `zh-TW`

`--volume-kms-key-id` (string)

ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:

- KMS Key ID: `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- Amazon Resource Name (ARN) of a KMS Key: `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`

`--vpc-config` (structure)

Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your custom entity recognizer. For more information, see [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) .

SecurityGroupIds -> (list)

The ID number for a security group on an instance of your private VPC. Security groups on your VPC function serve as a virtual firewall to control inbound and outbound traffic and provides security for the resources that youâll be accessing on the VPC. This ID number is preceded by âsg-â, for instance: âsg-03b388029b0a285eaâ. For more information, see [Security Groups for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) .

(string)

Subnets -> (list)

The ID for each subnet being used in your private VPC. This subnet is a subset of the a range of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPCâs Region. This ID number is preceded by âsubnet-â, for instance: âsubnet-04ccf456919e69055â. For more information, see [VPCs and Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) .

(string)

Shorthand Syntax:

```
SecurityGroupIds=string,string,Subnets=string,string
```

JSON Syntax:

```
{
  "SecurityGroupIds": ["string", ...],
  "Subnets": ["string", ...]
}
```

`--model-kms-key-id` (string)

ID for the KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:

- KMS Key ID: `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- Amazon Resource Name (ARN) of a KMS Key: `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`

`--model-policy` (string)

The JSON resource-based policy to attach to your custom entity recognizer model. You can use this policy to allow another Amazon Web Services account to import your custom model.

Provide your JSON as a UTF-8 encoded string without line breaks. To provide valid JSON for your policy, enclose the attribute names and values in double quotes. If the JSON body is also enclosed in double quotes, then you must escape the double quotes that are inside the policy:

`"{\"attribute\": \"value\", \"attribute\": [\"value\"]}"`

To avoid escaping quotes, you can use single quotes to enclose the policy and double quotes to enclose the JSON names and values:

`'{"attribute": "value", "attribute": ["value"]}'`

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

**To create a custom entity recognizer**

The following `create-entity-recognizer` example begins the training process for a custom entity recognizer model. This example uses a CSV file containing training documents, `raw_text.csv`, and a CSV entity list, `entity_list.csv` to train the model.
`entity-list.csv` contains the following columns: text and type.

```
aws comprehend create-entity-recognizer \
    --recognizer-name example-entity-recognizer
    --data-access-role-arn arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role \
    --input-data-config "EntityTypes=[{Type=DEVICE}],Documents={S3Uri=s3://amzn-s3-demo-bucket/trainingdata/raw_text.csv},EntityList={S3Uri=s3://amzn-s3-demo-bucket/trainingdata/entity_list.csv}"
    --language-code en
```

Output:

```
{
    "EntityRecognizerArn": "arn:aws:comprehend:us-west-2:111122223333:example-entity-recognizer/entityrecognizer1"
}
```

For more information, see [Custom entity recognition](https://docs.aws.amazon.com/comprehend/latest/dg/custom-entity-recognition.html) in the *Amazon Comprehend Developer Guide*.

## Output

EntityRecognizerArn -> (string)

The Amazon Resource Name (ARN) that identifies the entity recognizer.