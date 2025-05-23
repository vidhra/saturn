# create-pipelineÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/create-pipeline.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/create-pipeline.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codepipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/index.html#cli-aws-codepipeline) ]

# create-pipeline

## Description

Creates a pipeline.

### Note

In the pipeline structure, you must include either `artifactStore` or `artifactStores` in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use `artifactStores` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/CreatePipeline)

## Synopsis

```
create-pipeline
--pipeline <value>
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

`--pipeline` (structure)

Represents the structure of actions and stages to be performed in the pipeline.

name -> (string)

The name of the pipeline.

roleArn -> (string)

The Amazon Resource Name (ARN) for CodePipeline to use to either perform actions with no `actionRoleArn` , or to use to assume roles for actions with an `actionRoleArn` .

artifactStore -> (structure)

Represents information about the S3 bucket where artifacts are stored for the pipeline.

### Note

You must include either `artifactStore` or `artifactStores` in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use `artifactStores` .

type -> (string)

The type of the artifact store, such as S3.

location -> (string)

The S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any S3 bucket in the same Amazon Web Services Region as the pipeline to store your pipeline artifacts.

encryptionKey -> (structure)

The encryption key used to encrypt the data in the artifact store, such as an Amazon Web Services Key Management Service key. If this is undefined, the default key for Amazon S3 is used.

id -> (string)

The ID used to identify the key. For an Amazon Web Services KMS key, you can use the key ID, the key ARN, or the alias ARN.

### Note

Aliases are recognized only in the account that created the KMS key. For cross-account actions, you can only use the key ID or key ARN to identify the key. Cross-account actions involve using the role from the other account (AccountB), so specifying the key ID will use the key from the other account (AccountB).

type -> (string)

The type of encryption key, such as an Amazon Web Services KMS key. When creating or updating a pipeline, the value must be set to âKMSâ.

artifactStores -> (map)

A mapping of `artifactStore` objects and their corresponding Amazon Web Services Regions. There must be an artifact store for the pipeline Region and for each cross-region action in the pipeline.

### Note

You must include either `artifactStore` or `artifactStores` in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use `artifactStores` .

key -> (string)

value -> (structure)

The S3 bucket where artifacts for the pipeline are stored.

### Note

You must include either `artifactStore` or `artifactStores` in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use `artifactStores` .

type -> (string)

The type of the artifact store, such as S3.

location -> (string)

The S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any S3 bucket in the same Amazon Web Services Region as the pipeline to store your pipeline artifacts.

encryptionKey -> (structure)

The encryption key used to encrypt the data in the artifact store, such as an Amazon Web Services Key Management Service key. If this is undefined, the default key for Amazon S3 is used.

id -> (string)

The ID used to identify the key. For an Amazon Web Services KMS key, you can use the key ID, the key ARN, or the alias ARN.

### Note

Aliases are recognized only in the account that created the KMS key. For cross-account actions, you can only use the key ID or key ARN to identify the key. Cross-account actions involve using the role from the other account (AccountB), so specifying the key ID will use the key from the other account (AccountB).

type -> (string)

The type of encryption key, such as an Amazon Web Services KMS key. When creating or updating a pipeline, the value must be set to âKMSâ.

stages -> (list)

The stage in which to perform the action.

(structure)

Represents information about a stage and its definition.

name -> (string)

The name of the stage.

blockers -> (list)

Reserved for future use.

(structure)

Reserved for future use.

name -> (string)

Reserved for future use.

type -> (string)

Reserved for future use.

actions -> (list)

The actions included in a stage.

(structure)

Represents information about an action declaration.

name -> (string)

The action declarationâs name.

actionTypeId -> (structure)

Specifies the action type and the provider of the action.

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

runOrder -> (integer)

The order in which actions are run.

configuration -> (map)

The actionâs configuration. These are key-value pairs that specify input values for an action. For more information, see [Action Structure Requirements in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements) . For the list of configuration properties for the CloudFormation action type in CodePipeline, see [Configuration Properties Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html) in the *CloudFormation User Guide* . For template snippets with examples, see [Using Parameter Override Functions with CodePipeline Pipelines](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html) in the *CloudFormation User Guide* .

The values can be represented in either JSON or YAML format. For example, the JSON configuration item format is as follows:

*JSON:*

`"Configuration" : { Key : Value },`

key -> (string)

value -> (string)

commands -> (list)

The shell commands to run with your compute action in CodePipeline. All commands are supported except multi-line formats. While CodeBuild logs and permissions are used, you do not need to create any resources in CodeBuild.

### Note

Using compute time for this action will incur separate charges in CodeBuild.

(string)

outputArtifacts -> (list)

The name or ID of the result of the action declaration, such as a test or build artifact.

(structure)

Represents information about the output of an action.

name -> (string)

The name of the output of an artifact, such as âMy Appâ.

The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.

Output artifact names must be unique within a pipeline.

files -> (list)

The files that you want to associate with the output artifact that will be exported from the compute action.

(string)

inputArtifacts -> (list)

The name or ID of the artifact consumed by the action, such as a test or build artifact.

(structure)

Represents information about an artifact to be worked on, such as a test or build artifact.

name -> (string)

The name of the artifact to be worked on (for example, âMy Appâ).

Artifacts are the files that are worked on by actions in the pipeline. See the action configuration for each action for details about artifact parameters. For example, the S3 source action input artifact is a file name (or file path), and the files are generally provided as a ZIP file. Example artifact name: SampleApp_Windows.zip

The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.

outputVariables -> (list)

The list of variables that are to be exported from the compute action. This is specifically CodeBuild environment variables as used for that action.

(string)

roleArn -> (string)

The ARN of the IAM service role that performs the declared action. This is assumed through the roleArn for the pipeline.

region -> (string)

The action declarationâs Amazon Web Services Region, such as us-east-1.

namespace -> (string)

The variable namespace associated with the action. All variables produced as output by this action fall under this namespace.

timeoutInMinutes -> (integer)

A timeout duration in minutes that can be applied against the ActionTypeâs default timeout value specified in [Quotas for CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/limits.html) . This attribute is available only to the manual approval ActionType.

environmentVariables -> (list)

The environment variables for the action.

(structure)

The environment variables for the action.

name -> (string)

The environment variable name in the key-value pair.

value -> (string)

The environment variable value in the key-value pair.

type -> (string)

Specifies the type of use for the environment variable value. The value can be either `PLAINTEXT` or `SECRETS_MANAGER` . If the value is `SECRETS_MANAGER` , provide the Secrets reference in the EnvironmentVariable value.

onFailure -> (structure)

The method to use when a stage has not completed successfully. For example, configuring this field for rollback will roll back a failed stage automatically to the last successful pipeline execution in the stage.

result -> (string)

The specified result for when the failure conditions are met, such as rolling back the stage.

retryConfiguration -> (structure)

The retry configuration specifies automatic retry for a failed stage, along with the configured retry mode.

retryMode -> (string)

The method that you want to configure for automatic stage retry on stage failure. You can specify to retry only failed action in the stage or all actions in the stage.

conditions -> (list)

The conditions that are configured as failure conditions. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html) .

(structure)

The condition for the stage. A condition is made up of the rules and the result for the condition. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html) .. For more information about rules, see the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

result -> (string)

The action to be done when the condition is met. For example, rolling back an execution for a failure condition.

rules -> (list)

The rules that make up the condition.

(structure)

Represents information about the rule to be created for an associated condition. An example would be creating a new rule for an entry condition, such as a rule that checks for a test result before allowing the run to enter the deployment stage. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html) . For more information about rules, see the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

name -> (string)

The name of the rule that is created for the condition, such as `VariableCheck` .

ruleTypeId -> (structure)

The ID for the rule type, which is made up of the combined values for category, owner, provider, and version.

category -> (string)

A category defines what kind of rule can be run in the stage, and constrains the provider type for the rule. The valid category is `Rule` .

owner -> (string)

The creator of the rule being called. The valid value for the `Owner` field in the rule category is `AWS` .

provider -> (string)

The rule provider, such as the `DeploymentWindow` rule. For a list of rule provider names, see the rules listed in the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

version -> (string)

A string that describes the rule version.

configuration -> (map)

The action configuration fields for the rule.

key -> (string)

value -> (string)

commands -> (list)

The shell commands to run with your commands rule in CodePipeline. All commands are supported except multi-line formats. While CodeBuild logs and permissions are used, you do not need to create any resources in CodeBuild.

### Note

Using compute time for this action will incur separate charges in CodeBuild.

(string)

inputArtifacts -> (list)

The input artifacts fields for the rule, such as specifying an input file for the rule.

(structure)

Represents information about an artifact to be worked on, such as a test or build artifact.

name -> (string)

The name of the artifact to be worked on (for example, âMy Appâ).

Artifacts are the files that are worked on by actions in the pipeline. See the action configuration for each action for details about artifact parameters. For example, the S3 source action input artifact is a file name (or file path), and the files are generally provided as a ZIP file. Example artifact name: SampleApp_Windows.zip

The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.

roleArn -> (string)

The pipeline role ARN associated with the rule.

region -> (string)

The Region for the condition associated with the rule.

timeoutInMinutes -> (integer)

The action timeout for the rule.

onSuccess -> (structure)

The method to use when a stage has succeeded. For example, configuring this field for conditions will allow the stage to succeed when the conditions are met.

conditions -> (list)

The conditions that are success conditions.

(structure)

The condition for the stage. A condition is made up of the rules and the result for the condition. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html) .. For more information about rules, see the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

result -> (string)

The action to be done when the condition is met. For example, rolling back an execution for a failure condition.

rules -> (list)

The rules that make up the condition.

(structure)

Represents information about the rule to be created for an associated condition. An example would be creating a new rule for an entry condition, such as a rule that checks for a test result before allowing the run to enter the deployment stage. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html) . For more information about rules, see the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

name -> (string)

The name of the rule that is created for the condition, such as `VariableCheck` .

ruleTypeId -> (structure)

The ID for the rule type, which is made up of the combined values for category, owner, provider, and version.

category -> (string)

A category defines what kind of rule can be run in the stage, and constrains the provider type for the rule. The valid category is `Rule` .

owner -> (string)

The creator of the rule being called. The valid value for the `Owner` field in the rule category is `AWS` .

provider -> (string)

The rule provider, such as the `DeploymentWindow` rule. For a list of rule provider names, see the rules listed in the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

version -> (string)

A string that describes the rule version.

configuration -> (map)

The action configuration fields for the rule.

key -> (string)

value -> (string)

commands -> (list)

The shell commands to run with your commands rule in CodePipeline. All commands are supported except multi-line formats. While CodeBuild logs and permissions are used, you do not need to create any resources in CodeBuild.

### Note

Using compute time for this action will incur separate charges in CodeBuild.

(string)

inputArtifacts -> (list)

The input artifacts fields for the rule, such as specifying an input file for the rule.

(structure)

Represents information about an artifact to be worked on, such as a test or build artifact.

name -> (string)

The name of the artifact to be worked on (for example, âMy Appâ).

Artifacts are the files that are worked on by actions in the pipeline. See the action configuration for each action for details about artifact parameters. For example, the S3 source action input artifact is a file name (or file path), and the files are generally provided as a ZIP file. Example artifact name: SampleApp_Windows.zip

The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.

roleArn -> (string)

The pipeline role ARN associated with the rule.

region -> (string)

The Region for the condition associated with the rule.

timeoutInMinutes -> (integer)

The action timeout for the rule.

beforeEntry -> (structure)

The method to use when a stage allows entry. For example, configuring this field for conditions will allow entry to the stage when the conditions are met.

conditions -> (list)

The conditions that are configured as entry conditions.

(structure)

The condition for the stage. A condition is made up of the rules and the result for the condition. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html) .. For more information about rules, see the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

result -> (string)

The action to be done when the condition is met. For example, rolling back an execution for a failure condition.

rules -> (list)

The rules that make up the condition.

(structure)

Represents information about the rule to be created for an associated condition. An example would be creating a new rule for an entry condition, such as a rule that checks for a test result before allowing the run to enter the deployment stage. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html) . For more information about rules, see the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

name -> (string)

The name of the rule that is created for the condition, such as `VariableCheck` .

ruleTypeId -> (structure)

The ID for the rule type, which is made up of the combined values for category, owner, provider, and version.

category -> (string)

A category defines what kind of rule can be run in the stage, and constrains the provider type for the rule. The valid category is `Rule` .

owner -> (string)

The creator of the rule being called. The valid value for the `Owner` field in the rule category is `AWS` .

provider -> (string)

The rule provider, such as the `DeploymentWindow` rule. For a list of rule provider names, see the rules listed in the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

version -> (string)

A string that describes the rule version.

configuration -> (map)

The action configuration fields for the rule.

key -> (string)

value -> (string)

commands -> (list)

The shell commands to run with your commands rule in CodePipeline. All commands are supported except multi-line formats. While CodeBuild logs and permissions are used, you do not need to create any resources in CodeBuild.

### Note

Using compute time for this action will incur separate charges in CodeBuild.

(string)

inputArtifacts -> (list)

The input artifacts fields for the rule, such as specifying an input file for the rule.

(structure)

Represents information about an artifact to be worked on, such as a test or build artifact.

name -> (string)

The name of the artifact to be worked on (for example, âMy Appâ).

Artifacts are the files that are worked on by actions in the pipeline. See the action configuration for each action for details about artifact parameters. For example, the S3 source action input artifact is a file name (or file path), and the files are generally provided as a ZIP file. Example artifact name: SampleApp_Windows.zip

The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.

roleArn -> (string)

The pipeline role ARN associated with the rule.

region -> (string)

The Region for the condition associated with the rule.

timeoutInMinutes -> (integer)

The action timeout for the rule.

version -> (integer)

The version number of the pipeline. A new pipeline always has a version number of 1. This number is incremented when a pipeline is updated.

executionMode -> (string)

The method that the pipeline will use to handle multiple executions. The default mode is SUPERSEDED.

pipelineType -> (string)

CodePipeline provides the following pipeline types, which differ in characteristics and price, so that you can tailor your pipeline features and cost to the needs of your applications.

- V1 type pipelines have a JSON structure that contains standard pipeline, stage, and action-level parameters.
- V2 type pipelines have the same structure as a V1 type, along with additional parameters for release safety and trigger configuration.

### Warning

Including V2 parameters, such as triggers on Git tags, in the pipeline JSON when creating or updating a pipeline will result in the pipeline having the V2 type of pipeline and the associated costs.

For information about pricing for CodePipeline, see [Pricing](http://aws.amazon.com/codepipeline/pricing/) .

For information about which type of pipeline to choose, see [What type of pipeline is right for me?](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-types-planning.html) .

variables -> (list)

A list that defines the pipeline variables for a pipeline resource. Variable names can have alphanumeric and underscore characters, and the values must match `[A-Za-z0-9@\-_]+` .

(structure)

A variable declared at the pipeline level.

name -> (string)

The name of a pipeline-level variable.

defaultValue -> (string)

The value of a pipeline-level variable.

description -> (string)

The description of a pipeline-level variable. Itâs used to add additional context about the variable, and not being used at time when pipeline executes.

triggers -> (list)

The trigger configuration specifying a type of event, such as Git tags, that starts the pipeline.

### Note

When a trigger configuration is specified, default change detection for repository and branch commits is disabled.

(structure)

Represents information about the specified trigger configuration, such as the filter criteria and the source stage for the action that contains the trigger.

### Note

This is only supported for the `CodeStarSourceConnection` action type.

### Note

When a trigger configuration is specified, default change detection for repository and branch commits is disabled.

providerType -> (string)

The source provider for the event, such as connections configured for a repository with Git tags, for the specified trigger configuration.

gitConfiguration -> (structure)

Provides the filter criteria and the source stage for the repository event that starts the pipeline, such as Git tags.

sourceActionName -> (string)

The name of the pipeline source action where the trigger configuration, such as Git tags, is specified. The trigger configuration will start the pipeline upon the specified change only.

### Note

You can only specify one trigger configuration per source action.

push -> (list)

The field where the repository event that will start the pipeline, such as pushing Git tags, is specified with details.

(structure)

The event criteria that specify when a specified repository event will start the pipeline for the specified trigger configuration, such as the lists of Git tags to include and exclude.

tags -> (structure)

The field that contains the details for the Git tags trigger configuration.

includes -> (list)

The list of patterns of Git tags that, when pushed, are to be included as criteria that starts the pipeline.

(string)

excludes -> (list)

The list of patterns of Git tags that, when pushed, are to be excluded from starting the pipeline.

(string)

branches -> (structure)

The field that specifies to filter on branches for the push trigger configuration.

includes -> (list)

The list of patterns of Git branches that, when a commit is pushed, are to be included as criteria that starts the pipeline.

(string)

excludes -> (list)

The list of patterns of Git branches that, when a commit is pushed, are to be excluded from starting the pipeline.

(string)

filePaths -> (structure)

The field that specifies to filter on file paths for the push trigger configuration.

includes -> (list)

The list of patterns of Git repository file paths that, when a commit is pushed, are to be included as criteria that starts the pipeline.

(string)

excludes -> (list)

The list of patterns of Git repository file paths that, when a commit is pushed, are to be excluded from starting the pipeline.

(string)

pullRequest -> (list)

The field where the repository event that will start the pipeline is specified as pull requests.

(structure)

The event criteria for the pull request trigger configuration, such as the lists of branches or file paths to include and exclude.

The following are valid values for the events for this filter:

- CLOSED
- OPEN
- UPDATED

events -> (list)

The field that specifies which pull request events to filter on (OPEN, UPDATED, CLOSED) for the trigger configuration.

(string)

branches -> (structure)

The field that specifies to filter on branches for the pull request trigger configuration.

includes -> (list)

The list of patterns of Git branches that, when a commit is pushed, are to be included as criteria that starts the pipeline.

(string)

excludes -> (list)

The list of patterns of Git branches that, when a commit is pushed, are to be excluded from starting the pipeline.

(string)

filePaths -> (structure)

The field that specifies to filter on file paths for the pull request trigger configuration.

includes -> (list)

The list of patterns of Git repository file paths that, when a commit is pushed, are to be included as criteria that starts the pipeline.

(string)

excludes -> (list)

The list of patterns of Git repository file paths that, when a commit is pushed, are to be excluded from starting the pipeline.

(string)

JSON Syntax:

```
{
  "name": "string",
  "roleArn": "string",
  "artifactStore": {
    "type": "S3",
    "location": "string",
    "encryptionKey": {
      "id": "string",
      "type": "KMS"
    }
  },
  "artifactStores": {"string": {
        "type": "S3",
        "location": "string",
        "encryptionKey": {
          "id": "string",
          "type": "KMS"
        }
      }
    ...},
  "stages": [
    {
      "name": "string",
      "blockers": [
        {
          "name": "string",
          "type": "Schedule"
        }
        ...
      ],
      "actions": [
        {
          "name": "string",
          "actionTypeId": {
            "category": "Source"|"Build"|"Deploy"|"Test"|"Invoke"|"Approval"|"Compute",
            "owner": "AWS"|"ThirdParty"|"Custom",
            "provider": "string",
            "version": "string"
          },
          "runOrder": integer,
          "configuration": {"string": "string"
            ...},
          "commands": ["string", ...],
          "outputArtifacts": [
            {
              "name": "string",
              "files": ["string", ...]
            }
            ...
          ],
          "inputArtifacts": [
            {
              "name": "string"
            }
            ...
          ],
          "outputVariables": ["string", ...],
          "roleArn": "string",
          "region": "string",
          "namespace": "string",
          "timeoutInMinutes": integer,
          "environmentVariables": [
            {
              "name": "string",
              "value": "string",
              "type": "PLAINTEXT"|"SECRETS_MANAGER"
            }
            ...
          ]
        }
        ...
      ],
      "onFailure": {
        "result": "ROLLBACK"|"FAIL"|"RETRY"|"SKIP",
        "retryConfiguration": {
          "retryMode": "FAILED_ACTIONS"|"ALL_ACTIONS"
        },
        "conditions": [
          {
            "result": "ROLLBACK"|"FAIL"|"RETRY"|"SKIP",
            "rules": [
              {
                "name": "string",
                "ruleTypeId": {
                  "category": "Rule",
                  "owner": "AWS",
                  "provider": "string",
                  "version": "string"
                },
                "configuration": {"string": "string"
                  ...},
                "commands": ["string", ...],
                "inputArtifacts": [
                  {
                    "name": "string"
                  }
                  ...
                ],
                "roleArn": "string",
                "region": "string",
                "timeoutInMinutes": integer
              }
              ...
            ]
          }
          ...
        ]
      },
      "onSuccess": {
        "conditions": [
          {
            "result": "ROLLBACK"|"FAIL"|"RETRY"|"SKIP",
            "rules": [
              {
                "name": "string",
                "ruleTypeId": {
                  "category": "Rule",
                  "owner": "AWS",
                  "provider": "string",
                  "version": "string"
                },
                "configuration": {"string": "string"
                  ...},
                "commands": ["string", ...],
                "inputArtifacts": [
                  {
                    "name": "string"
                  }
                  ...
                ],
                "roleArn": "string",
                "region": "string",
                "timeoutInMinutes": integer
              }
              ...
            ]
          }
          ...
        ]
      },
      "beforeEntry": {
        "conditions": [
          {
            "result": "ROLLBACK"|"FAIL"|"RETRY"|"SKIP",
            "rules": [
              {
                "name": "string",
                "ruleTypeId": {
                  "category": "Rule",
                  "owner": "AWS",
                  "provider": "string",
                  "version": "string"
                },
                "configuration": {"string": "string"
                  ...},
                "commands": ["string", ...],
                "inputArtifacts": [
                  {
                    "name": "string"
                  }
                  ...
                ],
                "roleArn": "string",
                "region": "string",
                "timeoutInMinutes": integer
              }
              ...
            ]
          }
          ...
        ]
      }
    }
    ...
  ],
  "version": integer,
  "executionMode": "QUEUED"|"SUPERSEDED"|"PARALLEL",
  "pipelineType": "V1"|"V2",
  "variables": [
    {
      "name": "string",
      "defaultValue": "string",
      "description": "string"
    }
    ...
  ],
  "triggers": [
    {
      "providerType": "CodeStarSourceConnection",
      "gitConfiguration": {
        "sourceActionName": "string",
        "push": [
          {
            "tags": {
              "includes": ["string", ...],
              "excludes": ["string", ...]
            },
            "branches": {
              "includes": ["string", ...],
              "excludes": ["string", ...]
            },
            "filePaths": {
              "includes": ["string", ...],
              "excludes": ["string", ...]
            }
          }
          ...
        ],
        "pullRequest": [
          {
            "events": ["OPEN"|"UPDATED"|"CLOSED", ...],
            "branches": {
              "includes": ["string", ...],
              "excludes": ["string", ...]
            },
            "filePaths": {
              "includes": ["string", ...],
              "excludes": ["string", ...]
            }
          }
          ...
        ]
      }
    }
    ...
  ]
}
```

`--tags` (list)

The tags for the pipeline.

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

**To create a pipeline**

This example creates a pipeline in AWS CodePipeline using an already-created JSON file (here named MySecondPipeline.json) that contains the structure of the pipeline. For more information about the requirements for creating a pipeline, including the structure of the file, see the AWS CodePipeline User Guide.

Command:

```
aws codepipeline create-pipeline --cli-input-json file://MySecondPipeline.json
```

JSON file sample contents:

```
{
 "pipeline": {
  "roleArn": "arn:aws:iam::111111111111:role/AWS-CodePipeline-Service",
  "stages": [
    {
      "name": "Source",
      "actions": [
        {
          "inputArtifacts": [],
          "name": "Source",
          "actionTypeId": {
            "category": "Source",
            "owner": "AWS",
            "version": "1",
            "provider": "S3"
          },
          "outputArtifacts": [
            {
              "name": "MyApp"
            }
          ],
          "configuration": {
            "S3Bucket": "awscodepipeline-demo-bucket",
            "S3ObjectKey": "aws-codepipeline-s3-aws-codedeploy_linux.zip"
          },
          "runOrder": 1
        }
      ]
    },
    {
      "name": "Beta",
      "actions": [
        {
          "inputArtifacts": [
            {
              "name": "MyApp"
            }
          ],
          "name": "CodePipelineDemoFleet",
          "actionTypeId": {
            "category": "Deploy",
            "owner": "AWS",
            "version": "1",
            "provider": "CodeDeploy"
          },
          "outputArtifacts": [],
          "configuration": {
            "ApplicationName": "CodePipelineDemoApplication",
            "DeploymentGroupName": "CodePipelineDemoFleet"
          },
          "runOrder": 1
        }
      ]
    }
  ],
  "artifactStore": {
    "type": "S3",
    "location": "codepipeline-us-east-1-11EXAMPLE11"
  },
  "name": "MySecondPipeline",
  "version": 1
 }
}
```

Output:

```
This command returns the structure of the pipeline.
```

## Output

pipeline -> (structure)

Represents the structure of actions and stages to be performed in the pipeline.

name -> (string)

The name of the pipeline.

roleArn -> (string)

The Amazon Resource Name (ARN) for CodePipeline to use to either perform actions with no `actionRoleArn` , or to use to assume roles for actions with an `actionRoleArn` .

artifactStore -> (structure)

Represents information about the S3 bucket where artifacts are stored for the pipeline.

### Note

You must include either `artifactStore` or `artifactStores` in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use `artifactStores` .

type -> (string)

The type of the artifact store, such as S3.

location -> (string)

The S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any S3 bucket in the same Amazon Web Services Region as the pipeline to store your pipeline artifacts.

encryptionKey -> (structure)

The encryption key used to encrypt the data in the artifact store, such as an Amazon Web Services Key Management Service key. If this is undefined, the default key for Amazon S3 is used.

id -> (string)

The ID used to identify the key. For an Amazon Web Services KMS key, you can use the key ID, the key ARN, or the alias ARN.

### Note

Aliases are recognized only in the account that created the KMS key. For cross-account actions, you can only use the key ID or key ARN to identify the key. Cross-account actions involve using the role from the other account (AccountB), so specifying the key ID will use the key from the other account (AccountB).

type -> (string)

The type of encryption key, such as an Amazon Web Services KMS key. When creating or updating a pipeline, the value must be set to âKMSâ.

artifactStores -> (map)

A mapping of `artifactStore` objects and their corresponding Amazon Web Services Regions. There must be an artifact store for the pipeline Region and for each cross-region action in the pipeline.

### Note

You must include either `artifactStore` or `artifactStores` in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use `artifactStores` .

key -> (string)

value -> (structure)

The S3 bucket where artifacts for the pipeline are stored.

### Note

You must include either `artifactStore` or `artifactStores` in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use `artifactStores` .

type -> (string)

The type of the artifact store, such as S3.

location -> (string)

The S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any S3 bucket in the same Amazon Web Services Region as the pipeline to store your pipeline artifacts.

encryptionKey -> (structure)

The encryption key used to encrypt the data in the artifact store, such as an Amazon Web Services Key Management Service key. If this is undefined, the default key for Amazon S3 is used.

id -> (string)

The ID used to identify the key. For an Amazon Web Services KMS key, you can use the key ID, the key ARN, or the alias ARN.

### Note

Aliases are recognized only in the account that created the KMS key. For cross-account actions, you can only use the key ID or key ARN to identify the key. Cross-account actions involve using the role from the other account (AccountB), so specifying the key ID will use the key from the other account (AccountB).

type -> (string)

The type of encryption key, such as an Amazon Web Services KMS key. When creating or updating a pipeline, the value must be set to âKMSâ.

stages -> (list)

The stage in which to perform the action.

(structure)

Represents information about a stage and its definition.

name -> (string)

The name of the stage.

blockers -> (list)

Reserved for future use.

(structure)

Reserved for future use.

name -> (string)

Reserved for future use.

type -> (string)

Reserved for future use.

actions -> (list)

The actions included in a stage.

(structure)

Represents information about an action declaration.

name -> (string)

The action declarationâs name.

actionTypeId -> (structure)

Specifies the action type and the provider of the action.

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

runOrder -> (integer)

The order in which actions are run.

configuration -> (map)

The actionâs configuration. These are key-value pairs that specify input values for an action. For more information, see [Action Structure Requirements in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements) . For the list of configuration properties for the CloudFormation action type in CodePipeline, see [Configuration Properties Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html) in the *CloudFormation User Guide* . For template snippets with examples, see [Using Parameter Override Functions with CodePipeline Pipelines](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html) in the *CloudFormation User Guide* .

The values can be represented in either JSON or YAML format. For example, the JSON configuration item format is as follows:

*JSON:*

`"Configuration" : { Key : Value },`

key -> (string)

value -> (string)

commands -> (list)

The shell commands to run with your compute action in CodePipeline. All commands are supported except multi-line formats. While CodeBuild logs and permissions are used, you do not need to create any resources in CodeBuild.

### Note

Using compute time for this action will incur separate charges in CodeBuild.

(string)

outputArtifacts -> (list)

The name or ID of the result of the action declaration, such as a test or build artifact.

(structure)

Represents information about the output of an action.

name -> (string)

The name of the output of an artifact, such as âMy Appâ.

The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.

Output artifact names must be unique within a pipeline.

files -> (list)

The files that you want to associate with the output artifact that will be exported from the compute action.

(string)

inputArtifacts -> (list)

The name or ID of the artifact consumed by the action, such as a test or build artifact.

(structure)

Represents information about an artifact to be worked on, such as a test or build artifact.

name -> (string)

The name of the artifact to be worked on (for example, âMy Appâ).

Artifacts are the files that are worked on by actions in the pipeline. See the action configuration for each action for details about artifact parameters. For example, the S3 source action input artifact is a file name (or file path), and the files are generally provided as a ZIP file. Example artifact name: SampleApp_Windows.zip

The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.

outputVariables -> (list)

The list of variables that are to be exported from the compute action. This is specifically CodeBuild environment variables as used for that action.

(string)

roleArn -> (string)

The ARN of the IAM service role that performs the declared action. This is assumed through the roleArn for the pipeline.

region -> (string)

The action declarationâs Amazon Web Services Region, such as us-east-1.

namespace -> (string)

The variable namespace associated with the action. All variables produced as output by this action fall under this namespace.

timeoutInMinutes -> (integer)

A timeout duration in minutes that can be applied against the ActionTypeâs default timeout value specified in [Quotas for CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/limits.html) . This attribute is available only to the manual approval ActionType.

environmentVariables -> (list)

The environment variables for the action.

(structure)

The environment variables for the action.

name -> (string)

The environment variable name in the key-value pair.

value -> (string)

The environment variable value in the key-value pair.

type -> (string)

Specifies the type of use for the environment variable value. The value can be either `PLAINTEXT` or `SECRETS_MANAGER` . If the value is `SECRETS_MANAGER` , provide the Secrets reference in the EnvironmentVariable value.

onFailure -> (structure)

The method to use when a stage has not completed successfully. For example, configuring this field for rollback will roll back a failed stage automatically to the last successful pipeline execution in the stage.

result -> (string)

The specified result for when the failure conditions are met, such as rolling back the stage.

retryConfiguration -> (structure)

The retry configuration specifies automatic retry for a failed stage, along with the configured retry mode.

retryMode -> (string)

The method that you want to configure for automatic stage retry on stage failure. You can specify to retry only failed action in the stage or all actions in the stage.

conditions -> (list)

The conditions that are configured as failure conditions. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html) .

(structure)

The condition for the stage. A condition is made up of the rules and the result for the condition. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html) .. For more information about rules, see the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

result -> (string)

The action to be done when the condition is met. For example, rolling back an execution for a failure condition.

rules -> (list)

The rules that make up the condition.

(structure)

Represents information about the rule to be created for an associated condition. An example would be creating a new rule for an entry condition, such as a rule that checks for a test result before allowing the run to enter the deployment stage. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html) . For more information about rules, see the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

name -> (string)

The name of the rule that is created for the condition, such as `VariableCheck` .

ruleTypeId -> (structure)

The ID for the rule type, which is made up of the combined values for category, owner, provider, and version.

category -> (string)

A category defines what kind of rule can be run in the stage, and constrains the provider type for the rule. The valid category is `Rule` .

owner -> (string)

The creator of the rule being called. The valid value for the `Owner` field in the rule category is `AWS` .

provider -> (string)

The rule provider, such as the `DeploymentWindow` rule. For a list of rule provider names, see the rules listed in the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

version -> (string)

A string that describes the rule version.

configuration -> (map)

The action configuration fields for the rule.

key -> (string)

value -> (string)

commands -> (list)

The shell commands to run with your commands rule in CodePipeline. All commands are supported except multi-line formats. While CodeBuild logs and permissions are used, you do not need to create any resources in CodeBuild.

### Note

Using compute time for this action will incur separate charges in CodeBuild.

(string)

inputArtifacts -> (list)

The input artifacts fields for the rule, such as specifying an input file for the rule.

(structure)

Represents information about an artifact to be worked on, such as a test or build artifact.

name -> (string)

The name of the artifact to be worked on (for example, âMy Appâ).

Artifacts are the files that are worked on by actions in the pipeline. See the action configuration for each action for details about artifact parameters. For example, the S3 source action input artifact is a file name (or file path), and the files are generally provided as a ZIP file. Example artifact name: SampleApp_Windows.zip

The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.

roleArn -> (string)

The pipeline role ARN associated with the rule.

region -> (string)

The Region for the condition associated with the rule.

timeoutInMinutes -> (integer)

The action timeout for the rule.

onSuccess -> (structure)

The method to use when a stage has succeeded. For example, configuring this field for conditions will allow the stage to succeed when the conditions are met.

conditions -> (list)

The conditions that are success conditions.

(structure)

The condition for the stage. A condition is made up of the rules and the result for the condition. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html) .. For more information about rules, see the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

result -> (string)

The action to be done when the condition is met. For example, rolling back an execution for a failure condition.

rules -> (list)

The rules that make up the condition.

(structure)

Represents information about the rule to be created for an associated condition. An example would be creating a new rule for an entry condition, such as a rule that checks for a test result before allowing the run to enter the deployment stage. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html) . For more information about rules, see the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

name -> (string)

The name of the rule that is created for the condition, such as `VariableCheck` .

ruleTypeId -> (structure)

The ID for the rule type, which is made up of the combined values for category, owner, provider, and version.

category -> (string)

A category defines what kind of rule can be run in the stage, and constrains the provider type for the rule. The valid category is `Rule` .

owner -> (string)

The creator of the rule being called. The valid value for the `Owner` field in the rule category is `AWS` .

provider -> (string)

The rule provider, such as the `DeploymentWindow` rule. For a list of rule provider names, see the rules listed in the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

version -> (string)

A string that describes the rule version.

configuration -> (map)

The action configuration fields for the rule.

key -> (string)

value -> (string)

commands -> (list)

The shell commands to run with your commands rule in CodePipeline. All commands are supported except multi-line formats. While CodeBuild logs and permissions are used, you do not need to create any resources in CodeBuild.

### Note

Using compute time for this action will incur separate charges in CodeBuild.

(string)

inputArtifacts -> (list)

The input artifacts fields for the rule, such as specifying an input file for the rule.

(structure)

Represents information about an artifact to be worked on, such as a test or build artifact.

name -> (string)

The name of the artifact to be worked on (for example, âMy Appâ).

Artifacts are the files that are worked on by actions in the pipeline. See the action configuration for each action for details about artifact parameters. For example, the S3 source action input artifact is a file name (or file path), and the files are generally provided as a ZIP file. Example artifact name: SampleApp_Windows.zip

The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.

roleArn -> (string)

The pipeline role ARN associated with the rule.

region -> (string)

The Region for the condition associated with the rule.

timeoutInMinutes -> (integer)

The action timeout for the rule.

beforeEntry -> (structure)

The method to use when a stage allows entry. For example, configuring this field for conditions will allow entry to the stage when the conditions are met.

conditions -> (list)

The conditions that are configured as entry conditions.

(structure)

The condition for the stage. A condition is made up of the rules and the result for the condition. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html) .. For more information about rules, see the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

result -> (string)

The action to be done when the condition is met. For example, rolling back an execution for a failure condition.

rules -> (list)

The rules that make up the condition.

(structure)

Represents information about the rule to be created for an associated condition. An example would be creating a new rule for an entry condition, such as a rule that checks for a test result before allowing the run to enter the deployment stage. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html) . For more information about rules, see the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

name -> (string)

The name of the rule that is created for the condition, such as `VariableCheck` .

ruleTypeId -> (structure)

The ID for the rule type, which is made up of the combined values for category, owner, provider, and version.

category -> (string)

A category defines what kind of rule can be run in the stage, and constrains the provider type for the rule. The valid category is `Rule` .

owner -> (string)

The creator of the rule being called. The valid value for the `Owner` field in the rule category is `AWS` .

provider -> (string)

The rule provider, such as the `DeploymentWindow` rule. For a list of rule provider names, see the rules listed in the [CodePipeline rule reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html) .

version -> (string)

A string that describes the rule version.

configuration -> (map)

The action configuration fields for the rule.

key -> (string)

value -> (string)

commands -> (list)

The shell commands to run with your commands rule in CodePipeline. All commands are supported except multi-line formats. While CodeBuild logs and permissions are used, you do not need to create any resources in CodeBuild.

### Note

Using compute time for this action will incur separate charges in CodeBuild.

(string)

inputArtifacts -> (list)

The input artifacts fields for the rule, such as specifying an input file for the rule.

(structure)

Represents information about an artifact to be worked on, such as a test or build artifact.

name -> (string)

The name of the artifact to be worked on (for example, âMy Appâ).

Artifacts are the files that are worked on by actions in the pipeline. See the action configuration for each action for details about artifact parameters. For example, the S3 source action input artifact is a file name (or file path), and the files are generally provided as a ZIP file. Example artifact name: SampleApp_Windows.zip

The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.

roleArn -> (string)

The pipeline role ARN associated with the rule.

region -> (string)

The Region for the condition associated with the rule.

timeoutInMinutes -> (integer)

The action timeout for the rule.

version -> (integer)

The version number of the pipeline. A new pipeline always has a version number of 1. This number is incremented when a pipeline is updated.

executionMode -> (string)

The method that the pipeline will use to handle multiple executions. The default mode is SUPERSEDED.

pipelineType -> (string)

CodePipeline provides the following pipeline types, which differ in characteristics and price, so that you can tailor your pipeline features and cost to the needs of your applications.

- V1 type pipelines have a JSON structure that contains standard pipeline, stage, and action-level parameters.
- V2 type pipelines have the same structure as a V1 type, along with additional parameters for release safety and trigger configuration.

### Warning

Including V2 parameters, such as triggers on Git tags, in the pipeline JSON when creating or updating a pipeline will result in the pipeline having the V2 type of pipeline and the associated costs.

For information about pricing for CodePipeline, see [Pricing](http://aws.amazon.com/codepipeline/pricing/) .

For information about which type of pipeline to choose, see [What type of pipeline is right for me?](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-types-planning.html) .

variables -> (list)

A list that defines the pipeline variables for a pipeline resource. Variable names can have alphanumeric and underscore characters, and the values must match `[A-Za-z0-9@\-_]+` .

(structure)

A variable declared at the pipeline level.

name -> (string)

The name of a pipeline-level variable.

defaultValue -> (string)

The value of a pipeline-level variable.

description -> (string)

The description of a pipeline-level variable. Itâs used to add additional context about the variable, and not being used at time when pipeline executes.

triggers -> (list)

The trigger configuration specifying a type of event, such as Git tags, that starts the pipeline.

### Note

When a trigger configuration is specified, default change detection for repository and branch commits is disabled.

(structure)

Represents information about the specified trigger configuration, such as the filter criteria and the source stage for the action that contains the trigger.

### Note

This is only supported for the `CodeStarSourceConnection` action type.

### Note

When a trigger configuration is specified, default change detection for repository and branch commits is disabled.

providerType -> (string)

The source provider for the event, such as connections configured for a repository with Git tags, for the specified trigger configuration.

gitConfiguration -> (structure)

Provides the filter criteria and the source stage for the repository event that starts the pipeline, such as Git tags.

sourceActionName -> (string)

The name of the pipeline source action where the trigger configuration, such as Git tags, is specified. The trigger configuration will start the pipeline upon the specified change only.

### Note

You can only specify one trigger configuration per source action.

push -> (list)

The field where the repository event that will start the pipeline, such as pushing Git tags, is specified with details.

(structure)

The event criteria that specify when a specified repository event will start the pipeline for the specified trigger configuration, such as the lists of Git tags to include and exclude.

tags -> (structure)

The field that contains the details for the Git tags trigger configuration.

includes -> (list)

The list of patterns of Git tags that, when pushed, are to be included as criteria that starts the pipeline.

(string)

excludes -> (list)

The list of patterns of Git tags that, when pushed, are to be excluded from starting the pipeline.

(string)

branches -> (structure)

The field that specifies to filter on branches for the push trigger configuration.

includes -> (list)

The list of patterns of Git branches that, when a commit is pushed, are to be included as criteria that starts the pipeline.

(string)

excludes -> (list)

The list of patterns of Git branches that, when a commit is pushed, are to be excluded from starting the pipeline.

(string)

filePaths -> (structure)

The field that specifies to filter on file paths for the push trigger configuration.

includes -> (list)

The list of patterns of Git repository file paths that, when a commit is pushed, are to be included as criteria that starts the pipeline.

(string)

excludes -> (list)

The list of patterns of Git repository file paths that, when a commit is pushed, are to be excluded from starting the pipeline.

(string)

pullRequest -> (list)

The field where the repository event that will start the pipeline is specified as pull requests.

(structure)

The event criteria for the pull request trigger configuration, such as the lists of branches or file paths to include and exclude.

The following are valid values for the events for this filter:

- CLOSED
- OPEN
- UPDATED

events -> (list)

The field that specifies which pull request events to filter on (OPEN, UPDATED, CLOSED) for the trigger configuration.

(string)

branches -> (structure)

The field that specifies to filter on branches for the pull request trigger configuration.

includes -> (list)

The list of patterns of Git branches that, when a commit is pushed, are to be included as criteria that starts the pipeline.

(string)

excludes -> (list)

The list of patterns of Git branches that, when a commit is pushed, are to be excluded from starting the pipeline.

(string)

filePaths -> (structure)

The field that specifies to filter on file paths for the pull request trigger configuration.

includes -> (list)

The list of patterns of Git repository file paths that, when a commit is pushed, are to be included as criteria that starts the pipeline.

(string)

excludes -> (list)

The list of patterns of Git repository file paths that, when a commit is pushed, are to be excluded from starting the pipeline.

(string)

tags -> (list)

Specifies the tags applied to the pipeline.

(structure)

A tag is a key-value pair that is used to manage the resource.

key -> (string)

The tagâs key.

value -> (string)

The tagâs value.