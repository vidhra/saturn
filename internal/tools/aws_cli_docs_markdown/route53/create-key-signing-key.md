# create-key-signing-keyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-key-signing-key.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-key-signing-key.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html#cli-aws-route53) ]

# create-key-signing-key

## Description

Creates a new key-signing key (KSK) associated with a hosted zone. You can only have two KSKs per hosted zone.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/CreateKeySigningKey)

## Synopsis

```
create-key-signing-key
--caller-reference <value>
--hosted-zone-id <value>
--key-management-service-arn <value>
--name <value>
--status <value>
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

`--caller-reference` (string)

A unique string that identifies the request.

`--hosted-zone-id` (string)

The unique string (ID) used to identify a hosted zone.

`--key-management-service-arn` (string)

The Amazon resource name (ARN) for a customer managed key in Key Management Service (KMS). The `KeyManagementServiceArn` must be unique for each key-signing key (KSK) in a single hosted zone. To see an example of `KeyManagementServiceArn` that grants the correct permissions for DNSSEC, scroll down to **Example** .

You must configure the customer managed customer managed key as follows:

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

For more information about working with a customer managed key in KMS, see [Key Management Service concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) .

`--name` (string)

A string used to identify a key-signing key (KSK). `Name` can include numbers, letters, and underscores (_). `Name` must be unique for each key-signing key in the same hosted zone.

`--status` (string)

A string specifying the initial status of the key-signing key (KSK). You can set the value to `ACTIVE` or `INACTIVE` .

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

ChangeInfo -> (structure)

A complex type that describes change information about changes made to your hosted zone.

Id -> (string)

This element contains an ID that you use when performing a [GetChange](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html) action to get detailed information about the change.

Status -> (string)

The current state of the request. `PENDING` indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.

SubmittedAt -> (timestamp)

The date and time that the change request was submitted in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601) and Coordinated Universal Time (UTC). For example, the value `2017-03-27T17:48:16.751Z` represents March 27, 2017 at 17:48:16.751 UTC.

Comment -> (string)

A comment you can provide.

KeySigningKey -> (structure)

The key-signing key (KSK) that the request creates.

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

Location -> (string)

The unique URL representing the new key-signing key (KSK).