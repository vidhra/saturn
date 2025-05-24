# create-email-identityÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-email-identity.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-email-identity.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sesv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/index.html#cli-aws-sesv2) ]

# create-email-identity

## Description

Starts the process of verifying an email identity. An *identity* is an email address or domain that you use when you send email. Before you can use an identity to send email, you first have to verify it. By verifying an identity, you demonstrate that youâre the owner of the identity, and that youâve given Amazon SES API v2 permission to send email from the identity.

When you verify an email address, Amazon SES sends an email to the address. Your email address is verified as soon as you follow the link in the verification email.

When you verify a domain without specifying the `DkimSigningAttributes` object, this operation provides a set of DKIM tokens. You can convert these tokens into CNAME records, which you then add to the DNS configuration for your domain. Your domain is verified when Amazon SES detects these records in the DNS configuration for your domain. This verification method is known as [Easy DKIM](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html) .

Alternatively, you can perform the verification process by providing your own public-private key pair. This verification method is known as Bring Your Own DKIM (BYODKIM). To use BYODKIM, your call to the `CreateEmailIdentity` operation has to include the `DkimSigningAttributes` object. When you specify this object, you provide a selector (a component of the DNS record name that identifies the public key to use for DKIM authentication) and a private key.

When you verify a domain, this operation provides a set of DKIM tokens, which you can convert into CNAME tokens. You add these CNAME tokens to the DNS configuration for your domain. Your domain is verified when Amazon SES detects these records in the DNS configuration for your domain. For some DNS providers, it can take 72 hours or more to complete the domain verification process.

Additionally, you can associate an existing configuration set with the email identity that youâre verifying.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sesv2-2019-09-27/CreateEmailIdentity)

## Synopsis

```
create-email-identity
--email-identity <value>
[--tags <value>]
[--dkim-signing-attributes <value>]
[--configuration-set-name <value>]
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

The email address or domain to verify.

`--tags` (list)

An array of objects that define the tags (keys and values) to associate with the email identity.

(structure)

An object that defines the tags that are associated with a resource. A *tag* is a label that you optionally define and associate with a resource. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.

Each tag consists of a required *tag key* and an associated *tag value* , both of which you define. A tag key is a general label that acts as a category for a more specific tag value. A tag value acts as a descriptor within a tag key. A tag key can contain as many as 128 characters. A tag value can contain as many as 256 characters. The characters can be Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The following additional restrictions apply to tags:

- Tag keys and values are case sensitive.
- For each associated resource, each tag key must be unique and it can have only one value.
- The `aws:` prefix is reserved for use by Amazon Web Services; you canât use it in any tag keys or values that you define. In addition, you canât edit or remove tag keys or values that use this prefix. Tags that use this prefix donât count against the limit of 50 tags per resource.
- You can associate tags with public or shared resources, but the tags are available only for your Amazon Web Services account, not any other accounts that share the resource. In addition, the tags are available only for resources that are located in the specified Amazon Web Services Region for your Amazon Web Services account.

Key -> (string)

One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character.

Value -> (string)

The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you donât want a resource to have a specific tag value, donât specify a value for this parameter. If you donât specify a value, Amazon SES sets the value to an empty string.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--dkim-signing-attributes` (structure)

If your request includes this object, Amazon SES configures the identity to use Bring Your Own DKIM (BYODKIM) for DKIM authentication purposes, or, configures the key length to be used for [Easy DKIM](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html) .

You can only specify this object if the email identity is a domain, as opposed to an address.

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

`--configuration-set-name` (string)

The configuration set to use by default when sending from this identity. Note that any configuration set defined in the email sending request takes precedence.

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

IdentityType -> (string)

The email identity type. Note: the `MANAGED_DOMAIN` identity type is not supported.

VerifiedForSendingStatus -> (boolean)

Specifies whether or not the identity is verified. You can only send email from verified email addresses or domains. For more information about verifying identities, see the [Amazon Pinpoint User Guide](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage-verify.html) .

DkimAttributes -> (structure)

An object that contains information about the DKIM attributes for the identity.

SigningEnabled -> (boolean)

If the value is `true` , then the messages that you send from the identity are signed using DKIM. If the value is `false` , then the messages that you send from the identity arenât DKIM-signed.

Status -> (string)

Describes whether or not Amazon SES has successfully located the DKIM records in the DNS records for the domain. The status can be one of the following:

- `PENDING` â The verification process was initiated, but Amazon SES hasnât yet detected the DKIM records in the DNS configuration for the domain.
- `SUCCESS` â The verification process completed successfully.
- `FAILED` â The verification process failed. This typically occurs when Amazon SES fails to find the DKIM records in the DNS configuration of the domain.
- `TEMPORARY_FAILURE` â A temporary issue is preventing Amazon SES from determining the DKIM authentication status of the domain.
- `NOT_STARTED` â The DKIM verification process hasnât been initiated for the domain.

Tokens -> (list)

If you used [Easy DKIM](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html) to configure DKIM authentication for the domain, then this object contains a set of unique strings that you use to create a set of CNAME records that you add to the DNS configuration for your domain. When Amazon SES detects these records in the DNS configuration for your domain, the DKIM authentication process is complete.

If you configured DKIM authentication for the domain by providing your own public-private key pair, then this object contains the selector for the public key.

Regardless of the DKIM authentication method you use, Amazon SES searches for the appropriate records in the DNS configuration of the domain for up to 72 hours.

(string)

SigningAttributesOrigin -> (string)

A string that indicates how DKIM was configured for the identity. These are the possible values:

- `AWS_SES` â Indicates that DKIM was configured for the identity by using [Easy DKIM](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html) .
- `EXTERNAL` â Indicates that DKIM was configured for the identity by using Bring Your Own DKIM (BYODKIM).
- `AWS_SES_AF_SOUTH_1` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in Africa (Cape Town) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_EU_NORTH_1` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in Europe (Stockholm) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_AP_SOUTH_1` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in Asia Pacific (Mumbai) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_EU_WEST_3` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in Europe (Paris) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_EU_WEST_2` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in Europe (London) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_EU_SOUTH_1` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in Europe (Milan) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_EU_WEST_1` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in Europe (Ireland) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_AP_NORTHEAST_3` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in Asia Pacific (Osaka) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_AP_NORTHEAST_2` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in Asia Pacific (Seoul) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_ME_SOUTH_1` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in Middle East (Bahrain) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_AP_NORTHEAST_1` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in Asia Pacific (Tokyo) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_IL_CENTRAL_1` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in Israel (Tel Aviv) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_SA_EAST_1` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in South America (SÃ£o Paulo) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_CA_CENTRAL_1` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in Canada (Central) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_AP_SOUTHEAST_1` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in Asia Pacific (Singapore) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_AP_SOUTHEAST_2` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in Asia Pacific (Sydney) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_AP_SOUTHEAST_3` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in Asia Pacific (Jakarta) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_EU_CENTRAL_1` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in Europe (Frankfurt) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_US_EAST_1` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in US East (N. Virginia) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_US_EAST_2` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in US East (Ohio) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_US_WEST_1` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in US West (N. California) region using Deterministic Easy-DKIM (DEED).
- `AWS_SES_US_WEST_2` â Indicates that DKIM was configured for the identity by replicating signing attributes from a parent identity in US West (Oregon) region using Deterministic Easy-DKIM (DEED).

NextSigningKeyLength -> (string)

[Easy DKIM] The key length of the future DKIM key pair to be generated. This can be changed at most once per day.

CurrentSigningKeyLength -> (string)

[Easy DKIM] The key length of the DKIM key pair in use.

LastKeyGenerationTimestamp -> (timestamp)

[Easy DKIM] The last time a key pair was generated for this identity.