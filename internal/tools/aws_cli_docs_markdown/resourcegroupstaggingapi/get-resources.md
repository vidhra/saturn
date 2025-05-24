# get-resourcesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resourcegroupstaggingapi/get-resources.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resourcegroupstaggingapi/get-resources.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [resourcegroupstaggingapi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resourcegroupstaggingapi/index.html#cli-aws-resourcegroupstaggingapi) ]

# get-resources

## Description

Returns all the tagged or previously tagged resources that are located in the specified Amazon Web Services Region for the account.

Depending on what information you want returned, you can also specify the following:

- *Filters* that specify what tags and resource types you want returned. The response includes all tags that are associated with the requested resources.
- Information about compliance with the accountâs effective tag policy. For more information on tag policies, see [Tag Policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) in the *Organizations User Guide.*

This operation supports pagination, where the response can be sent in multiple pages. You should check the `PaginationToken` response parameter to determine if there are additional results available to return. Repeat the query, passing the `PaginationToken` response parameter value as an input to the next request until you recieve a `null` value. A null value for `PaginationToken` indicates that there are no more results waiting to be returned.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/resourcegroupstaggingapi-2017-01-26/GetResources)

`get-resources` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ResourceTagMappingList`

## Synopsis

```
get-resources
[--tag-filters <value>]
[--tags-per-page <value>]
[--resource-type-filters <value>]
[--include-compliance-details | --no-include-compliance-details]
[--exclude-compliant-resources | --no-exclude-compliant-resources]
[--resource-arn-list <value>]
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

`--tag-filters` (list)

Specifies a list of TagFilters (keys and values) to restrict the output to only those resources that have tags with the specified keys and, if included, the specified values. Each `TagFilter` must contain a key with values optional. A request can include up to 50 keys, and each key can include up to 20 values.

Note the following when deciding how to use TagFilters:

- If you *donât* specify a `TagFilter` , the response includes all resources that are currently tagged or ever had a tag. Resources that currently donât have tags are shown with an empty tag set, like this: `"Tags": []` .
- If you specify more than one filter in a single request, the response returns only those resources that satisfy all filters.
- If you specify a filter that contains more than one value for a key, the response returns resources that match *any* of the specified values for that key.
- If you donât specify a value for a key, the response returns all resources that are tagged with that key, with any or no value. For example, for the following filters: `filter1= {keyA,{value1}}` , `filter2={keyB,{value2,value3,value4}}` , `filter3= {keyC}` :
- `GetResources({filter1})` returns resources tagged with `key1=value1`
- `GetResources({filter2})` returns resources tagged with `key2=value2` or `key2=value3` or `key2=value4`
- `GetResources({filter3})` returns resources tagged with any tag with the key `key3` , and with any or no value
- `GetResources({filter1,filter2,filter3})` returns resources tagged with `(key1=value1) and (key2=value2 or key2=value3 or key2=value4) and (key3, any or no value)`

(structure)

A list of tags (keys and values) that are used to specify the associated resources.

Key -> (string)

One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.

Values -> (list)

One part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null.

(string)

Shorthand Syntax:

```
Key=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Values": ["string", ...]
  }
  ...
]
```

`--tags-per-page` (integer)

Amazon Web Services recommends using `ResourcesPerPage` instead of this parameter.

A limit that restricts the number of tags (key and value pairs) returned by `GetResources` in paginated output. A resource with no tags is counted as having one tag (one key and value pair).

`GetResources` does not split a resource and its associated tags across pages. If the specified `TagsPerPage` would cause such a break, a `PaginationToken` is returned in place of the affected resource and its tags. Use that token in another request to get the remaining data. For example, if you specify a `TagsPerPage` of `100` and the account has 22 resources with 10 tags each (meaning that each resource has 10 key and value pairs), the output will consist of three pages. The first page displays the first 10 resources, each with its 10 tags. The second page displays the next 10 resources, each with its 10 tags. The third page displays the remaining 2 resources, each with its 10 tags.

You can set `TagsPerPage` to a minimum of 100 items up to a maximum of 500 items.

`--resource-type-filters` (list)

Specifies the resource types that you want included in the response. The format of each resource type is `service[:resourceType]` . For example, specifying a resource type of `ec2` returns all Amazon EC2 resources (which includes EC2 instances). Specifying a resource type of `ec2:instance` returns only EC2 instances.

The string for each service name and resource type is the same as that embedded in a resourceâs Amazon Resource Name (ARN). For the list of services whose resources you can use in this parameter, see [Services that support the Resource Groups Tagging API](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/supported-services.html) .

You can specify multiple resource types by using an array. The array can include up to 100 items. Note that the length constraint requirement applies to each resource type filter. For example, the following string would limit the response to only Amazon EC2 instances, Amazon S3 buckets, or any Audit Manager resource:

`ec2:instance,s3:bucket,auditmanager`

(string)

Syntax:

```
"string" "string" ...
```

`--include-compliance-details` | `--no-include-compliance-details` (boolean)

Specifies whether to include details regarding the compliance with the effective tag policy. Set this to `true` to determine whether resources are compliant with the tag policy and to get details.

`--exclude-compliant-resources` | `--no-exclude-compliant-resources` (boolean)

Specifies whether to exclude resources that are compliant with the tag policy. Set this to `true` if you are interested in retrieving information on noncompliant resources only.

You can use this parameter only if the `IncludeComplianceDetails` parameter is also set to `true` .

`--resource-arn-list` (list)

Specifies a list of ARNs of resources for which you want to retrieve tag data. You canât specify both this parameter and any of the pagination parameters (`ResourcesPerPage` , `TagsPerPage` , `PaginationToken` ) in the same request. If you specify both, you get an `Invalid Parameter` exception.

If a resource specified by this parameter doesnât exist, it doesnât generate an error; it simply isnât included in the response.

An ARN (Amazon Resource Name) uniquely identifies a resource. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

(string)

Syntax:

```
"string" "string" ...
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

**To get a list of tagged resources**

The following `get-resources` example displays a list of resources in the account that are tagged with the specified key name and value.

```
aws resourcegroupstaggingapi get-resources \
    --tag-filters Key=Environment,Values=Production \
    --tags-per-page 100
```

Output:

```
{
    "ResourceTagMappingList": [
        {
            "ResourceARN": " arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0",
            "Tags": [
                {
                    "Key": "Environment",
                    "Value": "Production"
                }
            ]
        }
    ]
}
```

For more information, see [GetResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html) in the *Resource Groups Tagging API Reference*.

## Output

PaginationToken -> (string)

A string that indicates that there is more data available than this response contains. To receive the next part of the response, specify this response value as the `PaginationToken` value in the request for the next page.

ResourceTagMappingList -> (list)

A list of resource ARNs and the tags (keys and values) associated with each.

(structure)

A list of resource ARNs and the tags (keys and values) that are associated with each.

ResourceARN -> (string)

The ARN of the resource.

Tags -> (list)

The tags that have been applied to one or more Amazon Web Services resources.

(structure)

The metadata that you apply to Amazon Web Services resources to help you categorize and organize them. Each tag consists of a key and a value, both of which you define. For more information, see [Tagging Amazon Web Services Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference* .

Key -> (string)

One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.

Value -> (string)

One part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null.

ComplianceDetails -> (structure)

Information that shows whether a resource is compliant with the effective tag policy, including details on any noncompliant tag keys.

NoncompliantKeys -> (list)

These tag keys on the resource are noncompliant with the effective tag policy.

(string)

KeysWithNoncompliantValues -> (list)

These are keys defined in the effective policy that are on the resource with either incorrect case treatment or noncompliant values.

(string)

ComplianceStatus -> (boolean)

Whether a resource is compliant with the effective tag policy.