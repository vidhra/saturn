# stop-deploymentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/stop-deployment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/stop-deployment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appconfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/index.html#cli-aws-appconfig) ]

# stop-deployment

## Description

Stops a deployment. This API action works only on deployments that have a status of `DEPLOYING` , unless an `AllowRevert` parameter is supplied. If the `AllowRevert` parameter is supplied, the status of an in-progress deployment will be `ROLLED_BACK` . The status of a completed deployment will be `REVERTED` . AppConfig only allows a revert within 72 hours of deployment completion.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appconfig-2019-10-09/StopDeployment)

## Synopsis

```
stop-deployment
--application-id <value>
--environment-id <value>
--deployment-number <value>
[--allow-revert | --no-allow-revert]
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

`--application-id` (string)

The application ID.

`--environment-id` (string)

The environment ID.

`--deployment-number` (integer)

The sequence number of the deployment.

`--allow-revert` | `--no-allow-revert` (boolean)

A Boolean that enables AppConfig to rollback a `COMPLETED` deployment to the previous configuration version. This action moves the deployment to a status of `REVERTED` .

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

**To stop configuration deployment**

The following `stop-deployment` example stops the deployment of an application configuration to the specified environment.

```
aws appconfig stop-deployment \
    --application-id 339ohji \
    --environment-id 54j1r29 \
    --deployment-number 2
```

Output:

```
{
    "DeploymentNumber": 0,
    "DeploymentDurationInMinutes": 0,
    "GrowthFactor": 0.0,
    "FinalBakeTimeInMinutes": 0,
    "PercentageComplete": 0.0
}
```

For more information, see [Step 5: Deploying a configuration](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-deploying.html) in the *AWS AppConfig User Guide*.

## Output

ApplicationId -> (string)

The ID of the application that was deployed.

EnvironmentId -> (string)

The ID of the environment that was deployed.

DeploymentStrategyId -> (string)

The ID of the deployment strategy that was deployed.

ConfigurationProfileId -> (string)

The ID of the configuration profile that was deployed.

DeploymentNumber -> (integer)

The sequence number of the deployment.

ConfigurationName -> (string)

The name of the configuration.

ConfigurationLocationUri -> (string)

Information about the source location of the configuration.

ConfigurationVersion -> (string)

The configuration version that was deployed.

Description -> (string)

The description of the deployment.

DeploymentDurationInMinutes -> (integer)

Total amount of time the deployment lasted.

GrowthType -> (string)

The algorithm used to define how percentage grew over time.

GrowthFactor -> (float)

The percentage of targets to receive a deployed configuration during each interval.

FinalBakeTimeInMinutes -> (integer)

The amount of time that AppConfig monitored for alarms before considering the deployment to be complete and no longer eligible for automatic rollback.

State -> (string)

The state of the deployment.

EventLog -> (list)

A list containing all events related to a deployment. The most recent events are displayed first.

(structure)

An object that describes a deployment event.

EventType -> (string)

The type of deployment event. Deployment event types include the start, stop, or completion of a deployment; a percentage update; the start or stop of a bake period; and the start or completion of a rollback.

TriggeredBy -> (string)

The entity that triggered the deployment event. Events can be triggered by a user, AppConfig, an Amazon CloudWatch alarm, or an internal error.

Description -> (string)

A description of the deployment event. Descriptions include, but are not limited to, the following:

- The Amazon Web Services account or the Amazon CloudWatch alarm ARN that initiated a rollback.
- The percentage of hosts that received the deployment.
- A recommendation to attempt a new deployment (in the case of an internal error).

ActionInvocations -> (list)

The list of extensions that were invoked as part of the deployment.

(structure)

An extension that was invoked as part of a deployment event.

ExtensionIdentifier -> (string)

The name, the ID, or the Amazon Resource Name (ARN) of the extension.

ActionName -> (string)

The name of the action.

Uri -> (string)

The extension URI associated to the action point in the extension definition. The URI can be an Amazon Resource Name (ARN) for one of the following: an Lambda function, an Amazon Simple Queue Service queue, an Amazon Simple Notification Service topic, or the Amazon EventBridge default event bus.

RoleArn -> (string)

An Amazon Resource Name (ARN) for an Identity and Access Management assume role.

ErrorMessage -> (string)

The error message when an extension invocation fails.

ErrorCode -> (string)

The error code when an extension invocation fails.

InvocationId -> (string)

A system-generated ID for this invocation.

OccurredAt -> (timestamp)

The date and time the event occurred.

PercentageComplete -> (float)

The percentage of targets for which the deployment is available.

StartedAt -> (timestamp)

The time the deployment started.

CompletedAt -> (timestamp)

The time the deployment completed.

AppliedExtensions -> (list)

A list of extensions that were processed as part of the deployment. The extensions that were previously associated to the configuration profile, environment, or the application when `StartDeployment` was called.

(structure)

An extension that was invoked during a deployment.

ExtensionId -> (string)

The system-generated ID of the extension.

ExtensionAssociationId -> (string)

The system-generated ID for the association.

VersionNumber -> (integer)

The extension version number.

Parameters -> (map)

One or more parameters for the actions called by the extension.

key -> (string)

value -> (string)

KmsKeyArn -> (string)

The Amazon Resource Name of the Key Management Service key used to encrypt configuration data. You can encrypt secrets stored in Secrets Manager, Amazon Simple Storage Service (Amazon S3) objects encrypted with SSE-KMS, or secure string parameters stored in Amazon Web Services Systems Manager Parameter Store.

KmsKeyIdentifier -> (string)

The Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.

VersionLabel -> (string)

A user-defined label for an AppConfig hosted configuration version.