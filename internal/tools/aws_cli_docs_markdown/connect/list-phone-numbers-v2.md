# list-phone-numbers-v2Â¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-phone-numbers-v2.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-phone-numbers-v2.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# list-phone-numbers-v2

## Description

Lists phone numbers claimed to your Amazon Connect instance or traffic distribution group. If the provided `TargetArn` is a traffic distribution group, you can call this API in both Amazon Web Services Regions associated with traffic distribution group.

For more information about phone numbers, see [Set Up Phone Numbers for Your Contact Center](https://docs.aws.amazon.com/connect/latest/adminguide/contact-center-phone-number.html) in the *Amazon Connect Administrator Guide* .

### Note

- When given an instance ARN, `ListPhoneNumbersV2` returns only the phone numbers claimed to the instance.
- When given a traffic distribution group ARN `ListPhoneNumbersV2` returns only the phone numbers claimed to the traffic distribution group.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListPhoneNumbersV2)

`list-phone-numbers-v2` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ListPhoneNumbersSummaryList`

## Synopsis

```
list-phone-numbers-v2
[--target-arn <value>]
[--instance-id <value>]
[--phone-number-country-codes <value>]
[--phone-number-types <value>]
[--phone-number-prefix <value>]
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

`--target-arn` (string)

The Amazon Resource Name (ARN) for Amazon Connect instances or traffic distribution groups that phone number inbound traffic is routed through. If both `TargetArn` and `InstanceId` input are not provided, this API lists numbers claimed to all the Amazon Connect instances belonging to your account in the same Amazon Web Services Region as the request.

`--instance-id` (string)

The identifier of the Amazon Connect instance that phone numbers are claimed to. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance. If both `TargetArn` and `InstanceId` are not provided, this API lists numbers claimed to all the Amazon Connect instances belonging to your account in the same AWS Region as the request.

`--phone-number-country-codes` (list)

The ISO country code.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  AF
  AL
  DZ
  AS
  AD
  AO
  AI
  AQ
  AG
  AR
  AM
  AW
  AU
  AT
  AZ
  BS
  BH
  BD
  BB
  BY
  BE
  BZ
  BJ
  BM
  BT
  BO
  BA
  BW
  BR
  IO
  VG
  BN
  BG
  BF
  BI
  KH
  CM
  CA
  CV
  KY
  CF
  TD
  CL
  CN
  CX
  CC
  CO
  KM
  CK
  CR
  HR
  CU
  CW
  CY
  CZ
  CD
  DK
  DJ
  DM
  DO
  TL
  EC
  EG
  SV
  GQ
  ER
  EE
  ET
  FK
  FO
  FJ
  FI
  FR
  PF
  GA
  GM
  GE
  DE
  GH
  GI
  GR
  GL
  GD
  GU
  GT
  GG
  GN
  GW
  GY
  HT
  HN
  HK
  HU
  IS
  IN
  ID
  IR
  IQ
  IE
  IM
  IL
  IT
  CI
  JM
  JP
  JE
  JO
  KZ
  KE
  KI
  KW
  KG
  LA
  LV
  LB
  LS
  LR
  LY
  LI
  LT
  LU
  MO
  MK
  MG
  MW
  MY
  MV
  ML
  MT
  MH
  MR
  MU
  YT
  MX
  FM
  MD
  MC
  MN
  ME
  MS
  MA
  MZ
  MM
  NA
  NR
  NP
  NL
  AN
  NC
  NZ
  NI
  NE
  NG
  NU
  KP
  MP
  NO
  OM
  PK
  PW
  PA
  PG
  PY
  PE
  PH
  PN
  PL
  PT
  PR
  QA
  CG
  RE
  RO
  RU
  RW
  BL
  SH
  KN
  LC
  MF
  PM
  VC
  WS
  SM
  ST
  SA
  SN
  RS
  SC
  SL
  SG
  SX
  SK
  SI
  SB
  SO
  ZA
  KR
  ES
  LK
  SD
  SR
  SJ
  SZ
  SE
  CH
  SY
  TW
  TJ
  TZ
  TH
  TG
  TK
  TO
  TT
  TN
  TR
  TM
  TC
  TV
  VI
  UG
  UA
  AE
  GB
  US
  UY
  UZ
  VU
  VA
  VE
  VN
  WF
  EH
  YE
  ZM
  ZW
```

`--phone-number-types` (list)

The type of phone number.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  TOLL_FREE
  DID
  UIFN
  SHARED
  THIRD_PARTY_TF
  THIRD_PARTY_DID
  SHORT_CODE
```

`--phone-number-prefix` (string)

The prefix of the phone number. If provided, it must contain `+` as part of the country code.

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

## Output

NextToken -> (string)

If there are additional results, this is the token for the next set of results.

ListPhoneNumbersSummaryList -> (list)

Information about phone numbers that have been claimed to your Amazon Connect instances or traffic distribution groups.

(structure)

Information about phone numbers that have been claimed to your Amazon Connect instance or traffic distribution group.

PhoneNumberId -> (string)

A unique identifier for the phone number.

PhoneNumberArn -> (string)

The Amazon Resource Name (ARN) of the phone number.

PhoneNumber -> (string)

The phone number. Phone numbers are formatted `[+] [country code] [subscriber number including area code]` .

PhoneNumberCountryCode -> (string)

The ISO country code.

PhoneNumberType -> (string)

The type of phone number.

TargetArn -> (string)

The Amazon Resource Name (ARN) for Amazon Connect instances or traffic distribution groups that phone number inbound traffic is routed through.

InstanceId -> (string)

The identifier of the Amazon Connect instance that phone numbers are claimed to. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.

PhoneNumberDescription -> (string)

The description of the phone number.

SourcePhoneNumberArn -> (string)

The claimed phone number ARN that was previously imported from the external service, such as Amazon Web Services End User Messaging. If it is from Amazon Web Services End User Messaging, it looks like the ARN of the phone number that was imported from Amazon Web Services End User Messaging.