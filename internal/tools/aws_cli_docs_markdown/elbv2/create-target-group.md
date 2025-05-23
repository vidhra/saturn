# create-target-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-target-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-target-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elbv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/index.html#cli-aws-elbv2) ]

# create-target-group

## Description

Creates a target group.

For more information, see the following:

- [Target groups for your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html)
- [Target groups for your Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html)
- [Target groups for your Gateway Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/target-groups.html)

This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple target groups with the same settings, each call succeeds.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/CreateTargetGroup)

## Synopsis

```
create-target-group
--name <value>
[--protocol <value>]
[--protocol-version <value>]
[--port <value>]
[--vpc-id <value>]
[--health-check-protocol <value>]
[--health-check-port <value>]
[--health-check-enabled | --no-health-check-enabled]
[--health-check-path <value>]
[--health-check-interval-seconds <value>]
[--health-check-timeout-seconds <value>]
[--healthy-threshold-count <value>]
[--unhealthy-threshold-count <value>]
[--matcher <value>]
[--target-type <value>]
[--tags <value>]
[--ip-address-type <value>]
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

The name of the target group.

This name must be unique per region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.

`--protocol` (string)

The protocol to use for routing traffic to the targets. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocols are TCP, TLS, UDP, or TCP_UDP. For Gateway Load Balancers, the supported protocol is GENEVE. A TCP_UDP listener must be associated with a TCP_UDP target group. If the target is a Lambda function, this parameter does not apply.

Possible values:

- `HTTP`
- `HTTPS`
- `TCP`
- `TLS`
- `UDP`
- `TCP_UDP`
- `GENEVE`

`--protocol-version` (string)

[HTTP/HTTPS protocol] The protocol version. Specify `GRPC` to send requests to targets using gRPC. Specify `HTTP2` to send requests to targets using HTTP/2. The default is `HTTP1` , which sends requests to targets using HTTP/1.1.

`--port` (integer)

The port on which the targets receive traffic. This port is used unless you specify a port override when registering the target. If the target is a Lambda function, this parameter does not apply. If the protocol is GENEVE, the supported port is 6081.

`--vpc-id` (string)

The identifier of the virtual private cloud (VPC). If the target is a Lambda function, this parameter does not apply. Otherwise, this parameter is required.

`--health-check-protocol` (string)

The protocol the load balancer uses when performing health checks on targets. For Application Load Balancers, the default is HTTP. For Network Load Balancers and Gateway Load Balancers, the default is TCP. The TCP protocol is not supported for health checks if the protocol of the target group is HTTP or HTTPS. The GENEVE, TLS, UDP, and TCP_UDP protocols are not supported for health checks.

Possible values:

- `HTTP`
- `HTTPS`
- `TCP`
- `TLS`
- `UDP`
- `TCP_UDP`
- `GENEVE`

`--health-check-port` (string)

The port the load balancer uses when performing health checks on targets. If the protocol is HTTP, HTTPS, TCP, TLS, UDP, or TCP_UDP, the default is `traffic-port` , which is the port on which each target receives traffic from the load balancer. If the protocol is GENEVE, the default is port 80.

`--health-check-enabled` | `--no-health-check-enabled` (boolean)

Indicates whether health checks are enabled. If the target type is `lambda` , health checks are disabled by default but can be enabled. If the target type is `instance` , `ip` , or `alb` , health checks are always enabled and canât be disabled.

`--health-check-path` (string)

[HTTP/HTTPS health checks] The destination for health checks on the targets.

[HTTP1 or HTTP2 protocol version] The ping path. The default is /.

[GRPC protocol version] The path of a custom health check method with the format /package.service/method. The default is /Amazon Web Services.ALB/healthcheck.

`--health-check-interval-seconds` (integer)

The approximate amount of time, in seconds, between health checks of an individual target. The range is 5-300. If the target group protocol is TCP, TLS, UDP, TCP_UDP, HTTP or HTTPS, the default is 30 seconds. If the target group protocol is GENEVE, the default is 10 seconds. If the target type is `lambda` , the default is 35 seconds.

`--health-check-timeout-seconds` (integer)

The amount of time, in seconds, during which no response from a target means a failed health check. The range is 2â120 seconds. For target groups with a protocol of HTTP, the default is 6 seconds. For target groups with a protocol of TCP, TLS or HTTPS, the default is 10 seconds. For target groups with a protocol of GENEVE, the default is 5 seconds. If the target type is `lambda` , the default is 30 seconds.

`--healthy-threshold-count` (integer)

The number of consecutive health check successes required before considering a target healthy. The range is 2-10. If the target group protocol is TCP, TCP_UDP, UDP, TLS, HTTP or HTTPS, the default is 5. For target groups with a protocol of GENEVE, the default is 5. If the target type is `lambda` , the default is 5.

`--unhealthy-threshold-count` (integer)

The number of consecutive health check failures required before considering a target unhealthy. The range is 2-10. If the target group protocol is TCP, TCP_UDP, UDP, TLS, HTTP or HTTPS, the default is 2. For target groups with a protocol of GENEVE, the default is 2. If the target type is `lambda` , the default is 5.

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

`--target-type` (string)

The type of target that you must specify when registering targets with this target group. You canât specify targets for a target group using more than one target type.

- `instance` - Register targets by instance ID. This is the default value.
- `ip` - Register targets by IP address. You can specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group, the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10). You canât specify publicly routable IP addresses.
- `lambda` - Register a single Lambda function as a target.
- `alb` - Register a single Application Load Balancer as a target.

Possible values:

- `instance`
- `ip`
- `lambda`
- `alb`

`--tags` (list)

The tags to assign to the target group.

(structure)

Information about a tag.

Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--ip-address-type` (string)

The IP address type. The default value is `ipv4` .

Possible values:

- `ipv4`
- `ipv6`

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

**Example 1: To create a target group for an Application Load Balancer**

The following `create-target-group` example creates a target group for an Application Load Balancer where you register targets by instance ID (the target type is `instance`). This target group uses the HTTP protocol, port 80, and the default health check settings for an HTTP target group.

```
aws elbv2 create-target-group \
    --name my-targets \
    --protocol HTTP \
    --port 80 \
    --target-type instance \
    --vpc-id vpc-3ac0fb5f
```

Output:

```
{
    "TargetGroups": [
        {
            "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067",
            "TargetGroupName": "my-targets",
            "Protocol": "HTTP",
            "Port": 80,
            "VpcId": "vpc-3ac0fb5f",
            "HealthCheckProtocol": "HTTP",
            "HealthCheckPort": "traffic-port",
            "HealthCheckEnabled": true,
            "HealthCheckIntervalSeconds": 30,
            "HealthCheckTimeoutSeconds": 5,
            "HealthyThresholdCount": 5,
            "UnhealthyThresholdCount": 2,
            "HealthCheckPath": "/",
            "Matcher": {
                "HttpCode": "200"
            },
            "TargetType": "instance",
            "ProtocolVersion": "HTTP1",
            "IpAddressType": "ipv4"
        }
    ]
}
```

For more information, see [Create a target group](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-target-group.html) in the *User Guide for Application Load Balancers*.

**Example 2: To create a target group to route traffic from an Application Load Balancer to a Lambda function**

The following `create-target-group` example creates a target group for an Application Load Balancer where the target is a Lambda function (the target type is `lambda`). Health checks are disabled for this target group by default.

```
aws elbv2 create-target-group \
    --name my-lambda-target \
    --target-type lambda
```

Output:

```
{
    "TargetGroups": [
        {
            "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-lambda-target/a3003e085dbb8ddc",
            "TargetGroupName": "my-lambda-target",
            "HealthCheckEnabled": false,
            "HealthCheckIntervalSeconds": 35,
            "HealthCheckTimeoutSeconds": 30,
            "HealthyThresholdCount": 5,
            "UnhealthyThresholdCount": 2,
            "HealthCheckPath": "/",
            "Matcher": {
                "HttpCode": "200"
            },
            "TargetType": "lambda",
            "IpAddressType": "ipv4"
        }
    ]
}
```

For more information, see [Lambda functions as targets](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html) in the *User Guide for Application Load Balancers*.

**Example 3: To create a target group for a Network Load Balancer**

The following `create-target-group` example creates a target group for a Network Load Balancer where you register targets by IP address (the target type is `ip`). This target group uses the TCP protocol, port 80, and the default health check settings for a TCP target group.

```
aws elbv2 create-target-group \
    --name my-ip-targets \
    --protocol TCP \
    --port 80 \
    --target-type ip \
    --vpc-id vpc-3ac0fb5f
```

Output:

```
{
    "TargetGroups": [
        {
            "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-ip-targets/b6bba954d1361c78",
            "TargetGroupName": "my-ip-targets",
            "Protocol": "TCP",
            "Port": 80,
            "VpcId": "vpc-3ac0fb5f",
            "HealthCheckEnabled": true,
            "HealthCheckProtocol": "TCP",
            "HealthCheckPort": "traffic-port",
            "HealthCheckIntervalSeconds": 30,
            "HealthCheckTimeoutSeconds": 10,
            "HealthyThresholdCount": 5,
            "UnhealthyThresholdCount": 2,
            "TargetType": "ip",
            "IpAddressType": "ipv4"
        }
    ]
}
```

For more information, see [Create a target group](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-target-group.html) in the *User Guide for Network Load Balancers*.

**Example 4: To create a target group to route traffic from a Network Load Balancer to an Application Load Balancer**

The following `create-target-group` example creates a target group for a Network Load Balancer where you register an Application Load Balancer as a target (the target type is `alb`).

**aws elbv2 create-target-group**:
âname my-alb-target âprotocol TCP âport 80 âtarget-type alb âvpc-id vpc-3ac0fb5f

Output:

```
{
    "TargetGroups": [
        {
            "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-alb-target/a3003e085dbb8ddc",
            "TargetGroupName": "my-alb-target",
            "Protocol": "TCP",
            "Port": 80,
            "VpcId": "vpc-838475fe",
            "HealthCheckProtocol": "HTTP",
            "HealthCheckPort": "traffic-port",
            "HealthCheckEnabled": true,
            "HealthCheckIntervalSeconds": 30,
            "HealthCheckTimeoutSeconds": 6,
            "HealthyThresholdCount": 5,
            "UnhealthyThresholdCount": 2,
            "HealthCheckPath": "/",
            "Matcher": {
                "HttpCode": "200-399"
            },
            "TargetType": "alb",
            "IpAddressType": "ipv4"
        }
    ]
}
```

For more information, see [Create a target group with an Application Load Balancer as the target](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/application-load-balancer-target.html) in the *User Guide for Network Load Balancers*.

**Example 5: To create a target group for a Gateway Load Balancer**

The following `create-target-group` example creates a target group for a Gateway Load Balancer where the target is an instance, and the target group protocol is `GENEVE`.

```
aws elbv2 create-target-group \
    --name my-glb-targetgroup \
    --protocol GENEVE \
    --port 6081 \
    --target-type instance \
    --vpc-id vpc-838475fe
```

Output:

```
{
    "TargetGroups": [
        {
            "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-glb-targetgroup/00c3d57eacd6f40b6f",
            "TargetGroupName": "my-glb-targetgroup",
            "Protocol": "GENEVE",
            "Port": 6081,
            "VpcId": "vpc-838475fe",
            "HealthCheckProtocol": "TCP",
            "HealthCheckPort": "80",
            "HealthCheckEnabled": true,
            "HealthCheckIntervalSeconds": 10,
            "HealthCheckTimeoutSeconds": 5,
            "HealthyThresholdCount": 5,
            "UnhealthyThresholdCount": 2,
            "TargetType": "instance"
        }
    ]
}
```

For more information, see Create a target group <[https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/create-target-group.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/create-target-group.html)>`__ in the *Gateway Load Balancer User Guide*.

## Output

TargetGroups -> (list)

Information about the target group.

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