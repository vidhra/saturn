# start-simulation-job-batchÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/start-simulation-job-batch.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/start-simulation-job-batch.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [robomaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/index.html#cli-aws-robomaker) ]

# start-simulation-job-batch

## Description

### Warning

End of support notice: On September 10, 2025, Amazon Web Services will discontinue support for Amazon Web Services RoboMaker. After September 10, 2025, you will no longer be able to access the Amazon Web Services RoboMaker console or Amazon Web Services RoboMaker resources. For more information on transitioning to Batch to help run containerized simulations, visit [https://aws.amazon.com/blogs/hpc/run-simulations-using-multiple-containers-in-a-single-aws-batch-job/](https://aws.amazon.com/blogs/hpc/run-simulations-using-multiple-containers-in-a-single-aws-batch-job/) .

Starts a new simulation job batch. The batch is defined using one or more `SimulationJobRequest` objects.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/StartSimulationJobBatch)

## Synopsis

```
start-simulation-job-batch
[--client-request-token <value>]
[--batch-policy <value>]
--create-simulation-job-requests <value>
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

`--client-request-token` (string)

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

`--batch-policy` (structure)

The batch policy.

timeoutInSeconds -> (long)

The amount of time, in seconds, to wait for the batch to complete.

If a batch times out, and there are pending requests that were failing due to an internal failure (like `InternalServiceError` ), they will be moved to the failed list and the batch status will be `Failed` . If the pending requests were failing for any other reason, the failed pending requests will be moved to the failed list and the batch status will be `TimedOut` .

maxConcurrency -> (integer)

The number of active simulation jobs create as part of the batch that can be in an active state at the same time.

Active states include: `Pending` ,``Preparing`` , `Running` , `Restarting` , `RunningFailed` and `Terminating` . All other states are terminal states.

Shorthand Syntax:

```
timeoutInSeconds=long,maxConcurrency=integer
```

JSON Syntax:

```
{
  "timeoutInSeconds": long,
  "maxConcurrency": integer
}
```

`--create-simulation-job-requests` (list)

A list of simulation job requests to create in the batch.

(structure)

Information about a simulation job request.

outputLocation -> (structure)

The output location.

s3Bucket -> (string)

The S3 bucket for output.

s3Prefix -> (string)

The S3 folder in the `s3Bucket` where output files will be placed.

loggingConfig -> (structure)

The logging configuration.

recordAllRosTopics -> (boolean)

A boolean indicating whether to record all ROS topics.

### Warning

This API is no longer supported and will throw an error if used.

maxJobDurationInSeconds -> (long)

The maximum simulation job duration in seconds. The value must be 8 days (691,200 seconds) or less.

iamRole -> (string)

The IAM role name that allows the simulation instance to call the AWS APIs that are specified in its associated policies on your behalf. This is how credentials are passed in to your simulation job.

failureBehavior -> (string)

The failure behavior the simulation job.

Continue

Leaves the host running for its maximum timeout duration after a `4XX` error code.

Fail

Stop the simulation job and terminate the instance.

useDefaultApplications -> (boolean)

A Boolean indicating whether to use default applications in the simulation job. Default applications include Gazebo, rqt, rviz and terminal access.

robotApplications -> (list)

The robot applications to use in the simulation job.

(structure)

Application configuration information for a robot.

application -> (string)

The application information for the robot application.

applicationVersion -> (string)

The version of the robot application.

launchConfig -> (structure)

The launch configuration for the robot application.

packageName -> (string)

The package name.

launchFile -> (string)

The launch file name.

environmentVariables -> (map)

The environment variables for the application launch.

key -> (string)

value -> (string)

portForwardingConfig -> (structure)

The port forwarding configuration.

portMappings -> (list)

The port mappings for the configuration.

(structure)

An object representing a port mapping.

jobPort -> (integer)

The port number on the simulation job instance to use as a remote connection point.

applicationPort -> (integer)

The port number on the application.

enableOnPublicIp -> (boolean)

A Boolean indicating whether to enable this port mapping on public IP.

streamUI -> (boolean)

Boolean indicating whether a streaming session will be configured for the application. If `True` , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and launch the component. It must have a graphical user interface.

command -> (list)

If youâve specified `General` as the value for your `RobotSoftwareSuite` , you can use this field to specify a list of commands for your container image.

If youâve specified `SimulationRuntime` as the value for your `SimulationSoftwareSuite` , you can use this field to specify a list of commands for your container image.

(string)

uploadConfigurations -> (list)

The upload configurations for the robot application.

(structure)

Provides upload configuration information. Files are uploaded from the simulation job to a location you specify.

name -> (string)

A prefix that specifies where files will be uploaded in Amazon S3. It is appended to the simulation output location to determine the final path.

For example, if your simulation output location is `s3://amzn-s3-demo-bucket` and your upload configuration name is `robot-test` , your files will be uploaded to `s3://amzn-s3-demo-bucket/<simid>/<runid>/robot-test` .

path -> (string)

Specifies the path of the file(s) to upload. Standard Unix glob matching rules are accepted, with the addition of `**` as a *super asterisk* . For example, specifying `/var/log/**.log` causes all .log files in the `/var/log` directory tree to be collected. For more examples, see [Glob Library](https://github.com/gobwas/glob) .

uploadBehavior -> (string)

Specifies when to upload the files:

UPLOAD_ON_TERMINATE

Matching files are uploaded once the simulation enters the `TERMINATING` state. Matching files are not uploaded until all of your code (including tools) have stopped.

If there is a problem uploading a file, the upload is retried. If problems persist, no further upload attempts will be made.

UPLOAD_ROLLING_AUTO_REMOVE

Matching files are uploaded as they are created. They are deleted after they are uploaded. The specified path is checked every 5 seconds. A final check is made when all of your code (including tools) have stopped.

useDefaultUploadConfigurations -> (boolean)

A Boolean indicating whether to use default upload configurations. By default, `.ros` and `.gazebo` files are uploaded when the application terminates and all ROS topics will be recorded.

If you set this value, you must specify an `outputLocation` .

### Warning

This API is no longer supported and will throw an error if used.

tools -> (list)

Information about tools configured for the robot application.

(structure)

Information about a tool. Tools are used in a simulation job.

streamUI -> (boolean)

Boolean indicating whether a streaming session will be configured for the tool. If `True` , AWS RoboMaker will configure a connection so you can interact with the tool as it is running in the simulation. It must have a graphical user interface. The default is `False` .

name -> (string)

The name of the tool.

command -> (string)

Command-line arguments for the tool. It must include the tool executable name.

streamOutputToCloudWatch -> (boolean)

Boolean indicating whether logs will be recorded in CloudWatch for the tool. The default is `False` .

exitBehavior -> (string)

Exit behavior determines what happens when your tool quits running. `RESTART` will cause your tool to be restarted. `FAIL` will cause your job to exit. The default is `RESTART` .

useDefaultTools -> (boolean)

A Boolean indicating whether to use default robot application tools. The default tools are rviz, rqt, terminal and rosbag record. The default is `False` .

### Warning

This API is no longer supported and will throw an error if used.

simulationApplications -> (list)

The simulation applications to use in the simulation job.

(structure)

Information about a simulation application configuration.

application -> (string)

The application information for the simulation application.

applicationVersion -> (string)

The version of the simulation application.

launchConfig -> (structure)

The launch configuration for the simulation application.

packageName -> (string)

The package name.

launchFile -> (string)

The launch file name.

environmentVariables -> (map)

The environment variables for the application launch.

key -> (string)

value -> (string)

portForwardingConfig -> (structure)

The port forwarding configuration.

portMappings -> (list)

The port mappings for the configuration.

(structure)

An object representing a port mapping.

jobPort -> (integer)

The port number on the simulation job instance to use as a remote connection point.

applicationPort -> (integer)

The port number on the application.

enableOnPublicIp -> (boolean)

A Boolean indicating whether to enable this port mapping on public IP.

streamUI -> (boolean)

Boolean indicating whether a streaming session will be configured for the application. If `True` , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and launch the component. It must have a graphical user interface.

command -> (list)

If youâve specified `General` as the value for your `RobotSoftwareSuite` , you can use this field to specify a list of commands for your container image.

If youâve specified `SimulationRuntime` as the value for your `SimulationSoftwareSuite` , you can use this field to specify a list of commands for your container image.

(string)

uploadConfigurations -> (list)

Information about upload configurations for the simulation application.

(structure)

Provides upload configuration information. Files are uploaded from the simulation job to a location you specify.

name -> (string)

A prefix that specifies where files will be uploaded in Amazon S3. It is appended to the simulation output location to determine the final path.

For example, if your simulation output location is `s3://amzn-s3-demo-bucket` and your upload configuration name is `robot-test` , your files will be uploaded to `s3://amzn-s3-demo-bucket/<simid>/<runid>/robot-test` .

path -> (string)

Specifies the path of the file(s) to upload. Standard Unix glob matching rules are accepted, with the addition of `**` as a *super asterisk* . For example, specifying `/var/log/**.log` causes all .log files in the `/var/log` directory tree to be collected. For more examples, see [Glob Library](https://github.com/gobwas/glob) .

uploadBehavior -> (string)

Specifies when to upload the files:

UPLOAD_ON_TERMINATE

Matching files are uploaded once the simulation enters the `TERMINATING` state. Matching files are not uploaded until all of your code (including tools) have stopped.

If there is a problem uploading a file, the upload is retried. If problems persist, no further upload attempts will be made.

UPLOAD_ROLLING_AUTO_REMOVE

Matching files are uploaded as they are created. They are deleted after they are uploaded. The specified path is checked every 5 seconds. A final check is made when all of your code (including tools) have stopped.

worldConfigs -> (list)

A list of world configurations.

### Warning

This API is no longer supported and will throw an error if used.

(structure)

Configuration information for a world.

world -> (string)

The world generated by Simulation WorldForge.

useDefaultUploadConfigurations -> (boolean)

A Boolean indicating whether to use default upload configurations. By default, `.ros` and `.gazebo` files are uploaded when the application terminates and all ROS topics will be recorded.

If you set this value, you must specify an `outputLocation` .

### Warning

This API is no longer supported and will throw an error if used.

tools -> (list)

Information about tools configured for the simulation application.

(structure)

Information about a tool. Tools are used in a simulation job.

streamUI -> (boolean)

Boolean indicating whether a streaming session will be configured for the tool. If `True` , AWS RoboMaker will configure a connection so you can interact with the tool as it is running in the simulation. It must have a graphical user interface. The default is `False` .

name -> (string)

The name of the tool.

command -> (string)

Command-line arguments for the tool. It must include the tool executable name.

streamOutputToCloudWatch -> (boolean)

Boolean indicating whether logs will be recorded in CloudWatch for the tool. The default is `False` .

exitBehavior -> (string)

Exit behavior determines what happens when your tool quits running. `RESTART` will cause your tool to be restarted. `FAIL` will cause your job to exit. The default is `RESTART` .

useDefaultTools -> (boolean)

A Boolean indicating whether to use default simulation application tools. The default tools are rviz, rqt, terminal and rosbag record. The default is `False` .

### Warning

This API is no longer supported and will throw an error if used.

dataSources -> (list)

Specify data sources to mount read-only files from S3 into your simulation. These files are available under `/opt/robomaker/datasources/data_source_name` .

### Note

There is a limit of 100 files and a combined size of 25GB for all `DataSourceConfig` objects.

(structure)

Information about a data source.

name -> (string)

The name of the data source.

s3Bucket -> (string)

The S3 bucket where the data files are located.

s3Keys -> (list)

The list of S3 keys identifying the data source files.

(string)

type -> (string)

The data type for the data source that youâre using for your container image or simulation job. You can use this field to specify whether your data source is an Archive, an Amazon S3 prefix, or a file.

If you donât specify a field, the default value is `File` .

destination -> (string)

The location where your files are mounted in the container image.

If youâve specified the `type` of the data source as an `Archive` , you must provide an Amazon S3 object key to your archive. The object key must point to either a `.zip` or `.tar.gz` file.

If youâve specified the `type` of the data source as a `Prefix` , you provide the Amazon S3 prefix that points to the files that you are using for your data source.

If youâve specified the `type` of the data source as a `File` , you provide the Amazon S3 path to the file that youâre using as your data source.

vpcConfig -> (structure)

If your simulation job accesses resources in a VPC, you provide this parameter identifying the list of security group IDs and subnet IDs. These must belong to the same VPC. You must provide at least one security group and two subnet IDs.

subnets -> (list)

A list of one or more subnet IDs in your VPC.

(string)

securityGroups -> (list)

A list of one or more security groups IDs in your VPC.

(string)

assignPublicIp -> (boolean)

A boolean indicating whether to assign a public IP address.

compute -> (structure)

Compute information for the simulation job

simulationUnitLimit -> (integer)

The simulation unit limit. Your simulation is allocated CPU and memory proportional to the supplied simulation unit limit. A simulation unit is 1 vcpu and 2GB of memory. You are only billed for the SU utilization you consume up to the maximum value provided. The default is 15.

computeType -> (string)

Compute type information for the simulation job.

gpuUnitLimit -> (integer)

Compute GPU unit limit for the simulation job. It is the same as the number of GPUs allocated to the SimulationJob.

tags -> (map)

A map that contains tag keys and tag values that are attached to the simulation job request.

key -> (string)

value -> (string)

JSON Syntax:

```
[
  {
    "outputLocation": {
      "s3Bucket": "string",
      "s3Prefix": "string"
    },
    "loggingConfig": {
      "recordAllRosTopics": true|false
    },
    "maxJobDurationInSeconds": long,
    "iamRole": "string",
    "failureBehavior": "Fail"|"Continue",
    "useDefaultApplications": true|false,
    "robotApplications": [
      {
        "application": "string",
        "applicationVersion": "string",
        "launchConfig": {
          "packageName": "string",
          "launchFile": "string",
          "environmentVariables": {"string": "string"
            ...},
          "portForwardingConfig": {
            "portMappings": [
              {
                "jobPort": integer,
                "applicationPort": integer,
                "enableOnPublicIp": true|false
              }
              ...
            ]
          },
          "streamUI": true|false,
          "command": ["string", ...]
        },
        "uploadConfigurations": [
          {
            "name": "string",
            "path": "string",
            "uploadBehavior": "UPLOAD_ON_TERMINATE"|"UPLOAD_ROLLING_AUTO_REMOVE"
          }
          ...
        ],
        "useDefaultUploadConfigurations": true|false,
        "tools": [
          {
            "streamUI": true|false,
            "name": "string",
            "command": "string",
            "streamOutputToCloudWatch": true|false,
            "exitBehavior": "FAIL"|"RESTART"
          }
          ...
        ],
        "useDefaultTools": true|false
      }
      ...
    ],
    "simulationApplications": [
      {
        "application": "string",
        "applicationVersion": "string",
        "launchConfig": {
          "packageName": "string",
          "launchFile": "string",
          "environmentVariables": {"string": "string"
            ...},
          "portForwardingConfig": {
            "portMappings": [
              {
                "jobPort": integer,
                "applicationPort": integer,
                "enableOnPublicIp": true|false
              }
              ...
            ]
          },
          "streamUI": true|false,
          "command": ["string", ...]
        },
        "uploadConfigurations": [
          {
            "name": "string",
            "path": "string",
            "uploadBehavior": "UPLOAD_ON_TERMINATE"|"UPLOAD_ROLLING_AUTO_REMOVE"
          }
          ...
        ],
        "worldConfigs": [
          {
            "world": "string"
          }
          ...
        ],
        "useDefaultUploadConfigurations": true|false,
        "tools": [
          {
            "streamUI": true|false,
            "name": "string",
            "command": "string",
            "streamOutputToCloudWatch": true|false,
            "exitBehavior": "FAIL"|"RESTART"
          }
          ...
        ],
        "useDefaultTools": true|false
      }
      ...
    ],
    "dataSources": [
      {
        "name": "string",
        "s3Bucket": "string",
        "s3Keys": ["string", ...],
        "type": "Prefix"|"Archive"|"File",
        "destination": "string"
      }
      ...
    ],
    "vpcConfig": {
      "subnets": ["string", ...],
      "securityGroups": ["string", ...],
      "assignPublicIp": true|false
    },
    "compute": {
      "simulationUnitLimit": integer,
      "computeType": "CPU"|"GPU_AND_CPU",
      "gpuUnitLimit": integer
    },
    "tags": {"string": "string"
      ...}
  }
  ...
]
```

`--tags` (map)

A map that contains tag keys and tag values that are attached to the deployment job batch.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

arn -> (string)

The Amazon Resource Name (arn) of the batch.

status -> (string)

The status of the simulation job batch.

Pending

The simulation job batch request is pending.

InProgress

The simulation job batch is in progress.

Failed

The simulation job batch failed. One or more simulation job requests could not be completed due to an internal failure (like `InternalServiceError` ). See `failureCode` and `failureReason` for more information.

Completed

The simulation batch job completed. A batch is complete when (1) there are no pending simulation job requests in the batch and none of the failed simulation job requests are due to `InternalServiceError` and (2) when all created simulation jobs have reached a terminal state (for example, `Completed` or `Failed` ).

Canceled

The simulation batch job was cancelled.

Canceling

The simulation batch job is being cancelled.

Completing

The simulation batch job is completing.

TimingOut

The simulation job batch is timing out.

If a batch timing out, and there are pending requests that were failing due to an internal failure (like `InternalServiceError` ), the batch status will be `Failed` . If there are no such failing request, the batch status will be `TimedOut` .

TimedOut

The simulation batch job timed out.

createdAt -> (timestamp)

The time, in milliseconds since the epoch, when the simulation job batch was created.

clientRequestToken -> (string)

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

batchPolicy -> (structure)

The batch policy.

timeoutInSeconds -> (long)

The amount of time, in seconds, to wait for the batch to complete.

If a batch times out, and there are pending requests that were failing due to an internal failure (like `InternalServiceError` ), they will be moved to the failed list and the batch status will be `Failed` . If the pending requests were failing for any other reason, the failed pending requests will be moved to the failed list and the batch status will be `TimedOut` .

maxConcurrency -> (integer)

The number of active simulation jobs create as part of the batch that can be in an active state at the same time.

Active states include: `Pending` ,``Preparing`` , `Running` , `Restarting` , `RunningFailed` and `Terminating` . All other states are terminal states.

failureCode -> (string)

The failure code if the simulation job batch failed.

failureReason -> (string)

The reason the simulation job batch failed.

failedRequests -> (list)

A list of failed simulation job requests. The request failed to be created into a simulation job. Failed requests do not have a simulation job ID.

(structure)

Information about a failed create simulation job request.

request -> (structure)

The simulation job request.

outputLocation -> (structure)

The output location.

s3Bucket -> (string)

The S3 bucket for output.

s3Prefix -> (string)

The S3 folder in the `s3Bucket` where output files will be placed.

loggingConfig -> (structure)

The logging configuration.

recordAllRosTopics -> (boolean)

A boolean indicating whether to record all ROS topics.

### Warning

This API is no longer supported and will throw an error if used.

maxJobDurationInSeconds -> (long)

The maximum simulation job duration in seconds. The value must be 8 days (691,200 seconds) or less.

iamRole -> (string)

The IAM role name that allows the simulation instance to call the AWS APIs that are specified in its associated policies on your behalf. This is how credentials are passed in to your simulation job.

failureBehavior -> (string)

The failure behavior the simulation job.

Continue

Leaves the host running for its maximum timeout duration after a `4XX` error code.

Fail

Stop the simulation job and terminate the instance.

useDefaultApplications -> (boolean)

A Boolean indicating whether to use default applications in the simulation job. Default applications include Gazebo, rqt, rviz and terminal access.

robotApplications -> (list)

The robot applications to use in the simulation job.

(structure)

Application configuration information for a robot.

application -> (string)

The application information for the robot application.

applicationVersion -> (string)

The version of the robot application.

launchConfig -> (structure)

The launch configuration for the robot application.

packageName -> (string)

The package name.

launchFile -> (string)

The launch file name.

environmentVariables -> (map)

The environment variables for the application launch.

key -> (string)

value -> (string)

portForwardingConfig -> (structure)

The port forwarding configuration.

portMappings -> (list)

The port mappings for the configuration.

(structure)

An object representing a port mapping.

jobPort -> (integer)

The port number on the simulation job instance to use as a remote connection point.

applicationPort -> (integer)

The port number on the application.

enableOnPublicIp -> (boolean)

A Boolean indicating whether to enable this port mapping on public IP.

streamUI -> (boolean)

Boolean indicating whether a streaming session will be configured for the application. If `True` , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and launch the component. It must have a graphical user interface.

command -> (list)

If youâve specified `General` as the value for your `RobotSoftwareSuite` , you can use this field to specify a list of commands for your container image.

If youâve specified `SimulationRuntime` as the value for your `SimulationSoftwareSuite` , you can use this field to specify a list of commands for your container image.

(string)

uploadConfigurations -> (list)

The upload configurations for the robot application.

(structure)

Provides upload configuration information. Files are uploaded from the simulation job to a location you specify.

name -> (string)

A prefix that specifies where files will be uploaded in Amazon S3. It is appended to the simulation output location to determine the final path.

For example, if your simulation output location is `s3://amzn-s3-demo-bucket` and your upload configuration name is `robot-test` , your files will be uploaded to `s3://amzn-s3-demo-bucket/<simid>/<runid>/robot-test` .

path -> (string)

Specifies the path of the file(s) to upload. Standard Unix glob matching rules are accepted, with the addition of `**` as a *super asterisk* . For example, specifying `/var/log/**.log` causes all .log files in the `/var/log` directory tree to be collected. For more examples, see [Glob Library](https://github.com/gobwas/glob) .

uploadBehavior -> (string)

Specifies when to upload the files:

UPLOAD_ON_TERMINATE

Matching files are uploaded once the simulation enters the `TERMINATING` state. Matching files are not uploaded until all of your code (including tools) have stopped.

If there is a problem uploading a file, the upload is retried. If problems persist, no further upload attempts will be made.

UPLOAD_ROLLING_AUTO_REMOVE

Matching files are uploaded as they are created. They are deleted after they are uploaded. The specified path is checked every 5 seconds. A final check is made when all of your code (including tools) have stopped.

useDefaultUploadConfigurations -> (boolean)

A Boolean indicating whether to use default upload configurations. By default, `.ros` and `.gazebo` files are uploaded when the application terminates and all ROS topics will be recorded.

If you set this value, you must specify an `outputLocation` .

### Warning

This API is no longer supported and will throw an error if used.

tools -> (list)

Information about tools configured for the robot application.

(structure)

Information about a tool. Tools are used in a simulation job.

streamUI -> (boolean)

Boolean indicating whether a streaming session will be configured for the tool. If `True` , AWS RoboMaker will configure a connection so you can interact with the tool as it is running in the simulation. It must have a graphical user interface. The default is `False` .

name -> (string)

The name of the tool.

command -> (string)

Command-line arguments for the tool. It must include the tool executable name.

streamOutputToCloudWatch -> (boolean)

Boolean indicating whether logs will be recorded in CloudWatch for the tool. The default is `False` .

exitBehavior -> (string)

Exit behavior determines what happens when your tool quits running. `RESTART` will cause your tool to be restarted. `FAIL` will cause your job to exit. The default is `RESTART` .

useDefaultTools -> (boolean)

A Boolean indicating whether to use default robot application tools. The default tools are rviz, rqt, terminal and rosbag record. The default is `False` .

### Warning

This API is no longer supported and will throw an error if used.

simulationApplications -> (list)

The simulation applications to use in the simulation job.

(structure)

Information about a simulation application configuration.

application -> (string)

The application information for the simulation application.

applicationVersion -> (string)

The version of the simulation application.

launchConfig -> (structure)

The launch configuration for the simulation application.

packageName -> (string)

The package name.

launchFile -> (string)

The launch file name.

environmentVariables -> (map)

The environment variables for the application launch.

key -> (string)

value -> (string)

portForwardingConfig -> (structure)

The port forwarding configuration.

portMappings -> (list)

The port mappings for the configuration.

(structure)

An object representing a port mapping.

jobPort -> (integer)

The port number on the simulation job instance to use as a remote connection point.

applicationPort -> (integer)

The port number on the application.

enableOnPublicIp -> (boolean)

A Boolean indicating whether to enable this port mapping on public IP.

streamUI -> (boolean)

Boolean indicating whether a streaming session will be configured for the application. If `True` , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and launch the component. It must have a graphical user interface.

command -> (list)

If youâve specified `General` as the value for your `RobotSoftwareSuite` , you can use this field to specify a list of commands for your container image.

If youâve specified `SimulationRuntime` as the value for your `SimulationSoftwareSuite` , you can use this field to specify a list of commands for your container image.

(string)

uploadConfigurations -> (list)

Information about upload configurations for the simulation application.

(structure)

Provides upload configuration information. Files are uploaded from the simulation job to a location you specify.

name -> (string)

A prefix that specifies where files will be uploaded in Amazon S3. It is appended to the simulation output location to determine the final path.

For example, if your simulation output location is `s3://amzn-s3-demo-bucket` and your upload configuration name is `robot-test` , your files will be uploaded to `s3://amzn-s3-demo-bucket/<simid>/<runid>/robot-test` .

path -> (string)

Specifies the path of the file(s) to upload. Standard Unix glob matching rules are accepted, with the addition of `**` as a *super asterisk* . For example, specifying `/var/log/**.log` causes all .log files in the `/var/log` directory tree to be collected. For more examples, see [Glob Library](https://github.com/gobwas/glob) .

uploadBehavior -> (string)

Specifies when to upload the files:

UPLOAD_ON_TERMINATE

Matching files are uploaded once the simulation enters the `TERMINATING` state. Matching files are not uploaded until all of your code (including tools) have stopped.

If there is a problem uploading a file, the upload is retried. If problems persist, no further upload attempts will be made.

UPLOAD_ROLLING_AUTO_REMOVE

Matching files are uploaded as they are created. They are deleted after they are uploaded. The specified path is checked every 5 seconds. A final check is made when all of your code (including tools) have stopped.

worldConfigs -> (list)

A list of world configurations.

### Warning

This API is no longer supported and will throw an error if used.

(structure)

Configuration information for a world.

world -> (string)

The world generated by Simulation WorldForge.

useDefaultUploadConfigurations -> (boolean)

A Boolean indicating whether to use default upload configurations. By default, `.ros` and `.gazebo` files are uploaded when the application terminates and all ROS topics will be recorded.

If you set this value, you must specify an `outputLocation` .

### Warning

This API is no longer supported and will throw an error if used.

tools -> (list)

Information about tools configured for the simulation application.

(structure)

Information about a tool. Tools are used in a simulation job.

streamUI -> (boolean)

Boolean indicating whether a streaming session will be configured for the tool. If `True` , AWS RoboMaker will configure a connection so you can interact with the tool as it is running in the simulation. It must have a graphical user interface. The default is `False` .

name -> (string)

The name of the tool.

command -> (string)

Command-line arguments for the tool. It must include the tool executable name.

streamOutputToCloudWatch -> (boolean)

Boolean indicating whether logs will be recorded in CloudWatch for the tool. The default is `False` .

exitBehavior -> (string)

Exit behavior determines what happens when your tool quits running. `RESTART` will cause your tool to be restarted. `FAIL` will cause your job to exit. The default is `RESTART` .

useDefaultTools -> (boolean)

A Boolean indicating whether to use default simulation application tools. The default tools are rviz, rqt, terminal and rosbag record. The default is `False` .

### Warning

This API is no longer supported and will throw an error if used.

dataSources -> (list)

Specify data sources to mount read-only files from S3 into your simulation. These files are available under `/opt/robomaker/datasources/data_source_name` .

### Note

There is a limit of 100 files and a combined size of 25GB for all `DataSourceConfig` objects.

(structure)

Information about a data source.

name -> (string)

The name of the data source.

s3Bucket -> (string)

The S3 bucket where the data files are located.

s3Keys -> (list)

The list of S3 keys identifying the data source files.

(string)

type -> (string)

The data type for the data source that youâre using for your container image or simulation job. You can use this field to specify whether your data source is an Archive, an Amazon S3 prefix, or a file.

If you donât specify a field, the default value is `File` .

destination -> (string)

The location where your files are mounted in the container image.

If youâve specified the `type` of the data source as an `Archive` , you must provide an Amazon S3 object key to your archive. The object key must point to either a `.zip` or `.tar.gz` file.

If youâve specified the `type` of the data source as a `Prefix` , you provide the Amazon S3 prefix that points to the files that you are using for your data source.

If youâve specified the `type` of the data source as a `File` , you provide the Amazon S3 path to the file that youâre using as your data source.

vpcConfig -> (structure)

If your simulation job accesses resources in a VPC, you provide this parameter identifying the list of security group IDs and subnet IDs. These must belong to the same VPC. You must provide at least one security group and two subnet IDs.

subnets -> (list)

A list of one or more subnet IDs in your VPC.

(string)

securityGroups -> (list)

A list of one or more security groups IDs in your VPC.

(string)

assignPublicIp -> (boolean)

A boolean indicating whether to assign a public IP address.

compute -> (structure)

Compute information for the simulation job

simulationUnitLimit -> (integer)

The simulation unit limit. Your simulation is allocated CPU and memory proportional to the supplied simulation unit limit. A simulation unit is 1 vcpu and 2GB of memory. You are only billed for the SU utilization you consume up to the maximum value provided. The default is 15.

computeType -> (string)

Compute type information for the simulation job.

gpuUnitLimit -> (integer)

Compute GPU unit limit for the simulation job. It is the same as the number of GPUs allocated to the SimulationJob.

tags -> (map)

A map that contains tag keys and tag values that are attached to the simulation job request.

key -> (string)

value -> (string)

failureReason -> (string)

The failure reason of the simulation job request.

failureCode -> (string)

The failure code.

failedAt -> (timestamp)

The time, in milliseconds since the epoch, when the simulation job batch failed.

pendingRequests -> (list)

A list of pending simulation job requests. These requests have not yet been created into simulation jobs.

(structure)

Information about a simulation job request.

outputLocation -> (structure)

The output location.

s3Bucket -> (string)

The S3 bucket for output.

s3Prefix -> (string)

The S3 folder in the `s3Bucket` where output files will be placed.

loggingConfig -> (structure)

The logging configuration.

recordAllRosTopics -> (boolean)

A boolean indicating whether to record all ROS topics.

### Warning

This API is no longer supported and will throw an error if used.

maxJobDurationInSeconds -> (long)

The maximum simulation job duration in seconds. The value must be 8 days (691,200 seconds) or less.

iamRole -> (string)

The IAM role name that allows the simulation instance to call the AWS APIs that are specified in its associated policies on your behalf. This is how credentials are passed in to your simulation job.

failureBehavior -> (string)

The failure behavior the simulation job.

Continue

Leaves the host running for its maximum timeout duration after a `4XX` error code.

Fail

Stop the simulation job and terminate the instance.

useDefaultApplications -> (boolean)

A Boolean indicating whether to use default applications in the simulation job. Default applications include Gazebo, rqt, rviz and terminal access.

robotApplications -> (list)

The robot applications to use in the simulation job.

(structure)

Application configuration information for a robot.

application -> (string)

The application information for the robot application.

applicationVersion -> (string)

The version of the robot application.

launchConfig -> (structure)

The launch configuration for the robot application.

packageName -> (string)

The package name.

launchFile -> (string)

The launch file name.

environmentVariables -> (map)

The environment variables for the application launch.

key -> (string)

value -> (string)

portForwardingConfig -> (structure)

The port forwarding configuration.

portMappings -> (list)

The port mappings for the configuration.

(structure)

An object representing a port mapping.

jobPort -> (integer)

The port number on the simulation job instance to use as a remote connection point.

applicationPort -> (integer)

The port number on the application.

enableOnPublicIp -> (boolean)

A Boolean indicating whether to enable this port mapping on public IP.

streamUI -> (boolean)

Boolean indicating whether a streaming session will be configured for the application. If `True` , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and launch the component. It must have a graphical user interface.

command -> (list)

If youâve specified `General` as the value for your `RobotSoftwareSuite` , you can use this field to specify a list of commands for your container image.

If youâve specified `SimulationRuntime` as the value for your `SimulationSoftwareSuite` , you can use this field to specify a list of commands for your container image.

(string)

uploadConfigurations -> (list)

The upload configurations for the robot application.

(structure)

Provides upload configuration information. Files are uploaded from the simulation job to a location you specify.

name -> (string)

A prefix that specifies where files will be uploaded in Amazon S3. It is appended to the simulation output location to determine the final path.

For example, if your simulation output location is `s3://amzn-s3-demo-bucket` and your upload configuration name is `robot-test` , your files will be uploaded to `s3://amzn-s3-demo-bucket/<simid>/<runid>/robot-test` .

path -> (string)

Specifies the path of the file(s) to upload. Standard Unix glob matching rules are accepted, with the addition of `**` as a *super asterisk* . For example, specifying `/var/log/**.log` causes all .log files in the `/var/log` directory tree to be collected. For more examples, see [Glob Library](https://github.com/gobwas/glob) .

uploadBehavior -> (string)

Specifies when to upload the files:

UPLOAD_ON_TERMINATE

Matching files are uploaded once the simulation enters the `TERMINATING` state. Matching files are not uploaded until all of your code (including tools) have stopped.

If there is a problem uploading a file, the upload is retried. If problems persist, no further upload attempts will be made.

UPLOAD_ROLLING_AUTO_REMOVE

Matching files are uploaded as they are created. They are deleted after they are uploaded. The specified path is checked every 5 seconds. A final check is made when all of your code (including tools) have stopped.

useDefaultUploadConfigurations -> (boolean)

A Boolean indicating whether to use default upload configurations. By default, `.ros` and `.gazebo` files are uploaded when the application terminates and all ROS topics will be recorded.

If you set this value, you must specify an `outputLocation` .

### Warning

This API is no longer supported and will throw an error if used.

tools -> (list)

Information about tools configured for the robot application.

(structure)

Information about a tool. Tools are used in a simulation job.

streamUI -> (boolean)

Boolean indicating whether a streaming session will be configured for the tool. If `True` , AWS RoboMaker will configure a connection so you can interact with the tool as it is running in the simulation. It must have a graphical user interface. The default is `False` .

name -> (string)

The name of the tool.

command -> (string)

Command-line arguments for the tool. It must include the tool executable name.

streamOutputToCloudWatch -> (boolean)

Boolean indicating whether logs will be recorded in CloudWatch for the tool. The default is `False` .

exitBehavior -> (string)

Exit behavior determines what happens when your tool quits running. `RESTART` will cause your tool to be restarted. `FAIL` will cause your job to exit. The default is `RESTART` .

useDefaultTools -> (boolean)

A Boolean indicating whether to use default robot application tools. The default tools are rviz, rqt, terminal and rosbag record. The default is `False` .

### Warning

This API is no longer supported and will throw an error if used.

simulationApplications -> (list)

The simulation applications to use in the simulation job.

(structure)

Information about a simulation application configuration.

application -> (string)

The application information for the simulation application.

applicationVersion -> (string)

The version of the simulation application.

launchConfig -> (structure)

The launch configuration for the simulation application.

packageName -> (string)

The package name.

launchFile -> (string)

The launch file name.

environmentVariables -> (map)

The environment variables for the application launch.

key -> (string)

value -> (string)

portForwardingConfig -> (structure)

The port forwarding configuration.

portMappings -> (list)

The port mappings for the configuration.

(structure)

An object representing a port mapping.

jobPort -> (integer)

The port number on the simulation job instance to use as a remote connection point.

applicationPort -> (integer)

The port number on the application.

enableOnPublicIp -> (boolean)

A Boolean indicating whether to enable this port mapping on public IP.

streamUI -> (boolean)

Boolean indicating whether a streaming session will be configured for the application. If `True` , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and launch the component. It must have a graphical user interface.

command -> (list)

If youâve specified `General` as the value for your `RobotSoftwareSuite` , you can use this field to specify a list of commands for your container image.

If youâve specified `SimulationRuntime` as the value for your `SimulationSoftwareSuite` , you can use this field to specify a list of commands for your container image.

(string)

uploadConfigurations -> (list)

Information about upload configurations for the simulation application.

(structure)

Provides upload configuration information. Files are uploaded from the simulation job to a location you specify.

name -> (string)

A prefix that specifies where files will be uploaded in Amazon S3. It is appended to the simulation output location to determine the final path.

For example, if your simulation output location is `s3://amzn-s3-demo-bucket` and your upload configuration name is `robot-test` , your files will be uploaded to `s3://amzn-s3-demo-bucket/<simid>/<runid>/robot-test` .

path -> (string)

Specifies the path of the file(s) to upload. Standard Unix glob matching rules are accepted, with the addition of `**` as a *super asterisk* . For example, specifying `/var/log/**.log` causes all .log files in the `/var/log` directory tree to be collected. For more examples, see [Glob Library](https://github.com/gobwas/glob) .

uploadBehavior -> (string)

Specifies when to upload the files:

UPLOAD_ON_TERMINATE

Matching files are uploaded once the simulation enters the `TERMINATING` state. Matching files are not uploaded until all of your code (including tools) have stopped.

If there is a problem uploading a file, the upload is retried. If problems persist, no further upload attempts will be made.

UPLOAD_ROLLING_AUTO_REMOVE

Matching files are uploaded as they are created. They are deleted after they are uploaded. The specified path is checked every 5 seconds. A final check is made when all of your code (including tools) have stopped.

worldConfigs -> (list)

A list of world configurations.

### Warning

This API is no longer supported and will throw an error if used.

(structure)

Configuration information for a world.

world -> (string)

The world generated by Simulation WorldForge.

useDefaultUploadConfigurations -> (boolean)

A Boolean indicating whether to use default upload configurations. By default, `.ros` and `.gazebo` files are uploaded when the application terminates and all ROS topics will be recorded.

If you set this value, you must specify an `outputLocation` .

### Warning

This API is no longer supported and will throw an error if used.

tools -> (list)

Information about tools configured for the simulation application.

(structure)

Information about a tool. Tools are used in a simulation job.

streamUI -> (boolean)

Boolean indicating whether a streaming session will be configured for the tool. If `True` , AWS RoboMaker will configure a connection so you can interact with the tool as it is running in the simulation. It must have a graphical user interface. The default is `False` .

name -> (string)

The name of the tool.

command -> (string)

Command-line arguments for the tool. It must include the tool executable name.

streamOutputToCloudWatch -> (boolean)

Boolean indicating whether logs will be recorded in CloudWatch for the tool. The default is `False` .

exitBehavior -> (string)

Exit behavior determines what happens when your tool quits running. `RESTART` will cause your tool to be restarted. `FAIL` will cause your job to exit. The default is `RESTART` .

useDefaultTools -> (boolean)

A Boolean indicating whether to use default simulation application tools. The default tools are rviz, rqt, terminal and rosbag record. The default is `False` .

### Warning

This API is no longer supported and will throw an error if used.

dataSources -> (list)

Specify data sources to mount read-only files from S3 into your simulation. These files are available under `/opt/robomaker/datasources/data_source_name` .

### Note

There is a limit of 100 files and a combined size of 25GB for all `DataSourceConfig` objects.

(structure)

Information about a data source.

name -> (string)

The name of the data source.

s3Bucket -> (string)

The S3 bucket where the data files are located.

s3Keys -> (list)

The list of S3 keys identifying the data source files.

(string)

type -> (string)

The data type for the data source that youâre using for your container image or simulation job. You can use this field to specify whether your data source is an Archive, an Amazon S3 prefix, or a file.

If you donât specify a field, the default value is `File` .

destination -> (string)

The location where your files are mounted in the container image.

If youâve specified the `type` of the data source as an `Archive` , you must provide an Amazon S3 object key to your archive. The object key must point to either a `.zip` or `.tar.gz` file.

If youâve specified the `type` of the data source as a `Prefix` , you provide the Amazon S3 prefix that points to the files that you are using for your data source.

If youâve specified the `type` of the data source as a `File` , you provide the Amazon S3 path to the file that youâre using as your data source.

vpcConfig -> (structure)

If your simulation job accesses resources in a VPC, you provide this parameter identifying the list of security group IDs and subnet IDs. These must belong to the same VPC. You must provide at least one security group and two subnet IDs.

subnets -> (list)

A list of one or more subnet IDs in your VPC.

(string)

securityGroups -> (list)

A list of one or more security groups IDs in your VPC.

(string)

assignPublicIp -> (boolean)

A boolean indicating whether to assign a public IP address.

compute -> (structure)

Compute information for the simulation job

simulationUnitLimit -> (integer)

The simulation unit limit. Your simulation is allocated CPU and memory proportional to the supplied simulation unit limit. A simulation unit is 1 vcpu and 2GB of memory. You are only billed for the SU utilization you consume up to the maximum value provided. The default is 15.

computeType -> (string)

Compute type information for the simulation job.

gpuUnitLimit -> (integer)

Compute GPU unit limit for the simulation job. It is the same as the number of GPUs allocated to the SimulationJob.

tags -> (map)

A map that contains tag keys and tag values that are attached to the simulation job request.

key -> (string)

value -> (string)

createdRequests -> (list)

A list of created simulation job request summaries.

(structure)

Summary information for a simulation job.

arn -> (string)

The Amazon Resource Name (ARN) of the simulation job.

lastUpdatedAt -> (timestamp)

The time, in milliseconds since the epoch, when the simulation job was last updated.

name -> (string)

The name of the simulation job.

status -> (string)

The status of the simulation job.

simulationApplicationNames -> (list)

A list of simulation job simulation application names.

(string)

robotApplicationNames -> (list)

A list of simulation job robot application names.

(string)

dataSourceNames -> (list)

The names of the data sources.

(string)

computeType -> (string)

The compute type for the simulation job summary.

tags -> (map)

A map that contains tag keys and tag values that are attached to the deployment job batch.

key -> (string)

value -> (string)