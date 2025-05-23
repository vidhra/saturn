# get-opportunityÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/get-opportunity.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/get-opportunity.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [partnercentral-selling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/index.html#cli-aws-partnercentral-selling) ]

# get-opportunity

## Description

Fetches the `Opportunity` record from Partner Central by a given `Identifier` .

Use the `ListOpportunities` action or the event notification (from Amazon EventBridge) to obtain this identifier.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/partnercentral-selling-2022-07-26/GetOpportunity)

## Synopsis

```
get-opportunity
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

Specifies the catalog associated with the request. This field takes a string value from a predefined list: `AWS` or `Sandbox` . The catalog determines which environment the opportunity is fetched from. Use `AWS` to retrieve opportunities in the Amazon Web Services catalog, and `Sandbox` to retrieve opportunities in a secure, isolated testing environment.

`--identifier` (string)

Read-only, system generated `Opportunity` unique identifier.

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

The Amazon Resource Name (ARN) that uniquely identifies the opportunity.

Catalog -> (string)

Specifies the catalog associated with the request. This field takes a string value from a predefined list: `AWS` or `Sandbox` . The catalog determines which environment the opportunity information is retrieved from. Use `AWS` to retrieve opportunities in the Amazon Web Services catalog, and `Sandbox` to retrieve opportunities in a secure and isolated testing environment.

CreatedDate -> (timestamp)

`DateTime` when the `Opportunity` was last created.

Customer -> (structure)

Specifies details of the customer associated with the `Opportunity` .

Account -> (structure)

An object that contains the customerâs account details.

Address -> (structure)

Specifies the end `Customer` âs address details associated with the `Opportunity` .

City -> (string)

Specifies the end `Customer` âs city associated with the `Opportunity` .

CountryCode -> (string)

Specifies the end `Customer` âs country associated with the `Opportunity` .

PostalCode -> (string)

Specifies the end `Customer` âs postal code associated with the `Opportunity` .

StateOrRegion -> (string)

Specifies the end `Customer` âs state or region associated with the `Opportunity` .

Valid values: `Alabama | Alaska | American Samoa | Arizona | Arkansas | California | Colorado | Connecticut | Delaware | Dist. of Columbia | Federated States of Micronesia | Florida | Georgia | Guam | Hawaii | Idaho | Illinois | Indiana | Iowa | Kansas | Kentucky | Louisiana | Maine | Marshall Islands | Maryland | Massachusetts | Michigan | Minnesota | Mississippi | Missouri | Montana | Nebraska | Nevada | New Hampshire | New Jersey | New Mexico | New York | North Carolina | North Dakota | Northern Mariana Islands | Ohio | Oklahoma | Oregon | Palau | Pennsylvania | Puerto Rico | Rhode Island | South Carolina | South Dakota | Tennessee | Texas | Utah | Vermont | Virginia | Virgin Islands | Washington | West Virginia | Wisconsin | Wyoming | APO/AE | AFO/FPO | FPO, AP`

StreetAddress -> (string)

Specifies the end `Customer` âs street address associated with the `Opportunity` .

AwsAccountId -> (string)

Specifies the `Customer` Amazon Web Services account ID associated with the `Opportunity` .

CompanyName -> (string)

Specifies the end `Customer` âs company name associated with the `Opportunity` .

Duns -> (string)

Indicates the `Customer` DUNS number, if available.

Industry -> (string)

Specifies the industry the end `Customer` belongs to thatâs associated with the `Opportunity` . It refers to the category or sector where the customerâs business operates. This is a required field.

OtherIndustry -> (string)

Specifies the end `Customer` âs industry associated with the `Opportunity` , when the selected value in the `Industry` field is `Other` .

WebsiteUrl -> (string)

Specifies the end customerâs company website URL associated with the `Opportunity` . This value is crucial to map the customer within the Amazon Web Services CRM system. This field is required in all cases except when the opportunity is related to national security.

Contacts -> (list)

Represents the contact details for individuals associated with the customer of the `Opportunity` . This field captures relevant contacts, including decision-makers, influencers, and technical stakeholders within the customer organization. These contacts are key to progressing the opportunity.

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

Id -> (string)

Read-only, system generated `Opportunity` unique identifier.

LastModifiedDate -> (timestamp)

`DateTime` when the opportunity was last modified.

LifeCycle -> (structure)

An object that contains lifecycle details for the `Opportunity` .

ClosedLostReason -> (string)

Specifies the reason code when an opportunity is marked as *Closed Lost* . When you select an appropriate reason code, you communicate the context for closing the `Opportunity` , and aid in accurate reports and analysis of opportunity outcomes. The possible values are:

- Customer Deficiency: The customer lacked necessary resources or capabilities.
- Delay/Cancellation of Project: The project was delayed or canceled.
- Legal/Tax/Regulatory: Legal, tax, or regulatory issues prevented progress.
- Lost to CompetitorâGoogle: The opportunity was lost to Google.
- Lost to CompetitorâMicrosoft: The opportunity was lost to Microsoft.
- Lost to CompetitorâSoftLayer: The opportunity was lost to SoftLayer.
- Lost to CompetitorâVMWare: The opportunity was lost to VMWare.
- Lost to CompetitorâOther: The opportunity was lost to a competitor not listed above.
- No Opportunity: There was no opportunity to pursue.
- On Premises Deployment: The customer chose an on-premises solution.
- Partner Gap: The partner lacked necessary resources or capabilities.
- Price: The price was not competitive or acceptable to the customer.
- Security/Compliance: Security or compliance issues prevented progress.
- Technical Limitations: Technical limitations prevented progress.
- Customer Experience: Issues related to the customerâs experience impacted the decision.
- Other: Any reason not covered by the other values.
- People/Relationship/Governance: Issues related to people, relationships, or governance.
- Product/Technology: Issues related to the product or technology.
- Financial/Commercial: Financial or commercial issues impacted the decision.

NextSteps -> (string)

Specifies the upcoming actions or tasks for the `Opportunity` . Use this field to communicate with Amazon Web Services about the next actions required for the `Opportunity` .

NextStepsHistory -> (list)

Captures a chronological record of the next steps or actions planned or taken for the current opportunity, along with the timestamp.

(structure)

Read-only; shows the last 50 values and change dates for the `NextSteps` field.

Time -> (timestamp)

Indicates the step execution time.

Value -> (string)

Indicates the stepâs execution details.

ReviewComments -> (string)

Indicates why an opportunity was sent back for further details. Partners must take corrective action based on the `ReviewComments` .

ReviewStatus -> (string)

Indicates the review status of an opportunity referred by a partner. This field is read-only and only applicable for partner referrals. The possible values are:

- Pending Submission: Not submitted for validation (editable).
- Submitted: Submitted for validation, and Amazon Web Services hasnât reviewed it (read-only).
- In Review: Amazon Web Services is validating (read-only).
- Action Required: Issues that Amazon Web Services highlights need to be addressed. Partners should use the `UpdateOpportunity` API action to update the opportunity and helps to ensure that all required changes are made. Only the following fields are editable when the `Lifecycle.ReviewStatus` is `Action Required` :
- Customer.Account.Address.City
- Customer.Account.Address.CountryCode
- Customer.Account.Address.PostalCode
- Customer.Account.Address.StateOrRegion
- Customer.Account.Address.StreetAddress
- Customer.Account.WebsiteUrl
- LifeCycle.TargetCloseDate
- Project.ExpectedMonthlyAWSRevenue.Amount
- Project.ExpectedMonthlyAWSRevenue.CurrencyCode
- Project.CustomerBusinessProblem
- PartnerOpportunityIdentifier

After updates, the opportunity re-enters the validation phase. This process repeats until all issues are resolved, and the opportunityâs `Lifecycle.ReviewStatus` is set to `Approved` or `Rejected` .

- Approved: Validated and converted into the Amazon Web Services sellerâs pipeline (editable).
- Rejected: Disqualified (read-only).

ReviewStatusReason -> (string)

Indicates the reason a decision was made during the opportunity review process. This field combines the reasons for both disqualified and action required statuses, and provide clarity for why an opportunity was disqualified or requires further action.

Stage -> (string)

Specifies the current stage of the `Opportunity` âs lifecycle as it maps to Amazon Web Services stages from the current stage in the partner CRM. This field provides a translated value of the stage, and offers insight into the `Opportunity` âs progression in the sales cycle, according to Amazon Web Services definitions.

### Note

A lead and a prospect must be further matured to a `Qualified` opportunity before submission. Opportunities that were closed/lost before submission arenât suitable for submission.

The descriptions of each sales stage are:

- Prospect: Amazon Web Services identifies the opportunity. It can be active (Comes directly from the end customer through a lead) or latent (Your account team believes it exists based on research, account plans, sales plays).
- Qualified: Your account team engaged with the customer to discuss viability and requirements. The customer agreed that the opportunity is real, of interest, and may solve business/technical needs.
- Technical Validation: All parties understand the implementation plan.
- Business Validation: Pricing was proposed, and all parties agree to the steps to close.
- Committed: The customer signed the contract, but Amazon Web Services hasnât started billing.
- Launched: The workload is complete, and Amazon Web Services has started billing.
- Closed Lost: The opportunity is lost, and there are no steps to move forward.

TargetCloseDate -> (string)

Specifies the date when Amazon Web Services expects to start significant billing, when the project finishes, and when it moves into production. This field informs the Amazon Web Services seller about when the opportunity launches and starts to incur Amazon Web Services usage.

Ensure the `Target Close Date` isnât in the past.

Marketing -> (structure)

An object that contains marketing details for the `Opportunity` .

AwsFundingUsed -> (string)

Indicates if the `Opportunity` is a marketing development fund (MDF) funded activity.

CampaignName -> (string)

Specifies the `Opportunity` marketing campaign code. The Amazon Web Services campaign code is a reference to specific marketing initiatives, promotions, or activities. This field captures the identifier used to track and categorize the `Opportunity` within marketing campaigns. If you donât have a campaign code, contact your Amazon Web Services point of contact to obtain one.

Channels -> (list)

Specifies the `Opportunity` âs channel that the marketing activity is associated with or was contacted through. This field provides information about the specific marketing channel that contributed to the generation of the lead or contact.

(string)

Source -> (string)

Indicates if the `Opportunity` was sourced from an Amazon Web Services marketing activity. Use the value `Marketing Activity` . Use `None` if itâs not associated with an Amazon Web Services marketing activity. This field helps Amazon Web Services track the return on marketing investments and enables better distribution of marketing budgets among partners.

UseCases -> (list)

Specifies the marketing activity use case or purpose that led to the `Opportunity` âs creation or contact. This field captures the context or marketing activityâs executionâs intention and the direct correlation to the generated opportunity or contact. Must be empty when `Marketing.AWSFundingUsed = No` .

Valid values: `AI/ML | Analytics | Application Integration | Blockchain | Business Applications | Cloud Financial Management | Compute | Containers | Customer Engagement | Databases | Developer Tools | End User Computing | Front End Web & Mobile | Game Tech | IoT | Management & Governance | Media Services | Migration & Transfer | Networking & Content Delivery | Quantum Technologies | Robotics | Satellite | Security | Serverless | Storage | VR & AR`

(string)

NationalSecurity -> (string)

Indicates whether the `Opportunity` pertains to a national security project. This field must be set to `true` only when the customerâs industry is *Government* . Additional privacy and security measures apply during the review and management process for opportunities marked as `NationalSecurity` .

OpportunityTeam -> (list)

Represents the internal team handling the opportunity. Specify the members involved in collaborating on this opportunity within the partnerâs organization.

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

OpportunityType -> (string)

Specifies the opportunity type as renewal, new, or expansion.

Opportunity types:

- New opportunity: Represents a new business opportunity with a potential customer thatâs not previously engaged with your solutions or services.
- Renewal opportunity: Represents an opportunity to renew an existing contract or subscription with a current customer, which helps to ensure service continuity.
- Expansion opportunity: Represents an opportunity to expand the scope of a customerâs contract or subscription, either by adding new services or increasing the volume of existing services.

PartnerOpportunityIdentifier -> (string)

Specifies the opportunityâs unique identifier in the partnerâs CRM system. This value is essential to track and reconcile because itâs included in the outbound payload sent back to the partner.

PrimaryNeedsFromAws -> (list)

Identifies the type of support the partner needs from Amazon Web Services.

Valid values:

- CosellâArchitectural Validation: Confirmation from Amazon Web Services that the partnerâs proposed solution architecture is aligned with Amazon Web Services best practices and poses minimal architectural risks.
- CosellâBusiness Presentation: Request Amazon Web Services sellerâs participation in a joint customer presentation.
- CosellâCompetitive Information: Access to Amazon Web Services competitive resources and support for the partnerâs proposed solution.
- CosellâPricing Assistance: Connect with an Amazon Web Services seller for support situations where a partner may be receiving an upfront discount on a service (for example: EDP deals).
- CosellâTechnical Consultation: Connect with an Amazon Web Services Solutions Architect to address the partnerâs questions about the proposed solution.
- CosellâTotal Cost of Ownership Evaluation: Assistance with quoting different cost savings of proposed solutions on Amazon Web Services versus on-premises or a traditional hosting environment.
- CosellâDeal Support: Request Amazon Web Services sellerâs support to progress the opportunity (for example: joint customer call, strategic positioning).
- CosellâSupport for Public Tender/RFx: Opportunity related to the public sector where the partner needs Amazon Web Services RFx support.

(string)

Project -> (structure)

An object that contains project details summary for the `Opportunity` .

AdditionalComments -> (string)

Captures additional comments or information for the `Opportunity` that werenât captured in other fields.

ApnPrograms -> (list)

Specifies the Amazon Partner Network (APN) program that influenced the `Opportunity` . APN programs refer to specific partner programs or initiatives that can impact the `Opportunity` .

Valid values: `APN Immersion Days | APN Solution Space | ATO (Authority to Operate) | AWS Marketplace Campaign | IS Immersion Day SFID Program | ISV Workload Migration | Migration Acceleration Program | P3 | Partner Launch Initiative | Partner Opportunity Acceleration Funded | The Next Smart | VMware Cloud on AWS | Well-Architected | Windows | Workspaces/AppStream Accelerator Program | WWPS NDPP`

(string)

CompetitorName -> (string)

Name of the `Opportunity` âs competitor (if any). Use `Other` to submit a value not in the picklist.

CustomerBusinessProblem -> (string)

Describes the problem the end customer has, and how the partner is helping. Utilize this field to provide a concise narrative that outlines the customerâs business challenge or issue. Elaborate on how the partnerâs solution or offerings align to resolve the customerâs business problem. Include relevant information about the partnerâs value proposition, unique selling points, and expertise to tackle the issue. Offer insights on how the proposed solution meets the customerâs needs and provides value. Use concise language and precise descriptions to convey the context and significance of the `Opportunity` . The content in this field helps Amazon Web Services understand the nature of the `Opportunity` and the strategic fit of the partnerâs solution.

CustomerUseCase -> (string)

Specifies the proposed solution focus or type of workload for the Opportunity. This field captures the primary use case or objective of the proposed solution, and provides context and clarity to the addressed workload.

Valid values: `AI Machine Learning and Analytics | Archiving | Big Data: Data Warehouse/Data Integration/ETL/Data Lake/BI | Blockchain | Business Applications: Mainframe Modernization | Business Applications & Contact Center | Business Applications & SAP Production | Centralized Operations Management | Cloud Management Tools | Cloud Management Tools & DevOps with Continuous Integration & Continuous Delivery (CICD) | Configuration, Compliance & Auditing | Connected Services | Containers & Serverless | Content Delivery & Edge Services | Database | Edge Computing/End User Computing | Energy | Enterprise Governance & Controls | Enterprise Resource Planning | Financial Services | Healthcare and Life Sciences | High Performance Computing | Hybrid Application Platform | Industrial Software | IOT | Manufacturing, Supply Chain and Operations | Media & High performance computing (HPC) | Migration/Database Migration | Monitoring, logging and performance | Monitoring & Observability | Networking | Outpost | SAP | Security & Compliance | Storage & Backup | Training | VMC | VMWare | Web development & DevOps`

DeliveryModels -> (list)

Specifies the deployment or consumption model for your solution or service in the `Opportunity` âs context. You can select multiple options.

Optionsâ descriptions from the `Delivery Model` field are:

- SaaS or PaaS: Your Amazon Web Services based solution deployed as SaaS or PaaS in your Amazon Web Services environment.
- BYOL or AMI: Your Amazon Web Services based solution deployed as BYOL or AMI in the end customerâs Amazon Web Services environment.
- Managed Services: The end customerâs Amazon Web Services business management (For example: Consulting, design, implementation, billing support, cost optimization, technical support).
- Professional Services: Offerings to help enterprise end customers achieve specific business outcomes for enterprise cloud adoption (For example: Advisory or transformation planning).
- Resell: Amazon Web Services accounts and billing management for your customers.
- Other: Delivery model not described above.

(string)

ExpectedCustomerSpend -> (list)

Represents the estimated amount that the customer is expected to spend on AWS services related to the opportunity. This helps in evaluating the potential financial value of the opportunity for AWS.

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

OtherCompetitorNames -> (string)

Only allowed when `CompetitorNames` has `Other` selected.

OtherSolutionDescription -> (string)

Specifies the offered solution for the customerâs business problem when the `RelatedEntityIdentifiers.Solutions` field value is `Other` .

RelatedOpportunityIdentifier -> (string)

Specifies the current opportunityâs parent opportunity identifier.

SalesActivities -> (list)

Specifies the `Opportunity` âs sales activities conducted with the end customer. These activities help drive Amazon Web Services assignment priority.

Valid values:

- Initialized discussions with customer: Initial conversations with the customer to understand their needs and introduce your solution.
- Customer has shown interest in solution: After initial discussions, the customer is interested in your solution.
- Conducted POC/demo: You conducted a proof of concept (POC) or demonstration of the solution for the customer.
- In evaluation/planning stage: The customer is evaluating the solution and planning potential implementation.
- Agreed on solution to Business Problem: Both parties agree on how the solution addresses the customerâs business problem.
- Completed Action Plan: A detailed action plan is complete and outlines the steps for implementation.
- Finalized Deployment Need: Both parties agree with and finalized the deployment needs.
- SOW Signed: Both parties signed a statement of work (SOW), and formalize the agreement and detail the project scope and deliverables.

(string)

Title -> (string)

Specifies the `Opportunity` âs title or name.

RelatedEntityIdentifiers -> (structure)

Provides information about the associations of other entities with the opportunity. These entities include identifiers for `AWSProducts` , `Partner Solutions` , and `AWSMarketplaceOffers` .

AwsMarketplaceOffers -> (list)

Takes one value per opportunity. Each value is an Amazon Resource Name (ARN), in this format: `"offers": ["arn:aws:aws-marketplace:us-east-1:999999999999:AWSMarketplace/Offer/offer-sampleOffer32"]` .

Use the [ListEntities](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_ListEntities.html) action in the Marketplace Catalog APIs for a list of offers in the associated Marketplace seller account.

(string)

AwsProducts -> (list)

Enables the association of specific Amazon Web Services products with the `Opportunity` . Partners can indicate the relevant Amazon Web Services products for the `Opportunity` âs solution and align with the customerâs needs. Returns multiple values separated by commas. For example, `"AWSProducts" : ["AmazonRedshift", "AWSAppFabric", "AWSCleanRooms"]` .

Use the file with the list of Amazon Web Services products hosted on GitHub: [Amazon Web Services products](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/resources/aws_products.json) .

(string)

Solutions -> (list)

Enables partner solutions or offeringsâ association with an opportunity. To associate a solution, provide the solutionâs unique identifier, which you can obtain with the `ListSolutions` operation.

If the specific solution identifier is not available, you can use the value `Other` and provide details about the solution in the `otherSolutionOffered` field. But when the opportunity reaches the `Committed` stage or beyond, the `Other` value cannot be used, and a valid solution identifier must be provided.

By associating the relevant solutions with the opportunity, you can communicate the offerings that are being considered or implemented to address the customerâs business problem.

(string)

SoftwareRevenue -> (structure)

Specifies details of a customerâs procurement terms. Required only for partners in eligible programs.

DeliveryModel -> (string)

Specifies the customerâs intended payment type agreement or procurement method to acquire the solution or service outlined in the `Opportunity` .

EffectiveDate -> (string)

Specifies the `Opportunity` âs customer engagement start date for the contractâs effectiveness.

ExpirationDate -> (string)

Specifies the expiration date for the contract between the customer and Amazon Web Services partner. It signifies the termination date of the agreed-upon engagement period between both parties.

Value -> (structure)

Specifies the payment value (amount and currency).

Amount -> (string)

Specifies the payment amount.

CurrencyCode -> (string)

Specifies the payment currency.