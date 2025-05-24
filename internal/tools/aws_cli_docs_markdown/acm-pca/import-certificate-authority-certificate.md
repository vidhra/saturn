# import-certificate-authority-certificateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/import-certificate-authority-certificate.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/import-certificate-authority-certificate.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [acm-pca](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/index.html#cli-aws-acm-pca) ]

# import-certificate-authority-certificate

## Description

Imports a signed private CA certificate into Amazon Web Services Private CA. This action is used when you are using a chain of trust whose root is located outside Amazon Web Services Private CA. Before you can call this action, the following preparations must in place:

- In Amazon Web Services Private CA, call the [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html) action to create the private CA that you plan to back with the imported certificate.
- Call the [GetCertificateAuthorityCsr](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCsr.html) action to generate a certificate signing request (CSR).
- Sign the CSR using a root or intermediate CA hosted by either an on-premises PKI hierarchy or by a commercial CA.
- Create a certificate chain and copy the signed certificate and the certificate chain to your working directory.

Amazon Web Services Private CA supports three scenarios for installing a CA certificate:

- Installing a certificate for a root CA hosted by Amazon Web Services Private CA.
- Installing a subordinate CA certificate whose parent authority is hosted by Amazon Web Services Private CA.
- Installing a subordinate CA certificate whose parent authority is externally hosted.

The following additional requirements apply when you import a CA certificate.

- Only a self-signed certificate can be imported as a root CA.
- A self-signed certificate cannot be imported as a subordinate CA.
- Your certificate chain must not include the private CA certificate that you are importing.
- Your root CA must be the last certificate in your chain. The subordinate certificate, if any, that your root CA signed must be next to last. The subordinate certificate signed by the preceding subordinate CA must come next, and so on until your chain is built.
- The chain must be PEM-encoded.
- The maximum allowed size of a certificate is 32 KB.
- The maximum allowed size of a certificate chain is 2 MB.

*Enforcement of Critical Constraints*

Amazon Web Services Private CA allows the following extensions to be marked critical in the imported CA certificate or chain.

- Authority key identifier
- Basic constraints (*must* be marked critical)
- Certificate policies
- Extended key usage
- Inhibit anyPolicy
- Issuer alternative name
- Key usage
- Name constraints
- Policy mappings
- Subject alternative name
- Subject directory attributes
- Subject key identifier
- Subject information access

Amazon Web Services Private CA rejects the following extensions when they are marked critical in an imported CA certificate or chain.

- Authority information access
- CRL distribution points
- Freshest CRL
- Policy constraints

Amazon Web Services Private Certificate Authority will also reject any other extension marked as critical not contained on the preceding list of allowed extensions.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/ImportCertificateAuthorityCertificate)

## Synopsis

```
import-certificate-authority-certificate
--certificate-authority-arn <value>
--certificate <value>
[--certificate-chain <value>]
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

`--certificate-authority-arn` (string)

The Amazon Resource Name (ARN) that was returned when you called [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html) . This must be of the form:

[``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/import-certificate-authority-certificate.html#id1)arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* ``

`--certificate` (blob)

The PEM-encoded certificate for a private CA. This may be a self-signed certificate in the case of a root CA, or it may be signed by another CA that you control.

`--certificate-chain` (blob)

A PEM-encoded file that contains all of your certificates, other than the certificate youâre importing, chaining up to your root CA. Your Amazon Web Services Private CA-hosted or on-premises root certificate is the last in the chain, and each certificate in the chain signs the one preceding.

This parameter must be supplied when you import a subordinate CA. When you import a root CA, there is no chain.

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

**To import your certificate authority certificate into ACM PCA**

The following `import-certificate-authority-certificate` command imports the signed private CA certificate for the CA specified by the ARN into ACM PCA.

```
aws acm-pca import-certificate-authority-certificate --certificate-authority-arn arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/12345678-1234-1234-1234-123456789012 --certificate fileb://C:\ca_cert.pem --certificate-chain fileb://C:\ca_cert_chain.pem
```

## Output

None