# put-email-identity-dkim-signing-attributesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/put-email-identity-dkim-signing-attributes.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/put-email-identity-dkim-signing-attributes.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sesv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/index.html#cli-aws-sesv2) ]

# put-email-identity-dkim-signing-attributes

## Description

Used to configure or change the DKIM authentication settings for an email domain identity. You can use this operation to do any of the following:

- Update the signing attributes for an identity that uses Bring Your Own DKIM (BYODKIM).
- Update the key length that should be used for Easy DKIM.
- Change from using no DKIM authentication to using Easy DKIM.
- Change from using no DKIM authentication to using BYODKIM.
- Change from using Easy DKIM to using BYODKIM.
- Change from using BYODKIM to using Easy DKIM.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sesv2-2019-09-27/PutEmailIdentityDkimSigningAttributes)

## Synopsis

```
put-email-identity-dkim-signing-attributes
--email-identity <value>
--signing-attributes-origin <value>
[--signing-attributes <value>]
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

`--email-identity` (string)

The email identity.

`--signing-attributes-origin` (string)

The method to use to configure DKIM for the identity. There are the following possible values:

- `AWS_SES` â Configure DKIM for the identity by using [Easy DKIM](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html) .
- `EXTERNAL` â Configure DKIM for the identity by using Bring Your Own DKIM (BYODKIM).

Possible values:

- `AWS_SES`
- `EXTERNAL`
- `AWS_SES_AF_SOUTH_1`
- `AWS_SES_EU_NORTH_1`
- `AWS_SES_AP_SOUTH_1`
- `AWS_SES_EU_WEST_3`
- `AWS_SES_EU_WEST_2`
- `AWS_SES_EU_SOUTH_1`
- `AWS_SES_EU_WEST_1`
- `AWS_SES_AP_NORTHEAST_3`
- `AWS_SES_AP_NORTHEAST_2`
- `AWS_SES_ME_SOUTH_1`
- `AWS_SES_AP_NORTHEAST_1`
- `AWS_SES_IL_CENTRAL_1`
- `AWS_SES_SA_EAST_1`
- `AWS_SES_CA_CENTRAL_1`
- `AWS_SES_AP_SOUTHEAST_1`
- `AWS_SES_AP_SOUTHEAST_2`
- `AWS_SES_AP_SOUTHEAST_3`
- `AWS_SES_EU_CENTRAL_1`
- `AWS_SES_US_EAST_1`
- `AWS_SES_US_EAST_2`
- `AWS_SES_US_WEST_1`
- `AWS_SES_US_WEST_2`

`--signing-attributes` (structure)

An object that contains information about the private key and selector that you want to use to configure DKIM for the identity for Bring Your Own DKIM (BYODKIM) for the identity, or, configures the key length to be used for [Easy DKIM](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html) .

DomainSigningSelector -> (string)

[Bring Your Own DKIM] A string thatâs used to identify a public key in the DNS configuration for a domain.

DomainSigningPrivateKey -> (string)

[Bring Your Own DKIM] A private key thatâs used to generate a DKIM signature.

The private key must use 1024 or 2048-bit RSA encryption, and must be encoded using base64 encoding.

NextSigningKeyLength -> (string)

[Easy DKIM] The key length of the future DKIM key pair to be generated. This can be changed at most once per day.

DomainSigningAttributesOrigin -> (string)

The attribute to use for configuring DKIM for the identity depends on the operation:

- For `PutEmailIdentityDkimSigningAttributes` :
- None of the values are allowed - use the ` `SigningAttributesOrigin` [https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutEmailIdentityDkimSigningAttributes.html#SES-PutEmailIdentityDkimSigningAttributes-request](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutEmailIdentityDkimSigningAttributes.html#SES-PutEmailIdentityDkimSigningAttributes-request)-SigningAttributesOrigin`__ parameter instead
- For `CreateEmailIdentity` when replicating a parent identityâs DKIM configuration:
- Allowed values: All values except `AWS_SES` and `EXTERNAL`
- `AWS_SES` â Configure DKIM for the identity by using Easy DKIM.
- `EXTERNAL` â Configure DKIM for the identity by using Bring Your Own DKIM (BYODKIM).
- `AWS_SES_AF_SOUTH_1` â Configure DKIM for the identity by replicating from a parent identity in Africa (Cape Town) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_EU_NORTH_1` â Configure DKIM for the identity by replicating from a parent identity in Europe (Stockholm) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_AP_SOUTH_1` â Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Mumbai) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_EU_WEST_3` â Configure DKIM for the identity by replicating from a parent identity in Europe (Paris) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_EU_WEST_2` â Configure DKIM for the identity by replicating from a parent identity in Europe (London) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_EU_SOUTH_1` â Configure DKIM for the identity by replicating from a parent identity in Europe (Milan) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_EU_WEST_1` â Configure DKIM for the identity by replicating from a parent identity in Europe (Ireland) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_AP_NORTHEAST_3` â Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Osaka) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_AP_NORTHEAST_2` â Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Seoul) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_ME_SOUTH_1` â Configure DKIM for the identity by replicating from a parent identity in Middle East (Bahrain) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_AP_NORTHEAST_1` â Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Tokyo) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_IL_CENTRAL_1` â Configure DKIM for the identity by replicating from a parent identity in Israel (Tel Aviv) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_SA_EAST_1` â Configure DKIM for the identity by replicating from a parent identity in South America (SÃ£o Paulo) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_CA_CENTRAL_1` â Configure DKIM for the identity by replicating from a parent identity in Canada (Central) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_AP_SOUTHEAST_1` â Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Singapore) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_AP_SOUTHEAST_2` â Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Sydney) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_AP_SOUTHEAST_3` â Configure DKIM for the identity by replicating from a parent identity in Asia Pacific (Jakarta) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_EU_CENTRAL_1` â Configure DKIM for the identity by replicating from a parent identity in Europe (Frankfurt) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_US_EAST_1` â Configure DKIM for the identity by replicating from a parent identity in US East (N. Virginia) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_US_EAST_2` â Configure DKIM for the identity by replicating from a parent identity in US East (Ohio) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_US_WEST_1` â Configure DKIM for the identity by replicating from a parent identity in US West (N. California) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_US_WEST_2` â Configure DKIM for the identity by replicating from a parent identity in US West (Oregon) region using Deterministic Easy-DKIM (DEED).

Shorthand Syntax:

```
DomainSigningSelector=string,DomainSigningPrivateKey=string,NextSigningKeyLength=string,DomainSigningAttributesOrigin=string
```

JSON Syntax:

```
{
  "DomainSigningSelector": "string",
  "DomainSigningPrivateKey": "string",
  "NextSigningKeyLength": "RSA_1024_BIT"|"RSA_2048_BIT",
  "DomainSigningAttributesOrigin": "AWS_SES"|"EXTERNAL"|"AWS_SES_AF_SOUTH_1"|"AWS_SES_EU_NORTH_1"|"AWS_SES_AP_SOUTH_1"|"AWS_SES_EU_WEST_3"|"AWS_SES_EU_WEST_2"|"AWS_SES_EU_SOUTH_1"|"AWS_SES_EU_WEST_1"|"AWS_SES_AP_NORTHEAST_3"|"AWS_SES_AP_NORTHEAST_2"|"AWS_SES_ME_SOUTH_1"|"AWS_SES_AP_NORTHEAST_1"|"AWS_SES_IL_CENTRAL_1"|"AWS_SES_SA_EAST_1"|"AWS_SES_CA_CENTRAL_1"|"AWS_SES_AP_SOUTHEAST_1"|"AWS_SES_AP_SOUTHEAST_2"|"AWS_SES_AP_SOUTHEAST_3"|"AWS_SES_EU_CENTRAL_1"|"AWS_SES_US_EAST_1"|"AWS_SES_US_EAST_2"|"AWS_SES_US_WEST_1"|"AWS_SES_US_WEST_2"
}
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

## Output

DkimStatus -> (string)

The DKIM authentication status of the identity. Amazon SES determines the authentication status by searching for specific records in the DNS configuration for your domain. If you used [Easy DKIM](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html) to set up DKIM authentication, Amazon SES tries to find three unique CNAME records in the DNS configuration for your domain.

If you provided a public key to perform DKIM authentication, Amazon SES tries to find a TXT record that uses the selector that you specified. The value of the TXT record must be a public key thatâs paired with the private key that you specified in the process of creating the identity.

The status can be one of the following:

- `PENDING` â The verification process was initiated, but Amazon SES hasnât yet detected the DKIM records in the DNS configuration for the domain.
- `SUCCESS` â The verification process completed successfully.
- `FAILED` â The verification process failed. This typically occurs when Amazon SES fails to find the DKIM records in the DNS configuration of the domain.
- `TEMPORARY_FAILURE` â A temporary issue is preventing Amazon SES from determining the DKIM authentication status of the domain.
- `NOT_STARTED` â The DKIM verification process hasnât been initiated for the domain.

DkimTokens -> (list)

If you used [Easy DKIM](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html) to configure DKIM authentication for the domain, then this object contains a set of unique strings that you use to create a set of CNAME records that you add to the DNS configuration for your domain. When Amazon SES detects these records in the DNS configuration for your domain, the DKIM authentication process is complete.

If you configured DKIM authentication for the domain by providing your own public-private key pair, then this object contains the selector thatâs associated with your public key.

Regardless of the DKIM authentication method you use, Amazon SES searches for the appropriate records in the DNS configuration of the domain for up to 72 hours.

(string)