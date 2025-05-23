# update-serviceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/update-service.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/update-service.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicediscovery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/index.html#cli-aws-servicediscovery) ]

# update-service

## Description

Submits a request to perform the following operations:

- Update the TTL setting for existing `DnsRecords` configurations
- Add, update, or delete `HealthCheckConfig` for a specified service

### Note

You canât add, update, or delete a `HealthCheckCustomConfig` configuration.

For public and private DNS namespaces, note the following:

- If you omit any existing `DnsRecords` or `HealthCheckConfig` configurations from an `UpdateService` request, the configurations are deleted from the service.
- If you omit an existing `HealthCheckCustomConfig` configuration from an `UpdateService` request, the configuration isnât deleted from the service.

When you update settings for a service, Cloud Map also updates the corresponding settings in all the records and health checks that were created by using the specified service.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/UpdateService)

## Synopsis

```
update-service
--id <value>
--service <value>
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

The ID of the service that you want to update.

`--service` (structure)

A complex type that contains the new settings for the service. You can specify a maximum of 30 attributes (key-value pairs).

Description -> (string)

A description for the service.

DnsConfig -> (structure)

Information about the Route 53 DNS records that you want Cloud Map to create when you register an instance.

DnsRecords -> (list)

An array that contains one `DnsRecord` object for each Route 53 record that you want Cloud Map to create when you register an instance.

(structure)

A complex type that contains information about the Route 53 DNS records that you want Cloud Map to create when you register an instance.

Type -> (string)

The type of the resource, which indicates the type of value that Route 53 returns in response to DNS queries. You can specify values for `Type` in the following combinations:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/update-service.html#id1)`A` **
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/update-service.html#id3)`AAAA` **
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/update-service.html#id5)`A` ** and ** `AAAA` **
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/update-service.html#id7)`SRV` **
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/update-service.html#id9)`CNAME` **

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

HealthCheckConfig -> (structure)

*Public DNS and HTTP namespaces only.* Settings for an optional health check. If you specify settings for a health check, Cloud Map associates the health check with the records that you specify in `DnsConfig` .

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

JSON Syntax:

```
{
  "Description": "string",
  "DnsConfig": {
    "DnsRecords": [
      {
        "Type": "SRV"|"A"|"AAAA"|"CNAME",
        "TTL": long
      }
      ...
    ]
  },
  "HealthCheckConfig": {
    "Type": "HTTP"|"HTTPS"|"TCP",
    "ResourcePath": "string",
    "FailureThreshold": integer
  }
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

**To update a service**

The following `update-service` example updates a service to update the `DnsConfig` and `HealthCheckConfig` settings.

```
aws servicediscovery update-service \
    --id srv-e4anhexample0004 \
    --service "DnsConfig={DnsRecords=[{"Type"="A","TTL"=60}]},HealthCheckConfig={"Type"="HTTP","ResourcePath"="/","FailureThreshold"="2"}"
```

Output:

```
{
    "OperationId": "gv4g5meo7ndmeh4fqskygvk23d2fijwa-k9302yzd"
}
```

To confirm that the operation succeeded, you can run `get-operation`.

For more information about updating a service, see [Updating an AWS Cloud Map service](https://docs.aws.amazon.com/cloud-map/latest/dg/editing-services.html) in the *AWS Cloud Map Developer Guide*.

## Output

OperationId -> (string)

A value that you can use to determine whether the request completed successfully. To get the status of the operation, see [GetOperation](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetOperation.html) .