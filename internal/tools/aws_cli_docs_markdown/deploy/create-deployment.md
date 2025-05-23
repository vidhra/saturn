# create-deploymentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-deployment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-deployment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [deploy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/index.html#cli-aws-deploy) ]

# create-deployment

## Description

Deploys an application revision through the specified deployment group.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/CreateDeployment)

## Synopsis

```
create-deployment
--application-name <value>
[--deployment-group-name <value>]
[--revision <value>]
[--deployment-config-name <value>]
[--description <value>]
[--ignore-application-stop-failures | --no-ignore-application-stop-failures]
[--target-instances <value>]
[--auto-rollback-configuration <value>]
[--update-outdated-instances-only | --no-update-outdated-instances-only]
[--file-exists-behavior <value>]
[--override-alarm-configuration <value>]
[--s3-location <value>]
[--github-location <value>]
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

The name of an CodeDeploy application associated with the user or Amazon Web Services account.

`--deployment-group-name` (string)

The name of the deployment group.

`--revision` (structure)

The type and location of the revision to deploy.

revisionType -> (string)

The type of application revision:

- S3: An application revision stored in Amazon S3.
- GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
- String: A YAML-formatted or JSON-formatted string (Lambda deployments only).
- AppSpecContent: An `AppSpecContent` object that contains the contents of an AppSpec file for an Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.

s3Location -> (structure)

Information about the location of a revision stored in Amazon S3.

bucket -> (string)

The name of the Amazon S3 bucket where the application revision is stored.

key -> (string)

The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

bundleType -> (string)

The file type of the application revision. Must be one of the following:

- `tar` : A tar archive file.
- `tgz` : A compressed tar archive file.
- `zip` : A zip archive file.
- `YAML` : A YAML-formatted file.
- `JSON` : A JSON-formatted file.

version -> (string)

A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.

If the version is not specified, the system uses the most recent version by default.

eTag -> (string)

The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.

If the ETag is not specified as an input parameter, ETag validation of the object is skipped.

gitHubLocation -> (structure)

Information about the location of application artifacts stored in GitHub.

repository -> (string)

The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.

Specified as account/repository.

commitId -> (string)

The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.

string -> (structure)

Information about the location of an Lambda deployment revision stored as a RawString.

content -> (string)

The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

sha256 -> (string)

The SHA256 hash value of the revision content.

appSpecContent -> (structure)

The content of an AppSpec file for an Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString.

content -> (string)

The YAML-formatted or JSON-formatted revision string.

For an Lambda deployment, the content includes a Lambda function name, the alias for its original version, and the alias for its replacement version. The deployment shifts traffic from the original version of the Lambda function to the replacement version.

For an Amazon ECS deployment, the content includes the task name, information about the load balancer that serves traffic to the container, and more.

For both types of deployments, the content can specify Lambda functions that run at specified hooks, such as `BeforeInstall` , during a deployment.

sha256 -> (string)

The SHA256 hash value of the revision content.

Shorthand Syntax:

```
revisionType=string,s3Location={bucket=string,key=string,bundleType=string,version=string,eTag=string},gitHubLocation={repository=string,commitId=string},string={content=string,sha256=string},appSpecContent={content=string,sha256=string}
```

JSON Syntax:

```
{
  "revisionType": "S3"|"GitHub"|"String"|"AppSpecContent",
  "s3Location": {
    "bucket": "string",
    "key": "string",
    "bundleType": "tar"|"tgz"|"zip"|"YAML"|"JSON",
    "version": "string",
    "eTag": "string"
  },
  "gitHubLocation": {
    "repository": "string",
    "commitId": "string"
  },
  "string": {
    "content": "string",
    "sha256": "string"
  },
  "appSpecContent": {
    "content": "string",
    "sha256": "string"
  }
}
```

`--deployment-config-name` (string)

The name of a deployment configuration associated with the user or Amazon Web Services account.

If not specified, the value configured in the deployment group is used as the default. If the deployment group does not have a deployment configuration associated with it, `CodeDeployDefault` .``OneAtATime`` is used by default.

`--description` (string)

A comment about the deployment.

`--ignore-application-stop-failures` | `--no-ignore-application-stop-failures` (boolean)

If true, then if an `ApplicationStop` , `BeforeBlockTraffic` , or `AfterBlockTraffic` deployment lifecycle event to an instance fails, then the deployment continues to the next deployment lifecycle event. For example, if `ApplicationStop` fails, the deployment continues with `DownloadBundle` . If `BeforeBlockTraffic` fails, the deployment continues with `BlockTraffic` . If `AfterBlockTraffic` fails, the deployment continues with `ApplicationStop` .

If false or not specified, then if a lifecycle event fails during a deployment to an instance, that deployment fails. If deployment to that instance is part of an overall deployment and the number of healthy hosts is not less than the minimum number of healthy hosts, then a deployment to the next instance is attempted.

During a deployment, the CodeDeploy agent runs the scripts specified for `ApplicationStop` , `BeforeBlockTraffic` , and `AfterBlockTraffic` in the AppSpec file from the previous successful deployment. (All other scripts are run from the AppSpec file in the current deployment.) If one of these scripts contains an error and does not run successfully, the deployment can fail.

If the cause of the failure is a script from the last successful deployment that will never run successfully, create a new deployment and use `ignoreApplicationStopFailures` to specify that the `ApplicationStop` , `BeforeBlockTraffic` , and `AfterBlockTraffic` failures should be ignored.

`--target-instances` (structure)

Information about the instances that belong to the replacement environment in a blue/green deployment.

tagFilters -> (list)

The tag filter key, type, and value used to identify Amazon EC2 instances in a replacement environment for a blue/green deployment. Cannot be used in the same call as `ec2TagSet` .

(structure)

Information about an EC2 tag filter.

Key -> (string)

The tag filter key.

Value -> (string)

The tag filter value.

Type -> (string)

The tag filter type:

- `KEY_ONLY` : Key only.
- `VALUE_ONLY` : Value only.
- `KEY_AND_VALUE` : Key and value.

autoScalingGroups -> (list)

The names of one or more Auto Scaling groups to identify a replacement environment for a blue/green deployment.

(string)

ec2TagSet -> (structure)

Information about the groups of Amazon EC2 instance tags that an instance must be identified by in order for it to be included in the replacement environment for a blue/green deployment. Cannot be used in the same call as `tagFilters` .

ec2TagSetList -> (list)

A list that contains other lists of Amazon EC2 instance tag groups. For an instance to be included in the deployment group, it must be identified by all of the tag groups in the list.

(list)

(structure)

Information about an EC2 tag filter.

Key -> (string)

The tag filter key.

Value -> (string)

The tag filter value.

Type -> (string)

The tag filter type:

- `KEY_ONLY` : Key only.
- `VALUE_ONLY` : Value only.
- `KEY_AND_VALUE` : Key and value.

JSON Syntax:

```
{
  "tagFilters": [
    {
      "Key": "string",
      "Value": "string",
      "Type": "KEY_ONLY"|"VALUE_ONLY"|"KEY_AND_VALUE"
    }
    ...
  ],
  "autoScalingGroups": ["string", ...],
  "ec2TagSet": {
    "ec2TagSetList": [
      [
        {
          "Key": "string",
          "Value": "string",
          "Type": "KEY_ONLY"|"VALUE_ONLY"|"KEY_AND_VALUE"
        }
        ...
      ]
      ...
    ]
  }
}
```

`--auto-rollback-configuration` (structure)

Configuration information for an automatic rollback that is added when a deployment is created.

enabled -> (boolean)

Indicates whether a defined automatic rollback configuration is currently enabled.

events -> (list)

The event type or types that trigger a rollback.

(string)

Shorthand Syntax:

```
enabled=boolean,events=string,string
```

JSON Syntax:

```
{
  "enabled": true|false,
  "events": ["DEPLOYMENT_FAILURE"|"DEPLOYMENT_STOP_ON_ALARM"|"DEPLOYMENT_STOP_ON_REQUEST", ...]
}
```

`--update-outdated-instances-only` | `--no-update-outdated-instances-only` (boolean)

Indicates whether to deploy to all instances or only to instances that are not running the latest application revision.

`--file-exists-behavior` (string)

Information about how CodeDeploy handles files that already exist in a deployment target location but werenât part of the previous successful deployment.

The `fileExistsBehavior` parameter takes any of the following values:

- DISALLOW: The deployment fails. This is also the default behavior if no option is specified.
- OVERWRITE: The version of the file from the application revision currently being deployed replaces the version already on the instance.
- RETAIN: The version of the file already on the instance is kept and used as part of the new deployment.

Possible values:

- `DISALLOW`
- `OVERWRITE`
- `RETAIN`

`--override-alarm-configuration` (structure)

Allows you to specify information about alarms associated with a deployment. The alarm configuration that you specify here will override the alarm configuration at the deployment group level. Consider overriding the alarm configuration if you have set up alarms at the deployment group level that are causing deployment failures. In this case, you would call `CreateDeployment` to create a new deployment that uses a previous application revision that is known to work, and set its alarm configuration to turn off alarm polling. Turning off alarm polling ensures that the new deployment proceeds without being blocked by the alarm that was generated by the previous, failed, deployment.

### Note

If you specify an `overrideAlarmConfiguration` , you need the `UpdateDeploymentGroup` IAM permission when calling `CreateDeployment` .

enabled -> (boolean)

Indicates whether the alarm configuration is enabled.

ignorePollAlarmFailure -> (boolean)

Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from Amazon CloudWatch. The default value is false.

- `true` : The deployment proceeds even if alarm status information canât be retrieved from Amazon CloudWatch.
- `false` : The deployment stops if alarm status information canât be retrieved from Amazon CloudWatch.

alarms -> (list)

A list of alarms configured for the deployment or deployment group. A maximum of 10 alarms can be added.

(structure)

Information about an alarm.

name -> (string)

The name of the alarm. Maximum length is 255 characters. Each alarm name can be used only once in a list of alarms.

Shorthand Syntax:

```
enabled=boolean,ignorePollAlarmFailure=boolean,alarms=[{name=string},{name=string}]
```

JSON Syntax:

```
{
  "enabled": true|false,
  "ignorePollAlarmFailure": true|false,
  "alarms": [
    {
      "name": "string"
    }
    ...
  ]
}
```

`--s3-location` (structure)
Information about the location of the application revision in Amazon S3. You must specify the bucket, the key, and bundleType. Optionally, you can also specify an eTag and version.bucket -> (string)

The Amazon S3 bucket name.

key -> (string)

The Amazon S3 object key name.

bundleType -> (string)

The format of the bundle stored in Amazon S3.

eTag -> (string)

The Amazon S3 object eTag.

version -> (string)

The Amazon S3 object version.

Shorthand Syntax:

```
bucket=string,key=string,bundleType=string,eTag=string,version=string
```

JSON Syntax:

```
{
  "bucket": "string",
  "key": "string",
  "bundleType": "tar"|"tgz"|"zip",
  "eTag": "string",
  "version": "string"
}
```

`--github-location` (structure)
Information about the location of the application revision in GitHub. You must specify the repository and commit ID that references the application revision. For the repository, use the format GitHub-account/repository-name or GitHub-org/repository-name. For the commit ID, use the SHA1 Git commit reference.repository -> (string)

The GitHub account or organization and repository. Specify as GitHub-account/repository or GitHub-org/repository.

commitId -> (string)

The SHA1 Git commit reference.

Shorthand Syntax:

```
repository=string,commitId=string
```

JSON Syntax:

```
{
  "repository": "string",
  "commitId": "string"
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

**Example 1: To create a CodeDeploy deployment using the EC2/On-premises compute platform**

The following `create-deployment` example creates a deployment and associates it with the userâs AWS account.

```
aws deploy create-deployment \
    --application-name WordPress_App \
    --deployment-config-name CodeDeployDefault.OneAtATime \
    --deployment-group-name WordPress_DG \
    --description "My demo deployment" \
    --s3-location bucket=CodeDeployDemoBucket,bundleType=zip,eTag=dd56cfdEXAMPLE8e768f9d77fEXAMPLE,key=WordPressApp.zip
```

Output:

```
{
    "deploymentId": "d-A1B2C3111"
}
```

**Example 2: To create a CodeDeploy deployment using the Amazon ECS compute platform**

The following `create-deployment` example uses the following two files to deploy an Amazon ECS service.

Contents of `create-deployment.json` file:

```
{
    "applicationName": "ecs-deployment",
    "deploymentGroupName": "ecs-deployment-dg",
    "revision": {
        "revisionType": "S3",
        "s3Location": {
            "bucket": "ecs-deployment-bucket",
            "key": "appspec.yaml",
            "bundleType": "YAML"
        }
    }
}
```

That file, in turn, retrieves the following file `appspec.yaml` from an S3 bucket called `ecs-deployment-bucket`.

```
version: 0.0
Resources:
  - TargetService:
      Type: AWS::ECS::Service
      Properties:
        TaskDefinition: "arn:aws:ecs:region:123456789012:task-definition/ecs-task-def:2"
        LoadBalancerInfo:
          ContainerName: "sample-app"
          ContainerPort: 80
        PlatformVersion: "LATEST"
```

Command:

```
aws deploy create-deployment \
    --cli-input-json file://create-deployment.json \
    --region us-east-1
```

Output:

```
{
    "deploymentId": "d-1234ABCDE"
}
```

For more information, see [CreateDeployment](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeployment.html) in the *AWS CodeDeploy API Reference*.

## Output

deploymentId -> (string)

The unique ID of a deployment.