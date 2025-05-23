# create-model-invocation-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock/create-model-invocation-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock/create-model-invocation-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bedrock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock/index.html#cli-aws-bedrock) ]

# create-model-invocation-job

## Description

Creates a batch inference job to invoke a model on multiple prompts. Format your data according to [Format your inference data](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-data) and upload it to an Amazon S3 bucket. For more information, see [Process multiple prompts with batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html) .

The response returns a `jobArn` that you can use to stop or get details about the job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-2023-04-20/CreateModelInvocationJob)

## Synopsis

```
create-model-invocation-job
--job-name <value>
--role-arn <value>
[--client-request-token <value>]
--model-id <value>
--input-data-config <value>
--output-data-config <value>
[--vpc-config <value>]
[--timeout-duration-in-hours <value>]
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

`--job-name` (string)

A name to give the batch inference job.

`--role-arn` (string)

The Amazon Resource Name (ARN) of the service role with permissions to carry out and manage batch inference. You can use the console to create a default service role or follow the steps at [Create a service role for batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-iam-sr.html) .

`--client-request-token` (string)

A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) .

`--model-id` (string)

The unique identifier of the foundation model to use for the batch inference job.

`--input-data-config` (tagged union structure)

Details about the location of the input to the batch inference job.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3InputDataConfig`.

s3InputDataConfig -> (structure)

Contains the configuration of the S3 location of the input data.

s3InputFormat -> (string)

The format of the input data.

s3Uri -> (string)

The S3 location of the input data.

s3BucketOwner -> (string)

The ID of the Amazon Web Services account that owns the S3 bucket containing the input data.

Shorthand Syntax:

```
s3InputDataConfig={s3InputFormat=string,s3Uri=string,s3BucketOwner=string}
```

JSON Syntax:

```
{
  "s3InputDataConfig": {
    "s3InputFormat": "JSONL",
    "s3Uri": "string",
    "s3BucketOwner": "string"
  }
}
```

`--output-data-config` (tagged union structure)

Details about the location of the output of the batch inference job.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3OutputDataConfig`.

s3OutputDataConfig -> (structure)

Contains the configuration of the S3 location of the output data.

s3Uri -> (string)

The S3 location of the output data.

s3EncryptionKeyId -> (string)

The unique identifier of the key that encrypts the S3 location of the output data.

s3BucketOwner -> (string)

The ID of the Amazon Web Services account that owns the S3 bucket containing the output data.

Shorthand Syntax:

```
s3OutputDataConfig={s3Uri=string,s3EncryptionKeyId=string,s3BucketOwner=string}
```

JSON Syntax:

```
{
  "s3OutputDataConfig": {
    "s3Uri": "string",
    "s3EncryptionKeyId": "string",
    "s3BucketOwner": "string"
  }
}
```

`--vpc-config` (structure)

The configuration of the Virtual Private Cloud (VPC) for the data in the batch inference job. For more information, see [Protect batch inference jobs using a VPC](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-vpc) .

subnetIds -> (list)

An array of IDs for each subnet in the VPC to use.

(string)

securityGroupIds -> (list)

An array of IDs for each security group in the VPC to use.

(string)

Shorthand Syntax:

```
subnetIds=string,string,securityGroupIds=string,string
```

JSON Syntax:

```
{
  "subnetIds": ["string", ...],
  "securityGroupIds": ["string", ...]
}
```

`--timeout-duration-in-hours` (integer)

The number of hours after which to force the batch inference job to time out.

`--tags` (list)

Any tags to associate with the batch inference job. For more information, see [Tagging Amazon Bedrock resources](https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html) .

(structure)

Definition of the key/value pair for a tag.

key -> (string)

Key for the tag.

value -> (string)

Value for the tag.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
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

jobArn -> (string)

The Amazon Resource Name (ARN) of the batch inference job.