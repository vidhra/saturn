# get-stagesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-stages.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-stages.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [apigateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/index.html#cli-aws-apigateway) ]

# get-stages

## Description

Gets information about one or more Stage resources.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetStages)

## Synopsis

```
get-stages
--rest-api-id <value>
[--deployment-id <value>]
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

`--deployment-id` (string)

The stagesâ deployment identifiers.

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

**To get the list of stages for a REST API**

Command:

```
aws apigateway get-stages --rest-api-id 1234123412
```

Output:

```
{
    "item": [
        {
            "stageName": "dev",
            "cacheClusterSize": "0.5",
            "cacheClusterEnabled": true,
            "cacheClusterStatus": "AVAILABLE",
            "deploymentId": "123h64",
            "lastUpdatedDate": 1456185138,
            "createdDate": 1453589092,
            "methodSettings": {
                "~1resource~1subresource/POST": {
                    "cacheTtlInSeconds": 300,
                    "loggingLevel": "INFO",
                    "dataTraceEnabled": true,
                    "metricsEnabled": true,
                    "throttlingRateLimit": 500.0,
                    "cacheDataEncrypted": false,
                    "cachingEnabled": false,
                    "throttlingBurstLimit": 1000
                }
            }
        }
    ]
}
```

## Output

item -> (list)

The current page of elements from this collection.

(structure)

Represents a unique identifier for a version of a deployed RestApi that is callable by users.

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