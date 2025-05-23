# start-canary-dry-runÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/start-canary-dry-run.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/start-canary-dry-run.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [synthetics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/index.html#cli-aws-synthetics) ]

# start-canary-dry-run

## Description

Use this operation to start a dry run for a canary that has already been created

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/synthetics-2017-10-11/StartCanaryDryRun)

## Synopsis

```
start-canary-dry-run
--name <value>
[--code <value>]
[--runtime-version <value>]
[--run-config <value>]
[--vpc-config <value>]
[--execution-role-arn <value>]
[--success-retention-period-in-days <value>]
[--failure-retention-period-in-days <value>]
[--visual-reference <value>]
[--artifact-s3-location <value>]
[--artifact-config <value>]
[--provisioned-resource-cleanup <value>]
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

The name of the canary that you want to dry run. To find canary names, use [DescribeCanaries](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html) .

`--code` (structure)

Use this structure to input your script code for the canary. This structure contains the Lambda handler with the location where the canary should start running the script. If the script is stored in an S3 bucket, the bucket name, key, and version are also included. If the script was passed into the canary directly, the script code is contained in the value of `Zipfile` .

If you are uploading your canary scripts with an Amazon S3 bucket, your zip file should include your script in a certain folder structure.

- For Node.js canaries, the folder structure must be [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/start-canary-dry-run.html#id1)nodejs/node_modules/*myCanaryFilename.js* `` For more information, see [Packaging your Node.js canary files](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_WritingCanary_Nodejs.html#CloudWatch_Synthetics_Canaries_package)
- For Python canaries, the folder structure must be [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/start-canary-dry-run.html#id3)python/*myCanaryFilename.py* `` or [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/start-canary-dry-run.html#id5)python/*myFolder/myCanaryFilename.py* `` For more information, see [Packaging your Python canary files](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_WritingCanary_Python.html#CloudWatch_Synthetics_Canaries_WritingCanary_Python_package)

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

`--runtime-version` (string)

Specifies the runtime version to use for the canary. For a list of valid runtime versions and for more information about runtime versions, see [Canary Runtime Versions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html) .

`--run-config` (structure)

A structure that contains input information for a canary run.

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

`--vpc-config` (structure)

If this canary is to test an endpoint in a VPC, this structure contains information about the subnets and security groups of the VPC endpoint. For more information, see [Running a Canary in a VPC](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html) .

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

`--execution-role-arn` (string)

The ARN of the IAM role to be used to run the canary. This role must already exist, and must include `lambda.amazonaws.com` as a principal in the trust policy. The role must also have the following permissions:

`--success-retention-period-in-days` (integer)

The number of days to retain data on the failed runs for this canary. The valid range is 1 to 455 days.

This setting affects the range of information returned by [GetCanaryRuns](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html) , as well as the range of information displayed in the Synthetics console.

`--failure-retention-period-in-days` (integer)

The number of days to retain data on the failed runs for this canary. The valid range is 1 to 455 days.

This setting affects the range of information returned by [GetCanaryRuns](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html) , as well as the range of information displayed in the Synthetics console.

`--visual-reference` (structure)

An object that specifies what screenshots to use as a baseline for visual monitoring by this canary. It can optionally also specify parts of the screenshots to ignore during the visual monitoring comparison.

Visual monitoring is supported only on canaries running the **syn-puppeteer-node-3.2** runtime or later. For more information, see [Visual monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_SyntheticsLogger_VisualTesting.html) and [Visual monitoring blueprint](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Blueprints_VisualTesting.html)

BaseScreenshots -> (list)

An array of screenshots that will be used as the baseline for visual monitoring in future runs of this canary. If there is a screenshot that you donât want to be used for visual monitoring, remove it from this array.

(structure)

A structure representing a screenshot that is used as a baseline during visual monitoring comparisons made by the canary.

ScreenshotName -> (string)

The name of the screenshot. This is generated the first time the canary is run after the `UpdateCanary` operation that specified for this canary to perform visual monitoring.

IgnoreCoordinates -> (list)

Coordinates that define the part of a screen to ignore during screenshot comparisons. To obtain the coordinates to use here, use the CloudWatch console to draw the boundaries on the screen. For more information, see [Editing or deleting a canary](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/synthetics_canaries_deletion.html)

(string)

BaseCanaryRunId -> (string)

Specifies which canary run to use the screenshots from as the baseline for future visual monitoring with this canary. Valid values are `nextrun` to use the screenshots from the next run after this update is made, `lastrun` to use the screenshots from the most recent run before this update was made, or the value of `Id` in the [CanaryRun](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRun.html) from a run of this a canary in the past 31 days. If you specify the `Id` of a canary run older than 31 days, the operation returns a 400 validation exception error..

JSON Syntax:

```
{
  "BaseScreenshots": [
    {
      "ScreenshotName": "string",
      "IgnoreCoordinates": ["string", ...]
    }
    ...
  ],
  "BaseCanaryRunId": "string"
}
```

`--artifact-s3-location` (string)

The location in Amazon S3 where Synthetics stores artifacts from the test runs of this canary. Artifacts include the log file, screenshots, and HAR files. The name of the Amazon S3 bucket canât include a period (.).

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

`--provisioned-resource-cleanup` (string)

Specifies whether to also delete the Lambda functions and layers used by this canary when the canary is deleted. If the value of this parameter is `AUTOMATIC` , it means that the Lambda functions and layers will be deleted when the canary is deleted.

If the value of this parameter is `OFF` , then the value of the `DeleteLambda` parameter of the [DeleteCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteCanary.html) operation determines whether the Lambda functions and layers will be deleted.

Possible values:

- `AUTOMATIC`
- `OFF`

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

DryRunConfig -> (structure)

Returns the dry run configurations for a canary.

DryRunId -> (string)

The DryRunId associated with an existing canaryâs dry run. You can use this DryRunId to retrieve information about the dry run.

LastDryRunExecutionStatus -> (string)

Returns the last execution status for a canaryâs dry run.