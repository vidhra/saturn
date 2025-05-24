# put-integrationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/put-integration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/put-integration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [customer-profiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/index.html#cli-aws-customer-profiles) ]

# put-integration

## Description

Adds an integration between the service and a third-party service, which includes Amazon AppFlow and Amazon Connect.

An integration can belong to only one domain.

To add or remove tags on an existing Integration, see [TagResource](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_TagResource.html) /[UntagResource](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UntagResource.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/customer-profiles-2020-08-15/PutIntegration)

## Synopsis

```
put-integration
--domain-name <value>
[--uri <value>]
[--object-type-name <value>]
[--tags <value>]
[--flow-definition <value>]
[--object-type-names <value>]
[--role-arn <value>]
[--event-trigger-names <value>]
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

`--domain-name` (string)

The unique name of the domain.

`--uri` (string)

The URI of the S3 bucket or any other type of data source.

`--object-type-name` (string)

The name of the profile object type.

`--tags` (map)

The tags used to organize, track, or control access for this resource.

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

`--flow-definition` (structure)

The configuration that controls how Customer Profiles retrieves data from the source.

Description -> (string)

A description of the flow you want to create.

FlowName -> (string)

The specified name of the flow. Use underscores (_) or hyphens (-) only. Spaces are not allowed.

KmsArn -> (string)

The Amazon Resource Name of the AWS Key Management Service (KMS) key you provide for encryption.

SourceFlowConfig -> (structure)

The configuration that controls how Customer Profiles retrieves data from the source.

ConnectorProfileName -> (string)

The name of the AppFlow connector profile. This name must be unique for each connector profile in the AWS account.

ConnectorType -> (string)

The type of connector, such as Salesforce, Marketo, and so on.

IncrementalPullConfig -> (structure)

Defines the configuration for a scheduled incremental data pull. If a valid configuration is provided, the fields specified in the configuration are used when querying for the incremental data pull.

DatetimeTypeFieldName -> (string)

A field that specifies the date time or timestamp field as the criteria to use when importing incremental records from the source.

SourceConnectorProperties -> (structure)

Specifies the information that is required to query a particular source connector.

Marketo -> (structure)

The properties that are applied when Marketo is being used as a source.

Object -> (string)

The object specified in the Marketo flow source.

S3 -> (structure)

The properties that are applied when Amazon S3 is being used as the flow source.

BucketName -> (string)

The Amazon S3 bucket name where the source files are stored.

BucketPrefix -> (string)

The object key for the Amazon S3 bucket in which the source files are stored.

Salesforce -> (structure)

The properties that are applied when Salesforce is being used as a source.

Object -> (string)

The object specified in the Salesforce flow source.

EnableDynamicFieldUpdate -> (boolean)

The flag that enables dynamic fetching of new (recently added) fields in the Salesforce objects while running a flow.

IncludeDeletedRecords -> (boolean)

Indicates whether Amazon AppFlow includes deleted files in the flow run.

ServiceNow -> (structure)

The properties that are applied when ServiceNow is being used as a source.

Object -> (string)

The object specified in the ServiceNow flow source.

Zendesk -> (structure)

The properties that are applied when using Zendesk as a flow source.

Object -> (string)

The object specified in the Zendesk flow source.

Tasks -> (list)

A list of tasks that Customer Profiles performs while transferring the data in the flow run.

(structure)

A class for modeling different type of tasks. Task implementation varies based on the TaskType.

ConnectorOperator -> (structure)

The operation to be performed on the provided source fields.

Marketo -> (string)

The operation to be performed on the provided Marketo source fields.

S3 -> (string)

The operation to be performed on the provided Amazon S3 source fields.

Salesforce -> (string)

The operation to be performed on the provided Salesforce source fields.

ServiceNow -> (string)

The operation to be performed on the provided ServiceNow source fields.

Zendesk -> (string)

The operation to be performed on the provided Zendesk source fields.

DestinationField -> (string)

A field in a destination connector, or a field value against which Amazon AppFlow validates a source field.

SourceFields -> (list)

The source fields to which a particular task is applied.

(string)

TaskProperties -> (map)

A map used to store task-related information. The service looks for particular information based on the TaskType.

key -> (string)

value -> (string)

TaskType -> (string)

Specifies the particular task implementation that Amazon AppFlow performs.

TriggerConfig -> (structure)

The trigger settings that determine how and when the flow runs.

TriggerType -> (string)

Specifies the type of flow trigger. It can be OnDemand, Scheduled, or Event.

TriggerProperties -> (structure)

Specifies the configuration details of a schedule-triggered flow that you define. Currently, these settings only apply to the Scheduled trigger type.

Scheduled -> (structure)

Specifies the configuration details of a schedule-triggered flow that you define.

ScheduleExpression -> (string)

The scheduling expression that determines the rate at which the schedule will run, for example rate (5 minutes).

DataPullMode -> (string)

Specifies whether a scheduled flow has an incremental data transfer or a complete data transfer for each flow run.

ScheduleStartTime -> (timestamp)

Specifies the scheduled start time for a scheduled-trigger flow.

ScheduleEndTime -> (timestamp)

Specifies the scheduled end time for a scheduled-trigger flow.

Timezone -> (string)

Specifies the time zone used when referring to the date and time of a scheduled-triggered flow, such as America/New_York.

ScheduleOffset -> (long)

Specifies the optional offset that is added to the time interval for a schedule-triggered flow.

FirstExecutionFrom -> (timestamp)

Specifies the date range for the records to import from the connector in the first flow run.

JSON Syntax:

```
{
  "Description": "string",
  "FlowName": "string",
  "KmsArn": "string",
  "SourceFlowConfig": {
    "ConnectorProfileName": "string",
    "ConnectorType": "Salesforce"|"Marketo"|"Zendesk"|"Servicenow"|"S3",
    "IncrementalPullConfig": {
      "DatetimeTypeFieldName": "string"
    },
    "SourceConnectorProperties": {
      "Marketo": {
        "Object": "string"
      },
      "S3": {
        "BucketName": "string",
        "BucketPrefix": "string"
      },
      "Salesforce": {
        "Object": "string",
        "EnableDynamicFieldUpdate": true|false,
        "IncludeDeletedRecords": true|false
      },
      "ServiceNow": {
        "Object": "string"
      },
      "Zendesk": {
        "Object": "string"
      }
    }
  },
  "Tasks": [
    {
      "ConnectorOperator": {
        "Marketo": "PROJECTION"|"LESS_THAN"|"GREATER_THAN"|"BETWEEN"|"ADDITION"|"MULTIPLICATION"|"DIVISION"|"SUBTRACTION"|"MASK_ALL"|"MASK_FIRST_N"|"MASK_LAST_N"|"VALIDATE_NON_NULL"|"VALIDATE_NON_ZERO"|"VALIDATE_NON_NEGATIVE"|"VALIDATE_NUMERIC"|"NO_OP",
        "S3": "PROJECTION"|"LESS_THAN"|"GREATER_THAN"|"BETWEEN"|"LESS_THAN_OR_EQUAL_TO"|"GREATER_THAN_OR_EQUAL_TO"|"EQUAL_TO"|"NOT_EQUAL_TO"|"ADDITION"|"MULTIPLICATION"|"DIVISION"|"SUBTRACTION"|"MASK_ALL"|"MASK_FIRST_N"|"MASK_LAST_N"|"VALIDATE_NON_NULL"|"VALIDATE_NON_ZERO"|"VALIDATE_NON_NEGATIVE"|"VALIDATE_NUMERIC"|"NO_OP",
        "Salesforce": "PROJECTION"|"LESS_THAN"|"CONTAINS"|"GREATER_THAN"|"BETWEEN"|"LESS_THAN_OR_EQUAL_TO"|"GREATER_THAN_OR_EQUAL_TO"|"EQUAL_TO"|"NOT_EQUAL_TO"|"ADDITION"|"MULTIPLICATION"|"DIVISION"|"SUBTRACTION"|"MASK_ALL"|"MASK_FIRST_N"|"MASK_LAST_N"|"VALIDATE_NON_NULL"|"VALIDATE_NON_ZERO"|"VALIDATE_NON_NEGATIVE"|"VALIDATE_NUMERIC"|"NO_OP",
        "ServiceNow": "PROJECTION"|"CONTAINS"|"LESS_THAN"|"GREATER_THAN"|"BETWEEN"|"LESS_THAN_OR_EQUAL_TO"|"GREATER_THAN_OR_EQUAL_TO"|"EQUAL_TO"|"NOT_EQUAL_TO"|"ADDITION"|"MULTIPLICATION"|"DIVISION"|"SUBTRACTION"|"MASK_ALL"|"MASK_FIRST_N"|"MASK_LAST_N"|"VALIDATE_NON_NULL"|"VALIDATE_NON_ZERO"|"VALIDATE_NON_NEGATIVE"|"VALIDATE_NUMERIC"|"NO_OP",
        "Zendesk": "PROJECTION"|"GREATER_THAN"|"ADDITION"|"MULTIPLICATION"|"DIVISION"|"SUBTRACTION"|"MASK_ALL"|"MASK_FIRST_N"|"MASK_LAST_N"|"VALIDATE_NON_NULL"|"VALIDATE_NON_ZERO"|"VALIDATE_NON_NEGATIVE"|"VALIDATE_NUMERIC"|"NO_OP"
      },
      "DestinationField": "string",
      "SourceFields": ["string", ...],
      "TaskProperties": {"VALUE"|"VALUES"|"DATA_TYPE"|"UPPER_BOUND"|"LOWER_BOUND"|"SOURCE_DATA_TYPE"|"DESTINATION_DATA_TYPE"|"VALIDATION_ACTION"|"MASK_VALUE"|"MASK_LENGTH"|"TRUNCATE_LENGTH"|"MATH_OPERATION_FIELDS_ORDER"|"CONCAT_FORMAT"|"SUBFIELD_CATEGORY_MAP": "string"
        ...},
      "TaskType": "Arithmetic"|"Filter"|"Map"|"Mask"|"Merge"|"Truncate"|"Validate"
    }
    ...
  ],
  "TriggerConfig": {
    "TriggerType": "Scheduled"|"Event"|"OnDemand",
    "TriggerProperties": {
      "Scheduled": {
        "ScheduleExpression": "string",
        "DataPullMode": "Incremental"|"Complete",
        "ScheduleStartTime": timestamp,
        "ScheduleEndTime": timestamp,
        "Timezone": "string",
        "ScheduleOffset": long,
        "FirstExecutionFrom": timestamp
      }
    }
  }
}
```

`--object-type-names` (map)

A map in which each key is an event type from an external application such as Segment or Shopify, and each value is an `ObjectTypeName` (template) used to ingest the event. It supports the following event types: `SegmentIdentify` , `ShopifyCreateCustomers` , `ShopifyUpdateCustomers` , `ShopifyCreateDraftOrders` , `ShopifyUpdateDraftOrders` , `ShopifyCreateOrders` , and `ShopifyUpdatedOrders` .

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

`--role-arn` (string)

The Amazon Resource Name (ARN) of the IAM role. The Integration uses this role to make Customer Profiles requests on your behalf.

`--event-trigger-names` (list)

A list of unique names for active event triggers associated with the integration.

(string)

Syntax:

```
"string" "string" ...
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

DomainName -> (string)

The unique name of the domain.

Uri -> (string)

The URI of the S3 bucket or any other type of data source.

ObjectTypeName -> (string)

The name of the profile object type.

CreatedAt -> (timestamp)

The timestamp of when the domain was created.

LastUpdatedAt -> (timestamp)

The timestamp of when the domain was most recently edited.

Tags -> (map)

The tags used to organize, track, or control access for this resource.

key -> (string)

value -> (string)

ObjectTypeNames -> (map)

A map in which each key is an event type from an external application such as Segment or Shopify, and each value is an `ObjectTypeName` (template) used to ingest the event. It supports the following event types: `SegmentIdentify` , `ShopifyCreateCustomers` , `ShopifyUpdateCustomers` , `ShopifyCreateDraftOrders` , `ShopifyUpdateDraftOrders` , `ShopifyCreateOrders` , and `ShopifyUpdatedOrders` .

key -> (string)

value -> (string)

WorkflowId -> (string)

Unique identifier for the workflow.

IsUnstructured -> (boolean)

Boolean that shows if the Flow thatâs associated with the Integration is created in Amazon Appflow, or with ObjectTypeName equals _unstructured via API/CLI in flowDefinition.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role. The Integration uses this role to make Customer Profiles requests on your behalf.

EventTriggerNames -> (list)

A list of unique names for active event triggers associated with the integration. This list would be empty if no Event Trigger is associated with the integration.

(string)