# get-graphql-apiÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-graphql-api.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-graphql-api.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appsync](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/index.html#cli-aws-appsync) ]

# get-graphql-api

## Description

Retrieves a `GraphqlApi` object.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/GetGraphqlApi)

## Synopsis

```
get-graphql-api
--api-id <value>
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

The API ID for the GraphQL API.

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

graphqlApi -> (structure)

The `GraphqlApi` object.

name -> (string)

The API name.

apiId -> (string)

The API ID.

authenticationType -> (string)

The authentication type.

logConfig -> (structure)

The Amazon CloudWatch Logs configuration.

fieldLogLevel -> (string)

The field logging level. Values can be NONE, ERROR, or ALL.

- **NONE** : No field-level logs are captured.
- **ERROR** : Logs the following information only for the fields that are in error:
- The error section in the server response.
- Field-level errors.
- The generated request/response functions that got resolved for error fields.
- **ALL** : The following information is logged for all fields in the query:
- Field-level tracing information.
- The generated request/response functions that got resolved for each field.

cloudWatchLogsRoleArn -> (string)

The service role that AppSync assumes to publish to CloudWatch logs in your account.

excludeVerboseContent -> (boolean)

Set to TRUE to exclude sections that contain information such as headers, context, and evaluated mapping templates, regardless of logging level.

userPoolConfig -> (structure)

The Amazon Cognito user pool configuration.

userPoolId -> (string)

The user pool ID.

awsRegion -> (string)

The Amazon Web Services Region in which the user pool was created.

defaultAction -> (string)

The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesnât match the Amazon Cognito user pool configuration.

appIdClientRegex -> (string)

A regular expression for validating the incoming Amazon Cognito user pool app client ID. If this value isnât set, no filtering is applied.

openIDConnectConfig -> (structure)

The OpenID Connect configuration.

issuer -> (string)

The issuer for the OIDC configuration. The issuer returned by discovery must exactly match the value of `iss` in the ID token.

clientId -> (string)

The client identifier of the relying party at the OpenID identity provider. This identifier is typically obtained when the relying party is registered with the OpenID identity provider. You can specify a regular expression so that AppSync can validate against multiple client identifiers at a time.

iatTTL -> (long)

The number of milliseconds that a token is valid after itâs issued to a user.

authTTL -> (long)

The number of milliseconds that a token is valid after being authenticated.

arn -> (string)

The Amazon Resource Name (ARN).

uris -> (map)

The URIs.

key -> (string)

value -> (string)

tags -> (map)

The tags.

key -> (string)

The key for the tag.

value -> (string)

The value for the tag.

additionalAuthenticationProviders -> (list)

A list of additional authentication providers for the `GraphqlApi` API.

(structure)

Describes an additional authentication provider.

authenticationType -> (string)

The authentication type: API key, Identity and Access Management (IAM), OpenID Connect (OIDC), Amazon Cognito user pools, or Lambda.

openIDConnectConfig -> (structure)

The OIDC configuration.

issuer -> (string)

The issuer for the OIDC configuration. The issuer returned by discovery must exactly match the value of `iss` in the ID token.

clientId -> (string)

The client identifier of the relying party at the OpenID identity provider. This identifier is typically obtained when the relying party is registered with the OpenID identity provider. You can specify a regular expression so that AppSync can validate against multiple client identifiers at a time.

iatTTL -> (long)

The number of milliseconds that a token is valid after itâs issued to a user.

authTTL -> (long)

The number of milliseconds that a token is valid after being authenticated.

userPoolConfig -> (structure)

The Amazon Cognito user pool configuration.

userPoolId -> (string)

The user pool ID.

awsRegion -> (string)

The Amazon Web Services Region in which the user pool was created.

appIdClientRegex -> (string)

A regular expression for validating the incoming Amazon Cognito user pool app client ID. If this value isnât set, no filtering is applied.

lambdaAuthorizerConfig -> (structure)

Configuration for Lambda function authorization.

authorizerResultTtlInSeconds -> (integer)

The number of seconds a response should be cached for. The default is 0 seconds, which disables caching. If you donât specify a value for `authorizerResultTtlInSeconds` , the default value is used. The maximum value is one hour (3600 seconds). The Lambda function can override this by returning a `ttlOverride` key in its response.

authorizerUri -> (string)

The Amazon Resource Name (ARN) of the Lambda function to be called for authorization. This can be a standard Lambda ARN, a version ARN (`.../v3` ), or an alias ARN.

**Note** : This Lambda function must have the following resource-based policy assigned to it. When configuring Lambda authorizers in the console, this is done for you. To use the Command Line Interface (CLI), run the following:

`aws lambda add-permission --function-name "arn:aws:lambda:us-east-2:111122223333:function:my-function" --statement-id "appsync" --principal appsync.amazonaws.com --action lambda:InvokeFunction`

identityValidationExpression -> (string)

A regular expression for validation of tokens before the Lambda function is called.

xrayEnabled -> (boolean)

A flag indicating whether to use X-Ray tracing for this `GraphqlApi` .

wafWebAclArn -> (string)

The ARN of the WAF access control list (ACL) associated with this `GraphqlApi` , if one exists.

lambdaAuthorizerConfig -> (structure)

Configuration for Lambda function authorization.

authorizerResultTtlInSeconds -> (integer)

The number of seconds a response should be cached for. The default is 0 seconds, which disables caching. If you donât specify a value for `authorizerResultTtlInSeconds` , the default value is used. The maximum value is one hour (3600 seconds). The Lambda function can override this by returning a `ttlOverride` key in its response.

authorizerUri -> (string)

The Amazon Resource Name (ARN) of the Lambda function to be called for authorization. This can be a standard Lambda ARN, a version ARN (`.../v3` ), or an alias ARN.

**Note** : This Lambda function must have the following resource-based policy assigned to it. When configuring Lambda authorizers in the console, this is done for you. To use the Command Line Interface (CLI), run the following:

`aws lambda add-permission --function-name "arn:aws:lambda:us-east-2:111122223333:function:my-function" --statement-id "appsync" --principal appsync.amazonaws.com --action lambda:InvokeFunction`

identityValidationExpression -> (string)

A regular expression for validation of tokens before the Lambda function is called.

dns -> (map)

The DNS records for the API.

key -> (string)

value -> (string)

visibility -> (string)

Sets the value of the GraphQL API to public (`GLOBAL` ) or private (`PRIVATE` ). If no value is provided, the visibility will be set to `GLOBAL` by default. This value cannot be changed once the API has been created.

apiType -> (string)

The value that indicates whether the GraphQL API is a standard API (`GRAPHQL` ) or merged API (`MERGED` ).

mergedApiExecutionRoleArn -> (string)

The Identity and Access Management service role ARN for a merged API. The AppSync service assumes this role on behalf of the Merged API to validate access to source APIs at runtime and to prompt the `AUTO_MERGE` to update the merged API endpoint with the source API changes automatically.

owner -> (string)

The account owner of the GraphQL API.

ownerContact -> (string)

The owner contact information for an API resource.

This field accepts any string input with a length of 0 - 256 characters.

introspectionConfig -> (string)

Sets the value of the GraphQL API to enable (`ENABLED` ) or disable (`DISABLED` ) introspection. If no value is provided, the introspection configuration will be set to `ENABLED` by default. This field will produce an error if the operation attempts to use the introspection feature while this field is disabled.

For more information about introspection, see [GraphQL introspection](https://graphql.org/learn/introspection/) .

queryDepthLimit -> (integer)

The maximum depth a query can have in a single request. Depth refers to the amount of nested levels allowed in the body of query. The default value is `0` (or unspecified), which indicates thereâs no depth limit. If you set a limit, it can be between `1` and `75` nested levels. This field will produce a limit error if the operation falls out of bounds.

Note that fields can still be set to nullable or non-nullable. If a non-nullable field produces an error, the error will be thrown upwards to the first nullable field available.

resolverCountLimit -> (integer)

The maximum number of resolvers that can be invoked in a single request. The default value is `0` (or unspecified), which will set the limit to `10000` . When specified, the limit value can be between `1` and `10000` . This field will produce a limit error if the operation falls out of bounds.

enhancedMetricsConfig -> (structure)

The `enhancedMetricsConfig` object.

resolverLevelMetricsBehavior -> (string)

Controls how resolver metrics will be emitted to CloudWatch. Resolver metrics include:

- GraphQL errors: The number of GraphQL errors that occurred.
- Requests: The number of invocations that occurred during a request.
- Latency: The time to complete a resolver invocation.
- Cache hits: The number of cache hits during a request.
- Cache misses: The number of cache misses during a request.

These metrics can be emitted to CloudWatch per resolver or for all resolvers in the request. Metrics will be recorded by API ID and resolver name. `resolverLevelMetricsBehavior` accepts one of these values at a time:

- `FULL_REQUEST_RESOLVER_METRICS` : Records and emits metric data for all resolvers in the request.
- `PER_RESOLVER_METRICS` : Records and emits metric data for resolvers that have the `metricsConfig` value set to `ENABLED` .

dataSourceLevelMetricsBehavior -> (string)

Controls how data source metrics will be emitted to CloudWatch. Data source metrics include:

- Requests: The number of invocations that occured during a request.
- Latency: The time to complete a data source invocation.
- Errors: The number of errors that occurred during a data source invocation.

These metrics can be emitted to CloudWatch per data source or for all data sources in the request. Metrics will be recorded by API ID and data source name. `dataSourceLevelMetricsBehavior` accepts one of these values at a time:

- `FULL_REQUEST_DATA_SOURCE_METRICS` : Records and emits metric data for all data sources in the request.
- `PER_DATA_SOURCE_METRICS` : Records and emits metric data for data sources that have the `metricsConfig` value set to `ENABLED` .

operationLevelMetricsConfig -> (string)

Controls how operation metrics will be emitted to CloudWatch. Operation metrics include:

- Requests: The number of times a specified GraphQL operation was called.
- GraphQL errors: The number of GraphQL errors that occurred during a specified GraphQL operation.

Metrics will be recorded by API ID and operation name. You can set the value to `ENABLED` or `DISABLED` .