# describe-casesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-cases.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-cases.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [support](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/index.html#cli-aws-support) ]

# describe-cases

## Description

Returns a list of cases that you specify by passing one or more case IDs. You can use the `afterTime` and `beforeTime` parameters to filter the cases by date. You can set values for the `includeResolvedCases` and `includeCommunications` parameters to specify how much information to return.

The response returns the following in JSON format:

- One or more [CaseDetails](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_CaseDetails.html) data types.
- One or more `nextToken` values, which specify where to paginate the returned records represented by the `CaseDetails` objects.

Case data is available for 12 months after creation. If a case was created more than 12 months ago, a request might return an error.

### Note

- You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API.
- If you call the Amazon Web Services Support API from an account that doesnât have a Business, Enterprise On-Ramp, or Enterprise Support plan, the `SubscriptionRequiredException` error message appears. For information about changing your support plan, see [Amazon Web Services Support](http://aws.amazon.com/premiumsupport/) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeCases)

`describe-cases` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `cases`

## Synopsis

```
describe-cases
[--case-id-list <value>]
[--display-id <value>]
[--after-time <value>]
[--before-time <value>]
[--include-resolved-cases | --no-include-resolved-cases]
[--language <value>]
[--include-communications | --no-include-communications]
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

`--case-id-list` (list)

A list of ID numbers of the support cases you want returned. The maximum number of cases is 100.

(string)

Syntax:

```
"string" "string" ...
```

`--display-id` (string)

The ID displayed for a case in the Amazon Web Services Support Center user interface.

`--after-time` (string)

The start date for a filtered date search on support case communications. Case communications are available for 12 months after creation.

`--before-time` (string)

The end date for a filtered date search on support case communications. Case communications are available for 12 months after creation.

`--include-resolved-cases` | `--no-include-resolved-cases` (boolean)

Specifies whether to include resolved support cases in the `DescribeCases` response. By default, resolved cases arenât included.

`--language` (string)

The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (âzhâ), English (âenâ), Japanese (âjaâ) and Korean (âkoâ). You must specify the ISO 639-1 code for the `language` parameter if you want support in that language.

`--include-communications` | `--no-include-communications` (boolean)

Specifies whether to include communications in the `DescribeCases` response. By default, communications are included.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To describe a case**

The following `describe-cases` example returns information about the specified support case in your AWS account.

```
aws support describe-cases \
    --display-id "1234567890" \
    --after-time "2020-03-23T21:31:47.774Z" \
    --include-resolved-cases \
    --language "en" \
    --no-include-communications \
    --max-item 1
```

Output:

```
{
    "cases": [
        {
            "status": "resolved",
            "ccEmailAddresses": [],
            "timeCreated": "2020-03-23T21:31:47.774Z",
            "caseId": "case-12345678910-2013-c4c1d2bf33c5cf47",
            "severityCode": "low",
            "language": "en",
            "categoryCode": "using-aws",
            "serviceCode": "general-info",
            "submittedBy": "myemail@example.com",
            "displayId": "1234567890",
            "subject": "Question about my account"
        }
    ]
}
```

For more information, see [Case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html) in the *AWS Support User Guide*.

## Output

cases -> (list)

The details for the cases that match the request.

(structure)

A JSON-formatted object that contains the metadata for a support case. It is contained in the response from a  DescribeCases request. **CaseDetails** contains the following fields:

- **caseId** - The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47* .
- **categoryCode** - The category of problem for the support case. Corresponds to the `CategoryCode` values returned by a call to  DescribeServices .
- **displayId** - The identifier for the case on pages in the Amazon Web Services Support Center.
- **language** - The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (âzhâ), English (âenâ), Japanese (âjaâ) and Korean (âkoâ). You must specify the ISO 639-1 code for the `language` parameter if you want support in that language.
- **nextToken** - A resumption point for pagination.
- **recentCommunications** - One or more  Communication objects. Fields of these objects are `attachments` , `body` , `caseId` , `submittedBy` , and `timeCreated` .
- **serviceCode** - The identifier for the Amazon Web Services service that corresponds to the service code defined in the call to  DescribeServices .
- **severityCode** - The severity code assigned to the case. Contains one of the values returned by the call to  DescribeSeverityLevels . The possible values are: `low` , `normal` , `high` , `urgent` , and `critical` .
- **status** - The status of the case in the Amazon Web Services Support Center. Valid values:
- `all-open`
- `customer-action-completed`
- `opened`
- `pending-customer-action`
- `reopened`
- `resolved`
- `unassigned`
- `work-in-progress`
- **subject** - The subject line of the case.
- **submittedBy** - The email address of the account that submitted the case.
- **timeCreated** - The time the case was created, in ISO-8601 format.

caseId -> (string)

The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47*

displayId -> (string)

The ID displayed for the case in the Amazon Web Services Support Center. This is a numeric string.

subject -> (string)

The subject line for the case in the Amazon Web Services Support Center.

status -> (string)

The status of the case.

Valid values:

- `all-open`
- `customer-action-completed`
- `opened`
- `pending-customer-action`
- `reopened`
- `resolved`
- `unassigned`
- `work-in-progress`

serviceCode -> (string)

The code for the Amazon Web Services service. You can get a list of codes and the corresponding service names by calling  DescribeServices .

categoryCode -> (string)

The category of problem for the support case.

severityCode -> (string)

The code for the severity level returned by the call to  DescribeSeverityLevels .

submittedBy -> (string)

The email address of the account that submitted the case.

timeCreated -> (string)

The time that the case was created in the Amazon Web Services Support Center.

recentCommunications -> (structure)

The five most recent communications between you and Amazon Web Services Support Center, including the IDs of any attachments to the communications. Also includes a `nextToken` that you can use to retrieve earlier communications.

communications -> (list)

The five most recent communications associated with the case.

(structure)

A communication associated with a support case. The communication consists of the case ID, the message body, attachment information, the submitter of the communication, and the date and time of the communication.

caseId -> (string)

The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47*

body -> (string)

The text of the communication between the customer and Amazon Web Services Support.

submittedBy -> (string)

The identity of the account that submitted, or responded to, the support case. Customer entries include the IAM role as well as the email address (for example, âAdminRole (Role) <[janedoe@example.com](mailto:janedoe%40example.com)>). Entries from the Amazon Web Services Support team display âAmazon Web Services,â and donât show an email address.

timeCreated -> (string)

The time the communication was created.

attachmentSet -> (list)

Information about the attachments to the case communication.

(structure)

The file name and ID of an attachment to a case communication. You can use the ID to retrieve the attachment with the  DescribeAttachment operation.

attachmentId -> (string)

The ID of the attachment.

fileName -> (string)

The file name of the attachment.

nextToken -> (string)

A resumption point for pagination.

ccEmailAddresses -> (list)

The email addresses that receive copies of communication about the case.

(string)

language -> (string)

The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (âzhâ), English (âenâ), Japanese (âjaâ) and Korean (âkoâ). You must specify the ISO 639-1 code for the `language` parameter if you want support in that language.

nextToken -> (string)

A resumption point for pagination.