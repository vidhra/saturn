# create-workspace-bundleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/create-workspace-bundle.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/create-workspace-bundle.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [workspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/index.html#cli-aws-workspaces) ]

# create-workspace-bundle

## Description

Creates the specified WorkSpace bundle. For more information about creating WorkSpace bundles, see [Create a Custom WorkSpaces Image and Bundle](https://docs.aws.amazon.com/workspaces/latest/adminguide/create-custom-bundle.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/CreateWorkspaceBundle)

## Synopsis

```
create-workspace-bundle
--bundle-name <value>
--bundle-description <value>
--image-id <value>
--compute-type <value>
--user-storage <value>
[--root-storage <value>]
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

`--bundle-name` (string)

The name of the bundle.

`--bundle-description` (string)

The description of the bundle.

`--image-id` (string)

The identifier of the image that is used to create the bundle.

`--compute-type` (structure)

Describes the compute type of the bundle.

Name -> (string)

The compute type.

Shorthand Syntax:

```
Name=string
```

JSON Syntax:

```
{
  "Name": "VALUE"|"STANDARD"|"PERFORMANCE"|"POWER"|"GRAPHICS"|"POWERPRO"|"GENERALPURPOSE_4XLARGE"|"GENERALPURPOSE_8XLARGE"|"GRAPHICSPRO"|"GRAPHICS_G4DN"|"GRAPHICSPRO_G4DN"
}
```

`--user-storage` (structure)

Describes the user volume for a WorkSpace bundle.

Capacity -> (string)

The size of the user volume.

Shorthand Syntax:

```
Capacity=string
```

JSON Syntax:

```
{
  "Capacity": "string"
}
```

`--root-storage` (structure)

Describes the root volume for a WorkSpace bundle.

Capacity -> (string)

The size of the root volume.

Shorthand Syntax:

```
Capacity=string
```

JSON Syntax:

```
{
  "Capacity": "string"
}
```

`--tags` (list)

The tags associated with the bundle.

### Note

To add tags at the same time when youâre creating the bundle, you must create an IAM policy that grants your IAM user permissions to use `workspaces:CreateTags` .

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

WorkspaceBundle -> (structure)

Describes a WorkSpace bundle.

BundleId -> (string)

The identifier of the bundle.

Name -> (string)

The name of the bundle.

Owner -> (string)

The owner of the bundle. This is the account identifier of the owner, or `AMAZON` if the bundle is provided by Amazon Web Services.

Description -> (string)

The description of the bundle.

ImageId -> (string)

The identifier of the image that was used to create the bundle.

RootStorage -> (structure)

The size of the root volume.

Capacity -> (string)

The size of the root volume.

UserStorage -> (structure)

The size of the user volume.

Capacity -> (string)

The size of the user volume.

ComputeType -> (structure)

The compute type of the bundle. For more information, see [Amazon WorkSpaces Bundles](http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles) .

Name -> (string)

The compute type.

LastUpdatedTime -> (timestamp)

The last time that the bundle was updated.

CreationTime -> (timestamp)

The time when the bundle was created.

State -> (string)

The state of the WorkSpace bundle.

BundleType -> (string)

The type of WorkSpace bundle.