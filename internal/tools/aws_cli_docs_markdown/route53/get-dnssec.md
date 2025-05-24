# get-dnssecÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-dnssec.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-dnssec.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html#cli-aws-route53) ]

# get-dnssec

## Description

Returns information about DNSSEC for a specific hosted zone, including the key-signing keys (KSKs) in the hosted zone.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetDNSSEC)

## Synopsis

```
get-dnssec
--hosted-zone-id <value>
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

`--hosted-zone-id` (string)

A unique string used to identify a hosted zone.

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

Status -> (structure)

A string representing the status of DNSSEC.

ServeSignature -> (string)

A string that represents the current hosted zone signing status.

Status can have one of the following values:

SIGNING

DNSSEC signing is enabled for the hosted zone.

NOT_SIGNING

DNSSEC signing is not enabled for the hosted zone.

DELETING

DNSSEC signing is in the process of being removed for the hosted zone.

ACTION_NEEDED

There is a problem with signing in the hosted zone that requires you to take action to resolve. For example, the customer managed key might have been deleted, or the permissions for the customer managed key might have been changed.

INTERNAL_FAILURE

There was an error during a request. Before you can continue to work with DNSSEC signing, including with key-signing keys (KSKs), you must correct the problem by enabling or disabling DNSSEC signing for the hosted zone.

StatusMessage -> (string)

The status message provided for the following DNSSEC signing status: `INTERNAL_FAILURE` . The status message includes information about what the problem might be and steps that you can take to correct the issue.

KeySigningKeys -> (list)

The key-signing keys (KSKs) in your account.

(structure)

A key-signing key (KSK) is a complex type that represents a public/private key pair. The private key is used to generate a digital signature for the zone signing key (ZSK). The public key is stored in the DNS and is used to authenticate the ZSK. A KSK is always associated with a hosted zone; it cannot exist by itself.

Name -> (string)

A string used to identify a key-signing key (KSK). `Name` can include numbers, letters, and underscores (_). `Name` must be unique for each key-signing key in the same hosted zone.

KmsArn -> (string)

The Amazon resource name (ARN) used to identify the customer managed key in Key Management Service (KMS). The `KmsArn` must be unique for each key-signing key (KSK) in a single hosted zone.

You must configure the customer managed key as follows:

Status

Enabled

Key spec

ECC_NIST_P256

Key usage

Sign and verify

Key policy

The key policy must give permission for the following actions:

- DescribeKey
- GetPublicKey
- Sign

The key policy must also include the Amazon Route 53 service in the principal for your account. Specify the following:

- `"Service": "dnssec-route53.amazonaws.com"`

For more information about working with the customer managed key in KMS, see [Key Management Service concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) .

Flag -> (integer)

An integer that specifies how the key is used. For key-signing key (KSK), this value is always 257.

SigningAlgorithmMnemonic -> (string)

A string used to represent the signing algorithm. This value must follow the guidelines provided by [RFC-8624 Section 3.1](https://tools.ietf.org/html/rfc8624#section-3.1) .

SigningAlgorithmType -> (integer)

An integer used to represent the signing algorithm. This value must follow the guidelines provided by [RFC-8624 Section 3.1](https://tools.ietf.org/html/rfc8624#section-3.1) .

DigestAlgorithmMnemonic -> (string)

A string used to represent the delegation signer digest algorithm. This value must follow the guidelines provided by [RFC-8624 Section 3.3](https://tools.ietf.org/html/rfc8624#section-3.3) .

DigestAlgorithmType -> (integer)

An integer used to represent the delegation signer digest algorithm. This value must follow the guidelines provided by [RFC-8624 Section 3.3](https://tools.ietf.org/html/rfc8624#section-3.3) .

KeyTag -> (integer)

An integer used to identify the DNSSEC record for the domain name. The process used to calculate the value is described in [RFC-4034 Appendix B](https://tools.ietf.org/rfc/rfc4034.txt) .

DigestValue -> (string)

A cryptographic digest of a DNSKEY resource record (RR). DNSKEY records are used to publish the public key that resolvers can use to verify DNSSEC signatures that are used to secure certain kinds of information provided by the DNS system.

PublicKey -> (string)

The public key, represented as a Base64 encoding, as required by [RFC-4034 Page 5](https://tools.ietf.org/rfc/rfc4034.txt) .

DSRecord -> (string)

A string that represents a delegation signer (DS) record.

DNSKEYRecord -> (string)

A string that represents a DNSKEY record.

Status -> (string)

A string that represents the current key-signing key (KSK) status.

Status can have one of the following values:

ACTIVE

The KSK is being used for signing.

INACTIVE

The KSK is not being used for signing.

DELETING

The KSK is in the process of being deleted.

ACTION_NEEDED

There is a problem with the KSK that requires you to take action to resolve. For example, the customer managed key might have been deleted, or the permissions for the customer managed key might have been changed.

INTERNAL_FAILURE

There was an error during a request. Before you can continue to work with DNSSEC signing, including actions that involve this KSK, you must correct the problem. For example, you may need to activate or deactivate the KSK.

StatusMessage -> (string)

The status message provided for the following key-signing key (KSK) statuses: `ACTION_NEEDED` or `INTERNAL_FAILURE` . The status message includes information about what the problem might be and steps that you can take to correct the issue.

CreatedDate -> (timestamp)

The date when the key-signing key (KSK) was created.

LastModifiedDate -> (timestamp)

The last time that the key-signing key (KSK) was changed.