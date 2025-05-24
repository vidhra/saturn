# list-operationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/list-operations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/list-operations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53domains](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/index.html#cli-aws-route53domains) ]

# list-operations

## Description

Returns information about all of the operations that return an operation ID and that have ever been performed on domains that were registered by the current account.

This command runs only in the us-east-1 Region.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/ListOperations)

`list-operations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Operations`

## Synopsis

```
list-operations
[--submitted-since <value>]
[--max-items <value>]
[--status <value>]
[--type <value>]
[--sort-by <value>]
[--sort-order <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
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

`--submitted-since` (timestamp)

An optional parameter that lets you get information about all the operations that you submitted after a specified date and time. Specify the date and time in Unix time format and Coordinated Universal time (UTC).

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--status` (list)

The status of the operations.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  SUBMITTED
  IN_PROGRESS
  ERROR
  SUCCESSFUL
  FAILED
```

`--type` (list)

An arrays of the domains operation types.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  REGISTER_DOMAIN
  DELETE_DOMAIN
  TRANSFER_IN_DOMAIN
  UPDATE_DOMAIN_CONTACT
  UPDATE_NAMESERVER
  CHANGE_PRIVACY_PROTECTION
  DOMAIN_LOCK
  ENABLE_AUTORENEW
  DISABLE_AUTORENEW
  ADD_DNSSEC
  REMOVE_DNSSEC
  EXPIRE_DOMAIN
  TRANSFER_OUT_DOMAIN
  CHANGE_DOMAIN_OWNER
  RENEW_DOMAIN
  PUSH_DOMAIN
  INTERNAL_TRANSFER_OUT_DOMAIN
  INTERNAL_TRANSFER_IN_DOMAIN
  RELEASE_TO_GANDI
  TRANSFER_ON_RENEW
  RESTORE_DOMAIN
```

`--sort-by` (string)

The sort type for returned values.

Possible values:

- `SubmittedDate`

`--sort-order` (string)

The sort order for returned values, either ascending or descending.

Possible values:

- `ASC`
- `DESC`

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

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

**To list the status of operations that return an operation ID**

Some domain registration operations run asynchronously and return a response before they finish. These operations return an operation ID that you can use to get the current status. The following `list-operations` command lists summary information, including the status, about the current domain-registration operations.

This command runs only in the `us-east-1` Region. If your default region is set to `us-east-1`, you can omit the `region` parameter.

```
aws route53domains list-operations
    --region us-east-1
```

Output:

```
{
    "Operations": [
        {
            "OperationId": "aab9822f-1da0-4bf3-8a15-fd4e0example",
            "Status": "SUCCESSFUL",
            "Type": "DOMAIN_LOCK",
            "SubmittedDate": 1455321739.986
        },
        {
            "OperationId": "c24379ed-76be-42f8-bdad-9379bexample",
            "Status": "SUCCESSFUL",
            "Type": "UPDATE_NAMESERVER",
            "SubmittedDate": 1468960475.109
        },
        {
            "OperationId": "f47e1297-ef9e-4c2b-ae1e-a5fcbexample",
            "Status": "SUCCESSFUL",
            "Type": "RENEW_DOMAIN",
            "SubmittedDate": 1473561835.943
        },
        {
            "OperationId": "75584f23-b15f-459e-aed7-dc6f5example",
            "Status": "SUCCESSFUL",
            "Type": "UPDATE_DOMAIN_CONTACT",
            "SubmittedDate": 1547501003.41
        }
    ]
}
```

The output includes all the operations that return an operation ID and that you have performed on all the domains that you have ever registered using the current AWS account. If you want to get only the operations that you submitted after a specified date, you can include the `submitted-since` parameter and specify a date in Unix format and Coordinated Universal Time (UTC). The following command gets the status of all operations that were submitted after 12:00 am UTC on January 1, 2020.

```
aws route53domains list-operations \
    --submitted-since 1577836800
```

## Output

Operations -> (list)

Lists summaries of the operations.

(structure)

OperationSummary includes the following elements.

OperationId -> (string)

Identifier returned to track the requested action.

Status -> (string)

The current status of the requested operation in the system.

Type -> (string)

Type of the action requested.

SubmittedDate -> (timestamp)

The date when the request was submitted.

DomainName -> (string)

Name of the domain.

Message -> (string)

Message about the operation.

StatusFlag -> (string)

Automatically checks whether there are no outstanding operations on domains that need customer attention.

Valid values are:

- `PENDING_ACCEPTANCE` : The operation is waiting for acceptance from the account that is receiving the domain.
- `PENDING_CUSTOMER_ACTION` : The operation is waiting for customer action, for example, returning an email.
- `PENDING_AUTHORIZATION` : The operation is waiting for the form of authorization. For more information, see [ResendOperationAuthorization](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ResendOperationAuthorization.html) .
- `PENDING_PAYMENT_VERIFICATION` : The operation is waiting for the payment method to validate.
- `PENDING_SUPPORT_CASE` : The operation includes a support case and is waiting for its resolution.

LastUpdatedDate -> (timestamp)

The date when the last change was made in Unix time format and Coordinated Universal Time (UTC).

NextPageMarker -> (string)

If there are more operations than you specified for `MaxItems` in the request, submit another request and include the value of `NextPageMarker` in the value of `Marker` .