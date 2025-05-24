# create-private-dns-namespaceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/create-private-dns-namespace.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/create-private-dns-namespace.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicediscovery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/index.html#cli-aws-servicediscovery) ]

# create-private-dns-namespace

## Description

Creates a private namespace based on DNS, which is visible only inside a specified Amazon VPC. The namespace defines your service naming scheme. For example, if you name your namespace `example.com` and name your service `backend` , the resulting DNS name for the service is `backend.example.com` . Service instances that are registered using a private DNS namespace can be discovered using either a `DiscoverInstances` request or using DNS. For the current quota on the number of namespaces that you can create using the same Amazon Web Services account, see [Cloud Map quotas](https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html) in the *Cloud Map Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/CreatePrivateDnsNamespace)

## Synopsis

```
create-private-dns-namespace
--name <value>
[--creator-request-id <value>]
[--description <value>]
--vpc <value>
[--tags <value>]
[--properties <value>]
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

`--name` (string)

The name that you want to assign to this namespace. When you create a private DNS namespace, Cloud Map automatically creates an Amazon Route 53 private hosted zone that has the same name as the namespace.

`--creator-request-id` (string)

A unique string that identifies the request and that allows failed `CreatePrivateDnsNamespace` requests to be retried without the risk of running the operation twice. `CreatorRequestId` can be any unique string (for example, a date/timestamp).

`--description` (string)

A description for the namespace.

`--vpc` (string)

The ID of the Amazon VPC that you want to associate the namespace with.

`--tags` (list)

The tags to add to the namespace. Each tag consists of a key and an optional value that you define. Tags keys can be up to 128 characters in length, and tag values can be up to 256 characters in length.

(structure)

A custom key-value pair thatâs associated with a resource.

Key -> (string)

The key identifier, or name, of the tag.

Value -> (string)

The string value thatâs associated with the key of the tag. You can set the value of a tag to an empty string, but you canât set the value of a tag to null.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--properties` (structure)

Properties for the private DNS namespace.

DnsProperties -> (structure)

DNS properties for the private DNS namespace.

SOA -> (structure)

Fields for the Start of Authority (SOA) record for the hosted zone for the private DNS namespace.

TTL -> (long)

The time to live (TTL) for purposes of negative caching.

Shorthand Syntax:

```
DnsProperties={SOA={TTL=long}}
```

JSON Syntax:

```
{
  "DnsProperties": {
    "SOA": {
      "TTL": long
    }
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

**To create a private DNS namespace**

The following `create-private-dns-namespace` example creates a private DNS namespace.

```
aws servicediscovery create-private-dns-namespace \
    --name example.com \
    --vpc vpc-1c56417b
```

Output:

```
{
    "OperationId": "gv4g5meo7ndmeh4fqskygvk23d2fijwa-k9302yzd"
}
```

To confirm that the operation succeeded, you can run `get-operation`. For more information, see [get-operation](https://docs.aws.amazon.com/cli/latest/reference/servicediscovery/get-operation.html) .

For more information, see [Creating namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/creating-namespaces.html) in the *AWS Cloud Map Developer Guide*.

## Output

OperationId -> (string)

A value that you can use to determine whether the request completed successfully. To get the status of the operation, see [GetOperation](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetOperation.html) .