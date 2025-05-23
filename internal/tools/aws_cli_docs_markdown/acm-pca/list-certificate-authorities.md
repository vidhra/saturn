# list-certificate-authoritiesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/list-certificate-authorities.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/list-certificate-authorities.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [acm-pca](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/index.html#cli-aws-acm-pca) ]

# list-certificate-authorities

## Description

Lists the private certificate authorities that you created by using the [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html) action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/ListCertificateAuthorities)

`list-certificate-authorities` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `CertificateAuthorities`

## Synopsis

```
list-certificate-authorities
[--resource-owner <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--resource-owner` (string)

Use this parameter to filter the returned set of certificate authorities based on their owner. The default is SELF.

Possible values:

- `SELF`
- `OTHER_ACCOUNTS`

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To list your private certificate authorities**

The following `list-certificate-authorities` command lists information about all of the private CAs in your account.

```
aws acm-pca list-certificate-authorities --max-results 10
```

## Output

NextToken -> (string)

When the list is truncated, this value is present and should be used for the `NextToken` parameter in a subsequent pagination request.

CertificateAuthorities -> (list)

Summary information about each certificate authority you have created.

(structure)

Contains information about your private certificate authority (CA). Your private CA can issue and revoke X.509 digital certificates. Digital certificates verify that the entity named in the certificate **Subject** field owns or controls the public key contained in the **Subject Public Key Info** field. Call the [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html) action to create your private CA. You must then call the [GetCertificateAuthorityCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCertificate.html) action to retrieve a private CA certificate signing request (CSR). Sign the CSR with your Amazon Web Services Private CA-hosted or on-premises root or subordinate CA certificate. Call the [ImportCertificateAuthorityCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ImportCertificateAuthorityCertificate.html) action to import the signed certificate into Certificate Manager (ACM).

Arn -> (string)

Amazon Resource Name (ARN) for your private certificate authority (CA). The format is `` *12345678-1234-1234-1234-123456789012* `` .

OwnerAccount -> (string)

The Amazon Web Services account ID that owns the certificate authority.

CreatedAt -> (timestamp)

Date and time at which your private CA was created.

LastStateChangeAt -> (timestamp)

Date and time at which your private CA was last updated.

Type -> (string)

Type of your private CA.

Serial -> (string)

Serial number of your private CA.

Status -> (string)

Status of your private CA.

NotBefore -> (timestamp)

Date and time before which your private CA certificate is not valid.

NotAfter -> (timestamp)

Date and time after which your private CA certificate is not valid.

FailureReason -> (string)

Reason the request to create your private CA failed.

CertificateAuthorityConfiguration -> (structure)

Your private CA configuration.

KeyAlgorithm -> (string)

Type of the public key algorithm and size, in bits, of the key pair that your CA creates when it issues a certificate. When you create a subordinate CA, you must use a key algorithm supported by the parent CA.

SigningAlgorithm -> (string)

Name of the algorithm your private CA uses to sign certificate requests.

This parameter should not be confused with the `SigningAlgorithm` parameter used to sign certificates when they are issued.

Subject -> (structure)

Structure that contains X.500 distinguished name information for your private CA.

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

CsrExtensions -> (structure)

Specifies information to be added to the extension section of the certificate signing request (CSR).

KeyUsage -> (structure)

Indicates the purpose of the certificate and of the key contained in the certificate.

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

SubjectInformationAccess -> (list)

For CA certificates, provides a path to additional information pertaining to the CA, such as revocation and policy. For more information, see [Subject Information Access](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.2.2) in RFC 5280.

(structure)

Provides access information used by the `authorityInfoAccess` and `subjectInfoAccess` extensions described in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280) .

AccessMethod -> (structure)

The type and format of `AccessDescription` information.

CustomObjectIdentifier -> (string)

An object identifier (OID) specifying the `AccessMethod` . The OID must satisfy the regular expression shown below. For more information, see NISTâs definition of [Object Identifier (OID)](https://csrc.nist.gov/glossary/term/Object_Identifier) .

AccessMethodType -> (string)

Specifies the `AccessMethod` .

AccessLocation -> (structure)

The location of `AccessDescription` information.

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

RevocationConfiguration -> (structure)

Information about the Online Certificate Status Protocol (OCSP) configuration or certificate revocation list (CRL) created and maintained by your private CA.

CrlConfiguration -> (structure)

Configuration of the certificate revocation list (CRL), if any, maintained by your private CA. A CRL is typically updated approximately 30 minutes after a certificate is revoked. If for any reason a CRL update fails, Amazon Web Services Private CA makes further attempts every 15 minutes.

Enabled -> (boolean)

Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. You can use this value to enable certificate revocation for a new CA when you call the [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html) action or for an existing CA when you call the [UpdateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html) action.

ExpirationInDays -> (integer)

Validity period of the CRL in days.

CustomCname -> (string)

Name inserted into the certificate **CRL Distribution Points** extension that enables the use of an alias for the CRL distribution point. Use this value if you donât want the name of your S3 bucket to be public.

### Note

The content of a Canonical Name (CNAME) record must conform to [RFC2396](https://www.ietf.org/rfc/rfc2396.txt) restrictions on the use of special characters in URIs. Additionally, the value of the CNAME must not include a protocol prefix such as â[http://](http://)â or â[https://](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/list-certificate-authorities.html)â.

S3BucketName -> (string)

Name of the S3 bucket that contains the CRL. If you do not provide a value for the **CustomCname** argument, the name of your S3 bucket is placed into the **CRL Distribution Points** extension of the issued certificate. You can change the name of your bucket by calling the [UpdateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html) operation. You must specify a [bucket policy](https://docs.aws.amazon.com/privateca/latest/userguide/PcaCreateCa.html#s3-policies) that allows Amazon Web Services Private CA to write the CRL to your bucket.

### Note

The `S3BucketName` parameter must conform to the [S3 bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html) .

S3ObjectAcl -> (string)

Determines whether the CRL will be publicly readable or privately held in the CRL Amazon S3 bucket. If you choose PUBLIC_READ, the CRL will be accessible over the public internet. If you choose BUCKET_OWNER_FULL_CONTROL, only the owner of the CRL S3 bucket can access the CRL, and your PKI clients may need an alternative method of access.

If no value is specified, the default is `PUBLIC_READ` .

*Note:* This default can cause CA creation to fail in some circumstances. If you have have enabled the Block Public Access (BPA) feature in your S3 account, then you must specify the value of this parameter as `BUCKET_OWNER_FULL_CONTROL` , and not doing so results in an error. If you have disabled BPA in S3, then you can specify either `BUCKET_OWNER_FULL_CONTROL` or `PUBLIC_READ` as the value.

For more information, see [Blocking public access to the S3 bucket](https://docs.aws.amazon.com/privateca/latest/userguide/PcaCreateCa.html#s3-bpa) .

CrlDistributionPointExtensionConfiguration -> (structure)

Configures the behavior of the CRL Distribution Point extension for certificates issued by your certificate authority. If this field is not provided, then the CRl Distribution Point Extension will be present and contain the default CRL URL.

OmitExtension -> (boolean)

Configures whether the CRL Distribution Point extension should be populated with the default URL to the CRL. If set to `true` , then the CDP extension will not be present in any certificates issued by that CA unless otherwise specified through CSR or API passthrough.

### Note

Only set this if you have another way to distribute the CRL Distribution Points ffor certificates issued by your CA, such as the Matter Distributed Compliance Ledger

This configuration cannot be enabled with a custom CNAME set.

CrlType -> (string)

Specifies whether to create a complete or partitioned CRL. This setting determines the maximum number of certificates that the certificate authority can issue and revoke. For more information, see [Amazon Web Services Private CA quotas](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/privateca/latest/userguide/pca.html#limits_pca) .

- `COMPLETE` - The default setting. Amazon Web Services Private CA maintains a single CRL ï¬le for all unexpired certiï¬cates issued by a CA that have been revoked for any reason. Each certiï¬cate that Amazon Web Services Private CA issues is bound to a speciï¬c CRL through its CRL distribution point (CDP) extension, deï¬ned in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.9) .
- `PARTITIONED` - Compared to complete CRLs, partitioned CRLs dramatically increase the number of certiï¬cates your private CA can issue.

### Warning

When using partitioned CRLs, you must validate that the CRLâs associated issuing distribution point (IDP) URI matches the certiï¬cateâs CDP URI to ensure the right CRL has been fetched. Amazon Web Services Private CA marks the IDP extension as critical, which your client must be able to process.

CustomPath -> (string)

Designates a custom ï¬le path in S3 for CRL(s). For example, `http://<CustomName>/ <CustomPath>/<CrlPartition_GUID>.crl` .

OcspConfiguration -> (structure)

Configuration of Online Certificate Status Protocol (OCSP) support, if any, maintained by your private CA. When you revoke a certificate, OCSP responses may take up to 60 minutes to reflect the new status.

Enabled -> (boolean)

Flag enabling use of the Online Certificate Status Protocol (OCSP) for validating certificate revocation status.

OcspCustomCname -> (string)

By default, Amazon Web Services Private CA injects an Amazon Web Services domain into certificates being validated by the Online Certificate Status Protocol (OCSP). A customer can alternatively use this object to define a CNAME specifying a customized OCSP domain.

### Note

The content of a Canonical Name (CNAME) record must conform to [RFC2396](https://www.ietf.org/rfc/rfc2396.txt) restrictions on the use of special characters in URIs. Additionally, the value of the CNAME must not include a protocol prefix such as â[http://](http://)â or â[https://](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/list-certificate-authorities.html)â.

For more information, see [Customizing Online Certificate Status Protocol (OCSP)](https://docs.aws.amazon.com/privateca/latest/userguide/ocsp-customize.html) in the *Amazon Web Services Private Certificate Authority User Guide* .

RestorableUntil -> (timestamp)

The period during which a deleted CA can be restored. For more information, see the `PermanentDeletionTimeInDays` parameter of the [DeleteCertificateAuthorityRequest](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeleteCertificateAuthorityRequest.html) action.

KeyStorageSecurityStandard -> (string)

Defines a cryptographic key management compliance standard used for handling CA keys.

Default: FIPS_140_2_LEVEL_3_OR_HIGHER

Note: Amazon Web Services Region ap-northeast-3 supports only FIPS_140_2_LEVEL_2_OR_HIGHER. You must explicitly specify this parameter and value when creating a CA in that Region. Specifying a different value (or no value) results in an `InvalidArgsException` with the message âA certificate authority cannot be created in this region with the specified security standard.â

UsageMode -> (string)

Specifies whether the CA issues general-purpose certificates that typically require a revocation mechanism, or short-lived certificates that may optionally omit revocation because they expire quickly. Short-lived certificate validity is limited to seven days.

The default value is GENERAL_PURPOSE.