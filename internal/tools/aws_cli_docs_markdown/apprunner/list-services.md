# list-servicesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/list-services.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/list-services.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [apprunner](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/index.html#cli-aws-apprunner) ]

# list-services

## Description

Returns a list of running App Runner services in your Amazon Web Services account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/apprunner-2020-05-15/ListServices)

## Synopsis

```
list-services
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

`--next-token` (string)

A token from a previous result page. Used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones specified in the initial request.

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

**To get a paginated listing of App Runner services**

The following `list-services` example lists all App Runner services in the AWS account. Up to two services are listed in each response.
This example shows the first request. The response includes two results and a token that can be used in the next request.
When a subsequent response doesnât include a token, all services have been listed.

```
aws apprunner list-services \
    --cli-input-json file://input.json
```

Contents of `input.json`:

```
{
    "MaxResults": 2
}
```

Output:

```
{
    "NextToken": "eyJDdXN0b21lckFjY291bnRJZCI6IjI3MDIwNTQwMjg0NSIsIlNlcnZpY2VTdGF0dXNDb2RlIjoiUFJPVklTSU9OSU5HIiwiSGFzaEtleSI6IjI3MDIwNTQwMjg0NSNhYjhmOTRjZmUyOWE0NjBmYjg3NjBhZmQyZWU4NzU1NSJ9",
    "ServiceSummaryList": [
        {
            "CreatedAt": "2020-11-20T19:05:25Z",
            "UpdatedAt": "2020-11-23T12:41:37Z",
            "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa",
            "ServiceId": "8fe1e10304f84fd2b0df550fe98a71fa",
            "ServiceName": "python-app",
            "ServiceUrl": "psbqam834h.us-east-1.awsapprunner.com",
            "Status": "RUNNING"
        },
        {
            "CreatedAt": "2020-11-06T23:15:30Z",
            "UpdatedAt": "2020-11-23T13:21:22Z",
            "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/golang-container-app/ab8f94cfe29a460fb8760afd2ee87555",
            "ServiceId": "ab8f94cfe29a460fb8760afd2ee87555",
            "ServiceName": "golang-container-app",
            "ServiceUrl": "e2m8rrrx33.us-east-1.awsapprunner.com",
            "Status": "RUNNING"
        }
    ]
}
```

## Output

ServiceSummaryList -> (list)

A list of service summary information records. In a paginated request, the request returns up to `MaxResults` records for each call.

(structure)

Provides summary information for an App Runner service.

This type contains limited information about a service. It doesnât include configuration details. Itâs returned by the [ListServices](https://docs.aws.amazon.com/apprunner/latest/api/API_ListServices.html) action. Complete service information is returned by the [CreateService](https://docs.aws.amazon.com/apprunner/latest/api/API_CreateService.html) , [DescribeService](https://docs.aws.amazon.com/apprunner/latest/api/API_DescribeService.html) , and [DeleteService](https://docs.aws.amazon.com/apprunner/latest/api/API_DeleteService.html) actions using the [Service](https://docs.aws.amazon.com/apprunner/latest/api/API_Service.html) type.

ServiceName -> (string)

The customer-provided service name.

ServiceId -> (string)

An ID that App Runner generated for this service. Itâs unique within the Amazon Web Services Region.

ServiceArn -> (string)

The Amazon Resource Name (ARN) of this service.

ServiceUrl -> (string)

A subdomain URL that App Runner generated for this service. You can use this URL to access your service web application.

CreatedAt -> (timestamp)

The time when the App Runner service was created. Itâs in the Unix time stamp format.

UpdatedAt -> (timestamp)

The time when the App Runner service was last updated. Itâs in theUnix time stamp format.

Status -> (string)

The current state of the App Runner service. These particular values mean the following.

- `CREATE_FAILED` â The service failed to create. The failed service isnât usable, and still counts towards your service quota. To troubleshoot this failure, read the failure events and logs, change any parameters that need to be fixed, and rebuild your service using `UpdateService` .
- `DELETE_FAILED` â The service failed to delete and canât be successfully recovered. Retry the service deletion call to ensure that all related resources are removed.

NextToken -> (string)

The token that you can pass in a subsequent request to get the next result page. Itâs returned in a paginated request.