# search-resourcesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/search-resources.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/search-resources.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [resource-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/index.html#cli-aws-resource-groups) ]

# search-resources

## Description

Returns a list of Amazon Web Services resource identifiers that matches the specified query. The query uses the same format as a resource query in a  CreateGroup or  UpdateGroupQuery operation.

**Minimum permissions**

To run this command, you must have the following permissions:

- `resource-groups:SearchResources`
- `cloudformation:DescribeStacks`
- `cloudformation:ListStackResources`
- `tag:GetResources`

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/SearchResources)

`search-resources` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ResourceIdentifiers`

## Synopsis

```
search-resources
--resource-query <value>
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

`--resource-query` (structure)

The search query, using the same formats that are supported for resource group definition. For more information, see  CreateGroup .

Type -> (string)

The type of the query to perform. This can have one of two values:

- [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/search-resources.html#id1)`CLOUDFORMATION_STACK_1_0:` * Specifies that you want the group to contain the members of an CloudFormation stack. The `Query` contains a `StackIdentifier` element with an Amazon resource name (ARN) for a CloudFormation stack.
- [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/search-resources.html#id3)`TAG_FILTERS_1_0:` * Specifies that you want the group to include resource that have tags that match the query.

Query -> (string)

The query that defines a group or a search. The contents depends on the value of the `Type` element.

- `ResourceTypeFilters` â Applies to all `ResourceQuery` objects of either `Type` . This element contains one of the following two items:
- The value `AWS::AllSupported` . This causes the ResourceQuery to match resources of any resource type that also match the query.
- A list (a JSON array) of resource type identifiers that limit the query to only resources of the specified types. For the complete list of resource types that you can use in the array value for `ResourceTypeFilters` , see [Resources you can use with Resource Groups and Tag Editor](https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html) in the *Resource Groups User Guide* .

Example: `"ResourceTypeFilters": ["AWS::AllSupported"]` or `"ResourceTypeFilters": ["AWS::EC2::Instance", "AWS::S3::Bucket"]`

- `TagFilters` â applicable only if `Type` = `TAG_FILTERS_1_0` . The `Query` contains a JSON string that represents a collection of simple tag filters. The JSON string uses a syntax similar to the `` [GetResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html) `` operation, but uses only the `` [ResourceTypeFilters](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html#resourcegrouptagging-GetResources-request-ResourceTypeFilters) `` and `` [TagFilters](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html#resourcegrouptagging-GetResources-request-TagFiltersTagFilters) `` fields. If you specify more than one tag key, only resources that match all tag keys, and at least one value of each specified tag key, are returned in your query. If you specify more than one value for a tag key, a resource matches the filter if it has a tag key value that matches *any* of the specified values. For example, consider the following sample query for resources that have two tags, `Stage` and `Version` , with two values each:  `[{"Stage":["Test","Deploy"]},{"Version":["1","2"]}]`   The results of this resource query could include the following.
- An Amazon EC2 instance that has the following two tags: `{"Stage":"Deploy"}` , and `{"Version":"2"}`
- An S3 bucket that has the following two tags: `{"Stage":"Test"}` , and `{"Version":"1"}`

The resource query results would *not* include the following items in the results, however.

- An Amazon EC2 instance that has only the following tag: `{"Stage":"Deploy"}` . The instance does not have **all** of the tag keys specified in the filter, so it is excluded from the results.
- An RDS database that has the following two tags: `{"Stage":"Archived"}` and `{"Version":"4"}`   The database has all of the tag keys, but none of those keys has an associated value that matches at least one of the specified values in the filter.

Example: `"TagFilters": [ { "Key": "Stage", "Values": [ "Gamma", "Beta" ] }`

- `StackIdentifier` â applicable only if `Type` = `CLOUDFORMATION_STACK_1_0` . The value of this parameter is the Amazon Resource Name (ARN) of the CloudFormation stack whose resources you want included in the group.

Shorthand Syntax:

```
Type=string,Query=string
```

JSON Syntax:

```
{
  "Type": "TAG_FILTERS_1_0"|"CLOUDFORMATION_STACK_1_0",
  "Query": "string"
}
```

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To find resources that match a query**

The following `search-resources` example retrieves a list of all AWS resources that match the specified query.

```
aws resource-groups search-resources \
    --resource-query file://query.json
```

Contents of `query.json`:

```
{
    "Type": "TAG_FILTERS_1_0",
    "Query": "{\"ResourceTypeFilters\":[\"AWS::EC2::Instance\"],\"TagFilters\":[{\"Key\":\"Patch Group\", \"Values\":[\"Dev\"]}]}"
}
```

Output:

```
{
    "ResourceIdentifiers": [
        {
            "ResourceArn": "arn:aws:ec2:us-west-2:123456789012:instance/i-01a23bc45d67890ef",
            "ResourceType": "AWS::EC2::Instance"
        }
    ]
}
```

## Output

ResourceIdentifiers -> (list)

The ARNs and resource types of resources that are members of the group that you specified.

(structure)

A structure that contains the ARN of a resource and its resource type.

ResourceArn -> (string)

The Amazon resource name (ARN) of a resource.

ResourceType -> (string)

The resource type of a resource, such as `AWS::EC2::Instance` .

NextToken -> (string)

If present, indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null` .

QueryErrors -> (list)

A list of `QueryError` objects. Each error contains an `ErrorCode` and `Message` .

Possible values for `ErrorCode` :

- `CLOUDFORMATION_STACK_INACTIVE`
- `CLOUDFORMATION_STACK_NOT_EXISTING`
- `CLOUDFORMATION_STACK_UNASSUMABLE_ROLE`

(structure)

A two-part error structure that can occur in `ListGroupResources` or `SearchResources` .

ErrorCode -> (string)

Specifies the error code that was raised.

Message -> (string)

A message that explains the `ErrorCode` .