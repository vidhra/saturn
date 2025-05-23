# get-aws-opportunity-summaryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/get-aws-opportunity-summary.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/get-aws-opportunity-summary.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [partnercentral-selling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/index.html#cli-aws-partnercentral-selling) ]

# get-aws-opportunity-summary

## Description

Retrieves a summary of an AWS Opportunity. This summary includes high-level details about the opportunity sourced from AWS, such as lifecycle information, customer details, and involvement type. It is useful for tracking updates on the AWS opportunity corresponding to an opportunity in the partnerâs account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/partnercentral-selling-2022-07-26/GetAwsOpportunitySummary)

## Synopsis

```
get-aws-opportunity-summary
--catalog <value>
--related-opportunity-identifier <value>
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

Specifies the catalog in which the AWS Opportunity is located. Accepted values include `AWS` for production opportunities or `Sandbox` for testing purposes. The catalog determines which environment the opportunity data is pulled from.

`--related-opportunity-identifier` (string)

The unique identifier for the related partner opportunity. Use this field to correlate an AWS opportunity with its corresponding partner opportunity.

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

Catalog -> (string)

Specifies the catalog in which the AWS Opportunity exists. This is the environment (e.g., `AWS` or `Sandbox` ) where the opportunity is being managed.

Customer -> (structure)

Provides details about the customer associated with the AWS Opportunity, including account information, industry, and other customer data. These details help partners understand the business context of the opportunity.

Contacts -> (list)

Provides a list of customer contacts involved in the opportunity. These contacts may include decision makers, influencers, and other stakeholders within the customerâs organization.

(structure)

An object that contains a `Customer Partner` âs contact details.

BusinessTitle -> (string)

The partner contactâs title (job title or role) associated with the `Opportunity` . `BusinessTitle` supports either `PartnerAccountManager` or `OpportunityOwner` .

Email -> (string)

The contactâs email address associated with the `Opportunity` .

FirstName -> (string)

The contactâs first name associated with the `Opportunity` .

LastName -> (string)

The contactâs last name associated with the `Opportunity` .

Phone -> (string)

The contactâs phone number associated with the `Opportunity` .

Insights -> (structure)

Provides insights into the AWS Opportunity, including engagement score and recommended actions that AWS suggests for the partner.

EngagementScore -> (string)

Represents a score assigned by AWS to indicate the level of engagement and potential success for the opportunity. This score helps partners prioritize their efforts.

NextBestActions -> (string)

Provides recommendations from AWS on the next best actions to take in order to move the opportunity forward and increase the likelihood of success.

InvolvementType -> (string)

Specifies the type of involvement AWS has in the opportunity, such as direct cosell or advisory support. This field helps partners understand the role AWS plays in advancing the opportunity.

InvolvementTypeChangeReason -> (string)

Provides a reason for any changes in the involvement type of AWS in the opportunity. This field is used to track why the level of AWS engagement has changed from `For Visibility Only` to `Co-sell` offering transparency into the partnership dynamics.

LifeCycle -> (structure)

Contains lifecycle information for the AWS Opportunity, including review status, stage, and target close date. This field is crucial for partners to monitor the progression of the opportunity.

ClosedLostReason -> (string)

Indicates the reason why an opportunity was marked as `Closed Lost` . This helps in understanding the context behind the lost opportunity and aids in refining future strategies.

NextSteps -> (string)

Specifies the immediate next steps required to progress the opportunity. These steps are based on AWS guidance and the current stage of the opportunity.

NextStepsHistory -> (list)

Provides a historical log of previous next steps that were taken to move the opportunity forward. This helps in tracking the decision-making process and identifying any delays or obstacles encountered.

(structure)

Tracks the history of next steps associated with the opportunity. This field captures the actions planned for the future and their timeline.

Time -> (timestamp)

Indicates the date and time when a particular next step was recorded or planned. This helps in managing the timeline for the opportunity.

Value -> (string)

Represents the details of the next step recorded, such as follow-up actions or decisions made. This field helps in tracking progress and ensuring alignment with project goals.

Stage -> (string)

Represents the current stage of the opportunity in its lifecycle, such as `Qualification` , `Validation` , or `Closed Won` . This helps in understanding the opportunityâs progress.

TargetCloseDate -> (string)

Indicates the expected date by which the opportunity is projected to close. This field helps in planning resources and timelines for both the partner and AWS.

OpportunityTeam -> (list)

Details the AWS opportunity team, including members involved. This information helps partners know who from AWS is engaged and what their role is.

(structure)

Represents an Amazon Web Services team member for the engagement. This structure includes details such as name, email, and business title.

BusinessTitle -> (string)

Specifies the Amazon Web Services team memberâs business title and indicates their organizational role.

Email -> (string)

Provides the Amazon Web Services team memberâs email address.

FirstName -> (string)

Provides the Amazon Web Services team memberâs first name.

LastName -> (string)

Provides the Amazon Web Services team memberâs last name.

Origin -> (string)

Specifies whether the AWS Opportunity originated from AWS or the partner. This helps distinguish between opportunities that were sourced by AWS and those referred by the partner.

Project -> (structure)

Provides details about the project associated with the AWS Opportunity, including the customerâs business problem, expected outcomes, and project scope. This information is crucial for understanding the broader context of the opportunity.

ExpectedCustomerSpend -> (list)

Indicates the expected spending by the customer over the course of the project. This value helps partners and AWS estimate the financial impact of the opportunity. Use the [AWS Pricing Calculator](https://calculator.aws/#/) to create an estimate of the customerâs total spend. If only annual recurring revenue (ARR) is available, distribute it across 12 months to provide an average monthly value.

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

RelatedEntityIds -> (structure)

Lists related entity identifiers, such as AWS products or partner solutions, associated with the AWS Opportunity. These identifiers provide additional context and help partners understand which AWS services are involved.

AwsProducts -> (list)

Specifies the AWS products associated with the opportunity. This field helps track the specific products that are part of the proposed solution.

(string)

Solutions -> (list)

Specifies the partner solutions related to the opportunity. These solutions represent the partnerâs offerings that are being positioned as part of the overall AWS opportunity.

(string)

RelatedOpportunityId -> (string)

Provides the unique identifier of the related partner opportunity, allowing partners to link the AWS Opportunity to their corresponding opportunity in their CRM system.

Visibility -> (string)

Defines the visibility level for the AWS Opportunity. Use `Full` visibility for most cases, while `Limited` visibility is reserved for special programs or sensitive opportunities.