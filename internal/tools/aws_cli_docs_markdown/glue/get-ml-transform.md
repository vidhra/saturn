# get-ml-transformÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-ml-transform.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-ml-transform.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# get-ml-transform

## Description

Gets an Glue machine learning transform artifact and all its corresponding metadata. Machine learning transforms are a special type of transform that use machine learning to learn the details of the transformation to be performed by learning from examples provided by humans. These transformations are then saved by Glue. You can retrieve their metadata by calling `GetMLTransform` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetMLTransform)

## Synopsis

```
get-ml-transform
--transform-id <value>
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

`--transform-id` (string)

The unique identifier of the transform, generated at the time that the transform was created.

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

TransformId -> (string)

The unique identifier of the transform, generated at the time that the transform was created.

Name -> (string)

The unique name given to the transform when it was created.

Description -> (string)

A description of the transform.

Status -> (string)

The last known status of the transform (to indicate whether it can be used or not). One of âNOT_READYâ, âREADYâ, or âDELETINGâ.

CreatedOn -> (timestamp)

The date and time when the transform was created.

LastModifiedOn -> (timestamp)

The date and time when the transform was last modified.

InputRecordTables -> (list)

A list of Glue table definitions used by the transform.

(structure)

The database and table in the Glue Data Catalog that is used for input or output data.

DatabaseName -> (string)

A database name in the Glue Data Catalog.

TableName -> (string)

A table name in the Glue Data Catalog.

CatalogId -> (string)

A unique identifier for the Glue Data Catalog.

ConnectionName -> (string)

The name of the connection to the Glue Data Catalog.

AdditionalOptions -> (map)

Additional options for the table. Currently there are two keys supported:

- `pushDownPredicate` : to filter on partitions without having to list and read all the files in your dataset.
- `catalogPartitionPredicate` : to use server-side partition pruning using partition indexes in the Glue Data Catalog.

key -> (string)

value -> (string)

Parameters -> (structure)

The configuration parameters that are specific to the algorithm used.

TransformType -> (string)

The type of machine learning transform.

For information about the types of machine learning transforms, see [Creating Machine Learning Transforms](https://docs.aws.amazon.com/glue/latest/dg/add-job-machine-learning-transform.html) .

FindMatchesParameters -> (structure)

The parameters for the find matches algorithm.

PrimaryKeyColumnName -> (string)

The name of a column that uniquely identifies rows in the source table. Used to help identify matching records.

PrecisionRecallTradeoff -> (double)

The value selected when tuning your transform for a balance between precision and recall. A value of 0.5 means no preference; a value of 1.0 means a bias purely for precision, and a value of 0.0 means a bias for recall. Because this is a tradeoff, choosing values close to 1.0 means very low recall, and choosing values close to 0.0 results in very low precision.

The precision metric indicates how often your model is correct when it predicts a match.

The recall metric indicates that for an actual match, how often your model predicts the match.

AccuracyCostTradeoff -> (double)

The value that is selected when tuning your transform for a balance between accuracy and cost. A value of 0.5 means that the system balances accuracy and cost concerns. A value of 1.0 means a bias purely for accuracy, which typically results in a higher cost, sometimes substantially higher. A value of 0.0 means a bias purely for cost, which results in a less accurate `FindMatches` transform, sometimes with unacceptable accuracy.

Accuracy measures how well the transform finds true positives and true negatives. Increasing accuracy requires more machine resources and cost. But it also results in increased recall.

Cost measures how many compute resources, and thus money, are consumed to run the transform.

EnforceProvidedLabels -> (boolean)

The value to switch on or off to force the output to match the provided labels from users. If the value is `True` , the `find matches` transform forces the output to match the provided labels. The results override the normal conflation results. If the value is `False` , the `find matches` transform does not ensure all the labels provided are respected, and the results rely on the trained model.

Note that setting this value to true may increase the conflation execution time.

EvaluationMetrics -> (structure)

The latest evaluation metrics.

TransformType -> (string)

The type of machine learning transform.

FindMatchesMetrics -> (structure)

The evaluation metrics for the find matches algorithm.

AreaUnderPRCurve -> (double)

The area under the precision/recall curve (AUPRC) is a single number measuring the overall quality of the transform, that is independent of the choice made for precision vs. recall. Higher values indicate that you have a more attractive precision vs. recall tradeoff.

For more information, see [Precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall) in Wikipedia.

Precision -> (double)

The precision metric indicates when often your transform is correct when it predicts a match. Specifically, it measures how well the transform finds true positives from the total true positives possible.

For more information, see [Precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall) in Wikipedia.

Recall -> (double)

The recall metric indicates that for an actual match, how often your transform predicts the match. Specifically, it measures how well the transform finds true positives from the total records in the source data.

For more information, see [Precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall) in Wikipedia.

F1 -> (double)

The maximum F1 metric indicates the transformâs accuracy between 0 and 1, where 1 is the best accuracy.

For more information, see [F1 score](https://en.wikipedia.org/wiki/F1_score) in Wikipedia.

ConfusionMatrix -> (structure)

The confusion matrix shows you what your transform is predicting accurately and what types of errors it is making.

For more information, see [Confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix) in Wikipedia.

NumTruePositives -> (long)

The number of matches in the data that the transform correctly found, in the confusion matrix for your transform.

NumFalsePositives -> (long)

The number of nonmatches in the data that the transform incorrectly classified as a match, in the confusion matrix for your transform.

NumTrueNegatives -> (long)

The number of nonmatches in the data that the transform correctly rejected, in the confusion matrix for your transform.

NumFalseNegatives -> (long)

The number of matches in the data that the transform didnât find, in the confusion matrix for your transform.

ColumnImportances -> (list)

A list of `ColumnImportance` structures containing column importance metrics, sorted in order of descending importance.

(structure)

A structure containing the column name and column importance score for a column.

Column importance helps you understand how columns contribute to your model, by identifying which columns in your records are more important than others.

ColumnName -> (string)

The name of a column.

Importance -> (double)

The column importance score for the column, as a decimal.

LabelCount -> (integer)

The number of labels available for this transform.

Schema -> (list)

The `Map<Column, Type>` object that represents the schema that this transform accepts. Has an upper bound of 100 columns.

(structure)

A key-value pair representing a column and data type that this transform can run against. The `Schema` parameter of the `MLTransform` may contain up to 100 of these structures.

Name -> (string)

The name of the column.

DataType -> (string)

The type of data in the column.

Role -> (string)

The name or Amazon Resource Name (ARN) of the IAM role with the required permissions.

GlueVersion -> (string)

This value determines which version of Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see [Glue Versions](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html#release-notes-versions) in the developer guide.

MaxCapacity -> (double)

The number of Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the [Glue pricing page](https://aws.amazon.com/glue/pricing/) .

When the `WorkerType` field is set to a value other than `Standard` , the `MaxCapacity` field is set automatically and becomes read-only.

WorkerType -> (string)

The type of predefined worker that is allocated when this task runs. Accepts a value of Standard, G.1X, or G.2X.

- For the `Standard` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
- For the `G.1X` worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.
- For the `G.2X` worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.

NumberOfWorkers -> (integer)

The number of workers of a defined `workerType` that are allocated when this task runs.

Timeout -> (integer)

The timeout for a task run for this transform in minutes. This is the maximum time that a task run for this transform can consume resources before it is terminated and enters `TIMEOUT` status. The default is 2,880 minutes (48 hours).

MaxRetries -> (integer)

The maximum number of times to retry a task for this transform after a task run fails.

TransformEncryption -> (structure)

The encryption-at-rest settings of the transform that apply to accessing user data. Machine learning transforms can access user data encrypted in Amazon S3 using KMS.

MlUserDataEncryption -> (structure)

An `MLUserDataEncryption` object containing the encryption mode and customer-provided KMS key ID.

MlUserDataEncryptionMode -> (string)

The encryption mode applied to user data. Valid values are:

- DISABLED: encryption is disabled
- SSEKMS: use of server-side encryption with Key Management Service (SSE-KMS) for user data stored in Amazon S3.

KmsKeyId -> (string)

The ID for the customer-provided KMS key.

TaskRunSecurityConfigurationName -> (string)

The name of the security configuration.