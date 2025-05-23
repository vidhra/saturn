# get-agreement-termsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-agreement/get-agreement-terms.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-agreement/get-agreement-terms.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [marketplace-agreement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-agreement/index.html#cli-aws-marketplace-agreement) ]

# get-agreement-terms

## Description

Obtains details about the terms in an agreement that you participated in as proposer or acceptor.

The details include:

- `TermType` â The type of term, such as `LegalTerm` , `RenewalTerm` , or `ConfigurableUpfrontPricingTerm` .
- `TermID` â The ID of the particular term, which is common between offer and agreement.
- `TermPayload` â The key information contained in the term, such as the EULA for `LegalTerm` or pricing and dimensions for various pricing terms, such as `ConfigurableUpfrontPricingTerm` or `UsageBasedPricingTerm` .
- `Configuration` â The buyer/acceptorâs selection at the time of agreement creation, such as the number of units purchased for a dimension or setting the `EnableAutoRenew` flag.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/marketplace-agreement-2020-03-01/GetAgreementTerms)

## Synopsis

```
get-agreement-terms
--agreement-id <value>
[--max-results <value>]
[--next-token <value>]
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

`--agreement-id` (string)

The unique identifier of the agreement.

`--max-results` (integer)

The maximum number of agreements to return in the response.

`--next-token` (string)

A token to specify where to start pagination

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

acceptedTerms -> (list)

A subset of terms proposed by the proposer that have been accepted by the acceptor as part of the agreement creation.

(tagged union structure)

A subset of terms proposed by the proposer, which have been accepted by the acceptor as part of agreement creation.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `byolPricingTerm`, `configurableUpfrontPricingTerm`, `fixedUpfrontPricingTerm`, `freeTrialPricingTerm`, `legalTerm`, `paymentScheduleTerm`, `recurringPaymentTerm`, `renewalTerm`, `supportTerm`, `usageBasedPricingTerm`, `validityTerm`.

byolPricingTerm -> (structure)

Enables you and your customers to move your existing agreements to AWS Marketplace. The customer wonât be charged for product usage in AWS Marketplace because they already paid for the product outside of AWS Marketplace.

type -> (string)

Type of the term being updated.

configurableUpfrontPricingTerm -> (structure)

Defines a prepaid payment model that allows buyers to configure the entitlements they want to purchase and the duration.

configuration -> (structure)

Additional parameters specified by the acceptor while accepting the term.

dimensions -> (list)

Defines the dimensions that the acceptor has purchased from the overall set of dimensions presented in the rate card.

(structure)

Defines the dimensions that the acceptor has purchased from the overall set of dimensions presented in the rate card.

dimensionKey -> (string)

The name of key value of the dimension.

dimensionValue -> (integer)

The number of units of the dimension the acceptor has purchased.

### Note

For Agreements with `ConfigurableUpfrontPricingTerm` , the `RateCard` section will define the prices and dimensions defined by the seller (proposer), whereas the `Configuration` section will define the actual dimensions, prices, and units the buyer has chosen to accept.

selectorValue -> (string)

Defines the length of time for which the particular pricing/dimension is being purchased by the acceptor.

currencyCode -> (string)

Defines the currency for the prices mentioned in the term.

rateCards -> (list)

A rate card defines the per unit rates for product dimensions.

(structure)

Within the prepaid payment model defined under `ConfigurableUpfrontPricingTerm` , the `RateCardItem` defines all the various rate cards (including pricing and dimensions) that have been proposed.

constraints -> (structure)

Defines limits on how the term can be configured by acceptors.

multipleDimensionSelection -> (string)

Determines if buyers are allowed to select multiple dimensions in the rate card. The possible values are `Allowed` and `Disallowed` . The default value is `Allowed` .

quantityConfiguration -> (string)

Determines if acceptors are allowed to configure quantity for each dimension in rate card. The possible values are `Allowed` and `Disallowed` . The default value is `Allowed` .

rateCard -> (list)

Defines the per unit rates for product dimensions.

(structure)

Defines the per unit rates for each individual product dimension.

dimensionKey -> (string)

Dimension for which the given entitlement applies. Dimensions represent categories of capacity in a product and are specified when the product is listed in AWS Marketplace.

price -> (string)

Per unit price for the product dimension thatâs used for calculating the amount to be charged.

selector -> (structure)

Differentiates between the mutually exclusive rate cards in the same pricing term to be selected by the buyer.

type -> (string)

Category of selector.

value -> (string)

Contract duration. This field supports the ISO 8601 format.

type -> (string)

Category of selector.

fixedUpfrontPricingTerm -> (structure)

Defines a pre-paid pricing model where the customers are charged a fixed upfront amount.

currencyCode -> (string)

Defines the currency for the prices mentioned in this term.

duration -> (string)

Contract duration for the terms.

grants -> (list)

Entitlements granted to the acceptor of fixed upfront as part of agreement execution.

(structure)

Entitlements granted to the acceptor of fixed upfront as part of agreement execution.

dimensionKey -> (string)

Unique dimension key defined in the product document. Dimensions represent categories of capacity in a product and are specified when the product is listed in AWS Marketplace.

maxQuantity -> (integer)

Maximum amount of capacity that the buyer can be entitled to the given dimension of the product. If `MaxQuantity` is not provided, the buyer will be able to use an unlimited amount of the given dimension.

price -> (string)

Fixed amount to be charged to the customer when this term is accepted.

type -> (string)

Category of the term being updated.

freeTrialPricingTerm -> (structure)

Defines a short-term free pricing model where the buyers arenât charged anything within a specified limit.

duration -> (string)

Duration of the free trial period (5â31 days).

grants -> (list)

Entitlements granted to the acceptor of a free trial as part of an agreement execution.

(structure)

Entitlements granted to the acceptor of fixed upfront as part of agreement execution.

dimensionKey -> (string)

Unique dimension key defined in the product document. Dimensions represent categories of capacity in a product and are specified when the product is listed in AWS Marketplace.

maxQuantity -> (integer)

Maximum amount of capacity that the buyer can be entitled to the given dimension of the product. If `MaxQuantity` is not provided, the buyer will be able to use an unlimited amount of the given dimension.

type -> (string)

Category of the term.

legalTerm -> (structure)

Defines the list of text agreements proposed to the acceptors. An example is the end user license agreement (EULA).

documents -> (list)

List of references to legal resources proposed to the buyers. An example is the EULA.

(structure)

Includes the list of references to legal resources proposed by the proposer to the acceptor. Each `DocumentItem` refers to an individual reference.

type -> (string)

Category of the document. Document types include:

- `CustomEula` â A custom EULA provided by you as seller. A URL for a EULA stored in an accessible Amazon S3 bucket is required for this document type.
- `CustomDsa` â A custom Data Subscription Agreement (DSA) provided by you as seller. A URL for a DSA stored in an accessible Amazon S3 bucket is required for this document type.
- `StandardEula` â The Standard Contract for AWS Marketplace (SCMP). For more information about SCMP, see the AWS Marketplace Seller Guide. You donât provide a URL for this type because itâs managed by AWS Marketplace.
- `StandardDsa` â DSA for AWS Marketplace. For more information about the DSA, see the AWS Data Exchange User Guide. You donât provide a URL for this type because itâs managed by AWS Marketplace.

url -> (string)

A URL to the legal document for buyers to read. Required when `Type` is `CustomEula` .

version -> (string)

Version of standard contracts provided by AWS Marketplace. Required when Type is `StandardEula` or `StandardDsa` .

type -> (string)

Category of the term being updated.

paymentScheduleTerm -> (structure)

Defines an installment-based pricing model where customers are charged a fixed price on different dates during the agreement validity period. This is used most commonly for flexible payment schedule pricing.

currencyCode -> (string)

Defines the currency for the prices mentioned in the term.

schedule -> (list)

List of the payment schedule where each element defines one installment of payment. It contains the information necessary for calculating the price.

(structure)

An individual installment of the payment that includes the date and amount of the charge.

chargeAmount -> (string)

The price that the customer would pay on the scheduled date (chargeDate).

chargeDate -> (timestamp)

The date that the customer would pay the price defined in this payment schedule term. Invoices are generated on the date provided.

type -> (string)

Type of the term.

recurringPaymentTerm -> (structure)

Defines a pricing model where customers are charged a fixed recurring price at the end of each billing period.

billingPeriod -> (string)

Defines the recurrence at which buyers are charged.

currencyCode -> (string)

Defines the currency for the prices mentioned in this term.

price -> (string)

Amount charged to the buyer every billing period.

type -> (string)

Type of the term being updated.

renewalTerm -> (structure)

Defines that on graceful expiration of the agreement (when the agreement ends on its pre-defined end date), a new agreement will be created using the accepted terms on the existing agreement. In other words, the agreement will be renewed. Presence of `RenewalTerm` in the offer document means that auto-renewal is allowed. Buyers will have the option to accept or decline auto-renewal at the offer acceptance/agreement creation. Buyers can also change this flag from `True` to `False` or `False` to `True` at anytime during the agreementâs lifecycle.

configuration -> (structure)

Additional parameters specified by the acceptor while accepting the term.

enableAutoRenew -> (boolean)

Defines whether the acceptor has chosen to auto-renew the agreement at the end of its lifecycle. Can be set to `True` or `False` .

type -> (string)

Category of the term being updated.

supportTerm -> (structure)

Defines the customer support available for the acceptors when they purchase the software.

refundPolicy -> (string)

Free-text field about the refund policy description that will be shown to customers as is on the website and console.

type -> (string)

Category of the term being updated.

usageBasedPricingTerm -> (structure)

Defines a usage-based pricing model (typically, pay-as-you-go pricing), where the customers are charged based on product usage.

currencyCode -> (string)

Defines the currency for the prices mentioned in the term.

rateCards -> (list)

List of rate cards.

(structure)

Within the pay-as-you-go model defined under `UsageBasedPricingTerm` , the `UsageBasedRateCardItem` defines an individual rate for a product dimension.

rateCard -> (list)

Defines the per unit rates for product dimensions.

(structure)

Defines the per unit rates for each individual product dimension.

dimensionKey -> (string)

Dimension for which the given entitlement applies. Dimensions represent categories of capacity in a product and are specified when the product is listed in AWS Marketplace.

price -> (string)

Per unit price for the product dimension thatâs used for calculating the amount to be charged.

type -> (string)

Category of the term.

validityTerm -> (structure)

Defines the conditions that will keep an agreement created from this offer valid.

agreementDuration -> (string)

Defines the duration that the agreement remains active. If `AgreementStartDate` isnât provided, the agreement duration is relative to the agreement signature time. The duration is represented in the ISO_8601 format.

agreementEndDate -> (timestamp)

Defines the date when the agreement ends. The agreement ends at 23:59:59.999 UTC on the date provided. If `AgreementEndDate` isnât provided, the agreement end date is determined by the validity of individual terms.

agreementStartDate -> (timestamp)

Defines the date when agreement starts. The agreement starts at 00:00:00.000 UTC on the date provided. If `AgreementStartDate` isnât provided, the agreement start date is determined based on agreement signature time.

type -> (string)

Category of the term being updated.

nextToken -> (string)

A token to specify where to start pagination