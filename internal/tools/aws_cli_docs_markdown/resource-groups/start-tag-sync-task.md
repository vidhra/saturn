# start-tag-sync-taskÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/start-tag-sync-task.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/start-tag-sync-task.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [resource-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/index.html#cli-aws-resource-groups) ]

# start-tag-sync-task

## Description

Creates a new tag-sync task to onboard and sync resources tagged with a specific tag key-value pair to an application. To start a tag-sync task, you need a [resource tagging role](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-tag-sync.html#tag-sync-role) . The resource tagging role grants permissions to tag and untag applications resources and must include a trust policy that allows Resource Groups to assume the role and perform resource tagging tasks on your behalf.

For instructions on creating a tag-sync task, see [Create a tag-sync using the Resource Groups API](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-tag-sync.html#create-tag-sync) in the *Amazon Web Services Service Catalog AppRegistry Administrator Guide* .

**Minimum permissions**

To run this command, you must have the following permissions:

- `resource-groups:StartTagSyncTask` on the application group
- `resource-groups:CreateGroup`
- `iam:PassRole` on the role provided in the request

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/StartTagSyncTask)

## Synopsis

```
start-tag-sync-task
--group <value>
[--tag-key <value>]
[--tag-value <value>]
[--resource-query <value>]
--role-arn <value>
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

`--group` (string)

The Amazon resource name (ARN) or name of the application group for which you want to create a tag-sync task.

`--tag-key` (string)

The tag key. Resources tagged with this tag key-value pair will be added to the application. If a resource with this tag is later untagged, the tag-sync task removes the resource from the application.

When using the `TagKey` parameter, you must also specify the `TagValue` parameter. If you specify a tag key-value pair, you canât use the `ResourceQuery` parameter.

`--tag-value` (string)

The tag value. Resources tagged with this tag key-value pair will be added to the application. If a resource with this tag is later untagged, the tag-sync task removes the resource from the application.

When using the `TagValue` parameter, you must also specify the `TagKey` parameter. If you specify a tag key-value pair, you canât use the `ResourceQuery` parameter.

`--resource-query` (structure)

The query you can use to create the tag-sync task. With this method, all resources matching the query are added to the specified application group. A `ResourceQuery` specifies both a query `Type` and a `Query` string as JSON string objects. For more information on defining a resource query for a tag-sync task, see the tag-based query type in [Types of resource group queries](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#getting_started-query_types) in *Resource Groups User Guide* .

When using the `ResourceQuery` parameter, you cannot use the `TagKey` and `TagValue` parameters.

When you combine all of the elements together into a single string, any double quotes that are embedded inside another double quote pair must be escaped by preceding the embedded double quote with a backslash character (). For example, a complete `ResourceQuery` parameter must be formatted like the following CLI parameter example:

`--resource-query '{"Type":"TAG_FILTERS_1_0","Query":"{\"ResourceTypeFilters\":[\"AWS::AllSupported\"],\"TagFilters\":[{\"Key\":\"Stage\",\"Values\":[\"Test\"]}]}"}'`

In the preceding example, all of the double quote characters in the value part of the `Query` element must be escaped because the value itself is surrounded by double quotes. For more information, see [Quoting strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *Command Line Interface User Guide* .

For the complete list of resource types that you can use in the array value for `ResourceTypeFilters` , see [Resources you can use with Resource Groups and Tag Editor](https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html) in the *Resource Groups User Guide* . For example:

`"ResourceTypeFilters":["AWS::S3::Bucket", "AWS::EC2::Instance"]`

Type -> (string)

The type of the query to perform. This can have one of two values:

- [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/start-tag-sync-task.html#id1)`CLOUDFORMATION_STACK_1_0:` * Specifies that you want the group to contain the members of an CloudFormation stack. The `Query` contains a `StackIdentifier` element with an Amazon resource name (ARN) for a CloudFormation stack.
- [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/start-tag-sync-task.html#id3)`TAG_FILTERS_1_0:` * Specifies that you want the group to include resource that have tags that match the query.

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

`--role-arn` (string)

The Amazon resource name (ARN) of the role assumed by the service to tag and untag resources on your behalf.

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

GroupArn -> (string)

The Amazon resource name (ARN) of the application group for which you want to add or remove resources.

GroupName -> (string)

The name of the application group to onboard and sync resources.

TaskArn -> (string)

The Amazon resource name (ARN) of the new tag-sync task.

TagKey -> (string)

The tag key of the tag-sync task.

TagValue -> (string)

The tag value of the tag-sync task.

ResourceQuery -> (structure)

The query you can use to define a resource group or a search for resources. A `ResourceQuery` specifies both a query `Type` and a `Query` string as JSON string objects. See the examples section for example JSON strings. For more information about creating a resource group with a resource query, see [Build queries and groups in Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html) in the *Resource Groups User Guide*

When you combine all of the elements together into a single string, any double quotes that are embedded inside another double quote pair must be escaped by preceding the embedded double quote with a backslash character (). For example, a complete `ResourceQuery` parameter must be formatted like the following CLI parameter example:

`--resource-query '{"Type":"TAG_FILTERS_1_0","Query":"{\"ResourceTypeFilters\":[\"AWS::AllSupported\"],\"TagFilters\":[{\"Key\":\"Stage\",\"Values\":[\"Test\"]}]}"}'`

In the preceding example, all of the double quote characters in the value part of the `Query` element must be escaped because the value itself is surrounded by double quotes. For more information, see [Quoting strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *Command Line Interface User Guide* .

For the complete list of resource types that you can use in the array value for `ResourceTypeFilters` , see [Resources you can use with Resource Groups and Tag Editor](https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html) in the *Resource Groups User Guide* . For example:

`"ResourceTypeFilters":["AWS::S3::Bucket", "AWS::EC2::Instance"]`

Type -> (string)

The type of the query to perform. This can have one of two values:

- [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/start-tag-sync-task.html#id5)`CLOUDFORMATION_STACK_1_0:` * Specifies that you want the group to contain the members of an CloudFormation stack. The `Query` contains a `StackIdentifier` element with an Amazon resource name (ARN) for a CloudFormation stack.
- [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/start-tag-sync-task.html#id7)`TAG_FILTERS_1_0:` * Specifies that you want the group to include resource that have tags that match the query.

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

RoleArn -> (string)

The Amazon resource name (ARN) of the role assumed by the service to tag and untag resources on your behalf.