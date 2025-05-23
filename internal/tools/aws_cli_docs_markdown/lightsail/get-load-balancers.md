# get-load-balancersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancers.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancers.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lightsail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html#cli-aws-lightsail) ]

# get-load-balancers

## Description

Returns information about all load balancers in an account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetLoadBalancers)

`get-load-balancers` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `loadBalancers`

## Synopsis

```
get-load-balancers
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

**To get information about all load balancers**

The following `get-load-balancers` example displays details about all of the load balancers in the configured AWS Region.

```
aws lightsail get-load-balancers
```

Output:

```
{
    "loadBalancers": [
        {
            "name": "LoadBalancer-1",
            "arn": "arn:aws:lightsail:us-west-2:111122223333:LoadBalancer/40486b2b-1ad0-4152-83e4-cEXAMPLE6f4b",
            "supportCode": "6EXAMPLE3362/arn:aws:elasticloadbalancing:us-west-2:333322221111:loadbalancer/app/bEXAMPLE128cb59d86f946a9395dd304/1EXAMPLE8dd9d77e",
            "createdAt": 1571677906.723,
            "location": {
                "availabilityZone": "all",
                "regionName": "us-west-2"
            },
            "resourceType": "LoadBalancer",
            "tags": [],
            "dnsName": "bEXAMPLE128cb59d86f946a9395dd304-1486911371.us-west-2.elb.amazonaws.com",
            "state": "active",
            "protocol": "HTTP",
            "publicPorts": [
                80
            ],
            "healthCheckPath": "/",
            "instancePort": 80,
            "instanceHealthSummary": [
                {
                    "instanceName": "MEAN-3",
                    "instanceHealth": "healthy"
                },
                {
                    "instanceName": "MEAN-1",
                    "instanceHealth": "healthy"
                },
                {
                    "instanceName": "MEAN-2",
                    "instanceHealth": "healthy"
                }
            ],
            "tlsCertificateSummaries": [
                {
                    "name": "example-com",
                    "isAttached": false
                }
            ],
            "configurationOptions": {
                "SessionStickinessEnabled": "false",
                "SessionStickiness_LB_CookieDurationSeconds": "86400"
            }
        }
    ]
}
```

## Output

loadBalancers -> (list)

An array of LoadBalancer objects describing your load balancers.

(structure)

Describes a load balancer.

name -> (string)

The name of the load balancer (`my-load-balancer` ).

arn -> (string)

The Amazon Resource Name (ARN) of the load balancer.

supportCode -> (string)

The support code. Include this code in your email to support when you have questions about your Lightsail load balancer. This code enables our support team to look up your Lightsail information more easily.

createdAt -> (timestamp)

The date when your load balancer was created.

location -> (structure)

The AWS Region where your load balancer was created (`us-east-2a` ). Lightsail automatically creates your load balancer across Availability Zones.

availabilityZone -> (string)

The Availability Zone. Follows the format `us-east-2a` (case-sensitive).

regionName -> (string)

The Amazon Web Services Region name.

resourceType -> (string)

The resource type (`LoadBalancer` .

tags -> (list)

The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

(structure)

Describes a tag key and optional value assigned to an Amazon Lightsail resource.

For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

key -> (string)

The key of the tag.

Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value -> (string)

The value of the tag.

Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

dnsName -> (string)

The DNS name of your Lightsail load balancer.

state -> (string)

The status of your load balancer. Valid values are below.

protocol -> (string)

The protocol you have enabled for your load balancer. Valid values are below.

You canât just have `HTTP_HTTPS` , but you can have just `HTTP` .

publicPorts -> (list)

An array of public port settings for your load balancer. For HTTP, use port 80. For HTTPS, use port 443.

(integer)

healthCheckPath -> (string)

The path you specified to perform your health checks. If no path is specified, the load balancer tries to make a request to the default (root) page.

instancePort -> (integer)

The port where the load balancer will direct traffic to your Lightsail instances. For HTTP traffic, itâs port 80. For HTTPS traffic, itâs port 443.

instanceHealthSummary -> (list)

An array of InstanceHealthSummary objects describing the health of the load balancer.

(structure)

Describes information about the health of the instance.

instanceName -> (string)

The name of the Lightsail instance for which you are requesting health check data.

instanceHealth -> (string)

Describes the overall instance health. Valid values are below.

instanceHealthReason -> (string)

More information about the instance health. If the `instanceHealth` is `healthy` , then an `instanceHealthReason` value is not provided.

If ** `instanceHealth` ** is `initial` , the ** `instanceHealthReason` ** value can be one of the following:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancers.html#id1)`Lb.RegistrationInProgress` ** - The target instance is in the process of being registered with the load balancer.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancers.html#id3)`Lb.InitialHealthChecking` ** - The Lightsail load balancer is still sending the target instance the minimum number of health checks required to determine its health status.

If ** `instanceHealth` ** is `unhealthy` , the ** `instanceHealthReason` ** value can be one of the following:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancers.html#id5)`Instance.ResponseCodeMismatch` ** - The health checks did not return an expected HTTP code.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancers.html#id7)`Instance.Timeout` ** - The health check requests timed out.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancers.html#id9)`Instance.FailedHealthChecks` ** - The health checks failed because the connection to the target instance timed out, the target instance response was malformed, or the target instance failed the health check for an unknown reason.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancers.html#id11)`Lb.InternalError` ** - The health checks failed due to an internal error.

If ** `instanceHealth` ** is `unused` , the ** `instanceHealthReason` ** value can be one of the following:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancers.html#id13)`Instance.NotRegistered` ** - The target instance is not registered with the target group.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancers.html#id15)`Instance.NotInUse` ** - The target group is not used by any load balancer, or the target instance is in an Availability Zone that is not enabled for its load balancer.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancers.html#id17)`Instance.IpUnusable` ** - The target IP address is reserved for use by a Lightsail load balancer.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancers.html#id19)`Instance.InvalidState` ** - The target is in the stopped or terminated state.

If ** `instanceHealth` ** is `draining` , the ** `instanceHealthReason` ** value can be one of the following:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancers.html#id21)`Instance.DeregistrationInProgress` ** - The target instance is in the process of being deregistered and the deregistration delay period has not expired.

tlsCertificateSummaries -> (list)

An array of LoadBalancerTlsCertificateSummary objects that provide additional information about the SSL/TLS certificates. For example, if `true` , the certificate is attached to the load balancer.

(structure)

Provides a summary of SSL/TLS certificate metadata.

name -> (string)

The name of the SSL/TLS certificate.

isAttached -> (boolean)

When `true` , the SSL/TLS certificate is attached to the Lightsail load balancer.

configurationOptions -> (map)

A string to string map of the configuration options for your load balancer. Valid values are listed below.

key -> (string)

value -> (string)

ipAddressType -> (string)

The IP address type of the load balancer.

The possible values are `ipv4` for IPv4 only, `ipv6` for IPv6 only, and `dualstack` for IPv4 and IPv6.

httpsRedirectionEnabled -> (boolean)

A Boolean value that indicates whether HTTPS redirection is enabled for the load balancer.

tlsPolicyName -> (string)

The name of the TLS security policy for the load balancer.

nextPageToken -> (string)

The token to advance to the next page of results from your request.

A next page token is not returned if there are no more results to display.

To get the next page of results, perform another `GetLoadBalancers` request and specify the next page token using the `pageToken` parameter.