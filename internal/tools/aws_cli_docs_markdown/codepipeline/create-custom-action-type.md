# create-custom-action-typeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/create-custom-action-type.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/create-custom-action-type.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codepipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/index.html#cli-aws-codepipeline) ]

# create-custom-action-type

## Description

Creates a new custom action that can be used in all pipelines associated with the Amazon Web Services account. Only used for custom actions.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/CreateCustomActionType)

## Synopsis

```
create-custom-action-type
--category <value>
--provider <value>
[--settings <value>]
[--configuration-properties <value>]
--input-artifact-details <value>
--output-artifact-details <value>
[--tags <value>]
--action-version <value>
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

`--category` (string)

The category of the custom action, such as a build action or a test action.

Possible values:

- `Source`
- `Build`
- `Deploy`
- `Test`
- `Invoke`
- `Approval`
- `Compute`

`--provider` (string)

The provider of the service used in the custom action, such as CodeDeploy.

`--settings` (structure)

URLs that provide users information about this custom action.

thirdPartyConfigurationUrl -> (string)

The URL of a sign-up page where users can sign up for an external service and perform initial configuration of the action provided by that service.

entityUrlTemplate -> (string)

The URL returned to the CodePipeline console that provides a deep link to the resources of the external system, such as the configuration page for a CodeDeploy deployment group. This link is provided as part of the action display in the pipeline.

executionUrlTemplate -> (string)

The URL returned to the CodePipeline console that contains a link to the top-level landing page for the external system, such as the console page for CodeDeploy. This link is shown on the pipeline view page in the CodePipeline console and provides a link to the execution entity of the external action.

revisionUrlTemplate -> (string)

The URL returned to the CodePipeline console that contains a link to the page where customers can update or change the configuration of the external action.

Shorthand Syntax:

```
thirdPartyConfigurationUrl=string,entityUrlTemplate=string,executionUrlTemplate=string,revisionUrlTemplate=string
```

JSON Syntax:

```
{
  "thirdPartyConfigurationUrl": "string",
  "entityUrlTemplate": "string",
  "executionUrlTemplate": "string",
  "revisionUrlTemplate": "string"
}
```

`--configuration-properties` (list)

The configuration properties for the custom action.

### Note

You can refer to a name in the configuration properties of the custom action within the URL templates by following the format of {Config:name}, as long as the configuration property is both required and not secret. For more information, see [Create a Custom Action for a Pipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/how-to-create-custom-action.html) .

(structure)

Represents information about an action configuration property.

name -> (string)

The name of the action configuration property.

required -> (boolean)

Whether the configuration property is a required value.

key -> (boolean)

Whether the configuration property is a key.

secret -> (boolean)

Whether the configuration property is secret. Secrets are hidden from all calls except for `GetJobDetails` , `GetThirdPartyJobDetails` , `PollForJobs` , and `PollForThirdPartyJobs` .

When updating a pipeline, passing * * * * * without changing any other values of the action preserves the previous value of the secret.

queryable -> (boolean)

Indicates that the property is used with `PollForJobs` . When creating a custom action, an action can have up to one queryable property. If it has one, that property must be both required and not secret.

If you create a pipeline with a custom action type, and that custom action contains a queryable property, the value for that configuration property is subject to other restrictions. The value must be less than or equal to twenty (20) characters. The value can contain only alphanumeric characters, underscores, and hyphens.

description -> (string)

The description of the action configuration property that is displayed to users.

type -> (string)

The type of the configuration property.

Shorthand Syntax:

```
name=string,required=boolean,key=boolean,secret=boolean,queryable=boolean,description=string,type=string ...
```

JSON Syntax:

```
[
  {
    "name": "string",
    "required": true|false,
    "key": true|false,
    "secret": true|false,
    "queryable": true|false,
    "description": "string",
    "type": "String"|"Number"|"Boolean"
  }
  ...
]
```

`--input-artifact-details` (structure)

The details of the input artifact for the action, such as its commit ID.

minimumCount -> (integer)

The minimum number of artifacts allowed for the action type.

maximumCount -> (integer)

The maximum number of artifacts allowed for the action type.

Shorthand Syntax:

```
minimumCount=integer,maximumCount=integer
```

JSON Syntax:

```
{
  "minimumCount": integer,
  "maximumCount": integer
}
```

`--output-artifact-details` (structure)

The details of the output artifact of the action, such as its commit ID.

minimumCount -> (integer)

The minimum number of artifacts allowed for the action type.

maximumCount -> (integer)

The maximum number of artifacts allowed for the action type.

Shorthand Syntax:

```
minimumCount=integer,maximumCount=integer
```

JSON Syntax:

```
{
  "minimumCount": integer,
  "maximumCount": integer
}
```

`--tags` (list)

The tags for the custom action.

(structure)

A tag is a key-value pair that is used to manage the resource.

key -> (string)

The tagâs key.

value -> (string)

The tagâs value.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
  }
  ...
]
```

`--action-version` (string)

The version identifier of the custom action.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a custom action**

This example creates a custom action for AWS CodePipeline using an already-created JSON file (here named MyCustomAction.json) that contains the structure of the custom action. For more information about the requirements for creating a custom action, including the structure of the file, see the AWS CodePipeline User Guide.

```
aws codepipeline create-custom-action-type --cli-input-json file://MyCustomAction.json
```

Contents of JSON file `MyCustomAction.json`:

```
{
    "category": "Build",
    "provider": "MyJenkinsProviderName",
    "version": "1",
    "settings": {
        "entityUrlTemplate": "https://192.0.2.4/job/{Config:ProjectName}/",
        "executionUrlTemplate": "https://192.0.2.4/job/{Config:ProjectName}/lastSuccessfulBuild/{ExternalExecutionId}/"
    },
    "configurationProperties": [
        {
            "name": "MyJenkinsExampleBuildProject",
            "required": true,
            "key": true,
            "secret": false,
            "queryable": false,
            "description": "The name of the build project must be provided when this action is added to the pipeline.",
            "type": "String"
        }
    ],
    "inputArtifactDetails": {
        "maximumCount": 1,
        "minimumCount": 0
    },
    "outputArtifactDetails": {
        "maximumCount": 1,
        "minimumCount": 0
    }
}
```

This command returns the structure of the custom action.

## Output

actionType -> (structure)

Returns information about the details of an action type.

id -> (structure)

Represents information about an action type.

category -> (string)

A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the following values.

- Source
- Build
- Test
- Deploy
- Invoke
- Approval
- Compute

owner -> (string)

The creator of the action being called. There are three valid values for the `Owner` field in the action category section within your pipeline structure: `AWS` , `ThirdParty` , and `Custom` . For more information, see [Valid Action Types and Providers in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers) .

provider -> (string)

The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of CodeDeploy, which would be specified as `CodeDeploy` . For more information, see [Valid Action Types and Providers in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers) .

version -> (string)

A string that describes the action version.

settings -> (structure)

The settings for the action type.

thirdPartyConfigurationUrl -> (string)

The URL of a sign-up page where users can sign up for an external service and perform initial configuration of the action provided by that service.

entityUrlTemplate -> (string)

The URL returned to the CodePipeline console that provides a deep link to the resources of the external system, such as the configuration page for a CodeDeploy deployment group. This link is provided as part of the action display in the pipeline.

executionUrlTemplate -> (string)

The URL returned to the CodePipeline console that contains a link to the top-level landing page for the external system, such as the console page for CodeDeploy. This link is shown on the pipeline view page in the CodePipeline console and provides a link to the execution entity of the external action.

revisionUrlTemplate -> (string)

The URL returned to the CodePipeline console that contains a link to the page where customers can update or change the configuration of the external action.

actionConfigurationProperties -> (list)

The configuration properties for the action type.

(structure)

Represents information about an action configuration property.

name -> (string)

The name of the action configuration property.

required -> (boolean)

Whether the configuration property is a required value.

key -> (boolean)

Whether the configuration property is a key.

secret -> (boolean)

Whether the configuration property is secret. Secrets are hidden from all calls except for `GetJobDetails` , `GetThirdPartyJobDetails` , `PollForJobs` , and `PollForThirdPartyJobs` .

When updating a pipeline, passing * * * * * without changing any other values of the action preserves the previous value of the secret.

queryable -> (boolean)

Indicates that the property is used with `PollForJobs` . When creating a custom action, an action can have up to one queryable property. If it has one, that property must be both required and not secret.

If you create a pipeline with a custom action type, and that custom action contains a queryable property, the value for that configuration property is subject to other restrictions. The value must be less than or equal to twenty (20) characters. The value can contain only alphanumeric characters, underscores, and hyphens.

description -> (string)

The description of the action configuration property that is displayed to users.

type -> (string)

The type of the configuration property.

inputArtifactDetails -> (structure)

The details of the input artifact for the action, such as its commit ID.

minimumCount -> (integer)

The minimum number of artifacts allowed for the action type.

maximumCount -> (integer)

The maximum number of artifacts allowed for the action type.

outputArtifactDetails -> (structure)

The details of the output artifact of the action, such as its commit ID.

minimumCount -> (integer)

The minimum number of artifacts allowed for the action type.

maximumCount -> (integer)

The maximum number of artifacts allowed for the action type.

tags -> (list)

Specifies the tags applied to the custom action.

(structure)

A tag is a key-value pair that is used to manage the resource.

key -> (string)

The tagâs key.

value -> (string)

The tagâs value.