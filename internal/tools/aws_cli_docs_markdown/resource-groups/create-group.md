# create-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/create-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/create-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [resource-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/index.html#cli-aws-resource-groups) ]

# create-group

## Description

Creates a resource group with the specified name and description. You can optionally include either a resource query or a service configuration. For more information about constructing a resource query, see [Build queries and groups in Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/getting_started-query.html) in the *Resource Groups User Guide* . For more information about service-linked groups and service configurations, see [Service configurations for Resource Groups](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html) .

**Minimum permissions**

To run this command, you must have the following permissions:

- `resource-groups:CreateGroup`

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/CreateGroup)

## Synopsis

```
create-group
--name <value>
[--description <value>]
[--resource-query <value>]
[--tags <value>]
[--configuration <value>]
[--criticality <value>]
[--owner <value>]
[--display-name <value>]
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

`--name` (string)

The name of the group, which is the identifier of the group in other operations. You canât change the name of a resource group after you create it. A resource group name can consist of letters, numbers, hyphens, periods, and underscores. The name cannot start with `AWS` , `aws` , or any other possible capitalization; these are reserved. A resource group name must be unique within each Amazon Web Services Region in your Amazon Web Services account.

`--description` (string)

The description of the resource group. Descriptions can consist of letters, numbers, hyphens, underscores, periods, and spaces.

`--resource-query` (structure)

The resource query that determines which Amazon Web Services resources are members of this group. For more information about resource queries, see [Create a tag-based group in Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#gettingstarted-query-cli-tag) .

### Note

A resource group can contain either a `ResourceQuery` or a `Configuration` , but not both.

Type -> (string)

The type of the query to perform. This can have one of two values:

- [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/create-group.html#id1)`CLOUDFORMATION_STACK_1_0:` * Specifies that you want the group to contain the members of an CloudFormation stack. The `Query` contains a `StackIdentifier` element with an Amazon resource name (ARN) for a CloudFormation stack.
- [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/create-group.html#id3)`TAG_FILTERS_1_0:` * Specifies that you want the group to include resource that have tags that match the query.

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

`--tags` (map)

The tags to add to the group. A tag is key-value pair string.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--configuration` (list)

A configuration associates the resource group with an Amazon Web Services service and specifies how the service can interact with the resources in the group. A configuration is an array of  GroupConfigurationItem elements. For details about the syntax of service configurations, see [Service configurations for Resource Groups](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html) .

### Note

A resource group can contain either a `Configuration` or a `ResourceQuery` , but not both.

(structure)

An item in a group configuration. A group service configuration can have one or more items. For details about group service configuration syntax, see [Service configurations for resource groups](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html) .

Type -> (string)

Specifies the type of group configuration item. Each item must have a unique value for `type` . For the list of types that you can specify for a configuration item, see [Supported resource types and parameters](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types) .

Parameters -> (list)

A collection of parameters for this group configuration item. For the list of parameters that you can use with each configuration item type, see [Supported resource types and parameters](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types) .

(structure)

A parameter for a group configuration item. For details about group service configuration syntax, see [Service configurations for resource groups](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html) .

Name -> (string)

The name of the group configuration parameter. For the list of parameters that you can use with each configuration item type, see [Supported resource types and parameters](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types) .

Values -> (list)

The value or values to be used for the specified parameter. For the list of values you can use with each parameter, see [Supported resource types and parameters](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types) .

(string)

JSON Syntax:

```
[
  {
    "Type": "string",
    "Parameters": [
      {
        "Name": "string",
        "Values": ["string", ...]
      }
      ...
    ]
  }
  ...
]
```

`--criticality` (integer)

The critical rank of the application group on a scale of 1 to 10, with a rank of 1 being the most critical, and a rank of 10 being least critical.

`--owner` (string)

A name, email address or other identifier for the person or group who is considered as the owner of this application group within your organization.

`--display-name` (string)

The name of the application group, which you can change at any time.

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

**Example 1: To create a tag-based resource group**

The following `create-group` example creates a tag-based resource group of Amazon EC2 instances in the current region. Itâs based on a query for resources that are tagged with the key `Name`, and the value `WebServers`. The group name is `tbq-WebServer`. The query is in a separate JSON file that is passed to the command.

```
aws resource-groups create-group \
    --name tbq-WebServer \
    --resource-query file://query.json
```

Contents of `query.json`:

```
{
    "Type": "TAG_FILTERS_1_0",
    "Query": "{\"ResourceTypeFilters\":[\"AWS::EC2::Instance\"],\"TagFilters\":[{\"Key\":\"Name\", \"Values\":[\"WebServers\"]}]}"
}
```

Output:

```
{
    "Group": {
        "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/tbq-WebServer",
        "Name": "tbq-WebServer"
    },
    "ResourceQuery": {
        "Type": "TAG_FILTERS_1_0",
        "Query": "{\"ResourceTypeFilters\":[\"AWS::EC2::Instance\"],\"TagFilters\":[{\"Key\":\"Name\", \"Values\":[\"WebServers\"]}]}"
    }
}
```

**Example 2: To create a CloudFormation stack-based resource group**

The following `create-group` example creates an AWS CloudFormation stack-based resource group named `sampleCFNstackgroup`. The query includes all resources in the specified CloudFormation stack that are supported by AWS Resource Groups.

```
aws resource-groups create-group \
    --name cbq-CFNstackgroup \
    --resource-query file://query.json
```

Contents of `query.json`:

```
{
    "Type": "CLOUDFORMATION_STACK_1_0",
    "Query": "{\"ResourceTypeFilters\":[\"AWS::AllSupported\"],\"StackIdentifier\":\"arn:aws:cloudformation:us-west-2:123456789012:stack/MyCFNStack/1415z9z0-z39z-11z8-97z5-500z212zz6fz\"}"
}
```

Output:

```
{
    "Group": {
        "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/cbq-CFNstackgroup",
        "Name": "cbq-CFNstackgroup"
    },
    "ResourceQuery": {
        "Type": "CLOUDFORMATION_STACK_1_0",
        "Query": "{\"ResourceTypeFilters\":[\"AWS::AllSupported\"],\"StackIdentifier\":\"arn:aws:cloudformation:us-east-2:123456789012:stack/MyCFNStack/1415z9z0-z39z-11z8-97z5-500z212zz6fz\"}"}'
    }
}
```

For more information, see [Create Groups](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html) in the *AWS Resource Groups User Guide*.

## Output

Group -> (structure)

The description of the resource group.

GroupArn -> (string)

The Amazon resource name (ARN) of the resource group.

Name -> (string)

The name of the resource group.

Description -> (string)

The description of the resource group.

Criticality -> (integer)

The critical rank of the application group on a scale of 1 to 10, with a rank of 1 being the most critical, and a rank of 10 being least critical.

Owner -> (string)

A name, email address or other identifier for the person or group who is considered as the owner of this application group within your organization.

DisplayName -> (string)

The name of the application group, which you can change at any time.

ApplicationTag -> (map)

A tag that defines the application group membership. This tag is only supported for application groups.

key -> (string)

value -> (string)

ResourceQuery -> (structure)

The resource query associated with the group. For more information about resource queries, see [Create a tag-based group in Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#gettingstarted-query-cli-tag) .

Type -> (string)

The type of the query to perform. This can have one of two values:

- [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/create-group.html#id5)`CLOUDFORMATION_STACK_1_0:` * Specifies that you want the group to contain the members of an CloudFormation stack. The `Query` contains a `StackIdentifier` element with an Amazon resource name (ARN) for a CloudFormation stack.
- [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/create-group.html#id7)`TAG_FILTERS_1_0:` * Specifies that you want the group to include resource that have tags that match the query.

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

Tags -> (map)

The tags associated with the group.

key -> (string)

value -> (string)

GroupConfiguration -> (structure)

The service configuration associated with the resource group. For details about the syntax of a service configuration, see [Service configurations for Resource Groups](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html) .

Configuration -> (list)

The configuration currently associated with the group and in effect.

(structure)

An item in a group configuration. A group service configuration can have one or more items. For details about group service configuration syntax, see [Service configurations for resource groups](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html) .

Type -> (string)

Specifies the type of group configuration item. Each item must have a unique value for `type` . For the list of types that you can specify for a configuration item, see [Supported resource types and parameters](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types) .

Parameters -> (list)

A collection of parameters for this group configuration item. For the list of parameters that you can use with each configuration item type, see [Supported resource types and parameters](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types) .

(structure)

A parameter for a group configuration item. For details about group service configuration syntax, see [Service configurations for resource groups](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html) .

Name -> (string)

The name of the group configuration parameter. For the list of parameters that you can use with each configuration item type, see [Supported resource types and parameters](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types) .

Values -> (list)

The value or values to be used for the specified parameter. For the list of values you can use with each parameter, see [Supported resource types and parameters](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types) .

(string)

ProposedConfiguration -> (list)

If present, the new configuration that is in the process of being applied to the group.

(structure)

An item in a group configuration. A group service configuration can have one or more items. For details about group service configuration syntax, see [Service configurations for resource groups](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html) .

Type -> (string)

Specifies the type of group configuration item. Each item must have a unique value for `type` . For the list of types that you can specify for a configuration item, see [Supported resource types and parameters](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types) .

Parameters -> (list)

A collection of parameters for this group configuration item. For the list of parameters that you can use with each configuration item type, see [Supported resource types and parameters](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types) .

(structure)

A parameter for a group configuration item. For details about group service configuration syntax, see [Service configurations for resource groups](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html) .

Name -> (string)

The name of the group configuration parameter. For the list of parameters that you can use with each configuration item type, see [Supported resource types and parameters](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types) .

Values -> (list)

The value or values to be used for the specified parameter. For the list of values you can use with each parameter, see [Supported resource types and parameters](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types) .

(string)

Status -> (string)

The current status of an attempt to update the group configuration.

FailureReason -> (string)

If present, the reason why a request to update the group configuration failed.