# assign-opportunityÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/assign-opportunity.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/assign-opportunity.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [partnercentral-selling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/index.html#cli-aws-partnercentral-selling) ]

# assign-opportunity

## Description

Enables you to reassign an existing `Opportunity` to another user within your Partner Central account. The specified user receives the opportunity, and it appears on their Partner Central dashboard, allowing them to take necessary actions or proceed with the opportunity.

This is useful for distributing opportunities to the appropriate team members or departments within your organization, ensuring that each opportunity is handled by the right person. By default, the opportunity owner is the one who creates it. Currently, thereâs no API to enumerate the list of available users.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/partnercentral-selling-2022-07-26/AssignOpportunity)

## Synopsis

```
assign-opportunity
--assignee <value>
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

`--assignee` (structure)

Specifies the user or team member responsible for managing the assigned opportunity. This field identifies the *Assignee* based on the partnerâs internal team structure. Ensure that the email address is associated with a registered user in your Partner Central account.

BusinessTitle -> (string)

Specifies the business title of the assignee managing the opportunity. This helps clarify the individualâs role and responsibilities within the organization. Use the value `PartnerAccountManager` to update details of the opportunity owner.

Email -> (string)

Provides the email address of the assignee. This email is used for communications and notifications related to the opportunity.

FirstName -> (string)

Specifies the first name of the assignee managing the opportunity. The system automatically retrieves this value from the user profile by referencing the associated email address.

LastName -> (string)

Specifies the last name of the assignee managing the opportunity. The system automatically retrieves this value from the user profile by referencing the associated email address.

Shorthand Syntax:

```
BusinessTitle=string,Email=string,FirstName=string,LastName=string
```

JSON Syntax:

```
{
  "BusinessTitle": "string",
  "Email": "string",
  "FirstName": "string",
  "LastName": "string"
}
```

`--catalog` (string)

Specifies the catalog associated with the request. This field takes a string value from a predefined list: `AWS` or `Sandbox` . The catalog determines which environment the opportunity is assigned in. Use `AWS` to assign real opportunities in the Amazon Web Services catalog, and `Sandbox` for testing in secure, isolated environments.

`--identifier` (string)

Requires the `Opportunity` âs unique identifier when you want to assign it to another user. Provide the correct identifier so the intended opportunity is reassigned.

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