# list-eks-anywhere-subscriptionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/list-eks-anywhere-subscriptions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/list-eks-anywhere-subscriptions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [eks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/index.html#cli-aws-eks) ]

# list-eks-anywhere-subscriptions

## Description

Displays the full description of the subscription.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/ListEksAnywhereSubscriptions)

`list-eks-anywhere-subscriptions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `subscriptions`

## Synopsis

```
list-eks-anywhere-subscriptions
[--include-status <value>]
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

`--include-status` (list)

An array of subscription statuses to filter on.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  CREATING
  ACTIVE
  UPDATING
  EXPIRING
  EXPIRED
  DELETING
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

subscriptions -> (list)

A list of all subscription objects in the region, filtered by includeStatus and paginated by nextToken and maxResults.

(structure)

An EKS Anywhere subscription authorizing the customer to support for licensed clusters and access to EKS Anywhere Curated Packages.

id -> (string)

UUID identifying a subscription.

arn -> (string)

The Amazon Resource Name (ARN) for the subscription.

createdAt -> (timestamp)

The Unix timestamp in seconds for when the subscription was created.

effectiveDate -> (timestamp)

The Unix timestamp in seconds for when the subscription is effective.

expirationDate -> (timestamp)

The Unix timestamp in seconds for when the subscription will expire or auto renew, depending on the auto renew configuration of the subscription object.

licenseQuantity -> (integer)

The number of licenses included in a subscription. Valid values are between 1 and 100.

licenseType -> (string)

The type of licenses included in the subscription. Valid value is CLUSTER. With the CLUSTER license type, each license covers support for a single EKS Anywhere cluster.

term -> (structure)

An EksAnywhereSubscriptionTerm object.

duration -> (integer)

The duration of the subscription term. Valid values are 12 and 36, indicating a 12 month or 36 month subscription.

unit -> (string)

The term unit of the subscription. Valid value is `MONTHS` .

status -> (string)

The status of a subscription.

autoRenew -> (boolean)

A boolean indicating whether or not a subscription will auto renew when it expires.

licenseArns -> (list)

Amazon Web Services License Manager ARN associated with the subscription.

(string)

licenses -> (list)

Includes all of the claims in the license token necessary to validate the license for extended support.

(structure)

An EKS Anywhere license associated with a subscription.

id -> (string)

An id associated with an EKS Anywhere subscription license.

token -> (string)

An optional license token that can be used for extended support verification.

tags -> (map)

The metadata for a subscription to assist with categorization and organization. Each tag consists of a key and an optional value. Subscription tags do not propagate to any other resources associated with the subscription.

key -> (string)

One part of a key-value pair that make up a tag. A `key` is a general label that acts like a category for more specific tag values.

value -> (string)

The optional part of a key-value pair that make up a tag. A `value` acts as a descriptor within a tag category (key).

nextToken -> (string)

The nextToken value to include in a future ListEksAnywhereSubscriptions request. When the results of a ListEksAnywhereSubscriptions request exceed maxResults, you can use this value to retrieve the next page of results. This value is null when there are no more results to return.