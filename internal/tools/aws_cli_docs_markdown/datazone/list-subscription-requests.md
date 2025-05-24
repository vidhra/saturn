# list-subscription-requestsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/list-subscription-requests.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/list-subscription-requests.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [datazone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/index.html#cli-aws-datazone) ]

# list-subscription-requests

## Description

Lists Amazon DataZone subscription requests.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/datazone-2018-05-10/ListSubscriptionRequests)

`list-subscription-requests` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `items`

## Synopsis

```
list-subscription-requests
[--approver-project-id <value>]
--domain-identifier <value>
[--owning-project-id <value>]
[--sort-by <value>]
[--sort-order <value>]
[--status <value>]
[--subscribed-listing-id <value>]
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

`--approver-project-id` (string)

The identifier of the subscription request approverâs project.

`--domain-identifier` (string)

The identifier of the Amazon DataZone domain.

`--owning-project-id` (string)

The identifier of the project for the subscription requests.

`--sort-by` (string)

Specifies the way to sort the results of this action.

Possible values:

- `CREATED_AT`
- `UPDATED_AT`

`--sort-order` (string)

Specifies the sort order for the results of this action.

Possible values:

- `ASCENDING`
- `DESCENDING`

`--status` (string)

Specifies the status of the subscription requests.

### Note

This is not a required parameter, but if not specified, by default, Amazon DataZone returns only `PENDING` subscription requests.

Possible values:

- `PENDING`
- `ACCEPTED`
- `REJECTED`

`--subscribed-listing-id` (string)

The identifier of the subscribed listing.

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

items -> (list)

The results of the `ListSubscriptionRequests` action.

(structure)

The details of the subscription request.

createdAt -> (timestamp)

The timestamp of when a subscription request was created.

createdBy -> (string)

The Amazon DataZone user who created the subscription request.

decisionComment -> (string)

The decision comment of the subscription request.

domainId -> (string)

The identifier of the Amazon DataZone domain in which a subscription request exists.

existingSubscriptionId -> (string)

The ID of the existing subscription.

id -> (string)

The identifier of the subscription request.

metadataFormsSummary -> (list)

The summary of the metadata forms.

(structure)

The summary of the metadata form.

formName -> (string)

The form name of the metadata form.

typeName -> (string)

The type name of the metadata form.

typeRevision -> (string)

The type revision of the metadata form.

requestReason -> (string)

The reason for the subscription request.

reviewerId -> (string)

The identifier of the subscription request reviewer.

status -> (string)

The status of the subscription request.

subscribedListings -> (list)

The listings included in the subscription request.

(structure)

The details of the published asset for which the subscription grant is created.

description -> (string)

The description of the published asset for which the subscription grant is created.

id -> (string)

The identifier of the published asset for which the subscription grant is created.

item -> (tagged union structure)

The published asset for which the subscription grant is created.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `assetListing`, `productListing`.

assetListing -> (structure)

The asset for which the subscription grant is created.

assetScope -> (structure)

The asset scope of the subscribed asset listing.

assetId -> (string)

The asset ID of the asset scope.

errorMessage -> (string)

The error message of the asset scope.

filterIds -> (list)

The filter IDs of the asset scope.

(string)

status -> (string)

The status of the asset scope.

entityId -> (string)

The identifier of the published asset for which the subscription grant is created.

entityRevision -> (string)

The revision of the published asset for which the subscription grant is created.

entityType -> (string)

The type of the published asset for which the subscription grant is created.

forms -> (string)

The forms attached to the published asset for which the subscription grant is created.

glossaryTerms -> (list)

The glossary terms attached to the published asset for which the subscription grant is created.

(structure)

Details of a glossary term attached to the inventory asset.

name -> (string)

The name of a glossary term attached to the inventory asset.

shortDescription -> (string)

The shoft description of a glossary term attached to the inventory asset.

productListing -> (structure)

The data product listing.

assetListings -> (list)

The data assets of the data product listing.

(structure)

The listing of the asset in a data product.

entityId -> (string)

The entity ID of the listing of the asset in a data product.

entityRevision -> (string)

The entity revision of the listing of the asset in a data product.

entityType -> (string)

The entity type of the listing of the asset in a data product.

description -> (string)

The description of the data product listing.

entityId -> (string)

The ID of the data product listing.

entityRevision -> (string)

The revision of the data product listing.

glossaryTerms -> (list)

The glossary terms of the data product listing.

(structure)

Details of a glossary term attached to the inventory asset.

name -> (string)

The name of a glossary term attached to the inventory asset.

shortDescription -> (string)

The shoft description of a glossary term attached to the inventory asset.

name -> (string)

The name of the data product listing.

name -> (string)

The name of the published asset for which the subscription grant is created.

ownerProjectId -> (string)

The identifier of the project of the published asset for which the subscription grant is created.

ownerProjectName -> (string)

The name of the project that owns the published asset for which the subscription grant is created.

revision -> (string)

The revision of the published asset for which the subscription grant is created.

subscribedPrincipals -> (list)

The principals included in the subscription request.

(tagged union structure)

The principal that has the subscription grant for the asset.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `project`.

project -> (structure)

The project that has the subscription grant.

id -> (string)

The identifier of the project that has the subscription grant.

name -> (string)

The name of the project that has the subscription grant.

updatedAt -> (timestamp)

The timestamp of when the subscription request was updated.

updatedBy -> (string)

The identifier of the Amazon DataZone user who updated the subscription request.

nextToken -> (string)

When the number of subscription requests is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of subscription requests, the response includes a pagination token named `NextToken` . You can specify this `NextToken` value in a subsequent call to `ListSubscriptionRequests` to list the next set of subscription requests.