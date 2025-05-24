# issue-certificateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/issue-certificate.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/issue-certificate.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [acm-pca](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/index.html#cli-aws-acm-pca) ]

# issue-certificate

## Description

Uses your private certificate authority (CA), or one that has been shared with you, to issue a client certificate. This action returns the Amazon Resource Name (ARN) of the certificate. You can retrieve the certificate by calling the [GetCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificate.html) action and specifying the ARN.

### Note

You cannot use the ACM **ListCertificateAuthorities** action to retrieve the ARNs of the certificates that you issue by using Amazon Web Services Private CA.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/IssueCertificate)

## Synopsis

```
issue-certificate
[--api-passthrough <value>]
--certificate-authority-arn <value>
--csr <value>
--signing-algorithm <value>
[--template-arn <value>]
--validity <value>
[--validity-not-before <value>]
[--idempotency-token <value>]
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

`--api-passthrough` (structure)

Specifies X.509 certificate information to be included in the issued certificate. An `APIPassthrough` or `APICSRPassthrough` template variant must be selected, or else this parameter is ignored. For more information about using these templates, see [Understanding Certificate Templates](https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html) .

If conflicting or duplicate certificate information is supplied during certificate issuance, Amazon Web Services Private CA applies [order of operation rules](https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html#template-order-of-operations) to determine what information is used.

Extensions -> (structure)

Specifies X.509 extension information for a certificate.

CertificatePolicies -> (list)

Contains a sequence of one or more policy information terms, each of which consists of an object identifier (OID) and optional qualifiers. For more information, see NISTâs definition of [Object Identifier (OID)](https://csrc.nist.gov/glossary/term/Object_Identifier) .

In an end-entity certificate, these terms indicate the policy under which the certificate was issued and the purposes for which it may be used. In a CA certificate, these terms limit the set of policies for certification paths that include this certificate.

(structure)

Defines the X.509 `CertificatePolicies` extension.

CertPolicyId -> (string)

Specifies the object identifier (OID) of the certificate policy under which the certificate was issued. For more information, see NISTâs definition of [Object Identifier (OID)](https://csrc.nist.gov/glossary/term/Object_Identifier) .

PolicyQualifiers -> (list)

Modifies the given `CertPolicyId` with a qualifier. Amazon Web Services Private CA supports the certification practice statement (CPS) qualifier.

(structure)

Modifies the `CertPolicyId` of a `PolicyInformation` object with a qualifier. Amazon Web Services Private CA supports the certification practice statement (CPS) qualifier.

PolicyQualifierId -> (string)

Identifies the qualifier modifying a `CertPolicyId` .

Qualifier -> (structure)

Defines the qualifier type. Amazon Web Services Private CA supports the use of a URI for a CPS qualifier in this field.

CpsUri -> (string)

Contains a pointer to a certification practice statement (CPS) published by the CA.

ExtendedKeyUsage -> (list)

Specifies additional purposes for which the certified public key may be used other than basic purposes indicated in the `KeyUsage` extension.

(structure)

Specifies additional purposes for which the certified public key may be used other than basic purposes indicated in the `KeyUsage` extension.

ExtendedKeyUsageType -> (string)

Specifies a standard `ExtendedKeyUsage` as defined as in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.12) .

ExtendedKeyUsageObjectIdentifier -> (string)

Specifies a custom `ExtendedKeyUsage` with an object identifier (OID).

KeyUsage -> (structure)

Defines one or more purposes for which the key contained in the certificate can be used. Default value for each option is false.

DigitalSignature -> (boolean)

Key can be used for digital signing.

NonRepudiation -> (boolean)

Key can be used for non-repudiation.

KeyEncipherment -> (boolean)

Key can be used to encipher data.

DataEncipherment -> (boolean)

Key can be used to decipher data.

KeyAgreement -> (boolean)

Key can be used in a key-agreement protocol.

KeyCertSign -> (boolean)

Key can be used to sign certificates.

CRLSign -> (boolean)

Key can be used to sign CRLs.

EncipherOnly -> (boolean)

Key can be used only to encipher data.

DecipherOnly -> (boolean)

Key can be used only to decipher data.

SubjectAlternativeNames -> (list)

The subject alternative name extension allows identities to be bound to the subject of the certificate. These identities may be included in addition to or in place of the identity in the subject field of the certificate.

(structure)

Describes an ASN.1 X.400 `GeneralName` as defined in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280) . Only one of the following naming options should be provided. Providing more than one option results in an `InvalidArgsException` error.

OtherName -> (structure)

Represents `GeneralName` using an `OtherName` object.

TypeId -> (string)

Specifies an OID.

Value -> (string)

Specifies an OID value.

Rfc822Name -> (string)

Represents `GeneralName` as an [RFC 822](https://datatracker.ietf.org/doc/html/rfc822) email address.

DnsName -> (string)

Represents `GeneralName` as a DNS name.

DirectoryName -> (structure)

Contains information about the certificate subject. The `Subject` field in the certificate identifies the entity that owns or controls the public key in the certificate. The entity can be a user, computer, device, or service. The `Subject` must contain an X.500 distinguished name (DN). A DN is a sequence of relative distinguished names (RDNs). The RDNs are separated by commas in the certificate.

Country -> (string)

Two-digit code that specifies the country in which the certificate subject located.

Organization -> (string)

Legal name of the organization with which the certificate subject is affiliated.

OrganizationalUnit -> (string)

A subdivision or unit of the organization (such as sales or finance) with which the certificate subject is affiliated.

DistinguishedNameQualifier -> (string)

Disambiguating information for the certificate subject.

State -> (string)

State in which the subject of the certificate is located.

CommonName -> (string)

For CA and end-entity certificates in a private PKI, the common name (CN) can be any string within the length limit.

Note: In publicly trusted certificates, the common name must be a fully qualified domain name (FQDN) associated with the certificate subject.

SerialNumber -> (string)

The certificate serial number.

Locality -> (string)

The locality (such as a city or town) in which the certificate subject is located.

Title -> (string)

A title such as Mr. or Ms., which is pre-pended to the name to refer formally to the certificate subject.

Surname -> (string)

Family name. In the US and the UK, for example, the surname of an individual is ordered last. In Asian cultures the surname is typically ordered first.

GivenName -> (string)

First name.

Initials -> (string)

Concatenation that typically contains the first letter of the **GivenName** , the first letter of the middle name if one exists, and the first letter of the **Surname** .

Pseudonym -> (string)

Typically a shortened version of a longer **GivenName** . For example, Jonathan is often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.

GenerationQualifier -> (string)

Typically a qualifier appended to the name of an individual. Examples include Jr. for junior, Sr. for senior, and III for third.

CustomAttributes -> (list)

Contains a sequence of one or more X.500 relative distinguished names (RDNs), each of which consists of an object identifier (OID) and a value. For more information, see NISTâs definition of [Object Identifier (OID)](https://csrc.nist.gov/glossary/term/Object_Identifier) .

### Note

Custom attributes cannot be used in combination with standard attributes.

(structure)

Defines the X.500 relative distinguished name (RDN).

ObjectIdentifier -> (string)

Specifies the object identifier (OID) of the attribute type of the relative distinguished name (RDN).

Value -> (string)

Specifies the attribute value of relative distinguished name (RDN).

EdiPartyName -> (structure)

Represents `GeneralName` as an `EdiPartyName` object.

PartyName -> (string)

Specifies the party name.

NameAssigner -> (string)

Specifies the name assigner.

UniformResourceIdentifier -> (string)

Represents `GeneralName` as a URI.

IpAddress -> (string)

Represents `GeneralName` as an IPv4 or IPv6 address.

RegisteredId -> (string)

Represents `GeneralName` as an object identifier (OID).

CustomExtensions -> (list)

Contains a sequence of one or more X.509 extensions, each of which consists of an object identifier (OID), a base64-encoded value, and the critical flag. For more information, see the [Global OID reference database.](https://oidref.com/2.5.29)

(structure)

Specifies the X.509 extension information for a certificate.

Extensions present in `CustomExtensions` follow the `ApiPassthrough` [template rules](https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html#template-order-of-operations) .

ObjectIdentifier -> (string)

Specifies the object identifier (OID) of the X.509 extension. For more information, see the [Global OID reference database.](https://oidref.com/2.5.29)

Value -> (string)

Specifies the base64-encoded value of the X.509 extension.

Critical -> (boolean)

Specifies the critical flag of the X.509 extension.

Subject -> (structure)

Contains information about the certificate subject. The `Subject` field in the certificate identifies the entity that owns or controls the public key in the certificate. The entity can be a user, computer, device, or service. The `Subject` must contain an X.500 distinguished name (DN). A DN is a sequence of relative distinguished names (RDNs). The RDNs are separated by commas in the certificate.

Country -> (string)

Two-digit code that specifies the country in which the certificate subject located.

Organization -> (string)

Legal name of the organization with which the certificate subject is affiliated.

OrganizationalUnit -> (string)

A subdivision or unit of the organization (such as sales or finance) with which the certificate subject is affiliated.

DistinguishedNameQualifier -> (string)

Disambiguating information for the certificate subject.

State -> (string)

State in which the subject of the certificate is located.

CommonName -> (string)

For CA and end-entity certificates in a private PKI, the common name (CN) can be any string within the length limit.

Note: In publicly trusted certificates, the common name must be a fully qualified domain name (FQDN) associated with the certificate subject.

SerialNumber -> (string)

The certificate serial number.

Locality -> (string)

The locality (such as a city or town) in which the certificate subject is located.

Title -> (string)

A title such as Mr. or Ms., which is pre-pended to the name to refer formally to the certificate subject.

Surname -> (string)

Family name. In the US and the UK, for example, the surname of an individual is ordered last. In Asian cultures the surname is typically ordered first.

GivenName -> (string)

First name.

Initials -> (string)

Concatenation that typically contains the first letter of the **GivenName** , the first letter of the middle name if one exists, and the first letter of the **Surname** .

Pseudonym -> (string)

Typically a shortened version of a longer **GivenName** . For example, Jonathan is often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.

GenerationQualifier -> (string)

Typically a qualifier appended to the name of an individual. Examples include Jr. for junior, Sr. for senior, and III for third.

CustomAttributes -> (list)

Contains a sequence of one or more X.500 relative distinguished names (RDNs), each of which consists of an object identifier (OID) and a value. For more information, see NISTâs definition of [Object Identifier (OID)](https://csrc.nist.gov/glossary/term/Object_Identifier) .

### Note

Custom attributes cannot be used in combination with standard attributes.

(structure)

Defines the X.500 relative distinguished name (RDN).

ObjectIdentifier -> (string)

Specifies the object identifier (OID) of the attribute type of the relative distinguished name (RDN).

Value -> (string)

Specifies the attribute value of relative distinguished name (RDN).

JSON Syntax:

```
{
  "Extensions": {
    "CertificatePolicies": [
      {
        "CertPolicyId": "string",
        "PolicyQualifiers": [
          {
            "PolicyQualifierId": "CPS",
            "Qualifier": {
              "CpsUri": "string"
            }
          }
          ...
        ]
      }
      ...
    ],
    "ExtendedKeyUsage": [
      {
        "ExtendedKeyUsageType": "SERVER_AUTH"|"CLIENT_AUTH"|"CODE_SIGNING"|"EMAIL_PROTECTION"|"TIME_STAMPING"|"OCSP_SIGNING"|"SMART_CARD_LOGIN"|"DOCUMENT_SIGNING"|"CERTIFICATE_TRANSPARENCY",
        "ExtendedKeyUsageObjectIdentifier": "string"
      }
      ...
    ],
    "KeyUsage": {
      "DigitalSignature": true|false,
      "NonRepudiation": true|false,
      "KeyEncipherment": true|false,
      "DataEncipherment": true|false,
      "KeyAgreement": true|false,
      "KeyCertSign": true|false,
      "CRLSign": true|false,
      "EncipherOnly": true|false,
      "DecipherOnly": true|false
    },
    "SubjectAlternativeNames": [
      {
        "OtherName": {
          "TypeId": "string",
          "Value": "string"
        },
        "Rfc822Name": "string",
        "DnsName": "string",
        "DirectoryName": {
          "Country": "string",
          "Organization": "string",
          "OrganizationalUnit": "string",
          "DistinguishedNameQualifier": "string",
          "State": "string",
          "CommonName": "string",
          "SerialNumber": "string",
          "Locality": "string",
          "Title": "string",
          "Surname": "string",
          "GivenName": "string",
          "Initials": "string",
          "Pseudonym": "string",
          "GenerationQualifier": "string",
          "CustomAttributes": [
            {
              "ObjectIdentifier": "string",
              "Value": "string"
            }
            ...
          ]
        },
        "EdiPartyName": {
          "PartyName": "string",
          "NameAssigner": "string"
        },
        "UniformResourceIdentifier": "string",
        "IpAddress": "string",
        "RegisteredId": "string"
      }
      ...
    ],
    "CustomExtensions": [
      {
        "ObjectIdentifier": "string",
        "Value": "string",
        "Critical": true|false
      }
      ...
    ]
  },
  "Subject": {
    "Country": "string",
    "Organization": "string",
    "OrganizationalUnit": "string",
    "DistinguishedNameQualifier": "string",
    "State": "string",
    "CommonName": "string",
    "SerialNumber": "string",
    "Locality": "string",
    "Title": "string",
    "Surname": "string",
    "GivenName": "string",
    "Initials": "string",
    "Pseudonym": "string",
    "GenerationQualifier": "string",
    "CustomAttributes": [
      {
        "ObjectIdentifier": "string",
        "Value": "string"
      }
      ...
    ]
  }
}
```

`--certificate-authority-arn` (string)

The Amazon Resource Name (ARN) that was returned when you called [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html) . This must be of the form:

[``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/issue-certificate.html#id1)arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* ``

`--csr` (blob)

The certificate signing request (CSR) for the certificate you want to issue. As an example, you can use the following OpenSSL command to create the CSR and a 2048 bit RSA private key.

`openssl req -new -newkey rsa:2048 -days 365 -keyout private/test_cert_priv_key.pem -out csr/test_cert_.csr`

If you have a configuration file, you can then use the following OpenSSL command. The `usr_cert` block in the configuration file contains your X509 version 3 extensions.

`openssl req -new -config openssl_rsa.cnf -extensions usr_cert -newkey rsa:2048 -days 365 -keyout private/test_cert_priv_key.pem -out csr/test_cert_.csr`

Note: A CSR must provide either a *subject name* or a *subject alternative name* or the request will be rejected.

`--signing-algorithm` (string)

The name of the algorithm that will be used to sign the certificate to be issued.

This parameter should not be confused with the `SigningAlgorithm` parameter used to sign a CSR in the `CreateCertificateAuthority` action.

### Note

The specified signing algorithm family (RSA or ECDSA) must match the algorithm family of the CAâs secret key.

Possible values:

- `SHA256WITHECDSA`
- `SHA384WITHECDSA`
- `SHA512WITHECDSA`
- `SHA256WITHRSA`
- `SHA384WITHRSA`
- `SHA512WITHRSA`
- `SM3WITHSM2`

`--template-arn` (string)

Specifies a custom configuration template to use when issuing a certificate. If this parameter is not provided, Amazon Web Services Private CA defaults to the `EndEntityCertificate/V1` template. For CA certificates, you should choose the shortest path length that meets your needs. The path length is indicated by the PathLen*N* portion of the ARN, where *N* is the [CA depth](https://docs.aws.amazon.com/privateca/latest/userguide/PcaTerms.html#terms-cadepth) .

Note: The CA depth configured on a subordinate CA certificate must not exceed the limit set by its parents in the CA hierarchy.

For a list of `TemplateArn` values supported by Amazon Web Services Private CA, see [Understanding Certificate Templates](https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html) .

`--validity` (structure)

Information describing the end of the validity period of the certificate. This parameter sets the âNot Afterâ date for the certificate.

Certificate validity is the period of time during which a certificate is valid. Validity can be expressed as an explicit date and time when the certificate expires, or as a span of time after issuance, stated in days, months, or years. For more information, see [Validity](https://datatracker.ietf.org/doc/html/rfc5280#section-4.1.2.5) in RFC 5280.

This value is unaffected when `ValidityNotBefore` is also specified. For example, if `Validity` is set to 20 days in the future, the certificate will expire 20 days from issuance time regardless of the `ValidityNotBefore` value.

The end of the validity period configured on a certificate must not exceed the limit set on its parents in the CA hierarchy.

Value -> (long)

A long integer interpreted according to the value of `Type` , below.

Type -> (string)

Determines how *Amazon Web Services Private CA* interprets the `Value` parameter, an integer. Supported validity types include those listed below. Type definitions with values include a sample input value and the resulting output.

`END_DATE` : The specific date and time when the certificate will expire, expressed using UTCTime (YYMMDDHHMMSS) or GeneralizedTime (YYYYMMDDHHMMSS) format. When UTCTime is used, if the year field (YY) is greater than or equal to 50, the year is interpreted as 19YY. If the year field is less than 50, the year is interpreted as 20YY.

- Sample input value: 491231235959 (UTCTime format)
- Output expiration date/time: 12/31/2049 23:59:59

`ABSOLUTE` : The specific date and time when the validity of a certificate will start or expire, expressed in seconds since the Unix Epoch.

- Sample input value: 2524608000
- Output expiration date/time: 01/01/2050 00:00:00

`DAYS` , `MONTHS` , `YEARS` : The relative time from the moment of issuance until the certificate will expire, expressed in days, months, or years.

Example if `DAYS` , issued on 10/12/2020 at 12:34:54 UTC:

- Sample input value: 90
- Output expiration date: 01/10/2020 12:34:54 UTC

The minimum validity duration for a certificate using relative time (`DAYS` ) is one day. The minimum validity for a certificate using absolute time (`ABSOLUTE` or `END_DATE` ) is one second.

Shorthand Syntax:

```
Value=long,Type=string
```

JSON Syntax:

```
{
  "Value": long,
  "Type": "END_DATE"|"ABSOLUTE"|"DAYS"|"MONTHS"|"YEARS"
}
```

`--validity-not-before` (structure)

Information describing the start of the validity period of the certificate. This parameter sets the âNot Beforeâ date for the certificate.

By default, when issuing a certificate, Amazon Web Services Private CA sets the âNot Beforeâ date to the issuance time minus 60 minutes. This compensates for clock inconsistencies across computer systems. The `ValidityNotBefore` parameter can be used to customize the âNot Beforeâ value.

Unlike the `Validity` parameter, the `ValidityNotBefore` parameter is optional.

The `ValidityNotBefore` value is expressed as an explicit date and time, using the `Validity` type value `ABSOLUTE` . For more information, see [Validity](https://docs.aws.amazon.com/privateca/latest/APIReference/API_Validity.html) in this API reference and [Validity](https://datatracker.ietf.org/doc/html/rfc5280#section-4.1.2.5) in RFC 5280.

Value -> (long)

A long integer interpreted according to the value of `Type` , below.

Type -> (string)

Determines how *Amazon Web Services Private CA* interprets the `Value` parameter, an integer. Supported validity types include those listed below. Type definitions with values include a sample input value and the resulting output.

`END_DATE` : The specific date and time when the certificate will expire, expressed using UTCTime (YYMMDDHHMMSS) or GeneralizedTime (YYYYMMDDHHMMSS) format. When UTCTime is used, if the year field (YY) is greater than or equal to 50, the year is interpreted as 19YY. If the year field is less than 50, the year is interpreted as 20YY.

- Sample input value: 491231235959 (UTCTime format)
- Output expiration date/time: 12/31/2049 23:59:59

`ABSOLUTE` : The specific date and time when the validity of a certificate will start or expire, expressed in seconds since the Unix Epoch.

- Sample input value: 2524608000
- Output expiration date/time: 01/01/2050 00:00:00

`DAYS` , `MONTHS` , `YEARS` : The relative time from the moment of issuance until the certificate will expire, expressed in days, months, or years.

Example if `DAYS` , issued on 10/12/2020 at 12:34:54 UTC:

- Sample input value: 90
- Output expiration date: 01/10/2020 12:34:54 UTC

The minimum validity duration for a certificate using relative time (`DAYS` ) is one day. The minimum validity for a certificate using absolute time (`ABSOLUTE` or `END_DATE` ) is one second.

Shorthand Syntax:

```
Value=long,Type=string
```

JSON Syntax:

```
{
  "Value": long,
  "Type": "END_DATE"|"ABSOLUTE"|"DAYS"|"MONTHS"|"YEARS"
}
```

`--idempotency-token` (string)

Alphanumeric string that can be used to distinguish between calls to the **IssueCertificate** action. Idempotency tokens for **IssueCertificate** time out after five minutes. Therefore, if you call **IssueCertificate** multiple times with the same idempotency token within five minutes, Amazon Web Services Private CA recognizes that you are requesting only one certificate and will issue only one. If you change the idempotency token for each call, Amazon Web Services Private CA recognizes that you are requesting multiple certificates.

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

**To issue a private certificate**

The following `issue-certificate` command uses the private CA specified by the ARN to issue a private certificate.

```
aws acm-pca issue-certificate --certificate-authority-arn arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/12345678-1234-1234-1234-123456789012 --csr fileb://C:\cert_1.csr --signing-algorithm "SHA256WITHRSA" --validity Value=365,Type="DAYS" --idempotency-token 1234
```

## Output

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the issued certificate and the certificate serial number. This is of the form:

[``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/issue-certificate.html#id3)arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* /certificate/*286535153982981100925020015808220737245* ``