# create-source-locationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/create-source-location.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/create-source-location.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediatailor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/index.html#cli-aws-mediatailor) ]

# create-source-location

## Description

Creates a source location. A source location is a container for sources. For more information about source locations, see [Working with source locations](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html) in the *MediaTailor User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/CreateSourceLocation)

## Synopsis

```
create-source-location
[--access-configuration <value>]
[--default-segment-delivery-configuration <value>]
--http-configuration <value>
[--segment-delivery-configurations <value>]
--source-location-name <value>
[--tags <value>]
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

`--access-configuration` (structure)

Access configuration parameters. Configures the type of authentication used to access content from your source location.

AccessType -> (string)

The type of authentication used to access content from `HttpConfiguration::BaseUrl` on your source location.

`S3_SIGV4` - AWS Signature Version 4 authentication for Amazon S3 hosted virtual-style access. If your source location base URL is an Amazon S3 bucket, MediaTailor can use AWS Signature Version 4 (SigV4) authentication to access the bucket where your source content is stored. Your MediaTailor source location baseURL must follow the S3 virtual hosted-style request URL format. For example, [https://bucket-name.s3.Region.amazonaws.com/key-name](https://bucket-name.s3.Region.amazonaws.com/key-name).

Before you can use `S3_SIGV4` , you must meet these requirements:

- You must allow MediaTailor to access your S3 bucket by granting mediatailor.amazonaws.com principal access in IAM. For information about configuring access in IAM, see Access management in the IAM User Guide.
- The mediatailor.amazonaws.com service principal must have permissions to read all top level manifests referenced by the VodSource packaging configurations.
- The caller of the API must have s3:GetObject IAM permissions to read all top level manifests referenced by your MediaTailor VodSource packaging configurations.

`AUTODETECT_SIGV4` - AWS Signature Version 4 authentication for a set of supported services: MediaPackage Version 2 and Amazon S3 hosted virtual-style access. If your source location base URL is a MediaPackage Version 2 endpoint or an Amazon S3 bucket, MediaTailor can use AWS Signature Version 4 (SigV4) authentication to access the resource where your source content is stored.

Before you can use `AUTODETECT_SIGV4` with a MediaPackage Version 2 endpoint, you must meet these requirements:

- You must grant MediaTailor access to your MediaPackage endpoint by granting `mediatailor.amazonaws.com` principal access in an Origin Access policy on the endpoint.
- Your MediaTailor source location base URL must be a MediaPackage V2 endpoint.
- The caller of the API must have `mediapackagev2:GetObject` IAM permissions to read all top level manifests referenced by the MediaTailor source packaging configurations.

Before you can use `AUTODETECT_SIGV4` with an Amazon S3 bucket, you must meet these requirements:

- You must grant MediaTailor access to your S3 bucket by granting `mediatailor.amazonaws.com` principal access in IAM. For more information about configuring access in IAM, see [Access management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide.* .
- The `mediatailor.amazonaws.com` service principal must have permissions to read all top-level manifests referenced by the `VodSource` packaging configurations.
- The caller of the API must have `s3:GetObject` IAM permissions to read all top level manifests referenced by your MediaTailor `VodSource` packaging configurations.

SecretsManagerAccessTokenConfiguration -> (structure)

AWS Secrets Manager access token configuration parameters.

HeaderName -> (string)

The name of the HTTP header used to supply the access token in requests to the source location.

SecretArn -> (string)

The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the access token.

SecretStringKey -> (string)

The AWS Secrets Manager [SecretString](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html#SecretsManager-CreateSecret-request-SecretString.html) key associated with the access token. MediaTailor uses the key to look up SecretString key and value pair containing the access token.

Shorthand Syntax:

```
AccessType=string,SecretsManagerAccessTokenConfiguration={HeaderName=string,SecretArn=string,SecretStringKey=string}
```

JSON Syntax:

```
{
  "AccessType": "S3_SIGV4"|"SECRETS_MANAGER_ACCESS_TOKEN"|"AUTODETECT_SIGV4",
  "SecretsManagerAccessTokenConfiguration": {
    "HeaderName": "string",
    "SecretArn": "string",
    "SecretStringKey": "string"
  }
}
```

`--default-segment-delivery-configuration` (structure)

The optional configuration for the server that serves segments.

BaseUrl -> (string)

The hostname of the server that will be used to serve segments. This string must include the protocol, such as **https://** .

Shorthand Syntax:

```
BaseUrl=string
```

JSON Syntax:

```
{
  "BaseUrl": "string"
}
```

`--http-configuration` (structure)

The sourceâs HTTP package configurations.

BaseUrl -> (string)

The base URL for the source location host server. This string must include the protocol, such as **https://** .

Shorthand Syntax:

```
BaseUrl=string
```

JSON Syntax:

```
{
  "BaseUrl": "string"
}
```

`--segment-delivery-configurations` (list)

A list of the segment delivery configurations associated with this resource.

(structure)

The segment delivery configuration settings.

BaseUrl -> (string)

The base URL of the host or path of the segment delivery server that youâre using to serve segments. This is typically a content delivery network (CDN). The URL can be absolute or relative. To use an absolute URL include the protocol, such as `https://example.com/some/path` . To use a relative URL specify the relative path, such as `/some/path*` .

Name -> (string)

A unique identifier used to distinguish between multiple segment delivery configurations in a source location.

Shorthand Syntax:

```
BaseUrl=string,Name=string ...
```

JSON Syntax:

```
[
  {
    "BaseUrl": "string",
    "Name": "string"
  }
  ...
]
```

`--source-location-name` (string)

The name associated with the source location.

`--tags` (map)

The tags to assign to the source location. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html) .

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

AccessConfiguration -> (structure)

Access configuration parameters. Configures the type of authentication used to access content from your source location.

AccessType -> (string)

The type of authentication used to access content from `HttpConfiguration::BaseUrl` on your source location.

`S3_SIGV4` - AWS Signature Version 4 authentication for Amazon S3 hosted virtual-style access. If your source location base URL is an Amazon S3 bucket, MediaTailor can use AWS Signature Version 4 (SigV4) authentication to access the bucket where your source content is stored. Your MediaTailor source location baseURL must follow the S3 virtual hosted-style request URL format. For example, [https://bucket-name.s3.Region.amazonaws.com/key-name](https://bucket-name.s3.Region.amazonaws.com/key-name).

Before you can use `S3_SIGV4` , you must meet these requirements:

- You must allow MediaTailor to access your S3 bucket by granting mediatailor.amazonaws.com principal access in IAM. For information about configuring access in IAM, see Access management in the IAM User Guide.
- The mediatailor.amazonaws.com service principal must have permissions to read all top level manifests referenced by the VodSource packaging configurations.
- The caller of the API must have s3:GetObject IAM permissions to read all top level manifests referenced by your MediaTailor VodSource packaging configurations.

`AUTODETECT_SIGV4` - AWS Signature Version 4 authentication for a set of supported services: MediaPackage Version 2 and Amazon S3 hosted virtual-style access. If your source location base URL is a MediaPackage Version 2 endpoint or an Amazon S3 bucket, MediaTailor can use AWS Signature Version 4 (SigV4) authentication to access the resource where your source content is stored.

Before you can use `AUTODETECT_SIGV4` with a MediaPackage Version 2 endpoint, you must meet these requirements:

- You must grant MediaTailor access to your MediaPackage endpoint by granting `mediatailor.amazonaws.com` principal access in an Origin Access policy on the endpoint.
- Your MediaTailor source location base URL must be a MediaPackage V2 endpoint.
- The caller of the API must have `mediapackagev2:GetObject` IAM permissions to read all top level manifests referenced by the MediaTailor source packaging configurations.

Before you can use `AUTODETECT_SIGV4` with an Amazon S3 bucket, you must meet these requirements:

- You must grant MediaTailor access to your S3 bucket by granting `mediatailor.amazonaws.com` principal access in IAM. For more information about configuring access in IAM, see [Access management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide.* .
- The `mediatailor.amazonaws.com` service principal must have permissions to read all top-level manifests referenced by the `VodSource` packaging configurations.
- The caller of the API must have `s3:GetObject` IAM permissions to read all top level manifests referenced by your MediaTailor `VodSource` packaging configurations.

SecretsManagerAccessTokenConfiguration -> (structure)

AWS Secrets Manager access token configuration parameters.

HeaderName -> (string)

The name of the HTTP header used to supply the access token in requests to the source location.

SecretArn -> (string)

The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the access token.

SecretStringKey -> (string)

The AWS Secrets Manager [SecretString](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html#SecretsManager-CreateSecret-request-SecretString.html) key associated with the access token. MediaTailor uses the key to look up SecretString key and value pair containing the access token.

Arn -> (string)

The ARN to assign to the source location.

CreationTime -> (timestamp)

The time the source location was created.

DefaultSegmentDeliveryConfiguration -> (structure)

The optional configuration for the server that serves segments.

BaseUrl -> (string)

The hostname of the server that will be used to serve segments. This string must include the protocol, such as **https://** .

HttpConfiguration -> (structure)

The sourceâs HTTP package configurations.

BaseUrl -> (string)

The base URL for the source location host server. This string must include the protocol, such as **https://** .

LastModifiedTime -> (timestamp)

The time the source location was last modified.

SegmentDeliveryConfigurations -> (list)

The segment delivery configurations for the source location. For information about MediaTailor configurations, see [Working with configurations in AWS Elemental MediaTailor](https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html) .

(structure)

The segment delivery configuration settings.

BaseUrl -> (string)

The base URL of the host or path of the segment delivery server that youâre using to serve segments. This is typically a content delivery network (CDN). The URL can be absolute or relative. To use an absolute URL include the protocol, such as `https://example.com/some/path` . To use a relative URL specify the relative path, such as `/some/path*` .

Name -> (string)

A unique identifier used to distinguish between multiple segment delivery configurations in a source location.

SourceLocationName -> (string)

The name to assign to the source location.

Tags -> (map)

The tags to assign to the source location. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html) .

key -> (string)

value -> (string)