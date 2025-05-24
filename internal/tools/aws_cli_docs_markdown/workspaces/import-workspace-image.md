# import-workspace-imageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/import-workspace-image.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/import-workspace-image.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [workspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/index.html#cli-aws-workspaces) ]

# import-workspace-image

## Description

Imports the specified Windows 10 or 11 Bring Your Own License (BYOL) image into Amazon WorkSpaces. The image must be an already licensed Amazon EC2 image that is in your Amazon Web Services account, and you must own the image. For more information about creating BYOL images, see [Bring Your Own Windows Desktop Licenses](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/ImportWorkspaceImage)

## Synopsis

```
import-workspace-image
--ec2-image-id <value>
--ingestion-process <value>
--image-name <value>
--image-description <value>
[--tags <value>]
[--applications <value>]
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

`--ec2-image-id` (string)

The identifier of the EC2 image.

`--ingestion-process` (string)

The ingestion process to be used when importing the image, depending on which protocol you want to use for your BYOL Workspace image, either PCoIP, WSP, or bring your own protocol (BYOP). To use DCV, specify a value that ends in `_WSP` . To use PCoIP, specify a value that does not end in `_WSP` . To use BYOP, specify a value that ends in `_BYOP` .

For non-GPU-enabled bundles (bundles other than Graphics or GraphicsPro), specify `BYOL_REGULAR` , `BYOL_REGULAR_WSP` , or `BYOL_REGULAR_BYOP` , depending on the protocol.

### Note

The `BYOL_REGULAR_BYOP` and `BYOL_GRAPHICS_G4DN_BYOP` values are only supported by Amazon WorkSpaces Core. Contact your account team to be allow-listed to use these values. For more information, see [Amazon WorkSpaces Core](http://aws.amazon.com/workspaces/core/) .

Possible values:

- `BYOL_REGULAR`
- `BYOL_GRAPHICS`
- `BYOL_GRAPHICSPRO`
- `BYOL_GRAPHICS_G4DN`
- `BYOL_REGULAR_WSP`
- `BYOL_GRAPHICS_G4DN_WSP`
- `BYOL_REGULAR_BYOP`
- `BYOL_GRAPHICS_G4DN_BYOP`

`--image-name` (string)

The name of the WorkSpace image.

`--image-description` (string)

The description of the WorkSpace image.

`--tags` (list)

The tags. Each WorkSpaces resource can have a maximum of 50 tags.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--applications` (list)

If specified, the version of Microsoft Office to subscribe to. Valid only for Windows 10 and 11 BYOL images. For more information about subscribing to Office for BYOL images, see [Bring Your Own Windows Desktop Licenses](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html) .

### Note

- Although this parameter is an array, only one item is allowed at this time.
- During the image import process, non-GPU DCV (formerly WSP) WorkSpaces with Windows 11 support only `Microsoft_Office_2019` . GPU DCV (formerly WSP) WorkSpaces with Windows 11 do not support Office installation.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  Microsoft_Office_2016
  Microsoft_Office_2019
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

ImageId -> (string)

The identifier of the WorkSpace image.