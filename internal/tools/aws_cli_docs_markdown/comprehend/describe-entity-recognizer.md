# describe-entity-recognizerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-entity-recognizer.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-entity-recognizer.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [comprehend](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/index.html#cli-aws-comprehend) ]

# describe-entity-recognizer

## Description

Provides details about an entity recognizer including status, S3 buckets containing training data, recognizer metadata, metrics, and so on.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DescribeEntityRecognizer)

## Synopsis

```
describe-entity-recognizer
--entity-recognizer-arn <value>
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

`--entity-recognizer-arn` (string)

The Amazon Resource Name (ARN) that identifies the entity recognizer.

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

**To describe an entity recognizer**

The following `describe-entity-recognizer` example gets the properties of a custom entity recognizer model.

```
aws comprehend describe-entity-recognizer \
    entity-recognizer-arn arn:aws:comprehend:us-west-2:111122223333:entity-recognizer/business-recongizer-1/version/1
```

Output:

```
{
    "EntityRecognizerProperties": {
        "EntityRecognizerArn": "arn:aws:comprehend:us-west-2:111122223333:entity-recognizer/business-recongizer-1/version/1",
        "LanguageCode": "en",
        "Status": "TRAINED",
        "SubmitTime": "2023-06-14T20:44:59.631000+00:00",
        "EndTime": "2023-06-14T20:59:19.532000+00:00",
        "TrainingStartTime": "2023-06-14T20:48:52.811000+00:00",
        "TrainingEndTime": "2023-06-14T20:58:11.473000+00:00",
        "InputDataConfig": {
            "DataFormat": "COMPREHEND_CSV",
            "EntityTypes": [
                {
                    "Type": "BUSINESS"
                }
            ],
            "Documents": {
                "S3Uri": "s3://amzn-s3-demo-bucket/trainingdata/dataset/",
                "InputFormat": "ONE_DOC_PER_LINE"
            },
            "EntityList": {
                "S3Uri": "s3://amzn-s3-demo-bucket/trainingdata/entity.csv"
            }
        },
        "RecognizerMetadata": {
            "NumberOfTrainedDocuments": 1814,
            "NumberOfTestDocuments": 486,
            "EvaluationMetrics": {
                "Precision": 100.0,
                "Recall": 100.0,
                "F1Score": 100.0
            },
            "EntityTypes": [
                {
                    "Type": "BUSINESS",
                    "EvaluationMetrics": {
                        "Precision": 100.0,
                        "Recall": 100.0,
                        "F1Score": 100.0
                    },
                    "NumberOfTrainMentions": 1520
                }
            ]
        },
        "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role",
        "VersionName": "1"
    }
}
```

For more information, see [Custom entity recognition](https://docs.aws.amazon.com/comprehend/latest/dg/custom-entity-recognition.html) in the *Amazon Comprehend Developer Guide*.

## Output

EntityRecognizerProperties -> (structure)

Describes information associated with an entity recognizer.

EntityRecognizerArn -> (string)

The Amazon Resource Name (ARN) that identifies the entity recognizer.

LanguageCode -> (string)

The language of the input documents. All documents must be in the same language. Only English (âenâ) is currently supported.

Status -> (string)

Provides the status of the entity recognizer.

Message -> (string)

A description of the status of the recognizer.

SubmitTime -> (timestamp)

The time that the recognizer was submitted for processing.

EndTime -> (timestamp)

The time that the recognizer creation completed.

TrainingStartTime -> (timestamp)

The time that training of the entity recognizer started.

TrainingEndTime -> (timestamp)

The time that training of the entity recognizer was completed.

InputDataConfig -> (structure)

The input data properties of an entity recognizer.

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

RecognizerMetadata -> (structure)

Provides information about an entity recognizer.

NumberOfTrainedDocuments -> (integer)

The number of documents in the input data that were used to train the entity recognizer. Typically this is 80 to 90 percent of the input documents.

NumberOfTestDocuments -> (integer)

The number of documents in the input data that were used to test the entity recognizer. Typically this is 10 to 20 percent of the input documents.

EvaluationMetrics -> (structure)

Detailed information about the accuracy of an entity recognizer.

Precision -> (double)

A measure of the usefulness of the recognizer results in the test data. High precision means that the recognizer returned substantially more relevant results than irrelevant ones.

Recall -> (double)

A measure of how complete the recognizer results are for the test data. High recall means that the recognizer returned most of the relevant results.

F1Score -> (double)

A measure of how accurate the recognizer results are for the test data. It is derived from the `Precision` and `Recall` values. The `F1Score` is the harmonic average of the two scores. For plain text entity recognizer models, the range is 0 to 100, where 100 is the best score. For PDF/Word entity recognizer models, the range is 0 to 1, where 1 is the best score.

EntityTypes -> (list)

Entity types from the metadata of an entity recognizer.

(structure)

Individual item from the list of entity types in the metadata of an entity recognizer.

Type -> (string)

Type of entity from the list of entity types in the metadata of an entity recognizer.

EvaluationMetrics -> (structure)

Detailed information about the accuracy of the entity recognizer for a specific item on the list of entity types.

Precision -> (double)

A measure of the usefulness of the recognizer results for a specific entity type in the test data. High precision means that the recognizer returned substantially more relevant results than irrelevant ones.

Recall -> (double)

A measure of how complete the recognizer results are for a specific entity type in the test data. High recall means that the recognizer returned most of the relevant results.

F1Score -> (double)

A measure of how accurate the recognizer results are for a specific entity type in the test data. It is derived from the `Precision` and `Recall` values. The `F1Score` is the harmonic average of the two scores. The highest score is 1, and the worst score is 0.

NumberOfTrainMentions -> (integer)

Indicates the number of times the given entity type was seen in the training data.

DataAccessRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.

VolumeKmsKeyId -> (string)

ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:

- KMS Key ID: `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- Amazon Resource Name (ARN) of a KMS Key: `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`

VpcConfig -> (structure)

Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources you are using for your custom entity recognizer. For more information, see [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) .

SecurityGroupIds -> (list)

The ID number for a security group on an instance of your private VPC. Security groups on your VPC function serve as a virtual firewall to control inbound and outbound traffic and provides security for the resources that youâll be accessing on the VPC. This ID number is preceded by âsg-â, for instance: âsg-03b388029b0a285eaâ. For more information, see [Security Groups for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) .

(string)

Subnets -> (list)

The ID for each subnet being used in your private VPC. This subnet is a subset of the a range of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPCâs Region. This ID number is preceded by âsubnet-â, for instance: âsubnet-04ccf456919e69055â. For more information, see [VPCs and Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) .

(string)

ModelKmsKeyId -> (string)

ID for the KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:

- KMS Key ID: `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- Amazon Resource Name (ARN) of a KMS Key: `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`

VersionName -> (string)

The version name you assigned to the entity recognizer.

SourceModelArn -> (string)

The Amazon Resource Name (ARN) of the source model. This model was imported from a different Amazon Web Services account to create the entity recognizer model in your Amazon Web Services account.

FlywheelArn -> (string)

The Amazon Resource Number (ARN) of the flywheel

OutputDataConfig -> (structure)

Output data configuration.

FlywheelStatsS3Prefix -> (string)

The Amazon S3 prefix for the data lake location of the flywheel statistics.