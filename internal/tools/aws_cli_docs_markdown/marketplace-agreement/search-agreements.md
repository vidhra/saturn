# search-agreementsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-agreement/search-agreements.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-agreement/search-agreements.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [marketplace-agreement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-agreement/index.html#cli-aws-marketplace-agreement) ]

# search-agreements

## Description

Searches across all agreements that a proposer or an acceptor has in AWS Marketplace. The search returns a list of agreements with basic agreement information.

The following filter combinations are supported:

- `PartyType` as `Proposer` + `AgreementType` + `ResourceIdentifier`
- `PartyType` as `Proposer` + `AgreementType` + `OfferId`
- `PartyType` as `Proposer` + `AgreementType` + `AcceptorAccountId`
- `PartyType` as `Proposer` + `AgreementType` + `Status`
- `PartyType` as `Proposer` + `AgreementType` + `ResourceIdentifier` + `Status`
- `PartyType` as `Proposer` + `AgreementType` + `OfferId` + `Status`
- `PartyType` as `Proposer` + `AgreementType` + `AcceptorAccountId` + `Status`
- `PartyType` as `Proposer` + `AgreementType` + `ResourceType` + `Status`
- `PartyType` as `Proposer` + `AgreementType` + `AcceptorAccountId` + `ResourceType` + `Status`
- `PartyType` as `Proposer` + `AgreementType` + `AcceptorAccountId` + `OfferId`
- `PartyType` as `Proposer` + `AgreementType` + `AcceptorAccountId` + `OfferId` + `Status`
- `PartyType` as `Proposer` + `AgreementType` + `AcceptorAccountId` + `ResourceIdentifier`
- `PartyType` as `Proposer` + `AgreementType` + `AcceptorAccountId` + `ResourceIdentifier` + `Status`
- `PartyType` as `Proposer` + `AgreementType` + `AcceptorAccountId` + `ResourceType`

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/marketplace-agreement-2020-03-01/SearchAgreements)

## Synopsis

```
search-agreements
[--catalog <value>]
[--filters <value>]
[--max-results <value>]
[--next-token <value>]
[--sort <value>]
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

The catalog in which the agreement was created.

`--filters` (list)

The filter name and value pair used to return a specific list of results.

The following filters are supported:

- `ResourceIdentifier` â The unique identifier of the resource.
- `ResourceType` â Type of the resource, which is the product (`AmiProduct` , `ContainerProduct` , or `SaaSProduct` ).
- `PartyType` â The party type (either `Acceptor` or `Proposer` ) of the caller. For agreements where the caller is the proposer, use the `Proposer` filter. For agreements where the caller is the acceptor, use the `Acceptor` filter.
- `AcceptorAccountId` â The AWS account ID of the party accepting the agreement terms.
- `OfferId` â The unique identifier of the offer in which the terms are registered in the agreement token.
- `Status` â The current status of the agreement. Values include `ACTIVE` , `ARCHIVED` , `CANCELLED` , `EXPIRED` , `RENEWED` , `REPLACED` , and `TERMINATED` .
- `BeforeEndTime` â A date used to filter agreements with a date before the `endTime` of an agreement.
- `AfterEndTime` â A date used to filter agreements with a date after the `endTime` of an agreement.
- `AgreementType` â The type of agreement. Values include `PurchaseAgreement` or `VendorInsightsAgreement` .

(structure)

The filter name and value pair that is used to return a more specific list of results. Filters can be used to match a set of resources by various criteria, such as `offerId` or `productId` .

name -> (string)

The name of the filter.

values -> (list)

The filter value.

(string)

Shorthand Syntax:

```
name=string,values=string,string ...
```

JSON Syntax:

```
[
  {
    "name": "string",
    "values": ["string", ...]
  }
  ...
]
```

`--max-results` (integer)

The maximum number of agreements to return in the response.

`--next-token` (string)

A token to specify where to start pagination.

`--sort` (structure)

An object that contains the `SortBy` and `SortOrder` attributes.

sortBy -> (string)

The attribute on which the data is grouped, which can be by `StartTime` and `EndTime` . The default value is `EndTime` .

sortOrder -> (string)

The sorting order, which can be `ASCENDING` or `DESCENDING` . The default value is `DESCENDING` .

Shorthand Syntax:

```
sortBy=string,sortOrder=string
```

JSON Syntax:

```
{
  "sortBy": "string",
  "sortOrder": "ASCENDING"|"DESCENDING"
}
```

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

agreementViewSummaries -> (list)

A summary of the agreement, including top-level attributes (for example, the agreement ID, version, proposer, and acceptor).

(structure)

A summary of the agreement, including top-level attributes (for example, the agreement ID, version, proposer, and acceptor).

acceptanceTime -> (timestamp)

The date and time that the agreement was accepted.

acceptor -> (structure)

Details of the party accepting the agreement terms. This is commonly the buyer for `PurchaseAgreement.`

accountId -> (string)

The AWS account ID of the acceptor.

agreementId -> (string)

The unique identifier of the agreement.

agreementType -> (string)

The type of agreement. Values are `PurchaseAgreement` or `VendorInsightsAgreement` .

endTime -> (timestamp)

The date and time when the agreement ends. The field is `null` for pay-as-you-go agreements, which donât have end dates.

proposalSummary -> (structure)

A summary of the proposal

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

Details of the party proposing the agreement terms, most commonly the seller for `PurchaseAgreement` .

accountId -> (string)

The AWS account ID of the proposer.

startTime -> (timestamp)

The date and time when the agreement starts.

status -> (string)

The current status of the agreement.

nextToken -> (string)

The token used for pagination. The field is `null` if there are no more results.