# describe-observationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/describe-observation.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/describe-observation.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [application-insights](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/index.html#cli-aws-application-insights) ]

# describe-observation

## Description

Describes an anomaly or error with the application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/application-insights-2018-11-25/DescribeObservation)

## Synopsis

```
describe-observation
--observation-id <value>
[--account-id <value>]
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

`--observation-id` (string)

The ID of the observation.

`--account-id` (string)

The Amazon Web Services account ID for the resource group owner.

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

Observation -> (structure)

Information about the observation.

Id -> (string)

The ID of the observation type.

StartTime -> (timestamp)

The time when the observation was first detected, in epoch seconds.

EndTime -> (timestamp)

The time when the observation ended, in epoch seconds.

SourceType -> (string)

The source type of the observation.

SourceARN -> (string)

The source resource ARN of the observation.

LogGroup -> (string)

The log group name.

LineTime -> (timestamp)

The timestamp in the CloudWatch Logs that specifies when the matched line occurred.

LogText -> (string)

The log text of the observation.

LogFilter -> (string)

The log filter of the observation.

MetricNamespace -> (string)

The namespace of the observation metric.

MetricName -> (string)

The name of the observation metric.

Unit -> (string)

The unit of the source observation metric.

Value -> (double)

The value of the source observation metric.

CloudWatchEventId -> (string)

The ID of the CloudWatch Event-based observation related to the detected problem.

CloudWatchEventSource -> (string)

The source of the CloudWatch Event.

CloudWatchEventDetailType -> (string)

The detail type of the CloudWatch Event-based observation, for example, `EC2 Instance State-change Notification` .

HealthEventArn -> (string)

The Amazon Resource Name (ARN) of the Health Event-based observation.

HealthService -> (string)

The service to which the Health Event belongs, such as EC2.

HealthEventTypeCode -> (string)

The type of the Health event, for example, `AWS_EC2_POWER_CONNECTIVITY_ISSUE` .

HealthEventTypeCategory -> (string)

The category of the Health event, such as `issue` .

HealthEventDescription -> (string)

The description of the Health event provided by the service, such as Amazon EC2.

CodeDeployDeploymentId -> (string)

The deployment ID of the CodeDeploy-based observation related to the detected problem.

CodeDeployDeploymentGroup -> (string)

The deployment group to which the CodeDeploy deployment belongs.

CodeDeployState -> (string)

The status of the CodeDeploy deployment, for example `SUCCESS` or `FAILURE` .

CodeDeployApplication -> (string)

The CodeDeploy application to which the deployment belongs.

CodeDeployInstanceGroupId -> (string)

The instance group to which the CodeDeploy instance belongs.

Ec2State -> (string)

The state of the instance, such as `STOPPING` or `TERMINATING` .

RdsEventCategories -> (string)

The category of an RDS event.

RdsEventMessage -> (string)

The message of an RDS event.

S3EventName -> (string)

The name of the S3 CloudWatch Event-based observation.

StatesExecutionArn -> (string)

The Amazon Resource Name (ARN) of the step function execution-based observation.

StatesArn -> (string)

The Amazon Resource Name (ARN) of the step function-based observation.

StatesStatus -> (string)

The status of the step function-related observation.

StatesInput -> (string)

The input to the step function-based observation.

EbsEvent -> (string)

The type of EBS CloudWatch event, such as `createVolume` , `deleteVolume` or `attachVolume` .

EbsResult -> (string)

The result of an EBS CloudWatch event, such as `failed` or `succeeded` .

EbsCause -> (string)

The cause of an EBS CloudWatch event.

EbsRequestId -> (string)

The request ID of an EBS CloudWatch event.

XRayFaultPercent -> (integer)

The X-Ray request fault percentage for this node.

XRayThrottlePercent -> (integer)

The X-Ray request throttle percentage for this node.

XRayErrorPercent -> (integer)

The X-Ray request error percentage for this node.

XRayRequestCount -> (integer)

The X-Ray request count for this node.

XRayRequestAverageLatency -> (long)

The X-Ray node request average latency for this node.

XRayNodeName -> (string)

The name of the X-Ray node.

XRayNodeType -> (string)

The type of the X-Ray node.