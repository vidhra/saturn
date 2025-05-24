# update-origin-endpointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/update-origin-endpoint.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/update-origin-endpoint.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediapackage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/index.html#cli-aws-mediapackage) ]

# update-origin-endpoint

## Description

Updates an existing OriginEndpoint.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediapackage-2017-10-12/UpdateOriginEndpoint)

## Synopsis

```
update-origin-endpoint
[--authorization <value>]
[--cmaf-package <value>]
[--dash-package <value>]
[--description <value>]
[--hls-package <value>]
--id <value>
[--manifest-name <value>]
[--mss-package <value>]
[--origination <value>]
[--startover-window-seconds <value>]
[--time-delay-seconds <value>]
[--whitelist <value>]
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

`--authorization` (structure)
CDN Authorization credentialsCdnIdentifierSecret -> (string)

The Amazon Resource Name (ARN) for the secret in Secrets Manager that your Content Distribution Network (CDN) uses for authorization to access your endpoint.

SecretsRoleArn -> (string)

The Amazon Resource Name (ARN) for the IAM role that allows MediaPackage to communicate with AWS Secrets Manager.

Shorthand Syntax:

```
CdnIdentifierSecret=string,SecretsRoleArn=string
```

JSON Syntax:

```
{
  "CdnIdentifierSecret": "string",
  "SecretsRoleArn": "string"
}
```

`--cmaf-package` (structure)
A Common Media Application Format (CMAF) packaging configuration.Encryption -> (structure)

A Common Media Application Format (CMAF) encryption configuration.

ConstantInitializationVector -> (string)

An optional 128-bit, 16-byte hex value represented by a 32-character string, used in conjunction with the key for encrypting blocks. If you donât specify a value, then MediaPackage creates the constant initialization vector (IV).

EncryptionMethod -> (string)

The encryption method to use.

KeyRotationIntervalSeconds -> (integer)

Time (in seconds) between each encryption key rotation.

SpekeKeyProvider -> (structure)

A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

CertificateArn -> (string)

An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.

EncryptionContractConfiguration -> (structure)

Use encryptionContractConfiguration to configure one or more content encryption keys for your endpoints that use SPEKE 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use. Note the following considerations when using encryptionContractConfiguration: encryptionContractConfiguration can be used for DASH or CMAF endpoints that use SPEKE 2.0. SPEKE 2.0 relies on the CPIX 2.3 specification. You must disable key rotation for this endpoint by setting keyRotationIntervalSeconds to 0.

PresetSpeke20Audio -> (string)

A collection of audio encryption presets.

PresetSpeke20Video -> (string)

A collection of video encryption presets.

ResourceId -> (string)

The resource ID to include in key requests.

RoleArn -> (string)

An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.

SystemIds -> (list)

The system IDs to include in key requests.

(string)

Url -> (string)

The URL of the external key provider service.

HlsManifests -> (list)

A list of HLS manifest configurations

(structure)

A HTTP Live Streaming (HLS) manifest configuration.

AdMarkers -> (string)

This setting controls how ad markers are included in the packaged OriginEndpoint. âNONEâ will omit all SCTE-35 ad markers from the output. âPASSTHROUGHâ causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. âSCTE35_ENHANCEDâ generates ad markers and blackout tags based on SCTE-35 messages in the input source. âDATERANGEâ inserts EXT-X-DATERANGE tags to signal ad and program transition events in HLS and CMAF manifests. For this option, you must set a programDateTimeIntervalSeconds value that is greater than 0.

AdTriggers -> (list)

A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.

(string)

AdsOnDeliveryRestrictions -> (string)

This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing âNONEâ means no SCTE-35 messages become ads. Choosing âRESTRICTEDâ means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing âUNRESTRICTEDâ means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing âBOTHâ means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.

Id -> (string)

The ID of the manifest. The ID must be unique within the OriginEndpoint and it cannot be changed after it is created.

IncludeIframeOnlyStream -> (boolean)

When enabled, an I-Frame only stream will be included in the output.

ManifestName -> (string)

An optional short string appended to the end of the OriginEndpoint URL. If not specified, defaults to the manifestName for the OriginEndpoint.

PlaylistType -> (string)

The HTTP Live Streaming (HLS) playlist type. When either âEVENTâ or âVODâ is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.

PlaylistWindowSeconds -> (integer)

Time window (in seconds) contained in each parent manifest.

ProgramDateTimeIntervalSeconds -> (integer)

The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.

SegmentDurationSeconds -> (integer)

Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.

SegmentPrefix -> (string)

An optional custom string that is prepended to the name of each segment. If not specified, it defaults to the ChannelId.

StreamSelection -> (structure)

A StreamSelection configuration.

MaxVideoBitsPerSecond -> (integer)

The maximum video bitrate (bps) to include in output.

MinVideoBitsPerSecond -> (integer)

The minimum video bitrate (bps) to include in output.

StreamOrder -> (string)

A directive that determines the order of streams in the output.

JSON Syntax:

```
{
  "Encryption": {
    "ConstantInitializationVector": "string",
    "EncryptionMethod": "SAMPLE_AES"|"AES_CTR",
    "KeyRotationIntervalSeconds": integer,
    "SpekeKeyProvider": {
      "CertificateArn": "string",
      "EncryptionContractConfiguration": {
        "PresetSpeke20Audio": "PRESET-AUDIO-1"|"PRESET-AUDIO-2"|"PRESET-AUDIO-3"|"SHARED"|"UNENCRYPTED",
        "PresetSpeke20Video": "PRESET-VIDEO-1"|"PRESET-VIDEO-2"|"PRESET-VIDEO-3"|"PRESET-VIDEO-4"|"PRESET-VIDEO-5"|"PRESET-VIDEO-6"|"PRESET-VIDEO-7"|"PRESET-VIDEO-8"|"SHARED"|"UNENCRYPTED"
      },
      "ResourceId": "string",
      "RoleArn": "string",
      "SystemIds": ["string", ...],
      "Url": "string"
    }
  },
  "HlsManifests": [
    {
      "AdMarkers": "NONE"|"SCTE35_ENHANCED"|"PASSTHROUGH"|"DATERANGE",
      "AdTriggers": ["SPLICE_INSERT"|"BREAK"|"PROVIDER_ADVERTISEMENT"|"DISTRIBUTOR_ADVERTISEMENT"|"PROVIDER_PLACEMENT_OPPORTUNITY"|"DISTRIBUTOR_PLACEMENT_OPPORTUNITY"|"PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY"|"DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY", ...],
      "AdsOnDeliveryRestrictions": "NONE"|"RESTRICTED"|"UNRESTRICTED"|"BOTH",
      "Id": "string",
      "IncludeIframeOnlyStream": true|false,
      "ManifestName": "string",
      "PlaylistType": "NONE"|"EVENT"|"VOD",
      "PlaylistWindowSeconds": integer,
      "ProgramDateTimeIntervalSeconds": integer
    }
    ...
  ],
  "SegmentDurationSeconds": integer,
  "SegmentPrefix": "string",
  "StreamSelection": {
    "MaxVideoBitsPerSecond": integer,
    "MinVideoBitsPerSecond": integer,
    "StreamOrder": "ORIGINAL"|"VIDEO_BITRATE_ASCENDING"|"VIDEO_BITRATE_DESCENDING"
  }
}
```

`--dash-package` (structure)
A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.AdTriggers -> (list)

A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.

(string)

AdsOnDeliveryRestrictions -> (string)

This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing âNONEâ means no SCTE-35 messages become ads. Choosing âRESTRICTEDâ means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing âUNRESTRICTEDâ means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing âBOTHâ means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.

Encryption -> (structure)

A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.

KeyRotationIntervalSeconds -> (integer)

Time (in seconds) between each encryption key rotation.

SpekeKeyProvider -> (structure)

A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

CertificateArn -> (string)

An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.

EncryptionContractConfiguration -> (structure)

Use encryptionContractConfiguration to configure one or more content encryption keys for your endpoints that use SPEKE 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use. Note the following considerations when using encryptionContractConfiguration: encryptionContractConfiguration can be used for DASH or CMAF endpoints that use SPEKE 2.0. SPEKE 2.0 relies on the CPIX 2.3 specification. You must disable key rotation for this endpoint by setting keyRotationIntervalSeconds to 0.

PresetSpeke20Audio -> (string)

A collection of audio encryption presets.

PresetSpeke20Video -> (string)

A collection of video encryption presets.

ResourceId -> (string)

The resource ID to include in key requests.

RoleArn -> (string)

An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.

SystemIds -> (list)

The system IDs to include in key requests.

(string)

Url -> (string)

The URL of the external key provider service.

IncludeIframeOnlyStream -> (boolean)

When enabled, an I-Frame only stream will be included in the output.

ManifestLayout -> (string)

Determines the position of some tags in the Media Presentation Description (MPD). When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation. When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level. When set to DRM_TOP_LEVEL_COMPACT, content protection elements are placed the MPD level and referenced at the AdaptationSet level.

ManifestWindowSeconds -> (integer)

Time window (in seconds) contained in each manifest.

MinBufferTimeSeconds -> (integer)

Minimum duration (in seconds) that a player will buffer media before starting the presentation.

MinUpdatePeriodSeconds -> (integer)

Minimum duration (in seconds) between potential changes to the Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD).

PeriodTriggers -> (list)

A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains âADSâ, new periods will be created where the Channel source contains SCTE-35 ad markers.

(string)

Profile -> (string)

The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to âHBBTV_1_5â, HbbTV 1.5 compliant output is enabled. When set to âDVB-DASH_2014â, DVB-DASH 2014 compliant output is enabled.

SegmentDurationSeconds -> (integer)

Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.

SegmentTemplateFormat -> (string)

Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.

StreamSelection -> (structure)

A StreamSelection configuration.

MaxVideoBitsPerSecond -> (integer)

The maximum video bitrate (bps) to include in output.

MinVideoBitsPerSecond -> (integer)

The minimum video bitrate (bps) to include in output.

StreamOrder -> (string)

A directive that determines the order of streams in the output.

SuggestedPresentationDelaySeconds -> (integer)

Duration (in seconds) to delay live content before presentation.

UtcTiming -> (string)

Determines the type of UTCTiming included in the Media Presentation Description (MPD)

UtcTimingUri -> (string)

Specifies the value attribute of the UTCTiming field when utcTiming is set to HTTP-ISO, HTTP-HEAD or HTTP-XSDATE

JSON Syntax:

```
{
  "AdTriggers": ["SPLICE_INSERT"|"BREAK"|"PROVIDER_ADVERTISEMENT"|"DISTRIBUTOR_ADVERTISEMENT"|"PROVIDER_PLACEMENT_OPPORTUNITY"|"DISTRIBUTOR_PLACEMENT_OPPORTUNITY"|"PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY"|"DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY", ...],
  "AdsOnDeliveryRestrictions": "NONE"|"RESTRICTED"|"UNRESTRICTED"|"BOTH",
  "Encryption": {
    "KeyRotationIntervalSeconds": integer,
    "SpekeKeyProvider": {
      "CertificateArn": "string",
      "EncryptionContractConfiguration": {
        "PresetSpeke20Audio": "PRESET-AUDIO-1"|"PRESET-AUDIO-2"|"PRESET-AUDIO-3"|"SHARED"|"UNENCRYPTED",
        "PresetSpeke20Video": "PRESET-VIDEO-1"|"PRESET-VIDEO-2"|"PRESET-VIDEO-3"|"PRESET-VIDEO-4"|"PRESET-VIDEO-5"|"PRESET-VIDEO-6"|"PRESET-VIDEO-7"|"PRESET-VIDEO-8"|"SHARED"|"UNENCRYPTED"
      },
      "ResourceId": "string",
      "RoleArn": "string",
      "SystemIds": ["string", ...],
      "Url": "string"
    }
  },
  "IncludeIframeOnlyStream": true|false,
  "ManifestLayout": "FULL"|"COMPACT"|"DRM_TOP_LEVEL_COMPACT",
  "ManifestWindowSeconds": integer,
  "MinBufferTimeSeconds": integer,
  "MinUpdatePeriodSeconds": integer,
  "PeriodTriggers": ["ADS", ...],
  "Profile": "NONE"|"HBBTV_1_5"|"HYBRIDCAST"|"DVB_DASH_2014",
  "SegmentDurationSeconds": integer,
  "SegmentTemplateFormat": "NUMBER_WITH_TIMELINE"|"TIME_WITH_TIMELINE"|"NUMBER_WITH_DURATION",
  "StreamSelection": {
    "MaxVideoBitsPerSecond": integer,
    "MinVideoBitsPerSecond": integer,
    "StreamOrder": "ORIGINAL"|"VIDEO_BITRATE_ASCENDING"|"VIDEO_BITRATE_DESCENDING"
  },
  "SuggestedPresentationDelaySeconds": integer,
  "UtcTiming": "NONE"|"HTTP-HEAD"|"HTTP-ISO"|"HTTP-XSDATE",
  "UtcTimingUri": "string"
}
```

`--description` (string)
A short text description of the OriginEndpoint.

`--hls-package` (structure)
An HTTP Live Streaming (HLS) packaging configuration.AdMarkers -> (string)

This setting controls how ad markers are included in the packaged OriginEndpoint. âNONEâ will omit all SCTE-35 ad markers from the output. âPASSTHROUGHâ causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. âSCTE35_ENHANCEDâ generates ad markers and blackout tags based on SCTE-35 messages in the input source. âDATERANGEâ inserts EXT-X-DATERANGE tags to signal ad and program transition events in HLS and CMAF manifests. For this option, you must set a programDateTimeIntervalSeconds value that is greater than 0.

AdTriggers -> (list)

A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.

(string)

AdsOnDeliveryRestrictions -> (string)

This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing âNONEâ means no SCTE-35 messages become ads. Choosing âRESTRICTEDâ means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing âUNRESTRICTEDâ means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing âBOTHâ means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.

Encryption -> (structure)

An HTTP Live Streaming (HLS) encryption configuration.

ConstantInitializationVector -> (string)

A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.

EncryptionMethod -> (string)

The encryption method to use.

KeyRotationIntervalSeconds -> (integer)

Interval (in seconds) between each encryption key rotation.

RepeatExtXKey -> (boolean)

When enabled, the EXT-X-KEY tag will be repeated in output manifests.

SpekeKeyProvider -> (structure)

A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

CertificateArn -> (string)

An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.

EncryptionContractConfiguration -> (structure)

Use encryptionContractConfiguration to configure one or more content encryption keys for your endpoints that use SPEKE 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use. Note the following considerations when using encryptionContractConfiguration: encryptionContractConfiguration can be used for DASH or CMAF endpoints that use SPEKE 2.0. SPEKE 2.0 relies on the CPIX 2.3 specification. You must disable key rotation for this endpoint by setting keyRotationIntervalSeconds to 0.

PresetSpeke20Audio -> (string)

A collection of audio encryption presets.

PresetSpeke20Video -> (string)

A collection of video encryption presets.

ResourceId -> (string)

The resource ID to include in key requests.

RoleArn -> (string)

An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.

SystemIds -> (list)

The system IDs to include in key requests.

(string)

Url -> (string)

The URL of the external key provider service.

IncludeDvbSubtitles -> (boolean)

When enabled, MediaPackage passes through digital video broadcasting (DVB) subtitles into the output.

IncludeIframeOnlyStream -> (boolean)

When enabled, an I-Frame only stream will be included in the output.

PlaylistType -> (string)

The HTTP Live Streaming (HLS) playlist type. When either âEVENTâ or âVODâ is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.

PlaylistWindowSeconds -> (integer)

Time window (in seconds) contained in each parent manifest.

ProgramDateTimeIntervalSeconds -> (integer)

The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.

SegmentDurationSeconds -> (integer)

Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.

StreamSelection -> (structure)

A StreamSelection configuration.

MaxVideoBitsPerSecond -> (integer)

The maximum video bitrate (bps) to include in output.

MinVideoBitsPerSecond -> (integer)

The minimum video bitrate (bps) to include in output.

StreamOrder -> (string)

A directive that determines the order of streams in the output.

UseAudioRenditionGroup -> (boolean)

When enabled, audio streams will be placed in rendition groups in the output.

JSON Syntax:

```
{
  "AdMarkers": "NONE"|"SCTE35_ENHANCED"|"PASSTHROUGH"|"DATERANGE",
  "AdTriggers": ["SPLICE_INSERT"|"BREAK"|"PROVIDER_ADVERTISEMENT"|"DISTRIBUTOR_ADVERTISEMENT"|"PROVIDER_PLACEMENT_OPPORTUNITY"|"DISTRIBUTOR_PLACEMENT_OPPORTUNITY"|"PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY"|"DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY", ...],
  "AdsOnDeliveryRestrictions": "NONE"|"RESTRICTED"|"UNRESTRICTED"|"BOTH",
  "Encryption": {
    "ConstantInitializationVector": "string",
    "EncryptionMethod": "AES_128"|"SAMPLE_AES",
    "KeyRotationIntervalSeconds": integer,
    "RepeatExtXKey": true|false,
    "SpekeKeyProvider": {
      "CertificateArn": "string",
      "EncryptionContractConfiguration": {
        "PresetSpeke20Audio": "PRESET-AUDIO-1"|"PRESET-AUDIO-2"|"PRESET-AUDIO-3"|"SHARED"|"UNENCRYPTED",
        "PresetSpeke20Video": "PRESET-VIDEO-1"|"PRESET-VIDEO-2"|"PRESET-VIDEO-3"|"PRESET-VIDEO-4"|"PRESET-VIDEO-5"|"PRESET-VIDEO-6"|"PRESET-VIDEO-7"|"PRESET-VIDEO-8"|"SHARED"|"UNENCRYPTED"
      },
      "ResourceId": "string",
      "RoleArn": "string",
      "SystemIds": ["string", ...],
      "Url": "string"
    }
  },
  "IncludeDvbSubtitles": true|false,
  "IncludeIframeOnlyStream": true|false,
  "PlaylistType": "NONE"|"EVENT"|"VOD",
  "PlaylistWindowSeconds": integer,
  "ProgramDateTimeIntervalSeconds": integer,
  "SegmentDurationSeconds": integer,
  "StreamSelection": {
    "MaxVideoBitsPerSecond": integer,
    "MinVideoBitsPerSecond": integer,
    "StreamOrder": "ORIGINAL"|"VIDEO_BITRATE_ASCENDING"|"VIDEO_BITRATE_DESCENDING"
  },
  "UseAudioRenditionGroup": true|false
}
```

`--id` (string)
The ID of the OriginEndpoint to update.

`--manifest-name` (string)
A short string that will be appended to the end of the Endpoint URL.

`--mss-package` (structure)
A Microsoft Smooth Streaming (MSS) packaging configuration.Encryption -> (structure)

A Microsoft Smooth Streaming (MSS) encryption configuration.

SpekeKeyProvider -> (structure)

A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

CertificateArn -> (string)

An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.

EncryptionContractConfiguration -> (structure)

Use encryptionContractConfiguration to configure one or more content encryption keys for your endpoints that use SPEKE 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use. Note the following considerations when using encryptionContractConfiguration: encryptionContractConfiguration can be used for DASH or CMAF endpoints that use SPEKE 2.0. SPEKE 2.0 relies on the CPIX 2.3 specification. You must disable key rotation for this endpoint by setting keyRotationIntervalSeconds to 0.

PresetSpeke20Audio -> (string)

A collection of audio encryption presets.

PresetSpeke20Video -> (string)

A collection of video encryption presets.

ResourceId -> (string)

The resource ID to include in key requests.

RoleArn -> (string)

An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.

SystemIds -> (list)

The system IDs to include in key requests.

(string)

Url -> (string)

The URL of the external key provider service.

ManifestWindowSeconds -> (integer)

The time window (in seconds) contained in each manifest.

SegmentDurationSeconds -> (integer)

The duration (in seconds) of each segment.

StreamSelection -> (structure)

A StreamSelection configuration.

MaxVideoBitsPerSecond -> (integer)

The maximum video bitrate (bps) to include in output.

MinVideoBitsPerSecond -> (integer)

The minimum video bitrate (bps) to include in output.

StreamOrder -> (string)

A directive that determines the order of streams in the output.

JSON Syntax:

```
{
  "Encryption": {
    "SpekeKeyProvider": {
      "CertificateArn": "string",
      "EncryptionContractConfiguration": {
        "PresetSpeke20Audio": "PRESET-AUDIO-1"|"PRESET-AUDIO-2"|"PRESET-AUDIO-3"|"SHARED"|"UNENCRYPTED",
        "PresetSpeke20Video": "PRESET-VIDEO-1"|"PRESET-VIDEO-2"|"PRESET-VIDEO-3"|"PRESET-VIDEO-4"|"PRESET-VIDEO-5"|"PRESET-VIDEO-6"|"PRESET-VIDEO-7"|"PRESET-VIDEO-8"|"SHARED"|"UNENCRYPTED"
      },
      "ResourceId": "string",
      "RoleArn": "string",
      "SystemIds": ["string", ...],
      "Url": "string"
    }
  },
  "ManifestWindowSeconds": integer,
  "SegmentDurationSeconds": integer,
  "StreamSelection": {
    "MaxVideoBitsPerSecond": integer,
    "MinVideoBitsPerSecond": integer,
    "StreamOrder": "ORIGINAL"|"VIDEO_BITRATE_ASCENDING"|"VIDEO_BITRATE_DESCENDING"
  }
}
```

`--origination` (string)
Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination

Possible values:

- `ALLOW`
- `DENY`

`--startover-window-seconds` (integer)
Maximum duration (in seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.

`--time-delay-seconds` (integer)
Amount of delay (in seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.

`--whitelist` (list)
A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.(string)

Syntax:

```
"string" "string" ...
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To update an origin endpoint**

The following `update-origin-endpoint` command updates the origin endpoint named `cmaf_sports`. It changes the time delay to `0` seconds.

```
aws mediapackage update-origin-endpoint \
    --id cmaf_sports \
    --time-delay-seconds 0
```

Output:

```
{
    "Arn": "arn:aws:mediapackage:us-west-2:111222333:origin_endpoints/1dc6718be36f4f34bb9cd86bc50925e6",
    "ChannelId": "sportschannel",
    "CmafPackage": {
        "HlsManifests": [
            {
                "AdMarkers": "NONE",
                "Id": "cmaf_sports_endpoint",
                "IncludeIframeOnlyStream": false,
                "PlaylistType": "EVENT",
                "PlaylistWindowSeconds": 60,
                "ProgramDateTimeIntervalSeconds": 0,
                "Url": "https://c4af3793bf76b33c.mediapackage.us-west-2.amazonaws.com/out/v1/1dc6718be36f4f34bb9cd86bc50925e6/cmaf_sports_endpoint/index.m3u8"
            }
        ],
        "SegmentDurationSeconds": 2,
        "SegmentPrefix": "sportschannel"
    },
    "Id": "cmaf_sports",
    "ManifestName": "index",
    "StartoverWindowSeconds": 0,
    "Tags": {
        "region": "west",
        "media": "sports"
    },
    "TimeDelaySeconds": 0,
    "Url": "",
    "Whitelist": []
}
```

For more information, see [Editing an Endpoint](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-edit.html) in the *AWS Elemental MediaPackage User Guide*.

## Output

Arn -> (string)

The Amazon Resource Name (ARN) assigned to the OriginEndpoint.

Authorization -> (structure)

CDN Authorization credentials

CdnIdentifierSecret -> (string)

The Amazon Resource Name (ARN) for the secret in Secrets Manager that your Content Distribution Network (CDN) uses for authorization to access your endpoint.

SecretsRoleArn -> (string)

The Amazon Resource Name (ARN) for the IAM role that allows MediaPackage to communicate with AWS Secrets Manager.

ChannelId -> (string)

The ID of the Channel the OriginEndpoint is associated with.

CmafPackage -> (structure)

A Common Media Application Format (CMAF) packaging configuration.

Encryption -> (structure)

A Common Media Application Format (CMAF) encryption configuration.

ConstantInitializationVector -> (string)

An optional 128-bit, 16-byte hex value represented by a 32-character string, used in conjunction with the key for encrypting blocks. If you donât specify a value, then MediaPackage creates the constant initialization vector (IV).

EncryptionMethod -> (string)

The encryption method to use.

KeyRotationIntervalSeconds -> (integer)

Time (in seconds) between each encryption key rotation.

SpekeKeyProvider -> (structure)

A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

CertificateArn -> (string)

An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.

EncryptionContractConfiguration -> (structure)

Use encryptionContractConfiguration to configure one or more content encryption keys for your endpoints that use SPEKE 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use. Note the following considerations when using encryptionContractConfiguration: encryptionContractConfiguration can be used for DASH or CMAF endpoints that use SPEKE 2.0. SPEKE 2.0 relies on the CPIX 2.3 specification. You must disable key rotation for this endpoint by setting keyRotationIntervalSeconds to 0.

PresetSpeke20Audio -> (string)

A collection of audio encryption presets.

PresetSpeke20Video -> (string)

A collection of video encryption presets.

ResourceId -> (string)

The resource ID to include in key requests.

RoleArn -> (string)

An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.

SystemIds -> (list)

The system IDs to include in key requests.

(string)

Url -> (string)

The URL of the external key provider service.

HlsManifests -> (list)

A list of HLS manifest configurations

(structure)

A HTTP Live Streaming (HLS) manifest configuration.

AdMarkers -> (string)

This setting controls how ad markers are included in the packaged OriginEndpoint. âNONEâ will omit all SCTE-35 ad markers from the output. âPASSTHROUGHâ causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. âSCTE35_ENHANCEDâ generates ad markers and blackout tags based on SCTE-35 messages in the input source. âDATERANGEâ inserts EXT-X-DATERANGE tags to signal ad and program transition events in HLS and CMAF manifests. For this option, you must set a programDateTimeIntervalSeconds value that is greater than 0.

Id -> (string)

The ID of the manifest. The ID must be unique within the OriginEndpoint and it cannot be changed after it is created.

IncludeIframeOnlyStream -> (boolean)

When enabled, an I-Frame only stream will be included in the output.

ManifestName -> (string)

An optional short string appended to the end of the OriginEndpoint URL. If not specified, defaults to the manifestName for the OriginEndpoint.

PlaylistType -> (string)

The HTTP Live Streaming (HLS) playlist type. When either âEVENTâ or âVODâ is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.

PlaylistWindowSeconds -> (integer)

Time window (in seconds) contained in each parent manifest.

ProgramDateTimeIntervalSeconds -> (integer)

The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.

Url -> (string)

The URL of the packaged OriginEndpoint for consumption.

AdTriggers -> (list)

A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.

(string)

AdsOnDeliveryRestrictions -> (string)

This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing âNONEâ means no SCTE-35 messages become ads. Choosing âRESTRICTEDâ means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing âUNRESTRICTEDâ means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing âBOTHâ means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.

SegmentDurationSeconds -> (integer)

Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.

SegmentPrefix -> (string)

An optional custom string that is prepended to the name of each segment. If not specified, it defaults to the ChannelId.

StreamSelection -> (structure)

A StreamSelection configuration.

MaxVideoBitsPerSecond -> (integer)

The maximum video bitrate (bps) to include in output.

MinVideoBitsPerSecond -> (integer)

The minimum video bitrate (bps) to include in output.

StreamOrder -> (string)

A directive that determines the order of streams in the output.

CreatedAt -> (string)

The date and time the OriginEndpoint was created.

DashPackage -> (structure)

A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.

AdTriggers -> (list)

A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.

(string)

AdsOnDeliveryRestrictions -> (string)

This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing âNONEâ means no SCTE-35 messages become ads. Choosing âRESTRICTEDâ means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing âUNRESTRICTEDâ means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing âBOTHâ means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.

Encryption -> (structure)

A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.

KeyRotationIntervalSeconds -> (integer)

Time (in seconds) between each encryption key rotation.

SpekeKeyProvider -> (structure)

A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

CertificateArn -> (string)

An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.

EncryptionContractConfiguration -> (structure)

Use encryptionContractConfiguration to configure one or more content encryption keys for your endpoints that use SPEKE 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use. Note the following considerations when using encryptionContractConfiguration: encryptionContractConfiguration can be used for DASH or CMAF endpoints that use SPEKE 2.0. SPEKE 2.0 relies on the CPIX 2.3 specification. You must disable key rotation for this endpoint by setting keyRotationIntervalSeconds to 0.

PresetSpeke20Audio -> (string)

A collection of audio encryption presets.

PresetSpeke20Video -> (string)

A collection of video encryption presets.

ResourceId -> (string)

The resource ID to include in key requests.

RoleArn -> (string)

An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.

SystemIds -> (list)

The system IDs to include in key requests.

(string)

Url -> (string)

The URL of the external key provider service.

IncludeIframeOnlyStream -> (boolean)

When enabled, an I-Frame only stream will be included in the output.

ManifestLayout -> (string)

Determines the position of some tags in the Media Presentation Description (MPD). When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation. When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level. When set to DRM_TOP_LEVEL_COMPACT, content protection elements are placed the MPD level and referenced at the AdaptationSet level.

ManifestWindowSeconds -> (integer)

Time window (in seconds) contained in each manifest.

MinBufferTimeSeconds -> (integer)

Minimum duration (in seconds) that a player will buffer media before starting the presentation.

MinUpdatePeriodSeconds -> (integer)

Minimum duration (in seconds) between potential changes to the Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD).

PeriodTriggers -> (list)

A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains âADSâ, new periods will be created where the Channel source contains SCTE-35 ad markers.

(string)

Profile -> (string)

The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to âHBBTV_1_5â, HbbTV 1.5 compliant output is enabled. When set to âDVB-DASH_2014â, DVB-DASH 2014 compliant output is enabled.

SegmentDurationSeconds -> (integer)

Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.

SegmentTemplateFormat -> (string)

Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.

StreamSelection -> (structure)

A StreamSelection configuration.

MaxVideoBitsPerSecond -> (integer)

The maximum video bitrate (bps) to include in output.

MinVideoBitsPerSecond -> (integer)

The minimum video bitrate (bps) to include in output.

StreamOrder -> (string)

A directive that determines the order of streams in the output.

SuggestedPresentationDelaySeconds -> (integer)

Duration (in seconds) to delay live content before presentation.

UtcTiming -> (string)

Determines the type of UTCTiming included in the Media Presentation Description (MPD)

UtcTimingUri -> (string)

Specifies the value attribute of the UTCTiming field when utcTiming is set to HTTP-ISO, HTTP-HEAD or HTTP-XSDATE

Description -> (string)

A short text description of the OriginEndpoint.

HlsPackage -> (structure)

An HTTP Live Streaming (HLS) packaging configuration.

AdMarkers -> (string)

This setting controls how ad markers are included in the packaged OriginEndpoint. âNONEâ will omit all SCTE-35 ad markers from the output. âPASSTHROUGHâ causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. âSCTE35_ENHANCEDâ generates ad markers and blackout tags based on SCTE-35 messages in the input source. âDATERANGEâ inserts EXT-X-DATERANGE tags to signal ad and program transition events in HLS and CMAF manifests. For this option, you must set a programDateTimeIntervalSeconds value that is greater than 0.

AdTriggers -> (list)

A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.

(string)

AdsOnDeliveryRestrictions -> (string)

This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing âNONEâ means no SCTE-35 messages become ads. Choosing âRESTRICTEDâ means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing âUNRESTRICTEDâ means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing âBOTHâ means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.

Encryption -> (structure)

An HTTP Live Streaming (HLS) encryption configuration.

ConstantInitializationVector -> (string)

A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.

EncryptionMethod -> (string)

The encryption method to use.

KeyRotationIntervalSeconds -> (integer)

Interval (in seconds) between each encryption key rotation.

RepeatExtXKey -> (boolean)

When enabled, the EXT-X-KEY tag will be repeated in output manifests.

SpekeKeyProvider -> (structure)

A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

CertificateArn -> (string)

An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.

EncryptionContractConfiguration -> (structure)

Use encryptionContractConfiguration to configure one or more content encryption keys for your endpoints that use SPEKE 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use. Note the following considerations when using encryptionContractConfiguration: encryptionContractConfiguration can be used for DASH or CMAF endpoints that use SPEKE 2.0. SPEKE 2.0 relies on the CPIX 2.3 specification. You must disable key rotation for this endpoint by setting keyRotationIntervalSeconds to 0.

PresetSpeke20Audio -> (string)

A collection of audio encryption presets.

PresetSpeke20Video -> (string)

A collection of video encryption presets.

ResourceId -> (string)

The resource ID to include in key requests.

RoleArn -> (string)

An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.

SystemIds -> (list)

The system IDs to include in key requests.

(string)

Url -> (string)

The URL of the external key provider service.

IncludeDvbSubtitles -> (boolean)

When enabled, MediaPackage passes through digital video broadcasting (DVB) subtitles into the output.

IncludeIframeOnlyStream -> (boolean)

When enabled, an I-Frame only stream will be included in the output.

PlaylistType -> (string)

The HTTP Live Streaming (HLS) playlist type. When either âEVENTâ or âVODâ is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.

PlaylistWindowSeconds -> (integer)

Time window (in seconds) contained in each parent manifest.

ProgramDateTimeIntervalSeconds -> (integer)

The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.

SegmentDurationSeconds -> (integer)

Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.

StreamSelection -> (structure)

A StreamSelection configuration.

MaxVideoBitsPerSecond -> (integer)

The maximum video bitrate (bps) to include in output.

MinVideoBitsPerSecond -> (integer)

The minimum video bitrate (bps) to include in output.

StreamOrder -> (string)

A directive that determines the order of streams in the output.

UseAudioRenditionGroup -> (boolean)

When enabled, audio streams will be placed in rendition groups in the output.

Id -> (string)

The ID of the OriginEndpoint.

ManifestName -> (string)

A short string appended to the end of the OriginEndpoint URL.

MssPackage -> (structure)

A Microsoft Smooth Streaming (MSS) packaging configuration.

Encryption -> (structure)

A Microsoft Smooth Streaming (MSS) encryption configuration.

SpekeKeyProvider -> (structure)

A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

CertificateArn -> (string)

An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.

EncryptionContractConfiguration -> (structure)

Use encryptionContractConfiguration to configure one or more content encryption keys for your endpoints that use SPEKE 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use. Note the following considerations when using encryptionContractConfiguration: encryptionContractConfiguration can be used for DASH or CMAF endpoints that use SPEKE 2.0. SPEKE 2.0 relies on the CPIX 2.3 specification. You must disable key rotation for this endpoint by setting keyRotationIntervalSeconds to 0.

PresetSpeke20Audio -> (string)

A collection of audio encryption presets.

PresetSpeke20Video -> (string)

A collection of video encryption presets.

ResourceId -> (string)

The resource ID to include in key requests.

RoleArn -> (string)

An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.

SystemIds -> (list)

The system IDs to include in key requests.

(string)

Url -> (string)

The URL of the external key provider service.

ManifestWindowSeconds -> (integer)

The time window (in seconds) contained in each manifest.

SegmentDurationSeconds -> (integer)

The duration (in seconds) of each segment.

StreamSelection -> (structure)

A StreamSelection configuration.

MaxVideoBitsPerSecond -> (integer)

The maximum video bitrate (bps) to include in output.

MinVideoBitsPerSecond -> (integer)

The minimum video bitrate (bps) to include in output.

StreamOrder -> (string)

A directive that determines the order of streams in the output.

Origination -> (string)

Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination

StartoverWindowSeconds -> (integer)

Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.

Tags -> (map)

A collection of tags associated with a resource

key -> (string)

value -> (string)

TimeDelaySeconds -> (integer)

Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.

Url -> (string)

The URL of the packaged OriginEndpoint for consumption.

Whitelist -> (list)

A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.

(string)