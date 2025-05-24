# create-target-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/create-target-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/create-target-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [vpc-lattice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/index.html#cli-aws-vpc-lattice) ]

# create-target-group

## Description

Creates a target group. A target group is a collection of targets, or compute resources, that run your application or service. A target group can only be used by a single service.

For more information, see [Target groups](https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html) in the *Amazon VPC Lattice User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/vpc-lattice-2022-11-30/CreateTargetGroup)

## Synopsis

```
create-target-group
[--client-token <value>]
[--config <value>]
--name <value>
[--tags <value>]
--type <value>
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

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters arenât identical, the retry fails.

`--config` (structure)

The target group configuration.

healthCheck -> (structure)

The health check configuration. Not supported if the target group type is `LAMBDA` or `ALB` .

enabled -> (boolean)

Indicates whether health checking is enabled.

healthCheckIntervalSeconds -> (integer)

The approximate amount of time, in seconds, between health checks of an individual target. The range is 5â300 seconds. The default is 30 seconds.

healthCheckTimeoutSeconds -> (integer)

The amount of time, in seconds, to wait before reporting a target as unhealthy. The range is 1â120 seconds. The default is 5 seconds.

healthyThresholdCount -> (integer)

The number of consecutive successful health checks required before considering an unhealthy target healthy. The range is 2â10. The default is 5.

matcher -> (tagged union structure)

The codes to use when checking for a successful response from a target.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `httpCode`.

httpCode -> (string)

The HTTP code to use when checking for a successful response from a target.

path -> (string)

The destination for health checks on the targets. If the protocol version is `HTTP/1.1` or `HTTP/2` , specify a valid URI (for example, `/path?query` ). The default path is `/` . Health checks are not supported if the protocol version is `gRPC` , however, you can choose `HTTP/1.1` or `HTTP/2` and specify a valid URI.

port -> (integer)

The port used when performing health checks on targets. The default setting is the port that a target receives traffic on.

protocol -> (string)

The protocol used when performing health checks on targets. The possible protocols are `HTTP` and `HTTPS` . The default is `HTTP` .

protocolVersion -> (string)

The protocol version used when performing health checks on targets. The possible protocol versions are `HTTP1` and `HTTP2` .

unhealthyThresholdCount -> (integer)

The number of consecutive failed health checks required before considering a target unhealthy. The range is 2â10. The default is 2.

ipAddressType -> (string)

The type of IP address used for the target group. Supported only if the target group type is `IP` . The default is `IPV4` .

lambdaEventStructureVersion -> (string)

The version of the event structure that your Lambda function receives. Supported only if the target group type is `LAMBDA` . The default is `V1` .

port -> (integer)

The port on which the targets are listening. For HTTP, the default is 80. For HTTPS, the default is 443. Not supported if the target group type is `LAMBDA` .

protocol -> (string)

The protocol to use for routing traffic to the targets. The default is the protocol of the target group. Not supported if the target group type is `LAMBDA` .

protocolVersion -> (string)

The protocol version. The default is `HTTP1` . Not supported if the target group type is `LAMBDA` .

vpcIdentifier -> (string)

The ID of the VPC. Not supported if the target group type is `LAMBDA` .

Shorthand Syntax:

```
healthCheck={enabled=boolean,healthCheckIntervalSeconds=integer,healthCheckTimeoutSeconds=integer,healthyThresholdCount=integer,matcher={httpCode=string},path=string,port=integer,protocol=string,protocolVersion=string,unhealthyThresholdCount=integer},ipAddressType=string,lambdaEventStructureVersion=string,port=integer,protocol=string,protocolVersion=string,vpcIdentifier=string
```

JSON Syntax:

```
{
  "healthCheck": {
    "enabled": true|false,
    "healthCheckIntervalSeconds": integer,
    "healthCheckTimeoutSeconds": integer,
    "healthyThresholdCount": integer,
    "matcher": {
      "httpCode": "string"
    },
    "path": "string",
    "port": integer,
    "protocol": "HTTP"|"HTTPS"|"TCP",
    "protocolVersion": "HTTP1"|"HTTP2",
    "unhealthyThresholdCount": integer
  },
  "ipAddressType": "IPV4"|"IPV6",
  "lambdaEventStructureVersion": "V1"|"V2",
  "port": integer,
  "protocol": "HTTP"|"HTTPS"|"TCP",
  "protocolVersion": "HTTP1"|"HTTP2"|"GRPC",
  "vpcIdentifier": "string"
}
```

`--name` (string)

The name of the target group. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You canât use a hyphen as the first or last character, or immediately after another hyphen.

`--tags` (map)

The tags for the target group.

key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 128 Unicode characters. Valid characters are Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @ May not begin with `aws:` .

value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters. Valid characters are Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--type` (string)

The type of target group.

Possible values:

- `IP`
- `LAMBDA`
- `INSTANCE`
- `ALB`

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

**Example 1: To create a target group of type INSTANCE**

The following `create-target-group` example creates a target group with the specified name, type, and configuration.

```
aws vpc-lattice create-target-group \
    --name my-lattice-target-group-instance \
    --type INSTANCE \
    --config file://tg-config.json
```

Contents of `tg-config.json`:

```
{
    "port": 443,
    "protocol": "HTTPS",
    "protocolVersion": "HTTP1",
    "vpcIdentifier": "vpc-f1663d9868EXAMPLE"
}
```

Output:

```
{
    "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:targetgroup/tg-0eaa4b9ab4EXAMPLE",
    "config": {
        "healthCheck": {
            "enabled": true,
            "healthCheckIntervalSeconds": 30,
            "healthCheckTimeoutSeconds": 5,
            "healthyThresholdCount": 5,
            "matcher": {
                "httpCode": "200"
            },
            "path": "/",
            "protocol": "HTTPS",
            "protocolVersion": "HTTP1",
            "unhealthyThresholdCount": 2
        },
        "port": 443,
        "protocol": "HTTPS",
        "protocolVersion": "HTTP1",
        "vpcIdentifier": "vpc-f1663d9868EXAMPLE"
    },
    "id": "tg-0eaa4b9ab4EXAMPLE",
    "name": "my-lattice-target-group-instance",
    "status": "CREATE_IN_PROGRESS",
    "type": "INSTANCE"
}
```

**Example 2: To create a target group of type IP**

The following `create-target-group` example creates a target group with the specified name, type, and configuration.

```
aws vpc-lattice create-target-group \
    --name my-lattice-target-group-ip \
    --type IP \
    --config file://tg-config.json
```

Contents of `tg-config.json`:

```
{
    "ipAddressType": "IPV4",
    "port": 443,
    "protocol": "HTTPS",
    "protocolVersion": "HTTP1",
    "vpcIdentifier": "vpc-f1663d9868EXAMPLE"
}
```

Output:

```
{
    "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:targetgroup/tg-0eaa4b9ab4EXAMPLE",
    "config": {
        "healthCheck": {
            "enabled": true,
            "healthCheckIntervalSeconds": 30,
            "healthCheckTimeoutSeconds": 5,
            "healthyThresholdCount": 5,
            "matcher": {
                "httpCode": "200"
            },
            "path": "/",
            "protocol": "HTTPS",
            "protocolVersion": "HTTP1",
            "unhealthyThresholdCount": 2
        },
        "ipAddressType": "IPV4",
        "port": 443,
        "protocol": "HTTPS",
        "protocolVersion": "HTTP1",
        "vpcIdentifier": "vpc-f1663d9868EXAMPLE"
    },
    "id": "tg-0eaa4b9ab4EXAMPLE",
    "name": "my-lattice-target-group-ip",
    "status": "CREATE_IN_PROGRESS",
    "type": "IP"
}
```

**Example 3: To create a target group of type LAMBDA**

The following `create-target-group` example creates a target group with the specified name, type, and configuration.

```
aws vpc-lattice create-target-group \
    --name my-lattice-target-group-lambda \
    --type LAMBDA
```

Output:

```
{
    "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:targetgroup/tg-0eaa4b9ab4EXAMPLE",
    "id": "tg-0eaa4b9ab4EXAMPLE",
    "name": "my-lattice-target-group-lambda",
    "status": "CREATE_IN_PROGRESS",
    "type": "LAMBDA"
}
```

**Example 4: To create a target group of type ALB**

The following `create-target-group` example creates a target group with the specified name, type, and configuration.

```
aws vpc-lattice create-target-group \
    --name my-lattice-target-group-alb \
    --type ALB \
    --config file://tg-config.json
```

Contents of `tg-config.json`:

```
{
    "port": 443,
    "protocol": "HTTPS",
    "protocolVersion": "HTTP1",
    "vpcIdentifier": "vpc-f1663d9868EXAMPLE"
}
```

Output:

```
{
    "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:targetgroup/tg-0eaa4b9ab4EXAMPLE",
    "config": {
        "port": 443,
        "protocol": "HTTPS",
        "protocolVersion": "HTTP1",
        "vpcIdentifier": "vpc-f1663d9868EXAMPLE"
    },
    "id": "tg-0eaa4b9ab4EXAMPLE",
    "name": "my-lattice-target-group-alb",
    "status": "CREATE_IN_PROGRESS",
    "type": "ALB"
}
```

For more information, see [Target groups](https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html) in the *Amazon VPC Lattice User Guide*.

## Output

arn -> (string)

The Amazon Resource Name (ARN) of the target group.

config -> (structure)

The target group configuration.

healthCheck -> (structure)

The health check configuration. Not supported if the target group type is `LAMBDA` or `ALB` .

enabled -> (boolean)

Indicates whether health checking is enabled.

healthCheckIntervalSeconds -> (integer)

The approximate amount of time, in seconds, between health checks of an individual target. The range is 5â300 seconds. The default is 30 seconds.

healthCheckTimeoutSeconds -> (integer)

The amount of time, in seconds, to wait before reporting a target as unhealthy. The range is 1â120 seconds. The default is 5 seconds.

healthyThresholdCount -> (integer)

The number of consecutive successful health checks required before considering an unhealthy target healthy. The range is 2â10. The default is 5.

matcher -> (tagged union structure)

The codes to use when checking for a successful response from a target.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `httpCode`.

httpCode -> (string)

The HTTP code to use when checking for a successful response from a target.

path -> (string)

The destination for health checks on the targets. If the protocol version is `HTTP/1.1` or `HTTP/2` , specify a valid URI (for example, `/path?query` ). The default path is `/` . Health checks are not supported if the protocol version is `gRPC` , however, you can choose `HTTP/1.1` or `HTTP/2` and specify a valid URI.

port -> (integer)

The port used when performing health checks on targets. The default setting is the port that a target receives traffic on.

protocol -> (string)

The protocol used when performing health checks on targets. The possible protocols are `HTTP` and `HTTPS` . The default is `HTTP` .

protocolVersion -> (string)

The protocol version used when performing health checks on targets. The possible protocol versions are `HTTP1` and `HTTP2` .

unhealthyThresholdCount -> (integer)

The number of consecutive failed health checks required before considering a target unhealthy. The range is 2â10. The default is 2.

ipAddressType -> (string)

The type of IP address used for the target group. Supported only if the target group type is `IP` . The default is `IPV4` .

lambdaEventStructureVersion -> (string)

The version of the event structure that your Lambda function receives. Supported only if the target group type is `LAMBDA` . The default is `V1` .

port -> (integer)

The port on which the targets are listening. For HTTP, the default is 80. For HTTPS, the default is 443. Not supported if the target group type is `LAMBDA` .

protocol -> (string)

The protocol to use for routing traffic to the targets. The default is the protocol of the target group. Not supported if the target group type is `LAMBDA` .

protocolVersion -> (string)

The protocol version. The default is `HTTP1` . Not supported if the target group type is `LAMBDA` .

vpcIdentifier -> (string)

The ID of the VPC. Not supported if the target group type is `LAMBDA` .

id -> (string)

The ID of the target group.

name -> (string)

The name of the target group.

status -> (string)

The status. You can retry the operation if the status is `CREATE_FAILED` . However, if you retry it while the status is `CREATE_IN_PROGRESS` , there is no change in the status.

type -> (string)

The type of target group.