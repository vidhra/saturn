# describe-listener-attributesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-listener-attributes.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-listener-attributes.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elbv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/index.html#cli-aws-elbv2) ]

# describe-listener-attributes

## Description

Describes the attributes for the specified listener.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeListenerAttributes)

## Synopsis

```
describe-listener-attributes
--listener-arn <value>
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

`--listener-arn` (string)

The Amazon Resource Name (ARN) of the listener.

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

## Output

Attributes -> (list)

Information about the listener attributes.

(structure)

Information about a listener attribute.

Key -> (string)

The name of the attribute.

The following attribute is supported by Network Load Balancers, and Gateway Load Balancers.

- `tcp.idle_timeout.seconds` - The tcp idle timeout value, in seconds. The valid range is 60-6000 seconds. The default is 350 seconds.

The following attributes are only supported by Application Load Balancers.

- `routing.http.request.x_amzn_mtls_clientcert_serial_number.header_name` - Enables you to modify the header name of the **X-Amzn-Mtls-Clientcert-Serial-Number** HTTP request header.
- `routing.http.request.x_amzn_mtls_clientcert_issuer.header_name` - Enables you to modify the header name of the **X-Amzn-Mtls-Clientcert-Issuer** HTTP request header.
- `routing.http.request.x_amzn_mtls_clientcert_subject.header_name` - Enables you to modify the header name of the **X-Amzn-Mtls-Clientcert-Subject** HTTP request header.
- `routing.http.request.x_amzn_mtls_clientcert_validity.header_name` - Enables you to modify the header name of the **X-Amzn-Mtls-Clientcert-Validity** HTTP request header.
- `routing.http.request.x_amzn_mtls_clientcert_leaf.header_name` - Enables you to modify the header name of the **X-Amzn-Mtls-Clientcert-Leaf** HTTP request header.
- `routing.http.request.x_amzn_mtls_clientcert.header_name` - Enables you to modify the header name of the **X-Amzn-Mtls-Clientcert** HTTP request header.
- `routing.http.request.x_amzn_tls_version.header_name` - Enables you to modify the header name of the **X-Amzn-Tls-Version** HTTP request header.
- `routing.http.request.x_amzn_tls_cipher_suite.header_name` - Enables you to modify the header name of the **X-Amzn-Tls-Cipher-Suite** HTTP request header.
- `routing.http.response.server.enabled` - Enables you to allow or remove the HTTP response server header.
- `routing.http.response.strict_transport_security.header_value` - Informs browsers that the site should only be accessed using HTTPS, and that any future attempts to access it using HTTP should automatically be converted to HTTPS.
- `routing.http.response.access_control_allow_origin.header_value` - Specifies which origins are allowed to access the server.
- `routing.http.response.access_control_allow_methods.header_value` - Returns which HTTP methods are allowed when accessing the server from a different origin.
- `routing.http.response.access_control_allow_headers.header_value` - Specifies which headers can be used during the request.
- `routing.http.response.access_control_allow_credentials.header_value` - Indicates whether the browser should include credentials such as cookies or authentication when making requests.
- `routing.http.response.access_control_expose_headers.header_value` - Returns which headers the browser can expose to the requesting client.
- `routing.http.response.access_control_max_age.header_value` - Specifies how long the results of a preflight request can be cached, in seconds.
- `routing.http.response.content_security_policy.header_value` - Specifies restrictions enforced by the browser to help minimize the risk of certain types of security threats.
- `routing.http.response.x_content_type_options.header_value` - Indicates whether the MIME types advertised in the **Content-Type** headers should be followed and not be changed.
- `routing.http.response.x_frame_options.header_value` - Indicates whether the browser is allowed to render a page in a **frame** , **iframe** , **embed** or **object** .

Value -> (string)

The value of the attribute.