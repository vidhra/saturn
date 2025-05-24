# get-canaryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/get-canary.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/get-canary.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [synthetics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/index.html#cli-aws-synthetics) ]

# get-canary

## Description

Retrieves complete information about one canary. You must specify the name of the canary that you want. To get a list of canaries and their names, use [DescribeCanaries](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/synthetics-2017-10-11/GetCanary)

## Synopsis

```
get-canary
--name <value>
[--dry-run-id <value>]
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

`--name` (string)

The name of the canary that you want details for.

`--dry-run-id` (string)

The DryRunId associated with an existing canaryâs dry run. You can use this DryRunId to retrieve information about the dry run.

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

**To retrieve complete information about one canary**

The following `get-canary` example retrieves complete information about the canary named `demo_canary`.

```
aws synthetics get-canary \
    --name demo_canary
```

Output:

```
{
    "Canary": {
        "Id": "a1b2c3d4-5678-90ab-cdef-example11111",
        "Name": "demo_canary",
        "Code": {
            "SourceLocationArn": "arn:aws:lambda:us-east-1:123456789012:layer:cwsyn-demo_canary-a1b2c3d4-5678-90ab-cdef-example111118:1",
            "Handler": "pageLoadBlueprint.handler"
        },
        "ExecutionRoleArn": "arn:aws:iam::123456789012:role/demo_canary_role",
        "Schedule": {
            "Expression": "rate(10 minutes)",
            "DurationInSeconds": 0
        },
        "RunConfig": {
            "TimeoutInSeconds": 300,
            "MemoryInMB": 1000,
            "ActiveTracing": false
        },
        "SuccessRetentionPeriodInDays": 31,
        "FailureRetentionPeriodInDays": 31,
        "Status": {
            "State": "RUNNING"
        },
        "Timeline": {
            "Created": "2024-10-15T18:55:15.168000+05:30",
            "LastModified": "2024-10-15T18:55:40.540000+05:30",
            "LastStarted": "2024-10-15T18:55:40.540000+05:30"
        },
        "ArtifactS3Location": "cw-syn-results-123456789012-us-east-1/canary/us-east-1/demo_canary-a12-a123bc456789",
        "EngineArn": "arn:aws:lambda:us-east-1:123456789012:function:cwsyn-demo_canary-a1b2c3d4-5678-90ab-cdef-example111118:1",
        "RuntimeVersion": "syn-nodejs-puppeteer-9.1",
        "Tags": {
            "blueprint": "heartbeat"
        }
    }
}
```

For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) in the *Amazon CloudWatch User Guide*.

## Output

Canary -> (structure)

A structure that contains the full information about the canary.

Id -> (string)

The unique ID of this canary.

Name -> (string)

The name of the canary.

Code -> (structure)

This structure contains information about the canaryâs Lambda handler and where its code is stored by CloudWatch Synthetics.

SourceLocationArn -> (string)

The ARN of the Lambda layer where Synthetics stores the canary script code.

Handler -> (string)

The entry point to use for the source code when running the canary.

ExecutionRoleArn -> (string)

The ARN of the IAM role used to run the canary. This role must include `lambda.amazonaws.com` as a principal in the trust policy.

Schedule -> (structure)

A structure that contains information about how often the canary is to run, and when these runs are to stop.

Expression -> (string)

A `rate` expression or a `cron` expression that defines how often the canary is to run.

For a rate expression, The syntax is `rate(*number unit* )` . *unit* can be `minute` , `minutes` , or `hour` .

For example, `rate(1 minute)` runs the canary once a minute, `rate(10 minutes)` runs it once every 10 minutes, and `rate(1 hour)` runs it once every hour. You can specify a frequency between `rate(1 minute)` and `rate(1 hour)` .

Specifying `rate(0 minute)` or `rate(0 hour)` is a special value that causes the canary to run only once when it is started.

Use `cron(*expression* )` to specify a cron expression. For information about the syntax for cron expressions, see [Scheduling canary runs using cron](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_cron.html) .

DurationInSeconds -> (long)

How long, in seconds, for the canary to continue making regular runs after it was created. The runs are performed according to the schedule in the `Expression` value.

RetryConfig -> (structure)

A structure that contains the retry configuration for a canary

MaxRetries -> (integer)

The maximum number of retries. The value must be less than or equal to 2.

RunConfig -> (structure)

A structure that contains information about a canary run.

TimeoutInSeconds -> (integer)

How long the canary is allowed to run before it must stop.

MemoryInMB -> (integer)

The maximum amount of memory available to the canary while it is running, in MB. This value must be a multiple of 64.

ActiveTracing -> (boolean)

Displays whether this canary run used active X-Ray tracing.

SuccessRetentionPeriodInDays -> (integer)

The number of days to retain data about successful runs of this canary.

This setting affects the range of information returned by [GetCanaryRuns](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html) , as well as the range of information displayed in the Synthetics console.

FailureRetentionPeriodInDays -> (integer)

The number of days to retain data about failed runs of this canary.

This setting affects the range of information returned by [GetCanaryRuns](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html) , as well as the range of information displayed in the Synthetics console.

Status -> (structure)

A structure that contains information about the canaryâs status.

State -> (string)

The current state of the canary.

StateReason -> (string)

If the canary creation or update failed, this field provides details on the failure.

StateReasonCode -> (string)

If the canary creation or update failed, this field displays the reason code.

Timeline -> (structure)

A structure that contains information about when the canary was created, modified, and most recently run.

Created -> (timestamp)

The date and time the canary was created.

LastModified -> (timestamp)

The date and time the canary was most recently modified.

LastStarted -> (timestamp)

The date and time that the canaryâs most recent run started.

LastStopped -> (timestamp)

The date and time that the canaryâs most recent run ended.

ArtifactS3Location -> (string)

The location in Amazon S3 where Synthetics stores artifacts from the runs of this canary. Artifacts include the log file, screenshots, and HAR files.

EngineArn -> (string)

The ARN of the Lambda function that is used as your canaryâs engine. For more information about Lambda ARN format, see [Resources and Conditions for Lambda Actions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) .

RuntimeVersion -> (string)

Specifies the runtime version to use for the canary. For more information about runtime versions, see [Canary Runtime Versions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html) .

VpcConfig -> (structure)

If this canary is to test an endpoint in a VPC, this structure contains information about the subnets and security groups of the VPC endpoint. For more information, see [Running a Canary in a VPC](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html) .

VpcId -> (string)

The IDs of the VPC where this canary is to run.

SubnetIds -> (list)

The IDs of the subnets where this canary is to run.

(string)

SecurityGroupIds -> (list)

The IDs of the security groups for this canary.

(string)

Ipv6AllowedForDualStack -> (boolean)

Indicates whether this canary allows outbound IPv6 traffic if it is connected to dual-stack subnets.

VisualReference -> (structure)

If this canary performs visual monitoring by comparing screenshots, this structure contains the ID of the canary run to use as the baseline for screenshots, and the coordinates of any parts of the screen to ignore during the visual monitoring comparison.

BaseScreenshots -> (list)

An array of screenshots that are used as the baseline for comparisons during visual monitoring.

(structure)

A structure representing a screenshot that is used as a baseline during visual monitoring comparisons made by the canary.

ScreenshotName -> (string)

The name of the screenshot. This is generated the first time the canary is run after the `UpdateCanary` operation that specified for this canary to perform visual monitoring.

IgnoreCoordinates -> (list)

Coordinates that define the part of a screen to ignore during screenshot comparisons. To obtain the coordinates to use here, use the CloudWatch console to draw the boundaries on the screen. For more information, see [Editing or deleting a canary](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/synthetics_canaries_deletion.html)

(string)

BaseCanaryRunId -> (string)

The ID of the canary run that produced the baseline screenshots that are used for visual monitoring comparisons by this canary.

ProvisionedResourceCleanup -> (string)

Specifies whether to also delete the Lambda functions and layers used by this canary when the canary is deleted. If it is `AUTOMATIC` , the Lambda functions and layers will be deleted when the canary is deleted.

If the value of this parameter is `OFF` , then the value of the `DeleteLambda` parameter of the [DeleteCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteCanary.html) operation determines whether the Lambda functions and layers will be deleted.

Tags -> (map)

The list of key-value pairs that are associated with the canary.

key -> (string)

value -> (string)

ArtifactConfig -> (structure)

A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.

S3Encryption -> (structure)

A structure that contains the configuration of encryption settings for canary artifacts that are stored in Amazon S3.

EncryptionMode -> (string)

The encryption method to use for artifacts created by this canary. Specify `SSE_S3` to use server-side encryption (SSE) with an Amazon S3-managed key. Specify `SSE-KMS` to use server-side encryption with a customer-managed KMS key.

If you omit this parameter, an Amazon Web Services-managed KMS key is used.

KmsKeyArn -> (string)

The ARN of the customer-managed KMS key to use, if you specify `SSE-KMS` for `EncryptionMode`

DryRunConfig -> (structure)

Returns the dry run configurations for a canary.

DryRunId -> (string)

The DryRunId associated with an existing canaryâs dry run. You can use this DryRunId to retrieve information about the dry run.

LastDryRunExecutionStatus -> (string)

Returns the last execution status for a canaryâs dry run.