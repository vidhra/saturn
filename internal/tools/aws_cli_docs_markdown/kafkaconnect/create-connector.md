# create-connectorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafkaconnect/create-connector.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafkaconnect/create-connector.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kafkaconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafkaconnect/index.html#cli-aws-kafkaconnect) ]

# create-connector

## Description

Creates a connector using the specified properties.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kafkaconnect-2021-09-14/CreateConnector)

## Synopsis

```
create-connector
--capacity <value>
--connector-configuration <value>
[--connector-description <value>]
--connector-name <value>
--kafka-cluster <value>
--kafka-cluster-client-authentication <value>
--kafka-cluster-encryption-in-transit <value>
--kafka-connect-version <value>
[--log-delivery <value>]
--plugins <value>
--service-execution-role-arn <value>
[--worker-configuration <value>]
[--tags <value>]
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

`--capacity` (structure)

Information about the capacity allocated to the connector. Exactly one of the two properties must be specified.

autoScaling -> (structure)

Information about the auto scaling parameters for the connector.

maxWorkerCount -> (integer)

The maximum number of workers allocated to the connector.

mcuCount -> (integer)

The number of microcontroller units (MCUs) allocated to each connector worker. The valid values are 1,2,4,8.

minWorkerCount -> (integer)

The minimum number of workers allocated to the connector.

scaleInPolicy -> (structure)

The sacle-in policy for the connector.

cpuUtilizationPercentage -> (integer)

Specifies the CPU utilization percentage threshold at which you want connector scale in to be triggered.

scaleOutPolicy -> (structure)

The sacle-out policy for the connector.

cpuUtilizationPercentage -> (integer)

The CPU utilization percentage threshold at which you want connector scale out to be triggered.

provisionedCapacity -> (structure)

Details about a fixed capacity allocated to a connector.

mcuCount -> (integer)

The number of microcontroller units (MCUs) allocated to each connector worker. The valid values are 1,2,4,8.

workerCount -> (integer)

The number of workers that are allocated to the connector.

Shorthand Syntax:

```
autoScaling={maxWorkerCount=integer,mcuCount=integer,minWorkerCount=integer,scaleInPolicy={cpuUtilizationPercentage=integer},scaleOutPolicy={cpuUtilizationPercentage=integer}},provisionedCapacity={mcuCount=integer,workerCount=integer}
```

JSON Syntax:

```
{
  "autoScaling": {
    "maxWorkerCount": integer,
    "mcuCount": integer,
    "minWorkerCount": integer,
    "scaleInPolicy": {
      "cpuUtilizationPercentage": integer
    },
    "scaleOutPolicy": {
      "cpuUtilizationPercentage": integer
    }
  },
  "provisionedCapacity": {
    "mcuCount": integer,
    "workerCount": integer
  }
}
```

`--connector-configuration` (map)

A map of keys to values that represent the configuration for the connector.

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

`--connector-description` (string)

A summary description of the connector.

`--connector-name` (string)

The name of the connector.

`--kafka-cluster` (structure)

Specifies which Apache Kafka cluster to connect to.

apacheKafkaCluster -> (structure)

The Apache Kafka cluster to which the connector is connected.

bootstrapServers -> (string)

The bootstrap servers of the cluster.

vpc -> (structure)

Details of an Amazon VPC which has network connectivity to the Apache Kafka cluster.

securityGroups -> (list)

The security groups for the connector.

(string)

subnets -> (list)

The subnets for the connector.

(string)

JSON Syntax:

```
{
  "apacheKafkaCluster": {
    "bootstrapServers": "string",
    "vpc": {
      "securityGroups": ["string", ...],
      "subnets": ["string", ...]
    }
  }
}
```

`--kafka-cluster-client-authentication` (structure)

Details of the client authentication used by the Apache Kafka cluster.

authenticationType -> (string)

The type of client authentication used to connect to the Apache Kafka cluster. Value NONE means that no client authentication is used.

Shorthand Syntax:

```
authenticationType=string
```

JSON Syntax:

```
{
  "authenticationType": "NONE"|"IAM"
}
```

`--kafka-cluster-encryption-in-transit` (structure)

Details of encryption in transit to the Apache Kafka cluster.

encryptionType -> (string)

The type of encryption in transit to the Apache Kafka cluster.

Shorthand Syntax:

```
encryptionType=string
```

JSON Syntax:

```
{
  "encryptionType": "PLAINTEXT"|"TLS"
}
```

`--kafka-connect-version` (string)

The version of Kafka Connect. It has to be compatible with both the Apache Kafka clusterâs version and the plugins.

`--log-delivery` (structure)

Details about log delivery.

workerLogDelivery -> (structure)

The workers can send worker logs to different destination types. This configuration specifies the details of these destinations.

cloudWatchLogs -> (structure)

Details about delivering logs to Amazon CloudWatch Logs.

enabled -> (boolean)

Whether log delivery to Amazon CloudWatch Logs is enabled.

logGroup -> (string)

The name of the CloudWatch log group that is the destination for log delivery.

firehose -> (structure)

Details about delivering logs to Amazon Kinesis Data Firehose.

deliveryStream -> (string)

The name of the Kinesis Data Firehose delivery stream that is the destination for log delivery.

enabled -> (boolean)

Specifies whether connector logs get delivered to Amazon Kinesis Data Firehose.

s3 -> (structure)

Details about delivering logs to Amazon S3.

bucket -> (string)

The name of the S3 bucket that is the destination for log delivery.

enabled -> (boolean)

Specifies whether connector logs get sent to the specified Amazon S3 destination.

prefix -> (string)

The S3 prefix that is the destination for log delivery.

Shorthand Syntax:

```
workerLogDelivery={cloudWatchLogs={enabled=boolean,logGroup=string},firehose={deliveryStream=string,enabled=boolean},s3={bucket=string,enabled=boolean,prefix=string}}
```

JSON Syntax:

```
{
  "workerLogDelivery": {
    "cloudWatchLogs": {
      "enabled": true|false,
      "logGroup": "string"
    },
    "firehose": {
      "deliveryStream": "string",
      "enabled": true|false
    },
    "s3": {
      "bucket": "string",
      "enabled": true|false,
      "prefix": "string"
    }
  }
}
```

`--plugins` (list)

### Warning

Amazon MSK Connect does not currently support specifying multiple plugins as a list. To use more than one plugin for your connector, you can create a single custom plugin using a ZIP file that bundles multiple plugins together.

Specifies which plugin to use for the connector. You must specify a single-element list containing one `customPlugin` object.

(structure)

A plugin is an Amazon Web Services resource that contains the code that defines your connector logic.

customPlugin -> (structure)

Details about a custom plugin.

customPluginArn -> (string)

The Amazon Resource Name (ARN) of the custom plugin.

revision -> (long)

The revision of the custom plugin.

Shorthand Syntax:

```
customPlugin={customPluginArn=string,revision=long} ...
```

JSON Syntax:

```
[
  {
    "customPlugin": {
      "customPluginArn": "string",
      "revision": long
    }
  }
  ...
]
```

`--service-execution-role-arn` (string)

The Amazon Resource Name (ARN) of the IAM role used by the connector to access the Amazon Web Services resources that it needs. The types of resources depends on the logic of the connector. For example, a connector that has Amazon S3 as a destination must have permissions that allow it to write to the S3 destination bucket.

`--worker-configuration` (structure)

Specifies which worker configuration to use with the connector.

revision -> (long)

The revision of the worker configuration.

workerConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the worker configuration.

Shorthand Syntax:

```
revision=long,workerConfigurationArn=string
```

JSON Syntax:

```
{
  "revision": long,
  "workerConfigurationArn": "string"
}
```

`--tags` (map)

The tags you want to attach to the connector.

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

connectorArn -> (string)

The Amazon Resource Name (ARN) that Amazon assigned to the connector.

connectorName -> (string)

The name of the connector.

connectorState -> (string)

The state of the connector.