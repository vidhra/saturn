# get-tileÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-geospatial/get-tile.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-geospatial/get-tile.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker-geospatial](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-geospatial/index.html#cli-aws-sagemaker-geospatial) ]

# get-tile

## Description

Gets a web mercator tile for the given Earth Observation job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-geospatial-2020-05-27/GetTile)

## Synopsis

```
get-tile
--arn <value>
[--execution-role-arn <value>]
--image-assets <value>
[--image-mask | --no-image-mask]
[--output-data-type <value>]
[--output-format <value>]
[--property-filters <value>]
--target <value>
[--time-range-filter <value>]
--x <value>
--y <value>
--z <value>
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

`--arn` (string)

The Amazon Resource Name (ARN) of the tile operation.

`--execution-role-arn` (string)

The Amazon Resource Name (ARN) of the IAM role that you specify.

`--image-assets` (list)

The particular assets or bands to tile.

(string)

Syntax:

```
"string" "string" ...
```

`--image-mask` | `--no-image-mask` (boolean)

Determines whether or not to return a valid data mask.

`--output-data-type` (string)

The output data type of the tile operation.

Possible values:

- `INT32`
- `FLOAT32`
- `INT16`
- `FLOAT64`
- `UINT16`

`--output-format` (string)

The data format of the output tile. The formats include .npy, .png and .jpg.

`--property-filters` (string)

Property filters for the imagery to tile.

`--target` (string)

Determines what part of the Earth Observation job to tile. âINPUTâ or âOUTPUTâ are the valid options.

Possible values:

- `INPUT`
- `OUTPUT`

`--time-range-filter` (string)

Time range filter applied to imagery to find the images to tile.

`--x` (integer)

The x coordinate of the tile input.

`--y` (integer)

The y coordinate of the tile input.

`--z` (integer)

The z coordinate of the tile input.

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

BinaryFile -> (streaming blob)

The output binary file.