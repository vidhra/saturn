# list-health-checksÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-health-checks.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-health-checks.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html#cli-aws-route53) ]

# list-health-checks

## Description

Retrieve a list of the health checks that are associated with the current Amazon Web Services account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListHealthChecks)

`list-health-checks` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `HealthChecks`

## Synopsis

```
list-health-checks
[--max-items <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
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

`--max-items` (string)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (string)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

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

**To list the health checks associated with the current AWS account**

The following `list-health-checks` command lists detailed information about the first 100 health checks that are associated with the current AWS account.:

```
aws route53 list-health-checks
```

If you have more than 100 health checks, or if you want to list them in groups smaller than 100, include the `--maxitems` parameter. For example, to list health checks one at a time, use the following command:

```
aws route53 list-health-checks --max-items 1
```

To view the next health check, take the value of `NextToken` from the response to the previous command, and include it in the `--starting-token` parameter, for example:

```
aws route53 list-health-checks --max-items 1 --starting-token Z3M3LMPEXAMPLE
```

## Output

HealthChecks -> (list)

A complex type that contains one `HealthCheck` element for each health check that is associated with the current Amazon Web Services account.

(structure)

A complex type that contains information about one health check that is associated with the current Amazon Web Services account.

Id -> (string)

The identifier that Amazon Route 53 assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long.

CallerReference -> (string)

A unique string that you specified when you created the health check.

LinkedService -> (structure)

If the health check was created by another service, the service that created the health check. When a health check is created by another service, you canât edit or delete it using Amazon Route 53.

ServicePrincipal -> (string)

If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you canât edit or delete it using Amazon Route 53.

Description -> (string)

If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you canât edit or delete it using Amazon Route 53.

HealthCheckConfig -> (structure)

A complex type that contains detailed information about one health check.

IPAddress -> (string)

The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform health checks on. If you donât specify a value for `IPAddress` , Route 53 sends a DNS request to resolve the domain name that you specify in `FullyQualifiedDomainName` at the interval that you specify in `RequestInterval` . Using an IP address returned by DNS, Route 53 then checks the health of the endpoint.

Use one of the following formats for the value of `IPAddress` :

- **IPv4 address** : four values between 0 and 255, separated by periods (.), for example, `192.0.2.44` .
- **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:), for example, `2001:0db8:85a3:0000:0000:abcd:0001:2345` . You can also shorten IPv6 addresses as described in RFC 5952, for example, `2001:db8:85a3::abcd:1:2345` .

If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address, associate it with your EC2 instance, and specify the Elastic IP address for `IPAddress` . This ensures that the IP address of your instance will never change.

For more information, see [FullyQualifiedDomainName](https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName) .

Constraints: Route 53 canât check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you canât create health checks, see the following documents:

- [RFC 5735, Special Use IPv4 Addresses](https://tools.ietf.org/html/rfc5735)
- [RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space](https://tools.ietf.org/html/rfc6598)
- [RFC 5156, Special-Use IPv6 Addresses](https://tools.ietf.org/html/rfc5156)

When the value of `Type` is `CALCULATED` or `CLOUDWATCH_METRIC` , omit `IPAddress` .

Port -> (integer)

The port on the endpoint that you want Amazon Route 53 to perform health checks on.

### Note

Donât specify a value for `Port` when you specify a value for `Type` of `CLOUDWATCH_METRIC` or `CALCULATED` .

Type -> (string)

The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.

### Warning

You canât change the value of `Type` after you create a health check.

You can create the following types of health checks:

- **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400.
- **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.

### Warning

If you specify `HTTPS` for the value of `Type` , the endpoint must support TLS v1.0, v1.1, or v1.2.

- **HTTP_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and searches the first 5,120 bytes of the response body for the string that you specify in `SearchString` .
- **HTTPS_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an `HTTPS` request and searches the first 5,120 bytes of the response body for the string that you specify in `SearchString` .
- **TCP** : Route 53 tries to establish a TCP connection.
- **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If the state of the alarm is `OK` , the health check is considered healthy. If the state is `ALARM` , the health check is considered unhealthy. If CloudWatch doesnât have sufficient data to determine whether the state is `OK` or `ALARM` , the health check status depends on the setting for `InsufficientDataHealthStatus` : `Healthy` , `Unhealthy` , or `LastKnownStatus` .
- **CALCULATED** : For health checks that monitor the status of other health checks, Route 53 adds up the number of health checks that Route 53 health checkers consider to be healthy and compares that number with the value of `HealthThreshold` .
- **RECOVERY_CONTROL** : The health check is associated with a Route53 Application Recovery Controller routing control. If the routing control state is `ON` , the health check is considered healthy. If the state is `OFF` , the health check is considered unhealthy.

For more information, see [How Route 53 Determines Whether an Endpoint Is Healthy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html) in the *Amazon Route 53 Developer Guide* .

ResourcePath -> (string)

The path, if any, that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example, the file /docs/route53-health-check.html. You can also include query string parameters, for example, `/welcome.html?language=jp&login=y` .

FullyQualifiedDomainName -> (string)

Amazon Route 53 behavior depends on whether you specify a value for `IPAddress` .

**If you specify a value for** `IPAddress` :

Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and passes the value of `FullyQualifiedDomainName` in the `Host` header for all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Route 53 to perform health checks.

When Route 53 checks the health of an endpoint, here is how it constructs the `Host` header:

- If you specify a value of `80` for `Port` and `HTTP` or `HTTP_STR_MATCH` for `Type` , Route 53 passes the value of `FullyQualifiedDomainName` to the endpoint in the Host header.
- If you specify a value of `443` for `Port` and `HTTPS` or `HTTPS_STR_MATCH` for `Type` , Route 53 passes the value of `FullyQualifiedDomainName` to the endpoint in the `Host` header.
- If you specify another value for `Port` and any value except `TCP` for `Type` , Route 53 passes `FullyQualifiedDomainName:Port` to the endpoint in the `Host` header.

If you donât specify a value for `FullyQualifiedDomainName` , Route 53 substitutes the value of `IPAddress` in the `Host` header in each of the preceding cases.

**If you donât specify a value for** `IPAddress` :

Route 53 sends a DNS request to the domain that you specify for `FullyQualifiedDomainName` at the interval that you specify for `RequestInterval` . Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.

### Note

If you donât specify a value for `IPAddress` , Route 53 uses only IPv4 to send health checks to the endpoint. If thereâs no resource record set with a type of A for the name that you specify for `FullyQualifiedDomainName` , the health check fails with a âDNS resolution failedâ error.

If you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by `FullyQualifiedDomainName` , we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of `FullyQualifiedDomainName` , specify the domain name of the server (such as us-east-2-www.example.com), not the name of the resource record sets (www.example.com).

### Warning

In this configuration, if you create a health check for which the value of `FullyQualifiedDomainName` matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.

In addition, if the value that you specify for `Type` is `HTTP` , `HTTPS` , `HTTP_STR_MATCH` , or `HTTPS_STR_MATCH` , Route 53 passes the value of `FullyQualifiedDomainName` in the `Host` header, as it does when you specify a value for `IPAddress` . If the value of `Type` is `TCP` , Route 53 doesnât pass a `Host` header.

SearchString -> (string)

If the value of Type is `HTTP_STR_MATCH` or `HTTPS_STR_MATCH` , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Route 53 considers the resource healthy.

Route 53 considers case when searching for `SearchString` in the response body.

RequestInterval -> (integer)

The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health check request. Each Route 53 health checker makes requests at this interval.

### Warning

You canât change the value of `RequestInterval` after you create a health check.

If you donât specify a value for `RequestInterval` , the default value is `30` seconds.

FailureThreshold -> (integer)

The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see [How Amazon Route 53 Determines Whether an Endpoint Is Healthy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html) in the *Amazon Route 53 Developer Guide* .

If you donât specify a value for `FailureThreshold` , the default value is three health checks.

MeasureLatency -> (boolean)

Specify whether you want Amazon Route 53 to measure the latency between health checkers in multiple Amazon Web Services regions and your endpoint, and to display CloudWatch latency graphs on the **Health Checks** page in the Route 53 console.

### Warning

You canât change the value of `MeasureLatency` after you create a health check.

Inverted -> (boolean)

Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.

Disabled -> (boolean)

Stops Route 53 from performing health checks. When you disable a health check, hereâs what happens:

- **Health checks that check the health of endpoints:** Route 53 stops submitting requests to your application, server, or other resource.
- **Calculated health checks:** Route 53 stops aggregating the status of the referenced health checks.
- **Health checks that monitor CloudWatch alarms:** Route 53 stops monitoring the corresponding CloudWatch metrics.

After you disable a health check, Route 53 considers the status of the health check to always be healthy. If you configured DNS failover, Route 53 continues to route traffic to the corresponding resources. If you want to stop routing traffic to a resource, change the value of [Inverted](https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-Inverted) .

Charges for a health check still apply when the health check is disabled. For more information, see [Amazon Route 53 Pricing](http://aws.amazon.com/route53/pricing/) .

HealthThreshold -> (integer)

The number of child health checks that are associated with a `CALCULATED` health check that Amazon Route 53 must consider healthy for the `CALCULATED` health check to be considered healthy. To specify the child health checks that you want to associate with a `CALCULATED` health check, use the [ChildHealthChecks](https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-ChildHealthChecks) element.

Note the following:

- If you specify a number greater than the number of child health checks, Route 53 always considers this health check to be unhealthy.
- If you specify `0` , Route 53 always considers this health check to be healthy.

ChildHealthChecks -> (list)

(CALCULATED Health Checks Only) A complex type that contains one `ChildHealthCheck` element for each health check that you want to associate with a `CALCULATED` health check.

(string)

EnableSNI -> (boolean)

Specify whether you want Amazon Route 53 to send the value of `FullyQualifiedDomainName` to the endpoint in the `client_hello` message during TLS negotiation. This allows the endpoint to respond to `HTTPS` health check requests with the applicable SSL/TLS certificate.

Some endpoints require that `HTTPS` requests include the host name in the `client_hello` message. If you donât enable SNI, the status of the health check will be `SSL alert handshake_failure` . A health check can also have that status for other reasons. If SNI is enabled and youâre still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.

The SSL/TLS certificate on your endpoint includes a domain name in the `Common Name` field and possibly several more in the `Subject Alternative Names` field. One of the domain names in the certificate should match the value that you specify for `FullyQualifiedDomainName` . If the endpoint responds to the `client_hello` message with a certificate that does not include the domain name that you specified in `FullyQualifiedDomainName` , a health checker will retry the handshake. In the second attempt, the health checker will omit `FullyQualifiedDomainName` from the `client_hello` message.

Regions -> (list)

A complex type that contains one `Region` element for each region from which you want Amazon Route 53 health checkers to check the specified endpoint.

If you donât specify any regions, Route 53 health checkers automatically performs checks from all of the regions that are listed under **Valid Values** .

If you update a health check to remove a region that has been performing health checks, Route 53 will briefly continue to perform checks from that region to ensure that some health checkers are always checking the endpoint (for example, if you replace three regions with four different regions).

(string)

AlarmIdentifier -> (structure)

A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether the specified health check is healthy.

Region -> (string)

For the CloudWatch alarm that you want Route 53 health checkers to use to determine whether this health check is healthy, the region that the alarm was created in.

For the current list of CloudWatch regions, see [Amazon CloudWatch endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/cw_region.html) in the *Amazon Web Services General Reference* .

Name -> (string)

The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

### Note

Route 53 supports CloudWatch alarms with the following features:

- Standard-resolution metrics. High-resolution metrics arenât supported. For more information, see [High-Resolution Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics) in the *Amazon CloudWatch User Guide* .
- Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics arenât supported.

InsufficientDataHealthStatus -> (string)

When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:

- `Healthy` : Route 53 considers the health check to be healthy.
- `Unhealthy` : Route 53 considers the health check to be unhealthy.
- `LastKnownStatus` : Route 53 uses the status of the health check from the last time that CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy.

RoutingControlArn -> (string)

The Amazon Resource Name (ARN) for the Route 53 Application Recovery Controller routing control.

For more information about Route 53 Application Recovery Controller, see [Route 53 Application Recovery Controller Developer Guide.](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route-53-recovery.html) .

HealthCheckVersion -> (long)

The version of the health check. You can optionally pass this value in a call to `UpdateHealthCheck` to prevent overwriting another change to the health check.

CloudWatchAlarmConfiguration -> (structure)

A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is monitoring for this health check.

EvaluationPeriods -> (integer)

For the metric that the CloudWatch alarm is associated with, the number of periods that the metric is compared to the threshold.

Threshold -> (double)

For the metric that the CloudWatch alarm is associated with, the value the metric is compared with.

ComparisonOperator -> (string)

For the metric that the CloudWatch alarm is associated with, the arithmetic operation that is used for the comparison.

Period -> (integer)

For the metric that the CloudWatch alarm is associated with, the duration of one evaluation period in seconds.

MetricName -> (string)

The name of the CloudWatch metric that the alarm is associated with.

Namespace -> (string)

The namespace of the metric that the alarm is associated with. For more information, see [Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html) in the *Amazon CloudWatch User Guide* .

Statistic -> (string)

For the metric that the CloudWatch alarm is associated with, the statistic that is applied to the metric.

Dimensions -> (list)

For the metric that the CloudWatch alarm is associated with, a complex type that contains information about the dimensions for the metric. For information, see [Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html) in the *Amazon CloudWatch User Guide* .

(structure)

For the metric that the CloudWatch alarm is associated with, a complex type that contains information about one dimension.

Name -> (string)

For the metric that the CloudWatch alarm is associated with, the name of one dimension.

Value -> (string)

For the metric that the CloudWatch alarm is associated with, the value of one dimension.

Marker -> (string)

For the second and subsequent calls to `ListHealthChecks` , `Marker` is the value that you specified for the `marker` parameter in the previous request.

IsTruncated -> (boolean)

A flag that indicates whether there are more health checks to be listed. If the response was truncated, you can get the next group of health checks by submitting another `ListHealthChecks` request and specifying the value of `NextMarker` in the `marker` parameter.

NextMarker -> (string)

If `IsTruncated` is `true` , the value of `NextMarker` identifies the first health check that Amazon Route 53 returns if you submit another `ListHealthChecks` request and specify the value of `NextMarker` in the `marker` parameter.

MaxItems -> (string)

The value that you specified for the `maxitems` parameter in the call to `ListHealthChecks` that produced the current response.