# list-indicatorsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/list-indicators.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/list-indicators.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [detective](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/index.html#cli-aws-detective) ]

# list-indicators

## Description

Gets the indicators from an investigation. You can use the information from the indicators to determine if an IAM user and/or IAM role is involved in an unusual activity that could indicate malicious behavior and its impact.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/detective-2018-10-26/ListIndicators)

## Synopsis

```
list-indicators
--graph-arn <value>
--investigation-id <value>
[--indicator-type <value>]
[--next-token <value>]
[--max-results <value>]
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

`--graph-arn` (string)

The Amazon Resource Name (ARN) of the behavior graph.

`--investigation-id` (string)

The investigation ID of the investigation report.

`--indicator-type` (string)

For the list of indicators of compromise that are generated by Detective investigations, see [Detective investigations](https://docs.aws.amazon.com/detective/latest/userguide/detective-investigation-about.html) .

Possible values:

- `TTP_OBSERVED`
- `IMPOSSIBLE_TRAVEL`
- `FLAGGED_IP_ADDRESS`
- `NEW_GEOLOCATION`
- `NEW_ASO`
- `NEW_USER_AGENT`
- `RELATED_FINDING`
- `RELATED_FINDING_GROUP`

`--next-token` (string)

Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.

Each pagination token expires after 24 hours. Using an expired pagination token will return a Validation Exception error.

`--max-results` (integer)

Lists the maximum number of indicators in a page.

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

GraphArn -> (string)

The Amazon Resource Name (ARN) of the behavior graph.

InvestigationId -> (string)

The investigation ID of the investigation report.

NextToken -> (string)

Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.

Each pagination token expires after 24 hours. Using an expired pagination token will return a Validation Exception error.

Indicators -> (list)

Lists the indicators of compromise.

(structure)

Detective investigations triages indicators of compromises such as a finding and surfaces only the most critical and suspicious issues, so you can focus on high-level investigations. An `Indicator` lets you determine if an Amazon Web Services resource is involved in unusual activity that could indicate malicious behavior and its impact.

IndicatorType -> (string)

The type of indicator.

IndicatorDetail -> (structure)

Details about the indicators of compromise that are used to determine if a resource is involved in a security incident. An indicator of compromise (IOC) is an artifact observed in or on a network, system, or environment that can (with a high level of confidence) identify malicious activity or a security incident.

TTPsObservedDetail -> (structure)

Details about the indicator of compromise.

Tactic -> (string)

The tactic used, identified by the investigation.

Technique -> (string)

The technique used, identified by the investigation.

Procedure -> (string)

The procedure used, identified by the investigation.

IpAddress -> (string)

The IP address where the tactics, techniques, and procedure (TTP) was observed.

APIName -> (string)

The name of the API where the tactics, techniques, and procedure (TTP) was observed.

APISuccessCount -> (long)

The total number of successful API requests.

APIFailureCount -> (long)

The total number of failed API requests.

ImpossibleTravelDetail -> (structure)

Identifies unusual and impossible user activity for an account.

StartingIpAddress -> (string)

IP address where the resource was first used in the impossible travel.

EndingIpAddress -> (string)

IP address where the resource was last used in the impossible travel.

StartingLocation -> (string)

Location where the resource was first used in the impossible travel.

EndingLocation -> (string)

Location where the resource was last used in the impossible travel.

HourlyTimeDelta -> (integer)

Returns the time difference between the first and last timestamp the resource was used.

FlaggedIpAddressDetail -> (structure)

Suspicious IP addresses that are flagged, which indicates critical or severe threats based on threat intelligence by Detective. This indicator is derived from Amazon Web Services threat intelligence.

IpAddress -> (string)

IP address of the suspicious entity.

Reason -> (string)

Details the reason the IP address was flagged as suspicious.

NewGeolocationDetail -> (structure)

Contains details about the new geographic location.

Location -> (string)

Location where the resource was accessed.

IpAddress -> (string)

IP address using which the resource was accessed.

IsNewForEntireAccount -> (boolean)

Checks if the geolocation is new for the entire account.

NewAsoDetail -> (structure)

Contains details about the new Autonomous System Organization (ASO).

Aso -> (string)

Details about the new Autonomous System Organization (ASO).

IsNewForEntireAccount -> (boolean)

Checks if the Autonomous System Organization (ASO) is new for the entire account.

NewUserAgentDetail -> (structure)

Contains details about the new user agent.

UserAgent -> (string)

New user agent which accessed the resource.

IsNewForEntireAccount -> (boolean)

Checks if the user agent is new for the entire account.

RelatedFindingDetail -> (structure)

Contains details about related findings.

Arn -> (string)

The Amazon Resource Name (ARN) of the related finding.

Type -> (string)

The type of finding.

IpAddress -> (string)

The IP address of the finding.

RelatedFindingGroupDetail -> (structure)

Contains details about related finding groups.

Id -> (string)

The unique identifier for the finding group.