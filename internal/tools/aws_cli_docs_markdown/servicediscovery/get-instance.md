# get-instanceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-instance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-instance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicediscovery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/index.html#cli-aws-servicediscovery) ]

# get-instance

## Description

Gets information about a specified instance.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/GetInstance)

## Synopsis

```
get-instance
--service-id <value>
--instance-id <value>
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

`--service-id` (string)

The ID of the service that the instance is associated with.

`--instance-id` (string)

The ID of the instance that you want to get information about.

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

**To get the details of an instance**

The following `get-instance` example gets the attributes of a service.

```
aws servicediscovery get-instance \
    --service-id srv-e4anhexample0004
    --instance-id i-abcd1234
```

Output:

```
{
    "Instances": {
        "Id": "arn:aws:servicediscovery:us-west-2:111122223333;:service/srv-e4anhexample0004",
        "Attributes": {
            "AWS_INSTANCE_IPV4": "192.0.2.44",
            "AWS_INSTANCE_PORT": "80",
            "color": "green",
            "region": "us-west-2",
            "stage": "beta"
        }
    }
}
```

For more information, see [AWS Cloud Map service instances](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-instances.html) in the *AWS Cloud Map Developer Guide*.

## Output

Instance -> (structure)

A complex type that contains information about a specified instance.

Id -> (string)

An identifier that you want to associate with the instance. Note the following:

- If the service thatâs specified by `ServiceId` includes settings for an `SRV` record, the value of `InstanceId` is automatically included as part of the value for the `SRV` record. For more information, see [DnsRecord > Type](https://docs.aws.amazon.com/cloud-map/latest/api/API_DnsRecord.html#cloudmap-Type-DnsRecord-Type) .
- You can use this value to update an existing instance.
- To register a new instance, you must specify a value thatâs unique among instances that you register by using the same service.
- If you specify an existing `InstanceId` and `ServiceId` , Cloud Map updates the existing DNS records. If thereâs also an existing health check, Cloud Map deletes the old health check and creates a new one.

### Note

The health check isnât deleted immediately, so it will still appear for a while if you submit a `ListHealthChecks` request, for example.

CreatorRequestId -> (string)

A unique string that identifies the request and that allows failed `RegisterInstance` requests to be retried without the risk of executing the operation twice. You must use a unique `CreatorRequestId` string every time you submit a `RegisterInstance` request if youâre registering additional instances for the same namespace and service. `CreatorRequestId` can be any unique string (for example, a date/time stamp).

Attributes -> (map)

A string map that contains the following information for the service that you specify in `ServiceId` :

- The attributes that apply to the records that are defined in the service.
- For each attribute, the applicable value.

### Note

Do not include sensitive information in the attributes if the namespace is discoverable by public DNS queries.

Supported attribute keys include the following:

AWS_ALIAS_DNS_NAME

If you want Cloud Map to create a Route 53 alias record that routes traffic to an Elastic Load Balancing load balancer, specify the DNS name thatâs associated with the load balancer. For information about how to get the DNS name, see [AliasTarget->DNSName](https://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html#Route53-Type-AliasTarget-DNSName) in the *Route 53 API Reference* .

Note the following:

- The configuration for the service thatâs specified by `ServiceId` must include settings for an `A` record, an `AAAA` record, or both.
- In the service thatâs specified by `ServiceId` , the value of `RoutingPolicy` must be `WEIGHTED` .
- If the service thatâs specified by `ServiceId` includes `HealthCheckConfig` settings, Cloud Map creates the health check, but it wonât associate the health check with the alias record.
- Auto naming currently doesnât support creating alias records that route traffic to Amazon Web Services resources other than ELB load balancers.
- If you specify a value for `AWS_ALIAS_DNS_NAME` , donât specify values for any of the `AWS_INSTANCE` attributes.

AWS_EC2_INSTANCE_ID

*HTTP namespaces only.* The Amazon EC2 instance ID for the instance. The `AWS_INSTANCE_IPV4` attribute contains the primary private IPv4 address.

AWS_INIT_HEALTH_STATUS

If the service configuration includes `HealthCheckCustomConfig` , you can optionally use `AWS_INIT_HEALTH_STATUS` to specify the initial status of the custom health check, `HEALTHY` or `UNHEALTHY` . If you donât specify a value for `AWS_INIT_HEALTH_STATUS` , the initial status is `HEALTHY` .

AWS_INSTANCE_CNAME

If the service configuration includes a `CNAME` record, the domain name that you want Route 53 to return in response to DNS queries (for example, `example.com` ).

This value is required if the service specified by `ServiceId` includes settings for an `CNAME` record.

AWS_INSTANCE_IPV4

If the service configuration includes an `A` record, the IPv4 address that you want Route 53 to return in response to DNS queries (for example, `192.0.2.44` ).

This value is required if the service specified by `ServiceId` includes settings for an `A` record. If the service includes settings for an `SRV` record, you must specify a value for `AWS_INSTANCE_IPV4` , `AWS_INSTANCE_IPV6` , or both.

AWS_INSTANCE_IPV6

If the service configuration includes an `AAAA` record, the IPv6 address that you want Route 53 to return in response to DNS queries (for example, `2001:0db8:85a3:0000:0000:abcd:0001:2345` ).

This value is required if the service specified by `ServiceId` includes settings for an `AAAA` record. If the service includes settings for an `SRV` record, you must specify a value for `AWS_INSTANCE_IPV4` , `AWS_INSTANCE_IPV6` , or both.

AWS_INSTANCE_PORT

If the service includes an `SRV` record, the value that you want Route 53 to return for the port.

If the service includes `HealthCheckConfig` , the port on the endpoint that you want Route 53 to send requests to.

This value is required if you specified settings for an `SRV` record or a Route 53 health check when you created the service.

key -> (string)

value -> (string)