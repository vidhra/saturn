# list-engagement-invitationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/list-engagement-invitations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/list-engagement-invitations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [partnercentral-selling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/index.html#cli-aws-partnercentral-selling) ]

# list-engagement-invitations

## Description

Retrieves a list of engagement invitations sent to the partner. This allows partners to view all pending or past engagement invitations, helping them track opportunities shared by AWS.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/partnercentral-selling-2022-07-26/ListEngagementInvitations)

`list-engagement-invitations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `EngagementInvitationSummaries`

## Synopsis

```
list-engagement-invitations
--catalog <value>
[--engagement-identifier <value>]
--participant-type <value>
[--payload-type <value>]
[--sender-aws-account-id <value>]
[--sort <value>]
[--status <value>]
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

`--catalog` (string)

Specifies the catalog from which to list the engagement invitations. Use `AWS` for production invitations or `Sandbox` for testing environments.

`--engagement-identifier` (list)

Retrieves a list of engagement invitation summaries based on specified filters. The ListEngagementInvitations operation allows you to view all invitations that you have sent or received. You must specify the ParticipantType to filter invitations where you are either the SENDER or the RECEIVER. Invitations will automatically expire if not accepted within 15 days.

(string)

Syntax:

```
"string" "string" ...
```

`--participant-type` (string)

Specifies the type of participant for which to list engagement invitations. Identifies the role of the participant.

Possible values:

- `SENDER`
- `RECEIVER`

`--payload-type` (list)

Defines the type of payload associated with the engagement invitations to be listed. The attributes in this payload help decide on acceptance or rejection of the invitation.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  OpportunityInvitation
```

`--sender-aws-account-id` (list)

List of sender AWS account IDs to filter the invitations.

(string)

Syntax:

```
"string" "string" ...
```

`--sort` (structure)

Specifies the sorting options for listing engagement invitations. Invitations can be sorted by fields such as `InvitationDate` or `Status` to help partners view results in their preferred order.

SortBy -> (string)

Specifies the field by which the Engagement Invitations are sorted. Common values include `InvitationDate` and `Status` .

SortOrder -> (string)

Defines the order in which the Engagement Invitations are sorted. The values can be `ASC` (ascending) or `DESC` (descending).

Shorthand Syntax:

```
SortBy=string,SortOrder=string
```

JSON Syntax:

```
{
  "SortBy": "InvitationDate",
  "SortOrder": "ASCENDING"|"DESCENDING"
}
```

`--status` (list)

Status values to filter the invitations.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  ACCEPTED
  PENDING
  REJECTED
  EXPIRED
```

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

EngagementInvitationSummaries -> (list)

An array containing summaries of engagement invitations. Each summary includes information such as the invitation title, invitation date, and the current status of the invitation.

(structure)

Provides a summarized view of the Engagement Invitation, including details like the identifier, status, and sender. This summary helps partners track and manage AWS originated opportunities.

Arn -> (string)

The Amazon Resource Name (ARN) of the Engagement Invitation. The ARN is a unique identifier that allows partners to reference the invitation in their system and manage its lifecycle.

Catalog -> (string)

Specifies the catalog in which the Engagement Invitation resides. This can be either the `AWS` or `Sandbox` catalog, indicating whether the opportunity is live or being tested.

EngagementId -> (string)

The identifier of the Engagement associated with this invitation. This links the invitation to its parent Engagement.

EngagementTitle -> (string)

Provides a short title or description of the Engagement Invitation. This title helps partners quickly identify and differentiate between multiple engagement opportunities.

ExpirationDate -> (timestamp)

Indicates the date and time when the Engagement Invitation will expire. After this date, the invitation can no longer be accepted, and the opportunity will be unavailable to the partner.

Id -> (string)

Represents the unique identifier of the Engagement Invitation. This identifier is used to track the invitation and to manage responses like acceptance or rejection.

InvitationDate -> (timestamp)

Indicates the date when the Engagement Invitation was sent to the partner. This provides context for when the opportunity was shared and helps in tracking the timeline for engagement.

ParticipantType -> (string)

Identifies the role of the caller in the engagement invitation.

PayloadType -> (string)

Describes the type of payload associated with the Engagement Invitation, such as `Opportunity` or `MarketplaceOffer` . This helps partners understand the nature of the engagement request from AWS.

Receiver -> (tagged union structure)

Specifies the partner company or individual that received the Engagement Invitation. This field is important for tracking who the invitation was sent to within the partner organization.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Account`.

Account -> (structure)

Specifies the AWS account of the partner who received the Engagement Invitation. This field is used to track the invitation recipient within the AWS ecosystem.

Alias -> (string)

Represents the alias of the partner account receiving the Engagement Invitation, making it easier to identify and track the recipient in reports or logs.

AwsAccountId -> (string)

Indicates the AWS account ID of the partner who received the Engagement Invitation. This is a unique identifier for managing engagements with specific AWS accounts.

SenderAwsAccountId -> (string)

Specifies the AWS account ID of the sender who initiated the Engagement Invitation. This allows the partner to identify the AWS entity or representative responsible for sharing the opportunity.

SenderCompanyName -> (string)

Indicates the name of the company or AWS division that sent the Engagement Invitation. This information is useful for partners to know which part of AWS is requesting engagement.

Status -> (string)

Represents the current status of the Engagement Invitation, such as `Pending` , `Accepted` , or `Rejected` . The status helps track the progress and response to the invitation.

NextToken -> (string)

A pagination token returned when there are more results available than can be returned in a single call. Use this token to retrieve additional pages of engagement invitation summaries.