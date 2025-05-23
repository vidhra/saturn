# create-monitorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/create-monitor.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/create-monitor.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [internetmonitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/index.html#cli-aws-internetmonitor) ]

# create-monitor

## Description

Creates a monitor in Amazon CloudWatch Internet Monitor. A monitor is built based on information from the application resources that you add: VPCs, Network Load Balancers (NLBs), Amazon CloudFront distributions, and Amazon WorkSpaces directories. Internet Monitor then publishes internet measurements from Amazon Web Services that are specific to the *city-networks* . That is, the locations and ASNs (typically internet service providers or ISPs), where clients access your application. For more information, see [Using Amazon CloudWatch Internet Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html) in the *Amazon CloudWatch User Guide* .

When you create a monitor, you choose the percentage of traffic that you want to monitor. You can also set a maximum limit for the number of city-networks where client traffic is monitored, that caps the total traffic that Internet Monitor monitors. A city-network maximum is the limit of city-networks, but you only pay for the number of city-networks that are actually monitored. You can update your monitor at any time to change the percentage of traffic to monitor or the city-networks maximum. For more information, see [Choosing a city-network maximum value](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html) in the *Amazon CloudWatch User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/internetmonitor-2021-06-03/CreateMonitor)

## Synopsis

```
create-monitor
--monitor-name <value>
[--resources <value>]
[--client-token <value>]
[--tags <value>]
[--max-city-networks-to-monitor <value>]
[--internet-measurements-log-delivery <value>]
[--traffic-percentage-to-monitor <value>]
[--health-events-config <value>]
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

`--monitor-name` (string)

The name of the monitor.

`--resources` (list)

The resources to include in a monitor, which you provide as a set of Amazon Resource Names (ARNs). Resources can be VPCs, NLBs, Amazon CloudFront distributions, or Amazon WorkSpaces directories.

You can add a combination of VPCs and CloudFront distributions, or you can add WorkSpaces directories, or you can add NLBs. You canât add NLBs or WorkSpaces directories together with any other resources.

### Note

If you add only Amazon VPC resources, at least one VPC must have an Internet Gateway attached to it, to make sure that it has internet connectivity.

(string)

Syntax:

```
"string" "string" ...
```

`--client-token` (string)

A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. Donât reuse the same client token for other API requests.

`--tags` (map)

The tags for a monitor. You can add a maximum of 50 tags in Internet Monitor.

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

`--max-city-networks-to-monitor` (integer)

The maximum number of city-networks to monitor for your resources. A city-network is the location (city) where clients access your application resources from and the ASN or network provider, such as an internet service provider (ISP), that clients access the resources through. Setting this limit can help control billing costs.

To learn more, see [Choosing a city-network maximum value](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html) in the Amazon CloudWatch Internet Monitor section of the *CloudWatch User Guide* .

`--internet-measurements-log-delivery` (structure)

Publish internet measurements for Internet Monitor to an Amazon S3 bucket in addition to CloudWatch Logs.

S3Config -> (structure)

The configuration information for publishing Internet Monitor internet measurements to Amazon S3. The configuration includes the bucket name and (optionally) prefix for the S3 bucket to store the measurements, and the delivery status. The delivery status is `ENABLED` or `DISABLED` , depending on whether you choose to deliver internet measurements to S3 logs.

BucketName -> (string)

The Amazon S3 bucket name.

BucketPrefix -> (string)

The Amazon S3 bucket prefix.

LogDeliveryStatus -> (string)

The status of publishing Internet Monitor internet measurements to an Amazon S3 bucket.

Shorthand Syntax:

```
S3Config={BucketName=string,BucketPrefix=string,LogDeliveryStatus=string}
```

JSON Syntax:

```
{
  "S3Config": {
    "BucketName": "string",
    "BucketPrefix": "string",
    "LogDeliveryStatus": "ENABLED"|"DISABLED"
  }
}
```

`--traffic-percentage-to-monitor` (integer)

The percentage of the internet-facing traffic for your application that you want to monitor with this monitor. If you set a city-networks maximum, that limit overrides the traffic percentage that you set.

To learn more, see [Choosing an application traffic percentage to monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMTrafficPercentage.html) in the Amazon CloudWatch Internet Monitor section of the *CloudWatch User Guide* .

`--health-events-config` (structure)

Defines the threshold percentages and other configuration information for when Amazon CloudWatch Internet Monitor creates a health event. Internet Monitor creates a health event when an internet issue that affects your application end users has a health score percentage that is at or below a specific threshold, and, sometimes, when other criteria are met.

If you donât set a health event threshold, the default value is 95%.

For more information, see [Change health event thresholds](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-overview.html#IMUpdateThresholdFromOverview) in the Internet Monitor section of the *CloudWatch User Guide* .

AvailabilityScoreThreshold -> (double)

The health event threshold percentage set for availability scores.

PerformanceScoreThreshold -> (double)

The health event threshold percentage set for performance scores.

AvailabilityLocalHealthEventsConfig -> (structure)

The configuration that determines the threshold and other conditions for when Internet Monitor creates a health event for a local availability issue.

Status -> (string)

The status of whether Internet Monitor creates a health event based on a threshold percentage set for a local health score. The status can be `ENABLED` or `DISABLED` .

HealthScoreThreshold -> (double)

The health event threshold percentage set for a local health score.

MinTrafficImpact -> (double)

The minimum percentage of overall traffic for an application that must be impacted by an issue before Internet Monitor creates an event when a threshold is crossed for a local health score.

If you donât set a minimum traffic impact threshold, the default value is 0.1%.

PerformanceLocalHealthEventsConfig -> (structure)

The configuration that determines the threshold and other conditions for when Internet Monitor creates a health event for a local performance issue.

Status -> (string)

The status of whether Internet Monitor creates a health event based on a threshold percentage set for a local health score. The status can be `ENABLED` or `DISABLED` .

HealthScoreThreshold -> (double)

The health event threshold percentage set for a local health score.

MinTrafficImpact -> (double)

The minimum percentage of overall traffic for an application that must be impacted by an issue before Internet Monitor creates an event when a threshold is crossed for a local health score.

If you donât set a minimum traffic impact threshold, the default value is 0.1%.

Shorthand Syntax:

```
AvailabilityScoreThreshold=double,PerformanceScoreThreshold=double,AvailabilityLocalHealthEventsConfig={Status=string,HealthScoreThreshold=double,MinTrafficImpact=double},PerformanceLocalHealthEventsConfig={Status=string,HealthScoreThreshold=double,MinTrafficImpact=double}
```

JSON Syntax:

```
{
  "AvailabilityScoreThreshold": double,
  "PerformanceScoreThreshold": double,
  "AvailabilityLocalHealthEventsConfig": {
    "Status": "ENABLED"|"DISABLED",
    "HealthScoreThreshold": double,
    "MinTrafficImpact": double
  },
  "PerformanceLocalHealthEventsConfig": {
    "Status": "ENABLED"|"DISABLED",
    "HealthScoreThreshold": double,
    "MinTrafficImpact": double
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

Arn -> (string)

The Amazon Resource Name (ARN) of the monitor.

Status -> (string)

The status of a monitor.