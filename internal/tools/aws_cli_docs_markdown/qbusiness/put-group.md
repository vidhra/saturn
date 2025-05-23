# put-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/put-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/put-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qbusiness](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/index.html#cli-aws-qbusiness) ]

# put-group

## Description

Create, or updates, a mapping of usersâwho have access to a documentâto groups.

You can also map sub groups to groups. For example, the group âCompany Intellectual Property Teamsâ includes sub groups âResearchâ and âEngineeringâ. These sub groups include their own list of users or people who work in these teams. Only users who work in research and engineering, and therefore belong in the intellectual property group, can see top-secret company documents in their Amazon Q Business chat results.

There are two options for creating groups, either passing group members inline or using an S3 file via the S3PathForGroupMembers field. For inline groups, there is a limit of 1000 members per group and for provided S3 files there is a limit of 100 thousand members. When creating a group using an S3 file, you provide both an S3 file and a `RoleArn` for Amazon Q Buisness to access the file.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qbusiness-2023-11-27/PutGroup)

## Synopsis

```
put-group
--application-id <value>
--index-id <value>
--group-name <value>
[--data-source-id <value>]
--type <value>
--group-members <value>
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

`--application-id` (string)

The identifier of the application in which the user and group mapping belongs.

`--index-id` (string)

The identifier of the index in which you want to map users to their groups.

`--group-name` (string)

The list that contains your users or sub groups that belong the same group. For example, the group âCompanyâ includes the user âCEOâ and the sub groups âResearchâ, âEngineeringâ, and âSales and Marketingâ.

`--data-source-id` (string)

The identifier of the data source for which you want to map users to their groups. This is useful if a group is tied to multiple data sources, but you only want the group to access documents of a certain data source. For example, the groups âResearchâ, âEngineeringâ, and âSales and Marketingâ are all tied to the companyâs documents stored in the data sources Confluence and Salesforce. However, âSales and Marketingâ team only needs access to customer-related documents stored in Salesforce.

`--type` (string)

The type of the group.

Possible values:

- `INDEX`
- `DATASOURCE`

`--group-members` (structure)

A list of users or sub groups that belong to a group. This is for generating Amazon Q Business chat results only from document a user has access to.

memberGroups -> (list)

A list of sub groups that belong to a group. For example, the sub groups âResearchâ, âEngineeringâ, and âSales and Marketingâ all belong to the group âCompanyâ.

(structure)

The sub groups that belong to a group.

groupName -> (string)

The name of the sub group.

type -> (string)

The type of the sub group.

memberUsers -> (list)

A list of users that belong to a group. For example, a list of interns all belong to the âInternsâ group.

(structure)

The users that belong to a group.

userId -> (string)

The identifier of the user you want to map to a group.

type -> (string)

The type of the user.

s3PathForGroupMembers -> (structure)

Information required for Amazon Q Business to find a specific file in an Amazon S3 bucket.

bucket -> (string)

The name of the S3 bucket that contains the file.

key -> (string)

The name of the file.

Shorthand Syntax:

```
memberGroups=[{groupName=string,type=string},{groupName=string,type=string}],memberUsers=[{userId=string,type=string},{userId=string,type=string}],s3PathForGroupMembers={bucket=string,key=string}
```

JSON Syntax:

```
{
  "memberGroups": [
    {
      "groupName": "string",
      "type": "INDEX"|"DATASOURCE"
    }
    ...
  ],
  "memberUsers": [
    {
      "userId": "string",
      "type": "INDEX"|"DATASOURCE"
    }
    ...
  ],
  "s3PathForGroupMembers": {
    "bucket": "string",
    "key": "string"
  }
}
```

`--role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role that has access to the S3 file that contains your list of users that belong to a group.

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