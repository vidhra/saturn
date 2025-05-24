# list-namespacesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/list-namespaces.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/list-namespaces.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicediscovery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/index.html#cli-aws-servicediscovery) ]

# list-namespaces

## Description

Lists summary information about the namespaces that were created by the current Amazon Web Services account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/ListNamespaces)

`list-namespaces` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Namespaces`

## Synopsis

```
list-namespaces
[--filters <value>]
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

`--filters` (list)

A complex type that contains specifications for the namespaces that you want to list.

If you specify more than one filter, a namespace must match all filters to be returned by `ListNamespaces` .

(structure)

A complex type that identifies the namespaces that you want to list. You can choose to list public or private namespaces.

Name -> (string)

Specify the namespaces that you want to get using one of the following.

- `TYPE` : Gets the namespaces of the specified type.
- `NAME` : Gets the namespaces with the specified name.
- `HTTP_NAME` : Gets the namespaces with the specified HTTP name.

Values -> (list)

Specify the values that are applicable to the value that you specify for `Name` .

- `TYPE` : Specify `HTTP` , `DNS_PUBLIC` , or `DNS_PRIVATE` .
- `NAME` : Specify the name of the namespace, which is found in `Namespace.Name` .
- `HTTP_NAME` : Specify the HTTP name of the namespace, which is found in `Namespace.Properties.HttpProperties.HttpName` .

(string)

Condition -> (string)

Specify the operator that you want to use to determine whether a namespace matches the specified value. Valid values for `Condition` are one of the following.

- `EQ` : When you specify `EQ` for `Condition` , you can specify only one value. `EQ` is supported for `TYPE` , `NAME` , and `HTTP_NAME` . `EQ` is the default condition and can be omitted.
- `BEGINS_WITH` : When you specify `BEGINS_WITH` for `Condition` , you can specify only one value. `BEGINS_WITH` is supported for `TYPE` , `NAME` , and `HTTP_NAME` .

Shorthand Syntax:

```
Name=string,Values=string,string,Condition=string ...
```

JSON Syntax:

```
[
  {
    "Name": "TYPE"|"NAME"|"HTTP_NAME",
    "Values": ["string", ...],
    "Condition": "EQ"|"IN"|"BETWEEN"|"BEGINS_WITH"
  }
  ...
]
```

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

**To list namespaces**

The following `list-namespaces` example lists namespaces.

```
aws servicediscovery list-namespaces
```

Output:

```
{
    "Namespaces": [
        {
            "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-a3ccy2e7e3a7rile",
            "CreateDate": 1585354387.357,
            "Id": "ns-a3ccy2e7e3a7rile",
            "Name": "local",
            "Properties": {
                "DnsProperties": {
                    "HostedZoneId": "Z06752353VBUDTC32S84S"
                },
                "HttpProperties": {
                    "HttpName": "local"
                 }
            },
            "Type": "DNS_PRIVATE"
        },
        {
            "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-pocfyjtrsmwtvcxx",
            "CreateDate": 1586468974.698,
            "Description": "My second namespace",
            "Id": "ns-pocfyjtrsmwtvcxx",
            "Name": "My-second-namespace",
            "Properties": {
                "DnsProperties": {},
                "HttpProperties": {
                    "HttpName": "My-second-namespace"
                }
            },
            "Type": "HTTP"
        },
        {
            "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-ylexjili4cdxy3xm",
            "CreateDate": 1587055896.798,
            "Id": "ns-ylexjili4cdxy3xm",
            "Name": "example.com",
            "Properties": {
                "DnsProperties": {
                    "HostedZoneId": "Z09983722P0QME1B3KC8I"
                },
                 "HttpProperties": {
                     "HttpName": "example.com"
                }
            },
            "Type": "DNS_PRIVATE"
        }
    ]
}
```

For more information, see [Viewing a list of namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/listing-namespaces.html) in the *AWS Cloud Map Developer Guide*.

## Output

Namespaces -> (list)

An array that contains one `NamespaceSummary` object for each namespace that matches the specified filter criteria.

(structure)

A complex type that contains information about a namespace.

Id -> (string)

The ID of the namespace.

Arn -> (string)

The Amazon Resource Name (ARN) that Cloud Map assigns to the namespace when you create it.

Name -> (string)

The name of the namespace. When you create a namespace, Cloud Map automatically creates a Route 53 hosted zone that has the same name as the namespace.

Type -> (string)

The type of the namespace, either public or private.

Description -> (string)

A description for the namespace.

ServiceCount -> (integer)

The number of services that were created using the namespace.

Properties -> (structure)

The properties of the namespace.

DnsProperties -> (structure)

A complex type that contains the ID for the Route 53 hosted zone that Cloud Map creates when you create a namespace.

HostedZoneId -> (string)

The ID for the Route 53 hosted zone that Cloud Map creates when you create a namespace.

SOA -> (structure)

Start of Authority (SOA) record for the hosted zone.

TTL -> (long)

The time to live (TTL) for purposes of negative caching.

HttpProperties -> (structure)

A complex type that contains the name of an HTTP namespace.

HttpName -> (string)

The name of an HTTP namespace.

CreateDate -> (timestamp)

The date and time that the namespace was created.

NextToken -> (string)

If the response contains `NextToken` , submit another `ListNamespaces` request to get the next group of results. Specify the value of `NextToken` from the previous response in the next request.

### Note

Cloud Map gets `MaxResults` namespaces and then filters them based on the specified criteria. Itâs possible that no namespaces in the first `MaxResults` namespaces matched the specified criteria but that subsequent groups of `MaxResults` namespaces do contain namespaces that match the criteria.