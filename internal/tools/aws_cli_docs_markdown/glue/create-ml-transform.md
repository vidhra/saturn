# create-ml-transformÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-ml-transform.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-ml-transform.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# create-ml-transform

## Description

Creates an Glue machine learning transform. This operation creates the transform and all the necessary parameters to train it.

Call this operation as the first step in the process of using a machine learning transform (such as the `FindMatches` transform) for deduplicating data. You can provide an optional `Description` , in addition to the parameters that you want to use for your algorithm.

You must also specify certain parameters for the tasks that Glue runs on your behalf as part of learning from your data and creating a high-quality machine learning transform. These parameters include `Role` , and optionally, `AllocatedCapacity` , `Timeout` , and `MaxRetries` . For more information, see [Jobs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateMLTransform)

## Synopsis

```
create-ml-transform
--name <value>
[--description <value>]
--input-record-tables <value>
--parameters <value>
--role <value>
[--glue-version <value>]
[--max-capacity <value>]
[--worker-type <value>]
[--number-of-workers <value>]
[--timeout <value>]
[--max-retries <value>]
[--tags <value>]
[--transform-encryption <value>]
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

The unique name that you give the transform when you create it.

`--description` (string)

A description of the machine learning transform that is being defined. The default is an empty string.

`--input-record-tables` (list)

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

Shorthand Syntax:

```
DatabaseName=string,TableName=string,CatalogId=string,ConnectionName=string,AdditionalOptions={KeyName1=string,KeyName2=string} ...
```

JSON Syntax:

```
[
  {
    "DatabaseName": "string",
    "TableName": "string",
    "CatalogId": "string",
    "ConnectionName": "string",
    "AdditionalOptions": {"string": "string"
      ...}
  }
  ...
]
```

`--parameters` (structure)

The algorithmic parameters that are specific to the transform type used. Conditionally dependent on the transform type.

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

Shorthand Syntax:

```
TransformType=string,FindMatchesParameters={PrimaryKeyColumnName=string,PrecisionRecallTradeoff=double,AccuracyCostTradeoff=double,EnforceProvidedLabels=boolean}
```

JSON Syntax:

```
{
  "TransformType": "FIND_MATCHES",
  "FindMatchesParameters": {
    "PrimaryKeyColumnName": "string",
    "PrecisionRecallTradeoff": double,
    "AccuracyCostTradeoff": double,
    "EnforceProvidedLabels": true|false
  }
}
```

`--role` (string)

The name or Amazon Resource Name (ARN) of the IAM role with the required permissions. The required permissions include both Glue service role permissions to Glue resources, and Amazon S3 permissions required by the transform.

- This role needs Glue service role permissions to allow access to resources in Glue. See [Attach a Policy to IAM Users That Access Glue](https://docs.aws.amazon.com/glue/latest/dg/attach-policy-iam-user.html) .
- This role needs permission to your Amazon Simple Storage Service (Amazon S3) sources, targets, temporary directory, scripts, and any libraries used by the task run for this transform.

`--glue-version` (string)

This value determines which version of Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see [Glue Versions](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html#release-notes-versions) in the developer guide.

`--max-capacity` (double)

The number of Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the [Glue pricing page](https://aws.amazon.com/glue/pricing/) .

`MaxCapacity` is a mutually exclusive option with `NumberOfWorkers` and `WorkerType` .

- If either `NumberOfWorkers` or `WorkerType` is set, then `MaxCapacity` cannot be set.
- If `MaxCapacity` is set then neither `NumberOfWorkers` or `WorkerType` can be set.
- If `WorkerType` is set, then `NumberOfWorkers` is required (and vice versa).
- `MaxCapacity` and `NumberOfWorkers` must both be at least 1.

When the `WorkerType` field is set to a value other than `Standard` , the `MaxCapacity` field is set automatically and becomes read-only.

When the `WorkerType` field is set to a value other than `Standard` , the `MaxCapacity` field is set automatically and becomes read-only.

`--worker-type` (string)

The type of predefined worker that is allocated when this task runs. Accepts a value of Standard, G.1X, or G.2X.

- For the `Standard` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
- For the `G.1X` worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.
- For the `G.2X` worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.

`MaxCapacity` is a mutually exclusive option with `NumberOfWorkers` and `WorkerType` .

- If either `NumberOfWorkers` or `WorkerType` is set, then `MaxCapacity` cannot be set.
- If `MaxCapacity` is set then neither `NumberOfWorkers` or `WorkerType` can be set.
- If `WorkerType` is set, then `NumberOfWorkers` is required (and vice versa).
- `MaxCapacity` and `NumberOfWorkers` must both be at least 1.

Possible values:

- `Standard`
- `G.1X`
- `G.2X`
- `G.025X`
- `G.4X`
- `G.8X`
- `Z.2X`

`--number-of-workers` (integer)

The number of workers of a defined `workerType` that are allocated when this task runs.

If `WorkerType` is set, then `NumberOfWorkers` is required (and vice versa).

`--timeout` (integer)

The timeout of the task run for this transform in minutes. This is the maximum time that a task run for this transform can consume resources before it is terminated and enters `TIMEOUT` status. The default is 2,880 minutes (48 hours).

`--max-retries` (integer)

The maximum number of times to retry a task for this transform after a task run fails.

`--tags` (map)

The tags to use with this machine learning transform. You may use tags to limit access to the machine learning transform. For more information about tags in Glue, see [Amazon Web Services Tags in Glue](https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html) in the developer guide.

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

`--transform-encryption` (structure)

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

Shorthand Syntax:

```
MlUserDataEncryption={MlUserDataEncryptionMode=string,KmsKeyId=string},TaskRunSecurityConfigurationName=string
```

JSON Syntax:

```
{
  "MlUserDataEncryption": {
    "MlUserDataEncryptionMode": "DISABLED"|"SSE-KMS",
    "KmsKeyId": "string"
  },
  "TaskRunSecurityConfigurationName": "string"
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

TransformId -> (string)

A unique identifier that is generated for the transform.