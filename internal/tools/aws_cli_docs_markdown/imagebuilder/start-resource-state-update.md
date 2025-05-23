# start-resource-state-updateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/start-resource-state-update.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/start-resource-state-update.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [imagebuilder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/index.html#cli-aws-imagebuilder) ]

# start-resource-state-update

## Description

Begin asynchronous resource state update for lifecycle changes to the specified image resources.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/imagebuilder-2019-12-02/StartResourceStateUpdate)

## Synopsis

```
start-resource-state-update
--resource-arn <value>
--state <value>
[--execution-role <value>]
[--include-resources <value>]
[--exclusion-rules <value>]
[--update-at <value>]
[--client-token <value>]
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

`--resource-arn` (string)

The ARN of the Image Builder resource that is updated. The state update might also impact associated resources.

`--state` (structure)

Indicates the lifecycle action to take for this request.

status -> (string)

Shows the current lifecycle policy action that was applied to an impacted resource.

Shorthand Syntax:

```
status=string
```

JSON Syntax:

```
{
  "status": "AVAILABLE"|"DELETED"|"DEPRECATED"|"DISABLED"
}
```

`--execution-role` (string)

The name or Amazon Resource Name (ARN) of the IAM role thatâs used to update image state.

`--include-resources` (structure)

A list of image resources to update state for.

amis -> (boolean)

Specifies whether the lifecycle action should apply to distributed AMIs

snapshots -> (boolean)

Specifies whether the lifecycle action should apply to snapshots associated with distributed AMIs.

containers -> (boolean)

Specifies whether the lifecycle action should apply to distributed containers.

Shorthand Syntax:

```
amis=boolean,snapshots=boolean,containers=boolean
```

JSON Syntax:

```
{
  "amis": true|false,
  "snapshots": true|false,
  "containers": true|false
}
```

`--exclusion-rules` (structure)

Skip action on the image resource and associated resources if specified exclusion rules are met.

amis -> (structure)

Defines criteria for AMIs that are excluded from lifecycle actions.

isPublic -> (boolean)

Configures whether public AMIs are excluded from the lifecycle action.

regions -> (list)

Configures Amazon Web Services Regions that are excluded from the lifecycle action.

(string)

sharedAccounts -> (list)

Specifies Amazon Web Services accounts whose resources are excluded from the lifecycle action.

(string)

lastLaunched -> (structure)

Specifies configuration details for Image Builder to exclude the most recent resources from lifecycle actions.

value -> (integer)

The integer number of units for the time period. For example `6` (months).

unit -> (string)

Defines the unit of time that the lifecycle policy uses to calculate elapsed time since the last instance launched from the AMI. For example: days, weeks, months, or years.

tagMap -> (map)

Lists tags that should be excluded from lifecycle actions for the AMIs that have them.

key -> (string)

value -> (string)

Shorthand Syntax:

```
amis={isPublic=boolean,regions=[string,string],sharedAccounts=[string,string],lastLaunched={value=integer,unit=string},tagMap={KeyName1=string,KeyName2=string}}
```

JSON Syntax:

```
{
  "amis": {
    "isPublic": true|false,
    "regions": ["string", ...],
    "sharedAccounts": ["string", ...],
    "lastLaunched": {
      "value": integer,
      "unit": "DAYS"|"WEEKS"|"MONTHS"|"YEARS"
    },
    "tagMap": {"string": "string"
      ...}
  }
}
```

`--update-at` (timestamp)

The timestamp that indicates when resources are updated by a lifecycle action.

`--client-token` (string)

Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference* .

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

lifecycleExecutionId -> (string)

Identifies the lifecycle runtime instance that started the resource state update.

resourceArn -> (string)

The requested ARN of the Image Builder resource for the asynchronous update.