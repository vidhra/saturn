# describe-create-account-statusÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-create-account-status.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-create-account-status.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [organizations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/index.html#cli-aws-organizations) ]

# describe-create-account-status

## Description

Retrieves the current status of an asynchronous request to create an account.

This operation can be called only from the organizationâs management account or by a member account that is a delegated administrator for an Amazon Web Services service.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/DescribeCreateAccountStatus)

## Synopsis

```
describe-create-account-status
--create-account-request-id <value>
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

`--create-account-request-id` (string)

Specifies the `Id` value that uniquely identifies the `CreateAccount` request. You can get the value from the `CreateAccountStatus.Id` response in an earlier  CreateAccount request, or from the  ListCreateAccountStatus operation.

The [regex pattern](http://wikipedia.org/wiki/regex) for a create account request ID string requires âcar-â followed by from 8 to 32 lowercase letters or digits.

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

**To get the latest status about a request to create an account**

The following example shows how to request the latest status for a previous request to create an account in an organization. The specified ârequest-id comes from the response of the original call to create-account. The account creation request shows by the status field that Organizations successfully completed the creation of the account.

Command:

```
aws organizations describe-create-account-status --create-account-request-id car-examplecreateaccountrequestid111
```

Output:

```
{
  "CreateAccountStatus": {
    "State": "SUCCEEDED",
    "AccountId": "555555555555",
    "AccountName": "Beta account",
    "RequestedTimestamp": 1470684478.687,
    "CompletedTimestamp": 1470684532.472,
    "Id": "car-examplecreateaccountrequestid111"
  }
}
```

## Output

CreateAccountStatus -> (structure)

A structure that contains the current status of an account creation request.

Id -> (string)

The unique identifier (ID) that references this request. You get this value from the response of the initial  CreateAccount request to create the account.

The [regex pattern](http://wikipedia.org/wiki/regex) for a create account request ID string requires âcar-â followed by from 8 to 32 lowercase letters or digits.

AccountName -> (string)

The account name given to the account when it was created.

State -> (string)

The status of the asynchronous request to create an Amazon Web Services account.

RequestedTimestamp -> (timestamp)

The date and time that the request was made for the account creation.

CompletedTimestamp -> (timestamp)

The date and time that the account was created and the request completed.

AccountId -> (string)

If the account was created successfully, the unique identifier (ID) of the new account.

The [regex pattern](http://wikipedia.org/wiki/regex) for an account ID string requires exactly 12 digits.

GovCloudAccountId -> (string)

If the account was created successfully, the unique identifier (ID) of the new account in the Amazon Web Services GovCloud (US) Region.

FailureReason -> (string)

If the request failed, a description of the reason for the failure.

- ACCOUNT_LIMIT_EXCEEDED: The account couldnât be created because you reached the limit on the number of accounts in your organization.
- CONCURRENT_ACCOUNT_MODIFICATION: You already submitted a request with the same information.
- EMAIL_ALREADY_EXISTS: The account could not be created because another Amazon Web Services account with that email address already exists.
- FAILED_BUSINESS_VALIDATION: The Amazon Web Services account that owns your organization failed to receive business license validation.
- GOVCLOUD_ACCOUNT_ALREADY_EXISTS: The account in the Amazon Web Services GovCloud (US) Region could not be created because this Region already includes an account with that email address.
- IDENTITY_INVALID_BUSINESS_VALIDATION: The Amazon Web Services account that owns your organization canât complete business license validation because it doesnât have valid identity data.
- INVALID_ADDRESS: The account could not be created because the address you provided is not valid.
- INVALID_EMAIL: The account could not be created because the email address you provided is not valid.
- INVALID_PAYMENT_INSTRUMENT: The Amazon Web Services account that owns your organization does not have a supported payment method associated with the account. Amazon Web Services does not support cards issued by financial institutions in Russia or Belarus. For more information, see [Managing your Amazon Web Services payments](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-general.html) .
- INTERNAL_FAILURE: The account could not be created because of an internal failure. Try again later. If the problem persists, contact Amazon Web Services Customer Support.
- MISSING_BUSINESS_VALIDATION: The Amazon Web Services account that owns your organization has not received Business Validation.
- MISSING_PAYMENT_INSTRUMENT: You must configure the management account with a valid payment method, such as a credit card.
- PENDING_BUSINESS_VALIDATION: The Amazon Web Services account that owns your organization is still in the process of completing business license validation.
- UNKNOWN_BUSINESS_VALIDATION: The Amazon Web Services account that owns your organization has an unknown issue with business license validation.