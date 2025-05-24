# list-resourcesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/list-resources.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/list-resources.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [resource-explorer-2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/index.html#cli-aws-resource-explorer-2) ]

# list-resources

## Description

Returns a list of resources and their details that match the specified criteria. This query must use a view. If you donât explicitly specify a view, then Resource Explorer uses the default view for the Amazon Web Services Region in which you call this operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/resource-explorer-2-2022-07-28/ListResources)

`list-resources` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

`list-resources` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Resources`

## Synopsis

```
list-resources
[--filters <value>]
[--view-arn <value>]
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

`--filters` (structure)

An array of strings that specify which resources are included in the results of queries made using this view. When you use this view in a  Search operation, the filter string is combined with the searchâs `QueryString` parameter using a logical `AND` operator.

For information about the supported syntax, see [Search query reference for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html) in the *Amazon Web Services Resource Explorer User Guide* .

### Warning

This query string in the context of this operation supports only [filter prefixes](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-filters) with optional [operators](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-operators) . It doesnât support free-form text. For example, the string `region:us* service:ec2 -tag:stage=prod` includes all Amazon EC2 resources in any Amazon Web Services Region that begins with the letters `us` and is *not* tagged with a key `Stage` that has the value `prod` .

FilterString -> (string)

The string that contains the search keywords, prefixes, and operators to control the results that can be returned by a  Search operation. For more details, see [Search query syntax](https://docs.aws.amazon.com/resource-explorer/latest/APIReference/about-query-syntax.html) .

Shorthand Syntax:

```
FilterString=string
```

JSON Syntax:

```
{
  "FilterString": "string"
}
```

`--view-arn` (string)

Specifies the Amazon resource name (ARN) of the view to use for the query. If you donât specify a value for this parameter, then the operation automatically uses the default view for the Amazon Web Services Region in which you called this operation. If the Region either doesnât have a default view or if you donât have permission to use the default view, then the operation fails with a 401 Unauthorized exception.

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

If present, indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null` . The pagination tokens expire after 24 hours.

Resources -> (list)

The list of structures that describe the resources that match the query.

(structure)

A resource in Amazon Web Services that Amazon Web Services Resource Explorer has discovered, and for which it has stored information in the index of the Amazon Web Services Region that contains the resource.

Arn -> (string)

The [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource.

LastReportedAt -> (timestamp)

The date and time that Resource Explorer last queried this resource and updated the index with the latest information about the resource.

OwningAccountId -> (string)

The Amazon Web Services account that owns the resource.

Properties -> (list)

A structure with additional type-specific details about the resource. These properties can be added by turning on integration between Resource Explorer and other Amazon Web Services services.

(structure)

A structure that describes a property of a resource.

Data -> (document)

Details about this property. The content of this field is a JSON object that varies based on the resource type.

LastReportedAt -> (timestamp)

The date and time that the information about this resource property was last updated.

Name -> (string)

The name of this property of the resource.

Region -> (string)

The Amazon Web Services Region in which the resource was created and exists.

ResourceType -> (string)

The type of the resource.

Service -> (string)

The Amazon Web Services service that owns the resource and is responsible for creating and updating it.

ViewArn -> (string)

The Amazon resource name (ARN) of the view that this operation used to perform the search.