# list-group-resourcesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/list-group-resources.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/list-group-resources.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [resource-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/index.html#cli-aws-resource-groups) ]

# list-group-resources

## Description

Returns a list of Amazon resource names (ARNs) of the resources that are members of a specified resource group.

**Minimum permissions**

To run this command, you must have the following permissions:

- `resource-groups:ListGroupResources`
- `cloudformation:DescribeStacks`
- `cloudformation:ListStackResources`
- `tag:GetResources`

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/ListGroupResources)

`list-group-resources` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ResourceIdentifiers`, `Resources`

## Synopsis

```
list-group-resources
[--group-name <value>]
[--group <value>]
[--filters <value>]
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

`--group-name` (string)

### Warning

- **Deprecated - donât use this parameter. Use the ``Group`` request field instead.** *

`--group` (string)

The name or the Amazon resource name (ARN) of the resource group.

`--filters` (list)

Filters, formatted as  ResourceFilter objects, that you want to apply to a `ListGroupResources` operation. Filters the results to include only those of the specified resource types.

- `resource-type` - Filter resources by their type. Specify up to five resource types in the format `AWS::ServiceCode::ResourceType` . For example, `AWS::EC2::Instance` , or `AWS::S3::Bucket` .

When you specify a `resource-type` filter for `ListGroupResources` , Resource Groups validates your filter resource types against the types that are defined in the query associated with the group. For example, if a group contains only S3 buckets because its query specifies only that resource type, but your `resource-type` filter includes EC2 instances, AWS Resource Groups does not filter for EC2 instances. In this case, a `ListGroupResources` request returns a `BadRequestException` error with a message similar to the following:

`The resource types specified as filters in the request are not valid.`

The error includes a list of resource types that failed the validation because they are not part of the query associated with the group. This validation doesnât occur when the group query specifies `AWS::AllSupported` , because a group based on such a query can contain any of the allowed resource types for the query type (tag-based or Amazon CloudFront stack-based queries).

(structure)

A filter name and value pair that is used to obtain more specific results from a list of resources.

Name -> (string)

The name of the filter. Filter names are case-sensitive.

Values -> (list)

One or more filter values. Allowed filter values vary by resource filter name, and are case-sensitive.

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "resource-type",
    "Values": ["string", ...]
  }
  ...
]
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

**To list all of the resources in a resource group**

Example 1: The following `list-resource-groups` example lists all of the resources that are part of the specified resource group.

```
aws resource-groups list-group-resources \
    --group-name tbq-WebServer
```

Output:

```
{
    "ResourceIdentifiers": [
        {
            "ResourceArn": "arn:aws:ec2:us-west-2:123456789012:instance/i-09f77fa38c12345ab",
            "ResourceType": "AWS::EC2::Instance"
        }
    ]
}
```

Example 2: The following example lists all of the resources in the group that also have a âresource-typeâ of the âAWS::EC2::Instanceâ. :

**aws resource-groups list-group-resources**:
âgroup-name tbq-WebServer âfilters Name=resource-type,Values=AWS::EC2::Instance

## Output

Resources -> (list)

An array of resources from which you can determine each resourceâs identity, type, and group membership status.

(structure)

A structure returned by the  ListGroupResources operation that contains identity and group membership status information for one of the resources in the group.

Identifier -> (structure)

A structure that contains the ARN of a resource and its resource type.

ResourceArn -> (string)

The Amazon resource name (ARN) of a resource.

ResourceType -> (string)

The resource type of a resource, such as `AWS::EC2::Instance` .

Status -> (structure)

A structure that contains the status of this resourceâs membership in the group.

### Note

This field is present in the response only if the group is of type `AWS::EC2::HostManagement` .

Name -> (string)

The current status.

ResourceIdentifiers -> (list)

### Warning

** *Deprecated - donât use this parameter. Use the ``Resources`` response field instead.* **

(structure)

A structure that contains the ARN of a resource and its resource type.

ResourceArn -> (string)

The Amazon resource name (ARN) of a resource.

ResourceType -> (string)

The resource type of a resource, such as `AWS::EC2::Instance` .

NextToken -> (string)

If present, indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null` .

QueryErrors -> (list)

A list of `QueryError` objects. Each error contains an `ErrorCode` and `Message` . Possible values for ErrorCode are `CLOUDFORMATION_STACK_INACTIVE` , `CLOUDFORMATION_STACK_NOT_EXISTING` , `CLOUDFORMATION_STACK_UNASSUMABLE_ROLE` and `RESOURCE_TYPE_NOT_SUPPORTED` .

(structure)

A two-part error structure that can occur in `ListGroupResources` or `SearchResources` .

ErrorCode -> (string)

Specifies the error code that was raised.

Message -> (string)

A message that explains the `ErrorCode` .