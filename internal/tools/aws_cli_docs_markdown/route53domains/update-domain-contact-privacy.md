# update-domain-contact-privacyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/update-domain-contact-privacy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/update-domain-contact-privacy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53domains](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/index.html#cli-aws-route53domains) ]

# update-domain-contact-privacy

## Description

This operation updates the specified domain contactâs privacy setting. When privacy protection is enabled, your contact information is replaced with contact information for the registrar or with the phrase âREDACTED FOR PRIVACYâ, or âOn behalf of <domain name> owner.â

### Note

While some domains may allow different privacy settings per contact, we recommend specifying the same privacy setting for all contacts.

This operation affects only the contact information for the specified contact type (administrative, registrant, or technical). If the request succeeds, Amazon Route 53 returns an operation ID that you can use with [GetOperationDetail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html) to track the progress and completion of the action. If the request doesnât complete successfully, the domain registrant will be notified by email.

### Warning

By disabling the privacy service via API, you consent to the publication of the contact information provided for this domain via the public WHOIS database. You certify that you are the registrant of this domain name and have the authority to make this decision. You may withdraw your consent at any time by enabling privacy protection using either `UpdateDomainContactPrivacy` or the Route 53 console. Enabling privacy protection removes the contact information provided for this domain from the WHOIS database. For more information on our privacy practices, see [https://aws.amazon.com/privacy/](https://aws.amazon.com/privacy/) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/UpdateDomainContactPrivacy)

## Synopsis

```
update-domain-contact-privacy
--domain-name <value>
[--admin-privacy | --no-admin-privacy]
[--registrant-privacy | --no-registrant-privacy]
[--tech-privacy | --no-tech-privacy]
[--billing-privacy | --no-billing-privacy]
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

`--domain-name` (string)

The name of the domain that you want to update the privacy setting for.

`--admin-privacy` | `--no-admin-privacy` (boolean)

Whether you want to conceal contact information from WHOIS queries. If you specify `true` , WHOIS (âwho isâ) queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify `false` , WHOIS queries return the information that you entered for the admin contact.

### Note

You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.

`--registrant-privacy` | `--no-registrant-privacy` (boolean)

Whether you want to conceal contact information from WHOIS queries. If you specify `true` , WHOIS (âwho isâ) queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify `false` , WHOIS queries return the information that you entered for the registrant contact (domain owner).

### Note

You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.

`--tech-privacy` | `--no-tech-privacy` (boolean)

Whether you want to conceal contact information from WHOIS queries. If you specify `true` , WHOIS (âwho isâ) queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify `false` , WHOIS queries return the information that you entered for the technical contact.

### Note

You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.

`--billing-privacy` | `--no-billing-privacy` (boolean)

Whether you want to conceal contact information from WHOIS queries. If you specify `true` , WHOIS (âwho isâ) queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify `false` , WHOIS queries return the information that you entered for the billing contact.

### Note

You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.

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

**To update the privacy settings for the contacts for a domain**

The following `update-domain-contact-privacy` command turns off privacy protection for the administrative contact for the example.com domain. This command runs only in the `us-east-1` Region.

If your default region is set to `us-east-1`, you can omit the `region` parameter.

```
aws route53domains update-domain-contact-privacy \
    --region us-east-1 \
    --domain-name example.com \
    --no-admin-privacy
```

Output:

```
{
    "OperationId": "b3a219e9-d801-4244-b533-b7256example"
}
```

To confirm that the operation succeeded, you can run `get-operation-detail`. For more information, see [get-operation-detail](https://docs.aws.amazon.com/cli/latest/reference/route53domains/get-operation-detail.html) .

For more information, see [Enabling or Disabling Privacy Protection for Contact Information for a Domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-privacy-protection.html) in the *Amazon Route 53 Developer Guide*.

## Output

OperationId -> (string)

Identifier for tracking the progress of the request. To use this ID to query the operation status, use GetOperationDetail.