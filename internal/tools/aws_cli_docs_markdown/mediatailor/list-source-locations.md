# list-source-locationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/list-source-locations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/list-source-locations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediatailor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/index.html#cli-aws-mediatailor) ]

# list-source-locations

## Description

Lists the source locations for a channel. A source location defines the host server URL, and contains a list of sources.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/ListSourceLocations)

`list-source-locations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Items`

## Synopsis

```
list-source-locations
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

Items -> (list)

A list of source locations.

(structure)

A source location is a container for sources. For more information about source locations, see [Working with source locations](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html) in the *MediaTailor User Guide* .

AccessConfiguration -> (structure)

The access configuration for the source location.

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

The ARN of the SourceLocation.

CreationTime -> (timestamp)

The timestamp that indicates when the source location was created.

DefaultSegmentDeliveryConfiguration -> (structure)

The default segment delivery configuration.

BaseUrl -> (string)

The hostname of the server that will be used to serve segments. This string must include the protocol, such as **https://** .

HttpConfiguration -> (structure)

The HTTP configuration for the source location.

BaseUrl -> (string)

The base URL for the source location host server. This string must include the protocol, such as **https://** .

LastModifiedTime -> (timestamp)

The timestamp that indicates when the source location was last modified.

SegmentDeliveryConfigurations -> (list)

The segment delivery configurations for the source location.

(structure)

The segment delivery configuration settings.

BaseUrl -> (string)

The base URL of the host or path of the segment delivery server that youâre using to serve segments. This is typically a content delivery network (CDN). The URL can be absolute or relative. To use an absolute URL include the protocol, such as `https://example.com/some/path` . To use a relative URL specify the relative path, such as `/some/path*` .

Name -> (string)

A unique identifier used to distinguish between multiple segment delivery configurations in a source location.

SourceLocationName -> (string)

The name of the source location.

Tags -> (map)

The tags assigned to the source location. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html) .

key -> (string)

value -> (string)

NextToken -> (string)

Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.