# list-instancesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/list-instances.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/list-instances.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicediscovery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/index.html#cli-aws-servicediscovery) ]

# list-instances

## Description

Lists summary information about the instances that you registered by using a specified service.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/ListInstances)

`list-instances` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Instances`

## Synopsis

```
list-instances
--service-id <value>
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
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

`--service-id` (string)

The ID of the service that you want to list instances for.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

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

**To list service instances**

The following `list-instances` example lists service instances.

```
aws servicediscovery list-instances \
    --service-id srv-qzpwvt2tfqcegapy
```

Output:

```
{
    "Instances": [
        {
            "Id": "i-06bdabbae60f65a4e",
            "Attributes": {
                "AWS_INSTANCE_IPV4": "172.2.1.3",
                "AWS_INSTANCE_PORT": "808"
            }
        }
    ]
}
```

For more information, see [Viewing a list of service instances](https://docs.aws.amazon.com/cloud-map/latest/dg/listing-instances.html) in the *AWS Cloud Map Developer Guide*.

## Output

Instances -> (list)

Summary information about the instances that are associated with the specified service.

(structure)

A complex type that contains information about the instances that you registered by using a specified service.

Id -> (string)

The ID for an instance that you created by using a specified service.

Attributes -> (map)

A string map that contains the following information:

- The attributes that are associated with the instance.
- For each attribute, the applicable value.

Supported attribute keys include the following:

AWS_ALIAS_DNS_NAME

For an alias record that routes traffic to an Elastic Load Balancing load balancer, the DNS name thatâs associated with the load balancer.

AWS_EC2_INSTANCE_ID (HTTP namespaces only)

The Amazon EC2 instance ID for the instance. When the `AWS_EC2_INSTANCE_ID` attribute is specified, then the `AWS_INSTANCE_IPV4` attribute contains the primary private IPv4 address.

AWS_INIT_HEALTH_STATUS

If the service configuration includes `HealthCheckCustomConfig` , you can optionally use `AWS_INIT_HEALTH_STATUS` to specify the initial status of the custom health check, `HEALTHY` or `UNHEALTHY` . If you donât specify a value for `AWS_INIT_HEALTH_STATUS` , the initial status is `HEALTHY` .

AWS_INSTANCE_CNAME

For a `CNAME` record, the domain name that Route 53 returns in response to DNS queries (for example, `example.com` ).

AWS_INSTANCE_IPV4

For an `A` record, the IPv4 address that Route 53 returns in response to DNS queries (for example, `192.0.2.44` ).

AWS_INSTANCE_IPV6

For an `AAAA` record, the IPv6 address that Route 53 returns in response to DNS queries (for example, `2001:0db8:85a3:0000:0000:abcd:0001:2345` ).

AWS_INSTANCE_PORT

For an `SRV` record, the value that Route 53 returns for the port. In addition, if the service includes `HealthCheckConfig` , the port on the endpoint that Route 53 sends requests to.

key -> (string)

value -> (string)

NextToken -> (string)

If more than `MaxResults` instances match the specified criteria, you can submit another `ListInstances` request to get the next group of results. Specify the value of `NextToken` from the previous response in the next request.