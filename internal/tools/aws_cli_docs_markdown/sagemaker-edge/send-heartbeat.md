# send-heartbeatÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-edge/send-heartbeat.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-edge/send-heartbeat.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker-edge](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-edge/index.html#cli-aws-sagemaker-edge) ]

# send-heartbeat

## Description

Use to get the current status of devices registered on SageMaker Edge Manager.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-edge-2020-09-23/SendHeartbeat)

## Synopsis

```
send-heartbeat
[--agent-metrics <value>]
[--models <value>]
--agent-version <value>
--device-name <value>
--device-fleet-name <value>
[--deployment-result <value>]
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

`--agent-metrics` (list)

For internal use. Returns a list of SageMaker Edge Manager agent operating metrics.

(structure)

Information required for edge device metrics.

Dimension -> (string)

The dimension of metrics published.

MetricName -> (string)

Returns the name of the metric.

Value -> (double)

Returns the value of the metric.

Timestamp -> (timestamp)

Timestamp of when the metric was requested.

Shorthand Syntax:

```
Dimension=string,MetricName=string,Value=double,Timestamp=timestamp ...
```

JSON Syntax:

```
[
  {
    "Dimension": "string",
    "MetricName": "string",
    "Value": double,
    "Timestamp": timestamp
  }
  ...
]
```

`--models` (list)

Returns a list of models deployed on the the device.

(structure)

Information about a model deployed on an edge device that is registered with SageMaker Edge Manager.

ModelName -> (string)

The name of the model.

ModelVersion -> (string)

The version of the model.

LatestSampleTime -> (timestamp)

The timestamp of the last data sample taken.

LatestInference -> (timestamp)

The timestamp of the last inference that was made.

ModelMetrics -> (list)

Information required for model metrics.

(structure)

Information required for edge device metrics.

Dimension -> (string)

The dimension of metrics published.

MetricName -> (string)

Returns the name of the metric.

Value -> (double)

Returns the value of the metric.

Timestamp -> (timestamp)

Timestamp of when the metric was requested.

Shorthand Syntax:

```
ModelName=string,ModelVersion=string,LatestSampleTime=timestamp,LatestInference=timestamp,ModelMetrics=[{Dimension=string,MetricName=string,Value=double,Timestamp=timestamp},{Dimension=string,MetricName=string,Value=double,Timestamp=timestamp}] ...
```

JSON Syntax:

```
[
  {
    "ModelName": "string",
    "ModelVersion": "string",
    "LatestSampleTime": timestamp,
    "LatestInference": timestamp,
    "ModelMetrics": [
      {
        "Dimension": "string",
        "MetricName": "string",
        "Value": double,
        "Timestamp": timestamp
      }
      ...
    ]
  }
  ...
]
```

`--agent-version` (string)

Returns the version of the agent.

`--device-name` (string)

The unique name of the device.

`--device-fleet-name` (string)

The name of the fleet that the device belongs to.

`--deployment-result` (structure)

Returns the result of a deployment on the device.

DeploymentName -> (string)

The name and unique ID of the deployment.

DeploymentStatus -> (string)

Returns the bucket error code.

DeploymentStatusMessage -> (string)

Returns the detailed error message.

DeploymentStartTime -> (timestamp)

The timestamp of when the deployment was started on the agent.

DeploymentEndTime -> (timestamp)

The timestamp of when the deployment was ended, and the agent got the deployment results.

DeploymentModels -> (list)

Returns a list of models deployed on the agent.

(structure)

ModelHandle -> (string)

The unique handle of the model.

ModelName -> (string)

The name of the model.

ModelVersion -> (string)

The version of the model.

DesiredState -> (string)

The desired state of the model.

State -> (string)

Returns the current state of the model.

Status -> (string)

Returns the deployment status of the model.

StatusReason -> (string)

Returns the error message for the deployment status result.

RollbackFailureReason -> (string)

Returns the error message if there is a rollback.

Shorthand Syntax:

```
DeploymentName=string,DeploymentStatus=string,DeploymentStatusMessage=string,DeploymentStartTime=timestamp,DeploymentEndTime=timestamp,DeploymentModels=[{ModelHandle=string,ModelName=string,ModelVersion=string,DesiredState=string,State=string,Status=string,StatusReason=string,RollbackFailureReason=string},{ModelHandle=string,ModelName=string,ModelVersion=string,DesiredState=string,State=string,Status=string,StatusReason=string,RollbackFailureReason=string}]
```

JSON Syntax:

```
{
  "DeploymentName": "string",
  "DeploymentStatus": "string",
  "DeploymentStatusMessage": "string",
  "DeploymentStartTime": timestamp,
  "DeploymentEndTime": timestamp,
  "DeploymentModels": [
    {
      "ModelHandle": "string",
      "ModelName": "string",
      "ModelVersion": "string",
      "DesiredState": "DEPLOY"|"UNDEPLOY",
      "State": "DEPLOY"|"UNDEPLOY",
      "Status": "SUCCESS"|"FAIL",
      "StatusReason": "string",
      "RollbackFailureReason": "string"
    }
    ...
  ]
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

None