# get-functionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-function.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-function.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appsync](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/index.html#cli-aws-appsync) ]

# get-function

## Description

Get a `Function` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/GetFunction)

## Synopsis

```
get-function
--api-id <value>
--function-id <value>
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

`--api-id` (string)

The GraphQL API ID.

`--function-id` (string)

The `Function` ID.

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

functionConfiguration -> (structure)

The `Function` object.

functionId -> (string)

A unique ID representing the `Function` object.

functionArn -> (string)

The Amazon Resource Name (ARN) of the `Function` object.

name -> (string)

The name of the `Function` object.

description -> (string)

The `Function` description.

dataSourceName -> (string)

The name of the `DataSource` .

requestMappingTemplate -> (string)

The `Function` request mapping template. Functions support only the 2018-05-29 version of the request mapping template.

responseMappingTemplate -> (string)

The `Function` response mapping template.

functionVersion -> (string)

The version of the request mapping template. Currently, only the 2018-05-29 version of the template is supported.

syncConfig -> (structure)

Describes a Sync configuration for a resolver.

Specifies which Conflict Detection strategy and Resolution strategy to use when the resolver is invoked.

conflictHandler -> (string)

The Conflict Resolution strategy to perform in the event of a conflict.

- **OPTIMISTIC_CONCURRENCY** : Resolve conflicts by rejecting mutations when versions donât match the latest version at the server.
- **AUTOMERGE** : Resolve conflicts with the Automerge conflict resolution strategy.
- **LAMBDA** : Resolve conflicts with an Lambda function supplied in the `LambdaConflictHandlerConfig` .

conflictDetection -> (string)

The Conflict Detection strategy to use.

- **VERSION** : Detect conflicts based on object versions for this resolver.
- **NONE** : Do not detect conflicts when invoking this resolver.

lambdaConflictHandlerConfig -> (structure)

The `LambdaConflictHandlerConfig` when configuring `LAMBDA` as the Conflict Handler.

lambdaConflictHandlerArn -> (string)

The Amazon Resource Name (ARN) for the Lambda function to use as the Conflict Handler.

maxBatchSize -> (integer)

The maximum batching size for a resolver.

runtime -> (structure)

Describes a runtime used by an Amazon Web Services AppSync pipeline resolver or Amazon Web Services AppSync function. Specifies the name and version of the runtime to use. Note that if a runtime is specified, code must also be specified.

name -> (string)

The `name` of the runtime to use. Currently, the only allowed value is `APPSYNC_JS` .

runtimeVersion -> (string)

The `version` of the runtime to use. Currently, the only allowed version is `1.0.0` .

code -> (string)

The `function` code that contains the request and response functions. When code is used, the `runtime` is required. The `runtime` value must be `APPSYNC_JS` .