# create-engagement-invitationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/create-engagement-invitation.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/create-engagement-invitation.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [partnercentral-selling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/index.html#cli-aws-partnercentral-selling) ]

# create-engagement-invitation

## Description

This action creates an invitation from a sender to a single receiver to join an engagement.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/partnercentral-selling-2022-07-26/CreateEngagementInvitation)

## Synopsis

```
create-engagement-invitation
--catalog <value>
[--client-token <value>]
--engagement-identifier <value>
--invitation <value>
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

Specifies the catalog related to the engagement. Accepted values are `AWS` and `Sandbox` , which determine the environment in which the engagement is managed.

`--client-token` (string)

Specifies a unique, client-generated UUID to ensure that the request is handled exactly once. This token helps prevent duplicate invitation creations.

`--engagement-identifier` (string)

The unique identifier of the `Engagement` associated with the invitation. This parameter ensures the invitation is created within the correct `Engagement` context.

`--invitation` (structure)

The `Invitation` object all information necessary to initiate an engagement invitation to a partner. It contains a personalized message from the sender, the invitationâs receiver, and a payload. The `Payload` can be the `OpportunityInvitation` , which includes detailed structures for sender contacts, partner responsibilities, customer information, and project details.

Message -> (string)

A message accompanying the invitation.

Payload -> (tagged union structure)

Contains the data payload associated with the Engagement Invitation. This payload includes essential details related to the AWS opportunity and is used by partners to evaluate whether to accept or reject the engagement.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `OpportunityInvitation`.

OpportunityInvitation -> (structure)

Specifies the details of the opportunity invitation within the Engagement Invitation payload. This data helps partners understand the context, scope, and expected involvement for the opportunity from AWS.

Customer -> (structure)

Contains information about the customer related to the opportunity in the Engagement Invitation. This data helps partners understand the customerâs profile and requirements.

CompanyName -> (string)

Represents the name of the customerâs company associated with the Engagement Invitation. This field is used to identify the customer.

CountryCode -> (string)

Indicates the country in which the customerâs company operates. This field is useful for understanding regional requirements or compliance needs.

Industry -> (string)

Specifies the industry to which the customerâs company belongs. This field helps categorize the opportunity based on the customerâs business sector.

WebsiteUrl -> (string)

Provides the website URL of the customerâs company. This field helps partners verify the legitimacy and size of the customer organization.

Project -> (structure)

Describes the project details associated with the opportunity, including the customerâs needs and the scope of work expected to be performed.

BusinessProblem -> (string)

Describes the business problem that the project aims to solve. This information is crucial for understanding the projectâs goals and objectives.

ExpectedCustomerSpend -> (list)

Contains revenue estimates for the partner related to the project. This field provides an idea of the financial potential of the opportunity for the partner.

(structure)

Provides an estimate of the revenue that the partner is expected to generate from the opportunity. This information helps partners assess the financial value of the project.

Amount -> (string)

Represents the estimated monthly revenue that the partner expects to earn from the opportunity. This helps in forecasting financial returns.

CurrencyCode -> (string)

Indicates the currency in which the revenue estimate is provided. This helps in understanding the financial impact across different markets.

EstimationUrl -> (string)

A URL providing additional information or context about the spend estimation.

Frequency -> (string)

Indicates how frequently the customer is expected to spend the projected amount. This can include values such as `Monthly` , `Quarterly` , or `Annually` . The default value is `Monthly` , representing recurring monthly spend.

TargetCompany -> (string)

Specifies the name of the partner company that is expected to generate revenue from the opportunity. This field helps track the partnerâs involvement in the opportunity.

TargetCompletionDate -> (string)

Specifies the estimated date of project completion. This field helps track the project timeline and manage expectations.

Title -> (string)

Specifies the title of the project. This title helps partners quickly identify and understand the focus of the project.

ReceiverResponsibilities -> (list)

Outlines the responsibilities or expectations of the receiver in the context of the invitation.

(string)

SenderContacts -> (list)

Represents the contact details of the AWS representatives involved in sending the Engagement Invitation. These contacts are opportunity stakeholders.

(structure)

An object that contains the details of the sender-provided contact person for the `EngagementInvitation` .

BusinessTitle -> (string)

The sender-provided contactâs title (job title or role) associated with the `EngagementInvitation` .

Email -> (string)

The sender-provided contactâs email address associated with the `EngagementInvitation` .

FirstName -> (string)

The sender-provided contactâs last name associated with the `EngagementInvitation` .

LastName -> (string)

The sender-provided contactâs first name associated with the `EngagementInvitation` .

Phone -> (string)

The sender-provided contactâs phone number associated with the `EngagementInvitation` .

Receiver -> (tagged union structure)

Represents the entity that received the Engagement Invitation, including account and company details. This field is essential for tracking the partner who is being invited to collaborate.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Account`.

Account -> (structure)

Specifies the AWS account of the partner who received the Engagement Invitation. This field is used to track the invitation recipient within the AWS ecosystem.

Alias -> (string)

Represents the alias of the partner account receiving the Engagement Invitation, making it easier to identify and track the recipient in reports or logs.

AwsAccountId -> (string)

Indicates the AWS account ID of the partner who received the Engagement Invitation. This is a unique identifier for managing engagements with specific AWS accounts.

JSON Syntax:

```
{
  "Message": "string",
  "Payload": {
    "OpportunityInvitation": {
      "Customer": {
        "CompanyName": "string",
        "CountryCode": "US"|"AF"|"AX"|"AL"|"DZ"|"AS"|"AD"|"AO"|"AI"|"AQ"|"AG"|"AR"|"AM"|"AW"|"AU"|"AT"|"AZ"|"BS"|"BH"|"BD"|"BB"|"BY"|"BE"|"BZ"|"BJ"|"BM"|"BT"|"BO"|"BQ"|"BA"|"BW"|"BV"|"BR"|"IO"|"BN"|"BG"|"BF"|"BI"|"KH"|"CM"|"CA"|"CV"|"KY"|"CF"|"TD"|"CL"|"CN"|"CX"|"CC"|"CO"|"KM"|"CG"|"CK"|"CR"|"CI"|"HR"|"CU"|"CW"|"CY"|"CZ"|"CD"|"DK"|"DJ"|"DM"|"DO"|"EC"|"EG"|"SV"|"GQ"|"ER"|"EE"|"ET"|"FK"|"FO"|"FJ"|"FI"|"FR"|"GF"|"PF"|"TF"|"GA"|"GM"|"GE"|"DE"|"GH"|"GI"|"GR"|"GL"|"GD"|"GP"|"GU"|"GT"|"GG"|"GN"|"GW"|"GY"|"HT"|"HM"|"VA"|"HN"|"HK"|"HU"|"IS"|"IN"|"ID"|"IR"|"IQ"|"IE"|"IM"|"IL"|"IT"|"JM"|"JP"|"JE"|"JO"|"KZ"|"KE"|"KI"|"KR"|"KW"|"KG"|"LA"|"LV"|"LB"|"LS"|"LR"|"LY"|"LI"|"LT"|"LU"|"MO"|"MK"|"MG"|"MW"|"MY"|"MV"|"ML"|"MT"|"MH"|"MQ"|"MR"|"MU"|"YT"|"MX"|"FM"|"MD"|"MC"|"MN"|"ME"|"MS"|"MA"|"MZ"|"MM"|"NA"|"NR"|"NP"|"NL"|"AN"|"NC"|"NZ"|"NI"|"NE"|"NG"|"NU"|"NF"|"MP"|"NO"|"OM"|"PK"|"PW"|"PS"|"PA"|"PG"|"PY"|"PE"|"PH"|"PN"|"PL"|"PT"|"PR"|"QA"|"RE"|"RO"|"RU"|"RW"|"BL"|"SH"|"KN"|"LC"|"MF"|"PM"|"VC"|"WS"|"SM"|"ST"|"SA"|"SN"|"RS"|"SC"|"SL"|"SG"|"SX"|"SK"|"SI"|"SB"|"SO"|"ZA"|"GS"|"SS"|"ES"|"LK"|"SD"|"SR"|"SJ"|"SZ"|"SE"|"CH"|"SY"|"TW"|"TJ"|"TZ"|"TH"|"TL"|"TG"|"TK"|"TO"|"TT"|"TN"|"TR"|"TM"|"TC"|"TV"|"UG"|"UA"|"AE"|"GB"|"UM"|"UY"|"UZ"|"VU"|"VE"|"VN"|"VG"|"VI"|"WF"|"EH"|"YE"|"ZM"|"ZW",
        "Industry": "Aerospace"|"Agriculture"|"Automotive"|"Computers and Electronics"|"Consumer Goods"|"Education"|"Energy - Oil and Gas"|"Energy - Power and Utilities"|"Financial Services"|"Gaming"|"Government"|"Healthcare"|"Hospitality"|"Life Sciences"|"Manufacturing"|"Marketing and Advertising"|"Media and Entertainment"|"Mining"|"Non-Profit Organization"|"Professional Services"|"Real Estate and Construction"|"Retail"|"Software and Internet"|"Telecommunications"|"Transportation and Logistics"|"Travel"|"Wholesale and Distribution"|"Other",
        "WebsiteUrl": "string"
      },
      "Project": {
        "BusinessProblem": "string",
        "ExpectedCustomerSpend": [
          {
            "Amount": "string",
            "CurrencyCode": "USD"|"EUR"|"GBP"|"AUD"|"CAD"|"CNY"|"NZD"|"INR"|"JPY"|"CHF"|"SEK"|"AED"|"AFN"|"ALL"|"AMD"|"ANG"|"AOA"|"ARS"|"AWG"|"AZN"|"BAM"|"BBD"|"BDT"|"BGN"|"BHD"|"BIF"|"BMD"|"BND"|"BOB"|"BOV"|"BRL"|"BSD"|"BTN"|"BWP"|"BYN"|"BZD"|"CDF"|"CHE"|"CHW"|"CLF"|"CLP"|"COP"|"COU"|"CRC"|"CUC"|"CUP"|"CVE"|"CZK"|"DJF"|"DKK"|"DOP"|"DZD"|"EGP"|"ERN"|"ETB"|"FJD"|"FKP"|"GEL"|"GHS"|"GIP"|"GMD"|"GNF"|"GTQ"|"GYD"|"HKD"|"HNL"|"HRK"|"HTG"|"HUF"|"IDR"|"ILS"|"IQD"|"IRR"|"ISK"|"JMD"|"JOD"|"KES"|"KGS"|"KHR"|"KMF"|"KPW"|"KRW"|"KWD"|"KYD"|"KZT"|"LAK"|"LBP"|"LKR"|"LRD"|"LSL"|"LYD"|"MAD"|"MDL"|"MGA"|"MKD"|"MMK"|"MNT"|"MOP"|"MRU"|"MUR"|"MVR"|"MWK"|"MXN"|"MXV"|"MYR"|"MZN"|"NAD"|"NGN"|"NIO"|"NOK"|"NPR"|"OMR"|"PAB"|"PEN"|"PGK"|"PHP"|"PKR"|"PLN"|"PYG"|"QAR"|"RON"|"RSD"|"RUB"|"RWF"|"SAR"|"SBD"|"SCR"|"SDG"|"SGD"|"SHP"|"SLL"|"SOS"|"SRD"|"SSP"|"STN"|"SVC"|"SYP"|"SZL"|"THB"|"TJS"|"TMT"|"TND"|"TOP"|"TRY"|"TTD"|"TWD"|"TZS"|"UAH"|"UGX"|"USN"|"UYI"|"UYU"|"UZS"|"VEF"|"VND"|"VUV"|"WST"|"XAF"|"XCD"|"XDR"|"XOF"|"XPF"|"XSU"|"XUA"|"YER"|"ZAR"|"ZMW"|"ZWL",
            "EstimationUrl": "string",
            "Frequency": "Monthly",
            "TargetCompany": "string"
          }
          ...
        ],
        "TargetCompletionDate": "string",
        "Title": "string"
      },
      "ReceiverResponsibilities": ["Distributor"|"Reseller"|"Hardware Partner"|"Managed Service Provider"|"Software Partner"|"Services Partner"|"Training Partner"|"Co-Sell Facilitator"|"Facilitator", ...],
      "SenderContacts": [
        {
          "BusinessTitle": "string",
          "Email": "string",
          "FirstName": "string",
          "LastName": "string",
          "Phone": "string"
        }
        ...
      ]
    }
  },
  "Receiver": {
    "Account": {
      "Alias": "string",
      "AwsAccountId": "string"
    }
  }
}
```

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

The Amazon Resource Name (ARN) that uniquely identifies the engagement invitation.

Id -> (string)

Unique identifier assigned to the newly created engagement invitation.