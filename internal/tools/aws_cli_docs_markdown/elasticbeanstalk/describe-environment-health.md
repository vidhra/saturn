# describe-environment-healthÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-environment-health.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-environment-health.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticbeanstalk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/index.html#cli-aws-elasticbeanstalk) ]

# describe-environment-health

## Description

Returns information about the overall health of the specified environment. The **DescribeEnvironmentHealth** operation is only available with AWS Elastic Beanstalk Enhanced Health.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/DescribeEnvironmentHealth)

## Synopsis

```
describe-environment-health
[--environment-name <value>]
[--environment-id <value>]
[--attribute-names <value>]
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

Specify the environment by name.

You must specify either this or an EnvironmentName, or both.

`--environment-id` (string)

Specify the environment by ID.

You must specify either this or an EnvironmentName, or both.

`--attribute-names` (list)

Specify the response elements to return. To retrieve all attributes, set to `All` . If no attribute names are specified, returns the name of the environment.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  Status
  Color
  Causes
  ApplicationMetrics
  InstancesHealth
  All
  HealthStatus
  RefreshedAt
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

**To view environment health**

The following command retrieves overall health information for an environment named `my-env`:

```
aws elasticbeanstalk describe-environment-health --environment-name my-env --attribute-names All
```

Output:

```
{
    "Status": "Ready",
    "EnvironmentName": "my-env",
    "Color": "Green",
    "ApplicationMetrics": {
        "Duration": 10,
        "Latency": {
            "P99": 0.004,
            "P75": 0.002,
            "P90": 0.003,
            "P95": 0.004,
            "P85": 0.003,
            "P10": 0.001,
            "P999": 0.004,
            "P50": 0.001
        },
        "RequestCount": 45,
        "StatusCodes": {
            "Status3xx": 0,
            "Status2xx": 45,
            "Status5xx": 0,
            "Status4xx": 0
        }
    },
    "RefreshedAt": "2015-08-20T21:09:18Z",
    "HealthStatus": "Ok",
    "InstancesHealth": {
        "Info": 0,
        "Ok": 1,
        "Unknown": 0,
        "Severe": 0,
        "Warning": 0,
        "Degraded": 0,
        "NoData": 0,
        "Pending": 0
    },
    "Causes": []
}
```

Health information is only available for environments with enhanced health reporting enabled. For more information, see [Enhanced Health Reporting and Monitoring](http://integ-docs-aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced.html) in the *AWS Elastic Beanstalk Developer Guide*.

## Output

EnvironmentName -> (string)

The environmentâs name.

HealthStatus -> (string)

The [health status](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html) of the environment. For example, `Ok` .

Status -> (string)

The environmentâs operational status. `Ready` , `Launching` , `Updating` , `Terminating` , or `Terminated` .

Color -> (string)

The [health color](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html) of the environment.

Causes -> (list)

Descriptions of the data that contributed to the environmentâs current health status.

(string)

ApplicationMetrics -> (structure)

Application request metrics for the environment.

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

InstancesHealth -> (structure)

Summary health information for the instances in the environment.

NoData -> (integer)

**Grey.** AWS Elastic Beanstalk and the health agent are reporting no data on an instance.

Unknown -> (integer)

**Grey.** AWS Elastic Beanstalk and the health agent are reporting an insufficient amount of data on an instance.

Pending -> (integer)

**Grey.** An operation is in progress on an instance within the command timeout.

Ok -> (integer)

**Green.** An instance is passing health checks and the health agent is not reporting any problems.

Info -> (integer)

**Green.** An operation is in progress on an instance.

Warning -> (integer)

**Yellow.** The health agent is reporting a moderate number of request failures or other issues for an instance or environment.

Degraded -> (integer)

**Red.** The health agent is reporting a high number of request failures or other issues for an instance or environment.

Severe -> (integer)

**Red.** The health agent is reporting a very high number of request failures or other issues for an instance or environment.

RefreshedAt -> (timestamp)

The date and time that the health information was retrieved.