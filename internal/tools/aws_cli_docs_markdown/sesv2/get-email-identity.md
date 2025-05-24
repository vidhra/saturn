# get-email-identityÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-email-identity.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-email-identity.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sesv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/index.html#cli-aws-sesv2) ]

# get-email-identity

## Description

Provides information about a specific identity, including the identityâs verification status, sending authorization policies, its DKIM authentication status, and its custom Mail-From settings.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sesv2-2019-09-27/GetEmailIdentity)

## Synopsis

```
get-email-identity
--email-identity <value>
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

FeedbackForwardingStatus -> (boolean)

The feedback forwarding configuration for the identity.

If the value is `true` , you receive email notifications when bounce or complaint events occur. These notifications are sent to the address that you specified in the `Return-Path` header of the original email.

Youâre required to have a method of tracking bounces and complaints. If you havenât set up another mechanism for receiving bounce or complaint notifications (for example, by setting up an event destination), you receive an email notification when these events occur (even if this setting is disabled).

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

MailFromAttributes -> (structure)

An object that contains information about the Mail-From attributes for the email identity.

MailFromDomain -> (string)

The name of a domain that an email identity uses as a custom MAIL FROM domain.

MailFromDomainStatus -> (string)

The status of the MAIL FROM domain. This status can have the following values:

- `PENDING` â Amazon SES hasnât started searching for the MX record yet.
- `SUCCESS` â Amazon SES detected the required MX record for the MAIL FROM domain.
- `FAILED` â Amazon SES canât find the required MX record, or the record no longer exists.
- `TEMPORARY_FAILURE` â A temporary issue occurred, which prevented Amazon SES from determining the status of the MAIL FROM domain.

BehaviorOnMxFailure -> (string)

The action to take if the required MX record canât be found when you send an email. When you set this value to `USE_DEFAULT_VALUE` , the mail is sent using *amazonses.com* as the MAIL FROM domain. When you set this value to `REJECT_MESSAGE` , the Amazon SES API v2 returns a `MailFromDomainNotVerified` error, and doesnât attempt to deliver the email.

These behaviors are taken when the custom MAIL FROM domain configuration is in the `Pending` , `Failed` , and `TemporaryFailure` states.

Policies -> (map)

A map of policy names to policies.

key -> (string)

The name of the policy.

The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.

value -> (string)

The text of the policy in JSON format. The policy cannot exceed 4 KB.

For information about the syntax of sending authorization policies, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html) .

Tags -> (list)

An array of objects that define the tags (keys and values) that are associated with the email identity.

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

ConfigurationSetName -> (string)

The configuration set used by default when sending from this identity.

VerificationStatus -> (string)

The verification status of the identity. The status can be one of the following:

- `PENDING` â The verification process was initiated, but Amazon SES hasnât yet been able to verify the identity.
- `SUCCESS` â The verification process completed successfully.
- `FAILED` â The verification process failed.
- `TEMPORARY_FAILURE` â A temporary issue is preventing Amazon SES from determining the verification status of the identity.
- `NOT_STARTED` â The verification process hasnât been initiated for the identity.

VerificationInfo -> (structure)

An object that contains additional information about the verification status for the identity.

LastCheckedTimestamp -> (timestamp)

The last time a verification attempt was made for this identity.

LastSuccessTimestamp -> (timestamp)

The last time a successful verification was made for this identity.

ErrorType -> (string)

Provides the reason for the failure describing why Amazon SES was not able to successfully verify the identity. Below are the possible values:

- `INVALID_VALUE` â Amazon SES was able to find the record, but the value contained within the record was invalid. Ensure you have published the correct values for the record.
- `TYPE_NOT_FOUND` â The queried hostname exists but does not have the requested type of DNS record. Ensure that you have published the correct type of DNS record.
- `HOST_NOT_FOUND` â The queried hostname does not exist or was not reachable at the time of the request. Ensure that you have published the required DNS record(s).
- `SERVICE_ERROR` â A temporary issue is preventing Amazon SES from determining the verification status of the domain.
- `DNS_SERVER_ERROR` â The DNS server encountered an issue and was unable to complete the request.
- `REPLICATION_ACCESS_DENIED` â The verification failed because the user does not have the required permissions to replicate the DKIM key from the primary region. Ensure you have the necessary permissions in both primary and replica regions.
- `REPLICATION_PRIMARY_NOT_FOUND` â The verification failed because no corresponding identity was found in the specified primary region. Ensure the identity exists in the primary region before attempting replication.
- `REPLICATION_PRIMARY_BYO_DKIM_NOT_SUPPORTED` â The verification failed because the identity in the primary region is configured with Bring Your Own DKIM (BYODKIM). DKIM key replication is only supported for identities using Easy DKIM.
- `REPLICATION_REPLICA_AS_PRIMARY_NOT_SUPPORTED` â The verification failed because the specified primary identity is a replica of another identity, and multi-level replication is not supported; the primary identity must be a non-replica identity.
- `REPLICATION_PRIMARY_INVALID_REGION` â The verification failed due to an invalid primary region specified. Ensure you provide a valid Amazon Web Services region where Amazon SES is available and different from the replica region.

SOARecord -> (structure)

An object that contains information about the start of authority (SOA) record associated with the identity.

PrimaryNameServer -> (string)

Primary name server specified in the SOA record.

AdminEmail -> (string)

Administrative contact email from the SOA record.

SerialNumber -> (long)

Serial number from the SOA record.