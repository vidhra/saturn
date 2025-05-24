# get-lifecycle-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-lifecycle-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-lifecycle-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [imagebuilder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/index.html#cli-aws-imagebuilder) ]

# get-lifecycle-policy

## Description

Get details for the specified image lifecycle policy.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/imagebuilder-2019-12-02/GetLifecyclePolicy)

## Synopsis

```
get-lifecycle-policy
--lifecycle-policy-arn <value>
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

`--lifecycle-policy-arn` (string)

Specifies the Amazon Resource Name (ARN) of the image lifecycle policy resource to get.

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

lifecyclePolicy -> (structure)

The ARN of the image lifecycle policy resource that was returned.

arn -> (string)

The Amazon Resource Name (ARN) of the lifecycle policy resource.

name -> (string)

The name of the lifecycle policy.

description -> (string)

Optional description for the lifecycle policy.

status -> (string)

Indicates whether the lifecycle policy resource is enabled.

executionRole -> (string)

The name or Amazon Resource Name (ARN) of the IAM role that Image Builder uses to run the lifecycle policy. This is a custom role that you create.

resourceType -> (string)

The type of resources the lifecycle policy targets.

policyDetails -> (list)

The configuration details for a lifecycle policy resource.

(structure)

The configuration details for a lifecycle policy resource.

action -> (structure)

Configuration details for the policy action.

type -> (string)

Specifies the lifecycle action to take.

includeResources -> (structure)

Specifies the resources that the lifecycle policy applies to.

amis -> (boolean)

Specifies whether the lifecycle action should apply to distributed AMIs.

snapshots -> (boolean)

Specifies whether the lifecycle action should apply to snapshots associated with distributed AMIs.

containers -> (boolean)

Specifies whether the lifecycle action should apply to distributed containers.

filter -> (structure)

Specifies the resources that the lifecycle policy applies to.

type -> (string)

Filter resources based on either `age` or `count` .

value -> (integer)

The number of units for the time period or for the count. For example, a value of `6` might refer to six months or six AMIs.

### Note

For count-based filters, this value represents the minimum number of resources to keep on hand. If you have fewer resources than this number, the resource is excluded from lifecycle actions.

unit -> (string)

Defines the unit of time that the lifecycle policy uses to determine impacted resources. This is required for age-based rules.

retainAtLeast -> (integer)

For age-based filters, this is the number of resources to keep on hand after the lifecycle `DELETE` action is applied. Impacted resources are only deleted if you have more than this number of resources. If you have fewer resources than this number, the impacted resource is not deleted.

exclusionRules -> (structure)

Additional rules to specify resources that should be exempt from policy actions.

tagMap -> (map)

Contains a list of tags that Image Builder uses to skip lifecycle actions for Image Builder image resources that have them.

key -> (string)

value -> (string)

amis -> (structure)

Lists configuration values that apply to AMIs that Image Builder should exclude from the lifecycle action.

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

resourceSelection -> (structure)

Resource selection criteria used to run the lifecycle policy.

recipes -> (list)

A list of recipes that are used as selection criteria for the output images that the lifecycle policy applies to.

(structure)

Specifies an Image Builder recipe that the lifecycle policy uses for resource selection.

name -> (string)

The name of an Image Builder recipe that the lifecycle policy uses for resource selection.

semanticVersion -> (string)

The version of the Image Builder recipe specified by the `name` field.

tagMap -> (map)

A list of tags that are used as selection criteria for the Image Builder image resources that the lifecycle policy applies to.

key -> (string)

value -> (string)

dateCreated -> (timestamp)

The timestamp when Image Builder created the lifecycle policy resource.

dateUpdated -> (timestamp)

The timestamp when Image Builder updated the lifecycle policy resource.

dateLastRun -> (timestamp)

The timestamp for the last time Image Builder ran the lifecycle policy.

tags -> (map)

To help manage your lifecycle policy resources, you can assign your own metadata to each resource in the form of tags. Each tag consists of a key and an optional value, both of which you define.

key -> (string)

value -> (string)