# create-batch-inference-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/create-batch-inference-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/create-batch-inference-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [personalize](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/index.html#cli-aws-personalize) ]

# create-batch-inference-job

## Description

Generates batch recommendations based on a list of items or users stored in Amazon S3 and exports the recommendations to an Amazon S3 bucket.

To generate batch recommendations, specify the ARN of a solution version and an Amazon S3 URI for the input and output data. For user personalization, popular items, and personalized ranking solutions, the batch inference job generates a list of recommended items for each user ID in the input file. For related items solutions, the job generates a list of recommended items for each item ID in the input file.

For more information, see [Creating a batch inference job](https://docs.aws.amazon.com/personalize/latest/dg/getting-batch-recommendations.html) .

If you use the Similar-Items recipe, Amazon Personalize can add descriptive themes to batch recommendations. To generate themes, set the jobâs mode to `THEME_GENERATION` and specify the name of the field that contains item names in the input data.

For more information about generating themes, see [Batch recommendations with themes from Content Generator](https://docs.aws.amazon.com/personalize/latest/dg/themed-batch-recommendations.html) .

You canât get batch recommendations with the Trending-Now or Next-Best-Action recipes.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/personalize-2018-05-22/CreateBatchInferenceJob)

## Synopsis

```
create-batch-inference-job
--job-name <value>
--solution-version-arn <value>
[--filter-arn <value>]
[--num-results <value>]
--job-input <value>
--job-output <value>
--role-arn <value>
[--batch-inference-job-config <value>]
[--tags <value>]
[--batch-inference-job-mode <value>]
[--theme-generation-config <value>]
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

The name of the batch inference job to create.

`--solution-version-arn` (string)

The Amazon Resource Name (ARN) of the solution version that will be used to generate the batch inference recommendations.

`--filter-arn` (string)

The ARN of the filter to apply to the batch inference job. For more information on using filters, see [Filtering batch recommendations](https://docs.aws.amazon.com/personalize/latest/dg/filter-batch.html) .

`--num-results` (integer)

The number of recommendations to retrieve.

`--job-input` (structure)

The Amazon S3 path that leads to the input file to base your recommendations on. The input material must be in JSON format.

s3DataSource -> (structure)

The URI of the Amazon S3 location that contains your input data. The Amazon S3 bucket must be in the same region as the API endpoint you are calling.

path -> (string)

The file path of the Amazon S3 bucket.

kmsKeyArn -> (string)

The Amazon Resource Name (ARN) of the Key Management Service (KMS) key that Amazon Personalize uses to encrypt or decrypt the input and output files.

Shorthand Syntax:

```
s3DataSource={path=string,kmsKeyArn=string}
```

JSON Syntax:

```
{
  "s3DataSource": {
    "path": "string",
    "kmsKeyArn": "string"
  }
}
```

`--job-output` (structure)

The path to the Amazon S3 bucket where the jobâs output will be stored.

s3DataDestination -> (structure)

Information on the Amazon S3 bucket in which the batch inference jobâs output is stored.

path -> (string)

The file path of the Amazon S3 bucket.

kmsKeyArn -> (string)

The Amazon Resource Name (ARN) of the Key Management Service (KMS) key that Amazon Personalize uses to encrypt or decrypt the input and output files.

Shorthand Syntax:

```
s3DataDestination={path=string,kmsKeyArn=string}
```

JSON Syntax:

```
{
  "s3DataDestination": {
    "path": "string",
    "kmsKeyArn": "string"
  }
}
```

`--role-arn` (string)

The ARN of the Amazon Identity and Access Management role that has permissions to read and write to your input and output Amazon S3 buckets respectively.

`--batch-inference-job-config` (structure)

The configuration details of a batch inference job.

itemExplorationConfig -> (map)

A string to string map specifying the exploration configuration hyperparameters, including `explorationWeight` and `explorationItemAgeCutOff` , you want to use to configure the amount of item exploration Amazon Personalize uses when recommending items. See [User-Personalization](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-new-item-USER_PERSONALIZATION.html) .

key -> (string)

value -> (string)

Shorthand Syntax:

```
itemExplorationConfig={KeyName1=string,KeyName2=string}
```

JSON Syntax:

```
{
  "itemExplorationConfig": {"string": "string"
    ...}
}
```

`--tags` (list)

A list of [tags](https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html) to apply to the batch inference job.

(structure)

The optional metadata that you apply to resources to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. For more information see [Tagging Amazon Personalize resources](https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html) .

tagKey -> (string)

One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.

tagValue -> (string)

The optional part of a key-value pair that makes up a tag. A value acts as a descriptor within a tag category (key).

Shorthand Syntax:

```
tagKey=string,tagValue=string ...
```

JSON Syntax:

```
[
  {
    "tagKey": "string",
    "tagValue": "string"
  }
  ...
]
```

`--batch-inference-job-mode` (string)

The mode of the batch inference job. To generate descriptive themes for groups of similar items, set the job mode to `THEME_GENERATION` . If you donât want to generate themes, use the default `BATCH_INFERENCE` .

When you get batch recommendations with themes, you will incur additional costs. For more information, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/) .

Possible values:

- `BATCH_INFERENCE`
- `THEME_GENERATION`

`--theme-generation-config` (structure)

For theme generation jobs, specify the name of the column in your Items dataset that contains each itemâs name.

fieldsForThemeGeneration -> (structure)

Fields used to generate descriptive themes for a batch inference job.

itemName -> (string)

The name of the Items dataset column that stores the name of each item in the dataset.

Shorthand Syntax:

```
fieldsForThemeGeneration={itemName=string}
```

JSON Syntax:

```
{
  "fieldsForThemeGeneration": {
    "itemName": "string"
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

batchInferenceJobArn -> (string)

The ARN of the batch inference job.