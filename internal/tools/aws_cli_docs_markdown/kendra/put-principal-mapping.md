# put-principal-mappingÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/put-principal-mapping.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/put-principal-mapping.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kendra](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html#cli-aws-kendra) ]

# put-principal-mapping

## Description

Maps users to their groups so that you only need to provide the user ID when you issue the query.

You can also map sub groups to groups. For example, the group âCompany Intellectual Property Teamsâ includes sub groups âResearchâ and âEngineeringâ. These sub groups include their own list of users or people who work in these teams. Only users who work in research and engineering, and therefore belong in the intellectual property group, can see top-secret company documents in their search results.

This is useful for user context filtering, where search results are filtered based on the user or their group access to documents. For more information, see [Filtering on user context](https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html) .

If more than five `PUT` actions for a group are currently processing, a validation exception is thrown.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kendra-2019-02-03/PutPrincipalMapping)

## Synopsis

```
put-principal-mapping
--index-id <value>
[--data-source-id <value>]
--group-id <value>
--group-members <value>
[--ordering-id <value>]
[--role-arn <value>]
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

`--index-id` (string)

The identifier of the index you want to map users to their groups.

`--data-source-id` (string)

The identifier of the data source you want to map users to their groups.

This is useful if a group is tied to multiple data sources, but you only want the group to access documents of a certain data source. For example, the groups âResearchâ, âEngineeringâ, and âSales and Marketingâ are all tied to the companyâs documents stored in the data sources Confluence and Salesforce. However, âSales and Marketingâ team only needs access to customer-related documents stored in Salesforce.

`--group-id` (string)

The identifier of the group you want to map its users to.

`--group-members` (structure)

The list that contains your users that belong the same group. This can include sub groups that belong to a group.

For example, the group âCompany Aâ includes the user âCEOâ and the sub groups âResearchâ, âEngineeringâ, and âSales and Marketingâ.

If you have more than 1000 users and/or sub groups for a single group, you need to provide the path to the S3 file that lists your users and sub groups for a group. Your sub groups can contain more than 1000 users, but the list of sub groups that belong to a group (and/or users) must be no more than 1000.

MemberGroups -> (list)

A list of users that belong to a group. This can also include sub groups. For example, the sub groups âResearchâ, âEngineeringâ, and âSales and Marketingâ all belong to the group âCompany Aâ.

(structure)

The sub groups that belong to a group.

GroupId -> (string)

The identifier of the sub group you want to map to a group.

DataSourceId -> (string)

The identifier of the data source for the sub group you want to map to a group.

MemberUsers -> (list)

A list of users that belong to a group. For example, a list of interns all belong to the âInternsâ group.

(structure)

The users that belong to a group.

UserId -> (string)

The identifier of the user you want to map to a group.

S3PathforGroupMembers -> (structure)

If you have more than 1000 users and/or sub groups for a single group, you need to provide the path to the S3 file that lists your users and sub groups for a group. Your sub groups can contain more than 1000 users, but the list of sub groups that belong to a group (and/or users) must be no more than 1000.

You can download this [example S3 file](https://docs.aws.amazon.com/kendra/latest/dg/samples/group_members.zip) that uses the correct format for listing group members. Note, `dataSourceId` is optional. The value of `type` for a group is always `GROUP` and for a user it is always `USER` .

Bucket -> (string)

The name of the S3 bucket that contains the file.

Key -> (string)

The name of the file.

Shorthand Syntax:

```
MemberGroups=[{GroupId=string,DataSourceId=string},{GroupId=string,DataSourceId=string}],MemberUsers=[{UserId=string},{UserId=string}],S3PathforGroupMembers={Bucket=string,Key=string}
```

JSON Syntax:

```
{
  "MemberGroups": [
    {
      "GroupId": "string",
      "DataSourceId": "string"
    }
    ...
  ],
  "MemberUsers": [
    {
      "UserId": "string"
    }
    ...
  ],
  "S3PathforGroupMembers": {
    "Bucket": "string",
    "Key": "string"
  }
}
```

`--ordering-id` (long)

The timestamp identifier you specify to ensure Amazon Kendra doesnât override the latest `PUT` action with previous actions. The highest number ID, which is the ordering ID, is the latest action you want to process and apply on top of other actions with lower number IDs. This prevents previous actions with lower number IDs from possibly overriding the latest action.

The ordering ID can be the Unix time of the last update you made to a group members list. You would then provide this list when calling `PutPrincipalMapping` . This ensures your `PUT` action for that updated group with the latest members list doesnât get overwritten by earlier `PUT` actions for the same group which are yet to be processed.

The default ordering ID is the current Unix time in milliseconds that the action was received by Amazon Kendra.

`--role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role that has access to the S3 file that contains your list of users that belong to a group.

For more information, see [IAM roles for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html#iam-roles-ds) .

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

None