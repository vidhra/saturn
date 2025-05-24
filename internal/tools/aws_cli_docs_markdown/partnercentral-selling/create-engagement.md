# create-engagementÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/create-engagement.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/create-engagement.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [partnercentral-selling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/index.html#cli-aws-partnercentral-selling) ]

# create-engagement

## Description

The `CreateEngagement` action allows you to create an `Engagement` , which serves as a collaborative space between different parties such as AWS Partners and AWS Sellers. This action automatically adds the callerâs AWS account as an active member of the newly created `Engagement` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/partnercentral-selling-2022-07-26/CreateEngagement)

## Synopsis

```
create-engagement
--catalog <value>
[--client-token <value>]
[--contexts <value>]
--description <value>
--title <value>
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

The `CreateEngagementRequest$Catalog` parameter specifies the catalog related to the engagement. Accepted values are `AWS` and `Sandbox` , which determine the environment in which the engagement is managed.

`--client-token` (string)

The `CreateEngagementRequest$ClientToken` parameter specifies a unique, case-sensitive identifier to ensure that the request is handled exactly once. The value must not exceed sixty-four alphanumeric characters.

`--contexts` (list)

The `Contexts` field is a required array of objects, with a maximum of 5 contexts allowed, specifying detailed information about customer projects associated with the Engagement. Each context object contains a `Type` field indicating the context type, which must be `CustomerProject` in this version, and a `Payload` field containing the `CustomerProject` details. The `CustomerProject` object is composed of two main components: `Customer` and `Project` . The `Customer` object includes information such as `CompanyName` , `WebsiteUrl` , `Industry` , and `CountryCode` , providing essential details about the customer. The `Project` object contains `Title` , `BusinessProblem` , and `TargetCompletionDate` , offering insights into the specific project associated with the customer. This structure allows comprehensive context to be included within the Engagement, facilitating effective collaboration between parties by providing relevant customer and project information.

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

JSON Syntax:

```
[
  {
    "Payload": {
      "CustomerProject": {
        "Customer": {
          "CompanyName": "string",
          "CountryCode": "US"|"AF"|"AX"|"AL"|"DZ"|"AS"|"AD"|"AO"|"AI"|"AQ"|"AG"|"AR"|"AM"|"AW"|"AU"|"AT"|"AZ"|"BS"|"BH"|"BD"|"BB"|"BY"|"BE"|"BZ"|"BJ"|"BM"|"BT"|"BO"|"BQ"|"BA"|"BW"|"BV"|"BR"|"IO"|"BN"|"BG"|"BF"|"BI"|"KH"|"CM"|"CA"|"CV"|"KY"|"CF"|"TD"|"CL"|"CN"|"CX"|"CC"|"CO"|"KM"|"CG"|"CK"|"CR"|"CI"|"HR"|"CU"|"CW"|"CY"|"CZ"|"CD"|"DK"|"DJ"|"DM"|"DO"|"EC"|"EG"|"SV"|"GQ"|"ER"|"EE"|"ET"|"FK"|"FO"|"FJ"|"FI"|"FR"|"GF"|"PF"|"TF"|"GA"|"GM"|"GE"|"DE"|"GH"|"GI"|"GR"|"GL"|"GD"|"GP"|"GU"|"GT"|"GG"|"GN"|"GW"|"GY"|"HT"|"HM"|"VA"|"HN"|"HK"|"HU"|"IS"|"IN"|"ID"|"IR"|"IQ"|"IE"|"IM"|"IL"|"IT"|"JM"|"JP"|"JE"|"JO"|"KZ"|"KE"|"KI"|"KR"|"KW"|"KG"|"LA"|"LV"|"LB"|"LS"|"LR"|"LY"|"LI"|"LT"|"LU"|"MO"|"MK"|"MG"|"MW"|"MY"|"MV"|"ML"|"MT"|"MH"|"MQ"|"MR"|"MU"|"YT"|"MX"|"FM"|"MD"|"MC"|"MN"|"ME"|"MS"|"MA"|"MZ"|"MM"|"NA"|"NR"|"NP"|"NL"|"AN"|"NC"|"NZ"|"NI"|"NE"|"NG"|"NU"|"NF"|"MP"|"NO"|"OM"|"PK"|"PW"|"PS"|"PA"|"PG"|"PY"|"PE"|"PH"|"PN"|"PL"|"PT"|"PR"|"QA"|"RE"|"RO"|"RU"|"RW"|"BL"|"SH"|"KN"|"LC"|"MF"|"PM"|"VC"|"WS"|"SM"|"ST"|"SA"|"SN"|"RS"|"SC"|"SL"|"SG"|"SX"|"SK"|"SI"|"SB"|"SO"|"ZA"|"GS"|"SS"|"ES"|"LK"|"SD"|"SR"|"SJ"|"SZ"|"SE"|"CH"|"SY"|"TW"|"TJ"|"TZ"|"TH"|"TL"|"TG"|"TK"|"TO"|"TT"|"TN"|"TR"|"TM"|"TC"|"TV"|"UG"|"UA"|"AE"|"GB"|"UM"|"UY"|"UZ"|"VU"|"VE"|"VN"|"VG"|"VI"|"WF"|"EH"|"YE"|"ZM"|"ZW",
          "Industry": "Aerospace"|"Agriculture"|"Automotive"|"Computers and Electronics"|"Consumer Goods"|"Education"|"Energy - Oil and Gas"|"Energy - Power and Utilities"|"Financial Services"|"Gaming"|"Government"|"Healthcare"|"Hospitality"|"Life Sciences"|"Manufacturing"|"Marketing and Advertising"|"Media and Entertainment"|"Mining"|"Non-Profit Organization"|"Professional Services"|"Real Estate and Construction"|"Retail"|"Software and Internet"|"Telecommunications"|"Transportation and Logistics"|"Travel"|"Wholesale and Distribution"|"Other",
          "WebsiteUrl": "string"
        },
        "Project": {
          "BusinessProblem": "string",
          "TargetCompletionDate": "string",
          "Title": "string"
        }
      }
    },
    "Type": "CustomerProject"
  }
  ...
]
```

`--description` (string)

Provides a description of the `Engagement` .

`--title` (string)

Specifies the title of the `Engagement` .

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

The Amazon Resource Name (ARN) that identifies the engagement.

Id -> (string)

Unique identifier assigned to the newly created engagement.