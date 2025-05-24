# get-resource-snapshotÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/get-resource-snapshot.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/get-resource-snapshot.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [partnercentral-selling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/index.html#cli-aws-partnercentral-selling) ]

# get-resource-snapshot

## Description

Use this action to retrieve a specific snapshot record.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/partnercentral-selling-2022-07-26/GetResourceSnapshot)

## Synopsis

```
get-resource-snapshot
--catalog <value>
--engagement-identifier <value>
--resource-identifier <value>
--resource-snapshot-template-identifier <value>
--resource-type <value>
[--revision <value>]
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

Specifies the catalog related to the request. Valid values are:

- AWS: Retrieves the snapshot from the production AWS environment.
- Sandbox: Retrieves the snapshot from a sandbox environment used for testing or development purposes.

`--engagement-identifier` (string)

The unique identifier of the engagement associated with the snapshot. This field links the snapshot to a specific engagement context.

`--resource-identifier` (string)

The unique identifier of the specific resource that was snapshotted. The format and constraints of this identifier depend on the ResourceType specified. For `Opportunity` type, it will be an `opportunity ID`

`--resource-snapshot-template-identifier` (string)

he name of the template that defines the schema for the snapshot. This template determines which subset of the resource data is included in the snapshot and must correspond to an existing and valid template for the specified `ResourceType` .

`--resource-type` (string)

Specifies the type of resource that was snapshotted. This field determines the structure and content of the snapshot payload. Valid value includes:`Opportunity` : For opportunity-related data.

Possible values:

- `Opportunity`

`--revision` (integer)

Specifies which revision of the snapshot to retrieve. If omitted returns the latest revision.

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

The Amazon Resource Name (ARN) that uniquely identifies the resource snapshot.

Catalog -> (string)

The catalog in which the snapshot was created. Matches the Catalog specified in the request.

CreatedAt -> (timestamp)

The timestamp when the snapshot was created, in ISO 8601 format (e.g., â2023-06-01T14:30:00Zâ). This allows for precise tracking of when the snapshot was taken.

CreatedBy -> (string)

The AWS account ID of the principal (user or role) who created the snapshot. This helps in tracking the origin of the snapshot.

EngagementId -> (string)

The identifier of the engagement associated with this snapshot. Matches the EngagementIdentifier specified in the request.

Payload -> (tagged union structure)

Represents the payload of a resource snapshot. This structure is designed to accommodate different types of resource snapshots, currently supporting opportunity summaries.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `OpportunitySummary`.

OpportunitySummary -> (structure)

An object that contains an `opportunity` âs subset of fields.

Customer -> (structure)

An object that contains the customerâs `Account` and `Contact` .

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

Lifecycle -> (structure)

Contains information about the opportunityâs lifecycle, including its current stage, status, and important dates such as creation and last modification times.

NextSteps -> (string)

Describes the next steps for the opportunity shared through a snapshot.

ReviewStatus -> (string)

Defines the approval status of the opportunity shared through a snapshot.

Stage -> (string)

Defines the current stage of the opportunity shared through a snapshot.

TargetCloseDate -> (string)

The projected launch date of the opportunity shared through a snapshot.

OpportunityTeam -> (list)

Represents the internal team handling the opportunity. Specify the members involved in collaborating on an opportunity within the partnerâs organization.

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

Specifies the opportunity type.

PrimaryNeedsFromAws -> (list)

Identifies the type of support the partner needs from AWS.

(string)

Project -> (structure)

Contains summary information about the project associated with the opportunity, including project name, description, timeline, and other relevant details.

CustomerUseCase -> (string)

Specifies the proposed solution focus or type of workload for the project.

DeliveryModels -> (list)

Describes the deployment or consumption model for the partner solution or offering. This field indicates how the projectâs solution will be delivered or implemented for the customer.

(string)

ExpectedCustomerSpend -> (list)

Provides information about the anticipated customer spend related to this project. This may include details such as amount, frequency, and currency of expected expenditure.

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

OtherSolutionDescription -> (string)

Offers a description of other solutions if the standard solutions do not adequately cover the projectâs scope.

SalesActivities -> (list)

Lists the pre-sales activities that have occurred with the end-customer related to the opportunity. This field is conditionally mandatory when the project is qualified for Co-Sell and helps drive assignment priority on the AWS side. It provides insight into the engagement level with the customer.

(string)

RelatedEntityIdentifiers -> (structure)

This field provides the associationsâ information for other entities with the opportunity. These entities include identifiers for `AWSProducts` , `Partner Solutions` , and `AWSMarketplaceOffers` .

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

ResourceId -> (string)

The identifier of the specific resource that was snapshotted. Matches the ResourceIdentifier specified in the request.

ResourceSnapshotTemplateName -> (string)

The name of the view used for this snapshot. This is the same as the template name.

ResourceType -> (string)

The type of the resource that was snapshotted. Matches the ResourceType specified in the request.

Revision -> (integer)

The revision number of this snapshot. This is a positive integer that is sequential and unique within the context of a resource view.