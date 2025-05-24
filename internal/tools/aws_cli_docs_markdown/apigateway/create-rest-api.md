# create-rest-apiÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-rest-api.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-rest-api.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [apigateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/index.html#cli-aws-apigateway) ]

# create-rest-api

## Description

Creates a new RestApi resource.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/CreateRestApi)

## Synopsis

```
create-rest-api
--name <value>
[--description <value>]
[--clone-from <value>]
[--binary-media-types <value>]
[--minimum-compression-size <value>]
[--api-key-source <value>]
[--endpoint-configuration <value>]
[--policy <value>]
[--tags <value>]
[--disable-execute-api-endpoint | --no-disable-execute-api-endpoint]
[--api-version <value>]
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

The name of the RestApi.

`--description` (string)

The description of the RestApi.

`--clone-from` (string)

The ID of the RestApi that you want to clone from.

`--binary-media-types` (list)

The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.

(string)

Syntax:

```
"string" "string" ...
```

`--minimum-compression-size` (integer)

A nullable integer that is used to enable compression (with non-negative between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When compression is enabled, compression or decompression is not applied on the payload if the payload size is smaller than this value. Setting it to zero allows compression for any payload size.

`--api-key-source` (string)

The source of the API key for metering requests according to a usage plan. Valid values are: `HEADER` to read the API key from the `X-API-Key` header of a request. `AUTHORIZER` to read the API key from the `UsageIdentifierKey` from a custom authorizer.

Possible values:

- `HEADER`
- `AUTHORIZER`

`--endpoint-configuration` (structure)

The endpoint configuration of this RestApi showing the endpoint types and IP address types of the API.

types -> (list)

A list of endpoint types of an API (RestApi) or its custom domain name (DomainName). For an edge-optimized API and its custom domain name, the endpoint type is `"EDGE"` . For a regional API and its custom domain name, the endpoint type is `REGIONAL` . For a private API, the endpoint type is `PRIVATE` .

(string)

The endpoint type. The valid values are `EDGE` for edge-optimized API setup, most suitable for mobile applications; `REGIONAL` for regional API endpoint setup, most suitable for calling from AWS Region; and `PRIVATE` for private APIs.

ipAddressType -> (string)

The IP address types that can invoke an API (RestApi) or a DomainName. Use `ipv4` to allow only IPv4 addresses to invoke an API or DomainName, or use `dualstack` to allow both IPv4 and IPv6 addresses to invoke an API or a DomainName. For the `PRIVATE` endpoint type, only `dualstack` is supported.

vpcEndpointIds -> (list)

A list of VpcEndpointIds of an API (RestApi) against which to create Route53 ALIASes. It is only supported for `PRIVATE` endpoint type.

(string)

Shorthand Syntax:

```
types=string,string,ipAddressType=string,vpcEndpointIds=string,string
```

JSON Syntax:

```
{
  "types": ["REGIONAL"|"EDGE"|"PRIVATE", ...],
  "ipAddressType": "ipv4"|"dualstack",
  "vpcEndpointIds": ["string", ...]
}
```

`--policy` (string)

A stringified JSON policy document that applies to this RestApi regardless of the caller and Method configuration.

`--tags` (map)

The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with `aws:` . The tag value can be up to 256 characters.

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

`--disable-execute-api-endpoint` | `--no-disable-execute-api-endpoint` (boolean)

Specifies whether clients can invoke your API by using the default `execute-api` endpoint. By default, clients can invoke your API with the default `https://{api_id}.execute-api.{region}.amazonaws.com` endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint

`--api-version` (string)

A version identifier for the API.

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

**To create an API**

Command:

```
aws apigateway create-rest-api --name 'My First API' --description 'This is my first API'
```

**To create a duplicate API from an existing API**

Command:

```
aws apigateway create-rest-api --name 'Copy of My First API' --description 'This is a copy of my first API' --clone-from 1234123412
```

## Output

id -> (string)

The APIâs identifier. This identifier is unique across all of your APIs in API Gateway.

name -> (string)

The APIâs name.

description -> (string)

The APIâs description.

createdDate -> (timestamp)

The timestamp when the API was created.

version -> (string)

A version identifier for the API.

warnings -> (list)

The warning messages reported when `failonwarnings` is turned on during API import.

(string)

binaryMediaTypes -> (list)

The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.

(string)

minimumCompressionSize -> (integer)

A nullable integer that is used to enable compression (with non-negative between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When compression is enabled, compression or decompression is not applied on the payload if the payload size is smaller than this value. Setting it to zero allows compression for any payload size.

apiKeySource -> (string)

The source of the API key for metering requests according to a usage plan. Valid values are: >``HEADER`` to read the API key from the `X-API-Key` header of a request. `AUTHORIZER` to read the API key from the `UsageIdentifierKey` from a custom authorizer.

endpointConfiguration -> (structure)

The endpoint configuration of this RestApi showing the endpoint types and IP address types of the API.

types -> (list)

A list of endpoint types of an API (RestApi) or its custom domain name (DomainName). For an edge-optimized API and its custom domain name, the endpoint type is `"EDGE"` . For a regional API and its custom domain name, the endpoint type is `REGIONAL` . For a private API, the endpoint type is `PRIVATE` .

(string)

The endpoint type. The valid values are `EDGE` for edge-optimized API setup, most suitable for mobile applications; `REGIONAL` for regional API endpoint setup, most suitable for calling from AWS Region; and `PRIVATE` for private APIs.

ipAddressType -> (string)

The IP address types that can invoke an API (RestApi) or a DomainName. Use `ipv4` to allow only IPv4 addresses to invoke an API or DomainName, or use `dualstack` to allow both IPv4 and IPv6 addresses to invoke an API or a DomainName. For the `PRIVATE` endpoint type, only `dualstack` is supported.

vpcEndpointIds -> (list)

A list of VpcEndpointIds of an API (RestApi) against which to create Route53 ALIASes. It is only supported for `PRIVATE` endpoint type.

(string)

policy -> (string)

A stringified JSON policy document that applies to this RestApi regardless of the caller and Method configuration.

tags -> (map)

The collection of tags. Each tag element is associated with a given resource.

key -> (string)

value -> (string)

disableExecuteApiEndpoint -> (boolean)

Specifies whether clients can invoke your API by using the default `execute-api` endpoint. By default, clients can invoke your API with the default `https://{api_id}.execute-api.{region}.amazonaws.com` endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.

rootResourceId -> (string)

The APIâs root resource ID.