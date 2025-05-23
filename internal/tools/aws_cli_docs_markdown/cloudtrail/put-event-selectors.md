# put-event-selectorsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/put-event-selectors.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/put-event-selectors.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudtrail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/index.html#cli-aws-cloudtrail) ]

# put-event-selectors

## Description

Configures event selectors (also referred to as *basic event selectors* ) or advanced event selectors for your trail. You can use either `AdvancedEventSelectors` or `EventSelectors` , but not both. If you apply `AdvancedEventSelectors` to a trail, any existing `EventSelectors` are overwritten.

You can use `AdvancedEventSelectors` to log management events, data events for all resource types, and network activity events.

You can use `EventSelectors` to log management events and data events for the following resource types:

- `AWS::DynamoDB::Table`
- `AWS::Lambda::Function`
- `AWS::S3::Object`

You canât use `EventSelectors` to log network activity events.

If you want your trail to log Insights events, be sure the event selector or advanced event selector enables logging of the Insights event types you want configured for your trail. For more information about logging Insights events, see [Working with CloudTrail Insights](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.html) in the *CloudTrail User Guide* . By default, trails created without specific event selectors are configured to log all read and write management events, and no data events or network activity events.

When an event occurs in your account, CloudTrail evaluates the event selectors or advanced event selectors in all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesnât match any event selector, the trail doesnât log the event.

Example

- You create an event selector for a trail and specify that you want to log write-only events.
- The EC2 `GetConsoleOutput` and `RunInstances` API operations occur in your account.
- CloudTrail evaluates whether the events match your event selectors.
- The `RunInstances` is a write-only event and it matches your event selector. The trail logs the event.
- The `GetConsoleOutput` is a read-only event that doesnât match your event selector. The trail doesnât log the event.

The `PutEventSelectors` operation must be called from the Region in which the trail was created; otherwise, an `InvalidHomeRegionException` exception is thrown.

You can configure up to five event selectors for each trail.

You can add advanced event selectors, and conditions for your advanced event selectors, up to a maximum of 500 values for all conditions and selectors on a trail. For more information, see [Logging management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html) , [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) , [Logging network activity events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-network-events-with-cloudtrail.html) , and [Quotas in CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html) in the *CloudTrail User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/PutEventSelectors)

## Synopsis

```
put-event-selectors
--trail-name <value>
[--event-selectors <value>]
[--advanced-event-selectors <value>]
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

`--trail-name` (string)

Specifies the name of the trail or trail ARN. If you specify a trail name, the string must meet the following requirements:

- Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)
- Start with a letter or number, and end with a letter or number
- Be between 3 and 128 characters
- Have no adjacent periods, underscores or dashes. Names like `my-_namespace` and `my--namespace` are not valid.
- Not be in IP address format (for example, 192.168.5.4)

If you specify a trail ARN, it must be in the following format.

`arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`

`--event-selectors` (list)

Specifies the settings for your event selectors. You can use event selectors to log management events and data events for the following resource types:

- `AWS::DynamoDB::Table`
- `AWS::Lambda::Function`
- `AWS::S3::Object`

You canât use event selectors to log network activity events.

You can configure up to five event selectors for a trail. You can use either `EventSelectors` or `AdvancedEventSelectors` in a `PutEventSelectors` request, but not both. If you apply `EventSelectors` to a trail, any existing `AdvancedEventSelectors` are overwritten.

(structure)

Use event selectors to further specify the management and data event settings for your trail. By default, trails created without specific event selectors will be configured to log all read and write management events, and no data events. When an event occurs in your account, CloudTrail evaluates the event selector for all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesnât match any event selector, the trail doesnât log the event.

You can configure up to five event selectors for a trail.

You cannot apply both event selectors and advanced event selectors to a trail.

ReadWriteType -> (string)

Specify if you want your trail to log read-only events, write-only events, or all. For example, the EC2 `GetConsoleOutput` is a read-only API operation and `RunInstances` is a write-only API operation.

By default, the value is `All` .

IncludeManagementEvents -> (boolean)

Specify if you want your event selector to include management events for your trail.

For more information, see [Management Events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html) in the *CloudTrail User Guide* .

By default, the value is `true` .

The first copy of management events is free. You are charged for additional copies of management events that you are logging on any subsequent trail in the same Region. For more information about CloudTrail pricing, see [CloudTrail Pricing](http://aws.amazon.com/cloudtrail/pricing/) .

DataResources -> (list)

CloudTrail supports data event logging for Amazon S3 objects in standard S3 buckets, Lambda functions, and Amazon DynamoDB tables with basic event selectors. You can specify up to 250 resources for an individual event selector, but the total number of data resources cannot exceed 250 across all event selectors in a trail. This limit does not apply if you configure resource logging for all data events.

For more information, see [Data Events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) and [Limits in CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html) in the *CloudTrail User Guide* .

### Note

To log data events for all other resource types including objects stored in [directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html) , you must use [AdvancedEventSelectors](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html) . You must also use `AdvancedEventSelectors` if you want to filter on the `eventName` field.

(structure)

You can configure the `DataResource` in an `EventSelector` to log data events for the following three resource types:

- `AWS::DynamoDB::Table`
- `AWS::Lambda::Function`
- `AWS::S3::Object`

To log data events for all other resource types including objects stored in [directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html) , you must use [AdvancedEventSelectors](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html) . You must also use `AdvancedEventSelectors` if you want to filter on the `eventName` field.

Configure the `DataResource` to specify the resource type and resource ARNs for which you want to log data events.

### Note

The total number of allowed data resources is 250. This number can be distributed between 1 and 5 event selectors, but the total cannot exceed 250 across all selectors for the trail.

The following example demonstrates how logging works when you configure logging of all data events for a general purpose bucket named `amzn-s3-demo-bucket1` . In this example, the CloudTrail user specified an empty prefix, and the option to log both `Read` and `Write` data events.

- A user uploads an image file to `amzn-s3-demo-bucket1` .
- The `PutObject` API operation is an Amazon S3 object-level API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified an S3 bucket with an empty prefix, events that occur on any object in that bucket are logged. The trail processes and logs the event.
- A user uploads an object to an Amazon S3 bucket named `arn:aws:s3:::amzn-s3-demo-bucket1` .
- The `PutObject` API operation occurred for an object in an S3 bucket that the CloudTrail user didnât specify for the trail. The trail doesnât log the event.

The following example demonstrates how logging works when you configure logging of Lambda data events for a Lambda function named *MyLambdaFunction* , but not for all Lambda functions.

- A user runs a script that includes a call to the *MyLambdaFunction* function and the *MyOtherLambdaFunction* function.
- The `Invoke` API operation on *MyLambdaFunction* is an Lambda API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified logging data events for *MyLambdaFunction* , any invocations of that function are logged. The trail processes and logs the event.
- The `Invoke` API operation on *MyOtherLambdaFunction* is an Lambda API. Because the CloudTrail user did not specify logging data events for all Lambda functions, the `Invoke` operation for *MyOtherLambdaFunction* does not match the function specified for the trail. The trail doesnât log the event.

Type -> (string)

The resource type in which you want to log data events. You can specify the following *basic* event selector resource types:

- `AWS::DynamoDB::Table`
- `AWS::Lambda::Function`
- `AWS::S3::Object`

Additional resource types are available through *advanced* event selectors. For more information, see [AdvancedEventSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html) .

Values -> (list)

An array of Amazon Resource Name (ARN) strings or partial ARN strings for the specified resource type.

- To log data events for all objects in all S3 buckets in your Amazon Web Services account, specify the prefix as `arn:aws:s3` .

### Note

This also enables logging of data event activity performed by any user or role in your Amazon Web Services account, even if that activity is performed on a bucket that belongs to another Amazon Web Services account.

- To log data events for all objects in an S3 bucket, specify the bucket and an empty object prefix such as `arn:aws:s3:::amzn-s3-demo-bucket1/` . The trail logs data events for all objects in this S3 bucket.
- To log data events for specific objects, specify the S3 bucket and object prefix such as `arn:aws:s3:::amzn-s3-demo-bucket1/example-images` . The trail logs data events for objects in this S3 bucket that match the prefix.
- To log data events for all Lambda functions in your Amazon Web Services account, specify the prefix as `arn:aws:lambda` .

### Note

This also enables logging of `Invoke` activity performed by any user or role in your Amazon Web Services account, even if that activity is performed on a function that belongs to another Amazon Web Services account.

- To log data events for a specific Lambda function, specify the function ARN.

### Note

Lambda function ARNs are exact. For example, if you specify a function ARN *arn:aws:lambda:us-west-2:111111111111:function:helloworld* , data events will only be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld* . They will not be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld2* .

- To log data events for all DynamoDB tables in your Amazon Web Services account, specify the prefix as `arn:aws:dynamodb` .

(string)

ExcludeManagementEventSources -> (list)

An optional list of service event sources from which you do not want management events to be logged on your trail. In this release, the list can be empty (disables the filter), or it can filter out Key Management Service or Amazon RDS Data API events by containing `kms.amazonaws.com` or `rdsdata.amazonaws.com` . By default, `ExcludeManagementEventSources` is empty, and KMS and Amazon RDS Data API events are logged to your trail. You can exclude management event sources only in Regions that support the event source.

(string)

JSON Syntax:

```
[
  {
    "ReadWriteType": "ReadOnly"|"WriteOnly"|"All",
    "IncludeManagementEvents": true|false,
    "DataResources": [
      {
        "Type": "string",
        "Values": ["string", ...]
      }
      ...
    ],
    "ExcludeManagementEventSources": ["string", ...]
  }
  ...
]
```

`--advanced-event-selectors` (list)

Specifies the settings for advanced event selectors. You can use advanced event selectors to log management events, data events for all resource types, and network activity events.

You can add advanced event selectors, and conditions for your advanced event selectors, up to a maximum of 500 values for all conditions and selectors on a trail. You can use either `AdvancedEventSelectors` or `EventSelectors` , but not both. If you apply `AdvancedEventSelectors` to a trail, any existing `EventSelectors` are overwritten. For more information about advanced event selectors, see [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) and [Logging network activity events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-network-events-with-cloudtrail.html) in the *CloudTrail User Guide* .

(structure)

Advanced event selectors let you create fine-grained selectors for CloudTrail management, data, and network activity events. They help you control costs by logging only those events that are important to you. For more information about configuring advanced event selectors, see the [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) , [Logging network activity events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-network-events-with-cloudtrail.html) , and [Logging management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html) topics in the *CloudTrail User Guide* .

You cannot apply both event selectors and advanced event selectors to a trail.

For information about configurable advanced event selector fields, see [AdvancedEventSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html) in the *CloudTrail API Reference* .

Name -> (string)

An optional, descriptive name for an advanced event selector, such as âLog data events for only two S3 bucketsâ.

FieldSelectors -> (list)

Contains all selector statements in an advanced event selector.

(structure)

A single selector statement in an advanced event selector.

Field -> (string)

A field in a CloudTrail event record on which to filter events to be logged. For event data stores for CloudTrail Insights events, Config configuration items, Audit Manager evidence, or events outside of Amazon Web Services, the field is used only for selecting events as filtering is not supported.

For more information, see [AdvancedFieldSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.html) in the *CloudTrail API Reference* .

### Note

Selectors donât support the use of wildcards like `*` . To match multiple values with a single condition, you may use `StartsWith` , `EndsWith` , `NotStartsWith` , or `NotEndsWith` to explicitly match the beginning or end of the event field.

Equals -> (list)

An operator that includes events that match the exact value of the event record field specified as the value of `Field` . This is the only valid operator that you can use with the `readOnly` , `eventCategory` , and `resources.type` fields.

(string)

StartsWith -> (list)

An operator that includes events that match the first few characters of the event record field specified as the value of `Field` .

(string)

EndsWith -> (list)

An operator that includes events that match the last few characters of the event record field specified as the value of `Field` .

(string)

NotEquals -> (list)

An operator that excludes events that match the exact value of the event record field specified as the value of `Field` .

(string)

NotStartsWith -> (list)

An operator that excludes events that match the first few characters of the event record field specified as the value of `Field` .

(string)

NotEndsWith -> (list)

An operator that excludes events that match the last few characters of the event record field specified as the value of `Field` .

(string)

JSON Syntax:

```
[
  {
    "Name": "string",
    "FieldSelectors": [
      {
        "Field": "string",
        "Equals": ["string", ...],
        "StartsWith": ["string", ...],
        "EndsWith": ["string", ...],
        "NotEquals": ["string", ...],
        "NotStartsWith": ["string", ...],
        "NotEndsWith": ["string", ...]
      }
      ...
    ]
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

**Example 1: Configure a trail to log management events and data events by using advanced event selectors**

You can add advanced event selectors, and conditions for your advanced event selectors, up to a maximum of 500 values for all conditions and selectors on a trail. You can use advanced event selectors to log all available data event types. You can use either advanced event selectors or basic event selectors, but not both. If you apply advanced event selectors to a trail, any existing basic event selectors are overwritten.

The following `put-event-selectors` example creates an advanced event selector for a trail named `myTrail` to log all management events, log S3 PutObject and DeleteObject API calls for all but one S3 bucket, log data API calls for a Lambda function named `myFunction`, and log Publish API calls on an SNS topic named `myTopic`.

```
aws cloudtrail put-event-selectors \
    --trail-name myTrail \
    --advanced-event-selectors '[{"Name": "Log all management events", "FieldSelectors": [{ "Field": "eventCategory", "Equals": ["Management"] }] },{"Name": "Log PutObject and DeleteObject events for all but one bucket","FieldSelectors": [{ "Field": "eventCategory", "Equals": ["Data"] },{ "Field": "resources.type", "Equals": ["AWS::S3::Object"] },{ "Field": "eventName", "Equals": ["PutObject","DeleteObject"] },{ "Field": "resources.ARN", "NotStartsWith": ["arn:aws:s3:::amzn-s3-demo-bucket/"] }]},{"Name": "Log data events for a specific Lambda function","FieldSelectors": [{ "Field": "eventCategory", "Equals": ["Data"] },{ "Field": "resources.type", "Equals": ["AWS::Lambda::Function"] },{ "Field": "resources.ARN", "Equals": ["arn:aws:lambda:us-east-1:123456789012:function:myFunction"] }]},{"Name": "Log all Publish API calls on a specific SNS topic","FieldSelectors": [{ "Field": "eventCategory", "Equals": ["Data"] },{ "Field": "resources.type", "Equals": ["AWS::SNS::Topic"] },{ "Field": "eventName", "Equals": ["Publish"] },{ "Field": "resources.ARN", "Equals": ["arn:aws:sns:us-east-1:123456789012:myTopic.fifo"] }]}]'
```

Output:

```
{
    "TrailARN": "arn:aws:cloudtrail:us-east-1:123456789012:trail/myTrail",
    "AdvancedEventSelectors": [
        {
            "Name": "Log all management events",
            "FieldSelectors": [
                {
                    "Field": "eventCategory",
                    "Equals": [
                        "Management"
                    ]
                }
            ]
        },
        {
            "Name": "Log PutObject and DeleteObject events for all but one bucket",
            "FieldSelectors": [
                {
                    "Field": "eventCategory",
                    "Equals": [
                        "Data"
                    ]
                },
                {
                    "Field": "resources.type",
                    "Equals": [
                        "AWS::S3::Object"
                    ]
                },
                {
                    "Field": "eventName",
                    "Equals": [
                        "PutObject",
                        "DeleteObject"
                    ]
                },
                {
                    "Field": "resources.ARN",
                    "NotStartsWith": [
                        "arn:aws:s3:::amzn-s3-demo-bucket/"
                    ]
                }
            ]
        },
        {
            "Name": "Log data events for a specific Lambda function",
            "FieldSelectors": [
                {
                    "Field": "eventCategory",
                    "Equals": [
                        "Data"
                    ]
                },
                {
                    "Field": "resources.type",
                    "Equals": [
                        "AWS::Lambda::Function"
                    ]
                },
                {
                    "Field": "resources.ARN",
                    "Equals": [
                        "arn:aws:lambda:us-east-1:123456789012:function:myFunction"
                    ]
                }
            ]
        },
        {
            "Name": "Log all Publish API calls on a specific SNS topic",
            "FieldSelectors": [
                {
                    "Field": "eventCategory",
                    "Equals": [
                        "Data"
                    ]
                },
                {
                    "Field": "resources.type",
                    "Equals": [
                        "AWS::SNS::Topic"
                    ]
                },
                {
                    "Field": "eventName",
                    "Equals": [
                        "Publish"
                    ]
                },
                {
                    "Field": "resources.ARN",
                    "Equals": [
                        "arn:aws:sns:us-east-1:123456789012:myTopic.fifo"
                    ]
                }
            ]
        }
    ]
}
```

For more information, see [Log events by using advanced event selectors](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-advanced) in the *AWS CloudTrail User Guide*.

**Example 2: Configure event selectors for a trail to log all management events and data events**

You can configure up to 5 event selectors for a trail and up to 250 data resources for a trail. Event selectors are also referred to as basic event selectors. You can use event selectors to log management events and data events for S3 objects, Lambda functions, and DynnamoDB tables. To log data events for other resource types, you must use advanced event selectors.

The following `put-event-selectors` example creates an event selector for a trail named `TrailName` to include all management events, data events for two Amazon S3 bucket/prefix combinations, and data events for a single AWS Lambda function named `hello-world-python-function`.

```
aws cloudtrail put-event-selectors \
    --trail-name TrailName \
    --event-selectors '[{"ReadWriteType": "All","IncludeManagementEvents": true,"DataResources": [{"Type":"AWS::S3::Object", "Values": ["arn:aws:s3:::amzn-s3-demo-bucket/prefix","arn:aws:s3:::amzn-s3-demo-bucket2/prefix2"]},{"Type": "AWS::Lambda::Function","Values": ["arn:aws:lambda:us-west-2:999999999999:function:hello-world-python-function"]}]}]'
```

Output:

```
{
    "EventSelectors": [
        {
            "IncludeManagementEvents": true,
            "DataResources": [
                {
                    "Values": [
                        "arn:aws:s3:::amzn-s3-demo-bucket/prefix",
                        "arn:aws:s3:::amzn-s3-demo-bucket2/prefix2"
                    ],
                    "Type": "AWS::S3::Object"
                },
                {
                    "Values": [
                        "arn:aws:lambda:us-west-2:123456789012:function:hello-world-python-function"
                    ],
                    "Type": "AWS::Lambda::Function"
                },
            ],
            "ReadWriteType": "All"
        }
    ],
    "TrailARN": "arn:aws:cloudtrail:us-east-2:123456789012:trail/TrailName"
}
```

For more information, see [Log events by using basic event selectors](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-basic) in the *AWS CloudTrail User Guide*.

**Example 3: Configure event selectors for a trail to log management events, all S3 data events on S3 objects, and all Lambda data events on functions in your account**

The following `put-event-selectors` example creates an event selector for a trail named `TrailName2` that includes all management events, and all data events for all Amazon S3 buckets and AWS Lambda functions in the AWS account.

```
aws cloudtrail put-event-selectors \
    --trail-name TrailName2 \
    --event-selectors '[{"ReadWriteType": "All","IncludeManagementEvents": true,"DataResources": [{"Type":"AWS::S3::Object", "Values": ["arn:aws:s3"]},{"Type": "AWS::Lambda::Function","Values": ["arn:aws:lambda"]}]}]'
```

Output:

```
{
    "EventSelectors": [
        {
            "IncludeManagementEvents": true,
            "DataResources": [
                {
                    "Values": [
                        "arn:aws:s3"
                    ],
                    "Type": "AWS::S3::Object"
                },
                {
                    "Values": [
                        "arn:aws:lambda"
                    ],
                    "Type": "AWS::Lambda::Function"
                },
            ],
            "ReadWriteType": "All"
        }
    ],
    "TrailARN": "arn:aws:cloudtrail:us-east-2:123456789012:trail/TrailName2"
}
```

For more information, see [Log events by using basic event selectors](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-basic) in the *AWS CloudTrail User Guide*.

## Output

TrailARN -> (string)

Specifies the ARN of the trail that was updated with event selectors. The following is the format of a trail ARN.

`arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`

EventSelectors -> (list)

Specifies the event selectors configured for your trail.

(structure)

Use event selectors to further specify the management and data event settings for your trail. By default, trails created without specific event selectors will be configured to log all read and write management events, and no data events. When an event occurs in your account, CloudTrail evaluates the event selector for all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesnât match any event selector, the trail doesnât log the event.

You can configure up to five event selectors for a trail.

You cannot apply both event selectors and advanced event selectors to a trail.

ReadWriteType -> (string)

Specify if you want your trail to log read-only events, write-only events, or all. For example, the EC2 `GetConsoleOutput` is a read-only API operation and `RunInstances` is a write-only API operation.

By default, the value is `All` .

IncludeManagementEvents -> (boolean)

Specify if you want your event selector to include management events for your trail.

For more information, see [Management Events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html) in the *CloudTrail User Guide* .

By default, the value is `true` .

The first copy of management events is free. You are charged for additional copies of management events that you are logging on any subsequent trail in the same Region. For more information about CloudTrail pricing, see [CloudTrail Pricing](http://aws.amazon.com/cloudtrail/pricing/) .

DataResources -> (list)

CloudTrail supports data event logging for Amazon S3 objects in standard S3 buckets, Lambda functions, and Amazon DynamoDB tables with basic event selectors. You can specify up to 250 resources for an individual event selector, but the total number of data resources cannot exceed 250 across all event selectors in a trail. This limit does not apply if you configure resource logging for all data events.

For more information, see [Data Events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) and [Limits in CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html) in the *CloudTrail User Guide* .

### Note

To log data events for all other resource types including objects stored in [directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html) , you must use [AdvancedEventSelectors](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html) . You must also use `AdvancedEventSelectors` if you want to filter on the `eventName` field.

(structure)

You can configure the `DataResource` in an `EventSelector` to log data events for the following three resource types:

- `AWS::DynamoDB::Table`
- `AWS::Lambda::Function`
- `AWS::S3::Object`

To log data events for all other resource types including objects stored in [directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html) , you must use [AdvancedEventSelectors](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html) . You must also use `AdvancedEventSelectors` if you want to filter on the `eventName` field.

Configure the `DataResource` to specify the resource type and resource ARNs for which you want to log data events.

### Note

The total number of allowed data resources is 250. This number can be distributed between 1 and 5 event selectors, but the total cannot exceed 250 across all selectors for the trail.

The following example demonstrates how logging works when you configure logging of all data events for a general purpose bucket named `amzn-s3-demo-bucket1` . In this example, the CloudTrail user specified an empty prefix, and the option to log both `Read` and `Write` data events.

- A user uploads an image file to `amzn-s3-demo-bucket1` .
- The `PutObject` API operation is an Amazon S3 object-level API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified an S3 bucket with an empty prefix, events that occur on any object in that bucket are logged. The trail processes and logs the event.
- A user uploads an object to an Amazon S3 bucket named `arn:aws:s3:::amzn-s3-demo-bucket1` .
- The `PutObject` API operation occurred for an object in an S3 bucket that the CloudTrail user didnât specify for the trail. The trail doesnât log the event.

The following example demonstrates how logging works when you configure logging of Lambda data events for a Lambda function named *MyLambdaFunction* , but not for all Lambda functions.

- A user runs a script that includes a call to the *MyLambdaFunction* function and the *MyOtherLambdaFunction* function.
- The `Invoke` API operation on *MyLambdaFunction* is an Lambda API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified logging data events for *MyLambdaFunction* , any invocations of that function are logged. The trail processes and logs the event.
- The `Invoke` API operation on *MyOtherLambdaFunction* is an Lambda API. Because the CloudTrail user did not specify logging data events for all Lambda functions, the `Invoke` operation for *MyOtherLambdaFunction* does not match the function specified for the trail. The trail doesnât log the event.

Type -> (string)

The resource type in which you want to log data events. You can specify the following *basic* event selector resource types:

- `AWS::DynamoDB::Table`
- `AWS::Lambda::Function`
- `AWS::S3::Object`

Additional resource types are available through *advanced* event selectors. For more information, see [AdvancedEventSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html) .

Values -> (list)

An array of Amazon Resource Name (ARN) strings or partial ARN strings for the specified resource type.

- To log data events for all objects in all S3 buckets in your Amazon Web Services account, specify the prefix as `arn:aws:s3` .

### Note

This also enables logging of data event activity performed by any user or role in your Amazon Web Services account, even if that activity is performed on a bucket that belongs to another Amazon Web Services account.

- To log data events for all objects in an S3 bucket, specify the bucket and an empty object prefix such as `arn:aws:s3:::amzn-s3-demo-bucket1/` . The trail logs data events for all objects in this S3 bucket.
- To log data events for specific objects, specify the S3 bucket and object prefix such as `arn:aws:s3:::amzn-s3-demo-bucket1/example-images` . The trail logs data events for objects in this S3 bucket that match the prefix.
- To log data events for all Lambda functions in your Amazon Web Services account, specify the prefix as `arn:aws:lambda` .

### Note

This also enables logging of `Invoke` activity performed by any user or role in your Amazon Web Services account, even if that activity is performed on a function that belongs to another Amazon Web Services account.

- To log data events for a specific Lambda function, specify the function ARN.

### Note

Lambda function ARNs are exact. For example, if you specify a function ARN *arn:aws:lambda:us-west-2:111111111111:function:helloworld* , data events will only be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld* . They will not be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld2* .

- To log data events for all DynamoDB tables in your Amazon Web Services account, specify the prefix as `arn:aws:dynamodb` .

(string)

ExcludeManagementEventSources -> (list)

An optional list of service event sources from which you do not want management events to be logged on your trail. In this release, the list can be empty (disables the filter), or it can filter out Key Management Service or Amazon RDS Data API events by containing `kms.amazonaws.com` or `rdsdata.amazonaws.com` . By default, `ExcludeManagementEventSources` is empty, and KMS and Amazon RDS Data API events are logged to your trail. You can exclude management event sources only in Regions that support the event source.

(string)

AdvancedEventSelectors -> (list)

Specifies the advanced event selectors configured for your trail.

(structure)

Advanced event selectors let you create fine-grained selectors for CloudTrail management, data, and network activity events. They help you control costs by logging only those events that are important to you. For more information about configuring advanced event selectors, see the [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) , [Logging network activity events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-network-events-with-cloudtrail.html) , and [Logging management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html) topics in the *CloudTrail User Guide* .

You cannot apply both event selectors and advanced event selectors to a trail.

For information about configurable advanced event selector fields, see [AdvancedEventSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html) in the *CloudTrail API Reference* .

Name -> (string)

An optional, descriptive name for an advanced event selector, such as âLog data events for only two S3 bucketsâ.

FieldSelectors -> (list)

Contains all selector statements in an advanced event selector.

(structure)

A single selector statement in an advanced event selector.

Field -> (string)

A field in a CloudTrail event record on which to filter events to be logged. For event data stores for CloudTrail Insights events, Config configuration items, Audit Manager evidence, or events outside of Amazon Web Services, the field is used only for selecting events as filtering is not supported.

For more information, see [AdvancedFieldSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.html) in the *CloudTrail API Reference* .

### Note

Selectors donât support the use of wildcards like `*` . To match multiple values with a single condition, you may use `StartsWith` , `EndsWith` , `NotStartsWith` , or `NotEndsWith` to explicitly match the beginning or end of the event field.

Equals -> (list)

An operator that includes events that match the exact value of the event record field specified as the value of `Field` . This is the only valid operator that you can use with the `readOnly` , `eventCategory` , and `resources.type` fields.

(string)

StartsWith -> (list)

An operator that includes events that match the first few characters of the event record field specified as the value of `Field` .

(string)

EndsWith -> (list)

An operator that includes events that match the last few characters of the event record field specified as the value of `Field` .

(string)

NotEquals -> (list)

An operator that excludes events that match the exact value of the event record field specified as the value of `Field` .

(string)

NotStartsWith -> (list)

An operator that excludes events that match the first few characters of the event record field specified as the value of `Field` .

(string)

NotEndsWith -> (list)

An operator that excludes events that match the last few characters of the event record field specified as the value of `Field` .

(string)