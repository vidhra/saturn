# create-datasetÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/create-dataset.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/create-dataset.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [comprehend](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/index.html#cli-aws-comprehend) ]

# create-dataset

## Description

Creates a dataset to upload training or test data for a model associated with a flywheel. For more information about datasets, see [Flywheel overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html) in the *Amazon Comprehend Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/CreateDataset)

## Synopsis

```
create-dataset
--flywheel-arn <value>
--dataset-name <value>
[--dataset-type <value>]
[--description <value>]
--input-data-config <value>
[--client-request-token <value>]
[--tags <value>]
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

`--flywheel-arn` (string)

The Amazon Resource Number (ARN) of the flywheel of the flywheel to receive the data.

`--dataset-name` (string)

Name of the dataset.

`--dataset-type` (string)

The dataset type. You can specify that the data in a dataset is for training the model or for testing the model.

Possible values:

- `TRAIN`
- `TEST`

`--description` (string)

Description of the dataset.

`--input-data-config` (structure)

Information about the input data configuration. The type of input data varies based on the format of the input and whether the data is for a classifier model or an entity recognition model.

AugmentedManifests -> (list)

A list of augmented manifest files that provide training data for your custom model. An augmented manifest file is a labeled dataset that is produced by Amazon SageMaker Ground Truth.

(structure)

An augmented manifest file that provides training data for your custom model. An augmented manifest file is a labeled dataset that is produced by Amazon SageMaker Ground Truth.

AttributeNames -> (list)

The JSON attribute that contains the annotations for your training documents. The number of attribute names that you specify depends on whether your augmented manifest file is the output of a single labeling job or a chained labeling job.

If your file is the output of a single labeling job, specify the LabelAttributeName key that was used when the job was created in Ground Truth.

If your file is the output of a chained labeling job, specify the LabelAttributeName key for one or more jobs in the chain. Each LabelAttributeName key provides the annotations from an individual job.

(string)

S3Uri -> (string)

The Amazon S3 location of the augmented manifest file.

AnnotationDataS3Uri -> (string)

The S3 prefix to the annotation files that are referred in the augmented manifest file.

SourceDocumentsS3Uri -> (string)

The S3 prefix to the source files (PDFs) that are referred to in the augmented manifest file.

DocumentType -> (string)

The type of augmented manifest. If you donât specify, the default is PlainTextDocument.

`PLAIN_TEXT_DOCUMENT` A document type that represents any unicode text that is encoded in UTF-8.

DataFormat -> (string)

`COMPREHEND_CSV` : The data format is a two-column CSV file, where the first column contains labels and the second column contains documents.

`AUGMENTED_MANIFEST` : The data format

DocumentClassifierInputDataConfig -> (structure)

The input properties for training a document classifier model.

For more information on how the input file is formatted, see [Preparing training data](https://docs.aws.amazon.com/comprehend/latest/dg/prep-classifier-data.html) in the Comprehend Developer Guide.

S3Uri -> (string)

The Amazon S3 URI for the input data. The S3 bucket must be in the same Region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of input files.

For example, if you use the URI `S3://bucketName/prefix` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.

This parameter is required if you set `DataFormat` to `COMPREHEND_CSV` .

LabelDelimiter -> (string)

Indicates the delimiter used to separate each label for training a multi-label classifier. The default delimiter between labels is a pipe (|). You can use a different character as a delimiter (if itâs an allowed character) by specifying it under Delimiter for labels. If the training documents use a delimiter other than the default or the delimiter you specify, the labels on that line will be combined to make a single unique label, such as LABELLABELLABEL.

EntityRecognizerInputDataConfig -> (structure)

The input properties for training an entity recognizer model.

Annotations -> (structure)

The S3 location of the annotation documents for your custom entity recognizer.

S3Uri -> (string)

Specifies the Amazon S3 location where the training documents for an entity recognizer are located. The URI must be in the same Region as the API endpoint that you are calling.

Documents -> (structure)

The format and location of the training documents for your custom entity recognizer.

S3Uri -> (string)

Specifies the Amazon S3 location where the documents for the dataset are located.

InputFormat -> (string)

Specifies how the text in an input file should be processed. This is optional, and the default is ONE_DOC_PER_LINE. ONE_DOC_PER_FILE - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. ONE_DOC_PER_LINE - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.

EntityList -> (structure)

The S3 location of the entity list for your custom entity recognizer.

S3Uri -> (string)

Specifies the Amazon S3 location where the entity list is located.

JSON Syntax:

```
{
  "AugmentedManifests": [
    {
      "AttributeNames": ["string", ...],
      "S3Uri": "string",
      "AnnotationDataS3Uri": "string",
      "SourceDocumentsS3Uri": "string",
      "DocumentType": "PLAIN_TEXT_DOCUMENT"|"SEMI_STRUCTURED_DOCUMENT"
    }
    ...
  ],
  "DataFormat": "COMPREHEND_CSV"|"AUGMENTED_MANIFEST",
  "DocumentClassifierInputDataConfig": {
    "S3Uri": "string",
    "LabelDelimiter": "string"
  },
  "EntityRecognizerInputDataConfig": {
    "Annotations": {
      "S3Uri": "string"
    },
    "Documents": {
      "S3Uri": "string",
      "InputFormat": "ONE_DOC_PER_FILE"|"ONE_DOC_PER_LINE"
    },
    "EntityList": {
      "S3Uri": "string"
    }
  }
}
```

`--client-request-token` (string)

A unique identifier for the request. If you donât set the client request token, Amazon Comprehend generates one.

`--tags` (list)

Tags for the dataset.

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

**To create a flywheel dataset**

The following `create-dataset` example creates a dataset for a flywheel. This dataset will be used as additional training data as specified by the
`--dataset-type` tag.

```
aws comprehend create-dataset \
    --flywheel-arn arn:aws:comprehend:us-west-2:111122223333:flywheel/flywheel-entity \
    --dataset-name example-dataset \
    --dataset-type "TRAIN" \
    --input-data-config file://inputConfig.json
```

Contents of `file://inputConfig.json`:

```
{
    "DataFormat": "COMPREHEND_CSV",
    "DocumentClassifierInputDataConfig": {
        "S3Uri": "s3://amzn-s3-demo-bucket/training-data.csv"
    }
}
```

Output:

```
{
    "DatasetArn": "arn:aws:comprehend:us-west-2:111122223333:flywheel/flywheel-entity/dataset/example-dataset"
}
```

For more information, see [Flywheel Overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html) in *Amazon Comprehend Developer Guide*.

## Output

DatasetArn -> (string)

The ARN of the dataset.