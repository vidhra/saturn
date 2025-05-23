# compose-environmentsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/compose-environments.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/compose-environments.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticbeanstalk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/index.html#cli-aws-elasticbeanstalk) ]

# compose-environments

## Description

Create or update a group of environments that each run a separate component of a single application. Takes a list of version labels that specify application source bundles for each of the environments to create or update. The name of each environment and other required information must be included in the source bundles in an environment manifest named `env.yaml` . See [Compose Environments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-mgmt-compose.html) for details.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/ComposeEnvironments)

## Synopsis

```
compose-environments
[--application-name <value>]
[--group-name <value>]
[--version-labels <value>]
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

`--application-name` (string)

The name of the application to which the specified source bundles belong.

`--group-name` (string)

The name of the group to which the target environments belong. Specify a group name only if the environment name defined in each target environmentâs manifest ends with a + (plus) character. See [Environment Manifest (env.yaml)](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html) for details.

`--version-labels` (list)

A list of version labels, specifying one or more application source bundles that belong to the target application. Each source bundle must include an environment manifest that specifies the name of the environment and the name of the solution stack to use, and optionally can specify environment links to create.

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

## Output

Environments -> (list)

Returns an  EnvironmentDescription list.

(structure)

Describes the properties of an environment.

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

NextToken -> (string)

In a paginated request, the token that you can pass in a subsequent request to get the next response page.