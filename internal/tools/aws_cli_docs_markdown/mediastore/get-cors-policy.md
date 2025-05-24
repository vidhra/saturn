# get-cors-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/get-cors-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/get-cors-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediastore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/index.html#cli-aws-mediastore) ]

# get-cors-policy

## Description

Returns the cross-origin resource sharing (CORS) configuration information that is set for the container.

To use this operation, you must have permission to perform the `MediaStore:GetCorsPolicy` action. By default, the container owner has this permission and can grant it to others.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediastore-2017-09-01/GetCorsPolicy)

## Synopsis

```
get-cors-policy
--container-name <value>
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

The name of the container that the policy is assigned to.

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

**To view a CORS policy**

The following `get-cors-policy` example displays the cross-origin resource sharing (CORS) policy that is assigned to the specified container.

```
aws mediastore get-cors-policy \
    --container-name ExampleContainer \
    --region us-west-2
```

Output:

```
{
    "CorsPolicy": [
        {
            "AllowedMethods": [
                "GET",
                "HEAD"
            ],
            "MaxAgeSeconds": 3000,
            "AllowedOrigins": [
                ""
            ],
            "AllowedHeaders": [
                ""
            ]
        }
    ]
}
```

For more information, see [Viewing a CORS Policy](https://docs.aws.amazon.com/mediastore/latest/ug/cors-policy-viewing.html) in the *AWS Elemental MediaStore User Guide*.

## Output

CorsPolicy -> (list)

The CORS policy assigned to the container.

(structure)

A rule for a CORS policy. You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed.

AllowedOrigins -> (list)

One or more response headers that you want users to be able to access from their applications (for example, from a JavaScript `XMLHttpRequest` object).

Each CORS rule must have at least one `AllowedOrigins` element. The string value can include only one wildcard character (*), for example, [http://](http://)[*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/get-cors-policy.html#id1).example.com. Additionally, you can specify only one wildcard character to allow cross-origin access for all origins.

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