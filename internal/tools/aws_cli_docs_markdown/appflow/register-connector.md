# register-connectorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/register-connector.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/register-connector.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appflow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/index.html#cli-aws-appflow) ]

# register-connector

## Description

Registers a new custom connector with your Amazon Web Services account. Before you can register the connector, you must deploy the associated AWS lambda function in your account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appflow-2020-08-23/RegisterConnector)

## Synopsis

```
register-connector
[--connector-label <value>]
[--description <value>]
[--connector-provisioning-type <value>]
[--connector-provisioning-config <value>]
[--client-token <value>]
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

`--connector-label` (string)

The name of the connector. The name is unique for each `ConnectorRegistration` in your Amazon Web Services account.

`--description` (string)

A description about the connector thatâs being registered.

`--connector-provisioning-type` (string)

The provisioning type of the connector. Currently the only supported value is LAMBDA.

Possible values:

- `LAMBDA`

`--connector-provisioning-config` (structure)

The provisioning type of the connector. Currently the only supported value is LAMBDA.

lambda -> (structure)

Contains information about the configuration of the lambda which is being registered as the connector.

lambdaArn -> (string)

Lambda ARN of the connector being registered.

Shorthand Syntax:

```
lambda={lambdaArn=string}
```

JSON Syntax:

```
{
  "lambda": {
    "lambdaArn": "string"
  }
}
```

`--client-token` (string)

The `clientToken` parameter is an idempotency token. It ensures that your `RegisterConnector` request completes only once. You choose the value to pass. For example, if you donât receive a response from your request, you can safely retry the request with the same `clientToken` parameter value.

If you omit a `clientToken` value, the Amazon Web Services SDK that you are using inserts a value for you. This way, the SDK can safely retry requests multiple times after a network error. You must provide your own value for other use cases.

If you specify input parameters that differ from your first request, an error occurs. If you use a different value for `clientToken` , Amazon AppFlow considers it a new call to `RegisterConnector` . The token is active for 8 hours.

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

## Output

connectorArn -> (string)

The ARN of the connector being registered.