# describe-processing-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-processing-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-processing-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# describe-processing-job

## Description

Returns a description of a processing job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeProcessingJob)

## Synopsis

```
describe-processing-job
--processing-job-name <value>
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

`--processing-job-name` (string)

The name of the processing job. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account.

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

ProcessingInputs -> (list)

The inputs for a processing job.

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

ProcessingOutputConfig -> (structure)

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

ProcessingJobName -> (string)

The name of the processing job. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account.

ProcessingResources -> (structure)

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

StoppingCondition -> (structure)

The time limit for how long the processing job is allowed to run.

MaxRuntimeInSeconds -> (integer)

Specifies the maximum runtime in seconds.

AppSpecification -> (structure)

Configures the processing job to run a specified container image.

ImageUri -> (string)

The container image to be run by the processing job.

ContainerEntrypoint -> (list)

The entrypoint for a container used to run a processing job.

(string)

ContainerArguments -> (list)

The arguments for a container used to run a processing job.

(string)

Environment -> (map)

The environment variables set in the Docker container.

key -> (string)

value -> (string)

NetworkConfig -> (structure)

Networking options for a processing job.

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

RoleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.

ExperimentConfig -> (structure)

The configuration information used to create an experiment.

ExperimentName -> (string)

The name of an existing experiment to associate with the trial component.

TrialName -> (string)

The name of an existing trial to associate the trial component with. If not specified, a new trial is created.

TrialComponentDisplayName -> (string)

The display name for the trial component. If this key isnât specified, the display name is the trial component name.

RunName -> (string)

The name of the experiment run to associate with the trial component.

ProcessingJobArn -> (string)

The Amazon Resource Name (ARN) of the processing job.

ProcessingJobStatus -> (string)

Provides the status of a processing job.

ExitMessage -> (string)

An optional string, up to one KB in size, that contains metadata from the processing container when the processing job exits.

FailureReason -> (string)

A string, up to one KB in size, that contains the reason a processing job failed, if it failed.

ProcessingEndTime -> (timestamp)

The time at which the processing job completed.

ProcessingStartTime -> (timestamp)

The time at which the processing job started.

LastModifiedTime -> (timestamp)

The time at which the processing job was last modified.

CreationTime -> (timestamp)

The time at which the processing job was created.

MonitoringScheduleArn -> (string)

The ARN of a monitoring schedule for an endpoint associated with this processing job.

AutoMLJobArn -> (string)

The ARN of an AutoML job associated with this processing job.

TrainingJobArn -> (string)

The ARN of a training job associated with this processing job.