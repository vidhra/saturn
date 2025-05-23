# create-edge-deployment-planÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-edge-deployment-plan.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-edge-deployment-plan.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-edge-deployment-plan

## Description

Creates an edge deployment plan, consisting of multiple stages. Each stage may have a different deployment configuration and devices.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateEdgeDeploymentPlan)

## Synopsis

```
create-edge-deployment-plan
--edge-deployment-plan-name <value>
--model-configs <value>
--device-fleet-name <value>
[--stages <value>]
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

`--edge-deployment-plan-name` (string)

The name of the edge deployment plan.

`--model-configs` (list)

List of models associated with the edge deployment plan.

(structure)

Contains information about the configuration of a model in a deployment.

ModelHandle -> (string)

The name the device application uses to reference this model.

EdgePackagingJobName -> (string)

The edge packaging job associated with this deployment.

Shorthand Syntax:

```
ModelHandle=string,EdgePackagingJobName=string ...
```

JSON Syntax:

```
[
  {
    "ModelHandle": "string",
    "EdgePackagingJobName": "string"
  }
  ...
]
```

`--device-fleet-name` (string)

The device fleet used for this edge deployment plan.

`--stages` (list)

List of stages of the edge deployment plan. The number of stages is limited to 10 per deployment.

(structure)

Contains information about a stage in an edge deployment plan.

StageName -> (string)

The name of the stage.

DeviceSelectionConfig -> (structure)

Configuration of the devices in the stage.

DeviceSubsetType -> (string)

Type of device subsets to deploy to the current stage.

Percentage -> (integer)

Percentage of devices in the fleet to deploy to the current stage.

DeviceNames -> (list)

List of devices chosen to deploy.

(string)

DeviceNameContains -> (string)

A filter to select devices with names containing this name.

DeploymentConfig -> (structure)

Configuration of the deployment details.

FailureHandlingPolicy -> (string)

Toggle that determines whether to rollback to previous configuration if the current deployment fails. By default this is turned on. You may turn this off if you want to investigate the errors yourself.

Shorthand Syntax:

```
StageName=string,DeviceSelectionConfig={DeviceSubsetType=string,Percentage=integer,DeviceNames=[string,string],DeviceNameContains=string},DeploymentConfig={FailureHandlingPolicy=string} ...
```

JSON Syntax:

```
[
  {
    "StageName": "string",
    "DeviceSelectionConfig": {
      "DeviceSubsetType": "PERCENTAGE"|"SELECTION"|"NAMECONTAINS",
      "Percentage": integer,
      "DeviceNames": ["string", ...],
      "DeviceNameContains": "string"
    },
    "DeploymentConfig": {
      "FailureHandlingPolicy": "ROLLBACK_ON_FAILURE"|"DO_NOTHING"
    }
  }
  ...
]
```

`--tags` (list)

List of tags with which to tag the edge deployment plan.

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

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

EdgeDeploymentPlanArn -> (string)

The ARN of the edge deployment plan.