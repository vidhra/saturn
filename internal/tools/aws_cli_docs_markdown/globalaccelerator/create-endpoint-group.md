# create-endpoint-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-endpoint-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-endpoint-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [globalaccelerator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/index.html#cli-aws-globalaccelerator) ]

# create-endpoint-group

## Description

Create an endpoint group for the specified listener. An endpoint group is a collection of endpoints in one Amazon Web Services Region. A resource must be valid and active when you add it as an endpoint.

For more information about endpoint types and requirements for endpoints that you can add to Global Accelerator, see [Endpoints for standard accelerators](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints.html) in the *Global Accelerator Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/CreateEndpointGroup)

## Synopsis

```
create-endpoint-group
--listener-arn <value>
--endpoint-group-region <value>
[--endpoint-configurations <value>]
[--traffic-dial-percentage <value>]
[--health-check-port <value>]
[--health-check-protocol <value>]
[--health-check-path <value>]
[--health-check-interval-seconds <value>]
[--threshold-count <value>]
[--idempotency-token <value>]
[--port-overrides <value>]
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

`--listener-arn` (string)

The Amazon Resource Name (ARN) of the listener.

`--endpoint-group-region` (string)

The Amazon Web Services Region where the endpoint group is located. A listener can have only one endpoint group in a specific Region.

`--endpoint-configurations` (list)

The list of endpoint objects.

(structure)

A complex type for endpoints. A resource must be valid and active when you add it as an endpoint.

EndpointId -> (string)

An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID. For Amazon EC2 instances, this is the EC2 instance ID. A resource must be valid and active when you add it as an endpoint.

For cross-account endpoints, this must be the ARN of the resource.

Weight -> (integer)

The weight associated with the endpoint. When you add weights to endpoints, you configure Global Accelerator to route traffic based on proportions that you specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20). The result is that 4/20 of your traffic, on average, is routed to the first endpoint, 5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last endpoint. For more information, see [Endpoint weights](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html) in the *Global Accelerator Developer Guide* .

ClientIPPreservationEnabled -> (boolean)

Indicates whether client IP address preservation is enabled for an endpoint. The value is true or false. The default value is true for Application Load Balancer endpoints.

If the value is set to true, the clientâs IP address is preserved in the `X-Forwarded-For` request header as traffic travels to applications on the endpoint fronted by the accelerator.

Client IP address preservation is supported, in specific Amazon Web Services Regions, for endpoints that are Application Load Balancers, Amazon EC2 instances, and Network Load Balancers with security groups. IMPORTANT: You cannot use client IP address preservation with Network Load Balancers with TLS listeners.

For more information, see [Preserve client IP addresses in Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/preserve-client-ip-address.html) in the *Global Accelerator Developer Guide* .

AttachmentArn -> (string)

The Amazon Resource Name (ARN) of the cross-account attachment that specifies the endpoints (resources) that can be added to accelerators and principals that have permission to add the endpoints.

Shorthand Syntax:

```
EndpointId=string,Weight=integer,ClientIPPreservationEnabled=boolean,AttachmentArn=string ...
```

JSON Syntax:

```
[
  {
    "EndpointId": "string",
    "Weight": integer,
    "ClientIPPreservationEnabled": true|false,
    "AttachmentArn": "string"
  }
  ...
]
```

`--traffic-dial-percentage` (float)

The percentage of traffic to send to an Amazon Web Services Region. Additional traffic is distributed to other endpoint groups for this listener.

Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing.

The default value is 100.

`--health-check-port` (integer)

The port that Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default port is the listener port that this endpoint group is associated with. If listener port is a list of ports, Global Accelerator uses the first port in the list.

`--health-check-protocol` (string)

The protocol that Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default value is TCP.

Possible values:

- `TCP`
- `HTTP`
- `HTTPS`

`--health-check-path` (string)

If the protocol is HTTP/S, then this specifies the path that is the destination for health check targets. The default value is slash (/).

`--health-check-interval-seconds` (integer)

The timeâ10 seconds or 30 secondsâbetween each health check for an endpoint. The default value is 30.

`--threshold-count` (integer)

The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.

`--idempotency-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotencyâthat is, the uniquenessâof the request.

`--port-overrides` (list)

Override specific listener ports used to route traffic to endpoints that are part of this endpoint group. For example, you can create a port override in which the listener receives user traffic on ports 80 and 443, but your accelerator routes that traffic to ports 1080 and 1443, respectively, on the endpoints.

For more information, see [Overriding listener ports](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups-port-override.html) in the *Global Accelerator Developer Guide* .

(structure)

Override specific listener ports used to route traffic to endpoints that are part of an endpoint group. For example, you can create a port override in which the listener receives user traffic on ports 80 and 443, but your accelerator routes that traffic to ports 1080 and 1443, respectively, on the endpoints.

For more information, see [Overriding listener ports](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups-port-override.html) in the *Global Accelerator Developer Guide* .

ListenerPort -> (integer)

The listener port that you want to map to a specific endpoint port. This is the port that user traffic arrives to the Global Accelerator on.

EndpointPort -> (integer)

The endpoint port that you want a listener port to be mapped to. This is the port on the endpoint, such as the Application Load Balancer or Amazon EC2 instance.

Shorthand Syntax:

```
ListenerPort=integer,EndpointPort=integer ...
```

JSON Syntax:

```
[
  {
    "ListenerPort": integer,
    "EndpointPort": integer
  }
  ...
]
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

**To create an endpoint group**

The following `create-endpoint-group` example creates an endpoint group with one endpoint.

```
aws globalaccelerator create-endpoint-group \
    --listener-arn arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz \
    --endpoint-group-region us-east-1 \
    --endpoint-configurations EndpointId=i-1234567890abcdef0,Weight=128
```

Output:

```
{
    "EndpointGroup": {
        "TrafficDialPercentage": 100.0,
        "EndpointDescriptions": [
            {
                "Weight": 128,
                "EndpointId": "i-1234567890abcdef0"
            }
        ],
        "EndpointGroupArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz/endpoint-group/098765zyxwvu",
        "EndpointGroupRegion": "us-east-1"
    }
}
```

For more information, see [Endpoint groups in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups.html) in the *AWS Global Accelerator Developer Guide*.

## Output

EndpointGroup -> (structure)

The information about the endpoint group that was created.

EndpointGroupArn -> (string)

The Amazon Resource Name (ARN) of the endpoint group.

EndpointGroupRegion -> (string)

The Amazon Web Services Region where the endpoint group is located.

EndpointDescriptions -> (list)

The list of endpoint objects.

(structure)

A complex type for an endpoint. Each endpoint group can include one or more endpoints, such as load balancers.

EndpointId -> (string)

An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID. For Amazon EC2 instances, this is the EC2 instance ID.

An Application Load Balancer can be either internal or internet-facing.

Weight -> (integer)

The weight associated with the endpoint. When you add weights to endpoints, you configure Global Accelerator to route traffic based on proportions that you specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20). The result is that 4/20 of your traffic, on average, is routed to the first endpoint, 5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last endpoint. For more information, see [Endpoint weights](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html) in the *Global Accelerator Developer Guide* .

HealthState -> (string)

The health status of the endpoint.

HealthReason -> (string)

Returns a null result.

ClientIPPreservationEnabled -> (boolean)

Indicates whether client IP address preservation is enabled for an endpoint. The value is true or false. The default value is true for Application Load Balancers endpoints.

If the value is set to true, the clientâs IP address is preserved in the `X-Forwarded-For` request header as traffic travels to applications on the endpoint fronted by the accelerator.

Client IP address preservation is supported, in specific Amazon Web Services Regions, for endpoints that are Application Load Balancers, Amazon EC2 instances, and Network Load Balancers with security groups. IMPORTANT: You cannot use client IP address preservation with Network Load Balancers with TLS listeners.

For more information, see [Preserve client IP addresses in Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/preserve-client-ip-address.html) in the *Global Accelerator Developer Guide* .

TrafficDialPercentage -> (float)

The percentage of traffic to send to an Amazon Web Services Region. Additional traffic is distributed to other endpoint groups for this listener.

Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing.

The default value is 100.

HealthCheckPort -> (integer)

The port that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group.

The default port is the port for the listener that this endpoint group is associated with. If the listener port is a list, Global Accelerator uses the first specified port in the list of ports.

HealthCheckProtocol -> (string)

The protocol that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group. The default value is TCP.

HealthCheckPath -> (string)

If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator uses for the destination on the endpoints for health checks. The default is slash (/).

HealthCheckIntervalSeconds -> (integer)

The timeâ10 seconds or 30 secondsâbetween health checks for each endpoint. The default value is 30.

ThresholdCount -> (integer)

The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.

PortOverrides -> (list)

Allows you to override the destination ports used to route traffic to an endpoint. Using a port override lets you map a list of external destination ports (that your users send traffic to) to a list of internal destination ports that you want an application endpoint to receive traffic on.

(structure)

Override specific listener ports used to route traffic to endpoints that are part of an endpoint group. For example, you can create a port override in which the listener receives user traffic on ports 80 and 443, but your accelerator routes that traffic to ports 1080 and 1443, respectively, on the endpoints.

For more information, see [Overriding listener ports](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups-port-override.html) in the *Global Accelerator Developer Guide* .

ListenerPort -> (integer)

The listener port that you want to map to a specific endpoint port. This is the port that user traffic arrives to the Global Accelerator on.

EndpointPort -> (integer)

The endpoint port that you want a listener port to be mapped to. This is the port on the endpoint, such as the Application Load Balancer or Amazon EC2 instance.