# create-domain-nameÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-domain-name.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-domain-name.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [apigatewayv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/index.html#cli-aws-apigatewayv2) ]

# create-domain-name

## Description

Creates a domain name.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/CreateDomainName)

## Synopsis

```
create-domain-name
--domain-name <value>
[--domain-name-configurations <value>]
[--mutual-tls-authentication <value>]
[--tags <value>]
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

`--domain-name` (string)

The domain name.

`--domain-name-configurations` (list)

The domain name configurations.

(structure)

The domain name configuration.

ApiGatewayDomainName -> (string)

A domain name for the API.

CertificateArn -> (string)

An AWS-managed certificate that will be used by the edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.

CertificateName -> (string)

The user-friendly name of the certificate that will be used by the edge-optimized endpoint for this domain name.

CertificateUploadDate -> (timestamp)

The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded.

DomainNameStatus -> (string)

The status of the domain name migration. The valid values are AVAILABLE, UPDATING, PENDING_CERTIFICATE_REIMPORT, and PENDING_OWNERSHIP_VERIFICATION. If the status is UPDATING, the domain cannot be modified further until the existing operation is complete. If it is AVAILABLE, the domain can be updated.

DomainNameStatusMessage -> (string)

An optional text message containing detailed information about status of the domain name migration.

EndpointType -> (string)

The endpoint type.

HostedZoneId -> (string)

The Amazon Route 53 Hosted Zone ID of the endpoint.

IpAddressType -> (string)

The IP address types that can invoke the domain name. Use ipv4 to allow only IPv4 addresses to invoke your domain name, or use dualstack to allow both IPv4 and IPv6 addresses to invoke your domain name.

SecurityPolicy -> (string)

The Transport Layer Security (TLS) version of the security policy for this domain name. The valid values are TLS_1_0 and TLS_1_2.

OwnershipVerificationCertificateArn -> (string)

The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Only required when configuring mutual TLS and using an ACM imported or private CA certificate ARN as the regionalCertificateArn

Shorthand Syntax:

```
ApiGatewayDomainName=string,CertificateArn=string,CertificateName=string,CertificateUploadDate=timestamp,DomainNameStatus=string,DomainNameStatusMessage=string,EndpointType=string,HostedZoneId=string,IpAddressType=string,SecurityPolicy=string,OwnershipVerificationCertificateArn=string ...
```

JSON Syntax:

```
[
  {
    "ApiGatewayDomainName": "string",
    "CertificateArn": "string",
    "CertificateName": "string",
    "CertificateUploadDate": timestamp,
    "DomainNameStatus": "AVAILABLE"|"UPDATING"|"PENDING_CERTIFICATE_REIMPORT"|"PENDING_OWNERSHIP_VERIFICATION",
    "DomainNameStatusMessage": "string",
    "EndpointType": "REGIONAL"|"EDGE",
    "HostedZoneId": "string",
    "IpAddressType": "ipv4"|"dualstack",
    "SecurityPolicy": "TLS_1_0"|"TLS_1_2",
    "OwnershipVerificationCertificateArn": "string"
  }
  ...
]
```

`--mutual-tls-authentication` (structure)

The mutual TLS authentication configuration for a custom domain name.

TruststoreUri -> (string)

An Amazon S3 URL that specifies the truststore for mutual TLS authentication, for example, s3://bucket-name/key-name. The truststore can contain certificates from public or private certificate authorities. To update the truststore, upload a new version to S3, and then update your custom domain name to use the new version. To update the truststore, you must have permissions to access the S3 object.

TruststoreVersion -> (string)

The version of the S3 object that contains your truststore. To specify a version, you must have versioning enabled for the S3 bucket.

Shorthand Syntax:

```
TruststoreUri=string,TruststoreVersion=string
```

JSON Syntax:

```
{
  "TruststoreUri": "string",
  "TruststoreVersion": "string"
}
```

`--tags` (map)

The collection of tags associated with a domain name.

key -> (string)

value -> (string)

A string with a length between [0-1600].

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

**To create a custom domain name**

The following `create-domain-name` example creates a regional custom domain name for an API.

```
aws apigatewayv2 create-domain-name \
    --domain-name regional.example.com \
    --domain-name-configurations CertificateArn=arn:aws:acm:us-west-2:123456789012:certificate/123456789012-1234-1234-1234-12345678
```

Output:

```
{
    "ApiMappingSelectionExpression": "$request.basepath",
    "DomainName": "regional.example.com",
    "DomainNameConfigurations": [
        {
            "ApiGatewayDomainName": "d-id.execute-api.us-west-2.amazonaws.com",
            "CertificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/123456789012-1234-1234-1234-12345678",
            "EndpointType": "REGIONAL",
            "HostedZoneId": "123456789111",
            "SecurityPolicy": "TLS_1_2",
            "DomainNameStatus": "AVAILABLE"
        }
    ]
}
```

For more information, see [Setting up a regional custom domain name in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html) in the *Amazon API Gateway Developer Guide*.

## Output

ApiMappingSelectionExpression -> (string)

The API mapping selection expression.

DomainName -> (string)

The name of the DomainName resource.

DomainNameConfigurations -> (list)

The domain name configurations.

(structure)

The domain name configuration.

ApiGatewayDomainName -> (string)

A domain name for the API.

CertificateArn -> (string)

An AWS-managed certificate that will be used by the edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.

CertificateName -> (string)

The user-friendly name of the certificate that will be used by the edge-optimized endpoint for this domain name.

CertificateUploadDate -> (timestamp)

The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded.

DomainNameStatus -> (string)

The status of the domain name migration. The valid values are AVAILABLE, UPDATING, PENDING_CERTIFICATE_REIMPORT, and PENDING_OWNERSHIP_VERIFICATION. If the status is UPDATING, the domain cannot be modified further until the existing operation is complete. If it is AVAILABLE, the domain can be updated.

DomainNameStatusMessage -> (string)

An optional text message containing detailed information about status of the domain name migration.

EndpointType -> (string)

The endpoint type.

HostedZoneId -> (string)

The Amazon Route 53 Hosted Zone ID of the endpoint.

IpAddressType -> (string)

The IP address types that can invoke the domain name. Use ipv4 to allow only IPv4 addresses to invoke your domain name, or use dualstack to allow both IPv4 and IPv6 addresses to invoke your domain name.

SecurityPolicy -> (string)

The Transport Layer Security (TLS) version of the security policy for this domain name. The valid values are TLS_1_0 and TLS_1_2.

OwnershipVerificationCertificateArn -> (string)

The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Only required when configuring mutual TLS and using an ACM imported or private CA certificate ARN as the regionalCertificateArn

MutualTlsAuthentication -> (structure)

The mutual TLS authentication configuration for a custom domain name.

TruststoreUri -> (string)

An Amazon S3 URL that specifies the truststore for mutual TLS authentication, for example, s3://bucket-name/key-name. The truststore can contain certificates from public or private certificate authorities. To update the truststore, upload a new version to S3, and then update your custom domain name to use the new version. To update the truststore, you must have permissions to access the S3 object.

TruststoreVersion -> (string)

The version of the S3 object that contains your truststore. To specify a version, you must have versioning enabled for the S3 bucket.

TruststoreWarnings -> (list)

A list of warnings that API Gateway returns while processing your truststore. Invalid certificates produce warnings. Mutual TLS is still enabled, but some clients might not be able to access your API. To resolve warnings, upload a new truststore to S3, and then update you domain name to use the new version.

(string)

Tags -> (map)

The collection of tags associated with a domain name.

key -> (string)

value -> (string)

A string with a length between [0-1600].