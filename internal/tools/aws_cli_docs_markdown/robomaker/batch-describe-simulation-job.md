# batch-describe-simulation-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/batch-describe-simulation-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/batch-describe-simulation-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [robomaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/index.html#cli-aws-robomaker) ]

# batch-describe-simulation-job

## Description

### Warning

End of support notice: On September 10, 2025, Amazon Web Services will discontinue support for Amazon Web Services RoboMaker. After September 10, 2025, you will no longer be able to access the Amazon Web Services RoboMaker console or Amazon Web Services RoboMaker resources. For more information on transitioning to Batch to help run containerized simulations, visit [https://aws.amazon.com/blogs/hpc/run-simulations-using-multiple-containers-in-a-single-aws-batch-job/](https://aws.amazon.com/blogs/hpc/run-simulations-using-multiple-containers-in-a-single-aws-batch-job/) .

Describes one or more simulation jobs.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/BatchDescribeSimulationJob)

## Synopsis

```
batch-describe-simulation-job
--jobs <value>
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

`--jobs` (list)

A list of Amazon Resource Names (ARNs) of simulation jobs to describe.

(string)

Syntax:

```
"string" "string" ...
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

**To batch describe simulation jobs**

The following `batch-describe-simulation-job` example retrieves details for the three specified simulation jobs.

Command:

```
aws robomaker batch-describe-simulation-job \
--job arn:aws:robomaker:us-west-2:111111111111:simulation-job/sim-66bbb3gpxm8x arn:aws:robomaker:us-west-2:111111111111:simulation-job/sim-p0cpdrrwng2n arn:aws:robomaker:us-west-2:111111111111:simulation-job/sim-g8h6tglmblgw
```

Output:

```
{
    "jobs": [
        {
            "arn": "arn:aws:robomaker:us-west-2:111111111111:simulation-job/sim-66bbb3gpxm8x",
            "status": "Completed",
            "lastUpdatedAt": 1548959178.0,
            "failureBehavior": "Continue",
            "clientRequestToken": "6020408e-b05c-4310-9f13-4ed71c5221ed",
            "outputLocation": {
                "s3Bucket": "awsrobomakerobjecttracker-111111111-bundlesbucket-2lk584kiq1oa",
                "s3Prefix": "output"
            },
            "maxJobDurationInSeconds": 3600,
            "simulationTimeMillis": 0,
            "iamRole": "arn:aws:iam::111111111111:role/AWSRoboMakerObjectTracker-154895-SimulationJobRole-14D5ASA7PQE3A",
            "simulationApplications": [
                {
                    "application": "arn:aws:robomaker:us-west-2:111111111111:simulation-application/AWSRoboMakerObjectTracker-1548959046124_NPvyfcatq/1548959170096",
                    "applicationVersion": "$LATEST",
                    "launchConfig": {
                        "packageName": "object_tracker_simulation",
                        "launchFile": "local_training.launch",
                        "environmentVariables": {
                            "MARKOV_PRESET_FILE": "object_tracker.py",
                            "MODEL_S3_BUCKET": "awsrobomakerobjecttracker-111111111-bundlesbucket-2lk584kiq1oa",
                            "MODEL_S3_PREFIX": "model-store",
                            "ROS_AWS_REGION": "us-west-2"
                        }
                    }
                }
            ],
            "tags": {},
            "vpcConfig": {
                "subnets": [
                    "subnet-716dd52a",
                    "subnet-43c22325",
                    "subnet-3f526976"
                ],
                "securityGroups": [
                    "sg-3fb40545"
                ],
                "vpcId": "vpc-99895eff",
                "assignPublicIp": true
            }
        },
        {
            "arn": "arn:aws:robomaker:us-west-2:111111111111:simulation-job/sim-p0cpdrrwng2n",
            "status": "Completed",
            "lastUpdatedAt": 1548168817.0,
            "failureBehavior": "Continue",
            "clientRequestToken": "e4a23e75-f9a7-411d-835f-21881c82c58b",
            "outputLocation": {
                "s3Bucket": "awsrobomakercloudwatch-111111111111-bundlesbucket-14e5s9jvwtmv7",
                "s3Prefix": "output"
            },
            "maxJobDurationInSeconds": 3600,
            "simulationTimeMillis": 0,
            "iamRole": "arn:aws:iam::111111111111:role/AWSRoboMakerCloudWatch-154766341-SimulationJobRole-G0OBWTQ8YBG6",
            "robotApplications": [
                {
                    "application": "arn:aws:robomaker:us-west-2:111111111111:robot-application/AWSRoboMakerCloudWatch-1547663411642_NZbpqEJ3T/1547663517377",
                    "applicationVersion": "$LATEST",
                    "launchConfig": {
                        "packageName": "cloudwatch_robot",
                        "launchFile": "await_commands.launch",
                        "environmentVariables": {
                            "LAUNCH_ID": "1548168752173",
                            "ROS_AWS_REGION": "us-west-2"
                        }
                    }
                }
            ],
            "simulationApplications": [
                {
                    "application": "arn:aws:robomaker:us-west-2:111111111111:simulation-application/AWSRoboMakerCloudWatch-1547663411642_0LIt6D1h6/1547663521470",
                    "applicationVersion": "$LATEST",
                    "launchConfig": {
                        "packageName": "cloudwatch_simulation",
                        "launchFile": "bookstore_turtlebot_navigation.launch",
                        "environmentVariables": {
                            "LAUNCH_ID": "1548168752173",
                            "ROS_AWS_REGION": "us-west-2",
                            "TURTLEBOT3_MODEL": "waffle_pi"
                        }
                    }
                }
            ],
            "tags": {},
            "vpcConfig": {
                "subnets": [
                    "subnet-716dd52a",
                    "subnet-43c22325",
                    "subnet-3f526976"
                ],
                "securityGroups": [
                    "sg-3fb40545"
                ],
                "vpcId": "vpc-99895eff",
                "assignPublicIp": true
            }
        },
        {
            "arn": "arn:aws:robomaker:us-west-2:111111111111:simulation-job/sim-g8h6tglmblgw",
            "status": "Canceled",
            "lastUpdatedAt": 1546543442.0,
            "failureBehavior": "Fail",
            "clientRequestToken": "d796bbb4-2a2c-1abc-f2a9-0d9e547d853f",
            "outputLocation": {
                "s3Bucket": "sample-bucket",
                "s3Prefix": "SimulationLog_115490482698"
            },
            "maxJobDurationInSeconds": 28800,
            "simulationTimeMillis": 0,
            "iamRole": "arn:aws:iam::111111111111:role/RoboMakerSampleTheFirst",
            "robotApplications": [
                {
                    "application": "arn:aws:robomaker:us-west-2:111111111111:robot-application/RoboMakerHelloWorldRobot/1546541208251",
                    "applicationVersion": "$LATEST",
                    "launchConfig": {
                        "packageName": "hello_world_robot",
                        "launchFile": "rotate.launch"
                    }
                }
            ],
            "simulationApplications": [
                {
                    "application": "arn:aws:robomaker:us-west-2:111111111111:simulation-application/RoboMakerHelloWorldSimulation/1546541198985",
                    "applicationVersion": "$LATEST",
                    "launchConfig": {
                        "packageName": "hello_world_simulation",
                        "launchFile": "empty_world.launch"
                    }
                }
            ],
            "tags": {}
        }
    ],
    "unprocessedJobs": []
}
```

## Output

jobs -> (list)

A list of simulation jobs.

(structure)

Information about a simulation job.

arn -> (string)

The Amazon Resource Name (ARN) of the simulation job.

name -> (string)

The name of the simulation job.

status -> (string)

Status of the simulation job.

lastStartedAt -> (timestamp)

The time, in milliseconds since the epoch, when the simulation job was last started.

lastUpdatedAt -> (timestamp)

The time, in milliseconds since the epoch, when the simulation job was last updated.

failureBehavior -> (string)

The failure behavior the simulation job.

Continue

Leaves the host running for its maximum timeout duration after a `4XX` error code.

Fail

Stop the simulation job and terminate the instance.

failureCode -> (string)

The failure code of the simulation job if it failed.

failureReason -> (string)

The reason why the simulation job failed.

clientRequestToken -> (string)

A unique identifier for this `SimulationJob` request.

outputLocation -> (structure)

Location for output files generated by the simulation job.

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

simulationTimeMillis -> (long)

The simulation job execution duration in milliseconds.

iamRole -> (string)

The IAM role that allows the simulation instance to call the AWS APIs that are specified in its associated policies on your behalf. This is how credentials are passed in to your simulation job.

robotApplications -> (list)

A list of robot applications.

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

A list of simulation applications.

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

The data sources for the simulation job.

(structure)

Information about a data source.

name -> (string)

The name of the data source.

s3Bucket -> (string)

The S3 bucket where the data files are located.

s3Keys -> (list)

The list of S3 keys identifying the data source files.

(structure)

Information about S3 keys.

s3Key -> (string)

The S3 key.

etag -> (string)

The etag for the object.

type -> (string)

The data type for the data source that youâre using for your container image or simulation job. You can use this field to specify whether your data source is an Archive, an Amazon S3 prefix, or a file.

If you donât specify a field, the default value is `File` .

destination -> (string)

The location where your files are mounted in the container image.

If youâve specified the `type` of the data source as an `Archive` , you must provide an Amazon S3 object key to your archive. The object key must point to either a `.zip` or `.tar.gz` file.

If youâve specified the `type` of the data source as a `Prefix` , you provide the Amazon S3 prefix that points to the files that you are using for your data source.

If youâve specified the `type` of the data source as a `File` , you provide the Amazon S3 path to the file that youâre using as your data source.

tags -> (map)

A map that contains tag keys and tag values that are attached to the simulation job.

key -> (string)

value -> (string)

vpcConfig -> (structure)

VPC configuration information.

subnets -> (list)

A list of subnet IDs associated with the simulation job.

(string)

securityGroups -> (list)

A list of security group IDs associated with the simulation job.

(string)

vpcId -> (string)

The VPC ID associated with your simulation job.

assignPublicIp -> (boolean)

A boolean indicating if a public IP was assigned.

networkInterface -> (structure)

Information about a network interface.

networkInterfaceId -> (string)

The ID of the network interface.

privateIpAddress -> (string)

The IPv4 address of the network interface within the subnet.

publicIpAddress -> (string)

The IPv4 public address of the network interface.

compute -> (structure)

Compute information for the simulation job

simulationUnitLimit -> (integer)

The simulation unit limit. Your simulation is allocated CPU and memory proportional to the supplied simulation unit limit. A simulation unit is 1 vcpu and 2GB of memory. You are only billed for the SU utilization you consume up to the maximum value provided. The default is 15.

computeType -> (string)

Compute type response information for the simulation job.

gpuUnitLimit -> (integer)

Compute GPU unit limit for the simulation job. It is the same as the number of GPUs allocated to the SimulationJob.

unprocessedJobs -> (list)

A list of unprocessed simulation job Amazon Resource Names (ARNs).

(string)