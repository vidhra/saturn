# list-packaging-configurationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/list-packaging-configurations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/list-packaging-configurations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediapackage-vod](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/index.html#cli-aws-mediapackage-vod) ]

# list-packaging-configurations

## Description

Returns a collection of MediaPackage VOD PackagingConfiguration resources.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediapackage-vod-2018-11-07/ListPackagingConfigurations)

`list-packaging-configurations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `PackagingConfigurations`

## Synopsis

```
list-packaging-configurations
[--packaging-group-id <value>]
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

`--packaging-group-id` (string)
Returns MediaPackage VOD PackagingConfigurations associated with the specified PackagingGroup.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To list all packaging configurations**

The following `list-packaging-configurations` example lists all of the packaging configurations that are configured on the packaging group named `Packaging_group_1`.

```
aws mediapackage-vod list-packaging-configurations \
    --packaging-group-id Packaging_group_1
```

Output:

```
{
    "PackagingConfigurations":[
        {
            "Arn":"arn:aws:mediapackage-vod:us-west-2:111122223333:packaging-configurations/CMAF",
            "Id":"CMAF",
            "PackagingGroupId":"Packaging_group_1",
            "CmafPackage":[
                {
                    "SegmentDurationSeconds":"2"
                },
                {
                    "HlsManifests":{
                        "AdMarkers":"NONE",
                        "RepeatExtXKey":"False",
                        "ManifestName":"index",
                        "ProgramDateTimeIntervalSeconds":"0",
                        "IncludeIframeOnlyStream":"False"
                    }
                }
            ]
        },
        {
            "Arn":"arn:aws:mediapackage-vod:us-west-2:111122223333:packaging-configurations/DASH",
            "Id":"DASH",
            "PackagingGroupId":"Packaging_group_1",
            "DashPackage":[
                {
                    "SegmentDurationSeconds":"2"
                },
                {
                    "DashManifests":{
                        "ManifestName":"index",
                        "MinBufferTimeSeconds":"30",
                        "Profile":"NONE"
                    }
                }
            ]
        },
        {
            "Arn":"arn:aws:mediapackage-vod:us-west-2:111122223333:packaging-configurations/HLS",
            "Id":"HLS",
            "PackagingGroupId":"Packaging_group_1",
            "HlsPackage":[
                {
                    "SegmentDurationSeconds":"6",
                    "UseAudioRenditionGroup":"False"
                },
                {
                    "HlsManifests":{
                        "AdMarkers":"NONE",
                        "RepeatExtXKey":"False",
                        "ManifestName":"index",
                        "ProgramDateTimeIntervalSeconds":"0",
                        "IncludeIframeOnlyStream":"False"
                    }
                }
            ]
        },
        {
            "Arn":"arn:aws:mediapackage-vod:us-west-2:111122223333:packaging-configurations/New_config_0_copy",
            "Id":"New_config_0_copy",
            "PackagingGroupId":"Packaging_group_1",
            "HlsPackage":[
                {
                    "SegmentDurationSeconds":"6",
                    "UseAudioRenditionGroup":"False"
                },
                {
                    "Encryption":{
                        "EncryptionMethod":"AWS_128",
                        "SpekeKeyProvider":{
                           "RoleArn":"arn:aws:iam:111122223333::role/SPEKERole",
                            "Url":"https://lfgubdvs97.execute-api.us-west-2.amazonaws.com/EkeStage/copyProtection/",
                            "SystemIds":[
                                "81376844-f976-481e-a84e-cc25d39b0b33"
                            ]
                        }
                    }
                },
                {
                    "HlsManifests":{
                        "AdMarkers":"NONE",
                        "RepeatExtXKey":"False",
                        "ManifestName":"index",
                        "ProgramDateTimeIntervalSeconds":"0",
                        "IncludeIframeOnlyStream":"False"
                    }
                }
            ]
        }
    ]
}
```

For more information, see [Viewing Packaging Configuration Details](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-cfig-view.html) in the *AWS Elemental MediaPackage User Guide*.

## Output

NextToken -> (string)

A token that can be used to resume pagination from the end of the collection.

PackagingConfigurations -> (list)

A list of MediaPackage VOD PackagingConfiguration resources.

(structure)

A MediaPackage VOD PackagingConfiguration resource.

Arn -> (string)

The ARN of the PackagingConfiguration.

CmafPackage -> (structure)

A CMAF packaging configuration.

Encryption -> (structure)

A CMAF encryption configuration.

ConstantInitializationVector -> (string)

An optional 128-bit, 16-byte hex value represented by a 32-character string, used in conjunction with the key for encrypting blocks. If you donât specify a value, then MediaPackage creates the constant initialization vector (IV).

SpekeKeyProvider -> (structure)

A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

EncryptionContractConfiguration -> (structure)

Use encryptionContractConfiguration to configure one or more content encryption keys for your endpoints that use SPEKE 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use. Note the following considerations when using encryptionContractConfiguration: encryptionContractConfiguration can be used for DASH endpoints that use SPEKE 2.0. SPEKE 2.0 relies on the CPIX 2.3 specification. You must disable key rotation for this endpoint by setting keyRotationIntervalSeconds to 0.

PresetSpeke20Audio -> (string)

A collection of audio encryption presets.

PresetSpeke20Video -> (string)

A collection of video encryption presets.

RoleArn -> (string)

An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.

SystemIds -> (list)

The system IDs to include in key requests.

(string)

Url -> (string)

The URL of the external key provider service.

HlsManifests -> (list)

A list of HLS manifest configurations.

(structure)

An HTTP Live Streaming (HLS) manifest configuration.

AdMarkers -> (string)

This setting controls how ad markers are included in the packaged OriginEndpoint. âNONEâ will omit all SCTE-35 ad markers from the output. âPASSTHROUGHâ causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. âSCTE35_ENHANCEDâ generates ad markers and blackout tags based on SCTE-35 messages in the input source.

IncludeIframeOnlyStream -> (boolean)

When enabled, an I-Frame only stream will be included in the output.

ManifestName -> (string)

An optional string to include in the name of the manifest.

ProgramDateTimeIntervalSeconds -> (integer)

The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.

RepeatExtXKey -> (boolean)

When enabled, the EXT-X-KEY tag will be repeated in output manifests.

StreamSelection -> (structure)

A StreamSelection configuration.

MaxVideoBitsPerSecond -> (integer)

The maximum video bitrate (bps) to include in output.

MinVideoBitsPerSecond -> (integer)

The minimum video bitrate (bps) to include in output.

StreamOrder -> (string)

A directive that determines the order of streams in the output.

IncludeEncoderConfigurationInSegments -> (boolean)

When includeEncoderConfigurationInSegments is set to true, MediaPackage places your encoderâs Sequence Parameter Set (SPS), Picture Parameter Set (PPS), and Video Parameter Set (VPS) metadata in every video segment instead of in the init fragment. This lets you use different SPS/PPS/VPS settings for your assets during content playback.

SegmentDurationSeconds -> (integer)

Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.

CreatedAt -> (string)

The time the PackagingConfiguration was created.

DashPackage -> (structure)

A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.

DashManifests -> (list)

A list of DASH manifest configurations.

(structure)

A DASH manifest configuration.

ManifestLayout -> (string)

Determines the position of some tags in the Media Presentation Description (MPD). When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation. When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level.

ManifestName -> (string)

An optional string to include in the name of the manifest.

MinBufferTimeSeconds -> (integer)

Minimum duration (in seconds) that a player will buffer media before starting the presentation.

Profile -> (string)

The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to âHBBTV_1_5â, HbbTV 1.5 compliant output is enabled.

ScteMarkersSource -> (string)

The source of scte markers used. When set to SEGMENTS, the scte markers are sourced from the segments of the ingested content. When set to MANIFEST, the scte markers are sourced from the manifest of the ingested content.

StreamSelection -> (structure)

A StreamSelection configuration.

MaxVideoBitsPerSecond -> (integer)

The maximum video bitrate (bps) to include in output.

MinVideoBitsPerSecond -> (integer)

The minimum video bitrate (bps) to include in output.

StreamOrder -> (string)

A directive that determines the order of streams in the output.

Encryption -> (structure)

A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.

SpekeKeyProvider -> (structure)

A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

EncryptionContractConfiguration -> (structure)

Use encryptionContractConfiguration to configure one or more content encryption keys for your endpoints that use SPEKE 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use. Note the following considerations when using encryptionContractConfiguration: encryptionContractConfiguration can be used for DASH endpoints that use SPEKE 2.0. SPEKE 2.0 relies on the CPIX 2.3 specification. You must disable key rotation for this endpoint by setting keyRotationIntervalSeconds to 0.

PresetSpeke20Audio -> (string)

A collection of audio encryption presets.

PresetSpeke20Video -> (string)

A collection of video encryption presets.

RoleArn -> (string)

An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.

SystemIds -> (list)

The system IDs to include in key requests.

(string)

Url -> (string)

The URL of the external key provider service.

IncludeEncoderConfigurationInSegments -> (boolean)

When includeEncoderConfigurationInSegments is set to true, MediaPackage places your encoderâs Sequence Parameter Set (SPS), Picture Parameter Set (PPS), and Video Parameter Set (VPS) metadata in every video segment instead of in the init fragment. This lets you use different SPS/PPS/VPS settings for your assets during content playback.

IncludeIframeOnlyStream -> (boolean)

When enabled, an I-Frame only stream will be included in the output.

PeriodTriggers -> (list)

A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains âADSâ, new periods will be created where the Asset contains SCTE-35 ad markers.

(string)

SegmentDurationSeconds -> (integer)

Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.

SegmentTemplateFormat -> (string)

Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.

HlsPackage -> (structure)

An HTTP Live Streaming (HLS) packaging configuration.

Encryption -> (structure)

An HTTP Live Streaming (HLS) encryption configuration.

ConstantInitializationVector -> (string)

A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.

EncryptionMethod -> (string)

The encryption method to use.

SpekeKeyProvider -> (structure)

A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

EncryptionContractConfiguration -> (structure)

Use encryptionContractConfiguration to configure one or more content encryption keys for your endpoints that use SPEKE 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use. Note the following considerations when using encryptionContractConfiguration: encryptionContractConfiguration can be used for DASH endpoints that use SPEKE 2.0. SPEKE 2.0 relies on the CPIX 2.3 specification. You must disable key rotation for this endpoint by setting keyRotationIntervalSeconds to 0.

PresetSpeke20Audio -> (string)

A collection of audio encryption presets.

PresetSpeke20Video -> (string)

A collection of video encryption presets.

RoleArn -> (string)

An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.

SystemIds -> (list)

The system IDs to include in key requests.

(string)

Url -> (string)

The URL of the external key provider service.

HlsManifests -> (list)

A list of HLS manifest configurations.

(structure)

An HTTP Live Streaming (HLS) manifest configuration.

AdMarkers -> (string)

This setting controls how ad markers are included in the packaged OriginEndpoint. âNONEâ will omit all SCTE-35 ad markers from the output. âPASSTHROUGHâ causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. âSCTE35_ENHANCEDâ generates ad markers and blackout tags based on SCTE-35 messages in the input source.

IncludeIframeOnlyStream -> (boolean)

When enabled, an I-Frame only stream will be included in the output.

ManifestName -> (string)

An optional string to include in the name of the manifest.

ProgramDateTimeIntervalSeconds -> (integer)

The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.

RepeatExtXKey -> (boolean)

When enabled, the EXT-X-KEY tag will be repeated in output manifests.

StreamSelection -> (structure)

A StreamSelection configuration.

MaxVideoBitsPerSecond -> (integer)

The maximum video bitrate (bps) to include in output.

MinVideoBitsPerSecond -> (integer)

The minimum video bitrate (bps) to include in output.

StreamOrder -> (string)

A directive that determines the order of streams in the output.

IncludeDvbSubtitles -> (boolean)

When enabled, MediaPackage passes through digital video broadcasting (DVB) subtitles into the output.

SegmentDurationSeconds -> (integer)

Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.

UseAudioRenditionGroup -> (boolean)

When enabled, audio streams will be placed in rendition groups in the output.

Id -> (string)

The ID of the PackagingConfiguration.

MssPackage -> (structure)

A Microsoft Smooth Streaming (MSS) PackagingConfiguration.

Encryption -> (structure)

A Microsoft Smooth Streaming (MSS) encryption configuration.

SpekeKeyProvider -> (structure)

A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

EncryptionContractConfiguration -> (structure)

Use encryptionContractConfiguration to configure one or more content encryption keys for your endpoints that use SPEKE 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use. Note the following considerations when using encryptionContractConfiguration: encryptionContractConfiguration can be used for DASH endpoints that use SPEKE 2.0. SPEKE 2.0 relies on the CPIX 2.3 specification. You must disable key rotation for this endpoint by setting keyRotationIntervalSeconds to 0.

PresetSpeke20Audio -> (string)

A collection of audio encryption presets.

PresetSpeke20Video -> (string)

A collection of video encryption presets.

RoleArn -> (string)

An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.

SystemIds -> (list)

The system IDs to include in key requests.

(string)

Url -> (string)

The URL of the external key provider service.

MssManifests -> (list)

A list of MSS manifest configurations.

(structure)

A Microsoft Smooth Streaming (MSS) manifest configuration.

ManifestName -> (string)

An optional string to include in the name of the manifest.

StreamSelection -> (structure)

A StreamSelection configuration.

MaxVideoBitsPerSecond -> (integer)

The maximum video bitrate (bps) to include in output.

MinVideoBitsPerSecond -> (integer)

The minimum video bitrate (bps) to include in output.

StreamOrder -> (string)

A directive that determines the order of streams in the output.

SegmentDurationSeconds -> (integer)

The duration (in seconds) of each segment.

PackagingGroupId -> (string)

The ID of a PackagingGroup.

Tags -> (map)

A collection of tags associated with a resource

key -> (string)

value -> (string)