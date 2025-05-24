# describe-traffic-sourcesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-traffic-sources.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-traffic-sources.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [autoscaling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/index.html#cli-aws-autoscaling) ]

# describe-traffic-sources

## Description

Gets information about the traffic sources for the specified Auto Scaling group.

You can optionally provide a traffic source type. If you provide a traffic source type, then the results only include that traffic source type.

If you do not provide a traffic source type, then the results include all the traffic sources for the specified Auto Scaling group.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeTrafficSources)

## Synopsis

```
describe-traffic-sources
--auto-scaling-group-name <value>
[--traffic-source-type <value>]
[--next-token <value>]
[--max-records <value>]
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

`--auto-scaling-group-name` (string)

The name of the Auto Scaling group.

`--traffic-source-type` (string)

The traffic source type that you want to describe.

The following lists the valid values:

- `elb` if the traffic source is a Classic Load Balancer.
- `elbv2` if the traffic source is a Application Load Balancer, Gateway Load Balancer, or Network Load Balancer.
- `vpc-lattice` if the traffic source is VPC Lattice.

`--next-token` (string)

The token for the next set of items to return. (You received this token from a previous call.)

`--max-records` (integer)

The maximum number of items to return with this call. The maximum value is `50` .

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

TrafficSources -> (list)

Information about the traffic sources.

(structure)

Describes the state of a traffic source.

TrafficSource -> (string)

This is replaced by `Identifier` .

State -> (string)

Describes the current state of a traffic source.

The state values are as follows:

- `Adding` - The Auto Scaling instances are being registered with the load balancer or target group.
- `Added` - All Auto Scaling instances are registered with the load balancer or target group.
- `InService` - For an Elastic Load Balancing load balancer or target group, at least one Auto Scaling instance passed an `ELB` health check. For VPC Lattice, at least one Auto Scaling instance passed an `VPC_LATTICE` health check.
- `Removing` - The Auto Scaling instances are being deregistered from the load balancer or target group. If connection draining (deregistration delay) is enabled, Elastic Load Balancing or VPC Lattice waits for in-flight requests to complete before deregistering the instances.
- `Removed` - All Auto Scaling instances are deregistered from the load balancer or target group.

Identifier -> (string)

The unique identifier of the traffic source.

Type -> (string)

Provides additional context for the value of `Identifier` .

The following lists the valid values:

- `elb` if `Identifier` is the name of a Classic Load Balancer.
- `elbv2` if `Identifier` is the ARN of an Application Load Balancer, Gateway Load Balancer, or Network Load Balancer target group.
- `vpc-lattice` if `Identifier` is the ARN of a VPC Lattice target group.

Required if the identifier is the name of a Classic Load Balancer.

NextToken -> (string)

This string indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the `NextToken` value when requesting the next set of items. This value is null when there are no more items to return.