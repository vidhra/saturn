# discover-instancesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/discover-instances.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/discover-instances.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicediscovery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/index.html#cli-aws-servicediscovery) ]

# discover-instances

## Description

Discovers registered instances for a specified namespace and service. You can use `DiscoverInstances` to discover instances for any type of namespace. `DiscoverInstances` returns a randomized list of instances allowing customers to distribute traffic evenly across instances. For public and private DNS namespaces, you can also use DNS queries to discover instances.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/DiscoverInstances)

## Synopsis

```
discover-instances
--namespace-name <value>
--service-name <value>
[--max-results <value>]
[--query-parameters <value>]
[--optional-parameters <value>]
[--health-status <value>]
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

`--namespace-name` (string)

The `HttpName` name of the namespace. Itâs found in the `HttpProperties` member of the `Properties` member of the namespace. In most cases, `Name` and `HttpName` match. However, if you reuse `Name` for namespace creation, a generated hash is added to `HttpName` to distinguish the two.

`--service-name` (string)

The name of the service that you specified when you registered the instance.

`--max-results` (integer)

The maximum number of instances that you want Cloud Map to return in the response to a `DiscoverInstances` request. If you donât specify a value for `MaxResults` , Cloud Map returns up to 100 instances.

`--query-parameters` (map)

Filters to scope the results based on custom attributes for the instance (for example, `{version=v1, az=1a}` ). Only instances that match all the specified key-value pairs are returned.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--optional-parameters` (map)

Opportunistic filters to scope the results based on custom attributes. If there are instances that match both the filters specified in both the `QueryParameters` parameter and this parameter, all of these instances are returned. Otherwise, the filters are ignored, and only instances that match the filters that are specified in the `QueryParameters` parameter are returned.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--health-status` (string)

The health status of the instances that you want to discover. This parameter is ignored for services that donât have a health check configured, and all instances are returned.

HEALTHY

Returns healthy instances.

UNHEALTHY

Returns unhealthy instances.

ALL

Returns all instances.

HEALTHY_OR_ELSE_ALL

Returns healthy instances, unless none are reporting a healthy state. In that case, return all instances. This is also called failing open.

Possible values:

- `HEALTHY`
- `UNHEALTHY`
- `ALL`
- `HEALTHY_OR_ELSE_ALL`

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

**To discover registered instances**

The following `discover-instances` example discovers registered instances.

```
aws servicediscovery discover-instances \
    --namespace-name example.com \
    --service-name myservice \
    --max-results 10 \
    --health-status ALL
```

Output:

```
{
    "Instances": [
        {
            "InstanceId": "myservice-53",
            "NamespaceName": "example.com",
            "ServiceName": "myservice",
            "HealthStatus": "UNKNOWN",
            "Attributes": {
                "AWS_INSTANCE_IPV4": "172.2.1.3",
                "AWS_INSTANCE_PORT": "808"
            }
        }
    ]
}
```

For more information, see [AWS Cloud Map service instances](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-instances.html) in the *AWS Cloud Map Developer Guide*.

## Output

Instances -> (list)

A complex type that contains one `HttpInstanceSummary` for each registered instance.

(structure)

In a response to a [DiscoverInstances](https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html) request, `HttpInstanceSummary` contains information about one instance that matches the values that you specified in the request.

InstanceId -> (string)

The ID of an instance that matches the values that you specified in the request.

NamespaceName -> (string)

The `HttpName` name of the namespace. Itâs found in the `HttpProperties` member of the `Properties` member of the namespace.

ServiceName -> (string)

The name of the service that you specified when you registered the instance.

HealthStatus -> (string)

If you configured health checking in the service, the current health status of the service instance.

Attributes -> (map)

If you included any attributes when you registered the instance, the values of those attributes.

key -> (string)

value -> (string)

InstancesRevision -> (long)

The increasing revision associated to the response Instances list. If a new instance is registered or deregistered, the `InstancesRevision` updates. The health status updates donât update `InstancesRevision` .