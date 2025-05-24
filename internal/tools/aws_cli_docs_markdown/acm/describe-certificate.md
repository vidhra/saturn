# describe-certificateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/describe-certificate.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/describe-certificate.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [acm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/index.html#cli-aws-acm) ]

# describe-certificate

## Description

Returns detailed metadata about the specified ACM certificate.

If you have just created a certificate using the `RequestCertificate` action, there is a delay of several seconds before you can retrieve information about it.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/DescribeCertificate)

## Synopsis

```
describe-certificate
--certificate-arn <value>
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

`--certificate-arn` (string)

The Amazon Resource Name (ARN) of the ACM certificate. The ARN must have the following form:

`arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012`

For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

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

**To retrieve the fields contained in an ACM certificate**

The following `describe-certificate` command retrieves all of the fields for the certificate with the specified ARN:

```
aws acm describe-certificate --certificate-arn arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012
```

Output similar to the following is displayed:

```
{
  "Certificate": {
    "CertificateArn": "arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012",
    "CreatedAt": 1446835267.0,
    "DomainName": "www.example.com",
    "DomainValidationOptions": [
      {
        "DomainName": "www.example.com",
        "ValidationDomain": "www.example.com",
        "ValidationEmails": [
          "hostmaster@example.com",
          "admin@example.com",
          "owner@example.com.whoisprivacyservice.org",
          "tech@example.com.whoisprivacyservice.org",
          "admin@example.com.whoisprivacyservice.org",
          "postmaster@example.com",
          "webmaster@example.com",
          "administrator@example.com"
        ]
      },
      {
        "DomainName": "www.example.net",
        "ValidationDomain": "www.example.net",
        "ValidationEmails": [
          "postmaster@example.net",
          "admin@example.net",
          "owner@example.net.whoisprivacyservice.org",
          "tech@example.net.whoisprivacyservice.org",
          "admin@example.net.whoisprivacyservice.org",
          "hostmaster@example.net",
          "administrator@example.net",
          "webmaster@example.net"
        ]
      }
    ],
    "InUseBy": [],
    "IssuedAt": 1446835815.0,
    "Issuer": "Amazon",
    "KeyAlgorithm": "RSA-2048",
    "NotAfter": 1478433600.0,
    "NotBefore": 1446768000.0,
    "Serial": "0f:ac:b0:a3:8d:ea:65:52:2d:7d:01:3a:39:36:db:d6",
    "SignatureAlgorithm": "SHA256WITHRSA",
    "Status": "ISSUED",
    "Subject": "CN=www.example.com",
    "SubjectAlternativeNames": [
      "www.example.com",
      "www.example.net"
    ]
  }
}
```

## Output

Certificate -> (structure)

Metadata about an ACM certificate.

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate. For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

DomainName -> (string)

The fully qualified domain name for the certificate, such as www.example.com or example.com.

SubjectAlternativeNames -> (list)

One or more domain names (subject alternative names) included in the certificate. This list contains the domain names that are bound to the public key that is contained in the certificate. The subject alternative names include the canonical domain name (CN) of the certificate and additional domain names that can be used to connect to the website.

(string)

ManagedBy -> (string)

Identifies the Amazon Web Services service that manages the certificate issued by ACM.

DomainValidationOptions -> (list)

Contains information about the initial validation of each domain name that occurs as a result of the  RequestCertificate request. This field exists only when the certificate type is `AMAZON_ISSUED` .

(structure)

Contains information about the validation of each domain name in the certificate.

DomainName -> (string)

A fully qualified domain name (FQDN) in the certificate. For example, `www.example.com` or `example.com` .

ValidationEmails -> (list)

A list of email addresses that ACM used to send domain validation emails.

(string)

ValidationDomain -> (string)

The domain name that ACM used to send domain validation emails.

ValidationStatus -> (string)

The validation status of the domain name. This can be one of the following values:

- `PENDING_VALIDATION`
- SUCCESS
- FAILED

ResourceRecord -> (structure)

Contains the CNAME record that you add to your DNS database for domain validation. For more information, see [Use DNS to Validate Domain Ownership](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html) .

Note: The CNAME information that you need does not include the name of your domain. If you include your domain name in the DNS database CNAME record, validation fails. For example, if the name is â_a79865eb4cd1a6ab990a45779b4e0b96.yourdomain.comâ, only â_a79865eb4cd1a6ab990a45779b4e0b96â must be used.

Name -> (string)

The name of the DNS record to create in your domain. This is supplied by ACM.

Type -> (string)

The type of DNS record. Currently this can be `CNAME` .

Value -> (string)

The value of the CNAME record to add to your DNS database. This is supplied by ACM.

HttpRedirect -> (structure)

Contains information for HTTP-based domain validation of certificates requested through CloudFront and issued by ACM. This field exists only when the certificate type is `AMAZON_ISSUED` and the validation method is `HTTP` .

RedirectFrom -> (string)

The URL including the domain to be validated. The certificate authority sends `GET` requests here during validation.

RedirectTo -> (string)

The URL hosting the validation token. `RedirectFrom` must return this content or redirect here.

ValidationMethod -> (string)

Specifies the domain validation method.

Serial -> (string)

The serial number of the certificate.

Subject -> (string)

The name of the entity that is associated with the public key contained in the certificate.

Issuer -> (string)

The name of the certificate authority that issued and signed the certificate.

CreatedAt -> (timestamp)

The time at which the certificate was requested.

IssuedAt -> (timestamp)

The time at which the certificate was issued. This value exists only when the certificate type is `AMAZON_ISSUED` .

ImportedAt -> (timestamp)

The date and time when the certificate was imported. This value exists only when the certificate type is `IMPORTED` .

Status -> (string)

The status of the certificate.

A certificate enters status PENDING_VALIDATION upon being requested, unless it fails for any of the reasons given in the troubleshooting topic [Certificate request fails](https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting-failed.html) . ACM makes repeated attempts to validate a certificate for 72 hours and then times out. If a certificate shows status FAILED or VALIDATION_TIMED_OUT, delete the request, correct the issue with [DNS validation](https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html) or [Email validation](https://docs.aws.amazon.com/acm/latest/userguide/email-validation.html) , and try again. If validation succeeds, the certificate enters status ISSUED.

RevokedAt -> (timestamp)

The time at which the certificate was revoked. This value exists only when the certificate status is `REVOKED` .

RevocationReason -> (string)

The reason the certificate was revoked. This value exists only when the certificate status is `REVOKED` .

NotBefore -> (timestamp)

The time before which the certificate is not valid.

NotAfter -> (timestamp)

The time after which the certificate is not valid.

KeyAlgorithm -> (string)

The algorithm that was used to generate the public-private key pair.

SignatureAlgorithm -> (string)

The algorithm that was used to sign the certificate.

InUseBy -> (list)

A list of ARNs for the Amazon Web Services resources that are using the certificate. A certificate can be used by multiple Amazon Web Services resources.

(string)

FailureReason -> (string)

The reason the certificate request failed. This value exists only when the certificate status is `FAILED` . For more information, see [Certificate Request Failed](https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting.html#troubleshooting-failed) in the *Certificate Manager User Guide* .

Type -> (string)

The source of the certificate. For certificates provided by ACM, this value is `AMAZON_ISSUED` . For certificates that you imported with  ImportCertificate , this value is `IMPORTED` . ACM does not provide [managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html) for imported certificates. For more information about the differences between certificates that you import and those that ACM provides, see [Importing Certificates](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the *Certificate Manager User Guide* .

RenewalSummary -> (structure)

Contains information about the status of ACMâs [managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html) for the certificate. This field exists only when the certificate type is `AMAZON_ISSUED` .

RenewalStatus -> (string)

The status of ACMâs [managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html) of the certificate.

DomainValidationOptions -> (list)

Contains information about the validation of each domain name in the certificate, as it pertains to ACMâs [managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html) . This is different from the initial validation that occurs as a result of the  RequestCertificate request. This field exists only when the certificate type is `AMAZON_ISSUED` .

(structure)

Contains information about the validation of each domain name in the certificate.

DomainName -> (string)

A fully qualified domain name (FQDN) in the certificate. For example, `www.example.com` or `example.com` .

ValidationEmails -> (list)

A list of email addresses that ACM used to send domain validation emails.

(string)

ValidationDomain -> (string)

The domain name that ACM used to send domain validation emails.

ValidationStatus -> (string)

The validation status of the domain name. This can be one of the following values:

- `PENDING_VALIDATION`
- SUCCESS
- FAILED

ResourceRecord -> (structure)

Contains the CNAME record that you add to your DNS database for domain validation. For more information, see [Use DNS to Validate Domain Ownership](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html) .

Note: The CNAME information that you need does not include the name of your domain. If you include your domain name in the DNS database CNAME record, validation fails. For example, if the name is â_a79865eb4cd1a6ab990a45779b4e0b96.yourdomain.comâ, only â_a79865eb4cd1a6ab990a45779b4e0b96â must be used.

Name -> (string)

The name of the DNS record to create in your domain. This is supplied by ACM.

Type -> (string)

The type of DNS record. Currently this can be `CNAME` .

Value -> (string)

The value of the CNAME record to add to your DNS database. This is supplied by ACM.

HttpRedirect -> (structure)

Contains information for HTTP-based domain validation of certificates requested through CloudFront and issued by ACM. This field exists only when the certificate type is `AMAZON_ISSUED` and the validation method is `HTTP` .

RedirectFrom -> (string)

The URL including the domain to be validated. The certificate authority sends `GET` requests here during validation.

RedirectTo -> (string)

The URL hosting the validation token. `RedirectFrom` must return this content or redirect here.

ValidationMethod -> (string)

Specifies the domain validation method.

RenewalStatusReason -> (string)

The reason that a renewal request was unsuccessful.

UpdatedAt -> (timestamp)

The time at which the renewal summary was last updated.

KeyUsages -> (list)

A list of Key Usage X.509 v3 extension objects. Each object is a string value that identifies the purpose of the public key contained in the certificate. Possible extension values include DIGITAL_SIGNATURE, KEY_ENCHIPHERMENT, NON_REPUDIATION, and more.

(structure)

The Key Usage X.509 v3 extension defines the purpose of the public key contained in the certificate.

Name -> (string)

A string value that contains a Key Usage extension name.

ExtendedKeyUsages -> (list)

Contains a list of Extended Key Usage X.509 v3 extension objects. Each object specifies a purpose for which the certificate public key can be used and consists of a name and an object identifier (OID).

(structure)

The Extended Key Usage X.509 v3 extension defines one or more purposes for which the public key can be used. This is in addition to or in place of the basic purposes specified by the Key Usage extension.

Name -> (string)

The name of an Extended Key Usage value.

OID -> (string)

An object identifier (OID) for the extension value. OIDs are strings of numbers separated by periods. The following OIDs are defined in RFC 3280 and RFC 5280.

- `1.3.6.1.5.5.7.3.1 (TLS_WEB_SERVER_AUTHENTICATION)`
- `1.3.6.1.5.5.7.3.2 (TLS_WEB_CLIENT_AUTHENTICATION)`
- `1.3.6.1.5.5.7.3.3 (CODE_SIGNING)`
- `1.3.6.1.5.5.7.3.4 (EMAIL_PROTECTION)`
- `1.3.6.1.5.5.7.3.8 (TIME_STAMPING)`
- `1.3.6.1.5.5.7.3.9 (OCSP_SIGNING)`
- `1.3.6.1.5.5.7.3.5 (IPSEC_END_SYSTEM)`
- `1.3.6.1.5.5.7.3.6 (IPSEC_TUNNEL)`
- `1.3.6.1.5.5.7.3.7 (IPSEC_USER)`

CertificateAuthorityArn -> (string)

The Amazon Resource Name (ARN) of the private certificate authority (CA) that issued the certificate. This has the following format:

`arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012`

RenewalEligibility -> (string)

Specifies whether the certificate is eligible for renewal. At this time, only exported private certificates can be renewed with the  RenewCertificate command.

Options -> (structure)

Value that specifies whether to add the certificate to a transparency log. Certificate transparency makes it possible to detect SSL certificates that have been mistakenly or maliciously issued. A browser might respond to certificate that has not been logged by showing an error message. The logs are cryptographically secure.

CertificateTransparencyLoggingPreference -> (string)

You can opt out of certificate transparency logging by specifying the `DISABLED` option. Opt in by specifying `ENABLED` .