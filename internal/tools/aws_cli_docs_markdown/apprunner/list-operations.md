# list-operationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/list-operations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/list-operations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [apprunner](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/index.html#cli-aws-apprunner) ]

# list-operations

## Description

Return a list of operations that occurred on an App Runner service.

The resulting list of  OperationSummary objects is sorted in reverse chronological order. The first object on the list represents the last started operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/apprunner-2020-05-15/ListOperations)

## Synopsis

```
list-operations
--service-arn <value>
[--next-token <value>]
[--max-results <value>]
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

`--service-arn` (string)

The Amazon Resource Name (ARN) of the App Runner service that you want a list of operations for.

`--next-token` (string)

A token from a previous result page. Itâs used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones specified in the initial request.

If you donât specify `NextToken` , the request retrieves the first result page.

`--max-results` (integer)

The maximum number of results to include in each response (result page). Itâs used for a paginated request.

If you donât specify `MaxResults` , the request retrieves all available results in a single response.

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

**To list operations that occurred on a servicee**

The following `list-operations` example lists all operations that occurred on an App Runner service so far.
In this example, the service is new and only a single operation of type `CREATE_SERVICE` has occurred.

```
aws apprunner list-operations \
    --cli-input-json file://input.json
```

Contents of `input.json`:

```
{
    "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa"
}
```

Output:

```
{
    "OperationSummaryList": [
        {
            "EndedAt": 1606156217,
            "Id": "17fe9f55-7e91-4097-b243-fcabbb69a4cf",
            "StartedAt": 1606156014,
            "Status": "SUCCEEDED",
            "TargetArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa",
            "Type": "CREATE_SERVICE",
            "UpdatedAt": 1606156217
        }
    ]
}
```

## Output

OperationSummaryList -> (list)

A list of operation summary information records. In a paginated request, the request returns up to `MaxResults` records for each call.

(structure)

Provides summary information for an operation that occurred on an App Runner service.

Id -> (string)

A unique ID of this operation. Itâs unique in the scope of the App Runner service.

Type -> (string)

The type of operation. It indicates a specific action that occured.

Status -> (string)

The current state of the operation.

TargetArn -> (string)

The Amazon Resource Name (ARN) of the resource that the operation acted on (for example, an App Runner service).

StartedAt -> (timestamp)

The time when the operation started. Itâs in the Unix time stamp format.

EndedAt -> (timestamp)

The time when the operation ended. Itâs in the Unix time stamp format.

UpdatedAt -> (timestamp)

The time when the operation was last updated. Itâs in the Unix time stamp format.

NextToken -> (string)

The token that you can pass in a subsequent request to get the next result page. Itâs returned in a paginated request.