# describe-load-balancersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-load-balancers.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-load-balancers.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/index.html#cli-aws-elb) ]

# describe-load-balancers

## Description

Describes the specified the load balancers. If no load balancers are specified, the call describes all of your load balancers.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/DescribeLoadBalancers)

`describe-load-balancers` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `LoadBalancerDescriptions`

## Synopsis

```
describe-load-balancers
[--load-balancer-names <value>]
[--page-size <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--max-items <value>]
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

`--load-balancer-names` (list)

The names of the load balancers.

(string)

Syntax:

```
"string" "string" ...
```

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To describe your load balancers**

This example describes all of your load balancers.

Command:

```
aws elb describe-load-balancers
```

**To describe one of your load balancers**

This example describes the specified load balancer.

Command:

```
aws elb describe-load-balancers --load-balancer-name my-load-balancer
```

The following example response is for an HTTPS load balancer in a VPC.

Output:

```
{
  "LoadBalancerDescriptions": [
    {
      "Subnets": [
          "subnet-15aaab61"
      ],
      "CanonicalHostedZoneNameID": "Z3DZXE0EXAMPLE",
      "CanonicalHostedZoneName": "my-load-balancer-1234567890.us-west-2.elb.amazonaws.com",
      "ListenerDescriptions": [
          {
              "Listener": {
                  "InstancePort": 80,
                  "LoadBalancerPort": 80,
                  "Protocol": "HTTP",
                  "InstanceProtocol": "HTTP"
              },
              "PolicyNames": []
          },
          {
              "Listener": {
                  "InstancePort": 443,
                  "SSLCertificateId": "arn:aws:iam::123456789012:server-certificate/my-server-cert",
                  "LoadBalancerPort": 443,
                  "Protocol": "HTTPS",
                  "InstanceProtocol": "HTTPS"
              },
              "PolicyNames": [
                  "ELBSecurityPolicy-2015-03"
              ]
          }
      ],
      "HealthCheck": {
          "HealthyThreshold": 2,
          "Interval": 30,
          "Target": "HTTP:80/png",
          "Timeout": 3,
          "UnhealthyThreshold": 2
      },
      "VPCId": "vpc-a01106c2",
      "BackendServerDescriptions": [
          {
              "InstancePort": 80,
              "PolicyNames": [
                  "my-ProxyProtocol-policy"
              ]
          }
      ],
      "Instances": [
          {
              "InstanceId": "i-207d9717"
          },
          {
              "InstanceId": "i-afefb49b"
          }
      ],
      "DNSName": "my-load-balancer-1234567890.us-west-2.elb.amazonaws.com",
      "SecurityGroups": [
          "sg-a61988c3"
      ],
      "Policies": {
          "LBCookieStickinessPolicies": [
              {
                  "PolicyName": "my-duration-cookie-policy",
                  "CookieExpirationPeriod": 60
              }
          ],
          "AppCookieStickinessPolicies": [],
          "OtherPolicies": [
              "my-PublicKey-policy",
              "my-authentication-policy",
              "my-SSLNegotiation-policy",
              "my-ProxyProtocol-policy",
              "ELBSecurityPolicy-2015-03"
          ]
      },
      "LoadBalancerName": "my-load-balancer",
      "CreatedTime": "2015-03-19T03:24:02.650Z",
      "AvailabilityZones": [
          "us-west-2a"
      ],
      "Scheme": "internet-facing",
      "SourceSecurityGroup": {
          "OwnerAlias": "123456789012",
          "GroupName": "my-elb-sg"
      }
    }
  ]
}
```

## Output

LoadBalancerDescriptions -> (list)

Information about the load balancers.

(structure)

Information about a load balancer.

LoadBalancerName -> (string)

The name of the load balancer.

DNSName -> (string)

The DNS name of the load balancer.

CanonicalHostedZoneName -> (string)

The DNS name of the load balancer.

For more information, see [Configure a Custom Domain Name](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/using-domain-names-with-elb.html) in the *Classic Load Balancers Guide* .

CanonicalHostedZoneNameID -> (string)

The ID of the Amazon Route 53 hosted zone for the load balancer.

ListenerDescriptions -> (list)

The listeners for the load balancer.

(structure)

The policies enabled for a listener.

Listener -> (structure)

The listener.

Protocol -> (string)

The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.

LoadBalancerPort -> (integer)

The port on which the load balancer is listening. On EC2-VPC, you can specify any port from the range 1-65535. On EC2-Classic, you can specify any port from the following list: 25, 80, 443, 465, 587, 1024-65535.

InstanceProtocol -> (string)

The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.

If the front-end protocol is TCP or SSL, the back-end protocol must be TCP or SSL. If the front-end protocol is HTTP or HTTPS, the back-end protocol must be HTTP or HTTPS.

If there is another listener with the same `InstancePort` whose `InstanceProtocol` is secure, (HTTPS or SSL), the listenerâs `InstanceProtocol` must also be secure.

If there is another listener with the same `InstancePort` whose `InstanceProtocol` is HTTP or TCP, the listenerâs `InstanceProtocol` must be HTTP or TCP.

InstancePort -> (integer)

The port on which the instance is listening.

SSLCertificateId -> (string)

The Amazon Resource Name (ARN) of the server certificate.

PolicyNames -> (list)

The policies. If there are no policies enabled, the list is empty.

(string)

Policies -> (structure)

The policies defined for the load balancer.

AppCookieStickinessPolicies -> (list)

The stickiness policies created using  CreateAppCookieStickinessPolicy .

(structure)

Information about a policy for application-controlled session stickiness.

PolicyName -> (string)

The mnemonic name for the policy being created. The name must be unique within a set of policies for this load balancer.

CookieName -> (string)

The name of the application cookie used for stickiness.

LBCookieStickinessPolicies -> (list)

The stickiness policies created using  CreateLBCookieStickinessPolicy .

(structure)

Information about a policy for duration-based session stickiness.

PolicyName -> (string)

The name of the policy. This name must be unique within the set of policies for this load balancer.

CookieExpirationPeriod -> (long)

The time period, in seconds, after which the cookie should be considered stale. If this parameter is not specified, the stickiness session lasts for the duration of the browser session.

OtherPolicies -> (list)

The policies other than the stickiness policies.

(string)

BackendServerDescriptions -> (list)

Information about your EC2 instances.

(structure)

Information about the configuration of an EC2 instance.

InstancePort -> (integer)

The port on which the EC2 instance is listening.

PolicyNames -> (list)

The names of the policies enabled for the EC2 instance.

(string)

AvailabilityZones -> (list)

The Availability Zones for the load balancer.

(string)

Subnets -> (list)

The IDs of the subnets for the load balancer.

(string)

VPCId -> (string)

The ID of the VPC for the load balancer.

Instances -> (list)

The IDs of the instances for the load balancer.

(structure)

The ID of an EC2 instance.

InstanceId -> (string)

The instance ID.

HealthCheck -> (structure)

Information about the health checks conducted on the load balancer.

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

SourceSecurityGroup -> (structure)

The security group for the load balancer, which you can use as part of your inbound rules for your registered instances. To only allow traffic from load balancers, add a security group rule that specifies this source security group as the inbound source.

OwnerAlias -> (string)

The owner of the security group.

GroupName -> (string)

The name of the security group.

SecurityGroups -> (list)

The security groups for the load balancer. Valid only for load balancers in a VPC.

(string)

CreatedTime -> (timestamp)

The date and time the load balancer was created.

Scheme -> (string)

The type of load balancer. Valid only for load balancers in a VPC.

If `Scheme` is `internet-facing` , the load balancer has a public DNS name that resolves to a public IP address.

If `Scheme` is `internal` , the load balancer has a public DNS name that resolves to a private IP address.

NextMarker -> (string)

The marker to use when requesting the next set of results. If there are no additional results, the string is empty.