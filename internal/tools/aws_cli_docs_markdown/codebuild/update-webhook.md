# update-webhookÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/update-webhook.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/update-webhook.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codebuild](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/index.html#cli-aws-codebuild) ]

# update-webhook

## Description

Updates the webhook associated with an CodeBuild build project.

### Note

If you use Bitbucket for your repository, `rotateSecret` is ignored.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/UpdateWebhook)

## Synopsis

```
update-webhook
--project-name <value>
[--branch-filter <value>]
[--rotate-secret | --no-rotate-secret]
[--filter-groups <value>]
[--build-type <value>]
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

`--project-name` (string)

The name of the CodeBuild project.

`--branch-filter` (string)

A regular expression used to determine which repository branches are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If `branchFilter` is empty, then all branches are built.

### Note

It is recommended that you use `filterGroups` instead of `branchFilter` .

`--rotate-secret` | `--no-rotate-secret` (boolean)

A boolean value that specifies whether the associated GitHub repositoryâs secret token should be updated. If you use Bitbucket for your repository, `rotateSecret` is ignored.

`--filter-groups` (list)

An array of arrays of `WebhookFilter` objects used to determine if a webhook event can trigger a build. A filter group must contain at least one `EVENT` `WebhookFilter` .

(list)

(structure)

A filter used to determine which webhooks trigger a build.

type -> (string)

The type of webhook filter. There are 11 webhook filter types: `EVENT` , `ACTOR_ACCOUNT_ID` , `HEAD_REF` , `BASE_REF` , `FILE_PATH` , `COMMIT_MESSAGE` , `TAG_NAME` , `RELEASE_NAME` , `REPOSITORY_NAME` , `ORGANIZATION_NAME` , and `WORKFLOW_NAME` .

- EVENT

- A webhook event triggers a build when the provided `pattern` matches one of nine event types: `PUSH` , `PULL_REQUEST_CREATED` , `PULL_REQUEST_UPDATED` , `PULL_REQUEST_CLOSED` , `PULL_REQUEST_REOPENED` , `PULL_REQUEST_MERGED` , `RELEASED` , `PRERELEASED` , and `WORKFLOW_JOB_QUEUED` . The `EVENT` patterns are specified as a comma-separated string. For example, `PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED` filters all push, pull request created, and pull request updated events.

### Note

Types `PULL_REQUEST_REOPENED` and `WORKFLOW_JOB_QUEUED` work with GitHub and GitHub Enterprise only. Types `RELEASED` and `PRERELEASED` work with GitHub only.
- ACTOR_ACCOUNT_ID

- A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket account ID matches the regular expression `pattern` .
- HEAD_REF

- A webhook event triggers a build when the head reference matches the regular expression `pattern` . For example, `refs/heads/branch-name` and `refs/tags/tag-name` .

### Note

Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull request, Bitbucket push, and Bitbucket pull request events.
- BASE_REF

- A webhook event triggers a build when the base reference matches the regular expression `pattern` . For example, `refs/heads/branch-name` .

### Note

Works with pull request events only.
- FILE_PATH

- A webhook triggers a build when the path of a changed file matches the regular expression `pattern` .

### Note

Works with push and pull request events only.
- COMMIT_MESSAGE

- A webhook triggers a build when the head commit message matches the regular expression `pattern` .

### Note

Works with push and pull request events only.
- TAG_NAME

- A webhook triggers a build when the tag name of the release matches the regular expression `pattern` .

### Note

Works with `RELEASED` and `PRERELEASED` events only.
- RELEASE_NAME

- A webhook triggers a build when the release name matches the regular expression `pattern` .

### Note

Works with `RELEASED` and `PRERELEASED` events only.
- REPOSITORY_NAME

- A webhook triggers a build when the repository name matches the regular expression `pattern` .

### Note

Works with GitHub global or organization webhooks only.
- ORGANIZATION_NAME

- A webhook triggers a build when the organization name matches the regular expression `pattern` .

### Note

Works with GitHub global webhooks only.
- WORKFLOW_NAME

- A webhook triggers a build when the workflow name matches the regular expression `pattern` .

### Note

Works with `WORKFLOW_JOB_QUEUED` events only.

### Note

For CodeBuild-hosted Buildkite runner builds, WORKFLOW_NAME filters will filter by pipeline name.

pattern -> (string)

For a `WebHookFilter` that uses `EVENT` type, a comma-separated string that specifies one or more events. For example, the webhook filter `PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED` allows all push, pull request created, and pull request updated events to trigger a build.

For a `WebHookFilter` that uses any of the other filter types, a regular expression pattern. For example, a `WebHookFilter` that uses `HEAD_REF` for its `type` and the pattern `^refs/heads/` triggers a build when the head reference is a branch with a reference name `refs/heads/branch-name` .

excludeMatchedPattern -> (boolean)

Used to indicate that the `pattern` determines which webhook events do not trigger a build. If true, then a webhook event that does not match the `pattern` triggers a build. If false, then a webhook event that matches the `pattern` triggers a build.

Shorthand Syntax:

```
[{type=string,pattern=string,excludeMatchedPattern=boolean},{type=string,pattern=string,excludeMatchedPattern=boolean}] ...
```

JSON Syntax:

```
[
  [
    {
      "type": "EVENT"|"BASE_REF"|"HEAD_REF"|"ACTOR_ACCOUNT_ID"|"FILE_PATH"|"COMMIT_MESSAGE"|"WORKFLOW_NAME"|"TAG_NAME"|"RELEASE_NAME"|"REPOSITORY_NAME"|"ORGANIZATION_NAME",
      "pattern": "string",
      "excludeMatchedPattern": true|false
    }
    ...
  ]
  ...
]
```

`--build-type` (string)

Specifies the type of build this webhook will trigger.

### Note

`RUNNER_BUILDKITE_BUILD` is only available for `NO_SOURCE` source type projects configured for Buildkite runner builds. For more information about CodeBuild-hosted Buildkite runner builds, see [Tutorial: Configure a CodeBuild-hosted Buildkite runner](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-runner-buildkite.html) in the *CodeBuild user guide* .

Possible values:

- `BUILD`
- `BUILD_BATCH`
- `RUNNER_BUILDKITE_BUILD`

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

**To update the webhook for an AWS CodeBuild project**

The following `update-webhook` example updates a webhook for the specified CodeBuild project with two filter groups. The `--rotate-secret` parameter specifies that GitHub rotate the projectâs secret key every time a code change triggers a build. The first filter group specifies pull requests that are created, updated, or reopened on branches with Git reference names that match the regular expression `^refs/heads/master$` and head references that match `^refs/heads/myBranch$`.  The second filter group specifies push requests on branches with Git reference names that do not match the regular expression `^refs/heads/myBranch$`.

```
aws codebuild update-webhook \
    --project-name Project2 \
    --rotate-secret \
    --filter-groups "[[{\"type\":\"EVENT\",\"pattern\":\"PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED, PULL_REQUEST_REOPENED\"},{\"type\":\"HEAD_REF\",\"pattern\":\"^refs/heads/myBranch$\",\"excludeMatchedPattern\":true},{\"type\":\"BASE_REF\",\"pattern\":\"^refs/heads/master$\",\"excludeMatchedPattern\":true}],[{\"type\":\"EVENT\",\"pattern\":\"PUSH\"},{\"type\":\"HEAD_REF\",\"pattern\":\"^refs/heads/myBranch$\",\"excludeMatchedPattern\":true}]]"
```

Output:

```
{
    "webhook": {
        "filterGroups": [
            [
                {
                    "pattern": "PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED, PULL_REQUEST_REOPENED",
                    "type": "EVENT"
                },
                {
                    "excludeMatchedPattern": true,
                    "pattern": "refs/heads/myBranch$",
                    "type": "HEAD_REF"
                },
                {
                    "excludeMatchedPattern": true,
                    "pattern": "refs/heads/master$",
                    "type": "BASE_REF"
                }
            ],
            [
                {
                    "pattern": "PUSH",
                    "type": "EVENT"
                },
                {
                    "excludeMatchedPattern": true,
                    "pattern": "refs/heads/myBranch$",
                    "type": "HEAD_REF"
                }
            ]
        ],
        "lastModifiedSecret": 1556312220.133
    }
}
```

For more information, see [Change a Build Projectâs Settings (AWS CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/change-project.html#change-project-cli) in the *AWS CodeBuild User Guide*

## Output

webhook -> (structure)

Information about a repositoryâs webhook that is associated with a project in CodeBuild.

url -> (string)

The URL to the webhook.

payloadUrl -> (string)

The CodeBuild endpoint where webhook events are sent.

secret -> (string)

The secret token of the associated repository.

### Note

A Bitbucket webhook does not support `secret` .

branchFilter -> (string)

A regular expression used to determine which repository branches are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If `branchFilter` is empty, then all branches are built.

### Note

It is recommended that you use `filterGroups` instead of `branchFilter` .

filterGroups -> (list)

An array of arrays of `WebhookFilter` objects used to determine which webhooks are triggered. At least one `WebhookFilter` in the array must specify `EVENT` as its `type` .

For a build to be triggered, at least one filter group in the `filterGroups` array must pass. For a filter group to pass, each of its filters must pass.

(list)

(structure)

A filter used to determine which webhooks trigger a build.

type -> (string)

The type of webhook filter. There are 11 webhook filter types: `EVENT` , `ACTOR_ACCOUNT_ID` , `HEAD_REF` , `BASE_REF` , `FILE_PATH` , `COMMIT_MESSAGE` , `TAG_NAME` , `RELEASE_NAME` , `REPOSITORY_NAME` , `ORGANIZATION_NAME` , and `WORKFLOW_NAME` .

- EVENT

- A webhook event triggers a build when the provided `pattern` matches one of nine event types: `PUSH` , `PULL_REQUEST_CREATED` , `PULL_REQUEST_UPDATED` , `PULL_REQUEST_CLOSED` , `PULL_REQUEST_REOPENED` , `PULL_REQUEST_MERGED` , `RELEASED` , `PRERELEASED` , and `WORKFLOW_JOB_QUEUED` . The `EVENT` patterns are specified as a comma-separated string. For example, `PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED` filters all push, pull request created, and pull request updated events.

### Note

Types `PULL_REQUEST_REOPENED` and `WORKFLOW_JOB_QUEUED` work with GitHub and GitHub Enterprise only. Types `RELEASED` and `PRERELEASED` work with GitHub only.
- ACTOR_ACCOUNT_ID

- A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket account ID matches the regular expression `pattern` .
- HEAD_REF

- A webhook event triggers a build when the head reference matches the regular expression `pattern` . For example, `refs/heads/branch-name` and `refs/tags/tag-name` .

### Note

Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull request, Bitbucket push, and Bitbucket pull request events.
- BASE_REF

- A webhook event triggers a build when the base reference matches the regular expression `pattern` . For example, `refs/heads/branch-name` .

### Note

Works with pull request events only.
- FILE_PATH

- A webhook triggers a build when the path of a changed file matches the regular expression `pattern` .

### Note

Works with push and pull request events only.
- COMMIT_MESSAGE

- A webhook triggers a build when the head commit message matches the regular expression `pattern` .

### Note

Works with push and pull request events only.
- TAG_NAME

- A webhook triggers a build when the tag name of the release matches the regular expression `pattern` .

### Note

Works with `RELEASED` and `PRERELEASED` events only.
- RELEASE_NAME

- A webhook triggers a build when the release name matches the regular expression `pattern` .

### Note

Works with `RELEASED` and `PRERELEASED` events only.
- REPOSITORY_NAME

- A webhook triggers a build when the repository name matches the regular expression `pattern` .

### Note

Works with GitHub global or organization webhooks only.
- ORGANIZATION_NAME

- A webhook triggers a build when the organization name matches the regular expression `pattern` .

### Note

Works with GitHub global webhooks only.
- WORKFLOW_NAME

- A webhook triggers a build when the workflow name matches the regular expression `pattern` .

### Note

Works with `WORKFLOW_JOB_QUEUED` events only.

### Note

For CodeBuild-hosted Buildkite runner builds, WORKFLOW_NAME filters will filter by pipeline name.

pattern -> (string)

For a `WebHookFilter` that uses `EVENT` type, a comma-separated string that specifies one or more events. For example, the webhook filter `PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED` allows all push, pull request created, and pull request updated events to trigger a build.

For a `WebHookFilter` that uses any of the other filter types, a regular expression pattern. For example, a `WebHookFilter` that uses `HEAD_REF` for its `type` and the pattern `^refs/heads/` triggers a build when the head reference is a branch with a reference name `refs/heads/branch-name` .

excludeMatchedPattern -> (boolean)

Used to indicate that the `pattern` determines which webhook events do not trigger a build. If true, then a webhook event that does not match the `pattern` triggers a build. If false, then a webhook event that matches the `pattern` triggers a build.

buildType -> (string)

Specifies the type of build this webhook will trigger.

### Note

`RUNNER_BUILDKITE_BUILD` is only available for `NO_SOURCE` source type projects configured for Buildkite runner builds. For more information about CodeBuild-hosted Buildkite runner builds, see [Tutorial: Configure a CodeBuild-hosted Buildkite runner](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-runner-buildkite.html) in the *CodeBuild user guide* .

manualCreation -> (boolean)

If manualCreation is true, CodeBuild doesnât create a webhook in GitHub and instead returns `payloadUrl` and `secret` values for the webhook. The `payloadUrl` and `secret` values in the output can be used to manually create a webhook within GitHub.

### Note

manualCreation is only available for GitHub webhooks.

lastModifiedSecret -> (timestamp)

A timestamp that indicates the last time a repositoryâs secret token was modified.

scopeConfiguration -> (structure)

The scope configuration for global or organization webhooks.

### Note

Global or organization webhooks are only available for GitHub and Github Enterprise webhooks.

name -> (string)

The name of either the group, enterprise, or organization that will send webhook events to CodeBuild, depending on the type of webhook.

domain -> (string)

The domain of the GitHub Enterprise organization or the GitLab Self Managed group. Note that this parameter is only required if your projectâs source type is GITHUB_ENTERPRISE or GITLAB_SELF_MANAGED.

scope -> (string)

The type of scope for a GitHub or GitLab webhook. The scope default is GITHUB_ORGANIZATION.

status -> (string)

The status of the webhook. Valid values include:

- `CREATING` : The webhook is being created.
- `CREATE_FAILED` : The webhook has failed to create.
- `ACTIVE` : The webhook has succeeded and is active.
- `DELETING` : The webhook is being deleted.

statusMessage -> (string)

A message associated with the status of a webhook.