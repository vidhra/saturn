# create-dev-endpointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-dev-endpoint.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-dev-endpoint.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# create-dev-endpoint

## Description

Creates a new development endpoint.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateDevEndpoint)

## Synopsis

```
create-dev-endpoint
--endpoint-name <value>
--role-arn <value>
[--security-group-ids <value>]
[--subnet-id <value>]
[--public-key <value>]
[--public-keys <value>]
[--number-of-nodes <value>]
[--worker-type <value>]
[--glue-version <value>]
[--number-of-workers <value>]
[--extra-python-libs-s3-path <value>]
[--extra-jars-s3-path <value>]
[--security-configuration <value>]
[--tags <value>]
[--arguments <value>]
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

`--endpoint-name` (string)

The name to be assigned to the new `DevEndpoint` .

`--role-arn` (string)

The IAM role for the `DevEndpoint` .

`--security-group-ids` (list)

Security group IDs for the security groups to be used by the new `DevEndpoint` .

(string)

Syntax:

```
"string" "string" ...
```

`--subnet-id` (string)

The subnet ID for the new `DevEndpoint` to use.

`--public-key` (string)

The public key to be used by this `DevEndpoint` for authentication. This attribute is provided for backward compatibility because the recommended attribute to use is public keys.

`--public-keys` (list)

A list of public keys to be used by the development endpoints for authentication. The use of this attribute is preferred over a single public key because the public keys allow you to have a different private key per client.

### Note

If you previously created an endpoint with a public key, you must remove that key to be able to set a list of public keys. Call the `UpdateDevEndpoint` API with the public key content in the `deletePublicKeys` attribute, and the list of new keys in the `addPublicKeys` attribute.

(string)

Syntax:

```
"string" "string" ...
```

`--number-of-nodes` (integer)

The number of Glue Data Processing Units (DPUs) to allocate to this `DevEndpoint` .

`--worker-type` (string)

The type of predefined worker that is allocated to the development endpoint. Accepts a value of Standard, G.1X, or G.2X.

- For the `Standard` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
- For the `G.1X` worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.
- For the `G.2X` worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.

Known issue: when a development endpoint is created with the `G.2X` `WorkerType` configuration, the Spark drivers for the development endpoint will run on 4 vCPU, 16 GB of memory, and a 64 GB disk.

Possible values:

- `Standard`
- `G.1X`
- `G.2X`
- `G.025X`
- `G.4X`
- `G.8X`
- `Z.2X`

`--glue-version` (string)

Glue version determines the versions of Apache Spark and Python that Glue supports. The Python version indicates the version supported for running your ETL scripts on development endpoints.

For more information about the available Glue versions and corresponding Spark and Python versions, see [Glue version](https://docs.aws.amazon.com/glue/latest/dg/add-job.html) in the developer guide.

Development endpoints that are created without specifying a Glue version default to Glue 0.9.

You can specify a version of Python support for development endpoints by using the `Arguments` parameter in the `CreateDevEndpoint` or `UpdateDevEndpoint` APIs. If no arguments are provided, the version defaults to Python 2.

`--number-of-workers` (integer)

The number of workers of a defined `workerType` that are allocated to the development endpoint.

The maximum number of workers you can define are 299 for `G.1X` , and 149 for `G.2X` .

`--extra-python-libs-s3-path` (string)

The paths to one or more Python libraries in an Amazon S3 bucket that should be loaded in your `DevEndpoint` . Multiple values must be complete paths separated by a comma.

### Note

You can only use pure Python libraries with a `DevEndpoint` . Libraries that rely on C extensions, such as the [pandas](http://pandas.pydata.org/) Python data analysis library, are not yet supported.

`--extra-jars-s3-path` (string)

The path to one or more Java `.jar` files in an S3 bucket that should be loaded in your `DevEndpoint` .

`--security-configuration` (string)

The name of the `SecurityConfiguration` structure to be used with this `DevEndpoint` .

`--tags` (map)

The tags to use with this DevEndpoint. You may use tags to limit access to the DevEndpoint. For more information about tags in Glue, see [Amazon Web Services Tags in Glue](https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html) in the developer guide.

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

`--arguments` (map)

A map of arguments used to configure the `DevEndpoint` .

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

EndpointName -> (string)

The name assigned to the new `DevEndpoint` .

Status -> (string)

The current status of the new `DevEndpoint` .

SecurityGroupIds -> (list)

The security groups assigned to the new `DevEndpoint` .

(string)

SubnetId -> (string)

The subnet ID assigned to the new `DevEndpoint` .

RoleArn -> (string)

The Amazon Resource Name (ARN) of the role assigned to the new `DevEndpoint` .

YarnEndpointAddress -> (string)

The address of the YARN endpoint used by this `DevEndpoint` .

ZeppelinRemoteSparkInterpreterPort -> (integer)

The Apache Zeppelin port for the remote Apache Spark interpreter.

NumberOfNodes -> (integer)

The number of Glue Data Processing Units (DPUs) allocated to this DevEndpoint.

WorkerType -> (string)

The type of predefined worker that is allocated to the development endpoint. May be a value of Standard, G.1X, or G.2X.

GlueVersion -> (string)

Glue version determines the versions of Apache Spark and Python that Glue supports. The Python version indicates the version supported for running your ETL scripts on development endpoints.

For more information about the available Glue versions and corresponding Spark and Python versions, see [Glue version](https://docs.aws.amazon.com/glue/latest/dg/add-job.html) in the developer guide.

NumberOfWorkers -> (integer)

The number of workers of a defined `workerType` that are allocated to the development endpoint.

AvailabilityZone -> (string)

The Amazon Web Services Availability Zone where this `DevEndpoint` is located.

VpcId -> (string)

The ID of the virtual private cloud (VPC) used by this `DevEndpoint` .

ExtraPythonLibsS3Path -> (string)

The paths to one or more Python libraries in an S3 bucket that will be loaded in your `DevEndpoint` .

ExtraJarsS3Path -> (string)

Path to one or more Java `.jar` files in an S3 bucket that will be loaded in your `DevEndpoint` .

FailureReason -> (string)

The reason for a current failure in this `DevEndpoint` .

SecurityConfiguration -> (string)

The name of the `SecurityConfiguration` structure being used with this `DevEndpoint` .

CreatedTimestamp -> (timestamp)

The point in time at which this `DevEndpoint` was created.

Arguments -> (map)

The map of arguments used to configure this `DevEndpoint` .

Valid arguments are:

- `"--enable-glue-datacatalog": ""`

You can specify a version of Python support for development endpoints by using the `Arguments` parameter in the `CreateDevEndpoint` or `UpdateDevEndpoint` APIs. If no arguments are provided, the version defaults to Python 2.

key -> (string)

value -> (string)