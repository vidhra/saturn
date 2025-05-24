# describe-domain-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-domain-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-domain-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html#cli-aws-iot) ]

# describe-domain-configuration

## Description

Gets summary information about a domain configuration.

Requires permission to access the [DescribeDomainConfiguration](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeDomainConfiguration)

## Synopsis

```
describe-domain-configuration
--domain-configuration-name <value>
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

`--domain-configuration-name` (string)

The name of the domain configuration.

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

**To describe a domain configuration**

The following `describe-domain-configuration` example displays details about the specified domain configuration.

```
aws iot describe-domain-configuration \
    --domain-configuration-name "additionalDataDomain"
```

Output:

```
{
    "domainConfigurationName": "additionalDataDomain",
    "domainConfigurationArn": "arn:aws:iot:us-east-1:758EXAMPLE143:domainconfiguration/additionalDataDomain/norpw",
    "domainName": "d055exampleed74y71zfd-ats.beta.us-east-1.iot.amazonaws.com",
    "serverCertificates": [],
    "domainConfigurationStatus": "ENABLED",
    "serviceType": "DATA",
    "domainType": "AWS_MANAGED",
    "lastStatusChangeDate": 1601923783.774
}
```

For more information, see [Configurable Endpoints](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-configurable-aws.html) in the *AWS IoT Developer Guide*.

## Output

domainConfigurationName -> (string)

The name of the domain configuration.

domainConfigurationArn -> (string)

The ARN of the domain configuration.

domainName -> (string)

The name of the domain.

serverCertificates -> (list)

A list containing summary information about the server certificate included in the domain configuration.

(structure)

An object that contains information about a server certificate.

serverCertificateArn -> (string)

The ARN of the server certificate.

serverCertificateStatus -> (string)

The status of the server certificate.

serverCertificateStatusDetail -> (string)

Details that explain the status of the server certificate.

authorizerConfig -> (structure)

An object that specifies the authorization service for a domain.

defaultAuthorizerName -> (string)

The name of the authorization service for a domain configuration.

allowAuthorizerOverride -> (boolean)

A Boolean that specifies whether the domain configurationâs authorization service can be overridden.

domainConfigurationStatus -> (string)

A Boolean value that specifies the current state of the domain configuration.

serviceType -> (string)

The type of service delivered by the endpoint.

domainType -> (string)

The type of the domain.

lastStatusChangeDate -> (timestamp)

The date and time the domain configurationâs status was last changed.

tlsConfig -> (structure)

An object that specifies the TLS configuration for a domain.

securityPolicy -> (string)

The security policy for a domain configuration. For more information, see [Security policies](https://docs.aws.amazon.com/iot/latest/developerguide/transport-security.html#tls-policy-table) in the *Amazon Web Services IoT Core developer guide* .

serverCertificateConfig -> (structure)

The server certificate configuration.

enableOCSPCheck -> (boolean)

A Boolean value that indicates whether Online Certificate Status Protocol (OCSP) server certificate check is enabled or not.

For more information, see [Server certificate configuration for OCSP stapling](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-cert-config.html) from Amazon Web Services IoT Core Developer Guide.

ocspLambdaArn -> (string)

The Amazon Resource Name (ARN) for a Lambda function that acts as a Request for Comments (RFC) 6960-compliant Online Certificate Status Protocol (OCSP) responder, supporting basic OCSP responses. The Lambda function accepts a base64-encoding of the OCSP request in the Distinguished Encoding Rules (DER) format. The Lambda functionâs response is also a base64-encoded OCSP response in the DER format. The response size must not exceed 4 kilobytes (KiB). The Lambda function must be in the same Amazon Web Services account and region as the domain configuration. For more information, see [Configuring server certificate OCSP for private endpoints in Amazon Web Services IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-cert-config.html#iot-custom-endpoints-cert-config-ocsp-private-endpoint.html) from the Amazon Web Services IoT Core developer guide.

ocspAuthorizedResponderArn -> (string)

The Amazon Resource Name (ARN) for an X.509 certificate stored in Amazon Web Services Certificate Manager (ACM). If provided, Amazon Web Services IoT Core will use this certificate to validate the signature of the received OCSP response. The OCSP responder must sign responses using either this authorized responder certificate or the issuing certificate, depending on whether the ARN is provided or not. The certificate must be in the same Amazon Web Services account and region as the domain configuration.

authenticationType -> (string)

An enumerated string that speciï¬es the authentication type.

- `CUSTOM_AUTH_X509` - Use custom authentication and authorization with additional details from the X.509 client certificate.
- `CUSTOM_AUTH` - Use custom authentication and authorization. For more information, see [Custom authentication and authorization](https://docs.aws.amazon.com/iot/latest/developerguide/custom-authentication.html) .
- `AWS_X509` - Use X.509 client certificates without custom authentication and authorization. For more information, see [X.509 client certificates](https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html) .
- `AWS_SIGV4` - Use Amazon Web Services Signature Version 4. For more information, see [IAM users, groups, and roles](https://docs.aws.amazon.com/iot/latest/developerguide/custom-authentication.html) .
- `DEFAULT` - Use a combination of port and Application Layer Protocol Negotiation (ALPN) to specify authentication type. For more information, see [Device communication protocols](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html) .

applicationProtocol -> (string)

An enumerated string that speciï¬es the application-layer protocol.

- `SECURE_MQTT` - MQTT over TLS.
- `MQTT_WSS` - MQTT over WebSocket.
- `HTTPS` - HTTP over TLS.
- `DEFAULT` - Use a combination of port and Application Layer Protocol Negotiation (ALPN) to specify application_layer protocol. For more information, see [Device communication protocols](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html) .

clientCertificateConfig -> (structure)

An object that speciï¬es the client certificate conï¬guration for a domain.

clientCertificateCallbackArn -> (string)

The ARN of the Lambda function that IoT invokes after mutual TLS authentication during the connection.