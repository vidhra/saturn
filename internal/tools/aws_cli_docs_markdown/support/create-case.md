# create-caseÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/create-case.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/create-case.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [support](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/index.html#cli-aws-support) ]

# create-case

## Description

Creates a case in the Amazon Web Services Support Center. This operation is similar to how you create a case in the Amazon Web Services Support Center [Create Case](https://console.aws.amazon.com/support/home#/case/create) page.

The Amazon Web Services Support API doesnât support requesting service limit increases. You can submit a service limit increase in the following ways:

- Submit a request from the Amazon Web Services Support Center [Create Case](https://console.aws.amazon.com/support/home#/case/create) page.
- Use the Service Quotas [RequestServiceQuotaIncrease](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_RequestServiceQuotaIncrease.html) operation.

A successful `CreateCase` request returns an Amazon Web Services Support case number. You can use the  DescribeCases operation and specify the case number to get existing Amazon Web Services Support cases. After you create a case, use the  AddCommunicationToCase operation to add additional communication or attachments to an existing case.

The `caseId` is separate from the `displayId` that appears in the [Amazon Web Services Support Center](https://console.aws.amazon.com/support) . Use the  DescribeCases operation to get the `displayId` .

### Note

- You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API.
- If you call the Amazon Web Services Support API from an account that doesnât have a Business, Enterprise On-Ramp, or Enterprise Support plan, the `SubscriptionRequiredException` error message appears. For information about changing your support plan, see [Amazon Web Services Support](http://aws.amazon.com/premiumsupport/) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/CreateCase)

## Synopsis

```
create-case
--subject <value>
[--service-code <value>]
[--severity-code <value>]
[--category-code <value>]
--communication-body <value>
[--cc-email-addresses <value>]
[--language <value>]
[--issue-type <value>]
[--attachment-set-id <value>]
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

`--subject` (string)

The title of the support case. The title appears in the **Subject** field on the Amazon Web Services Support Center [Create Case](https://console.aws.amazon.com/support/home#/case/create) page.

`--service-code` (string)

The code for the Amazon Web Services service. You can use the  DescribeServices operation to get the possible `serviceCode` values.

`--severity-code` (string)

A value that indicates the urgency of the case. This value determines the response time according to your service level agreement with Amazon Web Services Support. You can use the  DescribeSeverityLevels operation to get the possible values for `severityCode` .

For more information, see  SeverityLevel and [Choosing a Severity](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html#choosing-severity) in the *Amazon Web Services Support User Guide* .

### Note

The availability of severity levels depends on the support plan for the Amazon Web Services account.

`--category-code` (string)

The category of problem for the support case. You also use the  DescribeServices operation to get the category code for a service. Each Amazon Web Services service defines its own set of category codes.

`--communication-body` (string)

The communication body text that describes the issue. This text appears in the **Description** field on the Amazon Web Services Support Center [Create Case](https://console.aws.amazon.com/support/home#/case/create) page.

`--cc-email-addresses` (list)

A list of email addresses that Amazon Web Services Support copies on case correspondence. Amazon Web Services Support identifies the account that creates the case when you specify your Amazon Web Services credentials in an HTTP POST method or use the [Amazon Web Services SDKs](http://aws.amazon.com/tools/) .

(string)

Syntax:

```
"string" "string" ...
```

`--language` (string)

The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (âzhâ), English (âenâ), Japanese (âjaâ) and Korean (âkoâ). You must specify the ISO 639-1 code for the `language` parameter if you want support in that language.

`--issue-type` (string)

The type of issue for the case. You can specify `customer-service` or `technical` . If you donât specify a value, the default is `technical` .

`--attachment-set-id` (string)

The ID of a set of one or more attachments for the case. Create the set by using the  AddAttachmentsToSet operation.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a case**

The following `create-case` example creates a support case for your AWS account.

```
aws support create-case \
    --category-code "using-aws" \
    --cc-email-addresses "myemail@example.com" \
    --communication-body "I want to learn more about an AWS service." \
    --issue-type "technical" \
    --language "en" \
    --service-code "general-info" \
    --severity-code "low" \
    --subject "Question about my account"
```

Output:

```
{
    "caseId": "case-12345678910-2013-c4c1d2bf33c5cf47"
}
```

For more information, see [Case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html) in the *AWS Support User Guide*.

## Output

caseId -> (string)

The support case ID requested or returned in the call. The case ID is an alphanumeric string in the following format: case-*12345678910-2013-c4c1d2bf33c5cf47*