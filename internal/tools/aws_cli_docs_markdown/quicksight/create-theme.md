# create-themeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-theme.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-theme.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [quicksight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/index.html#cli-aws-quicksight) ]

# create-theme

## Description

Creates a theme.

A *theme* is set of configuration options for color and layout. Themes apply to analyses and dashboards. For more information, see [Using Themes in Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/themes-in-quicksight.html) in the *Amazon QuickSight User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/CreateTheme)

## Synopsis

```
create-theme
--aws-account-id <value>
--theme-id <value>
--name <value>
--base-theme-id <value>
[--version-description <value>]
--configuration <value>
[--permissions <value>]
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

`--aws-account-id` (string)

The ID of the Amazon Web Services account where you want to store the new theme.

`--theme-id` (string)

An ID for the theme that you want to create. The theme ID is unique per Amazon Web Services Region in each Amazon Web Services account.

`--name` (string)

A display name for the theme.

`--base-theme-id` (string)

The ID of the theme that a custom theme will inherit from. All themes inherit from one of the starting themes defined by Amazon QuickSight. For a list of the starting themes, use `ListThemes` or choose **Themes** from within an analysis.

`--version-description` (string)

A description of the first version of the theme that youâre creating. Every time `UpdateTheme` is called, a new version is created. Each version of the theme has a description of the version in the `VersionDescription` field.

`--configuration` (structure)

The theme configuration, which contains the theme display properties.

DataColorPalette -> (structure)

Color properties that apply to chart data colors.

Colors -> (list)

The hexadecimal codes for the colors.

(string)

MinMaxGradient -> (list)

The minimum and maximum hexadecimal codes that describe a color gradient.

(string)

EmptyFillColor -> (string)

The hexadecimal code of a color that applies to charts where a lack of data is highlighted.

UIColorPalette -> (structure)

Color properties that apply to the UI and to charts, excluding the colors that apply to data.

PrimaryForeground -> (string)

The color of text and other foreground elements that appear over the primary background regions, such as grid lines, borders, table banding, icons, and so on.

PrimaryBackground -> (string)

The background color that applies to visuals and other high emphasis UI.

SecondaryForeground -> (string)

The foreground color that applies to any sheet title, sheet control text, or UI that appears over the secondary background.

SecondaryBackground -> (string)

The background color that applies to the sheet background and sheet controls.

Accent -> (string)

This color is that applies to selected states and buttons.

AccentForeground -> (string)

The foreground color that applies to any text or other elements that appear over the accent color.

Danger -> (string)

The color that applies to error messages.

DangerForeground -> (string)

The foreground color that applies to any text or other elements that appear over the error color.

Warning -> (string)

This color that applies to warning and informational messages.

WarningForeground -> (string)

The foreground color that applies to any text or other elements that appear over the warning color.

Success -> (string)

The color that applies to success messages, for example the check mark for a successful download.

SuccessForeground -> (string)

The foreground color that applies to any text or other elements that appear over the success color.

Dimension -> (string)

The color that applies to the names of fields that are identified as dimensions.

DimensionForeground -> (string)

The foreground color that applies to any text or other elements that appear over the dimension color.

Measure -> (string)

The color that applies to the names of fields that are identified as measures.

MeasureForeground -> (string)

The foreground color that applies to any text or other elements that appear over the measure color.

Sheet -> (structure)

Display options related to sheets.

Tile -> (structure)

The display options for tiles.

Border -> (structure)

The border around a tile.

Show -> (boolean)

The option to enable display of borders for visuals.

TileLayout -> (structure)

The layout options for tiles.

Gutter -> (structure)

The gutter settings that apply between tiles.

Show -> (boolean)

This Boolean value controls whether to display a gutter space between sheet tiles.

Margin -> (structure)

The margin settings that apply around the outside edge of sheets.

Show -> (boolean)

This Boolean value controls whether to display sheet margins.

Typography -> (structure)

Determines the typography options.

FontFamilies -> (list)

Determines the list of font families.

(structure)

Determines the font settings.

FontFamily -> (string)

Determines the font family settings.

JSON Syntax:

```
{
  "DataColorPalette": {
    "Colors": ["string", ...],
    "MinMaxGradient": ["string", ...],
    "EmptyFillColor": "string"
  },
  "UIColorPalette": {
    "PrimaryForeground": "string",
    "PrimaryBackground": "string",
    "SecondaryForeground": "string",
    "SecondaryBackground": "string",
    "Accent": "string",
    "AccentForeground": "string",
    "Danger": "string",
    "DangerForeground": "string",
    "Warning": "string",
    "WarningForeground": "string",
    "Success": "string",
    "SuccessForeground": "string",
    "Dimension": "string",
    "DimensionForeground": "string",
    "Measure": "string",
    "MeasureForeground": "string"
  },
  "Sheet": {
    "Tile": {
      "Border": {
        "Show": true|false
      }
    },
    "TileLayout": {
      "Gutter": {
        "Show": true|false
      },
      "Margin": {
        "Show": true|false
      }
    }
  },
  "Typography": {
    "FontFamilies": [
      {
        "FontFamily": "string"
      }
      ...
    ]
  }
}
```

`--permissions` (list)

A valid grouping of resource permissions to apply to the new theme.

(structure)

Permission for the resource.

Principal -> (string)

The Amazon Resource Name (ARN) of the principal. This can be one of the following:

- The ARN of an Amazon QuickSight user or group associated with a data source or dataset. (This is common.)
- The ARN of an Amazon QuickSight user, group, or namespace associated with an analysis, dashboard, template, or theme. (This is common.)
- The ARN of an Amazon Web Services account root: This is an IAM ARN rather than a QuickSight ARN. Use this option only to share resources (templates) across Amazon Web Services accounts. (This is less common.)

Actions -> (list)

The IAM action to grant or revoke permissions on.

(string)

Shorthand Syntax:

```
Principal=string,Actions=string,string ...
```

JSON Syntax:

```
[
  {
    "Principal": "string",
    "Actions": ["string", ...]
  }
  ...
]
```

`--tags` (list)

A map of the key-value pairs for the resource tag or tags that you want to add to the resource.

(structure)

The key or keys of the key-value pairs for the resource tag or tags assigned to the resource.

Key -> (string)

Tag key.

Value -> (string)

Tag value.

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

Arn -> (string)

The Amazon Resource Name (ARN) for the theme.

VersionArn -> (string)

The Amazon Resource Name (ARN) for the new theme.

ThemeId -> (string)

The ID of the theme.

CreationStatus -> (string)

The theme creation status.

Status -> (integer)

The HTTP status of the request.

RequestId -> (string)

The Amazon Web Services request ID for this operation.