# get-audience-generation-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/get-audience-generation-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/get-audience-generation-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cleanroomsml](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanroomsml/index.html#cli-aws-cleanroomsml) ]

# get-audience-generation-job

## Description

Returns information about an audience generation job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cleanroomsml-2023-09-06/GetAudienceGenerationJob)

## Synopsis

```
get-audience-generation-job
--audience-generation-job-arn <value>
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

`--audience-generation-job-arn` (string)

The Amazon Resource Name (ARN) of the audience generation job that you are interested in.

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

createTime -> (timestamp)

The time at which the audience generation job was created.

updateTime -> (timestamp)

The most recent time at which the audience generation job was updated.

audienceGenerationJobArn -> (string)

The Amazon Resource Name (ARN) of the audience generation job.

name -> (string)

The name of the audience generation job.

description -> (string)

The description of the audience generation job.

status -> (string)

The status of the audience generation job.

statusDetails -> (structure)

Details about the status of the audience generation job.

statusCode -> (string)

The status code that was returned. The status code is intended for programmatic error handling. Clean Rooms ML will not change the status code for existing error conditions.

message -> (string)

The error message that was returned. The message is intended for human consumption and can change at any time. Use the `statusCode` for programmatic error handling.

configuredAudienceModelArn -> (string)

The Amazon Resource Name (ARN) of the configured audience model used for this audience generation job.

seedAudience -> (structure)

The seed audience that was used for this audience generation job. This field will be null if the account calling the API is the account that started this audience generation job.

dataSource -> (structure)

Defines the Amazon S3 bucket where the seed audience for the generating audience is stored. A valid data source is a JSON line file in the following format:

`{"user_id": "111111"}`

`{"user_id": "222222"}`

`...`

s3Uri -> (string)

The Amazon S3 location URI.

roleArn -> (string)

The ARN of the IAM role that can read the Amazon S3 bucket where the seed audience is stored.

sqlParameters -> (structure)

The protected SQL query parameters.

queryString -> (string)

The query string to be submitted.

analysisTemplateArn -> (string)

The Amazon Resource Name (ARN) associated with the analysis template within a collaboration.

parameters -> (map)

The protected query SQL parameters.

key -> (string)

value -> (string)

sqlComputeConfiguration -> (tagged union structure)

Provides configuration information for the instances that will perform the compute work.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `worker`.

worker -> (structure)

The worker instances that will perform the compute work.

type -> (string)

The instance type of the compute workers that are used.

number -> (integer)

The number of compute workers that are used.

includeSeedInOutput -> (boolean)

Configure whether the seed users are included in the output audience. By default, Clean Rooms ML removes seed users from the output audience. If you specify `TRUE` , the seed users will appear first in the output. Clean Rooms ML does not explicitly reveal whether a user was in the seed, but the recipient of the audience will know that the first `minimumSeedSize` count of users are from the seed.

collaborationId -> (string)

The identifier of the collaboration that this audience generation job is associated with.

metrics -> (structure)

The relevance scores for different audience sizes and the recall score of the generated audience.

relevanceMetrics -> (list)

The relevance scores of the generated audience.

(structure)

The relevance score of a generated audience.

audienceSize -> (structure)

The size of the generated audience. Must match one of the sizes in the configured audience model.

type -> (string)

Whether the audience size is defined in absolute terms or as a percentage. You can use the `ABSOLUTE`   AudienceSize to configure out audience sizes using the count of identifiers in the output. You can use the `Percentage`   AudienceSize to configure sizes in the range 1-100 percent.

value -> (integer)

Specify an audience size value.

score -> (double)

The relevance score of the generated audience.

recallMetric -> (double)

The recall score of the generated audience. Recall is the percentage of the most similar users (by default, the most similar 20%) from a sample of the training data that are included in the seed audience by the audience generation job. Values range from 0-1, larger values indicate a better audience. A recall value approximately equal to the maximum bin size indicates that the audience model is equivalent to random selection.

startedBy -> (string)

The AWS account that started this audience generation job.

tags -> (map)

The tags that are associated to this audience generation job.

key -> (string)

value -> (string)

protectedQueryIdentifier -> (string)

The unique identifier of the protected query for this audience generation job.