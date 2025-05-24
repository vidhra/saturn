# evaluate-sessionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/voice-id/evaluate-session.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/voice-id/evaluate-session.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [voice-id](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/voice-id/index.html#cli-aws-voice-id) ]

# evaluate-session

## Description

Evaluates a specified session based on audio data accumulated during a streaming Amazon Connect Voice ID call.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/voice-id-2021-09-27/EvaluateSession)

## Synopsis

```
evaluate-session
--domain-id <value>
--session-name-or-id <value>
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

`--domain-id` (string)

The identifier of the domain where the session started.

`--session-name-or-id` (string)

The session identifier, or name of the session, that you want to evaluate. In Voice ID integration, this is the Contact-Id.

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

AuthenticationResult -> (structure)

Details resulting from the authentication process, such as authentication decision and authentication score.

AudioAggregationEndedAt -> (timestamp)

A timestamp of when audio aggregation ended for this authentication result.

AudioAggregationStartedAt -> (timestamp)

A timestamp of when audio aggregation started for this authentication result.

AuthenticationResultId -> (string)

The unique identifier for this authentication result. Because there can be multiple authentications for a given session, this field helps to identify if the returned result is from a previous streaming activity or a new result. Note that in absence of any new streaming activity, `AcceptanceThreshold` changes, or `SpeakerId` changes, Voice ID always returns cached Authentication Result for this API.

Configuration -> (structure)

The `AuthenticationConfiguration` used to generate this authentication result.

AcceptanceThreshold -> (integer)

The minimum threshold needed to successfully authenticate a speaker.

CustomerSpeakerId -> (string)

The client-provided identifier for the speaker whose authentication result is produced. Only present if a `SpeakerId` is provided for the session.

Decision -> (string)

The authentication decision produced by Voice ID, processed against the current session state and streamed audio of the speaker.

GeneratedSpeakerId -> (string)

The service-generated identifier for the speaker whose authentication result is produced.

Score -> (integer)

The authentication score for the speaker whose authentication result is produced. This value is only present if the authentication decision is either `ACCEPT` or `REJECT` .

DomainId -> (string)

The identifier of the domain that contains the session.

FraudDetectionResult -> (structure)

Details resulting from the fraud detection process, such as fraud detection decision and risk score.

AudioAggregationEndedAt -> (timestamp)

A timestamp of when audio aggregation ended for this fraud detection result.

AudioAggregationStartedAt -> (timestamp)

A timestamp of when audio aggregation started for this fraud detection result.

Configuration -> (structure)

The `FraudDetectionConfiguration` used to generate this fraud detection result.

RiskThreshold -> (integer)

Threshold value for determining whether the speaker is a fraudster. If the detected risk score calculated by Voice ID is higher than the threshold, the speaker is considered a fraudster.

WatchlistId -> (string)

The identifier of the watchlist against which fraud detection is performed.

Decision -> (string)

The fraud detection decision produced by Voice ID, processed against the current session state and streamed audio of the speaker.

FraudDetectionResultId -> (string)

The unique identifier for this fraud detection result. Given there can be multiple fraud detections for a given session, this field helps in identifying if the returned result is from previous streaming activity or a new result. Note that in the absence of any new streaming activity or risk threshold changes, Voice ID always returns cached Fraud Detection result for this API.

Reasons -> (list)

The reason speaker was flagged by the fraud detection system. This is only be populated if fraud detection Decision is `HIGH_RISK` , and the following possible values: `KNOWN_FRAUDSTER` and `VOICE_SPOOFING` .

(string)

RiskDetails -> (structure)

Details about each risk analyzed for this speaker. Currently, this contains KnownFraudsterRisk and VoiceSpoofingRisk details.

KnownFraudsterRisk -> (structure)

The details resulting from âKnown Fraudster Riskâ analysis of the speaker.

GeneratedFraudsterId -> (string)

The identifier of the fraudster that is the closest match to the speaker. If there are no fraudsters registered in a given domain, or if there are no fraudsters with a non-zero RiskScore, this value is `null` .

RiskScore -> (integer)

The score indicating the likelihood the speaker is a known fraudster.

VoiceSpoofingRisk -> (structure)

The details resulting from âVoice Spoofing Riskâ analysis of the speaker.

RiskScore -> (integer)

The score indicating the likelihood of speakerâs voice being spoofed.

SessionId -> (string)

The service-generated identifier of the session.

SessionName -> (string)

The client-provided name of the session.

StreamingStatus -> (string)

The current status of audio streaming for this session. This field is useful to infer next steps when the Authentication or Fraud Detection results are empty or the decision is `NOT_ENOUGH_SPEECH` . In this situation, if the `StreamingStatus` is `ONGOING/PENDING_CONFIGURATION` , it can mean that the client should call the API again later, after Voice ID has enough audio to produce a result. If the decision remains `NOT_ENOUGH_SPEECH` even after `StreamingStatus` is `ENDED` , it means that the previously streamed session did not have enough speech to perform evaluation, and a new streaming session is needed to try again.