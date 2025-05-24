# create-canaryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/create-canary.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/create-canary.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [synthetics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/index.html#cli-aws-synthetics) ]

# create-canary

## Description

Creates a canary. Canaries are scripts that monitor your endpoints and APIs from the outside-in. Canaries help you check the availability and latency of your web services and troubleshoot anomalies by investigating load time data, screenshots of the UI, logs, and metrics. You can set up a canary to run continuously or just once.

Do not use `CreateCanary` to modify an existing canary. Use [UpdateCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_UpdateCanary.html) instead.

To create canaries, you must have the `CloudWatchSyntheticsFullAccess` policy. If you are creating a new IAM role for the canary, you also need the `iam:CreateRole` , `iam:CreatePolicy` and `iam:AttachRolePolicy` permissions. For more information, see [Necessary Roles and Permissions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Roles) .

Do not include secrets or proprietary information in your canary names. The canary name makes up part of the Amazon Resource Name (ARN) for the canary, and the ARN is included in outbound calls over the internet. For more information, see [Security Considerations for Synthetics Canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/synthetics-2017-10-11/CreateCanary)

## Synopsis

```
create-canary
--name <value>
--code <value>
--artifact-s3-location <value>
--execution-role-arn <value>
--schedule <value>
[--run-config <value>]
[--success-retention-period-in-days <value>]
[--failure-retention-period-in-days <value>]
--runtime-version <value>
[--vpc-config <value>]
[--resources-to-replicate-tags <value>]
[--provisioned-resource-cleanup <value>]
[--tags <value>]
[--artifact-config <value>]
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

The name for this canary. Be sure to give it a descriptive name that distinguishes it from other canaries in your account.

Do not include secrets or proprietary information in your canary names. The canary name makes up part of the canary ARN, and the ARN is included in outbound calls over the internet. For more information, see [Security Considerations for Synthetics Canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html) .

`--code` (structure)

A structure that includes the entry point from which the canary should start running your script. If the script is stored in an S3 bucket, the bucket name, key, and version are also included.

S3Bucket -> (string)

If your canary script is located in S3, specify the bucket name here. Do not include `s3://` as the start of the bucket name.

S3Key -> (string)

The S3 key of your script. For more information, see [Working with Amazon S3 Objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingObjects.html) .

S3Version -> (string)

The S3 version ID of your script.

ZipFile -> (blob)

If you input your canary script directly into the canary instead of referring to an S3 location, the value of this parameter is the base64-encoded contents of the .zip file that contains the script. It must be smaller than 225 Kb.

For large canary scripts, we recommend that you use an S3 location instead of inputting it directly with this parameter.

Handler -> (string)

The entry point to use for the source code when running the canary. For canaries that use the `syn-python-selenium-1.0` runtime or a `syn-nodejs.puppeteer` runtime earlier than `syn-nodejs.puppeteer-3.4` , the handler must be specified as `` *fileName* .handler`` . For `syn-python-selenium-1.1` , `syn-nodejs.puppeteer-3.4` , and later runtimes, the handler can be specified as `` *fileName* .*functionName* `` , or you can specify a folder where canary scripts reside as `` *folder* /*fileName* .*functionName* `` .

Shorthand Syntax:

```
S3Bucket=string,S3Key=string,S3Version=string,ZipFile=blob,Handler=string
```

JSON Syntax:

```
{
  "S3Bucket": "string",
  "S3Key": "string",
  "S3Version": "string",
  "ZipFile": blob,
  "Handler": "string"
}
```

`--artifact-s3-location` (string)

The location in Amazon S3 where Synthetics stores artifacts from the test runs of this canary. Artifacts include the log file, screenshots, and HAR files. The name of the S3 bucket canât include a period (.).

`--execution-role-arn` (string)

The ARN of the IAM role to be used to run the canary. This role must already exist, and must include `lambda.amazonaws.com` as a principal in the trust policy. The role must also have the following permissions:

- `s3:PutObject`
- `s3:GetBucketLocation`
- `s3:ListAllMyBuckets`
- `cloudwatch:PutMetricData`
- `logs:CreateLogGroup`
- `logs:CreateLogStream`
- `logs:PutLogEvents`

`--schedule` (structure)

A structure that contains information about how often the canary is to run and when these test runs are to stop.

Expression -> (string)

A `rate` expression or a `cron` expression that defines how often the canary is to run.

For a rate expression, The syntax is `rate(*number unit* )` . *unit* can be `minute` , `minutes` , or `hour` .

For example, `rate(1 minute)` runs the canary once a minute, `rate(10 minutes)` runs it once every 10 minutes, and `rate(1 hour)` runs it once every hour. You can specify a frequency between `rate(1 minute)` and `rate(1 hour)` .

Specifying `rate(0 minute)` or `rate(0 hour)` is a special value that causes the canary to run only once when it is started.

Use `cron(*expression* )` to specify a cron expression. You canât schedule a canary to wait for more than a year before running. For information about the syntax for cron expressions, see [Scheduling canary runs using cron](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_cron.html) .

DurationInSeconds -> (long)

How long, in seconds, for the canary to continue making regular runs according to the schedule in the `Expression` value. If you specify 0, the canary continues making runs until you stop it. If you omit this field, the default of 0 is used.

RetryConfig -> (structure)

A structure that contains the retry configuration for a canary

MaxRetries -> (integer)

The maximum number of retries. The value must be less than or equal to 2.

Shorthand Syntax:

```
Expression=string,DurationInSeconds=long,RetryConfig={MaxRetries=integer}
```

JSON Syntax:

```
{
  "Expression": "string",
  "DurationInSeconds": long,
  "RetryConfig": {
    "MaxRetries": integer
  }
}
```

`--run-config` (structure)

A structure that contains the configuration for individual canary runs, such as timeout value and environment variables.

### Warning

Environment variable keys and values are encrypted at rest using Amazon Web Services owned KMS keys. However, the environment variables are not encrypted on the client side. Do not store sensitive information in them.

TimeoutInSeconds -> (integer)

How long the canary is allowed to run before it must stop. You canât set this time to be longer than the frequency of the runs of this canary.

If you omit this field, the frequency of the canary is used as this value, up to a maximum of 14 minutes.

MemoryInMB -> (integer)

The maximum amount of memory available to the canary while it is running, in MB. This value must be a multiple of 64.

ActiveTracing -> (boolean)

Specifies whether this canary is to use active X-Ray tracing when it runs. Active tracing enables this canary run to be displayed in the ServiceLens and X-Ray service maps even if the canary does not hit an endpoint that has X-Ray tracing enabled. Using X-Ray tracing incurs charges. For more information, see [Canaries and X-Ray tracing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_tracing.html) .

You can enable active tracing only for canaries that use version `syn-nodejs-2.0` or later for their canary runtime.

EnvironmentVariables -> (map)

Specifies the keys and values to use for any environment variables used in the canary script. Use the following format:

{ âkey1â : âvalue1â, âkey2â : âvalue2â, â¦}

Keys must start with a letter and be at least two characters. The total size of your environment variables cannot exceed 4 KB. You canât specify any Lambda reserved environment variables as the keys for your environment variables. For more information about reserved keys, see [Runtime environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-runtime) .

### Warning

Environment variable keys and values are encrypted at rest using Amazon Web Services owned KMS keys. However, the environment variables are not encrypted on the client side. Do not store sensitive information in them.

key -> (string)

value -> (string)

Shorthand Syntax:

```
TimeoutInSeconds=integer,MemoryInMB=integer,ActiveTracing=boolean,EnvironmentVariables={KeyName1=string,KeyName2=string}
```

JSON Syntax:

```
{
  "TimeoutInSeconds": integer,
  "MemoryInMB": integer,
  "ActiveTracing": true|false,
  "EnvironmentVariables": {"string": "string"
    ...}
}
```

`--success-retention-period-in-days` (integer)

The number of days to retain data about successful runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.

This setting affects the range of information returned by [GetCanaryRuns](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html) , as well as the range of information displayed in the Synthetics console.

`--failure-retention-period-in-days` (integer)

The number of days to retain data about failed runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.

This setting affects the range of information returned by [GetCanaryRuns](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html) , as well as the range of information displayed in the Synthetics console.

`--runtime-version` (string)

Specifies the runtime version to use for the canary. For a list of valid runtime versions and more information about runtime versions, see [Canary Runtime Versions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html) .

`--vpc-config` (structure)

If this canary is to test an endpoint in a VPC, this structure contains information about the subnet and security groups of the VPC endpoint. For more information, see [Running a Canary in a VPC](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html) .

SubnetIds -> (list)

The IDs of the subnets where this canary is to run.

(string)

SecurityGroupIds -> (list)

The IDs of the security groups for this canary.

(string)

Ipv6AllowedForDualStack -> (boolean)

Set this to `true` to allow outbound IPv6 traffic on VPC canaries that are connected to dual-stack subnets. The default is `false`

Shorthand Syntax:

```
SubnetIds=string,string,SecurityGroupIds=string,string,Ipv6AllowedForDualStack=boolean
```

JSON Syntax:

```
{
  "SubnetIds": ["string", ...],
  "SecurityGroupIds": ["string", ...],
  "Ipv6AllowedForDualStack": true|false
}
```

`--resources-to-replicate-tags` (list)

To have the tags that you apply to this canary also be applied to the Lambda function that the canary uses, specify this parameter with the value `lambda-function` .

If you specify this parameter and donât specify any tags in the `Tags` parameter, the canary creation fails.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  lambda-function
```

`--provisioned-resource-cleanup` (string)

Specifies whether to also delete the Lambda functions and layers used by this canary when the canary is deleted. If you omit this parameter, the default of `AUTOMATIC` is used, which means that the Lambda functions and layers will be deleted when the canary is deleted.

If the value of this parameter is `OFF` , then the value of the `DeleteLambda` parameter of the [DeleteCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteCanary.html) operation determines whether the Lambda functions and layers will be deleted.

Possible values:

- `AUTOMATIC`
- `OFF`

`--tags` (map)

A list of key-value pairs to associate with the canary. You can associate as many as 50 tags with a canary.

Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only the resources that have certain tag values.

To have the tags that you apply to this canary also be applied to the Lambda function that the canary uses, specify this parameter with the value `lambda-function` .

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

`--artifact-config` (structure)

A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.

S3Encryption -> (structure)

A structure that contains the configuration of the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3. Artifact encryption functionality is available only for canaries that use Synthetics runtime version syn-nodejs-puppeteer-3.3 or later. For more information, see [Encrypting canary artifacts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_artifact_encryption.html)

EncryptionMode -> (string)

The encryption method to use for artifacts created by this canary. Specify `SSE_S3` to use server-side encryption (SSE) with an Amazon S3-managed key. Specify `SSE-KMS` to use server-side encryption with a customer-managed KMS key.

If you omit this parameter, an Amazon Web Services-managed KMS key is used.

KmsKeyArn -> (string)

The ARN of the customer-managed KMS key to use, if you specify `SSE-KMS` for `EncryptionMode`

Shorthand Syntax:

```
S3Encryption={EncryptionMode=string,KmsKeyArn=string}
```

JSON Syntax:

```
{
  "S3Encryption": {
    "EncryptionMode": "SSE_S3"|"SSE_KMS",
    "KmsKeyArn": "string"
  }
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a canary**

The following `create-canary` example creates a canary named `demo_canary`.

```
aws synthetics create-canary \
    --name demo_canary \
    --code '{"S3Bucket": "artifacts3bucket", "S3Key":"demo_canary.zip", "Handler": "index.lambda_handler"}' \
    --artifact-s3-location s3://amzn-s3-demo-bucket/demo_canary.zip \
    --execution-role-arn arn:aws:iam::123456789012:role/demo_canary_role \
    --schedule Expression="rate(10 minutes)" \
    --runtime-version syn-nodejs-puppeteer-9.1
```

Output:

```
{
    "Canary": {
        "Id": "a1b2c3d4-5678-90ab-cdef-example11111",
        "Name": "demo_canary",
        "Code": {
            "Handler": "index.lambda_handler"
        },
        "ExecutionRoleArn": "arn:aws:iam::123456789012:role/demo_canary_role",
        "Schedule": {
            "Expression": "rate(10 minutes)",
            "DurationInSeconds": 0
        },
        "RunConfig": {
            "TimeoutInSeconds": 600,
            "MemoryInMB": 1000,
            "ActiveTracing": false
        },
        "SuccessRetentionPeriodInDays": 31,
        "FailureRetentionPeriodInDays": 31,
        "Status": {
            "State": "CREATING",
            "StateReasonCode": "CREATE_PENDING"
        },
        "Timeline": {
            "Created": "2024-10-15T19:03:08.826000+05:30",
            "LastModified": "2024-10-15T19:03:08.826000+05:30"
        },
        "ArtifactS3Location": "amzn-s3-demo-bucket/demo_canary.zip",
        "RuntimeVersion": "syn-nodejs-puppeteer-9.1",
        "Tags": {}
    }
}
```

For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) in the *Amazon CloudWatch User Guide*.

## Output

Canary -> (structure)

The full details about the canary you have created.

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