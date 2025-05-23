# create-flowÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/create-flow.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/create-flow.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appflow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/index.html#cli-aws-appflow) ]

# create-flow

## Description

Enables your application to create a new flow using Amazon AppFlow. You must create a connector profile before calling this API. Please note that the Request Syntax below shows syntax for multiple destinations, however, you can only transfer data to one item in this list at a time. Amazon AppFlow does not currently support flows to multiple destinations at once.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appflow-2020-08-23/CreateFlow)

## Synopsis

```
create-flow
--flow-name <value>
[--description <value>]
[--kms-arn <value>]
--trigger-config <value>
--source-flow-config <value>
--destination-flow-config-list <value>
--tasks <value>
[--tags <value>]
[--metadata-catalog-config <value>]
[--client-token <value>]
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

`--flow-name` (string)

The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only.

`--description` (string)

A description of the flow you want to create.

`--kms-arn` (string)

The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you donât provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key.

`--trigger-config` (structure)

The trigger settings that determine how and when the flow runs.

triggerType -> (string)

Specifies the type of flow trigger. This can be `OnDemand` , `Scheduled` , or `Event` .

triggerProperties -> (structure)

Specifies the configuration details of a schedule-triggered flow as defined by the user. Currently, these settings only apply to the `Scheduled` trigger type.

Scheduled -> (structure)

Specifies the configuration details of a schedule-triggered flow as defined by the user.

scheduleExpression -> (string)

The scheduling expression that determines the rate at which the schedule will run, for example `rate(5minutes)` .

dataPullMode -> (string)

Specifies whether a scheduled flow has an incremental data transfer or a complete data transfer for each flow run.

scheduleStartTime -> (timestamp)

The time at which the scheduled flow starts. The time is formatted as a timestamp that follows the ISO 8601 standard, such as `2022-04-26T13:00:00-07:00` .

scheduleEndTime -> (timestamp)

The time at which the scheduled flow ends. The time is formatted as a timestamp that follows the ISO 8601 standard, such as `2022-04-27T13:00:00-07:00` .

timezone -> (string)

Specifies the time zone used when referring to the dates and times of a scheduled flow, such as `America/New_York` . This time zone is only a descriptive label. It doesnât affect how Amazon AppFlow interprets the timestamps that you specify to schedule the flow.

If you want to schedule a flow by using times in a particular time zone, indicate the time zone as a UTC offset in your timestamps. For example, the UTC offsets for the `America/New_York` timezone are `-04:00` EDT and `-05:00 EST` .

scheduleOffset -> (long)

Specifies the optional offset that is added to the time interval for a schedule-triggered flow.

firstExecutionFrom -> (timestamp)

Specifies the date range for the records to import from the connector in the first flow run.

flowErrorDeactivationThreshold -> (integer)

Defines how many times a scheduled flow fails consecutively before Amazon AppFlow deactivates it.

Shorthand Syntax:

```
triggerType=string,triggerProperties={Scheduled={scheduleExpression=string,dataPullMode=string,scheduleStartTime=timestamp,scheduleEndTime=timestamp,timezone=string,scheduleOffset=long,firstExecutionFrom=timestamp,flowErrorDeactivationThreshold=integer}}
```

JSON Syntax:

```
{
  "triggerType": "Scheduled"|"Event"|"OnDemand",
  "triggerProperties": {
    "Scheduled": {
      "scheduleExpression": "string",
      "dataPullMode": "Incremental"|"Complete",
      "scheduleStartTime": timestamp,
      "scheduleEndTime": timestamp,
      "timezone": "string",
      "scheduleOffset": long,
      "firstExecutionFrom": timestamp,
      "flowErrorDeactivationThreshold": integer
    }
  }
}
```

`--source-flow-config` (structure)

The configuration that controls how Amazon AppFlow retrieves data from the source connector.

connectorType -> (string)

The type of connector, such as Salesforce, Amplitude, and so on.

apiVersion -> (string)

The API version of the connector when itâs used as a source in the flow.

connectorProfileName -> (string)

The name of the connector profile. This name must be unique for each connector profile in the Amazon Web Services account.

sourceConnectorProperties -> (structure)

Specifies the information that is required to query a particular source connector.

Amplitude -> (structure)

Specifies the information that is required for querying Amplitude.

object -> (string)

The object specified in the Amplitude flow source.

Datadog -> (structure)

Specifies the information that is required for querying Datadog.

object -> (string)

The object specified in the Datadog flow source.

Dynatrace -> (structure)

Specifies the information that is required for querying Dynatrace.

object -> (string)

The object specified in the Dynatrace flow source.

GoogleAnalytics -> (structure)

Specifies the information that is required for querying Google Analytics.

object -> (string)

The object specified in the Google Analytics flow source.

InforNexus -> (structure)

Specifies the information that is required for querying Infor Nexus.

object -> (string)

The object specified in the Infor Nexus flow source.

Marketo -> (structure)

Specifies the information that is required for querying Marketo.

object -> (string)

The object specified in the Marketo flow source.

S3 -> (structure)

Specifies the information that is required for querying Amazon S3.

bucketName -> (string)

The Amazon S3 bucket name where the source files are stored.

bucketPrefix -> (string)

The object key for the Amazon S3 bucket in which the source files are stored.

s3InputFormatConfig -> (structure)

When you use Amazon S3 as the source, the configuration format that you provide the flow input data.

s3InputFileType -> (string)

The file type that Amazon AppFlow gets from your Amazon S3 bucket.

Salesforce -> (structure)

Specifies the information that is required for querying Salesforce.

object -> (string)

The object specified in the Salesforce flow source.

enableDynamicFieldUpdate -> (boolean)

The flag that enables dynamic fetching of new (recently added) fields in the Salesforce objects while running a flow.

includeDeletedRecords -> (boolean)

Indicates whether Amazon AppFlow includes deleted files in the flow run.

dataTransferApi -> (string)

Specifies which Salesforce API is used by Amazon AppFlow when your flow transfers data from Salesforce.

AUTOMATIC

The default. Amazon AppFlow selects which API to use based on the number of records that your flow transfers from Salesforce. If your flow transfers fewer than 1,000,000 records, Amazon AppFlow uses Salesforce REST API. If your flow transfers 1,000,000 records or more, Amazon AppFlow uses Salesforce Bulk API 2.0.

Each of these Salesforce APIs structures data differently. If Amazon AppFlow selects the API automatically, be aware that, for recurring flows, the data output might vary from one flow run to the next. For example, if a flow runs daily, it might use REST API on one day to transfer 900,000 records, and it might use Bulk API 2.0 on the next day to transfer 1,100,000 records. For each of these flow runs, the respective Salesforce API formats the data differently. Some of the differences include how dates are formatted and null values are represented. Also, Bulk API 2.0 doesnât transfer Salesforce compound fields.

By choosing this option, you optimize flow performance for both small and large data transfers, but the tradeoff is inconsistent formatting in the output.

BULKV2

Amazon AppFlow uses only Salesforce Bulk API 2.0. This API runs asynchronous data transfers, and itâs optimal for large sets of data. By choosing this option, you ensure that your flow writes consistent output, but you optimize performance only for large data transfers.

Note that Bulk API 2.0 does not transfer Salesforce compound fields.

REST_SYNC

Amazon AppFlow uses only Salesforce REST API. By choosing this option, you ensure that your flow writes consistent output, but you decrease performance for large data transfers that are better suited for Bulk API 2.0. In some cases, if your flow attempts to transfer a vary large set of data, it might fail wituh a timed out error.

ServiceNow -> (structure)

Specifies the information that is required for querying ServiceNow.

object -> (string)

The object specified in the ServiceNow flow source.

Singular -> (structure)

Specifies the information that is required for querying Singular.

object -> (string)

The object specified in the Singular flow source.

Slack -> (structure)

Specifies the information that is required for querying Slack.

object -> (string)

The object specified in the Slack flow source.

Trendmicro -> (structure)

Specifies the information that is required for querying Trend Micro.

object -> (string)

The object specified in the Trend Micro flow source.

Veeva -> (structure)

Specifies the information that is required for querying Veeva.

object -> (string)

The object specified in the Veeva flow source.

documentType -> (string)

The document type specified in the Veeva document extract flow.

includeSourceFiles -> (boolean)

Boolean value to include source files in Veeva document extract flow.

includeRenditions -> (boolean)

Boolean value to include file renditions in Veeva document extract flow.

includeAllVersions -> (boolean)

Boolean value to include All Versions of files in Veeva document extract flow.

Zendesk -> (structure)

Specifies the information that is required for querying Zendesk.

object -> (string)

The object specified in the Zendesk flow source.

SAPOData -> (structure)

The properties that are applied when using SAPOData as a flow source.

objectPath -> (string)

The object path specified in the SAPOData flow source.

parallelismConfig -> (structure)

Sets the number of concurrent processes that transfers OData records from your SAP instance.

maxParallelism -> (integer)

The maximum number of processes that Amazon AppFlow runs at the same time when it retrieves your data from your SAP application.

paginationConfig -> (structure)

Sets the page size for each concurrent process that transfers OData records from your SAP instance.

maxPageSize -> (integer)

The maximum number of records that Amazon AppFlow receives in each page of the response from your SAP application. For transfers of OData records, the maximum page size is 3,000. For transfers of data that comes from an ODP provider, the maximum page size is 10,000.

CustomConnector -> (structure)

The properties that are applied when the custom connector is being used as a source.

entityName -> (string)

The entity specified in the custom connector as a source in the flow.

customProperties -> (map)

Custom properties that are required to use the custom connector as a source.

key -> (string)

value -> (string)

dataTransferApi -> (structure)

The API of the connector application that Amazon AppFlow uses to transfer your data.

Name -> (string)

The name of the connector application API.

Type -> (string)

You can specify one of the following types:

AUTOMATIC

The default. Optimizes a flow for datasets that fluctuate in size from small to large. For each flow run, Amazon AppFlow chooses to use the SYNC or ASYNC API type based on the amount of data that the run transfers.

SYNC

A synchronous API. This type of API optimizes a flow for small to medium-sized datasets.

ASYNC

An asynchronous API. This type of API optimizes a flow for large datasets.

Pardot -> (structure)

Specifies the information that is required for querying Salesforce Pardot.

object -> (string)

The object specified in the Salesforce Pardot flow source.

incrementalPullConfig -> (structure)

Defines the configuration for a scheduled incremental data pull. If a valid configuration is provided, the fields specified in the configuration are used when querying for the incremental data pull.

datetimeTypeFieldName -> (string)

A field that specifies the date time or timestamp field as the criteria to use when importing incremental records from the source.

JSON Syntax:

```
{
  "connectorType": "Salesforce"|"Singular"|"Slack"|"Redshift"|"S3"|"Marketo"|"Googleanalytics"|"Zendesk"|"Servicenow"|"Datadog"|"Trendmicro"|"Snowflake"|"Dynatrace"|"Infornexus"|"Amplitude"|"Veeva"|"EventBridge"|"LookoutMetrics"|"Upsolver"|"Honeycode"|"CustomerProfiles"|"SAPOData"|"CustomConnector"|"Pardot",
  "apiVersion": "string",
  "connectorProfileName": "string",
  "sourceConnectorProperties": {
    "Amplitude": {
      "object": "string"
    },
    "Datadog": {
      "object": "string"
    },
    "Dynatrace": {
      "object": "string"
    },
    "GoogleAnalytics": {
      "object": "string"
    },
    "InforNexus": {
      "object": "string"
    },
    "Marketo": {
      "object": "string"
    },
    "S3": {
      "bucketName": "string",
      "bucketPrefix": "string",
      "s3InputFormatConfig": {
        "s3InputFileType": "CSV"|"JSON"
      }
    },
    "Salesforce": {
      "object": "string",
      "enableDynamicFieldUpdate": true|false,
      "includeDeletedRecords": true|false,
      "dataTransferApi": "AUTOMATIC"|"BULKV2"|"REST_SYNC"
    },
    "ServiceNow": {
      "object": "string"
    },
    "Singular": {
      "object": "string"
    },
    "Slack": {
      "object": "string"
    },
    "Trendmicro": {
      "object": "string"
    },
    "Veeva": {
      "object": "string",
      "documentType": "string",
      "includeSourceFiles": true|false,
      "includeRenditions": true|false,
      "includeAllVersions": true|false
    },
    "Zendesk": {
      "object": "string"
    },
    "SAPOData": {
      "objectPath": "string",
      "parallelismConfig": {
        "maxParallelism": integer
      },
      "paginationConfig": {
        "maxPageSize": integer
      }
    },
    "CustomConnector": {
      "entityName": "string",
      "customProperties": {"string": "string"
        ...},
      "dataTransferApi": {
        "Name": "string",
        "Type": "SYNC"|"ASYNC"|"AUTOMATIC"
      }
    },
    "Pardot": {
      "object": "string"
    }
  },
  "incrementalPullConfig": {
    "datetimeTypeFieldName": "string"
  }
}
```

`--destination-flow-config-list` (list)

The configuration that controls how Amazon AppFlow places data in the destination connector.

(structure)

Contains information about the configuration of destination connectors present in the flow.

connectorType -> (string)

The type of connector, such as Salesforce, Amplitude, and so on.

apiVersion -> (string)

The API version that the destination connector uses.

connectorProfileName -> (string)

The name of the connector profile. This name must be unique for each connector profile in the Amazon Web Services account.

destinationConnectorProperties -> (structure)

This stores the information that is required to query a particular connector.

Redshift -> (structure)

The properties required to query Amazon Redshift.

object -> (string)

The object specified in the Amazon Redshift flow destination.

intermediateBucketName -> (string)

The intermediate bucket that Amazon AppFlow uses when moving data into Amazon Redshift.

bucketPrefix -> (string)

The object key for the bucket in which Amazon AppFlow places the destination files.

errorHandlingConfig -> (structure)

The settings that determine how Amazon AppFlow handles an error when placing data in the Amazon Redshift destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. `ErrorHandlingConfig` is a part of the destination connector details.

failOnFirstDestinationError -> (boolean)

Specifies if the flow should fail after the first instance of a failure when attempting to place data in the destination.

bucketPrefix -> (string)

Specifies the Amazon S3 bucket prefix.

bucketName -> (string)

Specifies the name of the Amazon S3 bucket.

S3 -> (structure)

The properties required to query Amazon S3.

bucketName -> (string)

The Amazon S3 bucket name in which Amazon AppFlow places the transferred data.

bucketPrefix -> (string)

The object key for the destination bucket in which Amazon AppFlow places the files.

s3OutputFormatConfig -> (structure)

The configuration that determines how Amazon AppFlow should format the flow output data when Amazon S3 is used as the destination.

fileType -> (string)

Indicates the file type that Amazon AppFlow places in the Amazon S3 bucket.

prefixConfig -> (structure)

Determines the prefix that Amazon AppFlow applies to the folder name in the Amazon S3 bucket. You can name folders according to the flow frequency and date.

prefixType -> (string)

Determines the format of the prefix, and whether it applies to the file name, file path, or both.

prefixFormat -> (string)

Determines the level of granularity for the date and time thatâs included in the prefix.

pathPrefixHierarchy -> (list)

Specifies whether the destination file path includes either or both of the following elements:

EXECUTION_ID

The ID that Amazon AppFlow assigns to the flow run.

SCHEMA_VERSION

The version number of your data schema. Amazon AppFlow assigns this version number. The version number increases by one when you change any of the following settings in your flow configuration:

- Source-to-destination field mappings
- Field data types
- Partition keys

(string)

aggregationConfig -> (structure)

The aggregation settings that you can use to customize the output format of your flow data.

aggregationType -> (string)

Specifies whether Amazon AppFlow aggregates the flow records into a single file, or leave them unaggregated.

targetFileSize -> (long)

The desired file size, in MB, for each output file that Amazon AppFlow writes to the flow destination. For each file, Amazon AppFlow attempts to achieve the size that you specify. The actual file sizes might differ from this target based on the number and size of the records that each file contains.

preserveSourceDataTyping -> (boolean)

If your file output format is Parquet, use this parameter to set whether Amazon AppFlow preserves the data types in your source data when it writes the output to Amazon S3.

- `true` : Amazon AppFlow preserves the data types when it writes to Amazon S3. For example, an integer or `1` in your source data is still an integer in your output.
- `false` : Amazon AppFlow converts all of the source data into strings when it writes to Amazon S3. For example, an integer of `1` in your source data becomes the string `"1"` in the output.

Salesforce -> (structure)

The properties required to query Salesforce.

object -> (string)

The object specified in the Salesforce flow destination.

idFieldNames -> (list)

The name of the field that Amazon AppFlow uses as an ID when performing a write operation such as update or delete.

(string)

errorHandlingConfig -> (structure)

The settings that determine how Amazon AppFlow handles an error when placing data in the Salesforce destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. `ErrorHandlingConfig` is a part of the destination connector details.

failOnFirstDestinationError -> (boolean)

Specifies if the flow should fail after the first instance of a failure when attempting to place data in the destination.

bucketPrefix -> (string)

Specifies the Amazon S3 bucket prefix.

bucketName -> (string)

Specifies the name of the Amazon S3 bucket.

writeOperationType -> (string)

This specifies the type of write operation to be performed in Salesforce. When the value is `UPSERT` , then `idFieldNames` is required.

dataTransferApi -> (string)

Specifies which Salesforce API is used by Amazon AppFlow when your flow transfers data to Salesforce.

AUTOMATIC

The default. Amazon AppFlow selects which API to use based on the number of records that your flow transfers to Salesforce. If your flow transfers fewer than 1,000 records, Amazon AppFlow uses Salesforce REST API. If your flow transfers 1,000 records or more, Amazon AppFlow uses Salesforce Bulk API 2.0.

Each of these Salesforce APIs structures data differently. If Amazon AppFlow selects the API automatically, be aware that, for recurring flows, the data output might vary from one flow run to the next. For example, if a flow runs daily, it might use REST API on one day to transfer 900 records, and it might use Bulk API 2.0 on the next day to transfer 1,100 records. For each of these flow runs, the respective Salesforce API formats the data differently. Some of the differences include how dates are formatted and null values are represented. Also, Bulk API 2.0 doesnât transfer Salesforce compound fields.

By choosing this option, you optimize flow performance for both small and large data transfers, but the tradeoff is inconsistent formatting in the output.

BULKV2

Amazon AppFlow uses only Salesforce Bulk API 2.0. This API runs asynchronous data transfers, and itâs optimal for large sets of data. By choosing this option, you ensure that your flow writes consistent output, but you optimize performance only for large data transfers.

Note that Bulk API 2.0 does not transfer Salesforce compound fields.

REST_SYNC

Amazon AppFlow uses only Salesforce REST API. By choosing this option, you ensure that your flow writes consistent output, but you decrease performance for large data transfers that are better suited for Bulk API 2.0. In some cases, if your flow attempts to transfer a vary large set of data, it might fail with a timed out error.

Snowflake -> (structure)

The properties required to query Snowflake.

object -> (string)

The object specified in the Snowflake flow destination.

intermediateBucketName -> (string)

The intermediate bucket that Amazon AppFlow uses when moving data into Snowflake.

bucketPrefix -> (string)

The object key for the destination bucket in which Amazon AppFlow places the files.

errorHandlingConfig -> (structure)

The settings that determine how Amazon AppFlow handles an error when placing data in the Snowflake destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. `ErrorHandlingConfig` is a part of the destination connector details.

failOnFirstDestinationError -> (boolean)

Specifies if the flow should fail after the first instance of a failure when attempting to place data in the destination.

bucketPrefix -> (string)

Specifies the Amazon S3 bucket prefix.

bucketName -> (string)

Specifies the name of the Amazon S3 bucket.

EventBridge -> (structure)

The properties required to query Amazon EventBridge.

object -> (string)

The object specified in the Amazon EventBridge flow destination.

errorHandlingConfig -> (structure)

The settings that determine how Amazon AppFlow handles an error when placing data in the destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. `ErrorHandlingConfig` is a part of the destination connector details.

failOnFirstDestinationError -> (boolean)

Specifies if the flow should fail after the first instance of a failure when attempting to place data in the destination.

bucketPrefix -> (string)

Specifies the Amazon S3 bucket prefix.

bucketName -> (string)

Specifies the name of the Amazon S3 bucket.

LookoutMetrics -> (structure)

The properties required to query Amazon Lookout for Metrics.

Upsolver -> (structure)

The properties required to query Upsolver.

bucketName -> (string)

The Upsolver Amazon S3 bucket name in which Amazon AppFlow places the transferred data.

bucketPrefix -> (string)

The object key for the destination Upsolver Amazon S3 bucket in which Amazon AppFlow places the files.

s3OutputFormatConfig -> (structure)

The configuration that determines how data is formatted when Upsolver is used as the flow destination.

fileType -> (string)

Indicates the file type that Amazon AppFlow places in the Upsolver Amazon S3 bucket.

prefixConfig -> (structure)

Specifies elements that Amazon AppFlow includes in the file and folder names in the flow destination.

prefixType -> (string)

Determines the format of the prefix, and whether it applies to the file name, file path, or both.

prefixFormat -> (string)

Determines the level of granularity for the date and time thatâs included in the prefix.

pathPrefixHierarchy -> (list)

Specifies whether the destination file path includes either or both of the following elements:

EXECUTION_ID

The ID that Amazon AppFlow assigns to the flow run.

SCHEMA_VERSION

The version number of your data schema. Amazon AppFlow assigns this version number. The version number increases by one when you change any of the following settings in your flow configuration:

- Source-to-destination field mappings
- Field data types
- Partition keys

(string)

aggregationConfig -> (structure)

The aggregation settings that you can use to customize the output format of your flow data.

aggregationType -> (string)

Specifies whether Amazon AppFlow aggregates the flow records into a single file, or leave them unaggregated.

targetFileSize -> (long)

The desired file size, in MB, for each output file that Amazon AppFlow writes to the flow destination. For each file, Amazon AppFlow attempts to achieve the size that you specify. The actual file sizes might differ from this target based on the number and size of the records that each file contains.

Honeycode -> (structure)

The properties required to query Amazon Honeycode.

object -> (string)

The object specified in the Amazon Honeycode flow destination.

errorHandlingConfig -> (structure)

The settings that determine how Amazon AppFlow handles an error when placing data in the destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. `ErrorHandlingConfig` is a part of the destination connector details.

failOnFirstDestinationError -> (boolean)

Specifies if the flow should fail after the first instance of a failure when attempting to place data in the destination.

bucketPrefix -> (string)

Specifies the Amazon S3 bucket prefix.

bucketName -> (string)

Specifies the name of the Amazon S3 bucket.

CustomerProfiles -> (structure)

The properties required to query Amazon Connect Customer Profiles.

domainName -> (string)

The unique name of the Amazon Connect Customer Profiles domain.

objectTypeName -> (string)

The object specified in the Amazon Connect Customer Profiles flow destination.

Zendesk -> (structure)

The properties required to query Zendesk.

object -> (string)

The object specified in the Zendesk flow destination.

idFieldNames -> (list)

A list of field names that can be used as an ID field when performing a write operation.

(string)

errorHandlingConfig -> (structure)

The settings that determine how Amazon AppFlow handles an error when placing data in the destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. `ErrorHandlingConfig` is a part of the destination connector details.

failOnFirstDestinationError -> (boolean)

Specifies if the flow should fail after the first instance of a failure when attempting to place data in the destination.

bucketPrefix -> (string)

Specifies the Amazon S3 bucket prefix.

bucketName -> (string)

Specifies the name of the Amazon S3 bucket.

writeOperationType -> (string)

The possible write operations in the destination connector. When this value is not provided, this defaults to the `INSERT` operation.

Marketo -> (structure)

The properties required to query Marketo.

object -> (string)

The object specified in the Marketo flow destination.

errorHandlingConfig -> (structure)

The settings that determine how Amazon AppFlow handles an error when placing data in the destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. `ErrorHandlingConfig` is a part of the destination connector details.

failOnFirstDestinationError -> (boolean)

Specifies if the flow should fail after the first instance of a failure when attempting to place data in the destination.

bucketPrefix -> (string)

Specifies the Amazon S3 bucket prefix.

bucketName -> (string)

Specifies the name of the Amazon S3 bucket.

CustomConnector -> (structure)

The properties that are required to query the custom Connector.

entityName -> (string)

The entity specified in the custom connector as a destination in the flow.

errorHandlingConfig -> (structure)

The settings that determine how Amazon AppFlow handles an error when placing data in the custom connector as destination.

failOnFirstDestinationError -> (boolean)

Specifies if the flow should fail after the first instance of a failure when attempting to place data in the destination.

bucketPrefix -> (string)

Specifies the Amazon S3 bucket prefix.

bucketName -> (string)

Specifies the name of the Amazon S3 bucket.

writeOperationType -> (string)

Specifies the type of write operation to be performed in the custom connector when itâs used as destination.

idFieldNames -> (list)

The name of the field that Amazon AppFlow uses as an ID when performing a write operation such as update, delete, or upsert.

(string)

customProperties -> (map)

The custom properties that are specific to the connector when itâs used as a destination in the flow.

key -> (string)

value -> (string)

SAPOData -> (structure)

The properties required to query SAPOData.

objectPath -> (string)

The object path specified in the SAPOData flow destination.

successResponseHandlingConfig -> (structure)

Determines how Amazon AppFlow handles the success response that it gets from the connector after placing data.

For example, this setting would determine where to write the response from a destination connector upon a successful insert operation.

bucketPrefix -> (string)

The Amazon S3 bucket prefix.

bucketName -> (string)

The name of the Amazon S3 bucket.

idFieldNames -> (list)

A list of field names that can be used as an ID field when performing a write operation.

(string)

errorHandlingConfig -> (structure)

The settings that determine how Amazon AppFlow handles an error when placing data in the destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. `ErrorHandlingConfig` is a part of the destination connector details.

failOnFirstDestinationError -> (boolean)

Specifies if the flow should fail after the first instance of a failure when attempting to place data in the destination.

bucketPrefix -> (string)

Specifies the Amazon S3 bucket prefix.

bucketName -> (string)

Specifies the name of the Amazon S3 bucket.

writeOperationType -> (string)

The possible write operations in the destination connector. When this value is not provided, this defaults to the `INSERT` operation.

JSON Syntax:

```
[
  {
    "connectorType": "Salesforce"|"Singular"|"Slack"|"Redshift"|"S3"|"Marketo"|"Googleanalytics"|"Zendesk"|"Servicenow"|"Datadog"|"Trendmicro"|"Snowflake"|"Dynatrace"|"Infornexus"|"Amplitude"|"Veeva"|"EventBridge"|"LookoutMetrics"|"Upsolver"|"Honeycode"|"CustomerProfiles"|"SAPOData"|"CustomConnector"|"Pardot",
    "apiVersion": "string",
    "connectorProfileName": "string",
    "destinationConnectorProperties": {
      "Redshift": {
        "object": "string",
        "intermediateBucketName": "string",
        "bucketPrefix": "string",
        "errorHandlingConfig": {
          "failOnFirstDestinationError": true|false,
          "bucketPrefix": "string",
          "bucketName": "string"
        }
      },
      "S3": {
        "bucketName": "string",
        "bucketPrefix": "string",
        "s3OutputFormatConfig": {
          "fileType": "CSV"|"JSON"|"PARQUET",
          "prefixConfig": {
            "prefixType": "FILENAME"|"PATH"|"PATH_AND_FILENAME",
            "prefixFormat": "YEAR"|"MONTH"|"DAY"|"HOUR"|"MINUTE",
            "pathPrefixHierarchy": ["EXECUTION_ID"|"SCHEMA_VERSION", ...]
          },
          "aggregationConfig": {
            "aggregationType": "None"|"SingleFile",
            "targetFileSize": long
          },
          "preserveSourceDataTyping": true|false
        }
      },
      "Salesforce": {
        "object": "string",
        "idFieldNames": ["string", ...],
        "errorHandlingConfig": {
          "failOnFirstDestinationError": true|false,
          "bucketPrefix": "string",
          "bucketName": "string"
        },
        "writeOperationType": "INSERT"|"UPSERT"|"UPDATE"|"DELETE",
        "dataTransferApi": "AUTOMATIC"|"BULKV2"|"REST_SYNC"
      },
      "Snowflake": {
        "object": "string",
        "intermediateBucketName": "string",
        "bucketPrefix": "string",
        "errorHandlingConfig": {
          "failOnFirstDestinationError": true|false,
          "bucketPrefix": "string",
          "bucketName": "string"
        }
      },
      "EventBridge": {
        "object": "string",
        "errorHandlingConfig": {
          "failOnFirstDestinationError": true|false,
          "bucketPrefix": "string",
          "bucketName": "string"
        }
      },
      "LookoutMetrics": {

      },
      "Upsolver": {
        "bucketName": "string",
        "bucketPrefix": "string",
        "s3OutputFormatConfig": {
          "fileType": "CSV"|"JSON"|"PARQUET",
          "prefixConfig": {
            "prefixType": "FILENAME"|"PATH"|"PATH_AND_FILENAME",
            "prefixFormat": "YEAR"|"MONTH"|"DAY"|"HOUR"|"MINUTE",
            "pathPrefixHierarchy": ["EXECUTION_ID"|"SCHEMA_VERSION", ...]
          },
          "aggregationConfig": {
            "aggregationType": "None"|"SingleFile",
            "targetFileSize": long
          }
        }
      },
      "Honeycode": {
        "object": "string",
        "errorHandlingConfig": {
          "failOnFirstDestinationError": true|false,
          "bucketPrefix": "string",
          "bucketName": "string"
        }
      },
      "CustomerProfiles": {
        "domainName": "string",
        "objectTypeName": "string"
      },
      "Zendesk": {
        "object": "string",
        "idFieldNames": ["string", ...],
        "errorHandlingConfig": {
          "failOnFirstDestinationError": true|false,
          "bucketPrefix": "string",
          "bucketName": "string"
        },
        "writeOperationType": "INSERT"|"UPSERT"|"UPDATE"|"DELETE"
      },
      "Marketo": {
        "object": "string",
        "errorHandlingConfig": {
          "failOnFirstDestinationError": true|false,
          "bucketPrefix": "string",
          "bucketName": "string"
        }
      },
      "CustomConnector": {
        "entityName": "string",
        "errorHandlingConfig": {
          "failOnFirstDestinationError": true|false,
          "bucketPrefix": "string",
          "bucketName": "string"
        },
        "writeOperationType": "INSERT"|"UPSERT"|"UPDATE"|"DELETE",
        "idFieldNames": ["string", ...],
        "customProperties": {"string": "string"
          ...}
      },
      "SAPOData": {
        "objectPath": "string",
        "successResponseHandlingConfig": {
          "bucketPrefix": "string",
          "bucketName": "string"
        },
        "idFieldNames": ["string", ...],
        "errorHandlingConfig": {
          "failOnFirstDestinationError": true|false,
          "bucketPrefix": "string",
          "bucketName": "string"
        },
        "writeOperationType": "INSERT"|"UPSERT"|"UPDATE"|"DELETE"
      }
    }
  }
  ...
]
```

`--tasks` (list)

A list of tasks that Amazon AppFlow performs while transferring the data in the flow run.

(structure)

A class for modeling different type of tasks. Task implementation varies based on the `TaskType` .

sourceFields -> (list)

The source fields to which a particular task is applied.

(string)

connectorOperator -> (structure)

The operation to be performed on the provided source fields.

Amplitude -> (string)

The operation to be performed on the provided Amplitude source fields.

Datadog -> (string)

The operation to be performed on the provided Datadog source fields.

Dynatrace -> (string)

The operation to be performed on the provided Dynatrace source fields.

GoogleAnalytics -> (string)

The operation to be performed on the provided Google Analytics source fields.

InforNexus -> (string)

The operation to be performed on the provided Infor Nexus source fields.

Marketo -> (string)

The operation to be performed on the provided Marketo source fields.

S3 -> (string)

The operation to be performed on the provided Amazon S3 source fields.

Salesforce -> (string)

The operation to be performed on the provided Salesforce source fields.

ServiceNow -> (string)

The operation to be performed on the provided ServiceNow source fields.

Singular -> (string)

The operation to be performed on the provided Singular source fields.

Slack -> (string)

The operation to be performed on the provided Slack source fields.

Trendmicro -> (string)

The operation to be performed on the provided Trend Micro source fields.

Veeva -> (string)

The operation to be performed on the provided Veeva source fields.

Zendesk -> (string)

The operation to be performed on the provided Zendesk source fields.

SAPOData -> (string)

The operation to be performed on the provided SAPOData source fields.

CustomConnector -> (string)

Operators supported by the custom connector.

Pardot -> (string)

The operation to be performed on the provided Salesforce Pardot source fields.

destinationField -> (string)

A field in a destination connector, or a field value against which Amazon AppFlow validates a source field.

taskType -> (string)

Specifies the particular task implementation that Amazon AppFlow performs.

taskProperties -> (map)

A map used to store task-related information. The execution service looks for particular information based on the `TaskType` .

key -> (string)

value -> (string)

Shorthand Syntax:

```
sourceFields=string,string,connectorOperator={Amplitude=string,Datadog=string,Dynatrace=string,GoogleAnalytics=string,InforNexus=string,Marketo=string,S3=string,Salesforce=string,ServiceNow=string,Singular=string,Slack=string,Trendmicro=string,Veeva=string,Zendesk=string,SAPOData=string,CustomConnector=string,Pardot=string},destinationField=string,taskType=string,taskProperties={KeyName1=string,KeyName2=string} ...
```

JSON Syntax:

```
[
  {
    "sourceFields": ["string", ...],
    "connectorOperator": {
      "Amplitude": "BETWEEN",
      "Datadog": "PROJECTION"|"BETWEEN"|"EQUAL_TO"|"ADDITION"|"MULTIPLICATION"|"DIVISION"|"SUBTRACTION"|"MASK_ALL"|"MASK_FIRST_N"|"MASK_LAST_N"|"VALIDATE_NON_NULL"|"VALIDATE_NON_ZERO"|"VALIDATE_NON_NEGATIVE"|"VALIDATE_NUMERIC"|"NO_OP",
      "Dynatrace": "PROJECTION"|"BETWEEN"|"EQUAL_TO"|"ADDITION"|"MULTIPLICATION"|"DIVISION"|"SUBTRACTION"|"MASK_ALL"|"MASK_FIRST_N"|"MASK_LAST_N"|"VALIDATE_NON_NULL"|"VALIDATE_NON_ZERO"|"VALIDATE_NON_NEGATIVE"|"VALIDATE_NUMERIC"|"NO_OP",
      "GoogleAnalytics": "PROJECTION"|"BETWEEN",
      "InforNexus": "PROJECTION"|"BETWEEN"|"EQUAL_TO"|"ADDITION"|"MULTIPLICATION"|"DIVISION"|"SUBTRACTION"|"MASK_ALL"|"MASK_FIRST_N"|"MASK_LAST_N"|"VALIDATE_NON_NULL"|"VALIDATE_NON_ZERO"|"VALIDATE_NON_NEGATIVE"|"VALIDATE_NUMERIC"|"NO_OP",
      "Marketo": "PROJECTION"|"LESS_THAN"|"GREATER_THAN"|"BETWEEN"|"ADDITION"|"MULTIPLICATION"|"DIVISION"|"SUBTRACTION"|"MASK_ALL"|"MASK_FIRST_N"|"MASK_LAST_N"|"VALIDATE_NON_NULL"|"VALIDATE_NON_ZERO"|"VALIDATE_NON_NEGATIVE"|"VALIDATE_NUMERIC"|"NO_OP",
      "S3": "PROJECTION"|"LESS_THAN"|"GREATER_THAN"|"BETWEEN"|"LESS_THAN_OR_EQUAL_TO"|"GREATER_THAN_OR_EQUAL_TO"|"EQUAL_TO"|"NOT_EQUAL_TO"|"ADDITION"|"MULTIPLICATION"|"DIVISION"|"SUBTRACTION"|"MASK_ALL"|"MASK_FIRST_N"|"MASK_LAST_N"|"VALIDATE_NON_NULL"|"VALIDATE_NON_ZERO"|"VALIDATE_NON_NEGATIVE"|"VALIDATE_NUMERIC"|"NO_OP",
      "Salesforce": "PROJECTION"|"LESS_THAN"|"CONTAINS"|"GREATER_THAN"|"BETWEEN"|"LESS_THAN_OR_EQUAL_TO"|"GREATER_THAN_OR_EQUAL_TO"|"EQUAL_TO"|"NOT_EQUAL_TO"|"ADDITION"|"MULTIPLICATION"|"DIVISION"|"SUBTRACTION"|"MASK_ALL"|"MASK_FIRST_N"|"MASK_LAST_N"|"VALIDATE_NON_NULL"|"VALIDATE_NON_ZERO"|"VALIDATE_NON_NEGATIVE"|"VALIDATE_NUMERIC"|"NO_OP",
      "ServiceNow": "PROJECTION"|"CONTAINS"|"LESS_THAN"|"GREATER_THAN"|"BETWEEN"|"LESS_THAN_OR_EQUAL_TO"|"GREATER_THAN_OR_EQUAL_TO"|"EQUAL_TO"|"NOT_EQUAL_TO"|"ADDITION"|"MULTIPLICATION"|"DIVISION"|"SUBTRACTION"|"MASK_ALL"|"MASK_FIRST_N"|"MASK_LAST_N"|"VALIDATE_NON_NULL"|"VALIDATE_NON_ZERO"|"VALIDATE_NON_NEGATIVE"|"VALIDATE_NUMERIC"|"NO_OP",
      "Singular": "PROJECTION"|"EQUAL_TO"|"ADDITION"|"MULTIPLICATION"|"DIVISION"|"SUBTRACTION"|"MASK_ALL"|"MASK_FIRST_N"|"MASK_LAST_N"|"VALIDATE_NON_NULL"|"VALIDATE_NON_ZERO"|"VALIDATE_NON_NEGATIVE"|"VALIDATE_NUMERIC"|"NO_OP",
      "Slack": "PROJECTION"|"LESS_THAN"|"GREATER_THAN"|"BETWEEN"|"LESS_THAN_OR_EQUAL_TO"|"GREATER_THAN_OR_EQUAL_TO"|"EQUAL_TO"|"ADDITION"|"MULTIPLICATION"|"DIVISION"|"SUBTRACTION"|"MASK_ALL"|"MASK_FIRST_N"|"MASK_LAST_N"|"VALIDATE_NON_NULL"|"VALIDATE_NON_ZERO"|"VALIDATE_NON_NEGATIVE"|"VALIDATE_NUMERIC"|"NO_OP",
      "Trendmicro": "PROJECTION"|"EQUAL_TO"|"ADDITION"|"MULTIPLICATION"|"DIVISION"|"SUBTRACTION"|"MASK_ALL"|"MASK_FIRST_N"|"MASK_LAST_N"|"VALIDATE_NON_NULL"|"VALIDATE_NON_ZERO"|"VALIDATE_NON_NEGATIVE"|"VALIDATE_NUMERIC"|"NO_OP",
      "Veeva": "PROJECTION"|"LESS_THAN"|"GREATER_THAN"|"CONTAINS"|"BETWEEN"|"LESS_THAN_OR_EQUAL_TO"|"GREATER_THAN_OR_EQUAL_TO"|"EQUAL_TO"|"NOT_EQUAL_TO"|"ADDITION"|"MULTIPLICATION"|"DIVISION"|"SUBTRACTION"|"MASK_ALL"|"MASK_FIRST_N"|"MASK_LAST_N"|"VALIDATE_NON_NULL"|"VALIDATE_NON_ZERO"|"VALIDATE_NON_NEGATIVE"|"VALIDATE_NUMERIC"|"NO_OP",
      "Zendesk": "PROJECTION"|"GREATER_THAN"|"ADDITION"|"MULTIPLICATION"|"DIVISION"|"SUBTRACTION"|"MASK_ALL"|"MASK_FIRST_N"|"MASK_LAST_N"|"VALIDATE_NON_NULL"|"VALIDATE_NON_ZERO"|"VALIDATE_NON_NEGATIVE"|"VALIDATE_NUMERIC"|"NO_OP",
      "SAPOData": "PROJECTION"|"LESS_THAN"|"CONTAINS"|"GREATER_THAN"|"BETWEEN"|"LESS_THAN_OR_EQUAL_TO"|"GREATER_THAN_OR_EQUAL_TO"|"EQUAL_TO"|"NOT_EQUAL_TO"|"ADDITION"|"MULTIPLICATION"|"DIVISION"|"SUBTRACTION"|"MASK_ALL"|"MASK_FIRST_N"|"MASK_LAST_N"|"VALIDATE_NON_NULL"|"VALIDATE_NON_ZERO"|"VALIDATE_NON_NEGATIVE"|"VALIDATE_NUMERIC"|"NO_OP",
      "CustomConnector": "PROJECTION"|"LESS_THAN"|"GREATER_THAN"|"CONTAINS"|"BETWEEN"|"LESS_THAN_OR_EQUAL_TO"|"GREATER_THAN_OR_EQUAL_TO"|"EQUAL_TO"|"NOT_EQUAL_TO"|"ADDITION"|"MULTIPLICATION"|"DIVISION"|"SUBTRACTION"|"MASK_ALL"|"MASK_FIRST_N"|"MASK_LAST_N"|"VALIDATE_NON_NULL"|"VALIDATE_NON_ZERO"|"VALIDATE_NON_NEGATIVE"|"VALIDATE_NUMERIC"|"NO_OP",
      "Pardot": "PROJECTION"|"EQUAL_TO"|"NO_OP"|"ADDITION"|"MULTIPLICATION"|"DIVISION"|"SUBTRACTION"|"MASK_ALL"|"MASK_FIRST_N"|"MASK_LAST_N"|"VALIDATE_NON_NULL"|"VALIDATE_NON_ZERO"|"VALIDATE_NON_NEGATIVE"|"VALIDATE_NUMERIC"
    },
    "destinationField": "string",
    "taskType": "Arithmetic"|"Filter"|"Map"|"Map_all"|"Mask"|"Merge"|"Passthrough"|"Truncate"|"Validate"|"Partition",
    "taskProperties": {"VALUE"|"VALUES"|"DATA_TYPE"|"UPPER_BOUND"|"LOWER_BOUND"|"SOURCE_DATA_TYPE"|"DESTINATION_DATA_TYPE"|"VALIDATION_ACTION"|"MASK_VALUE"|"MASK_LENGTH"|"TRUNCATE_LENGTH"|"MATH_OPERATION_FIELDS_ORDER"|"CONCAT_FORMAT"|"SUBFIELD_CATEGORY_MAP"|"EXCLUDE_SOURCE_FIELDS_LIST"|"INCLUDE_NEW_FIELDS"|"ORDERED_PARTITION_KEYS_LIST": "string"
      ...}
  }
  ...
]
```

`--tags` (map)

The tags used to organize, track, or control access for your flow.

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

`--metadata-catalog-config` (structure)

Specifies the configuration that Amazon AppFlow uses when it catalogs the data thatâs transferred by the associated flow. When Amazon AppFlow catalogs the data from a flow, it stores metadata in a data catalog.

glueDataCatalog -> (structure)

Specifies the configuration that Amazon AppFlow uses when it catalogs your data with the Glue Data Catalog.

roleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role that grants Amazon AppFlow the permissions it needs to create Data Catalog tables, databases, and partitions.

For an example IAM policy that has the required permissions, see [Identity-based policy examples for Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/security_iam_id-based-policy-examples.html) .

databaseName -> (string)

The name of the Data Catalog database that stores the metadata tables that Amazon AppFlow creates in your Amazon Web Services account. These tables contain metadata for the data thatâs transferred by the flow that you configure with this parameter.

### Note

When you configure a new flow with this parameter, you must specify an existing database.

tablePrefix -> (string)

A naming prefix for each Data Catalog table that Amazon AppFlow creates for the flow that you configure with this setting. Amazon AppFlow adds the prefix to the beginning of the each table name.

Shorthand Syntax:

```
glueDataCatalog={roleArn=string,databaseName=string,tablePrefix=string}
```

JSON Syntax:

```
{
  "glueDataCatalog": {
    "roleArn": "string",
    "databaseName": "string",
    "tablePrefix": "string"
  }
}
```

`--client-token` (string)

The `clientToken` parameter is an idempotency token. It ensures that your `CreateFlow` request completes only once. You choose the value to pass. For example, if you donât receive a response from your request, you can safely retry the request with the same `clientToken` parameter value.

If you omit a `clientToken` value, the Amazon Web Services SDK that you are using inserts a value for you. This way, the SDK can safely retry requests multiple times after a network error. You must provide your own value for other use cases.

If you specify input parameters that differ from your first request, an error occurs. If you use a different value for `clientToken` , Amazon AppFlow considers it a new call to `CreateFlow` . The token is active for 8 hours.

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

flowArn -> (string)

The flowâs Amazon Resource Name (ARN).

flowStatus -> (string)

Indicates the current status of the flow.