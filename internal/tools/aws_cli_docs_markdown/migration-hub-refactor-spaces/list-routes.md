# list-routesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migration-hub-refactor-spaces/list-routes.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migration-hub-refactor-spaces/list-routes.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [migration-hub-refactor-spaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migration-hub-refactor-spaces/index.html#cli-aws-migration-hub-refactor-spaces) ]

# list-routes

## Description

Lists all the Amazon Web Services Migration Hub Refactor Spaces routes within an application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/migration-hub-refactor-spaces-2021-10-26/ListRoutes)

`list-routes` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `RouteSummaryList`

## Synopsis

```
list-routes
--application-identifier <value>
--environment-identifier <value>
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

`--application-identifier` (string)

The ID of the application.

`--environment-identifier` (string)

The ID of the environment.

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

NextToken -> (string)

The token for the next page of results.

RouteSummaryList -> (list)

The list of `RouteSummary` objects.

(structure)

The summary information for the routes as a response to `ListRoutes` .

AppendSourcePath -> (boolean)

If set to `true` , this option appends the source path to the service URL endpoint.

ApplicationId -> (string)

The unique identifier of the application.

Arn -> (string)

The Amazon Resource Name (ARN) of the route.

CreatedByAccountId -> (string)

The Amazon Web Services account ID of the route creator.

CreatedTime -> (timestamp)

A timestamp that indicates when the route is created.

EnvironmentId -> (string)

The unique identifier of the environment.

Error -> (structure)

Any error associated with the route resource.

AccountId -> (string)

The Amazon Web Services account ID of the resource owner.

AdditionalDetails -> (map)

Additional details about the error.

key -> (string)

value -> (string)

Code -> (string)

The error code associated with the error.

Message -> (string)

The message associated with the error.

ResourceIdentifier -> (string)

The ID of the resource.

ResourceType -> (string)

The type of resource.

IncludeChildPaths -> (boolean)

Indicates whether to match all subpaths of the given source path. If this value is `false` , requests must match the source path exactly before they are forwarded to this routeâs service.

LastUpdatedTime -> (timestamp)

A timestamp that indicates when the route was last updated.

Methods -> (list)

A list of HTTP methods to match. An empty list matches all values. If a method is present, only HTTP requests using that method are forwarded to this routeâs service.

(string)

OwnerAccountId -> (string)

The Amazon Web Services account ID of the route owner.

PathResourceToId -> (map)

A mapping of Amazon API Gateway path resources to resource IDs.

key -> (string)

value -> (string)

RouteId -> (string)

The unique identifier of the route.

RouteType -> (string)

The route type of the route.

ServiceId -> (string)

The unique identifier of the service.

SourcePath -> (string)

This is the path that Refactor Spaces uses to match traffic. Paths must start with `/` and are relative to the base of the application. To use path parameters in the source path, add a variable in curly braces. For example, the resource path {user} represents a path parameter called âuserâ.

State -> (string)

The current state of the route.

Tags -> (map)

The tags assigned to the route.

key -> (string)

value -> (string)