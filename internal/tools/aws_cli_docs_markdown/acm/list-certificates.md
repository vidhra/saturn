# list-certificatesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/list-certificates.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/list-certificates.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [acm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/index.html#cli-aws-acm) ]

# list-certificates

## Description

Retrieves a list of certificate ARNs and domain names. You can request that only certificates that match a specific status be listed. You can also filter by specific attributes of the certificate. Default filtering returns only `RSA_2048` certificates. For more information, see  Filters .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/ListCertificates)

`list-certificates` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `CertificateSummaryList`

## Synopsis

```
list-certificates
[--certificate-statuses <value>]
[--includes <value>]
[--max-items <value>]
[--sort-by <value>]
[--sort-order <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
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

`--certificate-statuses` (list)

Filter the certificate list by status value.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  PENDING_VALIDATION
  ISSUED
  INACTIVE
  EXPIRED
  VALIDATION_TIMED_OUT
  REVOKED
  FAILED
```

`--includes` (structure)

Filter the certificate list. For more information, see the  Filters structure.

extendedKeyUsage -> (list)

Specify one or more  ExtendedKeyUsage extension values.

(string)

keyUsage -> (list)

Specify one or more  KeyUsage extension values.

(string)

keyTypes -> (list)

Specify one or more algorithms that can be used to generate key pairs.

Default filtering returns only `RSA_1024` and `RSA_2048` certificates that have at least one domain. To return other certificate types, provide the desired type signatures in a comma-separated list. For example, `"keyTypes": ["RSA_2048","RSA_4096"]` returns both `RSA_2048` and `RSA_4096` certificates.

(string)

managedBy -> (string)

Identifies the Amazon Web Services service that manages the certificate issued by ACM.

Shorthand Syntax:

```
extendedKeyUsage=string,string,keyUsage=string,string,keyTypes=string,string,managedBy=string
```

JSON Syntax:

```
{
  "extendedKeyUsage": ["TLS_WEB_SERVER_AUTHENTICATION"|"TLS_WEB_CLIENT_AUTHENTICATION"|"CODE_SIGNING"|"EMAIL_PROTECTION"|"TIME_STAMPING"|"OCSP_SIGNING"|"IPSEC_END_SYSTEM"|"IPSEC_TUNNEL"|"IPSEC_USER"|"ANY"|"NONE"|"CUSTOM", ...],
  "keyUsage": ["DIGITAL_SIGNATURE"|"NON_REPUDIATION"|"KEY_ENCIPHERMENT"|"DATA_ENCIPHERMENT"|"KEY_AGREEMENT"|"CERTIFICATE_SIGNING"|"CRL_SIGNING"|"ENCIPHER_ONLY"|"DECIPHER_ONLY"|"ANY"|"CUSTOM", ...],
  "keyTypes": ["RSA_1024"|"RSA_2048"|"RSA_3072"|"RSA_4096"|"EC_prime256v1"|"EC_secp384r1"|"EC_secp521r1", ...],
  "managedBy": "CLOUDFRONT"
}
```

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--sort-by` (string)

Specifies the field to sort results by. If you specify `SortBy` , you must also specify `SortOrder` .

Possible values:

- `CREATED_AT`

`--sort-order` (string)

Specifies the order of sorted results. If you specify `SortOrder` , you must also specify `SortBy` .

Possible values:

- `ASCENDING`
- `DESCENDING`

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

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

**To list the ACM certificates for an AWS account**

The following `list-certificates` command lists the ARNs of the certificates in your account:

```
aws acm list-certificates
```

The preceding command produces output similar to the following:

```
{
    "CertificateSummaryList": [
        {
            "CertificateArn": "arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012",
            "DomainName": "www.example.com"
        },
        {
            "CertificateArn": "arn:aws:acm:region:account:certificate/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            "DomainName": "www.example.net"
        }
    ]
}
```

You can decide how many certificates you want to display each time you call `list-certificates`. For example, if you have four certificates and you want to display no more than two at a time, set the `max-items` argument to 2 as in the following example:

```
aws acm list-certificates --max-items 2
```

Two certificate ARNs and a `NextToken` value will be displayed:

```
"CertificateSummaryList": [
  {
    "CertificateArn": "arn:aws:acm:region:account: \
            certificate/12345678-1234-1234-1234-123456789012",
    "DomainName": "www.example.com"
  },
  {
    "CertificateArn": "arn:aws:acm:region:account: \
             certificate/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "DomainName": "www.example.net"
  }
  ],
    "NextToken": "9f4d9f69-275a-41fe-b58e-2b837bd9ba48"
```

To display the next two certificates in your account, set this `NextToken` value in your next call:

```
aws acm list-certificates --max-items 2 --next-token 9f4d9f69-275a-41fe-b58e-2b837bd9ba48
```

You can filter your output by using the `certificate-statuses` argument. The following command displays certificates that have a PENDING_VALIDATION status:

```
aws acm list-certificates --certificate-statuses PENDING_VALIDATION
```

You can also filter your output by using the `includes` argument. The following command displays certificates filtered on the following properties. The certificates to be displayed:

```
- Specify that the RSA algorithm and a 2048 bit key are used to generate key pairs.
- Contain a Key Usage extension that specifies that the certificates can be used to create digital signatures.
- Contain an Extended Key Usage extension that specifies that the certificates can be used for code signing.

aws acm list-certificates --max-items 10 --includes extendedKeyUsage=CODE_SIGNING,keyUsage=DIGITAL_SIGNATURE,keyTypes=RSA_2048
```

## Output

NextToken -> (string)

When the list is truncated, this value is present and contains the value to use for the `NextToken` parameter in a subsequent pagination request.

CertificateSummaryList -> (list)

A list of ACM certificates.

(structure)

This structure is returned in the response object of  ListCertificates action.

CertificateArn -> (string)

Amazon Resource Name (ARN) of the certificate. This is of the form:

`arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012`

For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

DomainName -> (string)

Fully qualified domain name (FQDN), such as www.example.com or example.com, for the certificate.

SubjectAlternativeNameSummaries -> (list)

One or more domain names (subject alternative names) included in the certificate. This list contains the domain names that are bound to the public key that is contained in the certificate. The subject alternative names include the canonical domain name (CN) of the certificate and additional domain names that can be used to connect to the website.

When called by [ListCertificates](https://docs.aws.amazon.com/acm/latestAPIReference/API_ListCertificates.html) , this parameter will only return the first 100 subject alternative names included in the certificate. To display the full list of subject alternative names, use [DescribeCertificate](https://docs.aws.amazon.com/acm/latestAPIReference/API_DescribeCertificate.html) .

(string)

HasAdditionalSubjectAlternativeNames -> (boolean)

When called by [ListCertificates](https://docs.aws.amazon.com/acm/latestAPIReference/API_ListCertificates.html) , indicates whether the full list of subject alternative names has been included in the response. If false, the response includes all of the subject alternative names included in the certificate. If true, the response only includes the first 100 subject alternative names included in the certificate. To display the full list of subject alternative names, use [DescribeCertificate](https://docs.aws.amazon.com/acm/latestAPIReference/API_DescribeCertificate.html) .

Status -> (string)

The status of the certificate.

A certificate enters status PENDING_VALIDATION upon being requested, unless it fails for any of the reasons given in the troubleshooting topic [Certificate request fails](https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting-failed.html) . ACM makes repeated attempts to validate a certificate for 72 hours and then times out. If a certificate shows status FAILED or VALIDATION_TIMED_OUT, delete the request, correct the issue with [DNS validation](https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html) or [Email validation](https://docs.aws.amazon.com/acm/latest/userguide/email-validation.html) , and try again. If validation succeeds, the certificate enters status ISSUED.

Type -> (string)

The source of the certificate. For certificates provided by ACM, this value is `AMAZON_ISSUED` . For certificates that you imported with  ImportCertificate , this value is `IMPORTED` . ACM does not provide [managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html) for imported certificates. For more information about the differences between certificates that you import and those that ACM provides, see [Importing Certificates](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the *Certificate Manager User Guide* .

KeyAlgorithm -> (string)

The algorithm that was used to generate the public-private key pair.

KeyUsages -> (list)

A list of Key Usage X.509 v3 extension objects. Each object is a string value that identifies the purpose of the public key contained in the certificate. Possible extension values include DIGITAL_SIGNATURE, KEY_ENCHIPHERMENT, NON_REPUDIATION, and more.

(string)

ExtendedKeyUsages -> (list)

Contains a list of Extended Key Usage X.509 v3 extension objects. Each object specifies a purpose for which the certificate public key can be used and consists of a name and an object identifier (OID).

(string)

InUse -> (boolean)

Indicates whether the certificate is currently in use by any Amazon Web Services resources.

Exported -> (boolean)

Indicates whether the certificate has been exported. This value exists only when the certificate type is `PRIVATE` .

RenewalEligibility -> (string)

Specifies whether the certificate is eligible for renewal. At this time, only exported private certificates can be renewed with the  RenewCertificate command.

NotBefore -> (timestamp)

The time before which the certificate is not valid.

NotAfter -> (timestamp)

The time after which the certificate is not valid.

CreatedAt -> (timestamp)

The time at which the certificate was requested.

IssuedAt -> (timestamp)

The time at which the certificate was issued. This value exists only when the certificate type is `AMAZON_ISSUED` .

ImportedAt -> (timestamp)

The date and time when the certificate was imported. This value exists only when the certificate type is `IMPORTED` .

RevokedAt -> (timestamp)

The time at which the certificate was revoked. This value exists only when the certificate status is `REVOKED` .

ManagedBy -> (string)

Identifies the Amazon Web Services service that manages the certificate issued by ACM.