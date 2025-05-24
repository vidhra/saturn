# get-load-balancer-tls-certificatesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lightsail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html#cli-aws-lightsail) ]

# get-load-balancer-tls-certificates

## Description

Returns information about the TLS certificates that are associated with the specified Lightsail load balancer.

TLS is just an updated, more secure version of Secure Socket Layer (SSL).

You can have a maximum of 2 certificates associated with a Lightsail load balancer. One is active and the other is inactive.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetLoadBalancerTlsCertificates)

## Synopsis

```
get-load-balancer-tls-certificates
--load-balancer-name <value>
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

`--load-balancer-name` (string)

The name of the load balancer you associated with your SSL/TLS certificate.

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

**To get information about TLS certificates for a load balancer**

The following `get-load-balancer-tls-certificates` example displays details about the TLS certificates for the specified load balancer.

```
aws lightsail get-load-balancer-tls-certificates \
    --load-balancer-name LoadBalancer-1
```

Output:

```
{
    "tlsCertificates": [
        {
            "name": "example-com",
            "arn": "arn:aws:lightsail:us-west-2:111122223333:LoadBalancerTlsCertificate/d7bf4643-6a02-4cd4-b3c4-fEXAMPLE9b4d",
            "supportCode": "6EXAMPLE3362/arn:aws:acm:us-west-2:333322221111:certificate/9af8e32c-a54e-4a67-8c63-cEXAMPLEb314",
            "createdAt": 1571678025.3,
            "location": {
                "availabilityZone": "all",
                "regionName": "us-west-2"
            },
            "resourceType": "LoadBalancerTlsCertificate",
            "loadBalancerName": "LoadBalancer-1",
            "isAttached": false,
            "status": "ISSUED",
            "domainName": "example.com",
            "domainValidationRecords": [
                {
                    "name": "_dEXAMPLE4ede046a0319eb44a4eb3cbc.example.com.",
                    "type": "CNAME",
                    "value": "_bEXAMPLE0899fb7b6bf79d9741d1a383.hkvuiqjoua.acm-validations.aws.",
                    "validationStatus": "SUCCESS",
                    "domainName": "example.com"
                }
            ],
            "issuedAt": 1571678070.0,
            "issuer": "Amazon",
            "keyAlgorithm": "RSA-2048",
            "notAfter": 1605960000.0,
            "notBefore": 1571616000.0,
            "serial": "00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd:ee:ff",
            "signatureAlgorithm": "SHA256WITHRSA",
            "subject": "CN=example.com",
            "subjectAlternativeNames": [
                "example.com"
            ]
        }
    ]
}
```

## Output

tlsCertificates -> (list)

An array of LoadBalancerTlsCertificate objects describing your SSL/TLS certificates.

(structure)

Describes a load balancer SSL/TLS certificate.

TLS is just an updated, more secure version of Secure Socket Layer (SSL).

name -> (string)

The name of the SSL/TLS certificate (`my-certificate` ).

arn -> (string)

The Amazon Resource Name (ARN) of the SSL/TLS certificate.

supportCode -> (string)

The support code. Include this code in your email to support when you have questions about your Lightsail load balancer or SSL/TLS certificate. This code enables our support team to look up your Lightsail information more easily.

createdAt -> (timestamp)

The time when you created your SSL/TLS certificate.

location -> (structure)

The Amazon Web Services Region and Availability Zone where you created your certificate.

availabilityZone -> (string)

The Availability Zone. Follows the format `us-east-2a` (case-sensitive).

regionName -> (string)

The Amazon Web Services Region name.

resourceType -> (string)

The resource type (`LoadBalancerTlsCertificate` ).

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html#id1)`Instance` ** - A Lightsail instance (a virtual private server)
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html#id3)`StaticIp` ** - A static IP address
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html#id5)`KeyPair` ** - The key pair used to connect to a Lightsail instance
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html#id7)`InstanceSnapshot` ** - A Lightsail instance snapshot
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html#id9)`Domain` ** - A DNS zone
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html#id11)`PeeredVpc` ** - A peered VPC
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html#id13)`LoadBalancer` ** - A Lightsail load balancer
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html#id15)`LoadBalancerTlsCertificate` ** - An SSL/TLS certificate associated with a Lightsail load balancer
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html#id17)`Disk` ** - A Lightsail block storage disk
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html#id19)`DiskSnapshot` ** - A block storage disk snapshot

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

loadBalancerName -> (string)

The load balancer name where your SSL/TLS certificate is attached.

isAttached -> (boolean)

When `true` , the SSL/TLS certificate is attached to the Lightsail load balancer.

status -> (string)

The validation status of the SSL/TLS certificate. Valid values are below.

domainName -> (string)

The domain name for your SSL/TLS certificate.

domainValidationRecords -> (list)

An array of LoadBalancerTlsCertificateDomainValidationRecord objects describing the records.

(structure)

Describes the validation record of each domain name in the SSL/TLS certificate.

name -> (string)

A fully qualified domain name in the certificate. For example, `example.com` .

type -> (string)

The type of validation record. For example, `CNAME` for domain validation.

value -> (string)

The value for that type.

validationStatus -> (string)

The validation status. Valid values are listed below.

domainName -> (string)

The domain name against which your SSL/TLS certificate was validated.

dnsRecordCreationState -> (structure)

An object that describes the state of the canonical name (CNAME) records that are automatically added by Lightsail to the DNS of a domain to validate domain ownership.

code -> (string)

The status code for the automated DNS record creation.

Following are the possible values:

- `SUCCEEDED` - The validation records were successfully added.
- `STARTED` - The automatic DNS record creation has started.
- `FAILED` - The validation record addition failed.

message -> (string)

The message that describes the reason for the status code.

failureReason -> (string)

The validation failure reason, if any, of the certificate.

The following failure reasons are possible:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html#id21)`NO_AVAILABLE_CONTACTS` ** - This failure applies to email validation, which is not available for Lightsail certificates.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html#id23)`ADDITIONAL_VERIFICATION_REQUIRED` ** - Lightsail requires additional information to process this certificate request. This can happen as a fraud-protection measure, such as when the domain ranks within the Alexa top 1000 websites. To provide the required information, use the [AWS Support Center](https://console.aws.amazon.com/support/home) to contact AWS Support.

### Note

You cannot request a certificate for Amazon-owned domain names such as those ending in amazonaws.com, cloudfront.net, or elasticbeanstalk.com.

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html#id25)`DOMAIN_NOT_ALLOWED` ** - One or more of the domain names in the certificate request was reported as an unsafe domain by [VirusTotal](https://www.virustotal.com/gui/home/url) . To correct the problem, search for your domain name on the [VirusTotal](https://www.virustotal.com/gui/home/url) website. If your domain is reported as suspicious, see [Google Help for Hacked Websites](https://developers.google.com/web/fundamentals/security/hacked) to learn what you can do. If you believe that the result is a false positive, notify the organization that is reporting the domain. VirusTotal is an aggregate of several antivirus and URL scanners and cannot remove your domain from a block list itself. After you correct the problem and the VirusTotal registry has been updated, request a new certificate. If you see this error and your domain is not included in the VirusTotal list, visit the [AWS Support Center](https://console.aws.amazon.com/support/home) and create a case.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html#id27)`INVALID_PUBLIC_DOMAIN` ** - One or more of the domain names in the certificate request is not valid. Typically, this is because a domain name in the request is not a valid top-level domain. Try to request a certificate again, correcting any spelling errors or typos that were in the failed request, and ensure that all domain names in the request are for valid top-level domains. For example, you cannot request a certificate for `example.invalidpublicdomain` because `invalidpublicdomain` is not a valid top-level domain.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html#id29)`OTHER` ** - Typically, this failure occurs when there is a typographical error in one or more of the domain names in the certificate request. Try to request a certificate again, correcting any spelling errors or typos that were in the failed request.

issuedAt -> (timestamp)

The time when the SSL/TLS certificate was issued.

issuer -> (string)

The issuer of the certificate.

keyAlgorithm -> (string)

The algorithm used to generate the key pair (the public and private key).

notAfter -> (timestamp)

The timestamp when the SSL/TLS certificate expires.

notBefore -> (timestamp)

The timestamp when the SSL/TLS certificate is first valid.

renewalSummary -> (structure)

An object that describes the status of the certificate renewal managed by Lightsail.

renewalStatus -> (string)

The renewal status of the certificate.

The following renewal status are possible:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html#id31)`PendingAutoRenewal` ** - Lightsail is attempting to automatically validate the domain names of the certificate. No further action is required.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html#id33)`PendingValidation` ** - Lightsail couldnât automatically validate one or more domain names of the certificate. You must take action to validate these domain names or the certificate wonât be renewed. Check to make sure your certificateâs domain validation records exist in your domainâs DNS, and that your certificate remains in use.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html#id35)`Success` ** - All domain names in the certificate are validated, and Lightsail renewed the certificate. No further action is required.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html#id37)`Failed` ** - One or more domain names were not validated before the certificate expired, and Lightsail did not renew the certificate. You can request a new certificate using the `CreateCertificate` action.

domainValidationOptions -> (list)

Contains information about the validation of each domain name in the certificate, as it pertains to Lightsailâs managed renewal. This is different from the initial validation that occurs as a result of the RequestCertificate request.

(structure)

Contains information about the domain names on an SSL/TLS certificate that you will use to validate domain ownership.

domainName -> (string)

The fully qualified domain name in the certificate request.

validationStatus -> (string)

The status of the domain validation. Valid values are listed below.

revocationReason -> (string)

The reason the certificate was revoked. This value is present only when the certificate status is `REVOKED` .

revokedAt -> (timestamp)

The timestamp when the certificate was revoked. This value is present only when the certificate status is `REVOKED` .

serial -> (string)

The serial number of the certificate.

signatureAlgorithm -> (string)

The algorithm that was used to sign the certificate.

subject -> (string)

The name of the entity that is associated with the public key contained in the certificate.

subjectAlternativeNames -> (list)

An array of strings that specify the alternate domains (`example2.com` ) and subdomains (`blog.example.com` ) for the certificate.

(string)