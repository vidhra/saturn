# configure-health-checkÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/configure-health-check.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/configure-health-check.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/index.html#cli-aws-elb) ]

# configure-health-check

## Description

Specifies the health check settings to use when evaluating the health state of your EC2 instances.

For more information, see [Configure Health Checks for Your Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-healthchecks.html) in the *Classic Load Balancers Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/ConfigureHealthCheck)

## Synopsis

```
configure-health-check
--load-balancer-name <value>
--health-check <value>
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

`--load-balancer-name` (string)

The name of the load balancer.

`--health-check` (structure)

The configuration information.

Target -> (string)

The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range of valid ports is one (1) through 65535.

TCP is the default, specified as a TCP: port pair, for example â[TCP:5000](TCP:5000)â. In this case, a health check simply attempts to open a TCP connection to the instance on the specified port. Failure to connect within the configured timeout is considered unhealthy.

SSL is also specified as SSL: port pair, for example, SSL:5000.

For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a [HTTP:port;/;PathToPing](HTTP:port;/;PathToPing); grouping, for example â[HTTP:80/weather/us/wa/seattle](HTTP:80/weather/us/wa/seattle)â. In this case, a HTTP GET request is issued to the instance on the given port and path. Any answer other than â200 OKâ within the timeout period is considered unhealthy.

The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.

Interval -> (integer)

The approximate interval, in seconds, between health checks of an individual instance.

Timeout -> (integer)

The amount of time, in seconds, during which no response means a failed health check.

This value must be less than the `Interval` value.

UnhealthyThreshold -> (integer)

The number of consecutive health check failures required before moving the instance to the `Unhealthy` state.

HealthyThreshold -> (integer)

The number of consecutive health checks successes required before moving the instance to the `Healthy` state.

Shorthand Syntax:

```
Target=string,Interval=integer,Timeout=integer,UnhealthyThreshold=integer,HealthyThreshold=integer
```

JSON Syntax:

```
{
  "Target": "string",
  "Interval": integer,
  "Timeout": integer,
  "UnhealthyThreshold": integer,
  "HealthyThreshold": integer
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To specify the health check settings for your backend EC2 instances**

This example specifies the health check settings used to evaluate the health of your backend EC2 instances.

Command:

```
aws elb configure-health-check --load-balancer-name my-load-balancer --health-check Target=HTTP:80/png,Interval=30,UnhealthyThreshold=2,HealthyThreshold=2,Timeout=3
```

Output:

```
{
   "HealthCheck": {
       "HealthyThreshold": 2,
       "Interval": 30,
       "Target": "HTTP:80/png",
       "Timeout": 3,
       "UnhealthyThreshold": 2
   }
}
```

## Output

HealthCheck -> (structure)

The updated health check.

Target -> (string)

The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range of valid ports is one (1) through 65535.

TCP is the default, specified as a TCP: port pair, for example â[TCP:5000](TCP:5000)â. In this case, a health check simply attempts to open a TCP connection to the instance on the specified port. Failure to connect within the configured timeout is considered unhealthy.

SSL is also specified as SSL: port pair, for example, SSL:5000.

For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a [HTTP:port;/;PathToPing](HTTP:port;/;PathToPing); grouping, for example â[HTTP:80/weather/us/wa/seattle](HTTP:80/weather/us/wa/seattle)â. In this case, a HTTP GET request is issued to the instance on the given port and path. Any answer other than â200 OKâ within the timeout period is considered unhealthy.

The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.

Interval -> (integer)

The approximate interval, in seconds, between health checks of an individual instance.

Timeout -> (integer)

The amount of time, in seconds, during which no response means a failed health check.

This value must be less than the `Interval` value.

UnhealthyThreshold -> (integer)

The number of consecutive health check failures required before moving the instance to the `Unhealthy` state.

HealthyThreshold -> (integer)

The number of consecutive health checks successes required before moving the instance to the `Healthy` state.