# get-engagement-invitationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/get-engagement-invitation.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/get-engagement-invitation.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [partnercentral-selling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/index.html#cli-aws-partnercentral-selling) ]

# get-engagement-invitation

## Description

Retrieves the details of an engagement invitation shared by AWS with a partner. The information includes aspects such as customer, project details, and lifecycle information. To connect an engagement invitation with an opportunity, match the invitationâs `Payload.Project.Title` with opportunity `Project.Title` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/partnercentral-selling-2022-07-26/GetEngagementInvitation)

## Synopsis

```
get-engagement-invitation
--catalog <value>
--identifier <value>
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

`--catalog` (string)

Specifies the catalog associated with the request. The field accepts values from the predefined set: `AWS` for live operations or `Sandbox` for testing environments.

`--identifier` (string)

Specifies the unique identifier for the retrieved engagement invitation.

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

Arn -> (string)

The Amazon Resource Name (ARN) that identifies the engagement invitation.

Catalog -> (string)

Indicates the catalog from which the engagement invitation details are retrieved. This field helps in identifying the appropriate catalog (e.g., `AWS` or `Sandbox` ) used in the request.

EngagementDescription -> (string)

The description of the engagement associated with this invitation.

EngagementId -> (string)

The identifier of the engagement associated with this invitation.This ID links the invitation to its corresponding engagement.

EngagementTitle -> (string)

The title of the engagement invitation, summarizing the purpose or objectives of the opportunity shared by AWS.

ExistingMembers -> (list)

A list of active members currently part of the Engagement. This array contains a maximum of 10 members, each represented by an object with the following properties.

- CompanyName: The name of the memberâs company.
- WebsiteUrl: The website URL of the memberâs company.

(structure)

The EngagementMemberSummary provides a snapshot of essential information about participants in an AWS Partner Central Engagement. This compact data structure encapsulates key details of each member, facilitating efficient collaboration and management within the Engagement.

CompanyName -> (string)

The official name of the memberâs company or organization.

WebsiteUrl -> (string)

The URL of the member companyâs website. This offers a way to find more information about the member organization and serves as an additional identifier.

ExpirationDate -> (timestamp)

Indicates the date on which the engagement invitation will expire if not accepted by the partner.

Id -> (string)

Unique identifier assigned to the engagement invitation being retrieved.

InvitationDate -> (timestamp)

The date when the engagement invitation was sent to the partner.

InvitationMessage -> (string)

The message sent to the invited partner when the invitation was created.

Payload -> (tagged union structure)

Details of the engagement invitation payload, including specific data relevant to the invitationâs contents, such as customer information and opportunity insights.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `OpportunityInvitation`.

OpportunityInvitation -> (structure)

Specifies the details of the opportunity invitation within the Engagement Invitation payload. This data helps partners understand the context, scope, and expected involvement for the opportunity from AWS.

Customer -> (structure)

Contains information about the customer related to the opportunity in the Engagement Invitation. This data helps partners understand the customerâs profile and requirements.

CompanyName -> (string)

Represents the name of the customerâs company associated with the Engagement Invitation. This field is used to identify the customer.

CountryCode -> (string)

Indicates the country in which the customerâs company operates. This field is useful for understanding regional requirements or compliance needs.

Industry -> (string)

Specifies the industry to which the customerâs company belongs. This field helps categorize the opportunity based on the customerâs business sector.

WebsiteUrl -> (string)

Provides the website URL of the customerâs company. This field helps partners verify the legitimacy and size of the customer organization.

Project -> (structure)

Describes the project details associated with the opportunity, including the customerâs needs and the scope of work expected to be performed.

BusinessProblem -> (string)

Describes the business problem that the project aims to solve. This information is crucial for understanding the projectâs goals and objectives.

ExpectedCustomerSpend -> (list)

Contains revenue estimates for the partner related to the project. This field provides an idea of the financial potential of the opportunity for the partner.

(structure)

Provides an estimate of the revenue that the partner is expected to generate from the opportunity. This information helps partners assess the financial value of the project.

Amount -> (string)

Represents the estimated monthly revenue that the partner expects to earn from the opportunity. This helps in forecasting financial returns.

CurrencyCode -> (string)

Indicates the currency in which the revenue estimate is provided. This helps in understanding the financial impact across different markets.

EstimationUrl -> (string)

A URL providing additional information or context about the spend estimation.

Frequency -> (string)

Indicates how frequently the customer is expected to spend the projected amount. This can include values such as `Monthly` , `Quarterly` , or `Annually` . The default value is `Monthly` , representing recurring monthly spend.

TargetCompany -> (string)

Specifies the name of the partner company that is expected to generate revenue from the opportunity. This field helps track the partnerâs involvement in the opportunity.

TargetCompletionDate -> (string)

Specifies the estimated date of project completion. This field helps track the project timeline and manage expectations.

Title -> (string)

Specifies the title of the project. This title helps partners quickly identify and understand the focus of the project.

ReceiverResponsibilities -> (list)

Outlines the responsibilities or expectations of the receiver in the context of the invitation.

(string)

SenderContacts -> (list)

Represents the contact details of the AWS representatives involved in sending the Engagement Invitation. These contacts are opportunity stakeholders.

(structure)

An object that contains the details of the sender-provided contact person for the `EngagementInvitation` .

BusinessTitle -> (string)

The sender-provided contactâs title (job title or role) associated with the `EngagementInvitation` .

Email -> (string)

The sender-provided contactâs email address associated with the `EngagementInvitation` .

FirstName -> (string)

The sender-provided contactâs last name associated with the `EngagementInvitation` .

LastName -> (string)

The sender-provided contactâs first name associated with the `EngagementInvitation` .

Phone -> (string)

The sender-provided contactâs phone number associated with the `EngagementInvitation` .

PayloadType -> (string)

The type of payload contained in the engagement invitation, indicating what data or context the payload covers.

Receiver -> (tagged union structure)

Information about the partner organization or team that received the engagement invitation, including contact details and identifiers.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Account`.

Account -> (structure)

Specifies the AWS account of the partner who received the Engagement Invitation. This field is used to track the invitation recipient within the AWS ecosystem.

Alias -> (string)

Represents the alias of the partner account receiving the Engagement Invitation, making it easier to identify and track the recipient in reports or logs.

AwsAccountId -> (string)

Indicates the AWS account ID of the partner who received the Engagement Invitation. This is a unique identifier for managing engagements with specific AWS accounts.

RejectionReason -> (string)

If the engagement invitation was rejected, this field specifies the reason provided by the partner for the rejection.

SenderAwsAccountId -> (string)

Specifies the AWS Account ID of the sender, which identifies the AWS team responsible for sharing the engagement invitation.

SenderCompanyName -> (string)

The name of the AWS organization or team that sent the engagement invitation.

Status -> (string)

The current status of the engagement invitation.