# get-action-typeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-action-type.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-action-type.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codepipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/index.html#cli-aws-codepipeline) ]

# get-action-type

## Description

Returns information about an action type created for an external provider, where the action is to be used by customers of the external provider. The action can be created with any supported integration model.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/GetActionType)

## Synopsis

```
get-action-type
--category <value>
--owner <value>
--provider <value>
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

Defines what kind of action can be taken in the stage. The following are the valid values:

- `Source`
- `Build`
- `Test`
- `Deploy`
- `Approval`
- `Invoke`
- `Compute`

Possible values:

- `Source`
- `Build`
- `Deploy`
- `Test`
- `Invoke`
- `Approval`
- `Compute`

`--owner` (string)

The creator of an action type that was created with any supported integration model. There are two valid values: `AWS` and `ThirdParty` .

`--provider` (string)

The provider of the action type being called. The provider name is specified when the action type is created.

`--action-version` (string)

A string that describes the action type version.

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

actionType -> (structure)

The action type information for the requested action type, such as the action type ID.

description -> (string)

The description for the action type to be updated.

executor -> (structure)

Information about the executor for an action type that was created with any supported integration model.

configuration -> (structure)

The action configuration properties for the action type. These properties are specified in the action definition when the action type is created.

lambdaExecutorConfiguration -> (structure)

Details about the `Lambda` executor of the action type.

lambdaFunctionArn -> (string)

The ARN of the Lambda function used by the action engine.

jobWorkerExecutorConfiguration -> (structure)

Details about the `JobWorker` executor of the action type.

pollingAccounts -> (list)

The accounts in which the job worker is configured and might poll for jobs as part of the action execution.

(string)

pollingServicePrincipals -> (list)

The service Principals in which the job worker is configured and might poll for jobs as part of the action execution.

(string)

type -> (string)

The integration model used to create and update the action type, `Lambda` or `JobWorker` .

policyStatementsTemplate -> (string)

The policy statement that specifies the permissions in the CodePipeline customer account that are needed to successfully run an action.

To grant permission to another account, specify the account ID as the Principal, a domain-style identifier defined by the service, for example `codepipeline.amazonaws.com` .

### Note

The size of the passed JSON policy document cannot exceed 2048 characters.

jobTimeout -> (integer)

The timeout in seconds for the job. An action execution can have multiple jobs. This is the timeout for a single job, not the entire action execution.

id -> (structure)

The action category, owner, provider, and version of the action type to be updated.

category -> (string)

Defines what kind of action can be taken in the stage, one of the following:

- `Source`
- `Build`
- `Test`
- `Deploy`
- `Approval`
- `Invoke`

owner -> (string)

The creator of the action type being called: `AWS` or `ThirdParty` .

provider -> (string)

The provider of the action type being called. The provider name is supplied when the action type is created.

version -> (string)

A string that describes the action type version.

inputArtifactDetails -> (structure)

Details for the artifacts, such as application files, to be worked on by the action. For example, the minimum and maximum number of input artifacts allowed.

minimumCount -> (integer)

The minimum number of artifacts that can be used with the action type. For example, you should specify a minimum and maximum of zero input artifacts for an action type with a category of `source` .

maximumCount -> (integer)

The maximum number of artifacts that can be used with the actiontype. For example, you should specify a minimum and maximum of zero input artifacts for an action type with a category of `source` .

outputArtifactDetails -> (structure)

Details for the output artifacts, such as a built application, that are the result of the action. For example, the minimum and maximum number of output artifacts allowed.

minimumCount -> (integer)

The minimum number of artifacts that can be used with the action type. For example, you should specify a minimum and maximum of zero input artifacts for an action type with a category of `source` .

maximumCount -> (integer)

The maximum number of artifacts that can be used with the actiontype. For example, you should specify a minimum and maximum of zero input artifacts for an action type with a category of `source` .

permissions -> (structure)

Details identifying the accounts with permissions to use the action type.

allowedAccounts -> (list)

A list of Amazon Web Services account IDs with access to use the action type in their pipelines.

(string)

properties -> (list)

The properties of the action type to be updated.

(structure)

Represents information about each property specified in the action configuration, such as the description and key name that display for the customer using the action type.

name -> (string)

The property name that is displayed to users.

optional -> (boolean)

Whether the configuration property is an optional value.

key -> (boolean)

Whether the configuration property is a key.

noEcho -> (boolean)

Whether to omit the field value entered by the customer in the log. If `true` , the value is not saved in CloudTrail logs for the action execution.

queryable -> (boolean)

Indicates that the property is used with polling. An action type can have up to one queryable property. If it has one, that property must be both required and not secret.

description -> (string)

The description of the property that is displayed to users.

urls -> (structure)

The links associated with the action type to be updated.

configurationUrl -> (string)

The URL returned to the CodePipeline console that contains a link to the page where customers can configure the external action.

entityUrlTemplate -> (string)

The URL returned to the CodePipeline console that provides a deep link to the resources of the external system, such as a status page. This link is provided as part of the action display in the pipeline.

executionUrlTemplate -> (string)

The link to an execution page for the action type in progress. For example, for a CodeDeploy action, this link is shown on the pipeline view page in the CodePipeline console, and it links to a CodeDeploy status page.

revisionUrlTemplate -> (string)

The URL returned to the CodePipeline console that contains a link to the page where customers can update or change the configuration of the external action.