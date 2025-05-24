# get-engagementÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/get-engagement.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/get-engagement.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [partnercentral-selling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/index.html#cli-aws-partnercentral-selling) ]

# get-engagement

## Description

Use this action to retrieve the engagement record for a given `EngagementIdentifier` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/partnercentral-selling-2022-07-26/GetEngagement)

## Synopsis

```
get-engagement
--catalog <value>
--identifier <value>
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

`--catalog` (string)

Specifies the catalog related to the engagement request. Valid values are `AWS` and `Sandbox` .

`--identifier` (string)

Specifies the identifier of the Engagement record to retrieve.

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

Arn -> (string)

The Amazon Resource Name (ARN) of the engagement retrieved.

Contexts -> (list)

A list of context objects associated with the engagement. Each context provides additional information related to the Engagement, such as customer projects or documents.

(structure)

Provides detailed context information for an Engagement. This structure allows for specifying the type of context and its associated payload.

Payload -> (tagged union structure)

Contains the specific details of the Engagement context. The structure of this payload varies depending on the Type field.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `CustomerProject`.

CustomerProject -> (structure)

Contains detailed information about a customer project when the context type is âCustomerProjectâ. This field is present only when the Type in EngagementContextDetails is set to âCustomerProjectâ.

Customer -> (structure)

Contains details about the customer associated with the Engagement Invitation, including company information and industry.

CompanyName -> (string)

Represents the name of the customerâs company associated with the Engagement Invitation. This field is used to identify the customer.

CountryCode -> (string)

Indicates the country in which the customerâs company operates. This field is useful for understanding regional requirements or compliance needs.

Industry -> (string)

Specifies the industry to which the customerâs company belongs. This field helps categorize the opportunity based on the customerâs business sector.

WebsiteUrl -> (string)

Provides the website URL of the customerâs company. This field helps partners verify the legitimacy and size of the customer organization.

Project -> (structure)

Information about the customer project associated with the Engagement.

BusinessProblem -> (string)

A description of the business problem the project aims to solve.

TargetCompletionDate -> (string)

The target completion date for the customerâs project.

Title -> (string)

The title of the project.

Type -> (string)

Specifies the type of Engagement context. Valid values are âCustomerProjectâ or âDocumentâ, indicating whether the context relates to a customer project or a document respectively.

CreatedAt -> (timestamp)

The date and time when the Engagement was created, presented in ISO 8601 format (UTC). For example: â2023-05-01T20:37:46Zâ. This timestamp helps track the lifecycle of the Engagement.

CreatedBy -> (string)

The AWS account ID of the user who originally created the engagement. This field helps in tracking the origin of the engagement.

Description -> (string)

A more detailed description of the engagement. This provides additional context or information about the engagementâs purpose or scope.

Id -> (string)

The unique resource identifier of the engagement retrieved.

MemberCount -> (integer)

Specifies the current count of members participating in the Engagement. This count includes all active members regardless of their roles or permissions within the Engagement.

Title -> (string)

The title of the engagement. It provides a brief, descriptive name for the engagement that is meaningful and easily recognizable.