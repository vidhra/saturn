# get-serviceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-service.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-service.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicediscovery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/index.html#cli-aws-servicediscovery) ]

# get-service

## Description

Gets the settings for a specified service.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/GetService)

## Synopsis

```
get-service
--id <value>
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

`--id` (string)

The ID of the service that you want to get settings for.

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

**To get the settings of a service**

The following `get-service` example gets the settings of a specified service.

```
aws servicediscovery get-service \
    --id srv-e4anhexample0004
```

Output:

```
{
    "Service": {
        "Id": "srv-e4anhexample0004",
        "Arn": "arn:aws:servicediscovery:us-west-2:111122223333:service/srv-e4anhexample0004",
        "Name": "test-service",
        "NamespaceId": "ns-e4anhexample0004",
        "DnsConfig": {},
        "Type": "HTTP",
        "CreateDate": "2025-02-24T10:59:02.905000-06:00",
        "CreatorRequestId": "3f50f9d9-b14c-482e-a556-d2a22fe6106d"
    }
}
```

For more information, see [AWS Cloud Map services](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-services.html) in the *AWS Cloud Map Developer Guide*.

## Output

Service -> (structure)

A complex type that contains information about the service.

Id -> (string)

The ID that Cloud Map assigned to the service when you created it.

Arn -> (string)

The Amazon Resource Name (ARN) that Cloud Map assigns to the service when you create it.

Name -> (string)

The name of the service.

NamespaceId -> (string)

The ID of the namespace that was used to create the service.

Description -> (string)

The description of the service.

InstanceCount -> (integer)

The number of instances that are currently associated with the service. Instances that were previously associated with the service but that are deleted arenât included in the count. The count might not reflect pending registrations and deregistrations.

DnsConfig -> (structure)

A complex type that contains information about the Route 53 DNS records that you want Cloud Map to create when you register an instance.

### Warning

The record types of a service can only be changed by deleting the service and recreating it with a new `Dnsconfig` .

NamespaceId -> (string)

*Use NamespaceId in `Service <https://docs.aws.amazon.com/cloud-map/latest/api/API_Service.html>`__ instead.*

The ID of the namespace to use for DNS configuration.

RoutingPolicy -> (string)

The routing policy that you want to apply to all Route 53 DNS records that Cloud Map creates when you register an instance and specify this service.

### Note

If you want to use this service to register instances that create alias records, specify `WEIGHTED` for the routing policy.

You can specify the following values:

MULTIVALUE

If you define a health check for the service and the health check is healthy, Route 53 returns the applicable value for up to eight instances.

For example, suppose that the service includes configurations for one `A` record and a health check. You use the service to register 10 instances. Route 53 responds to DNS queries with IP addresses for up to eight healthy instances. If fewer than eight instances are healthy, Route 53 responds to every DNS query with the IP addresses for all of the healthy instances.

If you donât define a health check for the service, Route 53 assumes that all instances are healthy and returns the values for up to eight instances.

For more information about the multivalue routing policy, see [Multivalue Answer Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue) in the *Route 53 Developer Guide* .

WEIGHTED

Route 53 returns the applicable value from one randomly selected instance from among the instances that you registered using the same service. Currently, all records have the same weight, so you canât route more or less traffic to any instances.

For example, suppose that the service includes configurations for one `A` record and a health check. You use the service to register 10 instances. Route 53 responds to DNS queries with the IP address for one randomly selected instance from among the healthy instances. If no instances are healthy, Route 53 responds to DNS queries as if all of the instances were healthy.

If you donât define a health check for the service, Route 53 assumes that all instances are healthy and returns the applicable value for one randomly selected instance.

For more information about the weighted routing policy, see [Weighted Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted) in the *Route 53 Developer Guide* .

DnsRecords -> (list)

An array that contains one `DnsRecord` object for each Route 53 DNS record that you want Cloud Map to create when you register an instance.

### Warning

The record type of a service specified in a `DnsRecord` object canât be updated. To change a record type, you need to delete the service and recreate it with a new `DnsConfig` .

(structure)

A complex type that contains information about the Route 53 DNS records that you want Cloud Map to create when you register an instance.

Type -> (string)

The type of the resource, which indicates the type of value that Route 53 returns in response to DNS queries. You can specify values for `Type` in the following combinations:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-service.html#id1)`A` **
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-service.html#id3)`AAAA` **
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-service.html#id5)`A` ** and ** `AAAA` **
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-service.html#id7)`SRV` **
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-service.html#id9)`CNAME` **

If you want Cloud Map to create a Route 53 alias record when you register an instance, specify `A` or `AAAA` for `Type` .

You specify other settings, such as the IP address for `A` and `AAAA` records, when you register an instance. For more information, see [RegisterInstance](https://docs.aws.amazon.com/cloud-map/latest/api/API_RegisterInstance.html) .

The following values are supported:

A

Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

AAAA

Route 53 returns the IP address of the resource in IPv6 format, such as 2001:0db8:85a3:0000:0000:abcd:0001:2345.

CNAME

Route 53 returns the domain name of the resource, such as www.example.com. Note the following:

- You specify the domain name that you want to route traffic to when you register an instance. For more information, see [Attributes](https://docs.aws.amazon.com/cloud-map/latest/api/API_RegisterInstance.html#cloudmap-RegisterInstance-request-Attributes) in the topic [RegisterInstance](https://docs.aws.amazon.com/cloud-map/latest/api/API_RegisterInstance.html) .
- You must specify `WEIGHTED` for the value of `RoutingPolicy` .
- You canât specify both `CNAME` for `Type` and settings for `HealthCheckConfig` . If you do, the request will fail with an `InvalidInput` error.

SRV

Route 53 returns the value for an `SRV` record. The value for an `SRV` record uses the following values:

`priority weight port service-hostname`

Note the following about the values:

- The values of `priority` and `weight` are both set to `1` and canât be changed.
- The value of `port` comes from the value that you specify for the `AWS_INSTANCE_PORT` attribute when you submit a [RegisterInstance](https://docs.aws.amazon.com/cloud-map/latest/api/API_RegisterInstance.html) request.
- The value of `service-hostname` is a concatenation of the following values:
- The value that you specify for `InstanceId` when you register an instance.
- The name of the service.
- The name of the namespace.

For example, if the value of `InstanceId` is `test` , the name of the service is `backend` , and the name of the namespace is `example.com` , the value of `service-hostname` is the following:

`test.backend.example.com`

If you specify settings for an `SRV` record, note the following:

- If you specify values for `AWS_INSTANCE_IPV4` , `AWS_INSTANCE_IPV6` , or both in the `RegisterInstance` request, Cloud Map automatically creates `A` and/or `AAAA` records that have the same name as the value of `service-hostname` in the `SRV` record. You can ignore these records.
- If youâre using a system that requires a specific `SRV` format, such as HAProxy, see the [Name](https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html#cloudmap-CreateService-request-Name) element in the documentation about `CreateService` for information about how to specify the correct name format.

TTL -> (long)

The amount of time, in seconds, that you want DNS resolvers to cache the settings for this record.

### Note

Alias records donât include a TTL because Route 53 uses the TTL for the Amazon Web Services resource that an alias record routes traffic to. If you include the `AWS_ALIAS_DNS_NAME` attribute when you submit a [RegisterInstance](https://docs.aws.amazon.com/cloud-map/latest/api/API_RegisterInstance.html) request, the `TTL` value is ignored. Always specify a TTL for the service; you can use a service to register instances that create either alias or non-alias records.

Type -> (string)

Describes the systems that can be used to discover the service instances.

DNS_HTTP

The service instances can be discovered using either DNS queries or the `DiscoverInstances` API operation.

HTTP

The service instances can only be discovered using the `DiscoverInstances` API operation.

DNS

Reserved.

HealthCheckConfig -> (structure)

*Public DNS and HTTP namespaces only.* A complex type that contains settings for an optional health check. If you specify settings for a health check, Cloud Map associates the health check with the records that you specify in `DnsConfig` .

For information about the charges for health checks, see [Amazon Route 53 Pricing](http://aws.amazon.com/route53/pricing/) .

Type -> (string)

The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy.

### Warning

You canât change the value of `Type` after you create a health check.

You can create the following types of health checks:

- **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400.
- **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.

### Warning

If you specify HTTPS for the value of `Type` , the endpoint must support TLS v1.0 or later.

- **TCP** : Route 53 tries to establish a TCP connection. If you specify `TCP` for `Type` , donât specify a value for `ResourcePath` .

For more information, see [How Route 53 Determines Whether an Endpoint Is Healthy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html) in the *Route 53 Developer Guide* .

ResourcePath -> (string)

The path that you want Route 53 to request when performing health checks. The path can be any value that your endpoint returns an HTTP status code of a 2xx or 3xx format for when the endpoint is healthy. An example file is `/docs/route53-health-check.html` . Route 53 automatically adds the DNS name for the service. If you donât specify a value for `ResourcePath` , the default value is `/` .

If you specify `TCP` for `Type` , you must *not* specify a value for `ResourcePath` .

FailureThreshold -> (integer)

The number of consecutive health checks that an endpoint must pass or fail for Route 53 to change the current status of the endpoint from unhealthy to healthy or the other way around. For more information, see [How Route 53 Determines Whether an Endpoint Is Healthy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html) in the *Route 53 Developer Guide* .

HealthCheckCustomConfig -> (structure)

A complex type that contains information about an optional custom health check.

### Warning

If you specify a health check configuration, you can specify either `HealthCheckCustomConfig` or `HealthCheckConfig` but not both.

FailureThreshold -> (integer)

### Warning

This parameter is no longer supported and is always set to 1. Cloud Map waits for approximately 30 seconds after receiving an `UpdateInstanceCustomHealthStatus` request before changing the status of the service instance.

The number of 30-second intervals that you want Cloud Map to wait after receiving an `UpdateInstanceCustomHealthStatus` request before it changes the health status of a service instance.

Sending a second or subsequent `UpdateInstanceCustomHealthStatus` request with the same value before 30 seconds has passed doesnât accelerate the change. Cloud Map still waits `30` seconds after the first request to make the change.

CreateDate -> (timestamp)

The date and time that the service was created, in Unix format and Coordinated Universal Time (UTC). The value of `CreateDate` is accurate to milliseconds. For example, the value `1516925490.087` represents Friday, January 26, 2018 12:11:30.087 AM.

CreatorRequestId -> (string)

A unique string that identifies the request and that allows failed requests to be retried without the risk of running the operation twice. `CreatorRequestId` can be any unique string (for example, a date/timestamp).