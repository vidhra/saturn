# get-certificatesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-certificates.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-certificates.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lightsail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html#cli-aws-lightsail) ]

# get-certificates

## Description

Returns information about one or more Amazon Lightsail SSL/TLS certificates.

### Note

To get a summary of a certificate, omit `includeCertificateDetails` from your request. The response will include only the certificate Amazon Resource Name (ARN), certificate name, domain name, and tags.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetCertificates)

## Synopsis

```
get-certificates
[--certificate-statuses <value>]
[--include-certificate-details | --no-include-certificate-details]
[--certificate-name <value>]
[--page-token <value>]
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

`--certificate-statuses` (list)

The status of the certificates for which to return information.

For example, specify `ISSUED` to return only certificates with an `ISSUED` status.

When omitted, the response includes all of your certificates in the Amazon Web Services Region where the request is made, regardless of their current status.

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

`--include-certificate-details` | `--no-include-certificate-details` (boolean)

Indicates whether to include detailed information about the certificates in the response.

When omitted, the response includes only the certificate names, Amazon Resource Names (ARNs), domain names, and tags.

`--certificate-name` (string)

The name for the certificate for which to return information.

When omitted, the response includes all of your certificates in the Amazon Web Services Region where the request is made.

`--page-token` (string)

The token to advance to the next page of results from your request.

To get a page token, perform an initial `GetCertificates` request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.

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

certificates -> (list)

An object that describes certificates.

(structure)

Describes an Amazon Lightsail SSL/TLS certificate.

certificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate.

certificateName -> (string)

The name of the certificate.

domainName -> (string)

The domain name of the certificate.

certificateDetail -> (structure)

An object that describes a certificate in detail.

arn -> (string)

The Amazon Resource Name (ARN) of the certificate.

name -> (string)

The name of the certificate (`my-certificate` ).

domainName -> (string)

The domain name of the certificate.

status -> (string)

The validation status of the certificate.

serialNumber -> (string)

The serial number of the certificate.

subjectAlternativeNames -> (list)

An array of strings that specify the alternate domains (`example2.com` ) and subdomains (`blog.example.com` ) of the certificate.

(string)

domainValidationRecords -> (list)

An array of objects that describe the domain validation records of the certificate.

(structure)

Describes the domain name system (DNS) records that you must add to the DNS of your registered domain to validate ownership for an Amazon Lightsail SSL/TLS certificate.

domainName -> (string)

The domain name of the certificate validation record. For example, `example.com` or `www.example.com` .

resourceRecord -> (structure)

An object that describes the DNS records to add to your domainâs DNS to validate it for the certificate.

name -> (string)

The name of the record.

type -> (string)

The DNS record type.

value -> (string)

The value for the DNS record.

dnsRecordCreationState -> (structure)

An object that describes the state of the canonical name (CNAME) records that are automatically added by Lightsail to the DNS of the domain to validate domain ownership.

code -> (string)

The status code for the automated DNS record creation.

Following are the possible values:

- `SUCCEEDED` - The validation records were successfully added to the domain.
- `STARTED` - The automatic DNS record creation has started.
- `FAILED` - The validation records failed to be added to the domain.

message -> (string)

The message that describes the reason for the status code.

validationStatus -> (string)

The validation status of the record.

requestFailureReason -> (string)

The validation failure reason, if any, of the certificate.

The following failure reasons are possible:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-certificates.html#id1)`NO_AVAILABLE_CONTACTS` ** - This failure applies to email validation, which is not available for Lightsail certificates.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-certificates.html#id3)`ADDITIONAL_VERIFICATION_REQUIRED` ** - Lightsail requires additional information to process this certificate request. This can happen as a fraud-protection measure, such as when the domain ranks within the Alexa top 1000 websites. To provide the required information, use the [Amazon Web Services Support Center](https://console.aws.amazon.com/support/home) to contact Amazon Web Services Support.

### Note

You cannot request a certificate for Amazon-owned domain names such as those ending in amazonaws.com, cloudfront.net, or elasticbeanstalk.com.

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-certificates.html#id5)`DOMAIN_NOT_ALLOWED` ** - One or more of the domain names in the certificate request was reported as an unsafe domain by [VirusTotal](https://www.virustotal.com/gui/home/url) . To correct the problem, search for your domain name on the [VirusTotal](https://www.virustotal.com/gui/home/url) website. If your domain is reported as suspicious, see [Google Help for Hacked Websites](https://developers.google.com/web/fundamentals/security/hacked) to learn what you can do. If you believe that the result is a false positive, notify the organization that is reporting the domain. VirusTotal is an aggregate of several antivirus and URL scanners and cannot remove your domain from a block list itself. After you correct the problem and the VirusTotal registry has been updated, request a new certificate. If you see this error and your domain is not included in the VirusTotal list, visit the [Amazon Web Services Support Center](https://console.aws.amazon.com/support/home) and create a case.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-certificates.html#id7)`INVALID_PUBLIC_DOMAIN` ** - One or more of the domain names in the certificate request is not valid. Typically, this is because a domain name in the request is not a valid top-level domain. Try to request a certificate again, correcting any spelling errors or typos that were in the failed request, and ensure that all domain names in the request are for valid top-level domains. For example, you cannot request a certificate for `example.invalidpublicdomain` because `invalidpublicdomain` is not a valid top-level domain.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-certificates.html#id9)`OTHER` ** - Typically, this failure occurs when there is a typographical error in one or more of the domain names in the certificate request. Try to request a certificate again, correcting any spelling errors or typos that were in the failed request.

inUseResourceCount -> (integer)

The number of Lightsail resources that the certificate is attached to.

keyAlgorithm -> (string)

The algorithm used to generate the key pair (the public and private key) of the certificate.

createdAt -> (timestamp)

The timestamp when the certificate was created.

issuedAt -> (timestamp)

The timestamp when the certificate was issued.

issuerCA -> (string)

The certificate authority that issued the certificate.

notBefore -> (timestamp)

The timestamp when the certificate is first valid.

notAfter -> (timestamp)

The timestamp when the certificate expires.

eligibleToRenew -> (string)

The renewal eligibility of the certificate.

renewalSummary -> (structure)

An object that describes the status of the certificate renewal managed by Lightsail.

domainValidationRecords -> (list)

An array of objects that describe the domain validation records of the certificate.

(structure)

Describes the domain name system (DNS) records that you must add to the DNS of your registered domain to validate ownership for an Amazon Lightsail SSL/TLS certificate.

domainName -> (string)

The domain name of the certificate validation record. For example, `example.com` or `www.example.com` .

resourceRecord -> (structure)

An object that describes the DNS records to add to your domainâs DNS to validate it for the certificate.

name -> (string)

The name of the record.

type -> (string)

The DNS record type.

value -> (string)

The value for the DNS record.

dnsRecordCreationState -> (structure)

An object that describes the state of the canonical name (CNAME) records that are automatically added by Lightsail to the DNS of the domain to validate domain ownership.

code -> (string)

The status code for the automated DNS record creation.

Following are the possible values:

- `SUCCEEDED` - The validation records were successfully added to the domain.
- `STARTED` - The automatic DNS record creation has started.
- `FAILED` - The validation records failed to be added to the domain.

message -> (string)

The message that describes the reason for the status code.

validationStatus -> (string)

The validation status of the record.

renewalStatus -> (string)

The renewal status of the certificate.

The following renewal status are possible:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-certificates.html#id11)`PendingAutoRenewal` ** - Lightsail is attempting to automatically validate the domain names of the certificate. No further action is required.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-certificates.html#id13)`PendingValidation` ** - Lightsail couldnât automatically validate one or more domain names of the certificate. You must take action to validate these domain names or the certificate wonât be renewed. Check to make sure your certificateâs domain validation records exist in your domainâs DNS, and that your certificate remains in use.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-certificates.html#id15)`Success` ** - All domain names in the certificate are validated, and Lightsail renewed the certificate. No further action is required.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-certificates.html#id17)`Failed` ** - One or more domain names were not validated before the certificate expired, and Lightsail did not renew the certificate. You can request a new certificate using the `CreateCertificate` action.

renewalStatusReason -> (string)

The reason for the renewal status of the certificate.

updatedAt -> (timestamp)

The timestamp when the certificate was last updated.

revokedAt -> (timestamp)

The timestamp when the certificate was revoked. This value is present only when the certificate status is `REVOKED` .

revocationReason -> (string)

The reason the certificate was revoked. This value is present only when the certificate status is `REVOKED` .

tags -> (list)

The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

(structure)

Describes a tag key and optional value assigned to an Amazon Lightsail resource.

For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

key -> (string)

The key of the tag.

Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value -> (string)

The value of the tag.

Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

supportCode -> (string)

The support code. Include this code in your email to support when you have questions about your Lightsail certificate. This code enables our support team to look up your Lightsail information more easily.

tags -> (list)

The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

(structure)

Describes a tag key and optional value assigned to an Amazon Lightsail resource.

For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

key -> (string)

The key of the tag.

Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value -> (string)

The value of the tag.

Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

nextPageToken -> (string)

If `NextPageToken` is returned there are more results available. The value of `NextPageToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.