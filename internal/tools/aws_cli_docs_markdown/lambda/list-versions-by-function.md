# list-versions-by-functionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-versions-by-function.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-versions-by-function.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lambda](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/index.html#cli-aws-lambda) ]

# list-versions-by-function

## Description

Returns a list of [versions](https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html) , with the version-specific configuration of each. Lambda returns up to 50 versions per call.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListVersionsByFunction)

`list-versions-by-function` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Versions`

## Synopsis

```
list-versions-by-function
--function-name <value>
[--max-items <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
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

`--function-name` (string)

The name or ARN of the Lambda function.

**Name formats**

- **Function name** - `MyFunction` .
- **Function ARN** - `arn:aws:lambda:us-west-2:123456789012:function:MyFunction` .
- **Partial ARN** - `123456789012:function:MyFunction` .

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To retrieve a list of versions of a function**

The following `list-versions-by-function` example displays the list of versions for the `my-function` Lambda function.

```
aws lambda list-versions-by-function \
    --function-name my-function
```

Output:

```
{
    "Versions": [
        {
            "TracingConfig": {
                "Mode": "PassThrough"
            },
            "Version": "$LATEST",
            "CodeSha256": "sU0cJ2/hOZevwV/lTxCuQqK3gDZP3i8gUoqUUVRmY6E=",
            "FunctionName": "my-function",
            "VpcConfig": {
                "SubnetIds": [],
                "VpcId": "",
                "SecurityGroupIds": []
            },
            "MemorySize": 256,
            "RevisionId": "93017fc9-59cb-41dc-901b-4845ce4bf668",
            "CodeSize": 266,
            "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function:$LATEST",
            "Handler": "index.handler",
            "Role": "arn:aws:iam::123456789012:role/service-role/helloWorldPython-role-uy3l9qyq",
            "Timeout": 3,
            "LastModified": "2019-10-01T16:47:28.490+0000",
            "Runtime": "nodejs10.x",
            "Description": ""
        },
        {
            "TracingConfig": {
                "Mode": "PassThrough"
            },
            "Version": "1",
            "CodeSha256": "5tT2qgzYUHoqwR616pZ2dpkn/0J1FrzJmlKidWaaCgk=",
            "FunctionName": "my-function",
            "VpcConfig": {
                "SubnetIds": [],
                "VpcId": "",
                "SecurityGroupIds": []
            },
            "MemorySize": 256,
            "RevisionId": "949c8914-012e-4795-998c-e467121951b1",
            "CodeSize": 304,
            "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function:1",
            "Handler": "index.handler",
            "Role": "arn:aws:iam::123456789012:role/service-role/helloWorldPython-role-uy3l9qyq",
            "Timeout": 3,
            "LastModified": "2019-09-26T20:28:40.438+0000",
            "Runtime": "nodejs10.x",
            "Description": "new version"
        },
        {
            "TracingConfig": {
                "Mode": "PassThrough"
            },
            "Version": "2",
            "CodeSha256": "sU0cJ2/hOZevwV/lTxCuQqK3gDZP3i8gUoqUUVRmY6E=",
            "FunctionName": "my-function",
            "VpcConfig": {
                "SubnetIds": [],
                "VpcId": "",
                "SecurityGroupIds": []
            },
            "MemorySize": 256,
            "RevisionId": "cd669f21-0f3d-4e1c-9566-948837f2e2ea",
            "CodeSize": 266,
            "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function:2",
            "Handler": "index.handler",
            "Role": "arn:aws:iam::123456789012:role/service-role/helloWorldPython-role-uy3l9qyq",
            "Timeout": 3,
            "LastModified": "2019-10-01T16:47:28.490+0000",
            "Runtime": "nodejs10.x",
            "Description": "newer version"
        }
    ]
}
```

For more information, see [Configuring AWS Lambda Function Aliases](https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html) in the *AWS Lambda Developer Guide*.

## Output

NextMarker -> (string)

The pagination token thatâs included if more results are available.

Versions -> (list)

A list of Lambda function versions.

(structure)

Details about a functionâs configuration.

FunctionName -> (string)

The name of the function.

FunctionArn -> (string)

The functionâs Amazon Resource Name (ARN).

Runtime -> (string)

The identifier of the functionâs [runtime](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html) . Runtime is required if the deployment package is a .zip file archive. Specifying a runtime results in an error if youâre deploying a function using a container image.

The following list includes deprecated runtimes. Lambda blocks creating new functions and updating existing functions shortly after each runtime is deprecated. For more information, see [Runtime use after deprecation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels) .

For a list of all currently supported runtimes, see [Supported runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported) .

Role -> (string)

The functionâs execution role.

Handler -> (string)

The function that Lambda calls to begin running your function.

CodeSize -> (long)

The size of the functionâs deployment package, in bytes.

Description -> (string)

The functionâs description.

Timeout -> (integer)

The amount of time in seconds that Lambda allows a function to run before stopping it.

MemorySize -> (integer)

The amount of memory available to the function at runtime.

LastModified -> (string)

The date and time that the function was last updated, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).

CodeSha256 -> (string)

The SHA256 hash of the functionâs deployment package.

Version -> (string)

The version of the Lambda function.

VpcConfig -> (structure)

The functionâs networking configuration.

SubnetIds -> (list)

A list of VPC subnet IDs.

(string)

SecurityGroupIds -> (list)

A list of VPC security group IDs.

(string)

VpcId -> (string)

The ID of the VPC.

Ipv6AllowedForDualStack -> (boolean)

Allows outbound IPv6 traffic on VPC functions that are connected to dual-stack subnets.

DeadLetterConfig -> (structure)

The functionâs dead letter queue.

TargetArn -> (string)

The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

Environment -> (structure)

The functionâs [environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html) . Omitted from CloudTrail logs.

Variables -> (map)

Environment variable key-value pairs. Omitted from CloudTrail logs.

key -> (string)

value -> (string)

Error -> (structure)

Error messages for environment variables that couldnât be applied.

ErrorCode -> (string)

The error code.

Message -> (string)

The error message.

KMSKeyArn -> (string)

The ARN of the Key Management Service (KMS) customer managed key thatâs used to encrypt the following resources:

- The functionâs [environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption) .
- The functionâs [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-security.html) snapshots.
- When used with `SourceKMSKeyArn` , the unzipped version of the .zip deployment package thatâs used for function invocations. For more information, see [Specifying a customer managed key for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/encrypt-zip-package.html#enable-zip-custom-encryption) .
- The optimized version of the container image thatâs used for function invocations. Note that this is not the same key thatâs used to protect your container image in the Amazon Elastic Container Registry (Amazon ECR). For more information, see [Function lifecycle](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-lifecycle) .

If you donât provide a customer managed key, Lambda uses an [Amazon Web Services owned key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) or an [Amazon Web Services managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk) .

TracingConfig -> (structure)

The functionâs X-Ray tracing configuration.

Mode -> (string)

The tracing mode.

MasterArn -> (string)

For [Lambda@Edge](mailto:Lambda%40Edge) functions, the ARN of the main function.

RevisionId -> (string)

The latest updated revision of the function or alias.

Layers -> (list)

The functionâs [layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) .

(structure)

An [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) .

Arn -> (string)

The Amazon Resource Name (ARN) of the function layer.

CodeSize -> (long)

The size of the layer archive in bytes.

SigningProfileVersionArn -> (string)

The Amazon Resource Name (ARN) for a signing profile version.

SigningJobArn -> (string)

The Amazon Resource Name (ARN) of a signing job.

State -> (string)

The current state of the function. When the state is `Inactive` , you can reactivate the function by invoking it.

StateReason -> (string)

The reason for the functionâs current state.

StateReasonCode -> (string)

The reason code for the functionâs current state. When the code is `Creating` , you canât invoke or modify the function.

LastUpdateStatus -> (string)

The status of the last update that was performed on the function. This is first set to `Successful` after function creation completes.

LastUpdateStatusReason -> (string)

The reason for the last update that was performed on the function.

LastUpdateStatusReasonCode -> (string)

The reason code for the last update that was performed on the function.

FileSystemConfigs -> (list)

Connection settings for an [Amazon EFS file system](https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html) .

(structure)

Details about the connection between a Lambda function and an [Amazon EFS file system](https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html) .

Arn -> (string)

The Amazon Resource Name (ARN) of the Amazon EFS access point that provides access to the file system.

LocalMountPath -> (string)

The path where the function can access the file system, starting with `/mnt/` .

PackageType -> (string)

The type of deployment package. Set to `Image` for container image and set `Zip` for .zip file archive.

ImageConfigResponse -> (structure)

The functionâs image configuration values.

ImageConfig -> (structure)

Configuration values that override the container image Dockerfile.

EntryPoint -> (list)

Specifies the entry point to their application, which is typically the location of the runtime executable.

(string)

Command -> (list)

Specifies parameters that you want to pass in with ENTRYPOINT.

(string)

WorkingDirectory -> (string)

Specifies the working directory.

Error -> (structure)

Error response to `GetFunctionConfiguration` .

ErrorCode -> (string)

Error code.

Message -> (string)

Error message.

SigningProfileVersionArn -> (string)

The ARN of the signing profile version.

SigningJobArn -> (string)

The ARN of the signing job.

Architectures -> (list)

The instruction set architecture that the function supports. Architecture is a string array with one of the valid values. The default architecture value is `x86_64` .

(string)

EphemeralStorage -> (structure)

The size of the functionâs `/tmp` directory in MB. The default value is 512, but can be any whole number between 512 and 10,240 MB. For more information, see [Configuring ephemeral storage (console)](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-ephemeral-storage) .

Size -> (integer)

The size of the functionâs `/tmp` directory.

SnapStart -> (structure)

Set `ApplyOn` to `PublishedVersions` to create a snapshot of the initialized execution environment when you publish a function version. For more information, see [Improving startup performance with Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) .

ApplyOn -> (string)

When set to `PublishedVersions` , Lambda creates a snapshot of the execution environment when you publish a function version.

OptimizationStatus -> (string)

When you provide a [qualified Amazon Resource Name (ARN)](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html#versioning-versions-using) , this response element indicates whether SnapStart is activated for the specified function version.

RuntimeVersionConfig -> (structure)

The ARN of the runtime and any errors that occured.

RuntimeVersionArn -> (string)

The ARN of the runtime version you want the function to use.

Error -> (structure)

Error response when Lambda is unable to retrieve the runtime version for a function.

ErrorCode -> (string)

The error code.

Message -> (string)

The error message.

LoggingConfig -> (structure)

The functionâs Amazon CloudWatch Logs configuration settings.

LogFormat -> (string)

The format in which Lambda sends your functionâs application and system logs to CloudWatch. Select between plain text and structured JSON.

ApplicationLogLevel -> (string)

Set this property to filter the application logs for your function that Lambda sends to CloudWatch. Lambda only sends application logs at the selected level of detail and lower, where `TRACE` is the highest level and `FATAL` is the lowest.

SystemLogLevel -> (string)

Set this property to filter the system logs for your function that Lambda sends to CloudWatch. Lambda only sends system logs at the selected level of detail and lower, where `DEBUG` is the highest level and `WARN` is the lowest.

LogGroup -> (string)

The name of the Amazon CloudWatch log group the function sends logs to. By default, Lambda functions send logs to a default log group named `/aws/lambda/<function name>` . To use a different log group, enter an existing log group or enter a new log group name.