# create-processing-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-processing-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-processing-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-processing-job

## Description

Creates a processing job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateProcessingJob)

## Synopsis

```
create-processing-job
[--processing-inputs <value>]
[--processing-output-config <value>]
--processing-job-name <value>
--processing-resources <value>
[--stopping-condition <value>]
--app-specification <value>
[--environment <value>]
[--network-config <value>]
--role-arn <value>
[--tags <value>]
[--experiment-config <value>]
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

`--processing-inputs` (list)

An array of inputs configuring the data to download into the processing container.

(structure)

The inputs for a processing job. The processing input must specify exactly one of either `S3Input` or `DatasetDefinition` types.

InputName -> (string)

The name for the processing job input.

AppManaged -> (boolean)

When `True` , input operations such as data download are managed natively by the processing job application. When `False` (default), input operations are managed by Amazon SageMaker.

S3Input -> (structure)

Configuration for downloading input data from Amazon S3 into the processing container.

S3Uri -> (string)

The URI of the Amazon S3 prefix Amazon SageMaker downloads data required to run a processing job.

LocalPath -> (string)

The local path in your container where you want Amazon SageMaker to write input data to. `LocalPath` is an absolute path to the input data and must begin with `/opt/ml/processing/` . `LocalPath` is a required parameter when `AppManaged` is `False` (default).

S3DataType -> (string)

Whether you use an `S3Prefix` or a `ManifestFile` for the data type. If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for the processing job. If you choose `ManifestFile` , `S3Uri` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for the processing job.

S3InputMode -> (string)

Whether to use `File` or `Pipe` input mode. In File mode, Amazon SageMaker copies the data from the input source onto the local ML storage volume before starting your processing container. This is the most commonly used input mode. In `Pipe` mode, Amazon SageMaker streams input data from the source directly to your processing container into named pipes without using the ML storage volume.

S3DataDistributionType -> (string)

Whether to distribute the data from Amazon S3 to all processing instances with `FullyReplicated` , or whether the data from Amazon S3 is shared by Amazon S3 key, downloading one shard of data to each processing instance.

S3CompressionType -> (string)

Whether to GZIP-decompress the data in Amazon S3 as it is streamed into the processing container. `Gzip` can only be used when `Pipe` mode is specified as the `S3InputMode` . In `Pipe` mode, Amazon SageMaker streams input data from the source directly to your container without using the EBS volume.

DatasetDefinition -> (structure)

Configuration for a Dataset Definition input.

AthenaDatasetDefinition -> (structure)

Configuration for Athena Dataset Definition input.

Catalog -> (string)

The name of the data catalog used in Athena query execution.

Database -> (string)

The name of the database used in the Athena query execution.

QueryString -> (string)

The SQL query statements, to be executed.

WorkGroup -> (string)

The name of the workgroup in which the Athena query is being started.

OutputS3Uri -> (string)

The location in Amazon S3 where Athena query results are stored.

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt data generated from an Athena query execution.

OutputFormat -> (string)

The data storage format for Athena query results.

OutputCompression -> (string)

The compression used for Athena query results.

RedshiftDatasetDefinition -> (structure)

Configuration for Redshift Dataset Definition input.

ClusterId -> (string)

The Redshift cluster Identifier.

Database -> (string)

The name of the Redshift database used in Redshift query execution.

DbUser -> (string)

The database user name used in Redshift query execution.

QueryString -> (string)

The SQL query statements to be executed.

ClusterRoleArn -> (string)

The IAM role attached to your Redshift cluster that Amazon SageMaker uses to generate datasets.

OutputS3Uri -> (string)

The location in Amazon S3 where the Redshift query results are stored.

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt data from a Redshift execution.

OutputFormat -> (string)

The data storage format for Redshift query results.

OutputCompression -> (string)

The compression used for Redshift query results.

LocalPath -> (string)

The local path where you want Amazon SageMaker to download the Dataset Definition inputs to run a processing job. `LocalPath` is an absolute path to the input data. This is a required parameter when `AppManaged` is `False` (default).

DataDistributionType -> (string)

Whether the generated dataset is `FullyReplicated` or `ShardedByS3Key` (default).

InputMode -> (string)

Whether to use `File` or `Pipe` input mode. In `File` (default) mode, Amazon SageMaker copies the data from the input source onto the local Amazon Elastic Block Store (Amazon EBS) volumes before starting your training algorithm. This is the most commonly used input mode. In `Pipe` mode, Amazon SageMaker streams input data from the source directly to your algorithm without using the EBS volume.

Shorthand Syntax:

```
InputName=string,AppManaged=boolean,S3Input={S3Uri=string,LocalPath=string,S3DataType=string,S3InputMode=string,S3DataDistributionType=string,S3CompressionType=string},DatasetDefinition={AthenaDatasetDefinition={Catalog=string,Database=string,QueryString=string,WorkGroup=string,OutputS3Uri=string,KmsKeyId=string,OutputFormat=string,OutputCompression=string},RedshiftDatasetDefinition={ClusterId=string,Database=string,DbUser=string,QueryString=string,ClusterRoleArn=string,OutputS3Uri=string,KmsKeyId=string,OutputFormat=string,OutputCompression=string},LocalPath=string,DataDistributionType=string,InputMode=string} ...
```

JSON Syntax:

```
[
  {
    "InputName": "string",
    "AppManaged": true|false,
    "S3Input": {
      "S3Uri": "string",
      "LocalPath": "string",
      "S3DataType": "ManifestFile"|"S3Prefix",
      "S3InputMode": "Pipe"|"File",
      "S3DataDistributionType": "FullyReplicated"|"ShardedByS3Key",
      "S3CompressionType": "None"|"Gzip"
    },
    "DatasetDefinition": {
      "AthenaDatasetDefinition": {
        "Catalog": "string",
        "Database": "string",
        "QueryString": "string",
        "WorkGroup": "string",
        "OutputS3Uri": "string",
        "KmsKeyId": "string",
        "OutputFormat": "PARQUET"|"ORC"|"AVRO"|"JSON"|"TEXTFILE",
        "OutputCompression": "GZIP"|"SNAPPY"|"ZLIB"
      },
      "RedshiftDatasetDefinition": {
        "ClusterId": "string",
        "Database": "string",
        "DbUser": "string",
        "QueryString": "string",
        "ClusterRoleArn": "string",
        "OutputS3Uri": "string",
        "KmsKeyId": "string",
        "OutputFormat": "PARQUET"|"CSV",
        "OutputCompression": "None"|"GZIP"|"BZIP2"|"ZSTD"|"SNAPPY"
      },
      "LocalPath": "string",
      "DataDistributionType": "FullyReplicated"|"ShardedByS3Key",
      "InputMode": "Pipe"|"File"
    }
  }
  ...
]
```

`--processing-output-config` (structure)

Output configuration for the processing job.

Outputs -> (list)

An array of outputs configuring the data to upload from the processing container.

(structure)

Describes the results of a processing job. The processing output must specify exactly one of either `S3Output` or `FeatureStoreOutput` types.

OutputName -> (string)

The name for the processing job output.

S3Output -> (structure)

Configuration for processing job outputs in Amazon S3.

S3Uri -> (string)

A URI that identifies the Amazon S3 bucket where you want Amazon SageMaker to save the results of a processing job.

LocalPath -> (string)

The local path of a directory where you want Amazon SageMaker to upload its contents to Amazon S3. `LocalPath` is an absolute path to a directory containing output files. This directory will be created by the platform and exist when your containerâs entrypoint is invoked.

S3UploadMode -> (string)

Whether to upload the results of the processing job continuously or after the job completes.

FeatureStoreOutput -> (structure)

Configuration for processing job outputs in Amazon SageMaker Feature Store. This processing output type is only supported when `AppManaged` is specified.

FeatureGroupName -> (string)

The name of the Amazon SageMaker FeatureGroup to use as the destination for processing job output. Note that your processing script is responsible for putting records into your Feature Store.

AppManaged -> (boolean)

When `True` , output operations such as data upload are managed natively by the processing job application. When `False` (default), output operations are managed by Amazon SageMaker.

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt the processing job output. `KmsKeyId` can be an ID of a KMS key, ARN of a KMS key, or alias of a KMS key. The `KmsKeyId` is applied to all outputs.

JSON Syntax:

```
{
  "Outputs": [
    {
      "OutputName": "string",
      "S3Output": {
        "S3Uri": "string",
        "LocalPath": "string",
        "S3UploadMode": "Continuous"|"EndOfJob"
      },
      "FeatureStoreOutput": {
        "FeatureGroupName": "string"
      },
      "AppManaged": true|false
    }
    ...
  ],
  "KmsKeyId": "string"
}
```

`--processing-job-name` (string)

The name of the processing job. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account.

`--processing-resources` (structure)

Identifies the resources, ML compute instances, and ML storage volumes to deploy for a processing job. In distributed training, you specify more than one instance.

ClusterConfig -> (structure)

The configuration for the resources in a cluster used to run the processing job.

InstanceCount -> (integer)

The number of ML compute instances to use in the processing job. For distributed processing jobs, specify a value greater than 1. The default value is 1.

InstanceType -> (string)

The ML compute instance type for the processing job.

VolumeSizeInGB -> (integer)

The size of the ML storage volume in gigabytes that you want to provision. You must specify sufficient ML storage for your scenario.

### Note

Certain Nitro-based instances include local storage with a fixed total size, dependent on the instance type. When using these instances for processing, Amazon SageMaker mounts the local instance storage instead of Amazon EBS gp2 storage. You canât request a `VolumeSizeInGB` greater than the total size of the local instance storage.

For a list of instance types that support local instance storage, including the total size per instance type, see [Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes) .

VolumeKmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the processing job.

### Note

Certain Nitro-based instances include local storage, dependent on the instance type. Local storage volumes are encrypted using a hardware module on the instance. You canât request a `VolumeKmsKeyId` when using an instance type with local storage.

For a list of instance types that support local instance storage, see [Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes) .

For more information about local instance storage encryption, see [SSD Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html) .

Shorthand Syntax:

```
ClusterConfig={InstanceCount=integer,InstanceType=string,VolumeSizeInGB=integer,VolumeKmsKeyId=string}
```

JSON Syntax:

```
{
  "ClusterConfig": {
    "InstanceCount": integer,
    "InstanceType": "ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.m4.xlarge"|"ml.m4.2xlarge"|"ml.m4.4xlarge"|"ml.m4.10xlarge"|"ml.m4.16xlarge"|"ml.c4.xlarge"|"ml.c4.2xlarge"|"ml.c4.4xlarge"|"ml.c4.8xlarge"|"ml.p2.xlarge"|"ml.p2.8xlarge"|"ml.p2.16xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.18xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.12xlarge"|"ml.m5.24xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.8xlarge"|"ml.r5.12xlarge"|"ml.r5.16xlarge"|"ml.r5.24xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.16xlarge"|"ml.g5.12xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.r5d.large"|"ml.r5d.xlarge"|"ml.r5d.2xlarge"|"ml.r5d.4xlarge"|"ml.r5d.8xlarge"|"ml.r5d.12xlarge"|"ml.r5d.16xlarge"|"ml.r5d.24xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.12xlarge"|"ml.g6.16xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.12xlarge"|"ml.g6e.16xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge",
    "VolumeSizeInGB": integer,
    "VolumeKmsKeyId": "string"
  }
}
```

`--stopping-condition` (structure)

The time limit for how long the processing job is allowed to run.

MaxRuntimeInSeconds -> (integer)

Specifies the maximum runtime in seconds.

Shorthand Syntax:

```
MaxRuntimeInSeconds=integer
```

JSON Syntax:

```
{
  "MaxRuntimeInSeconds": integer
}
```

`--app-specification` (structure)

Configures the processing job to run a specified Docker container image.

ImageUri -> (string)

The container image to be run by the processing job.

ContainerEntrypoint -> (list)

The entrypoint for a container used to run a processing job.

(string)

ContainerArguments -> (list)

The arguments for a container used to run a processing job.

(string)

Shorthand Syntax:

```
ImageUri=string,ContainerEntrypoint=string,string,ContainerArguments=string,string
```

JSON Syntax:

```
{
  "ImageUri": "string",
  "ContainerEntrypoint": ["string", ...],
  "ContainerArguments": ["string", ...]
}
```

`--environment` (map)

The environment variables to set in the Docker container. Up to 100 key and values entries in the map are supported.

### Warning

Do not include any security-sensitive information including account access IDs, secrets, or tokens in any environment fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request environment variable or plain text fields.

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

`--network-config` (structure)

Networking options for a processing job, such as whether to allow inbound and outbound network calls to and from processing containers, and the VPC subnets and security groups to use for VPC-enabled processing jobs.

EnableInterContainerTrafficEncryption -> (boolean)

Whether to encrypt all communications between distributed processing jobs. Choose `True` to encrypt communications. Encryption provides greater security for distributed processing jobs, but the processing might take longer.

EnableNetworkIsolation -> (boolean)

Whether to allow inbound and outbound network calls to and from the containers used for the processing job.

VpcConfig -> (structure)

Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html) .

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html) .

(string)

Shorthand Syntax:

```
EnableInterContainerTrafficEncryption=boolean,EnableNetworkIsolation=boolean,VpcConfig={SecurityGroupIds=[string,string],Subnets=[string,string]}
```

JSON Syntax:

```
{
  "EnableInterContainerTrafficEncryption": true|false,
  "EnableNetworkIsolation": true|false,
  "VpcConfig": {
    "SecurityGroupIds": ["string", ...],
    "Subnets": ["string", ...]
  }
}
```

`--role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.

`--tags` (list)

(Optional) An array of key-value pairs. For more information, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-whatURL) in the *Amazon Web Services Billing and Cost Management User Guide* .

### Warning

Do not include any security-sensitive information including account access IDs, secrets, or tokens in any tags. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request tag variable or plain text fields.

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

`--experiment-config` (structure)

Associates a SageMaker job as a trial component with an experiment and trial. Specified when you call the following APIs:

- [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
- [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)
- [CreateTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html)

ExperimentName -> (string)

The name of an existing experiment to associate with the trial component.

TrialName -> (string)

The name of an existing trial to associate the trial component with. If not specified, a new trial is created.

TrialComponentDisplayName -> (string)

The display name for the trial component. If this key isnât specified, the display name is the trial component name.

RunName -> (string)

The name of the experiment run to associate with the trial component.

Shorthand Syntax:

```
ExperimentName=string,TrialName=string,TrialComponentDisplayName=string,RunName=string
```

JSON Syntax:

```
{
  "ExperimentName": "string",
  "TrialName": "string",
  "TrialComponentDisplayName": "string",
  "RunName": "string"
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

ProcessingJobArn -> (string)

The Amazon Resource Name (ARN) of the processing job.