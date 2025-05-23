# get-glyphsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-maps/get-glyphs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-maps/get-glyphs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [geo-maps](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/geo-maps/index.html#cli-aws-geo-maps) ]

# get-glyphs

## Description

`GetGlyphs` returns the mapâs glyphs.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/geo-maps-2020-11-19/GetGlyphs)

## Synopsis

```
get-glyphs
--font-stack <value>
--font-unicode-range <value>
<outfile>
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

`--font-stack` (string)

Name of the `FontStack` to retrieve.

Example: `Amazon Ember Bold,Noto Sans Bold` .

The supported font stacks are as follows:

- Amazon Ember Bold
- Amazon Ember Bold Italic
- Amazon Ember Bold,Noto Sans Bold
- Amazon Ember Bold,Noto Sans Bold,Noto Sans Arabic Bold
- Amazon Ember Condensed RC BdItalic
- Amazon Ember Condensed RC Bold
- Amazon Ember Condensed RC Bold Italic
- Amazon Ember Condensed RC Bold,Noto Sans Bold
- Amazon Ember Condensed RC Bold,Noto Sans Bold,Noto Sans Arabic Condensed Bold
- Amazon Ember Condensed RC Light
- Amazon Ember Condensed RC Light Italic
- Amazon Ember Condensed RC LtItalic
- Amazon Ember Condensed RC Regular
- Amazon Ember Condensed RC Regular Italic
- Amazon Ember Condensed RC Regular,Noto Sans Regular
- Amazon Ember Condensed RC Regular,Noto Sans Regular,Noto Sans Arabic Condensed Regular
- Amazon Ember Condensed RC RgItalic
- Amazon Ember Condensed RC ThItalic
- Amazon Ember Condensed RC Thin
- Amazon Ember Condensed RC Thin Italic
- Amazon Ember Heavy
- Amazon Ember Heavy Italic
- Amazon Ember Light
- Amazon Ember Light Italic
- Amazon Ember Medium
- Amazon Ember Medium Italic
- Amazon Ember Medium,Noto Sans Medium
- Amazon Ember Medium,Noto Sans Medium,Noto Sans Arabic Medium
- Amazon Ember Regular
- Amazon Ember Regular Italic
- Amazon Ember Regular Italic,Noto Sans Italic
- Amazon Ember Regular Italic,Noto Sans Italic,Noto Sans Arabic Regular
- Amazon Ember Regular,Noto Sans Regular
- Amazon Ember Regular,Noto Sans Regular,Noto Sans Arabic Regular
- Amazon Ember Thin
- Amazon Ember Thin Italic
- AmazonEmberCdRC_Bd
- AmazonEmberCdRC_BdIt
- AmazonEmberCdRC_Lt
- AmazonEmberCdRC_LtIt
- AmazonEmberCdRC_Rg
- AmazonEmberCdRC_RgIt
- AmazonEmberCdRC_Th
- AmazonEmberCdRC_ThIt
- AmazonEmber_Bd
- AmazonEmber_BdIt
- AmazonEmber_He
- AmazonEmber_HeIt
- AmazonEmber_Lt
- AmazonEmber_LtIt
- AmazonEmber_Md
- AmazonEmber_MdIt
- AmazonEmber_Rg
- AmazonEmber_RgIt
- AmazonEmber_Th
- AmazonEmber_ThIt
- Noto Sans Black
- Noto Sans Black Italic
- Noto Sans Bold
- Noto Sans Bold Italic
- Noto Sans Extra Bold
- Noto Sans Extra Bold Italic
- Noto Sans Extra Light
- Noto Sans Extra Light Italic
- Noto Sans Italic
- Noto Sans Light
- Noto Sans Light Italic
- Noto Sans Medium
- Noto Sans Medium Italic
- Noto Sans Regular
- Noto Sans Semi Bold
- Noto Sans Semi Bold Italic
- Noto Sans Thin
- Noto Sans Thin Italic
- NotoSans-Bold
- NotoSans-Italic
- NotoSans-Medium
- NotoSans-Regular
- Open Sans Regular,Arial Unicode MS Regular

`--font-unicode-range` (string)

A Unicode range of characters to download glyphs for. This must be aligned to multiples of 256.

Example: `0-255.pdf`

`outfile` (string)
Filename where the content will be saved

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

Blob -> (blob)

The Glyph, as a binary blob.

ContentType -> (string)

Header that represents the format of the response. The response returns the following as the HTTP body.

CacheControl -> (string)

Header that instructs caching configuration for the client.

ETag -> (string)

The glyphâs Etag.