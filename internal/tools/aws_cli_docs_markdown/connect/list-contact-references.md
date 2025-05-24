# list-contact-referencesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-contact-references.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-contact-references.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# list-contact-references

## Description

This API is in preview release for Amazon Connect and is subject to change.

For the specified `referenceTypes` , returns a list of references associated with the contact. *References* are links to documents that are related to a contact, such as emails, attachments, or URLs.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListContactReferences)

`list-contact-references` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ReferenceSummaryList`

## Synopsis

```
list-contact-references
--instance-id <value>
--contact-id <value>
--reference-types <value>
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--max-items <value>]
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

`--instance-id` (string)

The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.

`--contact-id` (string)

The identifier of the initial contact.

`--reference-types` (list)

The type of reference.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  URL
  ATTACHMENT
  CONTACT_ANALYSIS
  NUMBER
  STRING
  DATE
  EMAIL
  EMAIL_MESSAGE
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

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

## Output

ReferenceSummaryList -> (list)

Information about the flows.

(tagged union structure)

Contains summary information about a reference. `ReferenceSummary` contains only one non null field between the URL and attachment based on the reference type.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Url`, `Attachment`, `EmailMessage`, `String`, `Number`, `Date`, `Email`.

Url -> (structure)

Information about the reference when the `referenceType` is `URL` . Otherwise, null.

Name -> (string)

Identifier of the URL reference.

Value -> (string)

A valid URL.

Attachment -> (structure)

Information about the reference when the `referenceType` is `ATTACHMENT` . Otherwise, null.

Name -> (string)

Identifier of the attachment reference.

Value -> (string)

The location path of the attachment reference.

Status -> (string)

Status of the attachment reference type.

Arn -> (string)

The Amazon Resource Name (ARN) of the attachment reference.

EmailMessage -> (structure)

Information about the reference when the referenceType is `EMAIL_MESSAGE` . Otherwise, null.

Name -> (string)

The name of the email message reference

Arn -> (string)

The Amazon Resource Name (ARN) of the email message reference

String -> (structure)

Information about a reference when the `referenceType` is `STRING` . Otherwise, null.

Name -> (string)

Identifier of the string reference.

Value -> (string)

A valid string.

Number -> (structure)

Information about a reference when the `referenceType` is `NUMBER` . Otherwise, null.

Name -> (string)

Identifier of the number reference.

Value -> (string)

A valid number.

Date -> (structure)

Information about a reference when the `referenceType` is `DATE` . Otherwise, null.

Name -> (string)

Identifier of the date reference.

Value -> (string)

A valid date.

Email -> (structure)

Information about a reference when the `referenceType` is `EMAIL` . Otherwise, null.

Name -> (string)

Identifier of the email reference.

Value -> (string)

A valid email address.

NextToken -> (string)

If there are additional results, this is the token for the next set of results.

### Warning

This is always returned as null in the response.