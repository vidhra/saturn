# get-identity-dkim-attributesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-identity-dkim-attributes.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-identity-dkim-attributes.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/index.html#cli-aws-ses) ]

# get-identity-dkim-attributes

## Description

Returns the current status of Easy DKIM signing for an entity. For domain name identities, this operation also returns the DKIM tokens that are required for Easy DKIM signing, and whether Amazon SES has successfully verified that these tokens have been published.

This operation takes a list of identities as input and returns the following information for each:

- Whether Easy DKIM signing is enabled or disabled.
- A set of DKIM tokens that represent the identity. If the identity is an email address, the tokens represent the domain of that address.
- Whether Amazon SES has successfully verified the DKIM tokens published in the domainâs DNS. This information is only returned for domain name identities, not for email addresses.

This operation is throttled at one request per second and can only get DKIM attributes for up to 100 identities at a time.

For more information about creating DNS records using DKIM tokens, go to the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-easy-managing.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/GetIdentityDkimAttributes)

## Synopsis

```
get-identity-dkim-attributes
--identities <value>
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

`--identities` (list)

A list of one or more verified identities - email addresses, domains, or both.

(string)

Syntax:

```
"string" "string" ...
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To get the Amazon SES Easy DKIM attributes for a list of identities**

The following example uses the `get-identity-dkim-attributes` command to retrieve the Amazon SES Easy DKIM attributes for a list of identities:

```
aws ses get-identity-dkim-attributes --identities "example.com" "user@example.com"
```

Output:

```
{
   "DkimAttributes": {
       "example.com": {
           "DkimTokens": [
               "EXAMPLEjcs5xoyqytjsotsijas7236gr",
               "EXAMPLEjr76cvoc6mysspnioorxsn6ep",
               "EXAMPLEkbmkqkhlm2lyz77ppkulerm4k"
           ],
           "DkimEnabled": true,
           "DkimVerificationStatus": "Success"
       },
       "user@example.com": {
           "DkimEnabled": false,
           "DkimVerificationStatus": "NotStarted"
       }
   }
}
```

If you call this command with an identity that you have never submitted for verification, that identity wonât appear in the output.

For more information about Easy DKIM, see [Easy DKIM in Amazon SES](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html) in the *Amazon Simple Email Service Developer Guide*.

## Output

DkimAttributes -> (map)

The DKIM attributes for an email address or a domain.

key -> (string)

value -> (structure)

Represents the DKIM attributes of a verified email address or a domain.

DkimEnabled -> (boolean)

Is true if DKIM signing is enabled for email sent from the identity. Itâs false otherwise. The default value is true.

DkimVerificationStatus -> (string)

Describes whether Amazon SES has successfully verified the DKIM DNS records (tokens) published in the domain nameâs DNS. (This only applies to domain identities, not email address identities.)

DkimTokens -> (list)

A set of character strings that represent the domainâs identity. Using these tokens, you need to create DNS CNAME records that point to DKIM public keys that are hosted by Amazon SES. Amazon Web Services eventually detects that youâve updated your DNS records. This detection process might take up to 72 hours. After successful detection, Amazon SES is able to DKIM-sign email originating from that domain. (This only applies to domain identities, not email address identities.)

For more information about creating DNS records using DKIM tokens, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-easy.html) .

(string)