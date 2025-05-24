# create-flywheelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/create-flywheel.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/create-flywheel.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [comprehend](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/index.html#cli-aws-comprehend) ]

# create-flywheel

## Description

A flywheel is an Amazon Web Services resource that orchestrates the ongoing training of a model for custom classification or custom entity recognition. You can create a flywheel to start with an existing trained model, or Comprehend can create and train a new model.

When you create the flywheel, Comprehend creates a data lake in your account. The data lake holds the training data and test data for all versions of the model.

To use a flywheel with an existing trained model, you specify the active model version. Comprehend copies the modelâs training data and test data into the flywheelâs data lake.

To use the flywheel with a new model, you need to provide a dataset for training data (and optional test data) when you create the flywheel.

For more information about flywheels, see [Flywheel overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html) in the *Amazon Comprehend Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/CreateFlywheel)

## Synopsis

```
create-flywheel
--flywheel-name <value>
[--active-model-arn <value>]
--data-access-role-arn <value>
[--task-config <value>]
[--model-type <value>]
--data-lake-s3-uri <value>
[--data-security-config <value>]
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

`--flywheel-name` (string)

Name for the flywheel.

`--active-model-arn` (string)

To associate an existing model with the flywheel, specify the Amazon Resource Number (ARN) of the model version. Do not set `TaskConfig` or `ModelType` if you specify an `ActiveModelArn` .

`--data-access-role-arn` (string)

The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend the permissions required to access the flywheel data in the data lake.

`--task-config` (structure)

Configuration about the model associated with the flywheel. You need to set `TaskConfig` if you are creating a flywheel for a new model.

LanguageCode -> (string)

Language code for the language that the model supports.

DocumentClassificationConfig -> (structure)

Configuration required for a document classification model.

Mode -> (string)

Classification mode indicates whether the documents are `MULTI_CLASS` or `MULTI_LABEL` .

Labels -> (list)

One or more labels to associate with the custom classifier.

(string)

EntityRecognitionConfig -> (structure)

Configuration required for an entity recognition model.

EntityTypes -> (list)

Up to 25 entity types that the model is trained to recognize.

(structure)

An entity type within a labeled training dataset that Amazon Comprehend uses to train a custom entity recognizer.

Type -> (string)

An entity type within a labeled training dataset that Amazon Comprehend uses to train a custom entity recognizer.

Entity types must not contain the following invalid characters: n (line break), \n (escaped line break, r (carriage return), \r (escaped carriage return), t (tab), \t (escaped tab), and , (comma).

JSON Syntax:

```
{
  "LanguageCode": "en"|"es"|"fr"|"de"|"it"|"pt"|"ar"|"hi"|"ja"|"ko"|"zh"|"zh-TW",
  "DocumentClassificationConfig": {
    "Mode": "MULTI_CLASS"|"MULTI_LABEL",
    "Labels": ["string", ...]
  },
  "EntityRecognitionConfig": {
    "EntityTypes": [
      {
        "Type": "string"
      }
      ...
    ]
  }
}
```

`--model-type` (string)

The model type. You need to set `ModelType` if you are creating a flywheel for a new model.

Possible values:

- `DOCUMENT_CLASSIFIER`
- `ENTITY_RECOGNIZER`

`--data-lake-s3-uri` (string)

Enter the S3 location for the data lake. You can specify a new S3 bucket or a new folder of an existing S3 bucket. The flywheel creates the data lake at this location.

`--data-security-config` (structure)

Data security configurations.

ModelKmsKeyId -> (string)

ID for the KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:

- KMS Key ID: `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- Amazon Resource Name (ARN) of a KMS Key: `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`

VolumeKmsKeyId -> (string)

ID for the KMS key that Amazon Comprehend uses to encrypt the volume.

DataLakeKmsKeyId -> (string)

ID for the KMS key that Amazon Comprehend uses to encrypt the data in the data lake.

VpcConfig -> (structure)

Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for the job. For more information, see [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) .

SecurityGroupIds -> (list)

The ID number for a security group on an instance of your private VPC. Security groups on your VPC function serve as a virtual firewall to control inbound and outbound traffic and provides security for the resources that youâll be accessing on the VPC. This ID number is preceded by âsg-â, for instance: âsg-03b388029b0a285eaâ. For more information, see [Security Groups for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) .

(string)

Subnets -> (list)

The ID for each subnet being used in your private VPC. This subnet is a subset of the a range of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPCâs Region. This ID number is preceded by âsubnet-â, for instance: âsubnet-04ccf456919e69055â. For more information, see [VPCs and Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) .

(string)

Shorthand Syntax:

```
ModelKmsKeyId=string,VolumeKmsKeyId=string,DataLakeKmsKeyId=string,VpcConfig={SecurityGroupIds=[string,string],Subnets=[string,string]}
```

JSON Syntax:

```
{
  "ModelKmsKeyId": "string",
  "VolumeKmsKeyId": "string",
  "DataLakeKmsKeyId": "string",
  "VpcConfig": {
    "SecurityGroupIds": ["string", ...],
    "Subnets": ["string", ...]
  }
}
```

`--client-request-token` (string)

A unique identifier for the request. If you donât set the client request token, Amazon Comprehend generates one.

`--tags` (list)

The tags to associate with this flywheel.

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

**To create a flywheel**

The following `create-flywheel` example creates a flywheel to orchestrate the ongoing training of either a document classification or entity
recognition model. The flywheel in this example is created to manage an existing trained model specified by the `--active-model-arn` tag.
When the flywheel is created, a data lake is created at the `--input-data-lake` tag.

```
aws comprehend create-flywheel \
    --flywheel-name example-flywheel \
    --active-model-arn arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-model/version/1 \
    --data-access-role-arn arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role \
    --data-lake-s3-uri "s3://amzn-s3-demo-bucket"
```

Output:

```
{
    "FlywheelArn": "arn:aws:comprehend:us-west-2:111122223333:flywheel/example-flywheel"
}
```

For more information, see [Flywheel Overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html) in *Amazon Comprehend Developer Guide*.

## Output

FlywheelArn -> (string)

The Amazon Resource Number (ARN) of the flywheel.

ActiveModelArn -> (string)

The Amazon Resource Number (ARN) of the active model version.