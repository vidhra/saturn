# get-deploymentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/get-deployment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/get-deployment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [greengrassv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/index.html#cli-aws-greengrassv2) ]

# get-deployment

## Description

Gets a deployment. Deployments define the components that run on Greengrass core devices.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/greengrassv2-2020-11-30/GetDeployment)

## Synopsis

```
get-deployment
--deployment-id <value>
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

`--deployment-id` (string)

The ID of the deployment.

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

**To get a deployment**

The following `get-deployment` example gets information about the deployment of the AWS IoT Greengrass nucleus component to a group of core devices.

```
aws greengrassv2 get-deployment \
    --deployment-id a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
```

Output:

```
{
    "targetArn": "arn:aws:iot:us-west-2:123456789012:thinggroup/MyGreengrassCoreGroup",
    "revisionId": "14",
    "deploymentId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "deploymentName": "Deployment for MyGreengrassCoreGroup",
    "deploymentStatus": "ACTIVE",
    "iotJobId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "iotJobArn": "arn:aws:iot:us-west-2:123456789012:job/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "components": {
        "aws.greengrass.Nucleus": {
            "componentVersion": "2.0.3",
            "configurationUpdate": {
                "merge": "{\"jvmOptions\":\"-Xmx64m\",\"logging\":{\"level\":\"WARN\"}}",
                "reset": [
                    "/networkProxy",
                    "/mqtt"
                ]
            }
        }
    },
    "deploymentPolicies": {
        "failureHandlingPolicy": "ROLLBACK",
        "componentUpdatePolicy": {
            "timeoutInSeconds": 60,
            "action": "NOTIFY_COMPONENTS"
        },
        "configurationValidationPolicy": {
            "timeoutInSeconds": 60
        }
    },
    "iotJobConfiguration": {},
    "creationTimestamp": "2021-01-07T17:21:20.691000-08:00",
    "isLatestForTarget": false,
    "tags": {}
}
```

For more information, see [Deploy components to devices](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-deployments.html) in the *AWS IoT Greengrass V2 Developer Guide*.

## Output

targetArn -> (string)

The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the target IoT thing or thing group.

revisionId -> (string)

The revision number of the deployment.

deploymentId -> (string)

The ID of the deployment.

deploymentName -> (string)

The name of the deployment.

deploymentStatus -> (string)

The status of the deployment.

iotJobId -> (string)

The ID of the IoT job that applies the deployment to target devices.

iotJobArn -> (string)

The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the IoT job that applies the deployment to target devices.

components -> (map)

The components to deploy. This is a dictionary, where each key is the name of a component, and each keyâs value is the version and configuration to deploy for that component.

key -> (string)

value -> (structure)

Contains information about a component to deploy.

componentVersion -> (string)

The version of the component.

configurationUpdate -> (structure)

The configuration updates to deploy for the component. You can define *reset* updates and *merge* updates. A reset updates the keys that you specify to the default configuration for the component. A merge updates the core deviceâs component configuration with the keys and values that you specify. The IoT Greengrass Core software applies reset updates before it applies merge updates. For more information, see [Update component configurations](https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html) in the *IoT Greengrass V2 Developer Guide* .

merge -> (string)

A serialized JSON string that contains the configuration object to merge to target devices. The core device merges this configuration with the componentâs existing configuration. If this is the first time a component deploys on a device, the core device merges this configuration with the componentâs default configuration. This means that the core device keeps itâs existing configuration for keys and values that you donât specify in this object. For more information, see [Merge configuration updates](https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html#merge-configuration-update) in the *IoT Greengrass V2 Developer Guide* .

reset -> (list)

The list of configuration nodes to reset to default values on target devices. Use JSON pointers to specify each node to reset. JSON pointers start with a forward slash (`/` ) and use forward slashes to separate the key for each level in the object. For more information, see the [JSON pointer specification](https://tools.ietf.org/html/rfc6901) and [Reset configuration updates](https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html#reset-configuration-update) in the *IoT Greengrass V2 Developer Guide* .

(string)

runWith -> (structure)

The system user and group that the IoT Greengrass Core software uses to run component processes on the core device. If you omit this parameter, the IoT Greengrass Core software uses the system user and group that you configure for the core device. For more information, see [Configure the user and group that run components](https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-user) in the *IoT Greengrass V2 Developer Guide* .

posixUser -> (string)

The POSIX system user and, optionally, group to use to run this component on Linux core devices. The user, and group if specified, must exist on each Linux core device. Specify the user and group separated by a colon (`:` ) in the following format: `user:group` . The group is optional. If you donât specify a group, the IoT Greengrass Core software uses the primary user for the group.

If you omit this parameter, the IoT Greengrass Core software uses the default system user and group that you configure on the Greengrass nucleus component. For more information, see [Configure the user and group that run components](https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-user) .

systemResourceLimits -> (structure)

The system resource limits to apply to this componentâs process on the core device. IoT Greengrass currently supports this feature on only Linux core devices.

If you omit this parameter, the IoT Greengrass Core software uses the default system resource limits that you configure on the Greengrass nucleus component. For more information, see [Configure system resource limits for components](https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-system-resource-limits) .

memory -> (long)

The maximum amount of RAM, expressed in kilobytes, that a componentâs processes can use on the core device.

cpus -> (double)

The maximum amount of CPU time that a componentâs processes can use on the core device. A core deviceâs total CPU time is equivalent to the deviceâs number of CPU cores. For example, on a core device with 4 CPU cores, you can set this value to `2` to limit the componentâs processes to 50 percent usage of each CPU core. On a device with 1 CPU core, you can set this value to `0.25` to limit the componentâs processes to 25 percent usage of the CPU. If you set this value to a number greater than the number of CPU cores, the IoT Greengrass Core software doesnât limit the componentâs CPU usage.

windowsUser -> (string)

The Windows user to use to run this component on Windows core devices. The user must exist on each Windows core device, and its name and password must be in the LocalSystem accountâs Credentials Manager instance.

If you omit this parameter, the IoT Greengrass Core software uses the default Windows user that you configure on the Greengrass nucleus component. For more information, see [Configure the user and group that run components](https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-user) .

deploymentPolicies -> (structure)

The deployment policies for the deployment. These policies define how the deployment updates components and handles failure.

failureHandlingPolicy -> (string)

The failure handling policy for the configuration deployment. This policy defines what to do if the deployment fails.

Default: `ROLLBACK`

componentUpdatePolicy -> (structure)

The component update policy for the configuration deployment. This policy defines when itâs safe to deploy the configuration to devices.

timeoutInSeconds -> (integer)

The amount of time in seconds that each component on a device has to report that itâs safe to update. If the component waits for longer than this timeout, then the deployment proceeds on the device.

Default: `60`

action -> (string)

Whether or not to notify components and wait for components to become safe to update. Choose from the following options:

- `NOTIFY_COMPONENTS` â The deployment notifies each component before it stops and updates that component. Components can use the [SubscribeToComponentUpdates](https://docs.aws.amazon.com/greengrass/v2/developerguide/interprocess-communication.html#ipc-operation-subscribetocomponentupdates) IPC operation to receive these notifications. Then, components can respond with the [DeferComponentUpdate](https://docs.aws.amazon.com/greengrass/v2/developerguide/interprocess-communication.html#ipc-operation-defercomponentupdate) IPC operation. For more information, see [Create deployments](https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html) in the *IoT Greengrass V2 Developer Guide* .
- `SKIP_NOTIFY_COMPONENTS` â The deployment doesnât notify components or wait for them to be safe to update.

Default: `NOTIFY_COMPONENTS`

configurationValidationPolicy -> (structure)

The configuration validation policy for the configuration deployment. This policy defines how long each component has to validate its configure updates.

timeoutInSeconds -> (integer)

The amount of time in seconds that a component can validate its configuration updates. If the validation time exceeds this timeout, then the deployment proceeds for the device.

Default: `30`

iotJobConfiguration -> (structure)

The job configuration for the deployment configuration. The job configuration specifies the rollout, timeout, and stop configurations for the deployment configuration.

jobExecutionsRolloutConfig -> (structure)

The rollout configuration for the job. This configuration defines the rate at which the job rolls out to the fleet of target devices.

exponentialRate -> (structure)

The exponential rate to increase the job rollout rate.

baseRatePerMinute -> (integer)

The minimum number of devices that receive a pending job notification, per minute, when the job starts. This parameter defines the initial rollout rate of the job.

incrementFactor -> (double)

The exponential factor to increase the rollout rate for the job.

This parameter supports up to one digit after the decimal (for example, you can specify `1.5` , but not `1.55` ).

rateIncreaseCriteria -> (structure)

The criteria to increase the rollout rate for the job.

numberOfNotifiedThings -> (integer)

The number of devices to receive the job notification before the rollout rate increases.

numberOfSucceededThings -> (integer)

The number of devices to successfully run the configuration job before the rollout rate increases.

maximumPerMinute -> (integer)

The maximum number of devices that receive a pending job notification, per minute.

abortConfig -> (structure)

The stop configuration for the job. This configuration defines when and how to stop a job rollout.

criteriaList -> (list)

The list of criteria that define when and how to cancel the configuration deployment.

(structure)

Contains criteria that define when and how to cancel a job.

The deployment stops if the following conditions are true:

- The number of things that receive the deployment exceeds the `minNumberOfExecutedThings` .
- The percentage of failures with type `failureType` exceeds the `thresholdPercentage` .

failureType -> (string)

The type of job deployment failure that can cancel a job.

action -> (string)

The action to perform when the criteria are met.

thresholdPercentage -> (double)

The minimum percentage of `failureType` failures that occur before the job can cancel.

This parameter supports up to two digits after the decimal (for example, you can specify `10.9` or `10.99` , but not `10.999` ).

minNumberOfExecutedThings -> (integer)

The minimum number of things that receive the configuration before the job can cancel.

timeoutConfig -> (structure)

The timeout configuration for the job. This configuration defines the amount of time each device has to complete the job.

inProgressTimeoutInMinutes -> (long)

The amount of time, in minutes, that devices have to complete the job. The timer starts when the job status is set to `IN_PROGRESS` . If the job status doesnât change to a terminal state before the time expires, then the job status is set to `TIMED_OUT` .

The timeout interval must be between 1 minute and 7 days (10080 minutes).

creationTimestamp -> (timestamp)

The time at which the deployment was created, expressed in ISO 8601 format.

isLatestForTarget -> (boolean)

Whether or not the deployment is the latest revision for its target.

parentTargetArn -> (string)

The parent deploymentâs target [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) within a subdeployment.

tags -> (map)

A list of key-value pairs that contain metadata for the resource. For more information, see [Tag your resources](https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html) in the *IoT Greengrass V2 Developer Guide* .

key -> (string)

value -> (string)