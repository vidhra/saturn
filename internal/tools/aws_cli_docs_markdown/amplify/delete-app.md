# delete-appÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/delete-app.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/delete-app.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [amplify](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/index.html#cli-aws-amplify) ]

# delete-app

## Description

Deletes an existing Amplify app specified by an app ID.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/DeleteApp)

## Synopsis

```
delete-app
--app-id <value>
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

app -> (structure)

Represents the different branches of a repository for building, deploying, and hosting an Amplify app.

appId -> (string)

The unique ID of the Amplify app.

appArn -> (string)

The Amazon Resource Name (ARN) of the Amplify app.

name -> (string)

The name for the Amplify app.

tags -> (map)

The tag for the Amplify app.

key -> (string)

value -> (string)

description -> (string)

The description for the Amplify app.

repository -> (string)

The Git repository for the Amplify app.

platform -> (string)

The platform for the Amplify app. For a static app, set the platform type to `WEB` . For a dynamic server-side rendered (SSR) app, set the platform type to `WEB_COMPUTE` . For an app requiring Amplify Hostingâs original SSR support only, set the platform type to `WEB_DYNAMIC` .

If you are deploying an SSG only app with Next.js 14 or later, you must use the platform type `WEB_COMPUTE` .

createTime -> (timestamp)

A timestamp of when Amplify created the application.

updateTime -> (timestamp)

A timestamp of when Amplify updated the application.

computeRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role for an SSR app. The Compute role allows the Amplify Hosting compute service to securely access specific Amazon Web Services resources based on the roleâs permissions. For more information about the SSR Compute role, see [Adding an SSR Compute role](https://docs.aws.amazon.com/amplify/latest/userguide/amplify-SSR-compute-role.html) in the *Amplify User Guide* .

iamServiceRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM service role for the Amplify app.

environmentVariables -> (map)

The environment variables for the Amplify app.

For a list of the environment variables that are accessible to Amplify by default, see [Amplify Environment variables](https://docs.aws.amazon.com/amplify/latest/userguide/amplify-console-environment-variables.html) in the *Amplify Hosting User Guide* .

key -> (string)

value -> (string)

defaultDomain -> (string)

The default domain for the Amplify app.

enableBranchAutoBuild -> (boolean)

Enables the auto-building of branches for the Amplify app.

enableBranchAutoDeletion -> (boolean)

Automatically disconnect a branch in the Amplify console when you delete a branch from your Git repository.

enableBasicAuth -> (boolean)

Enables basic authorization for the Amplify appâs branches.

basicAuthCredentials -> (string)

The basic authorization credentials for branches for the Amplify app. You must base64-encode the authorization credentials and provide them in the format `user:password` .

customRules -> (list)

Describes the custom redirect and rewrite rules for the Amplify app.

(structure)

Describes a custom rewrite or redirect rule.

source -> (string)

The source pattern for a URL rewrite or redirect rule.

target -> (string)

The target pattern for a URL rewrite or redirect rule.

status -> (string)

The status code for a URL rewrite or redirect rule.

200

Represents a 200 rewrite rule.

301

Represents a 301 (moved permanently) redirect rule. This and all future requests should be directed to the target URL.

302

Represents a 302 temporary redirect rule.

404

Represents a 404 redirect rule.

404-200

Represents a 404 rewrite rule.

condition -> (string)

The condition for a URL rewrite or redirect rule, such as a country code.

productionBranch -> (structure)

Describes the information about a production branch of the Amplify app.

lastDeployTime -> (timestamp)

The last deploy time of the production branch.

status -> (string)

The status of the production branch.

thumbnailUrl -> (string)

The thumbnail URL for the production branch.

branchName -> (string)

The branch name for the production branch.

buildSpec -> (string)

Describes the content of the build specification (build spec) for the Amplify app.

customHeaders -> (string)

Describes the custom HTTP headers for the Amplify app.

enableAutoBranchCreation -> (boolean)

Enables automated branch creation for the Amplify app.

autoBranchCreationPatterns -> (list)

Describes the automated branch creation glob patterns for the Amplify app.

(string)

autoBranchCreationConfig -> (structure)

Describes the automated branch creation configuration for the Amplify app.

stage -> (string)

Describes the current stage for the autocreated branch.

framework -> (string)

The framework for the autocreated branch.

enableAutoBuild -> (boolean)

Enables auto building for the autocreated branch.

environmentVariables -> (map)

The environment variables for the autocreated branch.

key -> (string)

value -> (string)

basicAuthCredentials -> (string)

The basic authorization credentials for the autocreated branch. You must base64-encode the authorization credentials and provide them in the format `user:password` .

enableBasicAuth -> (boolean)

Enables basic authorization for the autocreated branch.

enablePerformanceMode -> (boolean)

Enables performance mode for the branch.

Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out.

buildSpec -> (string)

The build specification (build spec) for the autocreated branch.

enablePullRequestPreview -> (boolean)

Enables pull request previews for the autocreated branch.

pullRequestEnvironmentName -> (string)

The Amplify environment name for the pull request.

repositoryCloneMethod -> (string)

### Note

This is for internal use.

The Amplify service uses this parameter to specify the authentication protocol to use to access the Git repository for an Amplify app. Amplify specifies `TOKEN` for a GitHub repository, `SIGV4` for an Amazon Web Services CodeCommit repository, and `SSH` for GitLab and Bitbucket repositories.

cacheConfig -> (structure)

The cache configuration for the Amplify app. If you donât specify the cache configuration `type` , Amplify uses the default `AMPLIFY_MANAGED` setting.

type -> (string)

The type of cache configuration to use for an Amplify app.

The `AMPLIFY_MANAGED` cache configuration automatically applies an optimized cache configuration for your app based on its platform, routing rules, and rewrite rules. This is the default setting.

The `AMPLIFY_MANAGED_NO_COOKIES` cache configuration type is the same as `AMPLIFY_MANAGED` , except that it excludes all cookies from the cache key.

webhookCreateTime -> (timestamp)

A timestamp of when Amplify created the webhook in your Git repository.

wafConfiguration -> (structure)

Describes the Firewall configuration for the Amplify app. Firewall support enables you to protect your hosted applications with a direct integration with WAF.

webAclArn -> (string)

The Amazon Resource Name (ARN) for the web ACL associated with an Amplify app.

wafStatus -> (string)

The status of the process to associate or disassociate a web ACL to an Amplify app.

statusReason -> (string)

The reason for the current status of the Firewall configuration.