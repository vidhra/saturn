# create-pipelineÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/osis/create-pipeline.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/osis/create-pipeline.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [osis](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/osis/index.html#cli-aws-osis) ]

# create-pipeline

## Description

Creates an OpenSearch Ingestion pipeline. For more information, see [Creating Amazon OpenSearch Ingestion pipelines](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/creating-pipeline.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/osis-2022-01-01/CreatePipeline)

## Synopsis

```
create-pipeline
--pipeline-name <value>
--min-units <value>
--max-units <value>
--pipeline-configuration-body <value>
[--log-publishing-options <value>]
[--vpc-options <value>]
[--buffer-options <value>]
[--encryption-at-rest-options <value>]
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

`--pipeline-name` (string)

The name of the OpenSearch Ingestion pipeline to create. Pipeline names are unique across the pipelines owned by an account within an Amazon Web Services Region.

`--min-units` (integer)

The minimum pipeline capacity, in Ingestion Compute Units (ICUs).

`--max-units` (integer)

The maximum pipeline capacity, in Ingestion Compute Units (ICUs).

`--pipeline-configuration-body` (string)

The pipeline configuration in YAML format. The command accepts the pipeline configuration as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with `\n` .

`--log-publishing-options` (structure)

Key-value pairs to configure log publishing.

IsLoggingEnabled -> (boolean)

Whether logs should be published.

CloudWatchLogDestination -> (structure)

The destination for OpenSearch Ingestion logs sent to Amazon CloudWatch Logs. This parameter is required if `IsLoggingEnabled` is set to `true` .

LogGroup -> (string)

The name of the CloudWatch Logs group to send pipeline logs to. You can specify an existing log group or create a new one. For example, `/aws/vendedlogs/OpenSearchService/pipelines` .

Shorthand Syntax:

```
IsLoggingEnabled=boolean,CloudWatchLogDestination={LogGroup=string}
```

JSON Syntax:

```
{
  "IsLoggingEnabled": true|false,
  "CloudWatchLogDestination": {
    "LogGroup": "string"
  }
}
```

`--vpc-options` (structure)

Container for the values required to configure VPC access for the pipeline. If you donât specify these values, OpenSearch Ingestion creates the pipeline with a public endpoint.

SubnetIds -> (list)

A list of subnet IDs associated with the VPC endpoint.

(string)

SecurityGroupIds -> (list)

A list of security groups associated with the VPC endpoint.

(string)

VpcAttachmentOptions -> (structure)

Options for attaching a VPC to a pipeline.

AttachToVpc -> (boolean)

Whether a VPC is attached to the pipeline.

CidrBlock -> (string)

The CIDR block to be reserved for OpenSearch Ingestion to create elastic network interfaces (ENIs).

VpcEndpointManagement -> (string)

Defines whether you or Amazon OpenSearch Ingestion service create and manage the VPC endpoint configured for the pipeline.

Shorthand Syntax:

```
SubnetIds=string,string,SecurityGroupIds=string,string,VpcAttachmentOptions={AttachToVpc=boolean,CidrBlock=string},VpcEndpointManagement=string
```

JSON Syntax:

```
{
  "SubnetIds": ["string", ...],
  "SecurityGroupIds": ["string", ...],
  "VpcAttachmentOptions": {
    "AttachToVpc": true|false,
    "CidrBlock": "string"
  },
  "VpcEndpointManagement": "CUSTOMER"|"SERVICE"
}
```

`--buffer-options` (structure)

Key-value pairs to configure persistent buffering for the pipeline.

PersistentBufferEnabled -> (boolean)

Whether persistent buffering should be enabled.

Shorthand Syntax:

```
PersistentBufferEnabled=boolean
```

JSON Syntax:

```
{
  "PersistentBufferEnabled": true|false
}
```

`--encryption-at-rest-options` (structure)

Key-value pairs to configure encryption for data that is written to a persistent buffer.

KmsKeyArn -> (string)

The ARN of the KMS key used to encrypt buffer data. By default, data is encrypted using an Amazon Web Services owned key.

Shorthand Syntax:

```
KmsKeyArn=string
```

JSON Syntax:

```
{
  "KmsKeyArn": "string"
}
```

`--tags` (list)

List of tags to add to the pipeline upon creation.

(structure)

A tag (key-value pair) for an OpenSearch Ingestion pipeline.

Key -> (string)

The tag key. Tag keys must be unique for the pipeline to which they are attached.

Value -> (string)

The value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key value pair in a tag set of `project : Trinity` and `cost-center : Trinity`

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

## Output

Pipeline -> (structure)

Container for information about the created pipeline.

PipelineName -> (string)

The name of the pipeline.

PipelineArn -> (string)

The Amazon Resource Name (ARN) of the pipeline.

MinUnits -> (integer)

The minimum pipeline capacity, in Ingestion Compute Units (ICUs).

MaxUnits -> (integer)

The maximum pipeline capacity, in Ingestion Compute Units (ICUs).

Status -> (string)

The current status of the pipeline.

StatusReason -> (structure)

The reason for the current status of the pipeline.

Description -> (string)

A description of why a pipeline has a certain status.

PipelineConfigurationBody -> (string)

The Data Prepper pipeline configuration in YAML format.

CreatedAt -> (timestamp)

The date and time when the pipeline was created.

LastUpdatedAt -> (timestamp)

The date and time when the pipeline was last updated.

IngestEndpointUrls -> (list)

The ingestion endpoints for the pipeline, which you can send data to.

(string)

LogPublishingOptions -> (structure)

Key-value pairs that represent log publishing settings.

IsLoggingEnabled -> (boolean)

Whether logs should be published.

CloudWatchLogDestination -> (structure)

The destination for OpenSearch Ingestion logs sent to Amazon CloudWatch Logs. This parameter is required if `IsLoggingEnabled` is set to `true` .

LogGroup -> (string)

The name of the CloudWatch Logs group to send pipeline logs to. You can specify an existing log group or create a new one. For example, `/aws/vendedlogs/OpenSearchService/pipelines` .

VpcEndpoints -> (list)

The VPC interface endpoints that have access to the pipeline.

(structure)

An OpenSearch Ingestion-managed VPC endpoint that will access one or more pipelines.

VpcEndpointId -> (string)

The unique identifier of the endpoint.

VpcId -> (string)

The ID for your VPC. Amazon Web Services PrivateLink generates this value when you create a VPC.

VpcOptions -> (structure)

Information about the VPC, including associated subnets and security groups.

SubnetIds -> (list)

A list of subnet IDs associated with the VPC endpoint.

(string)

SecurityGroupIds -> (list)

A list of security groups associated with the VPC endpoint.

(string)

VpcAttachmentOptions -> (structure)

Options for attaching a VPC to a pipeline.

AttachToVpc -> (boolean)

Whether a VPC is attached to the pipeline.

CidrBlock -> (string)

The CIDR block to be reserved for OpenSearch Ingestion to create elastic network interfaces (ENIs).

VpcEndpointManagement -> (string)

Defines whether you or Amazon OpenSearch Ingestion service create and manage the VPC endpoint configured for the pipeline.

BufferOptions -> (structure)

Options that specify the configuration of a persistent buffer. To configure how OpenSearch Ingestion encrypts this data, set the `EncryptionAtRestOptions` . For more information, see [Persistent buffering](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/osis-features-overview.html#persistent-buffering) .

PersistentBufferEnabled -> (boolean)

Whether persistent buffering should be enabled.

EncryptionAtRestOptions -> (structure)

Options to control how OpenSearch encrypts buffer data.

KmsKeyArn -> (string)

The ARN of the KMS key used to encrypt buffer data. By default, data is encrypted using an Amazon Web Services owned key.

VpcEndpointService -> (string)

The VPC endpoint service name for the pipeline.

ServiceVpcEndpoints -> (list)

A list of VPC endpoints that OpenSearch Ingestion has created to other Amazon Web Services services.

(structure)

A container for information about VPC endpoints that were created to other services

ServiceName -> (string)

The name of the service for which a VPC endpoint was created.

VpcEndpointId -> (string)

The unique identifier of the VPC endpoint that was created.

Destinations -> (list)

Destinations to which the pipeline writes data.

(structure)

An object representing the destination of a pipeline.

ServiceName -> (string)

The name of the service receiving data from the pipeline.

Endpoint -> (string)

The endpoint receiving data from the pipeline.

Tags -> (list)

A list of tags associated with the given pipeline.

(structure)

A tag (key-value pair) for an OpenSearch Ingestion pipeline.

Key -> (string)

The tag key. Tag keys must be unique for the pipeline to which they are attached.

Value -> (string)

The value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key value pair in a tag set of `project : Trinity` and `cost-center : Trinity`