# start-protected-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/start-protected-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/start-protected-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cleanrooms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/index.html#cli-aws-cleanrooms) ]

# start-protected-job

## Description

Creates a protected job that is started by Clean Rooms.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cleanrooms-2022-02-17/StartProtectedJob)

## Synopsis

```
start-protected-job
--type <value>
--membership-identifier <value>
--job-parameters <value>
[--result-configuration <value>]
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

`--type` (string)

The type of protected job to start.

Possible values:

- `PYSPARK`

`--membership-identifier` (string)

A unique identifier for the membership to run this job against. Currently accepts a membership ID.

`--job-parameters` (structure)

The job parameters.

analysisTemplateArn -> (string)

The ARN of the analysis template.

Shorthand Syntax:

```
analysisTemplateArn=string
```

JSON Syntax:

```
{
  "analysisTemplateArn": "string"
}
```

`--result-configuration` (structure)

The details needed to write the job results.

outputConfiguration -> (tagged union structure)

The output configuration for a protected job result.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `member`.

member -> (structure)

The member of the protected job output configuration input.

accountId -> (string)

The account ID.

Shorthand Syntax:

```
outputConfiguration={member={accountId=string}}
```

JSON Syntax:

```
{
  "outputConfiguration": {
    "member": {
      "accountId": "string"
    }
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

## Output

protectedJob -> (structure)

The protected job.

id -> (string)

The identifier for a protected job instance.

membershipId -> (string)

he identifier for the membership.

membershipArn -> (string)

The ARN of the membership.

createTime -> (timestamp)

The creation time of the protected job.

jobParameters -> (structure)

The job parameters for the protected job.

analysisTemplateArn -> (string)

The ARN of the analysis template.

status -> (string)

The status of the protected job.

resultConfiguration -> (structure)

Contains any details needed to write the job results.

outputConfiguration -> (tagged union structure)

The output configuration.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3`, `member`.

s3 -> (structure)

If present, the output for a protected job with an S3 output type.

bucket -> (string)

The S3 bucket for job output.

keyPrefix -> (string)

The S3 prefix to unload the protected job results.

member -> (structure)

The member output configuration for a protected job.

accountId -> (string)

The account ID.

statistics -> (structure)

The statistics of the protected job.

totalDurationInMillis -> (long)

The duration of the protected job, from creation until job completion, in milliseconds.

billedResourceUtilization -> (structure)

The billed resource utilization for the protected job.

units -> (double)

The number of Clean Rooms Processing Unit (CRPU) hours that have been billed.

result -> (structure)

The result of the protected job.

output -> (tagged union structure)

The output of the protected job.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3`, `memberList`.

s3 -> (structure)

If present, the output for a protected job with an S3 output type.

location -> (string)

The S3 location for the protected job output.

memberList -> (list)

The list of member Amazon Web Services account(s) that received the results of the job.

(structure)

Details about the member who received the job result.

accountId -> (string)

The Amazon Web Services account ID of the member in the collaboration who can receive results from analyses.

error -> (structure)

The error from the protected job.

message -> (string)

The message for the protected job error.

code -> (string)

The error code for the protected job.