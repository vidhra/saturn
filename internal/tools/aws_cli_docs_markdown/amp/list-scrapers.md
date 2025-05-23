# list-scrapersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amp/list-scrapers.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amp/list-scrapers.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [amp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amp/index.html#cli-aws-amp) ]

# list-scrapers

## Description

The `ListScrapers` operation lists all of the scrapers in your account. This includes scrapers being created or deleted. You can optionally filter the returned list.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/amp-2020-08-01/ListScrapers)

`list-scrapers` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `scrapers`

## Synopsis

```
list-scrapers
[--filters <value>]
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

`--filters` (map)

(Optional) A list of key-value pairs to filter the list of scrapers returned. Keys include `status` , `sourceArn` , `destinationArn` , and `alias` .

Filters on the same key are `OR` âd together, and filters on different keys are `AND` âd together. For example, `status=ACTIVE&status=CREATING&alias=Test` , will return all scrapers that have the alias Test, and are either in status ACTIVE or CREATING.

To find all active scrapers that are sending metrics to a specific Amazon Managed Service for Prometheus workspace, you would use the ARN of the workspace in a query:

`status=ACTIVE&destinationArn=arn:aws:aps:us-east-1:123456789012:workspace/ws-example1-1234-abcd-56ef-123456789012`

If this is included, it filters the results to only the scrapers that match the filter.

key -> (string)

The name of the key to filter by. Currently supported filter keys are `status` , `sourceArn` , `destinationArn` , and `alias` .

value -> (list)

The values of the given key by which to filter.

(string)

The value for a given key by which to filter.

Shorthand Syntax:

```
KeyName1=string,string,KeyName2=string,string
```

JSON Syntax:

```
{"string": ["string", ...]
  ...}
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

nextToken -> (string)

A token indicating that there are more results to retrieve. You can use this token as part of your next `ListScrapers` operation to retrieve those results.

scrapers -> (list)

A list of `ScraperSummary` structures giving information about scrapers in the account that match the filters provided.

(structure)

The `ScraperSummary` structure contains a summary of the details about one scraper in your account.

alias -> (string)

(Optional) A name associated with the scraper.

arn -> (string)

The Amazon Resource Name (ARN) of the scraper.

createdAt -> (timestamp)

The date and time that the scraper was created.

destination -> (tagged union structure)

The Amazon Managed Service for Prometheus workspace the scraper sends metrics to.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `ampConfiguration`.

ampConfiguration -> (structure)

The Amazon Managed Service for Prometheus workspace to send metrics to.

workspaceArn -> (string)

ARN of the Amazon Managed Service for Prometheus workspace.

lastModifiedAt -> (timestamp)

The date and time that the scraper was last modified.

roleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role that provides permissions for the scraper to discover and collect metrics on your behalf.

roleConfiguration -> (structure)

This structure displays information about the IAM roles used for cross-account scraping configuration.

sourceRoleArn -> (string)

The Amazon Resource Name (ARN) of the role used in the source account to enable cross-account scraping. For information about the contents of this policy, see [Cross-account setup](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#cross-account-remote-write) .

targetRoleArn -> (string)

The Amazon Resource Name (ARN) of the role used in the target account to enable cross-account scraping. For information about the contents of this policy, see [Cross-account setup](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#cross-account-remote-write) .

scraperId -> (string)

The ID of the scraper.

source -> (tagged union structure)

The Amazon EKS cluster from which the scraper collects metrics.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `eksConfiguration`.

eksConfiguration -> (structure)

The Amazon EKS cluster from which a scraper collects metrics.

clusterArn -> (string)

ARN of the Amazon EKS cluster.

securityGroupIds -> (list)

A list of the security group IDs for the Amazon EKS cluster VPC configuration.

(string)

ID of a VPC security group.

subnetIds -> (list)

A list of subnet IDs for the Amazon EKS cluster VPC configuration.

(string)

ID of a VPC subnet.

status -> (structure)

A structure that contains the current status of the scraper.

statusCode -> (string)

The current status of the scraper.

statusReason -> (string)

If there is a failure, the reason for the failure.

tags -> (map)

(Optional) The list of tag keys and values associated with the scraper.

key -> (string)

The key of the tag. Must not begin with `aws:` .

value -> (string)

The value of the tag.