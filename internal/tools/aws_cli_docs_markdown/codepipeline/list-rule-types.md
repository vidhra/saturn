# list-rule-typesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-rule-types.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-rule-types.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codepipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/index.html#cli-aws-codepipeline) ]

# list-rule-types

## Description

Lists the rules for the condition. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html) .For more information about rules, see the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/ListRuleTypes)

## Synopsis

```
list-rule-types
[--rule-owner-filter <value>]
[--region-filter <value>]
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

`--rule-owner-filter` (string)

The rule owner to filter on.

Possible values:

- `AWS`

`--region-filter` (string)

The rule Region to filter on.

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

ruleTypes -> (list)

Lists the rules that are configured for the condition.

(structure)

The rule type, which is made up of the combined values for category, owner, provider, and version.

id -> (structure)

Represents information about a rule type.

category -> (string)

A category defines what kind of rule can be run in the stage, and constrains the provider type for the rule. The valid category is `Rule` .

owner -> (string)

The creator of the rule being called. The valid value for the `Owner` field in the rule category is `AWS` .

provider -> (string)

The rule provider, such as the `DeploymentWindow` rule. For a list of rule provider names, see the rules listed in the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

version -> (string)

A string that describes the rule version.

settings -> (structure)

Returns information about the settings for a rule type.

thirdPartyConfigurationUrl -> (string)

The URL of a sign-up page where users can sign up for an external service and perform initial configuration of the action provided by that service.

entityUrlTemplate -> (string)

The URL returned to the CodePipeline console that provides a deep link to the resources of the external system, such as the configuration page for a CodeDeploy deployment group. This link is provided as part of the action display in the pipeline.

executionUrlTemplate -> (string)

The URL returned to the CodePipeline console that contains a link to the top-level landing page for the external system, such as the console page for CodeDeploy. This link is shown on the pipeline view page in the CodePipeline console and provides a link to the execution entity of the external action.

revisionUrlTemplate -> (string)

The URL returned to the CodePipeline console that contains a link to the page where customers can update or change the configuration of the external action.

ruleConfigurationProperties -> (list)

The configuration properties for the rule type.

(structure)

Represents information about a rule configuration property.

name -> (string)

The name of the rule configuration property.

required -> (boolean)

Whether the configuration property is a required value.

key -> (boolean)

Whether the configuration property is a key.

secret -> (boolean)

Whether the configuration property is secret.

When updating a pipeline, passing * * * * * without changing any other values of the action preserves the previous value of the secret.

queryable -> (boolean)

Indicates whether the property can be queried.

If you create a pipeline with a condition and rule, and that rule contains a queryable property, the value for that configuration property is subject to other restrictions. The value must be less than or equal to twenty (20) characters. The value can contain only alphanumeric characters, underscores, and hyphens.

description -> (string)

The description of the action configuration property that is displayed to users.

type -> (string)

The type of the configuration property.

inputArtifactDetails -> (structure)

Returns information about the details of an artifact.

minimumCount -> (integer)

The minimum number of artifacts allowed for the action type.

maximumCount -> (integer)

The maximum number of artifacts allowed for the action type.