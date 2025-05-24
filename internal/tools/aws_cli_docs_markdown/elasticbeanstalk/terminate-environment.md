# terminate-environmentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/terminate-environment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/terminate-environment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticbeanstalk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/index.html#cli-aws-elasticbeanstalk) ]

# terminate-environment

## Description

Terminates the specified environment.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/TerminateEnvironment)

## Synopsis

```
terminate-environment
[--environment-id <value>]
[--environment-name <value>]
[--terminate-resources | --no-terminate-resources]
[--force-terminate | --no-force-terminate]
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

`--environment-id` (string)

The ID of the environment to terminate.

Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns `MissingRequiredParameter` error.

`--environment-name` (string)

The name of the environment to terminate.

Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns `MissingRequiredParameter` error.

`--terminate-resources` | `--no-terminate-resources` (boolean)

Indicates whether the associated AWS resources should shut down when the environment is terminated:

- `true` : The specified environment as well as the associated AWS resources, such as Auto Scaling group and LoadBalancer, are terminated.
- `false` : AWS Elastic Beanstalk resource management is removed from the environment, but the AWS resources continue to operate.

For more information, see the [AWS Elastic Beanstalk User Guide.](https://docs.aws.amazon.com/elasticbeanstalk/latest/ug/)

Default: `true`

Valid Values: `true` | `false`

`--force-terminate` | `--no-force-terminate` (boolean)

Terminates the target environment even if another environment in the same group is dependent on it.

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

**To terminate an environment**

The following command terminates an Elastic Beanstalk environment named `my-env`:

```
aws elasticbeanstalk terminate-environment --environment-name my-env
```

Output:

```
{
    "ApplicationName": "my-app",
    "EnvironmentName": "my-env",
    "Status": "Terminating",
    "EnvironmentId": "e-fh2eravpns",
    "EndpointURL": "awseb-e-f-AWSEBLoa-1I9XUMP4-8492WNUP202574.us-west-2.elb.amazonaws.com",
    "SolutionStackName": "64bit Amazon Linux 2015.03 v2.0.0 running Tomcat 8 Java 8",
    "CNAME": "my-env.elasticbeanstalk.com",
    "Health": "Grey",
    "AbortableOperationInProgress": false,
    "Tier": {
        "Version": " ",
        "Type": "Standard",
        "Name": "WebServer"
    },
    "DateUpdated": "2015-08-12T19:05:54.744Z",
    "DateCreated": "2015-08-12T18:52:53.622Z"
}
```

## Output

EnvironmentName -> (string)

The name of this environment.

EnvironmentId -> (string)

The ID of this environment.

ApplicationName -> (string)

The name of the application associated with this environment.

VersionLabel -> (string)

The application version deployed in this environment.

SolutionStackName -> (string)

The name of the `SolutionStack` deployed with this environment.

PlatformArn -> (string)

The ARN of the platform version.

TemplateName -> (string)

The name of the configuration template used to originally launch this environment.

Description -> (string)

Describes this environment.

EndpointURL -> (string)

For load-balanced, autoscaling environments, the URL to the LoadBalancer. For single-instance environments, the IP address of the instance.

CNAME -> (string)

The URL to the CNAME for this environment.

DateCreated -> (timestamp)

The creation date for this environment.

DateUpdated -> (timestamp)

The last modified date for this environment.

Status -> (string)

The current operational status of the environment:

- `Launching` : Environment is in the process of initial deployment.
- `Updating` : Environment is in the process of updating its configuration settings or application version.
- `Ready` : Environment is available to have an action performed on it, such as update or terminate.
- `Terminating` : Environment is in the shut-down process.
- `Terminated` : Environment is not running.

AbortableOperationInProgress -> (boolean)

Indicates if there is an in-progress environment configuration update or application version deployment that you can cancel.

`true:` There is an update in progress.

`false:` There are no updates currently in progress.

Health -> (string)

Describes the health status of the environment. AWS Elastic Beanstalk indicates the failure levels for a running environment:

- `Red` : Indicates the environment is not responsive. Occurs when three or more consecutive failures occur for an environment.
- `Yellow` : Indicates that something is wrong. Occurs when two consecutive failures occur for an environment.
- `Green` : Indicates the environment is healthy and fully functional.
- `Grey` : Default health for a new environment. The environment is not fully launched and health checks have not started or health checks are suspended during an `UpdateEnvironment` or `RestartEnvironment` request.

Default: `Grey`

HealthStatus -> (string)

Returns the health status of the application running in your environment. For more information, see [Health Colors and Statuses](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html) .

Resources -> (structure)

The description of the AWS resources used by this environment.

LoadBalancer -> (structure)

Describes the LoadBalancer.

LoadBalancerName -> (string)

The name of the LoadBalancer.

Domain -> (string)

The domain name of the LoadBalancer.

Listeners -> (list)

A list of Listeners used by the LoadBalancer.

(structure)

Describes the properties of a Listener for the LoadBalancer.

Protocol -> (string)

The protocol that is used by the Listener.

Port -> (integer)

The port that is used by the Listener.

Tier -> (structure)

Describes the current tier of this environment.

Name -> (string)

The name of this environment tier.

Valid values:

- For *Web server tier* â `WebServer`
- For *Worker tier* â `Worker`

Type -> (string)

The type of this environment tier.

Valid values:

- For *Web server tier* â `Standard`
- For *Worker tier* â `SQS/HTTP`

Version -> (string)

The version of this environment tier. When you donât set a value to it, Elastic Beanstalk uses the latest compatible worker tier version.

### Note

This member is deprecated. Any specific version that you set may become out of date. We recommend leaving it unspecified.

EnvironmentLinks -> (list)

A list of links to other environments in the same group.

(structure)

A link to another environment, defined in the environmentâs manifest. Links provide connection information in system properties that can be used to connect to another environment in the same group. See [Environment Manifest (env.yaml)](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html) for details.

LinkName -> (string)

The name of the link.

EnvironmentName -> (string)

The name of the linked environment (the dependency).

EnvironmentArn -> (string)

The environmentâs Amazon Resource Name (ARN), which can be used in other API requests that require an ARN.

OperationsRole -> (string)

The Amazon Resource Name (ARN) of the environmentâs operations role. For more information, see [Operations roles](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/iam-operationsrole.html) in the *AWS Elastic Beanstalk Developer Guide* .