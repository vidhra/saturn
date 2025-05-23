# create-branchÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/create-branch.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/create-branch.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [amplify](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/index.html#cli-aws-amplify) ]

# create-branch

## Description

Creates a new branch for an Amplify app.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/CreateBranch)

## Synopsis

```
create-branch
--app-id <value>
--branch-name <value>
[--description <value>]
[--stage <value>]
[--framework <value>]
[--enable-notification | --no-enable-notification]
[--enable-auto-build | --no-enable-auto-build]
[--enable-skew-protection | --no-enable-skew-protection]
[--environment-variables <value>]
[--basic-auth-credentials <value>]
[--enable-basic-auth | --no-enable-basic-auth]
[--enable-performance-mode | --no-enable-performance-mode]
[--tags <value>]
[--build-spec <value>]
[--ttl <value>]
[--display-name <value>]
[--enable-pull-request-preview | --no-enable-pull-request-preview]
[--pull-request-environment-name <value>]
[--backend-environment-arn <value>]
[--backend <value>]
[--compute-role-arn <value>]
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

`--app-id` (string)

The unique ID for an Amplify app.

`--branch-name` (string)

The name for the branch.

`--description` (string)

The description for the branch.

`--stage` (string)

Describes the current stage for the branch.

Possible values:

- `PRODUCTION`
- `BETA`
- `DEVELOPMENT`
- `EXPERIMENTAL`
- `PULL_REQUEST`

`--framework` (string)

The framework for the branch.

`--enable-notification` | `--no-enable-notification` (boolean)

Enables notifications for the branch.

`--enable-auto-build` | `--no-enable-auto-build` (boolean)

Enables auto building for the branch.

`--enable-skew-protection` | `--no-enable-skew-protection` (boolean)

Specifies whether the skew protection feature is enabled for the branch.

Deployment skew protection is available to Amplify applications to eliminate version skew issues between client and servers in web applications. When you apply skew protection to a branch, you can ensure that your clients always interact with the correct version of server-side assets, regardless of when a deployment occurs. For more information about skew protection, see [Skew protection for Amplify deployments](https://docs.aws.amazon.com/amplify/latest/userguide/skew-protection.html) in the *Amplify User Guide* .

`--environment-variables` (map)

The environment variables for the branch.

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

`--basic-auth-credentials` (string)

The basic authorization credentials for the branch. You must base64-encode the authorization credentials and provide them in the format `user:password` .

`--enable-basic-auth` | `--no-enable-basic-auth` (boolean)

Enables basic authorization for the branch.

`--enable-performance-mode` | `--no-enable-performance-mode` (boolean)

Enables performance mode for the branch.

Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out.

`--tags` (map)

The tag for the branch.

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

`--build-spec` (string)

The build specification (build spec) for the branch.

`--ttl` (string)

The content Time To Live (TTL) for the website in seconds.

`--display-name` (string)

The display name for a branch. This is used as the default domain prefix.

`--enable-pull-request-preview` | `--no-enable-pull-request-preview` (boolean)

Enables pull request previews for this branch.

`--pull-request-environment-name` (string)

The Amplify environment name for the pull request.

`--backend-environment-arn` (string)

The Amazon Resource Name (ARN) for a backend environment that is part of a Gen 1 Amplify app.

This field is available to Amplify Gen 1 apps only where the backend is created using Amplify Studio or the Amplify command line interface (CLI).

`--backend` (structure)

The backend for a `Branch` of an Amplify app. Use for a backend created from an CloudFormation stack.

This field is available to Amplify Gen 2 apps only. When you deploy an application with Amplify Gen 2, you provision the appâs backend infrastructure using Typescript code.

stackArn -> (string)

The Amazon Resource Name (ARN) for the CloudFormation stack.

Shorthand Syntax:

```
stackArn=string
```

JSON Syntax:

```
{
  "stackArn": "string"
}
```

`--compute-role-arn` (string)

The Amazon Resource Name (ARN) of the IAM role to assign to a branch of an SSR app. The SSR Compute role allows the Amplify Hosting compute service to securely access specific Amazon Web Services resources based on the roleâs permissions. For more information about the SSR Compute role, see [Adding an SSR Compute role](https://docs.aws.amazon.com/amplify/latest/userguide/amplify-SSR-compute-role.html) in the *Amplify User Guide* .

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

branch -> (structure)

Describes the branch for an Amplify app, which maps to a third-party repository branch.

branchArn -> (string)

The Amazon Resource Name (ARN) for a branch that is part of an Amplify app.

branchName -> (string)

The name for the branch that is part of an Amplify app.

description -> (string)

The description for the branch that is part of an Amplify app.

tags -> (map)

The tag for the branch of an Amplify app.

key -> (string)

value -> (string)

stage -> (string)

The current stage for the branch that is part of an Amplify app.

displayName -> (string)

The display name for the branch. This is used as the default domain prefix.

enableNotification -> (boolean)

Enables notifications for a branch that is part of an Amplify app.

createTime -> (timestamp)

A timestamp of when Amplify created the branch.

updateTime -> (timestamp)

A timestamp for the last updated time for a branch.

environmentVariables -> (map)

The environment variables specific to a branch of an Amplify app.

key -> (string)

value -> (string)

enableAutoBuild -> (boolean)

Enables auto-building on push for a branch of an Amplify app.

enableSkewProtection -> (boolean)

Specifies whether the skew protection feature is enabled for the branch.

Deployment skew protection is available to Amplify applications to eliminate version skew issues between client and servers in web applications. When you apply skew protection to a branch, you can ensure that your clients always interact with the correct version of server-side assets, regardless of when a deployment occurs. For more information about skew protection, see [Skew protection for Amplify deployments](https://docs.aws.amazon.com/amplify/latest/userguide/skew-protection.html) in the *Amplify User Guide* .

customDomains -> (list)

The custom domains for a branch of an Amplify app.

(string)

framework -> (string)

The framework for a branch of an Amplify app.

activeJobId -> (string)

The ID of the active job for a branch of an Amplify app.

totalNumberOfJobs -> (string)

The total number of jobs that are part of an Amplify app.

enableBasicAuth -> (boolean)

Enables basic authorization for a branch of an Amplify app.

enablePerformanceMode -> (boolean)

Enables performance mode for the branch.

Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out.

thumbnailUrl -> (string)

The thumbnail URL for the branch of an Amplify app.

basicAuthCredentials -> (string)

The basic authorization credentials for a branch of an Amplify app. You must base64-encode the authorization credentials and provide them in the format `user:password` .

buildSpec -> (string)

The build specification (build spec) content for the branch of an Amplify app.

ttl -> (string)

The content Time to Live (TTL) for the website in seconds.

associatedResources -> (list)

A list of custom resources that are linked to this branch.

(string)

enablePullRequestPreview -> (boolean)

Enables pull request previews for the branch.

pullRequestEnvironmentName -> (string)

The Amplify environment name for the pull request.

destinationBranch -> (string)

The destination branch if the branch is a pull request branch.

sourceBranch -> (string)

The source branch if the branch is a pull request branch.

backendEnvironmentArn -> (string)

The Amazon Resource Name (ARN) for a backend environment that is part of an Amplify app.

This property is available to Amplify Gen 1 apps only. When you deploy an application with Amplify Gen 2, you provision the appâs backend infrastructure using Typescript code.

backend -> (structure)

Describes the backend associated with an Amplify `Branch` .

This property is available to Amplify Gen 2 apps only. When you deploy an application with Amplify Gen 2, you provision the appâs backend infrastructure using Typescript code.

stackArn -> (string)

The Amazon Resource Name (ARN) for the CloudFormation stack.

computeRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role for a branch of an SSR app. The Compute role allows the Amplify Hosting compute service to securely access specific Amazon Web Services resources based on the roleâs permissions. For more information about the SSR Compute role, see [Adding an SSR Compute role](https://docs.aws.amazon.com/amplify/latest/userguide/amplify-SSR-compute-role.html) in the *Amplify User Guide* .