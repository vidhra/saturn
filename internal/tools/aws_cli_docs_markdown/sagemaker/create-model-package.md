# create-model-packageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-model-package.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-model-package.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-model-package

## Description

Creates a model package that you can use to create SageMaker models or list on Amazon Web Services Marketplace, or a versioned model that is part of a model group. Buyers can subscribe to model packages listed on Amazon Web Services Marketplace to create models in SageMaker.

To create a model package by specifying a Docker container that contains your inference code and the Amazon S3 location of your model artifacts, provide values for `InferenceSpecification` . To create a model from an algorithm resource that you created or subscribed to in Amazon Web Services Marketplace, provide a value for `SourceAlgorithmSpecification` .

### Note

There are two types of model packages:

- Versioned - a model that is part of a model group in the model registry.
- Unversioned - a model package that is not part of a model group.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateModelPackage)

## Synopsis

```
create-model-package
[--model-package-name <value>]
[--model-package-group-name <value>]
[--model-package-description <value>]
[--inference-specification <value>]
[--validation-specification <value>]
[--source-algorithm-specification <value>]
[--certify-for-marketplace | --no-certify-for-marketplace]
[--tags <value>]
[--model-approval-status <value>]
[--metadata-properties <value>]
[--model-metrics <value>]
[--client-token <value>]
[--domain <value>]
[--task <value>]
[--sample-payload-url <value>]
[--customer-metadata-properties <value>]
[--drift-check-baselines <value>]
[--additional-inference-specifications <value>]
[--skip-model-validation <value>]
[--source-uri <value>]
[--security-config <value>]
[--model-card <value>]
[--model-life-cycle <value>]
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

`--model-package-name` (string)

The name of the model package. The name must have 1 to 63 characters. Valid characters are a-z, A-Z, 0-9, and - (hyphen).

This parameter is required for unversioned models. It is not applicable to versioned models.

`--model-package-group-name` (string)

The name or Amazon Resource Name (ARN) of the model package group that this model version belongs to.

This parameter is required for versioned models, and does not apply to unversioned models.

`--model-package-description` (string)

A description of the model package.

`--inference-specification` (structure)

Specifies details about inference jobs that you can run with models based on this model package, including the following information:

- The Amazon ECR paths of containers that contain the inference code and model artifacts.
- The instance types that the model package supports for transform jobs and real-time endpoints used for inference.
- The input and output content formats that the model package supports for inference.

Containers -> (list)

The Amazon ECR registry path of the Docker image that contains the inference code.

(structure)

Describes the Docker container for the model package.

ContainerHostname -> (string)

The DNS host name for the Docker container.

Image -> (string)

The Amazon Elastic Container Registry (Amazon ECR) path where inference code is stored.

If you are using your own custom algorithm instead of an algorithm provided by SageMaker, the inference code must meet SageMaker requirements. SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html) .

ImageDigest -> (string)

An MD5 hash of the training algorithm that identifies the Docker image used for training.

ModelDataUrl -> (string)

The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single `gzip` compressed tar archive (`.tar.gz` suffix).

### Note

The model artifacts must be in an S3 bucket that is in the same region as the model package.

ModelDataSource -> (structure)

Specifies the location of ML model data to deploy during endpoint creation.

S3DataSource -> (structure)

Specifies the S3 location of ML model data to deploy.

S3Uri -> (string)

Specifies the S3 path of ML model data to deploy.

S3DataType -> (string)

Specifies the type of ML model data to deploy.

If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix as part of the ML model data to deploy. A valid key name prefix identified by `S3Uri` always ends with a forward slash (/).

If you choose `S3Object` , `S3Uri` identifies an object that is the ML model data to deploy.

CompressionType -> (string)

Specifies how the ML model data is prepared.

If you choose `Gzip` and choose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that is a gzip-compressed TAR archive. SageMaker will attempt to decompress and untar the object during model deployment.

If you choose `None` and chooose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that represents an uncompressed ML model to deploy.

If you choose None and choose `S3Prefix` as the value of `S3DataType` , `S3Uri` identifies a key name prefix, under which all objects represents the uncompressed ML model to deploy.

If you choose None, then SageMaker will follow rules below when creating model data files under /opt/ml/model directory for use by your inference code:

- If you choose `S3Object` as the value of `S3DataType` , then SageMaker will split the key of the S3 object referenced by `S3Uri` by slash (/), and use the last part as the filename of the file holding the content of the S3 object.
- If you choose `S3Prefix` as the value of `S3DataType` , then for each S3 object under the key name pefix referenced by `S3Uri` , SageMaker will trim its key by the prefix, and use the remainder as the path (relative to `/opt/ml/model` ) of the file holding the content of the S3 object. SageMaker will split the remainder by slash (/), using intermediate parts as directory names and the last part as filename of the file holding the content of the S3 object.
- Do not use any of the following as file names or directory names:
- An empty or blank string
- A string which contains null bytes
- A string longer than 255 bytes
- A single dot (`.` )
- A double dot (`..` )
- Ambiguous file names will result in model deployment failure. For example, if your uncompressed ML model consists of two S3 objects `s3://mybucket/model/weights` and `s3://mybucket/model/weights/part1` and you specify `s3://mybucket/model/` as the value of `S3Uri` and `S3Prefix` as the value of `S3DataType` , then it will result in name clash between `/opt/ml/model/weights` (a regular file) and `/opt/ml/model/weights/` (a directory).
- Do not organize the model artifacts in [S3 console using folders](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html) . When you create a folder in S3 console, S3 creates a 0-byte object with a key set to the folder name you provide. They key of the 0-byte object ends with a slash (/) which violates SageMaker restrictions on model artifact file names, leading to model deployment failure.

ModelAccessConfig -> (structure)

Specifies the access configuration file for the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig` . You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

AcceptEula -> (boolean)

Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

HubAccessConfig -> (structure)

Configuration information for hub access.

HubContentArn -> (string)

The ARN of the hub content for which deployment access is allowed.

ManifestS3Uri -> (string)

The Amazon S3 URI of the manifest file. The manifest file is a CSV file that stores the artifact locations.

ETag -> (string)

The ETag associated with S3 URI.

ManifestEtag -> (string)

The ETag associated with Manifest S3 URI.

ProductId -> (string)

The Amazon Web Services Marketplace product ID of the model package.

Environment -> (map)

The environment variables to set in the Docker container. Each key and value in the `Environment` string to string map can have length of up to 1024. We support up to 16 entries in the map.

key -> (string)

value -> (string)

ModelInput -> (structure)

A structure with Model Input details.

DataInputConfig -> (string)

The input configuration object for the model.

Framework -> (string)

The machine learning framework of the model package container image.

FrameworkVersion -> (string)

The framework version of the Model Package Container Image.

NearestModelName -> (string)

The name of a pre-trained machine learning benchmarked by Amazon SageMaker Inference Recommender model that matches your model. You can find a list of benchmarked models by calling `ListModelMetadata` .

AdditionalS3DataSource -> (structure)

The additional data source that is used during inference in the Docker container for your model package.

S3DataType -> (string)

The data type of the additional data source that you specify for use in inference or training.

S3Uri -> (string)

The uniform resource identifier (URI) used to identify an additional data source used in inference or training.

CompressionType -> (string)

The type of compression used for an additional data source used in inference or training. Specify `None` if your additional data source is not compressed.

ETag -> (string)

The ETag associated with S3 URI.

ModelDataETag -> (string)

The ETag associated with Model Data URL.

SupportedTransformInstanceTypes -> (list)

A list of the instance types on which a transformation job can be run or on which an endpoint can be deployed.

This parameter is required for unversioned models, and optional for versioned models.

(string)

SupportedRealtimeInferenceInstanceTypes -> (list)

A list of the instance types that are used to generate inferences in real-time.

This parameter is required for unversioned models, and optional for versioned models.

(string)

SupportedContentTypes -> (list)

The supported MIME types for the input data.

(string)

SupportedResponseMIMETypes -> (list)

The supported MIME types for the output data.

(string)

JSON Syntax:

```
{
  "Containers": [
    {
      "ContainerHostname": "string",
      "Image": "string",
      "ImageDigest": "string",
      "ModelDataUrl": "string",
      "ModelDataSource": {
        "S3DataSource": {
          "S3Uri": "string",
          "S3DataType": "S3Prefix"|"S3Object",
          "CompressionType": "None"|"Gzip",
          "ModelAccessConfig": {
            "AcceptEula": true|false
          },
          "HubAccessConfig": {
            "HubContentArn": "string"
          },
          "ManifestS3Uri": "string",
          "ETag": "string",
          "ManifestEtag": "string"
        }
      },
      "ProductId": "string",
      "Environment": {"string": "string"
        ...},
      "ModelInput": {
        "DataInputConfig": "string"
      },
      "Framework": "string",
      "FrameworkVersion": "string",
      "NearestModelName": "string",
      "AdditionalS3DataSource": {
        "S3DataType": "S3Object"|"S3Prefix",
        "S3Uri": "string",
        "CompressionType": "None"|"Gzip",
        "ETag": "string"
      },
      "ModelDataETag": "string"
    }
    ...
  ],
  "SupportedTransformInstanceTypes": ["ml.m4.xlarge"|"ml.m4.2xlarge"|"ml.m4.4xlarge"|"ml.m4.10xlarge"|"ml.m4.16xlarge"|"ml.c4.xlarge"|"ml.c4.2xlarge"|"ml.c4.4xlarge"|"ml.c4.8xlarge"|"ml.p2.xlarge"|"ml.p2.8xlarge"|"ml.p2.16xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.18xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.12xlarge"|"ml.m5.24xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.c6i.large"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.r6i.large"|"ml.r6i.xlarge"|"ml.r6i.2xlarge"|"ml.r6i.4xlarge"|"ml.r6i.8xlarge"|"ml.r6i.12xlarge"|"ml.r6i.16xlarge"|"ml.r6i.24xlarge"|"ml.r6i.32xlarge"|"ml.m7i.large"|"ml.m7i.xlarge"|"ml.m7i.2xlarge"|"ml.m7i.4xlarge"|"ml.m7i.8xlarge"|"ml.m7i.12xlarge"|"ml.m7i.16xlarge"|"ml.m7i.24xlarge"|"ml.m7i.48xlarge"|"ml.c7i.large"|"ml.c7i.xlarge"|"ml.c7i.2xlarge"|"ml.c7i.4xlarge"|"ml.c7i.8xlarge"|"ml.c7i.12xlarge"|"ml.c7i.16xlarge"|"ml.c7i.24xlarge"|"ml.c7i.48xlarge"|"ml.r7i.large"|"ml.r7i.xlarge"|"ml.r7i.2xlarge"|"ml.r7i.4xlarge"|"ml.r7i.8xlarge"|"ml.r7i.12xlarge"|"ml.r7i.16xlarge"|"ml.r7i.24xlarge"|"ml.r7i.48xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.12xlarge"|"ml.g5.16xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.inf2.xlarge"|"ml.inf2.8xlarge"|"ml.inf2.24xlarge"|"ml.inf2.48xlarge", ...],
  "SupportedRealtimeInferenceInstanceTypes": ["ml.t2.medium"|"ml.t2.large"|"ml.t2.xlarge"|"ml.t2.2xlarge"|"ml.m4.xlarge"|"ml.m4.2xlarge"|"ml.m4.4xlarge"|"ml.m4.10xlarge"|"ml.m4.16xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.12xlarge"|"ml.m5.24xlarge"|"ml.m5d.large"|"ml.m5d.xlarge"|"ml.m5d.2xlarge"|"ml.m5d.4xlarge"|"ml.m5d.12xlarge"|"ml.m5d.24xlarge"|"ml.c4.large"|"ml.c4.xlarge"|"ml.c4.2xlarge"|"ml.c4.4xlarge"|"ml.c4.8xlarge"|"ml.p2.xlarge"|"ml.p2.8xlarge"|"ml.p2.16xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.c5.large"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.18xlarge"|"ml.c5d.large"|"ml.c5d.xlarge"|"ml.c5d.2xlarge"|"ml.c5d.4xlarge"|"ml.c5d.9xlarge"|"ml.c5d.18xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.12xlarge"|"ml.r5.24xlarge"|"ml.r5d.large"|"ml.r5d.xlarge"|"ml.r5d.2xlarge"|"ml.r5d.4xlarge"|"ml.r5d.12xlarge"|"ml.r5d.24xlarge"|"ml.inf1.xlarge"|"ml.inf1.2xlarge"|"ml.inf1.6xlarge"|"ml.inf1.24xlarge"|"ml.dl1.24xlarge"|"ml.c6i.large"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.r6i.large"|"ml.r6i.xlarge"|"ml.r6i.2xlarge"|"ml.r6i.4xlarge"|"ml.r6i.8xlarge"|"ml.r6i.12xlarge"|"ml.r6i.16xlarge"|"ml.r6i.24xlarge"|"ml.r6i.32xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.12xlarge"|"ml.g5.16xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.12xlarge"|"ml.g6.16xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.r8g.medium"|"ml.r8g.large"|"ml.r8g.xlarge"|"ml.r8g.2xlarge"|"ml.r8g.4xlarge"|"ml.r8g.8xlarge"|"ml.r8g.12xlarge"|"ml.r8g.16xlarge"|"ml.r8g.24xlarge"|"ml.r8g.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.12xlarge"|"ml.g6e.16xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.p4d.24xlarge"|"ml.c7g.large"|"ml.c7g.xlarge"|"ml.c7g.2xlarge"|"ml.c7g.4xlarge"|"ml.c7g.8xlarge"|"ml.c7g.12xlarge"|"ml.c7g.16xlarge"|"ml.m6g.large"|"ml.m6g.xlarge"|"ml.m6g.2xlarge"|"ml.m6g.4xlarge"|"ml.m6g.8xlarge"|"ml.m6g.12xlarge"|"ml.m6g.16xlarge"|"ml.m6gd.large"|"ml.m6gd.xlarge"|"ml.m6gd.2xlarge"|"ml.m6gd.4xlarge"|"ml.m6gd.8xlarge"|"ml.m6gd.12xlarge"|"ml.m6gd.16xlarge"|"ml.c6g.large"|"ml.c6g.xlarge"|"ml.c6g.2xlarge"|"ml.c6g.4xlarge"|"ml.c6g.8xlarge"|"ml.c6g.12xlarge"|"ml.c6g.16xlarge"|"ml.c6gd.large"|"ml.c6gd.xlarge"|"ml.c6gd.2xlarge"|"ml.c6gd.4xlarge"|"ml.c6gd.8xlarge"|"ml.c6gd.12xlarge"|"ml.c6gd.16xlarge"|"ml.c6gn.large"|"ml.c6gn.xlarge"|"ml.c6gn.2xlarge"|"ml.c6gn.4xlarge"|"ml.c6gn.8xlarge"|"ml.c6gn.12xlarge"|"ml.c6gn.16xlarge"|"ml.r6g.large"|"ml.r6g.xlarge"|"ml.r6g.2xlarge"|"ml.r6g.4xlarge"|"ml.r6g.8xlarge"|"ml.r6g.12xlarge"|"ml.r6g.16xlarge"|"ml.r6gd.large"|"ml.r6gd.xlarge"|"ml.r6gd.2xlarge"|"ml.r6gd.4xlarge"|"ml.r6gd.8xlarge"|"ml.r6gd.12xlarge"|"ml.r6gd.16xlarge"|"ml.p4de.24xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.trn2.48xlarge"|"ml.inf2.xlarge"|"ml.inf2.8xlarge"|"ml.inf2.24xlarge"|"ml.inf2.48xlarge"|"ml.p5.48xlarge"|"ml.p5e.48xlarge"|"ml.p5en.48xlarge"|"ml.m7i.large"|"ml.m7i.xlarge"|"ml.m7i.2xlarge"|"ml.m7i.4xlarge"|"ml.m7i.8xlarge"|"ml.m7i.12xlarge"|"ml.m7i.16xlarge"|"ml.m7i.24xlarge"|"ml.m7i.48xlarge"|"ml.c7i.large"|"ml.c7i.xlarge"|"ml.c7i.2xlarge"|"ml.c7i.4xlarge"|"ml.c7i.8xlarge"|"ml.c7i.12xlarge"|"ml.c7i.16xlarge"|"ml.c7i.24xlarge"|"ml.c7i.48xlarge"|"ml.r7i.large"|"ml.r7i.xlarge"|"ml.r7i.2xlarge"|"ml.r7i.4xlarge"|"ml.r7i.8xlarge"|"ml.r7i.12xlarge"|"ml.r7i.16xlarge"|"ml.r7i.24xlarge"|"ml.r7i.48xlarge", ...],
  "SupportedContentTypes": ["string", ...],
  "SupportedResponseMIMETypes": ["string", ...]
}
```

`--validation-specification` (structure)

Specifies configurations for one or more transform jobs that SageMaker runs to test the model package.

ValidationRole -> (string)

The IAM roles to be used for the validation of the model package.

ValidationProfiles -> (list)

An array of `ModelPackageValidationProfile` objects, each of which specifies a batch transform job that SageMaker runs to validate your model package.

(structure)

Contains data, such as the inputs and targeted instance types that are used in the process of validating the model package.

The data provided in the validation profile is made available to your buyers on Amazon Web Services Marketplace.

ProfileName -> (string)

The name of the profile for the model package.

TransformJobDefinition -> (structure)

The `TransformJobDefinition` object that describes the transform job used for the validation of the model package.

MaxConcurrentTransforms -> (integer)

The maximum number of parallel requests that can be sent to each instance in a transform job. The default value is 1.

MaxPayloadInMB -> (integer)

The maximum payload size allowed, in MB. A payload is the data portion of a record (without metadata).

BatchStrategy -> (string)

A string that determines the number of records included in a single mini-batch.

`SingleRecord` means only one record is used per mini-batch. `MultiRecord` means a mini-batch is set to contain as many records that can fit within the `MaxPayloadInMB` limit.

Environment -> (map)

The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.

key -> (string)

value -> (string)

TransformInput -> (structure)

A description of the input source and the way the transform job consumes it.

DataSource -> (structure)

Describes the location of the channel data, which is, the S3 location of the input data that the model can consume.

S3DataSource -> (structure)

The S3 location of the data source that is associated with a channel.

S3DataType -> (string)

If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for batch transform.

If you choose `ManifestFile` , `S3Uri` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for batch transform.

The following values are compatible: `ManifestFile` , `S3Prefix`

The following value is not compatible: `AugmentedManifestFile`

S3Uri -> (string)

Depending on the value specified for the `S3DataType` , identifies either a key name prefix or a manifest. For example:

- A key name prefix might look like this: `s3://bucketname/exampleprefix/` .
- A manifest might look like this: `s3://bucketname/example.manifest`   The manifest is an S3 object which is a JSON file with the following format:   `[ {"prefix": "s3://customer_bucket/some/prefix/"},` `"relative/path/to/custdata-1",` `"relative/path/custdata-2",` `...` `"relative/path/custdata-N"` `]`   The preceding JSON matches the following `S3Uris` :   `s3://customer_bucket/some/prefix/relative/path/to/custdata-1` `s3://customer_bucket/some/prefix/relative/path/custdata-2` `...` `s3://customer_bucket/some/prefix/relative/path/custdata-N`   The complete set of `S3Uris` in this manifest constitutes the input data for the channel for this datasource. The object that each `S3Uris` points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.

ContentType -> (string)

The multipurpose internet mail extension (MIME) type of the data. Amazon SageMaker uses the MIME type with each http call to transfer data to the transform job.

CompressionType -> (string)

If your transform data is compressed, specify the compression type. Amazon SageMaker automatically decompresses the data for the transform job accordingly. The default value is `None` .

SplitType -> (string)

The method to use to split the transform jobâs data files into smaller batches. Splitting is necessary when the total size of each object is too large to fit in a single request. You can also use data splitting to improve performance by processing multiple concurrent mini-batches. The default value for `SplitType` is `None` , which indicates that input data files are not split, and request payloads contain the entire contents of an input object. Set the value of this parameter to `Line` to split records on a newline character boundary. `SplitType` also supports a number of record-oriented binary data formats. Currently, the supported record formats are:

- RecordIO
- TFRecord

When splitting is enabled, the size of a mini-batch depends on the values of the `BatchStrategy` and `MaxPayloadInMB` parameters. When the value of `BatchStrategy` is `MultiRecord` , Amazon SageMaker sends the maximum number of records in each request, up to the `MaxPayloadInMB` limit. If the value of `BatchStrategy` is `SingleRecord` , Amazon SageMaker sends individual records in each request.

### Note

Some data formats represent a record as a binary payload wrapped with extra padding bytes. When splitting is applied to a binary data format, padding is removed if the value of `BatchStrategy` is set to `SingleRecord` . Padding is not removed if the value of `BatchStrategy` is set to `MultiRecord` .

For more information about `RecordIO` , see [Create a Dataset Using RecordIO](https://mxnet.apache.org/api/faq/recordio) in the MXNet documentation. For more information about `TFRecord` , see [Consuming TFRecord data](https://www.tensorflow.org/guide/data#consuming_tfrecord_data) in the TensorFlow documentation.

TransformOutput -> (structure)

Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job.

S3OutputPath -> (string)

The Amazon S3 path where you want Amazon SageMaker to store the results of the transform job. For example, `s3://bucket-name/key-name-prefix` .

For every S3 object used as input for the transform job, batch transform stores the transformed data with an .``out`` suffix in a corresponding subfolder in the location in the output prefix. For example, for the input data stored at `s3://bucket-name/input-name-prefix/dataset01/data.csv` , batch transform stores the transformed data at `s3://bucket-name/output-name-prefix/input-name-prefix/data.csv.out` . Batch transform doesnât upload partially processed objects. For an input S3 object that contains multiple records, it creates an .``out`` file only if the transform job succeeds on the entire file. When the input contains multiple S3 objects, the batch transform job processes the listed S3 objects and uploads only the output for successfully processed objects. If any object fails in the transform job batch transform marks the job as failed to prompt investigation.

Accept -> (string)

The MIME type used to specify the output data. Amazon SageMaker uses the MIME type with each http call to transfer data from the transform job.

AssembleWith -> (string)

Defines how to assemble the results of the transform job as a single S3 object. Choose a format that is most convenient to you. To concatenate the results in binary format, specify `None` . To add a newline character at the end of every transformed record, specify `Line` .

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The `KmsKeyId` can be any of the following formats:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias name ARN: `arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias`

If you donât provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your roleâs account. For more information, see [KMS-Managed Encryption Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html) in the *Amazon Simple Storage Service Developer Guide.*

The KMS key policy must grant permission to the IAM role that you specify in your [CreateModel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModel.html) request. For more information, see [Using Key Policies in Amazon Web Services KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *Amazon Web Services Key Management Service Developer Guide* .

TransformResources -> (structure)

Identifies the ML compute instances for the transform job.

InstanceType -> (string)

The ML compute instance type for the transform job. If you are using built-in algorithms to transform moderately sized datasets, we recommend using ml.m4.xlarge or `ml.m5.large` instance types.

InstanceCount -> (integer)

The number of ML compute instances to use in the transform job. The default value is `1` , and the maximum is `100` . For distributed transform jobs, specify a value greater than `1` .

VolumeKmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt model data on the storage volume attached to the ML compute instance(s) that run the batch transform job.

### Note

Certain Nitro-based instances include local storage, dependent on the instance type. Local storage volumes are encrypted using a hardware module on the instance. You canât request a `VolumeKmsKeyId` when using an instance type with local storage.

For a list of instance types that support local instance storage, see [Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes) .

For more information about local instance storage encryption, see [SSD Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html) .

The `VolumeKmsKeyId` can be any of the following formats:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias name ARN: `arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias`

TransformAmiVersion -> (string)

Specifies an option from a collection of preconfigured Amazon Machine Image (AMI) images. Each image is configured by Amazon Web Services with a set of software and driver versions.

al2-ami-sagemaker-batch-gpu-470

- Accelerator: GPU
- NVIDIA driver version: 470

al2-ami-sagemaker-batch-gpu-535
- Accelerator: GPU
- NVIDIA driver version: 535

JSON Syntax:

```
{
  "ValidationRole": "string",
  "ValidationProfiles": [
    {
      "ProfileName": "string",
      "TransformJobDefinition": {
        "MaxConcurrentTransforms": integer,
        "MaxPayloadInMB": integer,
        "BatchStrategy": "MultiRecord"|"SingleRecord",
        "Environment": {"string": "string"
          ...},
        "TransformInput": {
          "DataSource": {
            "S3DataSource": {
              "S3DataType": "ManifestFile"|"S3Prefix"|"AugmentedManifestFile",
              "S3Uri": "string"
            }
          },
          "ContentType": "string",
          "CompressionType": "None"|"Gzip",
          "SplitType": "None"|"Line"|"RecordIO"|"TFRecord"
        },
        "TransformOutput": {
          "S3OutputPath": "string",
          "Accept": "string",
          "AssembleWith": "None"|"Line",
          "KmsKeyId": "string"
        },
        "TransformResources": {
          "InstanceType": "ml.m4.xlarge"|"ml.m4.2xlarge"|"ml.m4.4xlarge"|"ml.m4.10xlarge"|"ml.m4.16xlarge"|"ml.c4.xlarge"|"ml.c4.2xlarge"|"ml.c4.4xlarge"|"ml.c4.8xlarge"|"ml.p2.xlarge"|"ml.p2.8xlarge"|"ml.p2.16xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.18xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.12xlarge"|"ml.m5.24xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.c6i.large"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.r6i.large"|"ml.r6i.xlarge"|"ml.r6i.2xlarge"|"ml.r6i.4xlarge"|"ml.r6i.8xlarge"|"ml.r6i.12xlarge"|"ml.r6i.16xlarge"|"ml.r6i.24xlarge"|"ml.r6i.32xlarge"|"ml.m7i.large"|"ml.m7i.xlarge"|"ml.m7i.2xlarge"|"ml.m7i.4xlarge"|"ml.m7i.8xlarge"|"ml.m7i.12xlarge"|"ml.m7i.16xlarge"|"ml.m7i.24xlarge"|"ml.m7i.48xlarge"|"ml.c7i.large"|"ml.c7i.xlarge"|"ml.c7i.2xlarge"|"ml.c7i.4xlarge"|"ml.c7i.8xlarge"|"ml.c7i.12xlarge"|"ml.c7i.16xlarge"|"ml.c7i.24xlarge"|"ml.c7i.48xlarge"|"ml.r7i.large"|"ml.r7i.xlarge"|"ml.r7i.2xlarge"|"ml.r7i.4xlarge"|"ml.r7i.8xlarge"|"ml.r7i.12xlarge"|"ml.r7i.16xlarge"|"ml.r7i.24xlarge"|"ml.r7i.48xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.12xlarge"|"ml.g5.16xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.inf2.xlarge"|"ml.inf2.8xlarge"|"ml.inf2.24xlarge"|"ml.inf2.48xlarge",
          "InstanceCount": integer,
          "VolumeKmsKeyId": "string",
          "TransformAmiVersion": "string"
        }
      }
    }
    ...
  ]
}
```

`--source-algorithm-specification` (structure)

Details about the algorithm that was used to create the model package.

SourceAlgorithms -> (list)

A list of the algorithms that were used to create a model package.

(structure)

Specifies an algorithm that was used to create the model package. The algorithm must be either an algorithm resource in your SageMaker account or an algorithm in Amazon Web Services Marketplace that you are subscribed to.

ModelDataUrl -> (string)

The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single `gzip` compressed tar archive (`.tar.gz` suffix).

### Note

The model artifacts must be in an S3 bucket that is in the same Amazon Web Services region as the algorithm.

ModelDataSource -> (structure)

Specifies the location of ML model data to deploy during endpoint creation.

S3DataSource -> (structure)

Specifies the S3 location of ML model data to deploy.

S3Uri -> (string)

Specifies the S3 path of ML model data to deploy.

S3DataType -> (string)

Specifies the type of ML model data to deploy.

If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix as part of the ML model data to deploy. A valid key name prefix identified by `S3Uri` always ends with a forward slash (/).

If you choose `S3Object` , `S3Uri` identifies an object that is the ML model data to deploy.

CompressionType -> (string)

Specifies how the ML model data is prepared.

If you choose `Gzip` and choose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that is a gzip-compressed TAR archive. SageMaker will attempt to decompress and untar the object during model deployment.

If you choose `None` and chooose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that represents an uncompressed ML model to deploy.

If you choose None and choose `S3Prefix` as the value of `S3DataType` , `S3Uri` identifies a key name prefix, under which all objects represents the uncompressed ML model to deploy.

If you choose None, then SageMaker will follow rules below when creating model data files under /opt/ml/model directory for use by your inference code:

- If you choose `S3Object` as the value of `S3DataType` , then SageMaker will split the key of the S3 object referenced by `S3Uri` by slash (/), and use the last part as the filename of the file holding the content of the S3 object.
- If you choose `S3Prefix` as the value of `S3DataType` , then for each S3 object under the key name pefix referenced by `S3Uri` , SageMaker will trim its key by the prefix, and use the remainder as the path (relative to `/opt/ml/model` ) of the file holding the content of the S3 object. SageMaker will split the remainder by slash (/), using intermediate parts as directory names and the last part as filename of the file holding the content of the S3 object.
- Do not use any of the following as file names or directory names:
- An empty or blank string
- A string which contains null bytes
- A string longer than 255 bytes
- A single dot (`.` )
- A double dot (`..` )
- Ambiguous file names will result in model deployment failure. For example, if your uncompressed ML model consists of two S3 objects `s3://mybucket/model/weights` and `s3://mybucket/model/weights/part1` and you specify `s3://mybucket/model/` as the value of `S3Uri` and `S3Prefix` as the value of `S3DataType` , then it will result in name clash between `/opt/ml/model/weights` (a regular file) and `/opt/ml/model/weights/` (a directory).
- Do not organize the model artifacts in [S3 console using folders](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html) . When you create a folder in S3 console, S3 creates a 0-byte object with a key set to the folder name you provide. They key of the 0-byte object ends with a slash (/) which violates SageMaker restrictions on model artifact file names, leading to model deployment failure.

ModelAccessConfig -> (structure)

Specifies the access configuration file for the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig` . You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

AcceptEula -> (boolean)

Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

HubAccessConfig -> (structure)

Configuration information for hub access.

HubContentArn -> (string)

The ARN of the hub content for which deployment access is allowed.

ManifestS3Uri -> (string)

The Amazon S3 URI of the manifest file. The manifest file is a CSV file that stores the artifact locations.

ETag -> (string)

The ETag associated with S3 URI.

ManifestEtag -> (string)

The ETag associated with Manifest S3 URI.

ModelDataETag -> (string)

The ETag associated with Model Data URL.

AlgorithmName -> (string)

The name of an algorithm that was used to create the model package. The algorithm must be either an algorithm resource in your SageMaker account or an algorithm in Amazon Web Services Marketplace that you are subscribed to.

JSON Syntax:

```
{
  "SourceAlgorithms": [
    {
      "ModelDataUrl": "string",
      "ModelDataSource": {
        "S3DataSource": {
          "S3Uri": "string",
          "S3DataType": "S3Prefix"|"S3Object",
          "CompressionType": "None"|"Gzip",
          "ModelAccessConfig": {
            "AcceptEula": true|false
          },
          "HubAccessConfig": {
            "HubContentArn": "string"
          },
          "ManifestS3Uri": "string",
          "ETag": "string",
          "ManifestEtag": "string"
        }
      },
      "ModelDataETag": "string",
      "AlgorithmName": "string"
    }
    ...
  ]
}
```

`--certify-for-marketplace` | `--no-certify-for-marketplace` (boolean)

Whether to certify the model package for listing on Amazon Web Services Marketplace.

This parameter is optional for unversioned models, and does not apply to versioned models.

`--tags` (list)

A list of key value pairs associated with the model. For more information, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference Guide* .

If you supply `ModelPackageGroupName` , your model package belongs to the model group you specify and uses the tags associated with the model group. In this case, you cannot supply a `tag` argument.

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

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

`--model-approval-status` (string)

Whether the model is approved for deployment.

This parameter is optional for versioned models, and does not apply to unversioned models.

For versioned models, the value of this parameter must be set to `Approved` to deploy the model.

Possible values:

- `Approved`
- `Rejected`
- `PendingManualApproval`

`--metadata-properties` (structure)

Metadata properties of the tracking entity, trial, or trial component.

CommitId -> (string)

The commit ID.

Repository -> (string)

The repository.

GeneratedBy -> (string)

The entity this entity was generated by.

ProjectId -> (string)

The project ID.

Shorthand Syntax:

```
CommitId=string,Repository=string,GeneratedBy=string,ProjectId=string
```

JSON Syntax:

```
{
  "CommitId": "string",
  "Repository": "string",
  "GeneratedBy": "string",
  "ProjectId": "string"
}
```

`--model-metrics` (structure)

A structure that contains model metrics reports.

ModelQuality -> (structure)

Metrics that measure the quality of a model.

Statistics -> (structure)

Model quality statistics.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

Constraints -> (structure)

Model quality constraints.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

ModelDataQuality -> (structure)

Metrics that measure the quality of the input data for a model.

Statistics -> (structure)

Data quality statistics for a model.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

Constraints -> (structure)

Data quality constraints for a model.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

Bias -> (structure)

Metrics that measure bias in a model.

Report -> (structure)

The bias report for a model

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

PreTrainingReport -> (structure)

The pre-training bias report for a model.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

PostTrainingReport -> (structure)

The post-training bias report for a model.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

Explainability -> (structure)

Metrics that help explain a model.

Report -> (structure)

The explainability report for a model.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

Shorthand Syntax:

```
ModelQuality={Statistics={ContentType=string,ContentDigest=string,S3Uri=string},Constraints={ContentType=string,ContentDigest=string,S3Uri=string}},ModelDataQuality={Statistics={ContentType=string,ContentDigest=string,S3Uri=string},Constraints={ContentType=string,ContentDigest=string,S3Uri=string}},Bias={Report={ContentType=string,ContentDigest=string,S3Uri=string},PreTrainingReport={ContentType=string,ContentDigest=string,S3Uri=string},PostTrainingReport={ContentType=string,ContentDigest=string,S3Uri=string}},Explainability={Report={ContentType=string,ContentDigest=string,S3Uri=string}}
```

JSON Syntax:

```
{
  "ModelQuality": {
    "Statistics": {
      "ContentType": "string",
      "ContentDigest": "string",
      "S3Uri": "string"
    },
    "Constraints": {
      "ContentType": "string",
      "ContentDigest": "string",
      "S3Uri": "string"
    }
  },
  "ModelDataQuality": {
    "Statistics": {
      "ContentType": "string",
      "ContentDigest": "string",
      "S3Uri": "string"
    },
    "Constraints": {
      "ContentType": "string",
      "ContentDigest": "string",
      "S3Uri": "string"
    }
  },
  "Bias": {
    "Report": {
      "ContentType": "string",
      "ContentDigest": "string",
      "S3Uri": "string"
    },
    "PreTrainingReport": {
      "ContentType": "string",
      "ContentDigest": "string",
      "S3Uri": "string"
    },
    "PostTrainingReport": {
      "ContentType": "string",
      "ContentDigest": "string",
      "S3Uri": "string"
    }
  },
  "Explainability": {
    "Report": {
      "ContentType": "string",
      "ContentDigest": "string",
      "S3Uri": "string"
    }
  }
}
```

`--client-token` (string)

A unique token that guarantees that the call to this API is idempotent.

`--domain` (string)

The machine learning domain of your model package and its components. Common machine learning domains include computer vision and natural language processing.

`--task` (string)

The machine learning task your model package accomplishes. Common machine learning tasks include object detection and image classification. The following tasks are supported by Inference Recommender: `"IMAGE_CLASSIFICATION"` | `"OBJECT_DETECTION"` | `"TEXT_GENERATION"` [|](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-model-package.html#id1)`"IMAGE_SEGMENTATION"` | `"FILL_MASK"` | `"CLASSIFICATION"` | `"REGRESSION"` | `"OTHER"` .

Specify âOTHERâ if none of the tasks listed fit your use case.

`--sample-payload-url` (string)

The Amazon Simple Storage Service (Amazon S3) path where the sample payload is stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix). This archive can hold multiple files that are all equally used in the load test. Each file in the archive must satisfy the size constraints of the [InvokeEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpoint.html#API_runtime_InvokeEndpoint_RequestSyntax) call.

`--customer-metadata-properties` (map)

The metadata properties associated with the model package versions.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--drift-check-baselines` (structure)

Represents the drift check baselines that can be used when the model monitor is set using the model package. For more information, see the topic on [Drift Detection against Previous Baselines in SageMaker Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-quality-clarify-baseline-lifecycle.html#pipelines-quality-clarify-baseline-drift-detection) in the *Amazon SageMaker Developer Guide* .

Bias -> (structure)

Represents the drift check bias baselines that can be used when the model monitor is set using the model package.

ConfigFile -> (structure)

The bias config file for a model.

ContentType -> (string)

The type of content stored in the file source.

ContentDigest -> (string)

The digest of the file source.

S3Uri -> (string)

The Amazon S3 URI for the file source.

PreTrainingConstraints -> (structure)

The pre-training constraints.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

PostTrainingConstraints -> (structure)

The post-training constraints.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

Explainability -> (structure)

Represents the drift check explainability baselines that can be used when the model monitor is set using the model package.

Constraints -> (structure)

The drift check explainability constraints.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

ConfigFile -> (structure)

The explainability config file for the model.

ContentType -> (string)

The type of content stored in the file source.

ContentDigest -> (string)

The digest of the file source.

S3Uri -> (string)

The Amazon S3 URI for the file source.

ModelQuality -> (structure)

Represents the drift check model quality baselines that can be used when the model monitor is set using the model package.

Statistics -> (structure)

The drift check model quality statistics.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

Constraints -> (structure)

The drift check model quality constraints.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

ModelDataQuality -> (structure)

Represents the drift check model data quality baselines that can be used when the model monitor is set using the model package.

Statistics -> (structure)

The drift check model data quality statistics.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

Constraints -> (structure)

The drift check model data quality constraints.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

Shorthand Syntax:

```
Bias={ConfigFile={ContentType=string,ContentDigest=string,S3Uri=string},PreTrainingConstraints={ContentType=string,ContentDigest=string,S3Uri=string},PostTrainingConstraints={ContentType=string,ContentDigest=string,S3Uri=string}},Explainability={Constraints={ContentType=string,ContentDigest=string,S3Uri=string},ConfigFile={ContentType=string,ContentDigest=string,S3Uri=string}},ModelQuality={Statistics={ContentType=string,ContentDigest=string,S3Uri=string},Constraints={ContentType=string,ContentDigest=string,S3Uri=string}},ModelDataQuality={Statistics={ContentType=string,ContentDigest=string,S3Uri=string},Constraints={ContentType=string,ContentDigest=string,S3Uri=string}}
```

JSON Syntax:

```
{
  "Bias": {
    "ConfigFile": {
      "ContentType": "string",
      "ContentDigest": "string",
      "S3Uri": "string"
    },
    "PreTrainingConstraints": {
      "ContentType": "string",
      "ContentDigest": "string",
      "S3Uri": "string"
    },
    "PostTrainingConstraints": {
      "ContentType": "string",
      "ContentDigest": "string",
      "S3Uri": "string"
    }
  },
  "Explainability": {
    "Constraints": {
      "ContentType": "string",
      "ContentDigest": "string",
      "S3Uri": "string"
    },
    "ConfigFile": {
      "ContentType": "string",
      "ContentDigest": "string",
      "S3Uri": "string"
    }
  },
  "ModelQuality": {
    "Statistics": {
      "ContentType": "string",
      "ContentDigest": "string",
      "S3Uri": "string"
    },
    "Constraints": {
      "ContentType": "string",
      "ContentDigest": "string",
      "S3Uri": "string"
    }
  },
  "ModelDataQuality": {
    "Statistics": {
      "ContentType": "string",
      "ContentDigest": "string",
      "S3Uri": "string"
    },
    "Constraints": {
      "ContentType": "string",
      "ContentDigest": "string",
      "S3Uri": "string"
    }
  }
}
```

`--additional-inference-specifications` (list)

An array of additional Inference Specification objects. Each additional Inference Specification specifies artifacts based on this model package that can be used on inference endpoints. Generally used with SageMaker Neo to store the compiled artifacts.

(structure)

A structure of additional Inference Specification. Additional Inference Specification specifies details about inference jobs that can be run with models based on this model package

Name -> (string)

A unique name to identify the additional inference specification. The name must be unique within the list of your additional inference specifications for a particular model package.

Description -> (string)

A description of the additional Inference specification

Containers -> (list)

The Amazon ECR registry path of the Docker image that contains the inference code.

(structure)

Describes the Docker container for the model package.

ContainerHostname -> (string)

The DNS host name for the Docker container.

Image -> (string)

The Amazon Elastic Container Registry (Amazon ECR) path where inference code is stored.

If you are using your own custom algorithm instead of an algorithm provided by SageMaker, the inference code must meet SageMaker requirements. SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html) .

ImageDigest -> (string)

An MD5 hash of the training algorithm that identifies the Docker image used for training.

ModelDataUrl -> (string)

The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single `gzip` compressed tar archive (`.tar.gz` suffix).

### Note

The model artifacts must be in an S3 bucket that is in the same region as the model package.

ModelDataSource -> (structure)

Specifies the location of ML model data to deploy during endpoint creation.

S3DataSource -> (structure)

Specifies the S3 location of ML model data to deploy.

S3Uri -> (string)

Specifies the S3 path of ML model data to deploy.

S3DataType -> (string)

Specifies the type of ML model data to deploy.

If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix as part of the ML model data to deploy. A valid key name prefix identified by `S3Uri` always ends with a forward slash (/).

If you choose `S3Object` , `S3Uri` identifies an object that is the ML model data to deploy.

CompressionType -> (string)

Specifies how the ML model data is prepared.

If you choose `Gzip` and choose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that is a gzip-compressed TAR archive. SageMaker will attempt to decompress and untar the object during model deployment.

If you choose `None` and chooose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that represents an uncompressed ML model to deploy.

If you choose None and choose `S3Prefix` as the value of `S3DataType` , `S3Uri` identifies a key name prefix, under which all objects represents the uncompressed ML model to deploy.

If you choose None, then SageMaker will follow rules below when creating model data files under /opt/ml/model directory for use by your inference code:

- If you choose `S3Object` as the value of `S3DataType` , then SageMaker will split the key of the S3 object referenced by `S3Uri` by slash (/), and use the last part as the filename of the file holding the content of the S3 object.
- If you choose `S3Prefix` as the value of `S3DataType` , then for each S3 object under the key name pefix referenced by `S3Uri` , SageMaker will trim its key by the prefix, and use the remainder as the path (relative to `/opt/ml/model` ) of the file holding the content of the S3 object. SageMaker will split the remainder by slash (/), using intermediate parts as directory names and the last part as filename of the file holding the content of the S3 object.
- Do not use any of the following as file names or directory names:
- An empty or blank string
- A string which contains null bytes
- A string longer than 255 bytes
- A single dot (`.` )
- A double dot (`..` )
- Ambiguous file names will result in model deployment failure. For example, if your uncompressed ML model consists of two S3 objects `s3://mybucket/model/weights` and `s3://mybucket/model/weights/part1` and you specify `s3://mybucket/model/` as the value of `S3Uri` and `S3Prefix` as the value of `S3DataType` , then it will result in name clash between `/opt/ml/model/weights` (a regular file) and `/opt/ml/model/weights/` (a directory).
- Do not organize the model artifacts in [S3 console using folders](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html) . When you create a folder in S3 console, S3 creates a 0-byte object with a key set to the folder name you provide. They key of the 0-byte object ends with a slash (/) which violates SageMaker restrictions on model artifact file names, leading to model deployment failure.

ModelAccessConfig -> (structure)

Specifies the access configuration file for the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig` . You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

AcceptEula -> (boolean)

Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

HubAccessConfig -> (structure)

Configuration information for hub access.

HubContentArn -> (string)

The ARN of the hub content for which deployment access is allowed.

ManifestS3Uri -> (string)

The Amazon S3 URI of the manifest file. The manifest file is a CSV file that stores the artifact locations.

ETag -> (string)

The ETag associated with S3 URI.

ManifestEtag -> (string)

The ETag associated with Manifest S3 URI.

ProductId -> (string)

The Amazon Web Services Marketplace product ID of the model package.

Environment -> (map)

The environment variables to set in the Docker container. Each key and value in the `Environment` string to string map can have length of up to 1024. We support up to 16 entries in the map.

key -> (string)

value -> (string)

ModelInput -> (structure)

A structure with Model Input details.

DataInputConfig -> (string)

The input configuration object for the model.

Framework -> (string)

The machine learning framework of the model package container image.

FrameworkVersion -> (string)

The framework version of the Model Package Container Image.

NearestModelName -> (string)

The name of a pre-trained machine learning benchmarked by Amazon SageMaker Inference Recommender model that matches your model. You can find a list of benchmarked models by calling `ListModelMetadata` .

AdditionalS3DataSource -> (structure)

The additional data source that is used during inference in the Docker container for your model package.

S3DataType -> (string)

The data type of the additional data source that you specify for use in inference or training.

S3Uri -> (string)

The uniform resource identifier (URI) used to identify an additional data source used in inference or training.

CompressionType -> (string)

The type of compression used for an additional data source used in inference or training. Specify `None` if your additional data source is not compressed.

ETag -> (string)

The ETag associated with S3 URI.

ModelDataETag -> (string)

The ETag associated with Model Data URL.

SupportedTransformInstanceTypes -> (list)

A list of the instance types on which a transformation job can be run or on which an endpoint can be deployed.

(string)

SupportedRealtimeInferenceInstanceTypes -> (list)

A list of the instance types that are used to generate inferences in real-time.

(string)

SupportedContentTypes -> (list)

The supported MIME types for the input data.

(string)

SupportedResponseMIMETypes -> (list)

The supported MIME types for the output data.

(string)

JSON Syntax:

```
[
  {
    "Name": "string",
    "Description": "string",
    "Containers": [
      {
        "ContainerHostname": "string",
        "Image": "string",
        "ImageDigest": "string",
        "ModelDataUrl": "string",
        "ModelDataSource": {
          "S3DataSource": {
            "S3Uri": "string",
            "S3DataType": "S3Prefix"|"S3Object",
            "CompressionType": "None"|"Gzip",
            "ModelAccessConfig": {
              "AcceptEula": true|false
            },
            "HubAccessConfig": {
              "HubContentArn": "string"
            },
            "ManifestS3Uri": "string",
            "ETag": "string",
            "ManifestEtag": "string"
          }
        },
        "ProductId": "string",
        "Environment": {"string": "string"
          ...},
        "ModelInput": {
          "DataInputConfig": "string"
        },
        "Framework": "string",
        "FrameworkVersion": "string",
        "NearestModelName": "string",
        "AdditionalS3DataSource": {
          "S3DataType": "S3Object"|"S3Prefix",
          "S3Uri": "string",
          "CompressionType": "None"|"Gzip",
          "ETag": "string"
        },
        "ModelDataETag": "string"
      }
      ...
    ],
    "SupportedTransformInstanceTypes": ["ml.m4.xlarge"|"ml.m4.2xlarge"|"ml.m4.4xlarge"|"ml.m4.10xlarge"|"ml.m4.16xlarge"|"ml.c4.xlarge"|"ml.c4.2xlarge"|"ml.c4.4xlarge"|"ml.c4.8xlarge"|"ml.p2.xlarge"|"ml.p2.8xlarge"|"ml.p2.16xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.18xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.12xlarge"|"ml.m5.24xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.c6i.large"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.r6i.large"|"ml.r6i.xlarge"|"ml.r6i.2xlarge"|"ml.r6i.4xlarge"|"ml.r6i.8xlarge"|"ml.r6i.12xlarge"|"ml.r6i.16xlarge"|"ml.r6i.24xlarge"|"ml.r6i.32xlarge"|"ml.m7i.large"|"ml.m7i.xlarge"|"ml.m7i.2xlarge"|"ml.m7i.4xlarge"|"ml.m7i.8xlarge"|"ml.m7i.12xlarge"|"ml.m7i.16xlarge"|"ml.m7i.24xlarge"|"ml.m7i.48xlarge"|"ml.c7i.large"|"ml.c7i.xlarge"|"ml.c7i.2xlarge"|"ml.c7i.4xlarge"|"ml.c7i.8xlarge"|"ml.c7i.12xlarge"|"ml.c7i.16xlarge"|"ml.c7i.24xlarge"|"ml.c7i.48xlarge"|"ml.r7i.large"|"ml.r7i.xlarge"|"ml.r7i.2xlarge"|"ml.r7i.4xlarge"|"ml.r7i.8xlarge"|"ml.r7i.12xlarge"|"ml.r7i.16xlarge"|"ml.r7i.24xlarge"|"ml.r7i.48xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.12xlarge"|"ml.g5.16xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.inf2.xlarge"|"ml.inf2.8xlarge"|"ml.inf2.24xlarge"|"ml.inf2.48xlarge", ...],
    "SupportedRealtimeInferenceInstanceTypes": ["ml.t2.medium"|"ml.t2.large"|"ml.t2.xlarge"|"ml.t2.2xlarge"|"ml.m4.xlarge"|"ml.m4.2xlarge"|"ml.m4.4xlarge"|"ml.m4.10xlarge"|"ml.m4.16xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.12xlarge"|"ml.m5.24xlarge"|"ml.m5d.large"|"ml.m5d.xlarge"|"ml.m5d.2xlarge"|"ml.m5d.4xlarge"|"ml.m5d.12xlarge"|"ml.m5d.24xlarge"|"ml.c4.large"|"ml.c4.xlarge"|"ml.c4.2xlarge"|"ml.c4.4xlarge"|"ml.c4.8xlarge"|"ml.p2.xlarge"|"ml.p2.8xlarge"|"ml.p2.16xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.c5.large"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.18xlarge"|"ml.c5d.large"|"ml.c5d.xlarge"|"ml.c5d.2xlarge"|"ml.c5d.4xlarge"|"ml.c5d.9xlarge"|"ml.c5d.18xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.12xlarge"|"ml.r5.24xlarge"|"ml.r5d.large"|"ml.r5d.xlarge"|"ml.r5d.2xlarge"|"ml.r5d.4xlarge"|"ml.r5d.12xlarge"|"ml.r5d.24xlarge"|"ml.inf1.xlarge"|"ml.inf1.2xlarge"|"ml.inf1.6xlarge"|"ml.inf1.24xlarge"|"ml.dl1.24xlarge"|"ml.c6i.large"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.r6i.large"|"ml.r6i.xlarge"|"ml.r6i.2xlarge"|"ml.r6i.4xlarge"|"ml.r6i.8xlarge"|"ml.r6i.12xlarge"|"ml.r6i.16xlarge"|"ml.r6i.24xlarge"|"ml.r6i.32xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.12xlarge"|"ml.g5.16xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.12xlarge"|"ml.g6.16xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.r8g.medium"|"ml.r8g.large"|"ml.r8g.xlarge"|"ml.r8g.2xlarge"|"ml.r8g.4xlarge"|"ml.r8g.8xlarge"|"ml.r8g.12xlarge"|"ml.r8g.16xlarge"|"ml.r8g.24xlarge"|"ml.r8g.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.12xlarge"|"ml.g6e.16xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.p4d.24xlarge"|"ml.c7g.large"|"ml.c7g.xlarge"|"ml.c7g.2xlarge"|"ml.c7g.4xlarge"|"ml.c7g.8xlarge"|"ml.c7g.12xlarge"|"ml.c7g.16xlarge"|"ml.m6g.large"|"ml.m6g.xlarge"|"ml.m6g.2xlarge"|"ml.m6g.4xlarge"|"ml.m6g.8xlarge"|"ml.m6g.12xlarge"|"ml.m6g.16xlarge"|"ml.m6gd.large"|"ml.m6gd.xlarge"|"ml.m6gd.2xlarge"|"ml.m6gd.4xlarge"|"ml.m6gd.8xlarge"|"ml.m6gd.12xlarge"|"ml.m6gd.16xlarge"|"ml.c6g.large"|"ml.c6g.xlarge"|"ml.c6g.2xlarge"|"ml.c6g.4xlarge"|"ml.c6g.8xlarge"|"ml.c6g.12xlarge"|"ml.c6g.16xlarge"|"ml.c6gd.large"|"ml.c6gd.xlarge"|"ml.c6gd.2xlarge"|"ml.c6gd.4xlarge"|"ml.c6gd.8xlarge"|"ml.c6gd.12xlarge"|"ml.c6gd.16xlarge"|"ml.c6gn.large"|"ml.c6gn.xlarge"|"ml.c6gn.2xlarge"|"ml.c6gn.4xlarge"|"ml.c6gn.8xlarge"|"ml.c6gn.12xlarge"|"ml.c6gn.16xlarge"|"ml.r6g.large"|"ml.r6g.xlarge"|"ml.r6g.2xlarge"|"ml.r6g.4xlarge"|"ml.r6g.8xlarge"|"ml.r6g.12xlarge"|"ml.r6g.16xlarge"|"ml.r6gd.large"|"ml.r6gd.xlarge"|"ml.r6gd.2xlarge"|"ml.r6gd.4xlarge"|"ml.r6gd.8xlarge"|"ml.r6gd.12xlarge"|"ml.r6gd.16xlarge"|"ml.p4de.24xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.trn2.48xlarge"|"ml.inf2.xlarge"|"ml.inf2.8xlarge"|"ml.inf2.24xlarge"|"ml.inf2.48xlarge"|"ml.p5.48xlarge"|"ml.p5e.48xlarge"|"ml.p5en.48xlarge"|"ml.m7i.large"|"ml.m7i.xlarge"|"ml.m7i.2xlarge"|"ml.m7i.4xlarge"|"ml.m7i.8xlarge"|"ml.m7i.12xlarge"|"ml.m7i.16xlarge"|"ml.m7i.24xlarge"|"ml.m7i.48xlarge"|"ml.c7i.large"|"ml.c7i.xlarge"|"ml.c7i.2xlarge"|"ml.c7i.4xlarge"|"ml.c7i.8xlarge"|"ml.c7i.12xlarge"|"ml.c7i.16xlarge"|"ml.c7i.24xlarge"|"ml.c7i.48xlarge"|"ml.r7i.large"|"ml.r7i.xlarge"|"ml.r7i.2xlarge"|"ml.r7i.4xlarge"|"ml.r7i.8xlarge"|"ml.r7i.12xlarge"|"ml.r7i.16xlarge"|"ml.r7i.24xlarge"|"ml.r7i.48xlarge", ...],
    "SupportedContentTypes": ["string", ...],
    "SupportedResponseMIMETypes": ["string", ...]
  }
  ...
]
```

`--skip-model-validation` (string)

Indicates if you want to skip model validation.

Possible values:

- `All`
- `None`

`--source-uri` (string)

The URI of the source for the model package. If you want to clone a model package, set it to the model package Amazon Resource Name (ARN). If you want to register a model, set it to the model ARN.

`--security-config` (structure)

The KMS Key ID (`KMSKeyId` ) used for encryption of model package information.

KmsKeyId -> (string)

The KMS Key ID (`KMSKeyId` ) used for encryption of model package information.

Shorthand Syntax:

```
KmsKeyId=string
```

JSON Syntax:

```
{
  "KmsKeyId": "string"
}
```

`--model-card` (structure)

The model card associated with the model package. Since `ModelPackageModelCard` is tied to a model package, it is a specific usage of a model card and its schema is simplified compared to the schema of `ModelCard` . The `ModelPackageModelCard` schema does not include `model_package_details` , and `model_overview` is composed of the `model_creator` and `model_artifact` properties. For more information about the model package model card schema, see [Model package model card schema](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html#model-card-schema) . For more information about the model card associated with the model package, see [View the Details of a Model Version](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html) .

ModelCardContent -> (string)

The content of the model card. The content must follow the schema described in [Model Package Model Card Schema](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html#model-card-schema) .

ModelCardStatus -> (string)

The approval status of the model card within your organization. Different organizations might have different criteria for model card review and approval.

- `Draft` : The model card is a work in progress.
- `PendingReview` : The model card is pending review.
- `Approved` : The model card is approved.
- `Archived` : The model card is archived. No more updates can be made to the model card content. If you try to update the model card content, you will receive the message `Model Card is in Archived state` .

Shorthand Syntax:

```
ModelCardContent=string,ModelCardStatus=string
```

JSON Syntax:

```
{
  "ModelCardContent": "string",
  "ModelCardStatus": "Draft"|"PendingReview"|"Approved"|"Archived"
}
```

`--model-life-cycle` (structure)

A structure describing the current state of the model in its life cycle.

Stage -> (string)

The current stage in the model life cycle.

StageStatus -> (string)

The current status of a stage in model life cycle.

StageDescription -> (string)

Describes the stage related details.

Shorthand Syntax:

```
Stage=string,StageStatus=string,StageDescription=string
```

JSON Syntax:

```
{
  "Stage": "string",
  "StageStatus": "string",
  "StageDescription": "string"
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

ModelPackageArn -> (string)

The Amazon Resource Name (ARN) of the new model package.