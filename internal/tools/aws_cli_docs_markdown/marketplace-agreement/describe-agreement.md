# describe-agreementÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-agreement/describe-agreement.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-agreement/describe-agreement.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [marketplace-agreement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-agreement/index.html#cli-aws-marketplace-agreement) ]

# describe-agreement

## Description

Provides details about an agreement, such as the proposer, acceptor, start date, and end date.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/marketplace-agreement-2020-03-01/DescribeAgreement)

## Synopsis

```
describe-agreement
--agreement-id <value>
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

acceptanceTime -> (timestamp)

The date and time the offer was accepted or the agreement was created.

### Note

`AcceptanceTime` and `StartTime` can differ for future dated agreements (FDAs).

acceptor -> (structure)

The details of the party accepting the agreement terms. This is commonly the buyer for `PurchaseAgreement` .

accountId -> (string)

The AWS account ID of the acceptor.

agreementId -> (string)

The unique identifier of the agreement.

agreementType -> (string)

The type of agreement. Values are `PurchaseAgreement` or `VendorInsightsAgreement` .

endTime -> (timestamp)

The date and time when the agreement ends. The field is `null` for pay-as-you-go agreements, which donât have end dates.

estimatedCharges -> (structure)

The estimated cost of the agreement.

agreementValue -> (string)

The total known amount customer has to pay across the lifecycle of the agreement.

### Note

This is the total contract value if accepted terms contain `ConfigurableUpfrontPricingTerm` or `FixedUpfrontPricingTerm` . In the case of pure contract pricing, this will be the total value of the contract. In the case of contracts with consumption pricing, this will only include the committed value and not include any overages that occur.

If the accepted terms contain `PaymentScheduleTerm` , it will be the total payment schedule amount. This occurs when flexible payment schedule is used, and is the sum of all invoice charges in the payment schedule.

In case a customer has amended an agreement, by purchasing more units of any dimension, this will include both the original cost as well as the added cost incurred due to addition of new units.

This is `0` if the accepted terms contain `UsageBasedPricingTerm` without `ConfigurableUpfrontPricingTerm` or `RecurringPaymentTerm` . This occurs for usage-based pricing (such as SaaS metered or AMI/container hourly or monthly), because the exact usage is not known upfront.

currencyCode -> (string)

Defines the currency code for the charge.

proposalSummary -> (structure)

A summary of the proposal received from the proposer.

offerId -> (string)

The unique identifier of the offer in AWS Marketplace.

resources -> (list)

The list of resources involved in the agreement.

(structure)

The list of resources involved in the agreement.

id -> (string)

The unique identifier of the resource.

### Note

We mention the term resource, which is most commonly a product, so a `resourceId` is also a `productId` .

type -> (string)

Type of the resource, which is the product. Values include `SaaSProduct` or `AmiProduct` .

proposer -> (structure)

The details of the party proposing the agreement terms. This is commonly the seller for `PurchaseAgreement` .

accountId -> (string)

The AWS account ID of the proposer.

startTime -> (timestamp)

The date and time when the agreement starts.

status -> (string)

The current status of the agreement.

Statuses include:

- `ACTIVE` â The terms of the agreement are active.
- `ARCHIVED` â The agreement ended without a specified reason.
- `CANCELLED` â The acceptor ended the agreement before the defined end date.
- `EXPIRED` â The agreement ended on the defined end date.
- `RENEWED` â The agreement was renewed into a new agreement (for example, an auto-renewal).
- `REPLACED` â The agreement was replaced using an agreement replacement offer.
- `ROLLED_BACK` (Only applicable to inactive agreement revisions) â The agreement revision has been rolled back because of an error. An earlier revision is now active.
- `SUPERCEDED` (Only applicable to inactive agreement revisions) â The agreement revision is no longer active and another agreement revision is now active.
- `TERMINATED` â The agreement ended before the defined end date because of an AWS termination (for example, a payment failure).