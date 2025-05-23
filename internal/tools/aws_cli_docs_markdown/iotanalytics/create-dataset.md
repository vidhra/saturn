# create-datasetÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/create-dataset.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/create-dataset.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotanalytics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/index.html#cli-aws-iotanalytics) ]

# create-dataset

## Description

Used to create a dataset. A dataset stores data retrieved from a data store by applying a `queryAction` (a SQL query) or a `containerAction` (executing a containerized application). This operation creates the skeleton of a dataset. The dataset can be populated manually by calling `CreateDatasetContent` or automatically according to a trigger you specify.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/CreateDataset)

## Synopsis

```
create-dataset
--dataset-name <value>
--actions <value>
[--triggers <value>]
[--content-delivery-rules <value>]
[--retention-period <value>]
[--versioning-configuration <value>]
[--tags <value>]
[--late-data-rules <value>]
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

`--dataset-name` (string)

The name of the dataset.

`--actions` (list)

A list of actions that create the dataset contents.

(structure)

A `DatasetAction` object that specifies how dataset contents are automatically created.

actionName -> (string)

The name of the dataset action by which dataset contents are automatically created.

queryAction -> (structure)

An `SqlQueryDatasetAction` object that uses an SQL query to automatically create dataset contents.

sqlQuery -> (string)

A SQL query string.

filters -> (list)

Prefilters applied to message data.

(structure)

Information that is used to filter message data, to segregate it according to the timeframe in which it arrives.

deltaTime -> (structure)

Used to limit data to that which has arrived since the last execution of the action.

offsetSeconds -> (integer)

The number of seconds of estimated in-flight lag time of message data. When you create dataset contents using message data from a specified timeframe, some message data might still be in flight when processing begins, and so do not arrive in time to be processed. Use this field to make allowances for the in flight time of your message data, so that data not processed from a previous timeframe is included with the next timeframe. Otherwise, missed message data would be excluded from processing during the next timeframe too, because its timestamp places it within the previous timeframe.

timeExpression -> (string)

An expression by which the time of the message data might be determined. This can be the name of a timestamp field or a SQL expression that is used to derive the time the message data was generated.

containerAction -> (structure)

Information that allows the system to run a containerized application to create the dataset contents. The application must be in a Docker container along with any required support libraries.

image -> (string)

The ARN of the Docker container stored in your account. The Docker container contains an application and required support libraries and is used to generate dataset contents.

executionRoleArn -> (string)

The ARN of the role that gives permission to the system to access required resources to run the `containerAction` . This includes, at minimum, permission to retrieve the dataset contents that are the input to the containerized application.

resourceConfiguration -> (structure)

Configuration of the resource that executes the `containerAction` .

computeType -> (string)

The type of the compute resource used to execute the `containerAction` . Possible values are: `ACU_1` (vCPU=4, memory=16 GiB) or `ACU_2` (vCPU=8, memory=32 GiB).

volumeSizeInGB -> (integer)

The size, in GB, of the persistent storage available to the resource instance used to execute the `containerAction` (min: 1, max: 50).

variables -> (list)

The values of variables used in the context of the execution of the containerized application (basically, parameters passed to the application). Each variable must have a name and a value given by one of `stringValue` , `datasetContentVersionValue` , or `outputFileUriValue` .

(structure)

An instance of a variable to be passed to the `containerAction` execution. Each variable must have a name and a value given by one of `stringValue` , `datasetContentVersionValue` , or `outputFileUriValue` .

name -> (string)

The name of the variable.

stringValue -> (string)

The value of the variable as a string.

doubleValue -> (double)

The value of the variable as a double (numeric).

datasetContentVersionValue -> (structure)

The value of the variable as a structure that specifies a dataset content version.

datasetName -> (string)

The name of the dataset whose latest contents are used as input to the notebook or application.

outputFileUriValue -> (structure)

The value of the variable as a structure that specifies an output file URI.

fileName -> (string)

The URI of the location where dataset contents are stored, usually the URI of a file in an S3 bucket.

JSON Syntax:

```
[
  {
    "actionName": "string",
    "queryAction": {
      "sqlQuery": "string",
      "filters": [
        {
          "deltaTime": {
            "offsetSeconds": integer,
            "timeExpression": "string"
          }
        }
        ...
      ]
    },
    "containerAction": {
      "image": "string",
      "executionRoleArn": "string",
      "resourceConfiguration": {
        "computeType": "ACU_1"|"ACU_2",
        "volumeSizeInGB": integer
      },
      "variables": [
        {
          "name": "string",
          "stringValue": "string",
          "doubleValue": double,
          "datasetContentVersionValue": {
            "datasetName": "string"
          },
          "outputFileUriValue": {
            "fileName": "string"
          }
        }
        ...
      ]
    }
  }
  ...
]
```

`--triggers` (list)

A list of triggers. A trigger causes dataset contents to be populated at a specified time interval or when another datasetâs contents are created. The list of triggers can be empty or contain up to five `DataSetTrigger` objects.

(structure)

The `DatasetTrigger` that specifies when the dataset is automatically updated.

schedule -> (structure)

The Schedule when the trigger is initiated.

expression -> (string)

The expression that defines when to trigger an update. For more information, see [Schedule Expressions for Rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html) in the *Amazon CloudWatch Events User Guide* .

dataset -> (structure)

The dataset whose content creation triggers the creation of this datasetâs contents.

name -> (string)

The name of the dataset whose content generation triggers the new dataset content generation.

Shorthand Syntax:

```
schedule={expression=string},dataset={name=string} ...
```

JSON Syntax:

```
[
  {
    "schedule": {
      "expression": "string"
    },
    "dataset": {
      "name": "string"
    }
  }
  ...
]
```

`--content-delivery-rules` (list)

When dataset contents are created, they are delivered to destinations specified here.

(structure)

When dataset contents are created, they are delivered to destination specified here.

entryName -> (string)

The name of the dataset content delivery rules entry.

destination -> (structure)

The destination to which dataset contents are delivered.

iotEventsDestinationConfiguration -> (structure)

Configuration information for delivery of dataset contents to IoT Events.

inputName -> (string)

The name of the IoT Events input to which dataset contents are delivered.

roleArn -> (string)

The ARN of the role that grants IoT Analytics permission to deliver dataset contents to an IoT Events input.

s3DestinationConfiguration -> (structure)

Configuration information for delivery of dataset contents to Amazon S3.

bucket -> (string)

The name of the S3 bucket to which dataset contents are delivered.

key -> (string)

The key of the dataset contents object in an S3 bucket. Each object has a key that is a unique identifier. Each object has exactly one key.

You can create a unique key with the following options:

- Use `!{iotanalytics:scheduleTime}` to insert the time of a scheduled SQL query run.
- Use `!{iotanalytics:versionId}` to insert a unique hash that identifies a dataset content.
- Use `!{iotanalytics:creationTime}` to insert the creation time of a dataset content.

The following example creates a unique key for a CSV file: `dataset/mydataset/!{iotanalytics:scheduleTime}/!{iotanalytics:versionId}.csv`

### Note

If you donât use `!{iotanalytics:versionId}` to specify the key, you might get duplicate keys. For example, you might have two dataset contents with the same `scheduleTime` but different `versionId` s. This means that one dataset content overwrites the other.

glueConfiguration -> (structure)

Configuration information for coordination with Glue, a fully managed extract, transform and load (ETL) service.

tableName -> (string)

The name of the table in your Glue Data Catalog that is used to perform the ETL operations. An Glue Data Catalog table contains partitioned data and descriptions of data sources and targets.

databaseName -> (string)

The name of the database in your Glue Data Catalog in which the table is located. An Glue Data Catalog database contains metadata tables.

roleArn -> (string)

The ARN of the role that grants IoT Analytics permission to interact with your Amazon S3 and Glue resources.

JSON Syntax:

```
[
  {
    "entryName": "string",
    "destination": {
      "iotEventsDestinationConfiguration": {
        "inputName": "string",
        "roleArn": "string"
      },
      "s3DestinationConfiguration": {
        "bucket": "string",
        "key": "string",
        "glueConfiguration": {
          "tableName": "string",
          "databaseName": "string"
        },
        "roleArn": "string"
      }
    }
  }
  ...
]
```

`--retention-period` (structure)

Optional. How long, in days, versions of dataset contents are kept for the dataset. If not specified or set to `null` , versions of dataset contents are retained for at most 90 days. The number of versions of dataset contents retained is determined by the `versioningConfiguration` parameter. For more information, see [Keeping Multiple Versions of IoT Analytics datasets](https://docs.aws.amazon.com/iotanalytics/latest/userguide/getting-started.html#aws-iot-analytics-dataset-versions) in the *IoT Analytics User Guide* .

unlimited -> (boolean)

If true, message data is kept indefinitely.

numberOfDays -> (integer)

The number of days that message data is kept. The `unlimited` parameter must be false.

Shorthand Syntax:

```
unlimited=boolean,numberOfDays=integer
```

JSON Syntax:

```
{
  "unlimited": true|false,
  "numberOfDays": integer
}
```

`--versioning-configuration` (structure)

Optional. How many versions of dataset contents are kept. If not specified or set to null, only the latest version plus the latest succeeded version (if they are different) are kept for the time period specified by the `retentionPeriod` parameter. For more information, see [Keeping Multiple Versions of IoT Analytics datasets](https://docs.aws.amazon.com/iotanalytics/latest/userguide/getting-started.html#aws-iot-analytics-dataset-versions) in the *IoT Analytics User Guide* .

unlimited -> (boolean)

If true, unlimited versions of dataset contents are kept.

maxVersions -> (integer)

How many versions of dataset contents are kept. The `unlimited` parameter must be `false` .

Shorthand Syntax:

```
unlimited=boolean,maxVersions=integer
```

JSON Syntax:

```
{
  "unlimited": true|false,
  "maxVersions": integer
}
```

`--tags` (list)

Metadata which can be used to manage the dataset.

(structure)

A set of key-value pairs that are used to manage the resource.

key -> (string)

The tagâs key.

value -> (string)

The tagâs value.

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

`--late-data-rules` (list)

A list of data rules that send notifications to CloudWatch, when data arrives late. To specify `lateDataRules` , the dataset must use a [DeltaTimer](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_DeltaTime.html) filter.

(structure)

A structure that contains the name and configuration information of a late data rule.

ruleName -> (string)

The name of the late data rule.

ruleConfiguration -> (structure)

The information needed to configure the late data rule.

deltaTimeSessionWindowConfiguration -> (structure)

The information needed to configure a delta time session window.

timeoutInMinutes -> (integer)

A time interval. You can use `timeoutInMinutes` so that IoT Analytics can batch up late data notifications that have been generated since the last execution. IoT Analytics sends one batch of notifications to Amazon CloudWatch Events at one time.

For more information about how to write a timestamp expression, see [Date and Time Functions and Operators](https://prestodb.io/docs/0.172/functions/datetime.html) , in the *Presto 0.172 Documentation* .

Shorthand Syntax:

```
ruleName=string,ruleConfiguration={deltaTimeSessionWindowConfiguration={timeoutInMinutes=integer}} ...
```

JSON Syntax:

```
[
  {
    "ruleName": "string",
    "ruleConfiguration": {
      "deltaTimeSessionWindowConfiguration": {
        "timeoutInMinutes": integer
      }
    }
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a dataset**

The following `create-dataset` example creates a dataset. A dataset stores data retrieved from a data store by applying a `queryAction` (a SQL query) or a `containerAction` (executing a containerized application). This operation creates the skeleton of a dataset. You can populate the dataset manually by calling `CreateDatasetContent` or automatically according to a `trigger` you specify.

```
aws iotanalytics create-dataset \
    --cli-input-json file://create-dataset.json
```

Contents of `create-dataset.json`:

```
{
    "datasetName": "mydataset",
    "actions": [
        {
            "actionName": "myDatasetAction",
            "queryAction": {
                "sqlQuery": "SELECT * FROM mydatastore"
            }
        }
    ],
    "retentionPeriod": {
        "unlimited": true
    },
    "tags": [
        {
            "key": "Environment",
            "value": "Production"
        }
    ]
}
```

Output:

```
{
    "datasetName": "mydataset",
    "retentionPeriod": {
        "unlimited": true
    },
    "datasetArn": "arn:aws:iotanalytics:us-west-2:123456789012:dataset/mydataset"
}
```

For more information, see [CreateDataset](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_CreateDataset.html) in the *AWS IoT Analytics API Reference*.

## Output

datasetName -> (string)

The name of the dataset.

datasetArn -> (string)

The ARN of the dataset.

retentionPeriod -> (structure)

How long, in days, dataset contents are kept for the dataset.

unlimited -> (boolean)

If true, message data is kept indefinitely.

numberOfDays -> (integer)

The number of days that message data is kept. The `unlimited` parameter must be false.