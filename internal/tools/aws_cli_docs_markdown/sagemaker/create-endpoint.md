# create-endpointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-endpoint.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-endpoint.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-endpoint

## Description

Creates an endpoint using the endpoint configuration specified in the request. SageMaker uses the endpoint to provision resources and deploy models. You create the endpoint configuration with the [CreateEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html) API.

Use this API to deploy models using SageMaker hosting services.

### Note

You must not delete an `EndpointConfig` that is in use by an endpoint that is live or while the `UpdateEndpoint` or `CreateEndpoint` operations are being performed on the endpoint. To update an endpoint, you must create a new `EndpointConfig` .

The endpoint name must be unique within an Amazon Web Services Region in your Amazon Web Services account.

When it receives the request, SageMaker creates the endpoint, launches the resources (ML compute instances), and deploys the model(s) on them.

### Note

When you call [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html) , a load call is made to DynamoDB to verify that your endpoint configuration exists. When you read data from a DynamoDB table supporting ` `Eventually Consistent Reads` [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency).html`__ , the response might not reflect the results of a recently completed write operation. The response might include some stale data. If the dependent entities are not yet in DynamoDB, this causes a validation error. If you repeat your read request after a short time, the response should return the latest data. So retry logic is recommended to handle these possible issues. We also recommend that customers call [DescribeEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpointConfig.html) before calling [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html) to minimize the potential impact of a DynamoDB eventually consistent read.

When SageMaker receives the request, it sets the endpoint status to `Creating` . After it creates the endpoint, it sets the status to `InService` . SageMaker can then process incoming requests for inferences. To check the status of an endpoint, use the [DescribeEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpoint.html) API.

If any of the models hosted at this endpoint get model data from an Amazon S3 location, SageMaker uses Amazon Web Services Security Token Service to download model artifacts from the S3 path you provided. Amazon Web Services STS is activated in your Amazon Web Services account by default. If you previously deactivated Amazon Web Services STS for a region, you need to reactivate Amazon Web Services STS for that region. For more information, see [Activating and Deactivating Amazon Web Services STS in an Amazon Web Services Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html) in the *Amazon Web Services Identity and Access Management User Guide* .

### Note

To add the IAM role policies for using this API operation, go to the [IAM console](https://console.aws.amazon.com/iam/) , and choose Roles in the left navigation pane. Search the IAM role that you want to grant access to use the [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html) and [CreateEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html) API operations, add the following policies to the role.

- Option 1: For a full SageMaker access, search and attach the `AmazonSageMakerFullAccess` policy.
- Option 2: For granting a limited access to an IAM role, paste the following Action elements manually into the JSON file of the IAM role:   `"Action": ["sagemaker:CreateEndpoint", "sagemaker:CreateEndpointConfig"]` `"Resource": [` `"arn:aws:sagemaker:region:account-id:endpoint/endpointName"` `"arn:aws:sagemaker:region:account-id:endpoint-config/endpointConfigName"` `]`   For more information, see [SageMaker API Permissions: Actions, Permissions, and Resources Reference](https://docs.aws.amazon.com/sagemaker/latest/dg/api-permissions-reference.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateEndpoint)

## Synopsis

```
create-endpoint
--endpoint-name <value>
--endpoint-config-name <value>
[--deployment-config <value>]
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

`--endpoint-name` (string)

The name of the endpoint.The name must be unique within an Amazon Web Services Region in your Amazon Web Services account. The name is case-insensitive in `CreateEndpoint` , but the case is preserved and must be matched in [InvokeEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpoint.html) .

`--endpoint-config-name` (string)

The name of an endpoint configuration. For more information, see [CreateEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html) .

`--deployment-config` (structure)

The deployment configuration for an endpoint, which contains the desired deployment strategy and rollback configurations.

BlueGreenUpdatePolicy -> (structure)

Update policy for a blue/green deployment. If this update policy is specified, SageMaker creates a new fleet during the deployment while maintaining the old fleet. SageMaker flips traffic to the new fleet according to the specified traffic routing configuration. Only one update policy should be used in the deployment configuration. If no update policy is specified, SageMaker uses a blue/green deployment strategy with all at once traffic shifting by default.

TrafficRoutingConfiguration -> (structure)

Defines the traffic routing strategy to shift traffic from the old fleet to the new fleet during an endpoint deployment.

Type -> (string)

Traffic routing strategy type.

- `ALL_AT_ONCE` : Endpoint traffic shifts to the new fleet in a single step.
- `CANARY` : Endpoint traffic shifts to the new fleet in two steps. The first step is the canary, which is a small portion of the traffic. The second step is the remainder of the traffic.
- `LINEAR` : Endpoint traffic shifts to the new fleet in n steps of a configurable size.

WaitIntervalInSeconds -> (integer)

The waiting time (in seconds) between incremental steps to turn on traffic on the new endpoint fleet.

CanarySize -> (structure)

Batch size for the first step to turn on traffic on the new endpoint fleet. `Value` must be less than or equal to 50% of the variantâs total instance count.

Type -> (string)

Specifies the endpoint capacity type.

- `INSTANCE_COUNT` : The endpoint activates based on the number of instances.
- `CAPACITY_PERCENT` : The endpoint activates based on the specified percentage of capacity.

Value -> (integer)

Defines the capacity size, either as a number of instances or a capacity percentage.

LinearStepSize -> (structure)

Batch size for each step to turn on traffic on the new endpoint fleet. `Value` must be 10-50% of the variantâs total instance count.

Type -> (string)

Specifies the endpoint capacity type.

- `INSTANCE_COUNT` : The endpoint activates based on the number of instances.
- `CAPACITY_PERCENT` : The endpoint activates based on the specified percentage of capacity.

Value -> (integer)

Defines the capacity size, either as a number of instances or a capacity percentage.

TerminationWaitInSeconds -> (integer)

Additional waiting time in seconds after the completion of an endpoint deployment before terminating the old endpoint fleet. Default is 0.

MaximumExecutionTimeoutInSeconds -> (integer)

Maximum execution timeout for the deployment. Note that the timeout value should be larger than the total waiting time specified in `TerminationWaitInSeconds` and `WaitIntervalInSeconds` .

RollingUpdatePolicy -> (structure)

Specifies a rolling deployment strategy for updating a SageMaker endpoint.

MaximumBatchSize -> (structure)

Batch size for each rolling step to provision capacity and turn on traffic on the new endpoint fleet, and terminate capacity on the old endpoint fleet. Value must be between 5% to 50% of the variantâs total instance count.

Type -> (string)

Specifies the endpoint capacity type.

- `INSTANCE_COUNT` : The endpoint activates based on the number of instances.
- `CAPACITY_PERCENT` : The endpoint activates based on the specified percentage of capacity.

Value -> (integer)

Defines the capacity size, either as a number of instances or a capacity percentage.

WaitIntervalInSeconds -> (integer)

The length of the baking period, during which SageMaker monitors alarms for each batch on the new fleet.

MaximumExecutionTimeoutInSeconds -> (integer)

The time limit for the total deployment. Exceeding this limit causes a timeout.

RollbackMaximumBatchSize -> (structure)

Batch size for rollback to the old endpoint fleet. Each rolling step to provision capacity and turn on traffic on the old endpoint fleet, and terminate capacity on the new endpoint fleet. If this field is absent, the default value will be set to 100% of total capacity which means to bring up the whole capacity of the old fleet at once during rollback.

Type -> (string)

Specifies the endpoint capacity type.

- `INSTANCE_COUNT` : The endpoint activates based on the number of instances.
- `CAPACITY_PERCENT` : The endpoint activates based on the specified percentage of capacity.

Value -> (integer)

Defines the capacity size, either as a number of instances or a capacity percentage.

AutoRollbackConfiguration -> (structure)

Automatic rollback configuration for handling endpoint deployment failures and recovery.

Alarms -> (list)

List of CloudWatch alarms in your account that are configured to monitor metrics on an endpoint. If any alarms are tripped during a deployment, SageMaker rolls back the deployment.

(structure)

An Amazon CloudWatch alarm configured to monitor metrics on an endpoint.

AlarmName -> (string)

The name of a CloudWatch alarm in your account.

JSON Syntax:

```
{
  "BlueGreenUpdatePolicy": {
    "TrafficRoutingConfiguration": {
      "Type": "ALL_AT_ONCE"|"CANARY"|"LINEAR",
      "WaitIntervalInSeconds": integer,
      "CanarySize": {
        "Type": "INSTANCE_COUNT"|"CAPACITY_PERCENT",
        "Value": integer
      },
      "LinearStepSize": {
        "Type": "INSTANCE_COUNT"|"CAPACITY_PERCENT",
        "Value": integer
      }
    },
    "TerminationWaitInSeconds": integer,
    "MaximumExecutionTimeoutInSeconds": integer
  },
  "RollingUpdatePolicy": {
    "MaximumBatchSize": {
      "Type": "INSTANCE_COUNT"|"CAPACITY_PERCENT",
      "Value": integer
    },
    "WaitIntervalInSeconds": integer,
    "MaximumExecutionTimeoutInSeconds": integer,
    "RollbackMaximumBatchSize": {
      "Type": "INSTANCE_COUNT"|"CAPACITY_PERCENT",
      "Value": integer
    }
  },
  "AutoRollbackConfiguration": {
    "Alarms": [
      {
        "AlarmName": "string"
      }
      ...
    ]
  }
}
```

`--tags` (list)

An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging Amazon Web Services Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) .

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

EndpointArn -> (string)

The Amazon Resource Name (ARN) of the endpoint.