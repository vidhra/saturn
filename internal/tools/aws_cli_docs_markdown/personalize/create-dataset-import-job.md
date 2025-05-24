# create-dataset-import-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/create-dataset-import-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/create-dataset-import-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [personalize](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/index.html#cli-aws-personalize) ]

# create-dataset-import-job

## Description

Creates a job that imports training data from your data source (an Amazon S3 bucket) to an Amazon Personalize dataset. To allow Amazon Personalize to import the training data, you must specify an IAM service role that has permission to read from the data source, as Amazon Personalize makes a copy of your data and processes it internally. For information on granting access to your Amazon S3 bucket, see [Giving Amazon Personalize Access to Amazon S3 Resources](https://docs.aws.amazon.com/personalize/latest/dg/granting-personalize-s3-access.html) .

If you already created a recommender or deployed a custom solution version with a campaign, how new bulk records influence recommendations depends on the domain use case or recipe that you use. For more information, see [How new data influences real-time recommendations](https://docs.aws.amazon.com/personalize/latest/dg/how-new-data-influences-recommendations.html) .

### Warning

By default, a dataset import job replaces any existing data in the dataset that you imported in bulk. To add new records without replacing existing data, specify INCREMENTAL for the import mode in the CreateDatasetImportJob operation.

**Status**

A dataset import job can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

To get the status of the import job, call [DescribeDatasetImportJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDatasetImportJob.html) , providing the Amazon Resource Name (ARN) of the dataset import job. The dataset import is complete when the status shows as ACTIVE. If the status shows as CREATE FAILED, the response includes a `failureReason` key, which describes why the job failed.

### Note

Importing takes time. You must wait until the status shows as ACTIVE before training a model using the dataset.

**Related APIs**

- [ListDatasetImportJobs](https://docs.aws.amazon.com/personalize/latest/dg/API_ListDatasetImportJobs.html)
- [DescribeDatasetImportJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDatasetImportJob.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/personalize-2018-05-22/CreateDatasetImportJob)

## Synopsis

```
create-dataset-import-job
--job-name <value>
--dataset-arn <value>
--data-source <value>
--role-arn <value>
[--tags <value>]
[--import-mode <value>]
[--publish-attribution-metrics-to-s3 | --no-publish-attribution-metrics-to-s3]
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

The name for the dataset import job.

`--dataset-arn` (string)

The ARN of the dataset that receives the imported data.

`--data-source` (structure)

The Amazon S3 bucket that contains the training data to import.

dataLocation -> (string)

For dataset import jobs, the path to the Amazon S3 bucket where the data that you want to upload to your dataset is stored. For data deletion jobs, the path to the Amazon S3 bucket that stores the list of records to delete.

For example:

`s3://bucket-name/folder-name/fileName.csv`

If your CSV files are in a folder in your Amazon S3 bucket and you want your import job or data deletion job to consider multiple files, you can specify the path to the folder. With a data deletion job, Amazon Personalize uses all files in the folder and any sub folder. Use the following syntax with a `/` after the folder name:

`s3://bucket-name/folder-name/`

Shorthand Syntax:

```
dataLocation=string
```

JSON Syntax:

```
{
  "dataLocation": "string"
}
```

`--role-arn` (string)

The ARN of the IAM role that has permissions to read from the Amazon S3 data source.

`--tags` (list)

A list of [tags](https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html) to apply to the dataset import job.

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

`--import-mode` (string)

Specify how to add the new records to an existing dataset. The default import mode is `FULL` . If you havenât imported bulk records into the dataset previously, you can only specify `FULL` .

- Specify `FULL` to overwrite all existing bulk data in your dataset. Data you imported individually is not replaced.
- Specify `INCREMENTAL` to append the new records to the existing data in your dataset. Amazon Personalize replaces any record with the same ID with the new one.

Possible values:

- `FULL`
- `INCREMENTAL`

`--publish-attribution-metrics-to-s3` | `--no-publish-attribution-metrics-to-s3` (boolean)

If you created a metric attribution, specify whether to publish metrics for this import job to Amazon S3

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

datasetImportJobArn -> (string)

The ARN of the dataset import job.