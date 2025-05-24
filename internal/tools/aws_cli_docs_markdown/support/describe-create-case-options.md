# describe-create-case-optionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-create-case-options.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-create-case-options.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [support](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/index.html#cli-aws-support) ]

# describe-create-case-options

## Description

Returns a list of CreateCaseOption types along with the corresponding supported hours and language availability. You can specify the `language` `categoryCode` , `issueType` and `serviceCode` used to retrieve the CreateCaseOptions.

### Note

- You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API.
- If you call the Amazon Web Services Support API from an account that doesnât have a Business, Enterprise On-Ramp, or Enterprise Support plan, the `SubscriptionRequiredException` error message appears. For information about changing your support plan, see [Amazon Web Services Support](http://aws.amazon.com/premiumsupport/) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeCreateCaseOptions)

## Synopsis

```
describe-create-case-options
--issue-type <value>
--service-code <value>
--language <value>
--category-code <value>
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

`--issue-type` (string)

The type of issue for the case. You can specify `customer-service` or `technical` . If you donât specify a value, the default is `technical` .

`--service-code` (string)

The code for the Amazon Web Services service. You can use the  DescribeServices operation to get the possible `serviceCode` values.

`--language` (string)

The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (âzhâ), English (âenâ), Japanese (âjaâ) and Korean (âkoâ). You must specify the ISO 639-1 code for the `language` parameter if you want support in that language.

`--category-code` (string)

The category of problem for the support case. You also use the  DescribeServices operation to get the category code for a service. Each Amazon Web Services service defines its own set of category codes.

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

languageAvailability -> (string)

Language availability can be any of the following:

- available
- best_effort
- unavailable

communicationTypes -> (list)

A JSON-formatted array that contains the available communication type options, along with the available support timeframes for the given inputs.

(structure)

A JSON-formatted object that contains the CommunicationTypeOptions for creating a case for a certain communication channel. It is contained in the response from a  DescribeCreateCaseOptions request. **CommunicationTypeOptions** contains the following fields:

- **datesWithoutSupport** - A JSON-formatted list containing date and time ranges for periods without support in UTC time. Date and time format is RFC 3339 : âyyyy-MM-ddâTâHH:mm:ss.SSSZZâ.
- **supportedHours** - A JSON-formatted list containing time ranges when support are available. Time format is RFC 3339 : âHH:mm:ss.SSSâ.
- **type** - A string value indicating the communication type that the aforementioned rules apply to. At the moment the type value can assume one of 3 values at the moment `chat` , `web` and `call` .

type -> (string)

A string value indicating the communication type. At the moment the type value can assume one of 3 values at the moment chat, web and call.

supportedHours -> (list)

A JSON-formatted list containing time ranges when support is available.

(structure)

Time range object with `startTime` and `endTime` range in RFC 3339 format. `'HH:mm:ss.SSS'` .

startTime -> (string)

Start Time. RFC 3339 format `'HH:mm:ss.SSS'` .

endTime -> (string)

End Time. RFC 3339 format `'HH:mm:ss.SSS'` .

datesWithoutSupport -> (list)

A JSON-formatted list containing date and time ranges for periods without support

(structure)

Date and time (UTC) format in RFC 3339 : âyyyy-MM-ddâTâHH:mm:ss.SSSZZâ.

startDateTime -> (string)

A JSON object containing start and date time (UTC). Date and time format is RFC 3339 : âyyyy-MM-ddâTâHH:mm:ss.SSSZZâ.

endDateTime -> (string)

End Date Time (UTC). RFC 3339 format : âyyyy-MM-ddâTâHH:mm:ss.SSSZZâ.