# list-membershipsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/list-memberships.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/list-memberships.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cleanrooms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/index.html#cli-aws-cleanrooms) ]

# list-memberships

## Description

Lists all memberships resources within the callerâs account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cleanrooms-2022-02-17/ListMemberships)

`list-memberships` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `membershipSummaries`

## Synopsis

```
list-memberships
[--status <value>]
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

`--status` (string)

A filter which will return only memberships in the specified status.

Possible values:

- `ACTIVE`
- `REMOVED`
- `COLLABORATION_DELETED`

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

The pagination token thatâs used to fetch the next set of results.

membershipSummaries -> (list)

The list of memberships returned from the ListMemberships operation.

(structure)

The membership object listed by the request.

id -> (string)

The unique ID for the membershipâs collaboration.

arn -> (string)

The unique ARN for the membership.

collaborationArn -> (string)

The unique ARN for the membershipâs associated collaboration.

collaborationId -> (string)

The unique ID for the membershipâs collaboration.

collaborationCreatorAccountId -> (string)

The identifier of the Amazon Web Services principal that created the collaboration. Currently only supports Amazon Web Services account ID.

collaborationCreatorDisplayName -> (string)

The display name of the collaboration creator.

collaborationName -> (string)

The name for the membershipâs collaboration.

createTime -> (timestamp)

The time when the membership was created.

updateTime -> (timestamp)

The time the membership metadata was last updated.

status -> (string)

The status of the membership.

memberAbilities -> (list)

The abilities granted to the collaboration member.

(string)

mlMemberAbilities -> (structure)

Provides a summary of the ML abilities for the collaboration member.

customMLMemberAbilities -> (list)

The custom ML member abilities for a collaboration member.

(string)

paymentConfiguration -> (structure)

The payment responsibilities accepted by the collaboration member.

queryCompute -> (structure)

The payment responsibilities accepted by the collaboration member for query compute costs.

isResponsible -> (boolean)

Indicates whether the collaboration member has accepted to pay for query compute costs (`TRUE` ) or has not accepted to pay for query compute costs (`FALSE` ).

If the collaboration creator has not specified anyone to pay for query compute costs, then the member who can query is the default payer.

An error message is returned for the following reasons:

- If you set the value to `FALSE` but you are responsible to pay for query compute costs.
- If you set the value to `TRUE` but you are not responsible to pay for query compute costs.

machineLearning -> (structure)

The payment responsibilities accepted by the collaboration member for machine learning costs.

modelTraining -> (structure)

The payment responsibilities accepted by the member for model training.

isResponsible -> (boolean)

Indicates whether the collaboration member has accepted to pay for model training costs (`TRUE` ) or has not accepted to pay for model training costs (`FALSE` ).

If the collaboration creator has not specified anyone to pay for model training costs, then the member who can query is the default payer.

An error message is returned for the following reasons:

- If you set the value to `FALSE` but you are responsible to pay for model training costs.
- If you set the value to `TRUE` but you are not responsible to pay for model training costs.

modelInference -> (structure)

The payment responsibilities accepted by the member for model inference.

isResponsible -> (boolean)

Indicates whether the collaboration member has accepted to pay for model inference costs (`TRUE` ) or has not accepted to pay for model inference costs (`FALSE` ).

If the collaboration creator has not specified anyone to pay for model inference costs, then the member who can query is the default payer.

An error message is returned for the following reasons:

- If you set the value to `FALSE` but you are responsible to pay for model inference costs.
- If you set the value to `TRUE` but you are not responsible to pay for model inference costs.

jobCompute -> (structure)

The payment responsibilities accepted by the collaboration member for job compute costs.

isResponsible -> (boolean)

Indicates whether the collaboration member has accepted to pay for job compute costs (`TRUE` ) or has not accepted to pay for query and job compute costs (`FALSE` ).

There is only one member who pays for queries and jobs.

An error message is returned for the following reasons:

- If you set the value to `FALSE` but you are responsible to pay for query and job compute costs.
- If you set the value to `TRUE` but you are not responsible to pay for query and job compute costs.