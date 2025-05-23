# update-simulation-applicationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/update-simulation-application.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/update-simulation-application.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [robomaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/index.html#cli-aws-robomaker) ]

# update-simulation-application

## Description

### Warning

End of support notice: On September 10, 2025, Amazon Web Services will discontinue support for Amazon Web Services RoboMaker. After September 10, 2025, you will no longer be able to access the Amazon Web Services RoboMaker console or Amazon Web Services RoboMaker resources. For more information on transitioning to Batch to help run containerized simulations, visit [https://aws.amazon.com/blogs/hpc/run-simulations-using-multiple-containers-in-a-single-aws-batch-job/](https://aws.amazon.com/blogs/hpc/run-simulations-using-multiple-containers-in-a-single-aws-batch-job/) .

Updates a simulation application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/UpdateSimulationApplication)

## Synopsis

```
update-simulation-application
--application <value>
[--sources <value>]
--simulation-software-suite <value>
--robot-software-suite <value>
[--rendering-engine <value>]
[--current-revision-id <value>]
[--environment <value>]
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

`--application` (string)

The application information for the simulation application.

`--sources` (list)

The sources of the simulation application.

(structure)

Information about a source configuration.

s3Bucket -> (string)

The Amazon S3 bucket name.

s3Key -> (string)

The s3 object key.

architecture -> (string)

The target processor architecture for the application.

Shorthand Syntax:

```
s3Bucket=string,s3Key=string,architecture=string ...
```

JSON Syntax:

```
[
  {
    "s3Bucket": "string",
    "s3Key": "string",
    "architecture": "X86_64"|"ARM64"|"ARMHF"
  }
  ...
]
```

`--simulation-software-suite` (structure)

The simulation software suite used by the simulation application.

name -> (string)

The name of the simulation software suite. `SimulationRuntime` is the only supported value.

version -> (string)

The version of the simulation software suite. Not applicable for `SimulationRuntime` .

Shorthand Syntax:

```
name=string,version=string
```

JSON Syntax:

```
{
  "name": "Gazebo"|"RosbagPlay"|"SimulationRuntime",
  "version": "string"
}
```

`--robot-software-suite` (structure)

Information about the robot software suite.

name -> (string)

The name of the robot software suite. `General` is the only supported value.

version -> (string)

The version of the robot software suite. Not applicable for General software suite.

Shorthand Syntax:

```
name=string,version=string
```

JSON Syntax:

```
{
  "name": "ROS"|"ROS2"|"General",
  "version": "Kinetic"|"Melodic"|"Dashing"|"Foxy"
}
```

`--rendering-engine` (structure)

The rendering engine for the simulation application.

name -> (string)

The name of the rendering engine.

version -> (string)

The version of the rendering engine.

Shorthand Syntax:

```
name=string,version=string
```

JSON Syntax:

```
{
  "name": "OGRE",
  "version": "string"
}
```

`--current-revision-id` (string)

The revision id for the robot application.

`--environment` (structure)

The object that contains the Docker image URI for your simulation application.

uri -> (string)

The Docker image URI for either your robot or simulation applications.

Shorthand Syntax:

```
uri=string
```

JSON Syntax:

```
{
  "uri": "string"
}
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

**To update a simulation application**

This example updates a simulation application.

Command:

```
aws robomaker update-simulation-application --application arn:aws:robomaker:us-west-2:111111111111:simulation-application/MySimulationApplication/1551203427605 --sources s3Bucket=amzn-s3-demo-bucket,s3Key=my-simulation-application.tar.gz,architecture=X86_64 --robot-software-suite name=ROS,version=Kinetic --simulation-software-suite name=Gazebo,version=7 --rendering-engine name=OGRE,version=1.x
```

Output:

```
{
  "arn": "arn:aws:robomaker:us-west-2:111111111111:simulation-application/MySimulationApplication/1551203427605",
  "name": "MySimulationApplication",
  "version": "$LATEST",
  "sources": [
      {
          "s3Bucket": "amzn-s3-demo-bucket",
          "s3Key": "my-simulation-application.tar.gz",
          "architecture": "X86_64"
      }
  ],
  "simulationSoftwareSuite": {
      "name": "Gazebo",
      "version": "7"
  },
  "robotSoftwareSuite": {
      "name": "ROS",
      "version": "Kinetic"
  },
  "renderingEngine": {
      "name": "OGRE",
      "version": "1.x"
  },
  "lastUpdatedAt": 1551289361.0,
  "revisionId": "4a22cb5d-93c5-4cef-9311-52bdd119b79e"
}
```

## Output

arn -> (string)

The Amazon Resource Name (ARN) of the updated simulation application.

name -> (string)

The name of the simulation application.

version -> (string)

The version of the robot application.

sources -> (list)

The sources of the simulation application.

(structure)

Information about a source.

s3Bucket -> (string)

The s3 bucket name.

s3Key -> (string)

The s3 object key.

etag -> (string)

A hash of the object specified by `s3Bucket` and `s3Key` .

architecture -> (string)

The taget processor architecture for the application.

simulationSoftwareSuite -> (structure)

The simulation software suite used by the simulation application.

name -> (string)

The name of the simulation software suite. `SimulationRuntime` is the only supported value.

version -> (string)

The version of the simulation software suite. Not applicable for `SimulationRuntime` .

robotSoftwareSuite -> (structure)

Information about the robot software suite.

name -> (string)

The name of the robot software suite. `General` is the only supported value.

version -> (string)

The version of the robot software suite. Not applicable for General software suite.

renderingEngine -> (structure)

The rendering engine for the simulation application.

name -> (string)

The name of the rendering engine.

version -> (string)

The version of the rendering engine.

lastUpdatedAt -> (timestamp)

The time, in milliseconds since the epoch, when the simulation application was last updated.

revisionId -> (string)

The revision id of the simulation application.

environment -> (structure)

The object that contains the Docker image URI used for your simulation application.

uri -> (string)

The Docker image URI for either your robot or simulation applications.