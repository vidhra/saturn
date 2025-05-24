# describe-templateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-template.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-template.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [quicksight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/index.html#cli-aws-quicksight) ]

# describe-template

## Description

Describes a templateâs metadata.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/DescribeTemplate)

## Synopsis

```
describe-template
--aws-account-id <value>
--template-id <value>
[--version-number <value>]
[--alias-name <value>]
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

The ID of the Amazon Web Services account that contains the template that youâre describing.

`--template-id` (string)

The ID for the template.

`--version-number` (long)

(Optional) The number for the version to describe. If a `VersionNumber` parameter value isnât provided, the latest version of the template is described.

`--alias-name` (string)

The alias of the template that you want to describe. If you name a specific alias, you describe the version that the alias points to. You can specify the latest version of the template by providing the keyword `$LATEST` in the `AliasName` parameter. The keyword `$PUBLISHED` doesnât apply to templates.

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

Template -> (structure)

The template structure for the object you want to describe.

Arn -> (string)

The Amazon Resource Name (ARN) of the template.

Name -> (string)

The display name of the template.

Version -> (structure)

A structure describing the versions of the template.

CreatedTime -> (timestamp)

The time that this template version was created.

Errors -> (list)

Errors associated with this template version.

(structure)

List of errors that occurred when the template version creation failed.

Type -> (string)

Type of error.

Message -> (string)

Description of the error type.

ViolatedEntities -> (list)

An error path that shows which entities caused the template error.

(structure)

An object, structure, or sub-structure of an analysis, template, or dashboard.

Path -> (string)

The hierarchical path of the entity within the analysis, template, or dashboard definition tree.

VersionNumber -> (long)

The version number of the template version.

Status -> (string)

The status that is associated with the template.

- `CREATION_IN_PROGRESS`
- `CREATION_SUCCESSFUL`
- `CREATION_FAILED`
- `UPDATE_IN_PROGRESS`
- `UPDATE_SUCCESSFUL`
- `UPDATE_FAILED`
- `DELETED`

DataSetConfigurations -> (list)

Schema of the dataset identified by the placeholder. Any dashboard created from this template should be bound to new datasets matching the same schema described through this API operation.

(structure)

Dataset configuration.

Placeholder -> (string)

Placeholder.

DataSetSchema -> (structure)

Dataset schema.

ColumnSchemaList -> (list)

A structure containing the list of column schemas.

(structure)

The column schema.

Name -> (string)

The name of the column schema.

DataType -> (string)

The data type of the column schema.

GeographicRole -> (string)

The geographic role of the column schema.

ColumnGroupSchemaList -> (list)

A structure containing the list of column group schemas.

(structure)

The column group schema.

Name -> (string)

The name of the column group schema.

ColumnGroupColumnSchemaList -> (list)

A structure containing the list of schemas for column group columns.

(structure)

A structure describing the name, data type, and geographic role of the columns.

Name -> (string)

The name of the column groupâs column schema.

Description -> (string)

The description of the template.

SourceEntityArn -> (string)

The Amazon Resource Name (ARN) of an analysis or template that was used to create this template.

ThemeArn -> (string)

The ARN of the theme associated with this version of the template.

Sheets -> (list)

A list of the associated sheets with the unique identifier and name of each sheet.

(structure)

A *sheet* , which is an object that contains a set of visuals that are viewed together on one page in Amazon QuickSight. Every analysis and dashboard contains at least one sheet. Each sheet contains at least one visualization widget, for example a chart, pivot table, or narrative insight. Sheets can be associated with other components, such as controls, filters, and so on.

SheetId -> (string)

The unique identifier associated with a sheet.

Name -> (string)

The name of a sheet. This name is displayed on the sheetâs tab in the Amazon QuickSight console.

Images -> (list)

A list of images on a sheet.

(structure)

An image that is located on a sheet.

SheetImageId -> (string)

The ID of the sheet image.

Source -> (structure)

The source of the image.

SheetImageStaticFileSource -> (structure)

The source of the static file that contains the image.

StaticFileId -> (string)

The ID of the static file that contains the image.

Scaling -> (structure)

Determines how the image is scaled.

ScalingType -> (string)

The scaling option to use when fitting the image inside the container.

Valid values are defined as follows:

- `SCALE_TO_WIDTH` : The image takes up the entire width of the container. The image aspect ratio is preserved.
- `SCALE_TO_HEIGHT` : The image takes up the entire height of the container. The image aspect ratio is preserved.
- `SCALE_TO_CONTAINER` : The image takes up the entire width and height of the container. The image aspect ratio is not preserved.
- `SCALE_NONE` : The image is displayed in its original size and is not scaled to the container.

Tooltip -> (structure)

The tooltip to be shown when hovering over the image.

TooltipText -> (structure)

The text that appears in the tooltip.

PlainText -> (string)

The plain text format.

Visibility -> (string)

The visibility of the tooltip.

ImageContentAltText -> (string)

The alt text for the image.

Interactions -> (structure)

The general image interactions setup for an image.

ImageMenuOption -> (structure)

The menu options for the image.

AvailabilityStatus -> (string)

The availability status of the image menu. If the value of this property is set to `ENABLED` , dashboard readers can interact with the image menu.

Actions -> (list)

A list of custom actions that are configured for an image.

(structure)

A custom action defined on an image.

CustomActionId -> (string)

The ID of the custom action.

Name -> (string)

The name of the custom action.

Status -> (string)

The status of the custom action.

Trigger -> (string)

The trigger of the `VisualCustomAction` .

Valid values are defined as follows:

- `CLICK` : Initiates a custom action by a left pointer click on a data point.
- `MENU` : Initiates a custom action by right pointer click from the menu.

ActionOperations -> (list)

A list of `ImageCustomActionOperations` .

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

(structure)

The operation that is defined by the custom action.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

NavigationOperation -> (structure)

The navigation operation that navigates between different sheets in the same analysis.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

LocalNavigationConfiguration -> (structure)

The configuration that chooses the navigation target.

TargetSheetId -> (string)

The sheet that is targeted for navigation in the same analysis.

URLOperation -> (structure)

The URL operation that opens a link to another webpage.

URLTemplate -> (string)

THe URL link of the `CustomActionURLOperation` .

URLTarget -> (string)

The target of the `CustomActionURLOperation` .

Valid values are defined as follows:

- `NEW_TAB` : Opens the target URL in a new browser tab.
- `NEW_WINDOW` : Opens the target URL in a new browser window.
- `SAME_TAB` : Opens the target URL in the same browser tab.

SetParametersOperation -> (structure)

The set parameter operation that sets parameters in custom action.

ParameterValueConfigurations -> (list)

The parameter that determines the value configuration.

(structure)

The configuration of adding parameters in action.

DestinationParameterName -> (string)

The destination parameter name of the `SetParameterValueConfiguration` .

Value -> (structure)

The configuration of destination parameter values.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

CustomValuesConfiguration -> (structure)

The configuration of custom values for destination parameter in `DestinationParameterValueConfiguration` .

IncludeNullValue -> (boolean)

Includes the null value in custom action parameter values.

CustomValues -> (structure)

The customized parameter values.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

StringValues -> (list)

A list of string-type parameter values.

(string)

IntegerValues -> (list)

A list of integer-type parameter values.

(long)

DecimalValues -> (list)

A list of decimal-type parameter values.

(double)

DateTimeValues -> (list)

A list of datetime-type parameter values.

(timestamp)

SelectAllValueOptions -> (string)

The configuration that selects all options.

SourceParameterName -> (string)

The source parameter name of the destination parameter.

SourceField -> (string)

The source field ID of the destination parameter.

SourceColumn -> (structure)

A column of a data set.

DataSetIdentifier -> (string)

The data set that the column belongs to.

ColumnName -> (string)

The name of the column.

TemplateId -> (string)

The ID for the template. This is unique per Amazon Web Services Region for each Amazon Web Services account.

LastUpdatedTime -> (timestamp)

Time when this was last updated.

CreatedTime -> (timestamp)

Time when this was created.

Status -> (integer)

The HTTP status of the request.

RequestId -> (string)

The Amazon Web Services request ID for this operation.