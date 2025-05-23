# put-cors-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/put-cors-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/put-cors-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediastore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/index.html#cli-aws-mediastore) ]

# put-cors-policy

## Description

Sets the cross-origin resource sharing (CORS) configuration on a container so that the container can service cross-origin requests. For example, you might want to enable a request whose origin is [http://www.example.com](http://www.example.com) to access your AWS Elemental MediaStore container at my.example.container.com by using the browserâs XMLHttpRequest capability.

To enable CORS on a container, you attach a CORS policy to the container. In the CORS policy, you configure rules that identify origins and the HTTP methods that can be executed on your container. The policy can contain up to 398,000 characters. You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed.

To learn more about CORS, see [Cross-Origin Resource Sharing (CORS) in AWS Elemental MediaStore](https://docs.aws.amazon.com/mediastore/latest/ug/cors-policy.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/PutCorsPolicy)

## Synopsis

```
put-cors-policy
--container-name <value>
--cors-policy <value>
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

`--container-name` (string)

The name of the container that you want to assign the CORS policy to.

`--cors-policy` (list)

The CORS policy to apply to the container.

(structure)

A rule for a CORS policy. You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed.

AllowedOrigins -> (list)

One or more response headers that you want users to be able to access from their applications (for example, from a JavaScript `XMLHttpRequest` object).

Each CORS rule must have at least one `AllowedOrigins` element. The string value can include only one wildcard character (*), for example, [http://](http://)[*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/put-cors-policy.html#id1).example.com. Additionally, you can specify only one wildcard character to allow cross-origin access for all origins.

(string)

AllowedMethods -> (list)

Identifies an HTTP method that the origin that is specified in the rule is allowed to execute.

Each CORS rule must contain at least one `AllowedMethods` and one `AllowedOrigins` element.

(string)

AllowedHeaders -> (list)

Specifies which headers are allowed in a preflight `OPTIONS` request through the `Access-Control-Request-Headers` header. Each header name that is specified in `Access-Control-Request-Headers` must have a corresponding entry in the rule. Only the headers that were requested are sent back.

This element can contain only one wildcard character (*).

(string)

MaxAgeSeconds -> (integer)

The time in seconds that your browser caches the preflight response for the specified resource.

A CORS rule can have only one `MaxAgeSeconds` element.

ExposeHeaders -> (list)

One or more headers in the response that you want users to be able to access from their applications (for example, from a JavaScript `XMLHttpRequest` object).

This element is optional for each rule.

(string)

Shorthand Syntax:

```
AllowedOrigins=string,string,AllowedMethods=string,string,AllowedHeaders=string,string,MaxAgeSeconds=integer,ExposeHeaders=string,string ...
```

JSON Syntax:

```
[
  {
    "AllowedOrigins": ["string", ...],
    "AllowedMethods": ["PUT"|"GET"|"DELETE"|"HEAD", ...],
    "AllowedHeaders": ["string", ...],
    "MaxAgeSeconds": integer,
    "ExposeHeaders": ["string", ...]
  }
  ...
]
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

**Example 1: To add a CORS policy**

The following `put-cors-policy` example adds a cross-origin resource sharing (CORS) policy to the specified container. The contents of the CORS policy are in the file named `corsPolicy.json`.

```
aws mediastore put-cors-policy \
    --container-name ExampleContainer \
    --cors-policy file://corsPolicy.json
```

This command produces no output.

For more information, see [Adding a CORS Policy to a Container](https://docs.aws.amazon.com/mediastore/latest/ug/cors-policy-adding.html) in the *AWS Elemental MediaStore User Guide*.

**Example 2: To edit a CORS policy**

The following `put-cors-policy` example updates the cross-origin resource sharing (CORS) policy that is assigned to the specified container. The contents of the updated CORS policy are in the file named `corsPolicy2.json`.

For more information, see [Editing a CORS Policy](https://docs.aws.amazon.com/mediastore/latest/ug/cors-policy-editing.html) in the *AWS Elemental MediaStore User Guide*.

## Output

None