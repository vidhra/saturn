# describe-brandÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-brand.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-brand.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [quicksight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/index.html#cli-aws-quicksight) ]

# describe-brand

## Description

Describes a brand.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/DescribeBrand)

## Synopsis

```
describe-brand
--aws-account-id <value>
--brand-id <value>
[--version-id <value>]
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

`--aws-account-id` (string)

The ID of the Amazon Web Services account that owns the brand.

`--brand-id` (string)

The ID of the Amazon QuickSight brand.

`--version-id` (string)

The ID of the specific version. The default value is the latest version.

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

RequestId -> (string)

The Amazon Web Services request ID for this operation.

BrandDetail -> (structure)

The details of the brand.

BrandId -> (string)

The ID of the Amazon QuickSight brand.

Arn -> (string)

The Amazon Resource Name (ARN) of the brand.

BrandStatus -> (string)

The status of the brand.

CreatedTime -> (timestamp)

The time that the brand was created.

LastUpdatedTime -> (timestamp)

The last time the brand was updated.

VersionId -> (string)

The ID of the version.

VersionStatus -> (string)

The status of the version.

Errors -> (list)

A list of errors that occurred during the most recent brand operation.

(string)

Logo -> (structure)

The logo details.

AltText -> (string)

The alt text for the logo.

LogoSet -> (structure)

A set of configured logos.

Primary -> (structure)

The primary logo.

Original -> (structure)

The original image.

Source -> (tagged union structure)

The source of the logo image.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `PublicUrl`, `S3Uri`.

PublicUrl -> (string)

The public URL that points to the source image.

S3Uri -> (string)

The Amazon S3 URI that points to the source image.

GeneratedImageUrl -> (string)

The URL that points to the generated logo image.

Height64 -> (structure)

The image with the height set to 64 pixels.

Source -> (tagged union structure)

The source of the logo image.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `PublicUrl`, `S3Uri`.

PublicUrl -> (string)

The public URL that points to the source image.

S3Uri -> (string)

The Amazon S3 URI that points to the source image.

GeneratedImageUrl -> (string)

The URL that points to the generated logo image.

Height32 -> (structure)

The image with the height set to 32 pixels.

Source -> (tagged union structure)

The source of the logo image.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `PublicUrl`, `S3Uri`.

PublicUrl -> (string)

The public URL that points to the source image.

S3Uri -> (string)

The Amazon S3 URI that points to the source image.

GeneratedImageUrl -> (string)

The URL that points to the generated logo image.

Favicon -> (structure)

The favicon logo.

Original -> (structure)

The original image.

Source -> (tagged union structure)

The source of the logo image.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `PublicUrl`, `S3Uri`.

PublicUrl -> (string)

The public URL that points to the source image.

S3Uri -> (string)

The Amazon S3 URI that points to the source image.

GeneratedImageUrl -> (string)

The URL that points to the generated logo image.

Height64 -> (structure)

The image with the height set to 64 pixels.

Source -> (tagged union structure)

The source of the logo image.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `PublicUrl`, `S3Uri`.

PublicUrl -> (string)

The public URL that points to the source image.

S3Uri -> (string)

The Amazon S3 URI that points to the source image.

GeneratedImageUrl -> (string)

The URL that points to the generated logo image.

Height32 -> (structure)

The image with the height set to 32 pixels.

Source -> (tagged union structure)

The source of the logo image.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `PublicUrl`, `S3Uri`.

PublicUrl -> (string)

The public URL that points to the source image.

S3Uri -> (string)

The Amazon S3 URI that points to the source image.

GeneratedImageUrl -> (string)

The URL that points to the generated logo image.

BrandDefinition -> (structure)

The definition of the brand.

BrandName -> (string)

The name of the brand.

Description -> (string)

The description of the brand.

ApplicationTheme -> (structure)

The application theme of the brand.

BrandColorPalette -> (structure)

The color palette.

Primary -> (structure)

The primary color.

Foreground -> (string)

The foreground color.

Background -> (string)

The background color.

Secondary -> (structure)

The secondary color.

Foreground -> (string)

The foreground color.

Background -> (string)

The background color.

Accent -> (structure)

The color that is used for accent elements.

Foreground -> (string)

The foreground color.

Background -> (string)

The background color.

Measure -> (structure)

The color that is used for measure elements.

Foreground -> (string)

The foreground color.

Background -> (string)

The background color.

Dimension -> (structure)

The color that is used for dimension elements.

Foreground -> (string)

The foreground color.

Background -> (string)

The background color.

Success -> (structure)

The color that is used for success elements.

Foreground -> (string)

The foreground color.

Background -> (string)

The background color.

Info -> (structure)

The color that is used for info elements.

Foreground -> (string)

The foreground color.

Background -> (string)

The background color.

Warning -> (structure)

The color that is used for warning elements.

Foreground -> (string)

The foreground color.

Background -> (string)

The background color.

Danger -> (structure)

The color that is used for danger elements.

Foreground -> (string)

The foreground color.

Background -> (string)

The background color.

BrandElementStyle -> (structure)

The element style.

NavbarStyle -> (structure)

The navigation bar style.

GlobalNavbar -> (structure)

The global navigation bar style.

Foreground -> (string)

The foreground color.

Background -> (string)

The background color.

ContextualNavbar -> (structure)

The contextual navigation bar style.

Foreground -> (string)

The foreground color.

Background -> (string)

The background color.

LogoConfiguration -> (structure)

The logo configuration of the brand.

AltText -> (string)

The alt text for the logo.

LogoSet -> (structure)

A set of configured logos.

Primary -> (structure)

The primary logo.

Original -> (structure)

The original image.

Source -> (tagged union structure)

The source of the image.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `PublicUrl`, `S3Uri`.

PublicUrl -> (string)

The public URL that points to the source image.

S3Uri -> (string)

The Amazon S3 URI that points to the source image.

Favicon -> (structure)

The favicon logo.

Original -> (structure)

The original image.

Source -> (tagged union structure)

The source of the image.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `PublicUrl`, `S3Uri`.

PublicUrl -> (string)

The public URL that points to the source image.

S3Uri -> (string)

The Amazon S3 URI that points to the source image.