# get-campaignÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotfleetwise/get-campaign.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotfleetwise/get-campaign.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotfleetwise](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotfleetwise/index.html#cli-aws-iotfleetwise) ]

# get-campaign

## Description

Retrieves information about a campaign.

### Warning

Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see [Amazon Web Services Region and feature availability](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html) in the *Amazon Web Services IoT FleetWise Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotfleetwise-2021-06-17/GetCampaign)

## Synopsis

```
get-campaign
--name <value>
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

The name of the campaign to retrieve information about.

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

name -> (string)

The name of the campaign.

arn -> (string)

The Amazon Resource Name (ARN) of the campaign.

description -> (string)

The description of the campaign.

signalCatalogArn -> (string)

The ARN of a signal catalog.

targetArn -> (string)

The ARN of the vehicle or the fleet targeted by the campaign.

status -> (string)

The state of the campaign. The status can be one of: `CREATING` , `WAITING_FOR_APPROVAL` , `RUNNING` , and `SUSPENDED` .

startTime -> (timestamp)

The time, in milliseconds, to deliver a campaign after it was approved.

expiryTime -> (timestamp)

The time the campaign expires, in seconds since epoch (January 1, 1970 at midnight UTC time). Vehicle data wonât be collected after the campaign expires.

postTriggerCollectionDuration -> (long)

How long (in seconds) to collect raw data after a triggering event initiates the collection.

diagnosticsMode -> (string)

Option for a vehicle to send diagnostic trouble codes to Amazon Web Services IoT FleetWise.

spoolingMode -> (string)

Whether to store collected data after a vehicle lost a connection with the cloud. After a connection is re-established, the data is automatically forwarded to Amazon Web Services IoT FleetWise.

compression -> (string)

Whether to compress signals before transmitting data to Amazon Web Services IoT FleetWise. If `OFF` is specified, the signals arenât compressed. If itâs not specified, `SNAPPY` is used.

priority -> (integer)

A number indicating the priority of one campaign over another campaign for a certain vehicle or fleet. A campaign with the lowest value is deployed to vehicles before any other campaigns.

signalsToCollect -> (list)

Information about a list of signals to collect data on.

(structure)

Information about a signal.

name -> (string)

The name of the signal.

maxSampleCount -> (long)

The maximum number of samples to collect.

minimumSamplingIntervalMs -> (long)

The minimum duration of time (in milliseconds) between two triggering events to collect data.

### Note

If a signal changes often, you might want to collect data at a slower rate.

dataPartitionId -> (string)

The ID of the data partition this signal is associated with.

The ID must match one of the IDs provided in `dataPartitions` . This is accomplished either by specifying a particular data partition ID or by using `default` for an established default partition. You can establish a default partition in the `DataPartition` data type.

### Note

If you upload a signal as a condition for a campaignâs data partition, the same signal must be included in `signalsToCollect` .

### Warning

Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see [Amazon Web Services Region and feature availability](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html) in the *Amazon Web Services IoT FleetWise Developer Guide* .

collectionScheme -> (tagged union structure)

Information about the data collection scheme associated with the campaign.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `timeBasedCollectionScheme`, `conditionBasedCollectionScheme`.

timeBasedCollectionScheme -> (structure)

Information about a collection scheme that uses a time period to decide how often to collect data.

periodMs -> (long)

The time period (in milliseconds) to decide how often to collect data. For example, if the time period is `60000` , the Edge Agent software collects data once every minute.

conditionBasedCollectionScheme -> (structure)

Information about a collection scheme that uses a simple logical expression to recognize what data to collect.

expression -> (string)

The logical expression used to recognize what data to collect. For example, `$variable.`Vehicle.OutsideAirTemperature` >= 105.0` .

minimumTriggerIntervalMs -> (long)

The minimum duration of time between two triggering events to collect data, in milliseconds.

### Note

If a signal changes often, you might want to collect data at a slower rate.

triggerMode -> (string)

Whether to collect data for all triggering events (`ALWAYS` ). Specify (`RISING_EDGE` ), or specify only when the condition first evaluates to false. For example, triggering on âAirbagDeployedâ; Users arenât interested on triggering when the airbag is already exploded; they only care about the change from not deployed => deployed.

conditionLanguageVersion -> (integer)

Specifies the version of the conditional expression language.

dataExtraDimensions -> (list)

A list of vehicle attributes associated with the campaign.

(string)

creationTime -> (timestamp)

The time the campaign was created in seconds since epoch (January 1, 1970 at midnight UTC time).

lastModificationTime -> (timestamp)

The last time the campaign was modified.

dataDestinationConfigs -> (list)

The destination where the campaign sends data. You can send data to an MQTT topic, or store it in Amazon S3 or Amazon Timestream.

MQTT is the publish/subscribe messaging protocol used by Amazon Web Services IoT to communicate with your devices.

Amazon S3 optimizes the cost of data storage and provides additional mechanisms to use vehicle data, such as data lakes, centralized data storage, data processing pipelines, and analytics.

You can use Amazon Timestream to access and analyze time series data, and Timestream to query vehicle data so that you can identify trends and patterns.

(tagged union structure)

The destination where the campaign sends data. You can send data to an MQTT topic, or store it in Amazon S3 or Amazon Timestream.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3Config`, `timestreamConfig`, `mqttTopicConfig`.

s3Config -> (structure)

The Amazon S3 bucket where the Amazon Web Services IoT FleetWise campaign sends data.

bucketArn -> (string)

The Amazon Resource Name (ARN) of the Amazon S3 bucket.

dataFormat -> (string)

Specify the format that files are saved in the Amazon S3 bucket. You can save files in an Apache Parquet or JSON format.

- Parquet - Store data in a columnar storage file format. Parquet is optimal for fast data retrieval and can reduce costs. This option is selected by default.
- JSON - Store data in a standard text-based JSON file format.

storageCompressionFormat -> (string)

By default, stored data is compressed as a .gzip file. Compressed files have a reduced file size, which can optimize the cost of data storage.

prefix -> (string)

Enter an S3 bucket prefix. The prefix is the string of characters after the bucket name and before the object name. You can use the prefix to organize data stored in Amazon S3 buckets. For more information, see [Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) in the *Amazon Simple Storage Service User Guide* .

By default, Amazon Web Services IoT FleetWise sets the prefix `processed-data/year=YY/month=MM/date=DD/hour=HH/` (in UTC) to data it delivers to Amazon S3. You can enter a prefix to append it to this default prefix. For example, if you enter the prefix `vehicles` , the prefix will be `vehicles/processed-data/year=YY/month=MM/date=DD/hour=HH/` .

timestreamConfig -> (structure)

The Amazon Timestream table where the campaign sends data.

timestreamTableArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Timestream table.

executionRoleArn -> (string)

The Amazon Resource Name (ARN) of the task execution role that grants Amazon Web Services IoT FleetWise permission to deliver data to the Amazon Timestream table.

mqttTopicConfig -> (structure)

The MQTT topic to which the Amazon Web Services IoT FleetWise campaign routes data.

### Warning

Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see [Amazon Web Services Region and feature availability](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html) in the *Amazon Web Services IoT FleetWise Developer Guide* .

mqttTopicArn -> (string)

The ARN of the MQTT topic.

executionRoleArn -> (string)

The ARN of the role that grants Amazon Web Services IoT FleetWise permission to access and act on messages sent to the MQTT topic.

dataPartitions -> (list)

The data partitions associated with the signals collected from the vehicle.

(structure)

The configuration for signal data storage and upload options. You can only specify these options when the campaignâs spooling mode is `TO_DISK` .

### Warning

Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see [Amazon Web Services Region and feature availability](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html) in the *Amazon Web Services IoT FleetWise Developer Guide* .

id -> (string)

The ID of the data partition. The data partition ID must be unique within a campaign. You can establish a data partition as the default partition for a campaign by using `default` as the ID.

storageOptions -> (structure)

The storage options for a data partition.

maximumSize -> (structure)

The maximum storage size of the data stored in the data partition.

### Note

Newer data overwrites older data when the partition reaches the maximum size.

unit -> (string)

The data type of the data to store.

value -> (integer)

The maximum amount of time to store data.

storageLocation -> (string)

The folder name for the data partition under the campaign storage folder.

minimumTimeToLive -> (structure)

The amount of time that data in this partition will be kept on disk.

- After the designated amount of time passes, the data can be removed, but itâs not guaranteed to be removed.
- Before the time expires, data in this partition can still be deleted if the partition reaches its configured maximum size.
- Newer data will overwrite older data when the partition reaches the maximum size.

unit -> (string)

The time increment type.

value -> (integer)

The minimum amount of time to store the data.

uploadOptions -> (structure)

The upload options for the data partition.

expression -> (string)

The logical expression used to recognize what data to collect. For example, `$variable.`Vehicle.OutsideAirTemperature` >= 105.0` .

conditionLanguageVersion -> (integer)

The version of the condition language. Defaults to the most recent condition language version.

signalsToFetch -> (list)

Information about a list of signals to fetch data from.

(structure)

Information about the signal to be fetched.

### Warning

Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see [Amazon Web Services Region and feature availability](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html) in the *Amazon Web Services IoT FleetWise Developer Guide* .

fullyQualifiedName -> (string)

The fully qualified name of the signal to be fetched.

signalFetchConfig -> (tagged union structure)

The configuration of the signal fetch operation.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `timeBased`, `conditionBased`.

timeBased -> (structure)

The configuration of a time-based signal fetch operation.

executionFrequencyMs -> (long)

The frequency with which the signal fetch will be executed.

conditionBased -> (structure)

The configuration of a condition-based signal fetch operation.

conditionExpression -> (string)

The condition that must be satisfied to trigger a signal fetch.

triggerMode -> (string)

Indicates the mode in which the signal fetch is triggered.

conditionLanguageVersion -> (integer)

The version of the condition language used.

actions -> (list)

The actions to be performed by the signal fetch.

(string)