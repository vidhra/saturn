# list-apisÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/list-apis.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/list-apis.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appsync](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/index.html#cli-aws-appsync) ]

# list-apis

## Description

Lists the APIs in your AppSync account.

`ListApis` returns only the high level API details. For more detailed information about an API, use `GetApi` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListApis)

`list-apis` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `apis`

## Synopsis

```
list-apis
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

## Output

apis -> (list)

The `Api` objects.

(structure)

Describes an AppSync API. You can use `Api` for an AppSync API with your preferred configuration, such as an Event API that provides real-time message publishing and message subscriptions over WebSockets.

apiId -> (string)

The `Api` ID.

name -> (string)

The name of the `Api` .

ownerContact -> (string)

The owner contact information for the `Api`

tags -> (map)

A map with keys of `TagKey` objects and values of `TagValue` objects.

key -> (string)

The key for the tag.

value -> (string)

The value for the tag.

dns -> (map)

The DNS records for the API. This will include an HTTP and a real-time endpoint.

key -> (string)

value -> (string)

apiArn -> (string)

The Amazon Resource Name (ARN) for the `Api` .

created -> (timestamp)

The date and time that the `Api` was created.

xrayEnabled -> (boolean)

A flag indicating whether to use X-Ray tracing for this `Api` .

wafWebAclArn -> (string)

The Amazon Resource Name (ARN) of the WAF web access control list (web ACL) associated with this `Api` , if one exists.

eventConfig -> (structure)

The Event API configuration. This includes the default authorization configuration for connecting, publishing, and subscribing to an Event API.

authProviders -> (list)

A list of authorization providers.

(structure)

Describes an authorization provider.

authType -> (string)

The authorization type.

cognitoConfig -> (structure)

Describes an Amazon Cognito user pool configuration.

userPoolId -> (string)

The user pool ID.

awsRegion -> (string)

The Amazon Web Services Region in which the user pool was created.

appIdClientRegex -> (string)

A regular expression for validating the incoming Amazon Cognito user pool app client ID. If this value isnât set, no filtering is applied.

openIDConnectConfig -> (structure)

Describes an OpenID Connect (OIDC) configuration.

issuer -> (string)

The issuer for the OIDC configuration. The issuer returned by discovery must exactly match the value of `iss` in the ID token.

clientId -> (string)

The client identifier of the relying party at the OpenID identity provider. This identifier is typically obtained when the relying party is registered with the OpenID identity provider. You can specify a regular expression so that AppSync can validate against multiple client identifiers at a time.

iatTTL -> (long)

The number of milliseconds that a token is valid after itâs issued to a user.

authTTL -> (long)

The number of milliseconds that a token is valid after being authenticated.

lambdaAuthorizerConfig -> (structure)

A `LambdaAuthorizerConfig` specifies how to authorize AppSync API access when using the `AWS_LAMBDA` authorizer mode. Be aware that an AppSync API can have only one Lambda authorizer configured at a time.

authorizerResultTtlInSeconds -> (integer)

The number of seconds a response should be cached for. The default is 0 seconds, which disables caching. If you donât specify a value for `authorizerResultTtlInSeconds` , the default value is used. The maximum value is one hour (3600 seconds). The Lambda function can override this by returning a `ttlOverride` key in its response.

authorizerUri -> (string)

The Amazon Resource Name (ARN) of the Lambda function to be called for authorization. This can be a standard Lambda ARN, a version ARN (`.../v3` ), or an alias ARN.

**Note** : This Lambda function must have the following resource-based policy assigned to it. When configuring Lambda authorizers in the console, this is done for you. To use the Command Line Interface (CLI), run the following:

`aws lambda add-permission --function-name "arn:aws:lambda:us-east-2:111122223333:function:my-function" --statement-id "appsync" --principal appsync.amazonaws.com --action lambda:InvokeFunction`

identityValidationExpression -> (string)

A regular expression for validation of tokens before the Lambda function is called.

connectionAuthModes -> (list)

A list of valid authorization modes for the Event API connections.

(structure)

Describes an authorization configuration. Use `AuthMode` to specify the publishing and subscription authorization configuration for an Event API.

authType -> (string)

The authorization type.

defaultPublishAuthModes -> (list)

A list of valid authorization modes for the Event API publishing.

(structure)

Describes an authorization configuration. Use `AuthMode` to specify the publishing and subscription authorization configuration for an Event API.

authType -> (string)

The authorization type.

defaultSubscribeAuthModes -> (list)

A list of valid authorization modes for the Event API subscriptions.

(structure)

Describes an authorization configuration. Use `AuthMode` to specify the publishing and subscription authorization configuration for an Event API.

authType -> (string)

The authorization type.

logConfig -> (structure)

The CloudWatch Logs configuration for the Event API.

logLevel -> (string)

The type of information to log for the Event API.

cloudWatchLogsRoleArn -> (string)

The IAM service role that AppSync assumes to publish CloudWatch Logs in your account.

nextToken -> (string)

An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.