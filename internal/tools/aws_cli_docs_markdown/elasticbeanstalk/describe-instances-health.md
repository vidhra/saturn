# describe-instances-healthÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-instances-health.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-instances-health.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticbeanstalk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/index.html#cli-aws-elasticbeanstalk) ]

# describe-instances-health

## Description

Retrieves detailed information about the health of instances in your AWS Elastic Beanstalk. This operation requires [enhanced health reporting](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribeInstancesHealth)

## Synopsis

```
describe-instances-health
[--environment-name <value>]
[--environment-id <value>]
[--attribute-names <value>]
[--next-token <value>]
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

`--environment-name` (string)

Specify the AWS Elastic Beanstalk environment by name.

`--environment-id` (string)

Specify the AWS Elastic Beanstalk environment by ID.

`--attribute-names` (list)

Specifies the response elements you wish to receive. To retrieve all attributes, set to `All` . If no attribute names are specified, returns a list of instances.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  HealthStatus
  Color
  Causes
  ApplicationMetrics
  RefreshedAt
  LaunchedAt
  System
  Deployment
  AvailabilityZone
  InstanceType
  All
```

`--next-token` (string)

Specify the pagination token returned by a previous call.

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

**To view environment health**

The following command retrieves health information for instances in an environment named `my-env`:

```
aws elasticbeanstalk describe-instances-health --environment-name my-env --attribute-names All
```

Output:

```
{
    "InstanceHealthList": [
        {
            "InstanceId": "i-08691cc7",
            "ApplicationMetrics": {
                "Duration": 10,
                "Latency": {
                    "P99": 0.006,
                    "P75": 0.002,
                    "P90": 0.004,
                    "P95": 0.005,
                    "P85": 0.003,
                    "P10": 0.0,
                    "P999": 0.006,
                    "P50": 0.001
                },
                "RequestCount": 48,
                "StatusCodes": {
                    "Status3xx": 0,
                    "Status2xx": 47,
                    "Status5xx": 0,
                    "Status4xx": 1
                }
            },
            "System": {
                "LoadAverage": [
                    0.0,
                    0.02,
                    0.05
                ],
                "CPUUtilization": {
                    "SoftIRQ": 0.1,
                    "IOWait": 0.2,
                    "System": 0.3,
                    "Idle": 97.8,
                    "User": 1.5,
                    "IRQ": 0.0,
                    "Nice": 0.1
                }
            },
            "Color": "Green",
            "HealthStatus": "Ok",
            "LaunchedAt": "2015-08-13T19:17:09Z",
            "Causes": []
        }
    ],
    "RefreshedAt": "2015-08-20T21:09:08Z"
}
```

Health information is only available for environments with enhanced health reporting enabled. For more information, see [Enhanced Health Reporting and Monitoring](http://integ-docs-aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced.html) in the *AWS Elastic Beanstalk Developer Guide*.

## Output

InstanceHealthList -> (list)

Detailed health information about each instance.

The output differs slightly between Linux and Windows environments. There is a difference in the members that are supported under the `<CPUUtilization>` type.

(structure)

Detailed health information about an Amazon EC2 instance in your Elastic Beanstalk environment.

InstanceId -> (string)

The ID of the Amazon EC2 instance.

HealthStatus -> (string)

Returns the health status of the specified instance. For more information, see [Health Colors and Statuses](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html) .

Color -> (string)

Represents the color indicator that gives you information about the health of the EC2 instance. For more information, see [Health Colors and Statuses](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html) .

Causes -> (list)

Represents the causes, which provide more information about the current health status.

(string)

LaunchedAt -> (timestamp)

The time at which the EC2 instance was launched.

ApplicationMetrics -> (structure)

Request metrics from your application.

Duration -> (integer)

The amount of time that the metrics cover (usually 10 seconds). For example, you might have 5 requests (`request_count` ) within the most recent time slice of 10 seconds (`duration` ).

RequestCount -> (integer)

Average number of requests handled by the web server per second over the last 10 seconds.

StatusCodes -> (structure)

Represents the percentage of requests over the last 10 seconds that resulted in each type of status code response.

Status2xx -> (integer)

The percentage of requests over the last 10 seconds that resulted in a 2xx (200, 201, etc.) status code.

Status3xx -> (integer)

The percentage of requests over the last 10 seconds that resulted in a 3xx (300, 301, etc.) status code.

Status4xx -> (integer)

The percentage of requests over the last 10 seconds that resulted in a 4xx (400, 401, etc.) status code.

Status5xx -> (integer)

The percentage of requests over the last 10 seconds that resulted in a 5xx (500, 501, etc.) status code.

Latency -> (structure)

Represents the average latency for the slowest X percent of requests over the last 10 seconds. Latencies are in seconds with one millisecond resolution.

P999 -> (double)

The average latency for the slowest 0.1 percent of requests over the last 10 seconds.

P99 -> (double)

The average latency for the slowest 1 percent of requests over the last 10 seconds.

P95 -> (double)

The average latency for the slowest 5 percent of requests over the last 10 seconds.

P90 -> (double)

The average latency for the slowest 10 percent of requests over the last 10 seconds.

P85 -> (double)

The average latency for the slowest 15 percent of requests over the last 10 seconds.

P75 -> (double)

The average latency for the slowest 25 percent of requests over the last 10 seconds.

P50 -> (double)

The average latency for the slowest 50 percent of requests over the last 10 seconds.

P10 -> (double)

The average latency for the slowest 90 percent of requests over the last 10 seconds.

System -> (structure)

Operating system metrics from the instance.

CPUUtilization -> (structure)

CPU utilization metrics for the instance.

User -> (double)

Percentage of time that the CPU has spent in the `User` state over the last 10 seconds.

Nice -> (double)

Available on Linux environments only.

Percentage of time that the CPU has spent in the `Nice` state over the last 10 seconds.

System -> (double)

Available on Linux environments only.

Percentage of time that the CPU has spent in the `System` state over the last 10 seconds.

Idle -> (double)

Percentage of time that the CPU has spent in the `Idle` state over the last 10 seconds.

IOWait -> (double)

Available on Linux environments only.

Percentage of time that the CPU has spent in the `I/O Wait` state over the last 10 seconds.

IRQ -> (double)

Available on Linux environments only.

Percentage of time that the CPU has spent in the `IRQ` state over the last 10 seconds.

SoftIRQ -> (double)

Available on Linux environments only.

Percentage of time that the CPU has spent in the `SoftIRQ` state over the last 10 seconds.

Privileged -> (double)

Available on Windows environments only.

Percentage of time that the CPU has spent in the `Privileged` state over the last 10 seconds.

LoadAverage -> (list)

Load average in the last 1-minute, 5-minute, and 15-minute periods. For more information, see [Operating System Metrics](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-metrics.html#health-enhanced-metrics-os) .

(double)

Deployment -> (structure)

Information about the most recent deployment to an instance.

VersionLabel -> (string)

The version label of the application version in the deployment.

DeploymentId -> (long)

The ID of the deployment. This number increases by one each time that you deploy source code or change instance configuration settings.

Status -> (string)

The status of the deployment:

- `In Progress` : The deployment is in progress.
- `Deployed` : The deployment succeeded.
- `Failed` : The deployment failed.

DeploymentTime -> (timestamp)

For in-progress deployments, the time that the deployment started.

For completed deployments, the time that the deployment ended.

AvailabilityZone -> (string)

The availability zone in which the instance runs.

InstanceType -> (string)

The instanceâs type.

RefreshedAt -> (timestamp)

The date and time that the health information was retrieved.

NextToken -> (string)

Pagination token for the next page of results, if available.