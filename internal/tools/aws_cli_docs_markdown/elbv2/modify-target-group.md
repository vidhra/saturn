# modify-target-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-target-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-target-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elbv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/index.html#cli-aws-elbv2) ]

# modify-target-group

## Description

Modifies the health checks used when evaluating the health state of the targets in the specified target group.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/ModifyTargetGroup)

## Synopsis

```
modify-target-group
--target-group-arn <value>
[--health-check-protocol <value>]
[--health-check-port <value>]
[--health-check-path <value>]
[--health-check-enabled | --no-health-check-enabled]
[--health-check-interval-seconds <value>]
[--health-check-timeout-seconds <value>]
[--healthy-threshold-count <value>]
[--unhealthy-threshold-count <value>]
[--matcher <value>]
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

`--target-group-arn` (string)

The Amazon Resource Name (ARN) of the target group.

`--health-check-protocol` (string)

The protocol the load balancer uses when performing health checks on targets. For Application Load Balancers, the default is HTTP. For Network Load Balancers and Gateway Load Balancers, the default is TCP. The TCP protocol is not supported for health checks if the protocol of the target group is HTTP or HTTPS. It is supported for health checks only if the protocol of the target group is TCP, TLS, UDP, or TCP_UDP. The GENEVE, TLS, UDP, and TCP_UDP protocols are not supported for health checks.

Possible values:

- `HTTP`
- `HTTPS`
- `TCP`
- `TLS`
- `UDP`
- `TCP_UDP`
- `GENEVE`

`--health-check-port` (string)

The port the load balancer uses when performing health checks on targets.

`--health-check-path` (string)

[HTTP/HTTPS health checks] The destination for health checks on the targets.

[HTTP1 or HTTP2 protocol version] The ping path. The default is /.

[GRPC protocol version] The path of a custom health check method with the format /package.service/method. The default is /Amazon Web Services.ALB/healthcheck.

`--health-check-enabled` | `--no-health-check-enabled` (boolean)

Indicates whether health checks are enabled.

`--health-check-interval-seconds` (integer)

The approximate amount of time, in seconds, between health checks of an individual target.

`--health-check-timeout-seconds` (integer)

[HTTP/HTTPS health checks] The amount of time, in seconds, during which no response means a failed health check.

`--healthy-threshold-count` (integer)

The number of consecutive health checks successes required before considering an unhealthy target healthy.

`--unhealthy-threshold-count` (integer)

The number of consecutive health check failures required before considering the target unhealthy.

`--matcher` (structure)

[HTTP/HTTPS health checks] The HTTP or gRPC codes to use when checking for a successful response from a target. For target groups with a protocol of TCP, TCP_UDP, UDP or TLS the range is 200-599. For target groups with a protocol of HTTP or HTTPS, the range is 200-499. For target groups with a protocol of GENEVE, the range is 200-399.

HttpCode -> (string)

For Application Load Balancers, you can specify values between 200 and 499, with the default value being 200. You can specify multiple values (for example, â200,202â) or a range of values (for example, â200-299â).

For Network Load Balancers, you can specify values between 200 and 599, with the default value being 200-399. You can specify multiple values (for example, â200,202â) or a range of values (for example, â200-299â).

For Gateway Load Balancers, this must be â200â399â.

Note that when using shorthand syntax, some values such as commas need to be escaped.

GrpcCode -> (string)

You can specify values between 0 and 99. You can specify multiple values (for example, â0,1â) or a range of values (for example, â0-5â). The default value is 12.

Shorthand Syntax:

```
HttpCode=string,GrpcCode=string
```

JSON Syntax:

```
{
  "HttpCode": "string",
  "GrpcCode": "string"
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

**To modify the health check configuration for a target group**

The following `modify-target-group` example changes the configuration of the health checks used to evaluate the health of the targets for the specified target group. Note that due to the way the CLI parses commas, you must surround the range for the `--matcher` option with single quotes instead of double quotes.

```
aws elbv2 modify-target-group \
    --target-group-arn arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-https-targets/2453ed029918f21f \
    --health-check-protocol HTTPS \
    --health-check-port 443 \
    --matcher HttpCode='200,299'
```

Output:

```
{
    "TargetGroups": [
        {
            "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-https-targets/2453ed029918f21f",
            "TargetGroupName": "my-https-targets",
            "Protocol": "HTTPS",
            "Port": 443,
            "VpcId": "vpc-3ac0fb5f",
            "HealthCheckProtocol": "HTTPS",
            "HealthCheckPort": "443",
            "HealthCheckEnabled": true,
            "HealthCheckIntervalSeconds": 30,
            "HealthCheckTimeoutSeconds": 5,
            "HealthyThresholdCount": 5,
            "UnhealthyThresholdCount": 2,
            "Matcher": {
                "HttpCode": "200,299"
            },
            "LoadBalancerArns": [
                "arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188"
            ],
            "TargetType": "instance",
            "ProtocolVersion": "HTTP1",
            "IpAddressType": "ipv4"
        }
    ]
}
```

For more information, see [Target groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html) in the *Applicaion Load Balancers Guide*.

## Output

TargetGroups -> (list)

Information about the modified target group.

(structure)

Information about a target group.

TargetGroupArn -> (string)

The Amazon Resource Name (ARN) of the target group.

TargetGroupName -> (string)

The name of the target group.

Protocol -> (string)

The protocol to use for routing traffic to the targets.

Port -> (integer)

The port on which the targets are listening. This parameter is not used if the target is a Lambda function.

VpcId -> (string)

The ID of the VPC for the targets.

HealthCheckProtocol -> (string)

The protocol to use to connect with the target. The GENEVE, TLS, UDP, and TCP_UDP protocols are not supported for health checks.

HealthCheckPort -> (string)

The port to use to connect with the target.

HealthCheckEnabled -> (boolean)

Indicates whether health checks are enabled.

HealthCheckIntervalSeconds -> (integer)

The approximate amount of time, in seconds, between health checks of an individual target.

HealthCheckTimeoutSeconds -> (integer)

The amount of time, in seconds, during which no response means a failed health check.

HealthyThresholdCount -> (integer)

The number of consecutive health checks successes required before considering an unhealthy target healthy.

UnhealthyThresholdCount -> (integer)

The number of consecutive health check failures required before considering the target unhealthy.

HealthCheckPath -> (string)

The destination for health checks on the targets.

Matcher -> (structure)

The HTTP or gRPC codes to use when checking for a successful response from a target.

HttpCode -> (string)

For Application Load Balancers, you can specify values between 200 and 499, with the default value being 200. You can specify multiple values (for example, â200,202â) or a range of values (for example, â200-299â).

For Network Load Balancers, you can specify values between 200 and 599, with the default value being 200-399. You can specify multiple values (for example, â200,202â) or a range of values (for example, â200-299â).

For Gateway Load Balancers, this must be â200â399â.

Note that when using shorthand syntax, some values such as commas need to be escaped.

GrpcCode -> (string)

You can specify values between 0 and 99. You can specify multiple values (for example, â0,1â) or a range of values (for example, â0-5â). The default value is 12.

LoadBalancerArns -> (list)

The Amazon Resource Name (ARN) of the load balancer that routes traffic to this target group. You can use each target group with only one load balancer.

(string)

TargetType -> (string)

The type of target that you must specify when registering targets with this target group. The possible values are `instance` (register targets by instance ID), `ip` (register targets by IP address), `lambda` (register a single Lambda function as a target), or `alb` (register a single Application Load Balancer as a target).

ProtocolVersion -> (string)

[HTTP/HTTPS protocol] The protocol version. The possible values are `GRPC` , `HTTP1` , and `HTTP2` .

IpAddressType -> (string)

The IP address type. The default value is `ipv4` .