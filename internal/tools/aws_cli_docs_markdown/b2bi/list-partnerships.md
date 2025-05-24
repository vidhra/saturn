# list-partnershipsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/b2bi/list-partnerships.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/b2bi/list-partnerships.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [b2bi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/b2bi/index.html#cli-aws-b2bi) ]

# list-partnerships

## Description

Lists the partnerships associated with your Amazon Web Services account for your current or specified region. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/b2bi-2022-06-23/ListPartnerships)

`list-partnerships` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `partnerships`

## Synopsis

```
list-partnerships
[--profile-id <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
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

`--profile-id` (string)

Specifies the unique, system-generated identifier for the profile connected to this partnership.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

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

partnerships -> (list)

Specifies a list of your partnerships.

(structure)

A structure that contains the details for a partnership. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.

profileId -> (string)

Returns the unique, system-generated identifier for the profile connected to this partnership.

partnershipId -> (string)

Returns the unique, system-generated identifier for a partnership.

name -> (string)

Returns the name of the partnership.

capabilities -> (list)

Returns one or more capabilities associated with this partnership.

(string)

capabilityOptions -> (structure)

Contains the details for an Outbound EDI capability.

outboundEdi -> (tagged union structure)

A structure that contains the outbound EDI options.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `x12`.

x12 -> (structure)

A structure that contains an X12 envelope structure.

common -> (structure)

A container for the X12 outbound EDI headers.

interchangeControlHeaders -> (structure)

In X12 EDI messages, delimiters are used to mark the end of segments or elements, and are defined in the interchange control header.

senderIdQualifier -> (string)

Located at position ISA-05 in the header. Qualifier for the sender ID. Together, the ID and qualifier uniquely identify the sending trading partner.

senderId -> (string)

Located at position ISA-06 in the header. This value (along with the `senderIdQualifier` ) identifies the sender of the interchange.

receiverIdQualifier -> (string)

Located at position ISA-07 in the header. Qualifier for the receiver ID. Together, the ID and qualifier uniquely identify the receiving trading partner.

receiverId -> (string)

Located at position ISA-08 in the header. This value (along with the `receiverIdQualifier` ) identifies the intended recipient of the interchange.

repetitionSeparator -> (string)

Located at position ISA-11 in the header. This string makes it easier when you need to group similar adjacent element values together without using extra segments.

### Note

This parameter is only honored for version greater than 401 (`VERSION_4010` and higher).

For versions less than 401, this field is called [StandardsId](https://www.stedi.com/edi/x12-004010/segment/ISA#ISA-11) , in which case our service sets the value to `U` .

acknowledgmentRequestedCode -> (string)

Located at position ISA-14 in the header. The value â1â indicates that the sender is requesting an interchange acknowledgment at receipt of the interchange. The value â0â is used otherwise.

usageIndicatorCode -> (string)

Located at position ISA-15 in the header. Specifies how this interchange is being used:

- `T` indicates this interchange is for testing.
- `P` indicates this interchange is for production.
- `I` indicates this interchange is informational.

functionalGroupHeaders -> (structure)

The functional group headers for the X12 object.

applicationSenderCode -> (string)

A value representing the code used to identify the party transmitting a message, at position GS-02.

applicationReceiverCode -> (string)

A value representing the code used to identify the party receiving a message, at position GS-03.

responsibleAgencyCode -> (string)

A code that identifies the issuer of the standard, at position GS-07.

delimiters -> (structure)

The delimiters, for example semicolon (`;` ), that separates sections of the headers for the X12 object.

componentSeparator -> (string)

The component, or sub-element, separator. The default value is `:` (colon).

dataElementSeparator -> (string)

The data element separator. The default value is `*` (asterisk).

segmentTerminator -> (string)

The segment terminator. The default value is `~` (tilde).

validateEdi -> (boolean)

Specifies whether or not to validate the EDI for this X12 object: `TRUE` or `FALSE` .

tradingPartnerId -> (string)

Returns the unique, system-generated identifier for a trading partner.

createdAt -> (timestamp)

Returns a timestamp for creation date and time of the partnership.

modifiedAt -> (timestamp)

Returns a timestamp that identifies the most recent date and time that the partnership was modified.

nextToken -> (string)

When additional results are obtained from the command, a `NextToken` parameter is returned in the output. You can then pass the `NextToken` parameter in a subsequent command to continue listing additional resources.