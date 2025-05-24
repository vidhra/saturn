# update-stageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-stage.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-stage.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [apigateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/index.html#cli-aws-apigateway) ]

# update-stage

## Description

Changes information about a Stage resource.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateStage)

## Synopsis

```
update-stage
--rest-api-id <value>
--stage-name <value>
[--patch-operations <value>]
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

`--rest-api-id` (string)

The string identifier of the associated RestApi.

`--stage-name` (string)

The name of the Stage resource to change information about.

`--patch-operations` (list)

For more information about supported patch operations, see [Patch Operations](https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html) .

(structure)

For more information about supported patch operations, see [Patch Operations](https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html) .

op -> (string)

An update operation to be performed with this PATCH request. The valid value can be add, remove, replace or copy. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message..

path -> (string)

The op operationâs target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {ânameâ:âvalueâ}, the path for this property is /name. If the name property value is a JSON object (e.g., {ânameâ: {âchild/nameâ: âchild-valueâ}}), the path for the child/name property will be /name/child~1name. Any slash (â/â) character appearing in path names must be escaped with â~1â, as shown in the example above. Each op operation can have only one path associated with it.

value -> (string)

The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., â{âaâ: â¦}â.

from -> (string)

The copy update operationâs source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with âopâ:âcopyâ, âfromâ:â/canarySettings/deploymentIdâ and âpathâ:â/deploymentIdâ.

Shorthand Syntax:

```
op=string,path=string,value=string,from=string ...
```

JSON Syntax:

```
[
  {
    "op": "add"|"remove"|"replace"|"move"|"copy"|"test",
    "path": "string",
    "value": "string",
    "from": "string"
  }
  ...
]
```

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

**Example 1: To override the stage settings for a resource and method**

The following `update-stage` example overrides the stage settings and turns off full request/response logging for a specific resource and method.

```
aws apigateway update-stage \
    --rest-api-id 1234123412 \
    --stage-name 'dev' \
    --patch-operations op=replace,path=/~1resourceName/GET/logging/dataTrace,value=false
```

Output:

```
{
    "deploymentId": "5ubd17",
    "stageName": "dev",
    "cacheClusterEnabled": false,
    "cacheClusterStatus": "NOT_AVAILABLE",
    "methodSettings": {
        "~1resourceName/GET": {
            "metricsEnabled": false,
            "dataTraceEnabled": false,
            "throttlingBurstLimit": 5000,
            "throttlingRateLimit": 10000.0,
            "cachingEnabled": false,
            "cacheTtlInSeconds": 300,
            "cacheDataEncrypted": false,
            "requireAuthorizationForCacheControl": true,
            "unauthorizedCacheControlHeaderStrategy": "SUCCEED_WITH_RESPONSE_HEADER"
        }
    },
    "tracingEnabled": false,
    "createdDate": "2022-07-18T10:11:18-07:00",
    "lastUpdatedDate": "2022-07-18T10:19:04-07:00"
}
```

For more information, see [Setting up a stage for a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-stages.html) in the *Amazon API Gateway Developer Guide*.

**Example 2: To update the stage settings for all resources and methods of an API stage**

The following `update-stage` example turns on full request/response logging for all resources and methods of an API stage.

```
aws apigateway update-stage \
    --rest-api-id 1234123412 \
    --stage-name 'dev' \
    --patch-operations 'op=replace,path=/*/*/logging/dataTrace,value=true'
```

Output:

```
{
    "deploymentId": "5ubd17",
    "stageName": "dev",
    "cacheClusterEnabled": false,
    "cacheClusterStatus": "NOT_AVAILABLE",
    "methodSettings": {
        "*/*": {
            "metricsEnabled": false,
            "dataTraceEnabled": true,
            "throttlingBurstLimit": 5000,
            "throttlingRateLimit": 10000.0,
            "cachingEnabled": false,
            "cacheTtlInSeconds": 300,
            "cacheDataEncrypted": false,
            "requireAuthorizationForCacheControl": true,
            "unauthorizedCacheControlHeaderStrategy": "SUCCEED_WITH_RESPONSE_HEADER"
        }
    },
    "tracingEnabled": false,
    "createdDate": "2022-07-18T10:11:18-07:00",
    "lastUpdatedDate": "2022-07-18T10:31:04-07:00"
}
```

For more information, see [Setting up a stage for a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-stages.html) in the *Amazon API Gateway Developer Guide*.

## Output

deploymentId -> (string)

The identifier of the Deployment that the stage points to.

clientCertificateId -> (string)

The identifier of a client certificate for an API stage.

stageName -> (string)

The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.

description -> (string)

The stageâs description.

cacheClusterEnabled -> (boolean)

Specifies whether a cache cluster is enabled for the stage. To activate a method-level cache, set `CachingEnabled` to `true` for a method.

cacheClusterSize -> (string)

The stageâs cache capacity in GB. For more information about choosing a cache size, see [Enabling API caching to enhance responsiveness](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html) .

cacheClusterStatus -> (string)

The status of the cache cluster for the stage, if enabled.

methodSettings -> (map)

A map that defines the method settings for a Stage resource. Keys (designated as `/{method_setting_key` below) are method paths defined as `{resource_path}/{http_method}` for an individual method override, or `/\*/\*` for overriding all methods in the stage.

key -> (string)

value -> (structure)

Specifies the method setting properties.

metricsEnabled -> (boolean)

Specifies whether Amazon CloudWatch metrics are enabled for this method.

loggingLevel -> (string)

Specifies the logging level for this method, which affects the log entries pushed to Amazon CloudWatch Logs. Valid values are `OFF` , `ERROR` , and `INFO` . Choose `ERROR` to write only error-level entries to CloudWatch Logs, or choose `INFO` to include all `ERROR` events as well as extra informational events.

dataTraceEnabled -> (boolean)

Specifies whether data trace logging is enabled for this method, which affects the log entries pushed to Amazon CloudWatch Logs. This can be useful to troubleshoot APIs, but can result in logging sensitive data. We recommend that you donât enable this option for production APIs.

throttlingBurstLimit -> (integer)

Specifies the throttling burst limit.

throttlingRateLimit -> (double)

Specifies the throttling rate limit.

cachingEnabled -> (boolean)

Specifies whether responses should be cached and returned for requests. A cache cluster must be enabled on the stage for responses to be cached.

cacheTtlInSeconds -> (integer)

Specifies the time to live (TTL), in seconds, for cached responses. The higher the TTL, the longer the response will be cached.

cacheDataEncrypted -> (boolean)

Specifies whether the cached responses are encrypted.

requireAuthorizationForCacheControl -> (boolean)

Specifies whether authorization is required for a cache invalidation request.

unauthorizedCacheControlHeaderStrategy -> (string)

Specifies how to handle unauthorized requests for cache invalidation.

variables -> (map)

A map that defines the stage variables for a Stage resource. Variable names can have alphanumeric and underscore characters, and the values must match `[A-Za-z0-9-._~:/?#&=,]+` .

key -> (string)

value -> (string)

documentationVersion -> (string)

The version of the associated API documentation.

accessLogSettings -> (structure)

Settings for logging access in this stage.

format -> (string)

A single line format of the access logs of data, as specified by selected $context variables. The format must include at least `$context.requestId` .

destinationArn -> (string)

The Amazon Resource Name (ARN) of the CloudWatch Logs log group or Kinesis Data Firehose delivery stream to receive access logs. If you specify a Kinesis Data Firehose delivery stream, the stream name must begin with `amazon-apigateway-` .

canarySettings -> (structure)

Settings for the canary deployment in this stage.

percentTraffic -> (double)

The percent (0-100) of traffic diverted to a canary deployment.

deploymentId -> (string)

The ID of the canary deployment.

stageVariableOverrides -> (map)

Stage variables overridden for a canary release deployment, including new stage variables introduced in the canary. These stage variables are represented as a string-to-string map between stage variable names and their values.

key -> (string)

value -> (string)

useStageCache -> (boolean)

A Boolean flag to indicate whether the canary deployment uses the stage cache or not.

tracingEnabled -> (boolean)

Specifies whether active tracing with X-ray is enabled for the Stage.

webAclArn -> (string)

The ARN of the WebAcl associated with the Stage.

tags -> (map)

The collection of tags. Each tag element is associated with a given resource.

key -> (string)

value -> (string)

createdDate -> (timestamp)

The timestamp when the stage was created.

lastUpdatedDate -> (timestamp)

The timestamp when the stage last updated.