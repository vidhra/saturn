# start-buildÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/start-build.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/start-build.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codebuild](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/index.html#cli-aws-codebuild) ]

# start-build

## Description

Starts running a build with the settings defined in the project. These setting include: how to run a build, where to get the source code, which build environment to use, which build commands to run, and where to store the build output.

You can also start a build run by overriding some of the build settings in the project. The overrides only apply for that specific start build request. The settings in the project are unaltered.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/StartBuild)

## Synopsis

```
start-build
--project-name <value>
[--secondary-sources-override <value>]
[--secondary-sources-version-override <value>]
[--source-version <value>]
[--artifacts-override <value>]
[--secondary-artifacts-override <value>]
[--environment-variables-override <value>]
[--source-type-override <value>]
[--source-location-override <value>]
[--source-auth-override <value>]
[--git-clone-depth-override <value>]
[--git-submodules-config-override <value>]
[--buildspec-override <value>]
[--insecure-ssl-override | --no-insecure-ssl-override]
[--report-build-status-override | --no-report-build-status-override]
[--build-status-config-override <value>]
[--environment-type-override <value>]
[--image-override <value>]
[--compute-type-override <value>]
[--certificate-override <value>]
[--cache-override <value>]
[--service-role-override <value>]
[--privileged-mode-override | --no-privileged-mode-override]
[--timeout-in-minutes-override <value>]
[--queued-timeout-in-minutes-override <value>]
[--encryption-key-override <value>]
[--idempotency-token <value>]
[--logs-config-override <value>]
[--registry-credential-override <value>]
[--image-pull-credentials-type-override <value>]
[--debug-session-enabled | --no-debug-session-enabled]
[--fleet-override <value>]
[--auto-retry-limit-override <value>]
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

The name of the CodeBuild build project to start running a build.

`--secondary-sources-override` (list)

An array of `ProjectSource` objects.

(structure)

Information about the build input source code for the build project.

type -> (string)

The type of repository that contains the source code to be built. Valid values include:

- `BITBUCKET` : The source code is in a Bitbucket repository.
- `CODECOMMIT` : The source code is in an CodeCommit repository.
- `CODEPIPELINE` : The source code settings are specified in the source action of a pipeline in CodePipeline.
- `GITHUB` : The source code is in a GitHub repository.
- `GITHUB_ENTERPRISE` : The source code is in a GitHub Enterprise Server repository.
- `GITLAB` : The source code is in a GitLab repository.
- `GITLAB_SELF_MANAGED` : The source code is in a self-managed GitLab repository.
- `NO_SOURCE` : The project does not have input source code.
- `S3` : The source code is in an Amazon S3 bucket.

location -> (string)

Information about the location of the source code to be built. Valid values include:

- For source code settings that are specified in the source action of a pipeline in CodePipeline, `location` should not be specified. If it is specified, CodePipeline ignores it. This is because CodePipeline uses the settings in a pipelineâs source action instead of this value.
- For source code in an CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, `https://git-codecommit.<region-ID>.amazonaws.com/v1/repos/<repo-name>` ).
- For source code in an Amazon S3 input bucket, one of the following.
- The path to the ZIP file that contains the source code (for example, `<bucket-name>/<path>/<object-name>.zip` ).
- The path to the folder that contains the source code (for example, `<bucket-name>/<path-to-source-code>/<folder>/` ).
- For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your Amazon Web Services account to your GitHub account. Use the CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page, for **Organization access** , choose **Request access** next to each repository you want to allow CodeBuild to have access to, and then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the CodeBuild console.) To instruct CodeBuild to use this connection, in the `source` object, set the `auth` objectâs `type` value to `OAUTH` .
- For source code in an GitLab or self-managed GitLab repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your Amazon Web Services account to your GitLab account. Use the CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitLab, on the Connections **Authorize application** page, choose **Authorize** . Then on the CodeConnections **Create GitLab connection** page, choose **Connect to GitLab** . (After you have connected to your GitLab account, you do not need to finish creating the build project. You can leave the CodeBuild console.) To instruct CodeBuild to override the default connection and use this connection instead, set the `auth` objectâs `type` value to `CODECONNECTIONS` in the `source` object.
- For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your Amazon Web Services account to your Bitbucket account. Use the CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the CodeBuild console.) To instruct CodeBuild to use this connection, in the `source` object, set the `auth` objectâs `type` value to `OAUTH` .

If you specify `CODEPIPELINE` for the `Type` property, donât specify this property. For all of the other types, you must specify `Location` .

gitCloneDepth -> (integer)

Information about the Git clone depth for the build project.

gitSubmodulesConfig -> (structure)

Information about the Git submodules configuration for the build project.

fetchSubmodules -> (boolean)

Set to true to fetch Git submodules for your CodeBuild build project.

buildspec -> (string)

The buildspec file declaration to use for the builds in this build project.

If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in `CODEBUILD_SRC_DIR` environment variable, or the path to an S3 bucket. The bucket must be in the same Amazon Web Services Region as the build project. Specify the buildspec file using its ARN (for example, `arn:aws:s3:::my-codebuild-sample2/buildspec.yml` ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see [Buildspec File Name and Storage Location](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec-ref-name-storage) .

auth -> (structure)

Information about the authorization settings for CodeBuild to access the source code to be built.

type -> (string)

The authorization type to use. Valid options are OAUTH, CODECONNECTIONS, or SECRETS_MANAGER.

resource -> (string)

The resource value that applies to the specified authorization type.

reportBuildStatus -> (boolean)

Set to true to report the status of a buildâs start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, GitLab, GitLab Self Managed, GitLab, GitLab Self Managed, or Bitbucket. If this is set and you use a different source provider, an `invalidInputException` is thrown.

To be able to report the build status to the source provider, the user associated with the source provider must have write access to the repo. If the user does not have write access, the build status cannot be updated. For more information, see [Source provider access](https://docs.aws.amazon.com/codebuild/latest/userguide/access-tokens.html) in the *CodeBuild User Guide* .

The status of a build triggered by a webhook is always reported to your source provider.

If your projectâs builds are triggered by a webhook, you must push a new commit to the repo for a change to this property to take effect.

buildStatusConfig -> (structure)

Contains information that defines how the build project reports the build status to the source provider. This option is only used when the source provider is `GITHUB` , `GITHUB_ENTERPRISE` , or `BITBUCKET` .

context -> (string)

Specifies the context of the build status CodeBuild sends to the source provider. The usage of this parameter depends on the source provider.

Bitbucket

This parameter is used for the `name` parameter in the Bitbucket commit status. For more information, see [build](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/commit/%7Bnode%7D/statuses/build) in the Bitbucket API documentation.

GitHub/GitHub Enterprise Server

This parameter is used for the `context` parameter in the GitHub commit status. For more information, see [Create a commit status](https://developer.github.com/v3/repos/statuses/#create-a-commit-status) in the GitHub developer guide.

targetUrl -> (string)

Specifies the target url of the build status CodeBuild sends to the source provider. The usage of this parameter depends on the source provider.

Bitbucket

This parameter is used for the `url` parameter in the Bitbucket commit status. For more information, see [build](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/commit/%7Bnode%7D/statuses/build) in the Bitbucket API documentation.

GitHub/GitHub Enterprise Server

This parameter is used for the `target_url` parameter in the GitHub commit status. For more information, see [Create a commit status](https://developer.github.com/v3/repos/statuses/#create-a-commit-status) in the GitHub developer guide.

insecureSsl -> (boolean)

Enable this flag to ignore SSL warnings while connecting to the project source code.

sourceIdentifier -> (string)

An identifier for this project source. The identifier can only contain alphanumeric characters and underscores, and must be less than 128 characters in length.

Shorthand Syntax:

```
type=string,location=string,gitCloneDepth=integer,gitSubmodulesConfig={fetchSubmodules=boolean},buildspec=string,auth={type=string,resource=string},reportBuildStatus=boolean,buildStatusConfig={context=string,targetUrl=string},insecureSsl=boolean,sourceIdentifier=string ...
```

JSON Syntax:

```
[
  {
    "type": "CODECOMMIT"|"CODEPIPELINE"|"GITHUB"|"GITLAB"|"GITLAB_SELF_MANAGED"|"S3"|"BITBUCKET"|"GITHUB_ENTERPRISE"|"NO_SOURCE",
    "location": "string",
    "gitCloneDepth": integer,
    "gitSubmodulesConfig": {
      "fetchSubmodules": true|false
    },
    "buildspec": "string",
    "auth": {
      "type": "OAUTH"|"CODECONNECTIONS"|"SECRETS_MANAGER",
      "resource": "string"
    },
    "reportBuildStatus": true|false,
    "buildStatusConfig": {
      "context": "string",
      "targetUrl": "string"
    },
    "insecureSsl": true|false,
    "sourceIdentifier": "string"
  }
  ...
]
```

`--secondary-sources-version-override` (list)

An array of `ProjectSourceVersion` objects that specify one or more versions of the projectâs secondary sources to be used for this build only.

(structure)

A source identifier and its corresponding version.

sourceIdentifier -> (string)

An identifier for a source in the build project. The identifier can only contain alphanumeric characters and underscores, and must be less than 128 characters in length.

sourceVersion -> (string)

The source version for the corresponding source identifier. If specified, must be one of:

- For CodeCommit: the commit ID, branch, or Git tag to use.
- For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format `pr/pull-request-ID` (for example, `pr/25` ). If a branch name is specified, the branchâs HEAD commit ID is used. If not specified, the default branchâs HEAD commit ID is used.
- For GitLab: the commit ID, branch, or Git tag to use.
- For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branchâs HEAD commit ID is used. If not specified, the default branchâs HEAD commit ID is used.
- For Amazon S3: the version ID of the object that represents the build input ZIP file to use.

For more information, see [Source Version Sample with CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html) in the *CodeBuild User Guide* .

Shorthand Syntax:

```
sourceIdentifier=string,sourceVersion=string ...
```

JSON Syntax:

```
[
  {
    "sourceIdentifier": "string",
    "sourceVersion": "string"
  }
  ...
]
```

`--source-version` (string)

The version of the build input to be built, for this build only. If not specified, the latest version is used. If specified, the contents depends on the source provider:

CodeCommit

The commit ID, branch, or Git tag to use.

GitHub

The commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format `pr/pull-request-ID` (for example `pr/25` ). If a branch name is specified, the branchâs HEAD commit ID is used. If not specified, the default branchâs HEAD commit ID is used.

GitLab

The commit ID, branch, or Git tag to use.

Bitbucket

The commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branchâs HEAD commit ID is used. If not specified, the default branchâs HEAD commit ID is used.

Amazon S3

The version ID of the object that represents the build input ZIP file to use.

If `sourceVersion` is specified at the project level, then this `sourceVersion` (at the build level) takes precedence.

For more information, see [Source Version Sample with CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html) in the *CodeBuild User Guide* .

`--artifacts-override` (structure)

Build output artifact settings that override, for this build only, the latest ones already defined in the build project.

type -> (string)

The type of build output artifact. Valid values include:

- `CODEPIPELINE` : The build project has build output generated through CodePipeline.

### Note

The `CODEPIPELINE` type is not supported for `secondaryArtifacts` .

- `NO_ARTIFACTS` : The build project does not produce any build output.
- `S3` : The build project stores build output in Amazon S3.

location -> (string)

Information about the build output artifact location:

- If `type` is set to `CODEPIPELINE` , CodePipeline ignores this value if specified. This is because CodePipeline manages its build output locations instead of CodeBuild.
- If `type` is set to `NO_ARTIFACTS` , this value is ignored if specified, because no build output is produced.
- If `type` is set to `S3` , this is the name of the output bucket.

path -> (string)

Along with `namespaceType` and `name` , the pattern that CodeBuild uses to name and store the output artifact:

- If `type` is set to `CODEPIPELINE` , CodePipeline ignores this value if specified. This is because CodePipeline manages its build output names instead of CodeBuild.
- If `type` is set to `NO_ARTIFACTS` , this value is ignored if specified, because no build output is produced.
- If `type` is set to `S3` , this is the path to the output artifact. If `path` is not specified, `path` is not used.

For example, if `path` is set to `MyArtifacts` , `namespaceType` is set to `NONE` , and `name` is set to `MyArtifact.zip` , the output artifact is stored in the output bucket at `MyArtifacts/MyArtifact.zip` .

namespaceType -> (string)

Along with `path` and `name` , the pattern that CodeBuild uses to determine the name and location to store the output artifact:

- If `type` is set to `CODEPIPELINE` , CodePipeline ignores this value if specified. This is because CodePipeline manages its build output names instead of CodeBuild.
- If `type` is set to `NO_ARTIFACTS` , this value is ignored if specified, because no build output is produced.
- If `type` is set to `S3` , valid values include:
- `BUILD_ID` : Include the build ID in the location of the build output artifact.
- `NONE` : Do not include the build ID. This is the default if `namespaceType` is not specified.

For example, if `path` is set to `MyArtifacts` , `namespaceType` is set to `BUILD_ID` , and `name` is set to `MyArtifact.zip` , the output artifact is stored in `MyArtifacts/<build-ID>/MyArtifact.zip` .

name -> (string)

Along with `path` and `namespaceType` , the pattern that CodeBuild uses to name and store the output artifact:

- If `type` is set to `CODEPIPELINE` , CodePipeline ignores this value if specified. This is because CodePipeline manages its build output names instead of CodeBuild.
- If `type` is set to `NO_ARTIFACTS` , this value is ignored if specified, because no build output is produced.
- If `type` is set to `S3` , this is the name of the output artifact object. If you set the name to be a forward slash (â/â), the artifact is stored in the root of the output bucket.

For example:

- If `path` is set to `MyArtifacts` , `namespaceType` is set to `BUILD_ID` , and `name` is set to `MyArtifact.zip` , then the output artifact is stored in `MyArtifacts/<build-ID>/MyArtifact.zip` .
- If `path` is empty, `namespaceType` is set to `NONE` , and `name` is set to â`/` â, the output artifact is stored in the root of the output bucket.
- If `path` is set to `MyArtifacts` , `namespaceType` is set to `BUILD_ID` , and `name` is set to â`/` â, the output artifact is stored in `MyArtifacts/<build-ID>` .

packaging -> (string)

The type of build output artifact to create:

- If `type` is set to `CODEPIPELINE` , CodePipeline ignores this value if specified. This is because CodePipeline manages its build output artifacts instead of CodeBuild.
- If `type` is set to `NO_ARTIFACTS` , this value is ignored if specified, because no build output is produced.
- If `type` is set to `S3` , valid values include:
- `NONE` : CodeBuild creates in the output bucket a folder that contains the build output. This is the default if `packaging` is not specified.
- `ZIP` : CodeBuild creates in the output bucket a ZIP file that contains the build output.

overrideArtifactName -> (boolean)

If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.

encryptionDisabled -> (boolean)

Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon S3. If this is set with another artifacts type, an invalidInputException is thrown.

artifactIdentifier -> (string)

An identifier for this artifact definition.

bucketOwnerAccess -> (string)

Specifies the bucket ownerâs access for objects that another account uploads to their Amazon S3 bucket. By default, only the account that uploads the objects to the bucket has access to these objects. This property allows you to give the bucket owner access to these objects.

### Note

To use this property, your CodeBuild service role must have the `s3:PutBucketAcl` permission. This permission allows CodeBuild to modify the access control list for the bucket.

This property can be one of the following values:

NONE

The bucket owner does not have access to the objects. This is the default.

READ_ONLY

The bucket owner has read-only access to the objects. The uploading account retains ownership of the objects.

FULL

The bucket owner has full access to the objects. Object ownership is determined by the following criteria:

- If the bucket is configured with the **Bucket owner preferred** setting, the bucket owner owns the objects. The uploading account will have object access as specified by the bucketâs policy.
- Otherwise, the uploading account retains ownership of the objects.

For more information about Amazon S3 object ownership, see [Controlling ownership of uploaded objects using S3 Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon Simple Storage Service User Guide* .

Shorthand Syntax:

```
type=string,location=string,path=string,namespaceType=string,name=string,packaging=string,overrideArtifactName=boolean,encryptionDisabled=boolean,artifactIdentifier=string,bucketOwnerAccess=string
```

JSON Syntax:

```
{
  "type": "CODEPIPELINE"|"S3"|"NO_ARTIFACTS",
  "location": "string",
  "path": "string",
  "namespaceType": "NONE"|"BUILD_ID",
  "name": "string",
  "packaging": "NONE"|"ZIP",
  "overrideArtifactName": true|false,
  "encryptionDisabled": true|false,
  "artifactIdentifier": "string",
  "bucketOwnerAccess": "NONE"|"READ_ONLY"|"FULL"
}
```

`--secondary-artifacts-override` (list)

An array of `ProjectArtifacts` objects.

(structure)

Information about the build output artifacts for the build project.

type -> (string)

The type of build output artifact. Valid values include:

- `CODEPIPELINE` : The build project has build output generated through CodePipeline.

### Note

The `CODEPIPELINE` type is not supported for `secondaryArtifacts` .

- `NO_ARTIFACTS` : The build project does not produce any build output.
- `S3` : The build project stores build output in Amazon S3.

location -> (string)

Information about the build output artifact location:

- If `type` is set to `CODEPIPELINE` , CodePipeline ignores this value if specified. This is because CodePipeline manages its build output locations instead of CodeBuild.
- If `type` is set to `NO_ARTIFACTS` , this value is ignored if specified, because no build output is produced.
- If `type` is set to `S3` , this is the name of the output bucket.

path -> (string)

Along with `namespaceType` and `name` , the pattern that CodeBuild uses to name and store the output artifact:

- If `type` is set to `CODEPIPELINE` , CodePipeline ignores this value if specified. This is because CodePipeline manages its build output names instead of CodeBuild.
- If `type` is set to `NO_ARTIFACTS` , this value is ignored if specified, because no build output is produced.
- If `type` is set to `S3` , this is the path to the output artifact. If `path` is not specified, `path` is not used.

For example, if `path` is set to `MyArtifacts` , `namespaceType` is set to `NONE` , and `name` is set to `MyArtifact.zip` , the output artifact is stored in the output bucket at `MyArtifacts/MyArtifact.zip` .

namespaceType -> (string)

Along with `path` and `name` , the pattern that CodeBuild uses to determine the name and location to store the output artifact:

- If `type` is set to `CODEPIPELINE` , CodePipeline ignores this value if specified. This is because CodePipeline manages its build output names instead of CodeBuild.
- If `type` is set to `NO_ARTIFACTS` , this value is ignored if specified, because no build output is produced.
- If `type` is set to `S3` , valid values include:
- `BUILD_ID` : Include the build ID in the location of the build output artifact.
- `NONE` : Do not include the build ID. This is the default if `namespaceType` is not specified.

For example, if `path` is set to `MyArtifacts` , `namespaceType` is set to `BUILD_ID` , and `name` is set to `MyArtifact.zip` , the output artifact is stored in `MyArtifacts/<build-ID>/MyArtifact.zip` .

name -> (string)

Along with `path` and `namespaceType` , the pattern that CodeBuild uses to name and store the output artifact:

- If `type` is set to `CODEPIPELINE` , CodePipeline ignores this value if specified. This is because CodePipeline manages its build output names instead of CodeBuild.
- If `type` is set to `NO_ARTIFACTS` , this value is ignored if specified, because no build output is produced.
- If `type` is set to `S3` , this is the name of the output artifact object. If you set the name to be a forward slash (â/â), the artifact is stored in the root of the output bucket.

For example:

- If `path` is set to `MyArtifacts` , `namespaceType` is set to `BUILD_ID` , and `name` is set to `MyArtifact.zip` , then the output artifact is stored in `MyArtifacts/<build-ID>/MyArtifact.zip` .
- If `path` is empty, `namespaceType` is set to `NONE` , and `name` is set to â`/` â, the output artifact is stored in the root of the output bucket.
- If `path` is set to `MyArtifacts` , `namespaceType` is set to `BUILD_ID` , and `name` is set to â`/` â, the output artifact is stored in `MyArtifacts/<build-ID>` .

packaging -> (string)

The type of build output artifact to create:

- If `type` is set to `CODEPIPELINE` , CodePipeline ignores this value if specified. This is because CodePipeline manages its build output artifacts instead of CodeBuild.
- If `type` is set to `NO_ARTIFACTS` , this value is ignored if specified, because no build output is produced.
- If `type` is set to `S3` , valid values include:
- `NONE` : CodeBuild creates in the output bucket a folder that contains the build output. This is the default if `packaging` is not specified.
- `ZIP` : CodeBuild creates in the output bucket a ZIP file that contains the build output.

overrideArtifactName -> (boolean)

If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.

encryptionDisabled -> (boolean)

Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon S3. If this is set with another artifacts type, an invalidInputException is thrown.

artifactIdentifier -> (string)

An identifier for this artifact definition.

bucketOwnerAccess -> (string)

Specifies the bucket ownerâs access for objects that another account uploads to their Amazon S3 bucket. By default, only the account that uploads the objects to the bucket has access to these objects. This property allows you to give the bucket owner access to these objects.

### Note

To use this property, your CodeBuild service role must have the `s3:PutBucketAcl` permission. This permission allows CodeBuild to modify the access control list for the bucket.

This property can be one of the following values:

NONE

The bucket owner does not have access to the objects. This is the default.

READ_ONLY

The bucket owner has read-only access to the objects. The uploading account retains ownership of the objects.

FULL

The bucket owner has full access to the objects. Object ownership is determined by the following criteria:

- If the bucket is configured with the **Bucket owner preferred** setting, the bucket owner owns the objects. The uploading account will have object access as specified by the bucketâs policy.
- Otherwise, the uploading account retains ownership of the objects.

For more information about Amazon S3 object ownership, see [Controlling ownership of uploaded objects using S3 Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon Simple Storage Service User Guide* .

Shorthand Syntax:

```
type=string,location=string,path=string,namespaceType=string,name=string,packaging=string,overrideArtifactName=boolean,encryptionDisabled=boolean,artifactIdentifier=string,bucketOwnerAccess=string ...
```

JSON Syntax:

```
[
  {
    "type": "CODEPIPELINE"|"S3"|"NO_ARTIFACTS",
    "location": "string",
    "path": "string",
    "namespaceType": "NONE"|"BUILD_ID",
    "name": "string",
    "packaging": "NONE"|"ZIP",
    "overrideArtifactName": true|false,
    "encryptionDisabled": true|false,
    "artifactIdentifier": "string",
    "bucketOwnerAccess": "NONE"|"READ_ONLY"|"FULL"
  }
  ...
]
```

`--environment-variables-override` (list)

A set of environment variables that overrides, for this build only, the latest ones already defined in the build project.

(structure)

Information about an environment variable for a build project or a build.

name -> (string)

The name or key of the environment variable.

value -> (string)

The value of the environment variable.

### Warning

We strongly discourage the use of `PLAINTEXT` environment variables to store sensitive values, especially Amazon Web Services secret key IDs. `PLAINTEXT` environment variables can be displayed in plain text using the CodeBuild console and the CLI. For sensitive values, we recommend you use an environment variable of type `PARAMETER_STORE` or `SECRETS_MANAGER` .

type -> (string)

The type of environment variable. Valid values include:

- `PARAMETER_STORE` : An environment variable stored in Systems Manager Parameter Store. For environment variables of this type, specify the name of the parameter as the `value` of the EnvironmentVariable. The parameter value will be substituted for the name at runtime. You can also define Parameter Store environment variables in the buildspec. To learn how to do so, see [env/parameter-store](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec.env.parameter-store) in the *CodeBuild User Guide* .
- `PLAINTEXT` : An environment variable in plain text format. This is the default value.
- `SECRETS_MANAGER` : An environment variable stored in Secrets Manager. For environment variables of this type, specify the name of the secret as the `value` of the EnvironmentVariable. The secret value will be substituted for the name at runtime. You can also define Secrets Manager environment variables in the buildspec. To learn how to do so, see [env/secrets-manager](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec.env.secrets-manager) in the *CodeBuild User Guide* .

Shorthand Syntax:

```
name=string,value=string,type=string ...
```

JSON Syntax:

```
[
  {
    "name": "string",
    "value": "string",
    "type": "PLAINTEXT"|"PARAMETER_STORE"|"SECRETS_MANAGER"
  }
  ...
]
```

`--source-type-override` (string)

A source input type, for this build, that overrides the source input defined in the build project.

Possible values:

- `CODECOMMIT`
- `CODEPIPELINE`
- `GITHUB`
- `GITLAB`
- `GITLAB_SELF_MANAGED`
- `S3`
- `BITBUCKET`
- `GITHUB_ENTERPRISE`
- `NO_SOURCE`

`--source-location-override` (string)

A location that overrides, for this build, the source location for the one defined in the build project.

`--source-auth-override` (structure)

An authorization type for this build that overrides the one defined in the build project. This override applies only if the build projectâs source is BitBucket, GitHub, GitLab, or GitLab Self Managed.

type -> (string)

The authorization type to use. Valid options are OAUTH, CODECONNECTIONS, or SECRETS_MANAGER.

resource -> (string)

The resource value that applies to the specified authorization type.

Shorthand Syntax:

```
type=string,resource=string
```

JSON Syntax:

```
{
  "type": "OAUTH"|"CODECONNECTIONS"|"SECRETS_MANAGER",
  "resource": "string"
}
```

`--git-clone-depth-override` (integer)

The user-defined depth of history, with a minimum value of 0, that overrides, for this build only, any previous depth of history defined in the build project.

`--git-submodules-config-override` (structure)

Information about the Git submodules configuration for this build of an CodeBuild build project.

fetchSubmodules -> (boolean)

Set to true to fetch Git submodules for your CodeBuild build project.

Shorthand Syntax:

```
fetchSubmodules=boolean
```

JSON Syntax:

```
{
  "fetchSubmodules": true|false
}
```

`--buildspec-override` (string)

A buildspec file declaration that overrides the latest one defined in the build project, for this build only. The buildspec defined on the project is not changed.

If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in `CODEBUILD_SRC_DIR` environment variable, or the path to an S3 bucket. The bucket must be in the same Amazon Web Services Region as the build project. Specify the buildspec file using its ARN (for example, `arn:aws:s3:::my-codebuild-sample2/buildspec.yml` ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see [Buildspec File Name and Storage Location](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec-ref-name-storage) .

### Note

Since this property allows you to change the build commands that will run in the container, you should note that an IAM principal with the ability to call this API and set this parameter can override the default settings. Moreover, we encourage that you use a trustworthy buildspec location like a file in your source repository or a Amazon S3 bucket.

`--insecure-ssl-override` | `--no-insecure-ssl-override` (boolean)

Enable this flag to override the insecure SSL setting that is specified in the build project. The insecure SSL setting determines whether to ignore SSL warnings while connecting to the project source code. This override applies only if the buildâs source is GitHub Enterprise.

`--report-build-status-override` | `--no-report-build-status-override` (boolean)

Set to true to report to your source provider the status of a buildâs start and completion. If you use this option with a source provider other than GitHub, GitHub Enterprise, GitLab, GitLab Self Managed, or Bitbucket, an `invalidInputException` is thrown.

To be able to report the build status to the source provider, the user associated with the source provider must have write access to the repo. If the user does not have write access, the build status cannot be updated. For more information, see [Source provider access](https://docs.aws.amazon.com/codebuild/latest/userguide/access-tokens.html) in the *CodeBuild User Guide* .

### Note

The status of a build triggered by a webhook is always reported to your source provider.

`--build-status-config-override` (structure)

Contains information that defines how the build project reports the build status to the source provider. This option is only used when the source provider is `GITHUB` , `GITHUB_ENTERPRISE` , or `BITBUCKET` .

context -> (string)

Specifies the context of the build status CodeBuild sends to the source provider. The usage of this parameter depends on the source provider.

Bitbucket

This parameter is used for the `name` parameter in the Bitbucket commit status. For more information, see [build](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/commit/%7Bnode%7D/statuses/build) in the Bitbucket API documentation.

GitHub/GitHub Enterprise Server

This parameter is used for the `context` parameter in the GitHub commit status. For more information, see [Create a commit status](https://developer.github.com/v3/repos/statuses/#create-a-commit-status) in the GitHub developer guide.

targetUrl -> (string)

Specifies the target url of the build status CodeBuild sends to the source provider. The usage of this parameter depends on the source provider.

Bitbucket

This parameter is used for the `url` parameter in the Bitbucket commit status. For more information, see [build](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/commit/%7Bnode%7D/statuses/build) in the Bitbucket API documentation.

GitHub/GitHub Enterprise Server

This parameter is used for the `target_url` parameter in the GitHub commit status. For more information, see [Create a commit status](https://developer.github.com/v3/repos/statuses/#create-a-commit-status) in the GitHub developer guide.

Shorthand Syntax:

```
context=string,targetUrl=string
```

JSON Syntax:

```
{
  "context": "string",
  "targetUrl": "string"
}
```

`--environment-type-override` (string)

A container type for this build that overrides the one specified in the build project.

Possible values:

- `WINDOWS_CONTAINER`
- `LINUX_CONTAINER`
- `LINUX_GPU_CONTAINER`
- `ARM_CONTAINER`
- `WINDOWS_SERVER_2019_CONTAINER`
- `WINDOWS_SERVER_2022_CONTAINER`
- `LINUX_LAMBDA_CONTAINER`
- `ARM_LAMBDA_CONTAINER`
- `LINUX_EC2`
- `ARM_EC2`
- `WINDOWS_EC2`
- `MAC_ARM`

`--image-override` (string)

The name of an image for this build that overrides the one specified in the build project.

`--compute-type-override` (string)

The name of a compute type for this build that overrides the one specified in the build project.

Possible values:

- `BUILD_GENERAL1_SMALL`
- `BUILD_GENERAL1_MEDIUM`
- `BUILD_GENERAL1_LARGE`
- `BUILD_GENERAL1_XLARGE`
- `BUILD_GENERAL1_2XLARGE`
- `BUILD_LAMBDA_1GB`
- `BUILD_LAMBDA_2GB`
- `BUILD_LAMBDA_4GB`
- `BUILD_LAMBDA_8GB`
- `BUILD_LAMBDA_10GB`
- `ATTRIBUTE_BASED_COMPUTE`
- `CUSTOM_INSTANCE_TYPE`

`--certificate-override` (string)

The name of a certificate for this build that overrides the one specified in the build project.

`--cache-override` (structure)

A ProjectCache object specified for this build that overrides the one defined in the build project.

type -> (string)

The type of cache used by the build project. Valid values include:

- `NO_CACHE` : The build project does not use any cache.
- `S3` : The build project reads and writes from and to S3.
- `LOCAL` : The build project stores a cache locally on a build host that is only available to that build host.

location -> (string)

Information about the cache location:

- `NO_CACHE` or `LOCAL` : This value is ignored.
- `S3` : This is the S3 bucket name/prefix.

modes -> (list)

An array of strings that specify the local cache modes. You can use one or more local cache modes at the same time. This is only used for `LOCAL` cache types.

Possible values are:

LOCAL_SOURCE_CACHE

Caches Git metadata for primary and secondary sources. After the cache is created, subsequent builds pull only the change between commits. This mode is a good choice for projects with a clean working directory and a source that is a large Git repository. If you choose this option and your project does not use a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

LOCAL_DOCKER_LAYER_CACHE

Caches existing Docker layers. This mode is a good choice for projects that build or pull large Docker images. It can prevent the performance issues caused by pulling large Docker images down from the network.

### Note

- You can use a Docker layer cache in the Linux environment only.
- The `privileged` flag must be set so that your project has the required Docker permissions.
- You should consider the security implications before you use a Docker layer cache.

LOCAL_CUSTOM_CACHE

Caches directories you specify in the buildspec file. This mode is a good choice if your build scenario is not suited to one of the other three local cache modes. If you use a custom cache:

- Only directories can be specified for caching. You cannot specify individual files.
- Symlinks are used to reference cached directories.
- Cached directories are linked to your build before it downloads its project sources. Cached items are overridden if a source item has the same name. Directories are specified using cache paths in the buildspec file.

(string)

cacheNamespace -> (string)

Defines the scope of the cache. You can use this namespace to share a cache across multiple projects. For more information, see [Cache sharing between projects](https://docs.aws.amazon.com/codebuild/latest/userguide/caching-s3.html#caching-s3-sharing) in the *CodeBuild User Guide* .

Shorthand Syntax:

```
type=string,location=string,modes=string,string,cacheNamespace=string
```

JSON Syntax:

```
{
  "type": "NO_CACHE"|"S3"|"LOCAL",
  "location": "string",
  "modes": ["LOCAL_DOCKER_LAYER_CACHE"|"LOCAL_SOURCE_CACHE"|"LOCAL_CUSTOM_CACHE", ...],
  "cacheNamespace": "string"
}
```

`--service-role-override` (string)

The name of a service role for this build that overrides the one specified in the build project.

`--privileged-mode-override` | `--no-privileged-mode-override` (boolean)

Enable this flag to override privileged mode in the build project.

`--timeout-in-minutes-override` (integer)

The number of build timeout minutes, from 5 to 2160 (36 hours), that overrides, for this build only, the latest setting already defined in the build project.

`--queued-timeout-in-minutes-override` (integer)

The number of minutes a build is allowed to be queued before it times out.

`--encryption-key-override` (string)

The Key Management Service customer master key (CMK) that overrides the one specified in the build project. The CMK key encrypts the build output artifacts.

### Note

You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.

You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMKâs alias (using the format `alias/<alias-name>` ).

`--idempotency-token` (string)

A unique, case sensitive identifier you provide to ensure the idempotency of the StartBuild request. The token is included in the StartBuild request and is valid for 5 minutes. If you repeat the StartBuild request with the same token, but change a parameter, CodeBuild returns a parameter mismatch error.

`--logs-config-override` (structure)

Log settings for this build that override the log settings defined in the build project.

cloudWatchLogs -> (structure)

Information about CloudWatch Logs for a build project. CloudWatch Logs are enabled by default.

status -> (string)

The current status of the logs in CloudWatch Logs for a build project. Valid values are:

- `ENABLED` : CloudWatch Logs are enabled for this build project.
- `DISABLED` : CloudWatch Logs are not enabled for this build project.

groupName -> (string)

The group name of the logs in CloudWatch Logs. For more information, see [Working with Log Groups and Log Streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) .

streamName -> (string)

The prefix of the stream name of the CloudWatch Logs. For more information, see [Working with Log Groups and Log Streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) .

s3Logs -> (structure)

Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by default.

status -> (string)

The current status of the S3 build logs. Valid values are:

- `ENABLED` : S3 build logs are enabled for this build project.
- `DISABLED` : S3 build logs are not enabled for this build project.

location -> (string)

The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is `my-bucket` , and your path prefix is `build-log` , then acceptable formats are `my-bucket/build-log` or `arn:aws:s3:::my-bucket/build-log` .

encryptionDisabled -> (boolean)

Set to true if you do not want your S3 build log output encrypted. By default S3 build logs are encrypted.

bucketOwnerAccess -> (string)

Specifies the bucket ownerâs access for objects that another account uploads to their Amazon S3 bucket. By default, only the account that uploads the objects to the bucket has access to these objects. This property allows you to give the bucket owner access to these objects.

### Note

To use this property, your CodeBuild service role must have the `s3:PutBucketAcl` permission. This permission allows CodeBuild to modify the access control list for the bucket.

This property can be one of the following values:

NONE

The bucket owner does not have access to the objects. This is the default.

READ_ONLY

The bucket owner has read-only access to the objects. The uploading account retains ownership of the objects.

FULL

The bucket owner has full access to the objects. Object ownership is determined by the following criteria:

- If the bucket is configured with the **Bucket owner preferred** setting, the bucket owner owns the objects. The uploading account will have object access as specified by the bucketâs policy.
- Otherwise, the uploading account retains ownership of the objects.

For more information about Amazon S3 object ownership, see [Controlling ownership of uploaded objects using S3 Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon Simple Storage Service User Guide* .

Shorthand Syntax:

```
cloudWatchLogs={status=string,groupName=string,streamName=string},s3Logs={status=string,location=string,encryptionDisabled=boolean,bucketOwnerAccess=string}
```

JSON Syntax:

```
{
  "cloudWatchLogs": {
    "status": "ENABLED"|"DISABLED",
    "groupName": "string",
    "streamName": "string"
  },
  "s3Logs": {
    "status": "ENABLED"|"DISABLED",
    "location": "string",
    "encryptionDisabled": true|false,
    "bucketOwnerAccess": "NONE"|"READ_ONLY"|"FULL"
  }
}
```

`--registry-credential-override` (structure)

The credentials for access to a private registry.

credential -> (string)

The Amazon Resource Name (ARN) or name of credentials created using Secrets Manager.

### Note

The `credential` can use the name of the credentials only if they exist in your current Amazon Web Services Region.

credentialProvider -> (string)

The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for Secrets Manager.

Shorthand Syntax:

```
credential=string,credentialProvider=string
```

JSON Syntax:

```
{
  "credential": "string",
  "credentialProvider": "SECRETS_MANAGER"
}
```

`--image-pull-credentials-type-override` (string)

The type of credentials CodeBuild uses to pull images in your build. There are two valid values:

CODEBUILD

Specifies that CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust CodeBuildâs service principal.

SERVICE_ROLE

Specifies that CodeBuild uses your build projectâs service role.

When using a cross-account or private registry image, you must use `SERVICE_ROLE` credentials. When using an CodeBuild curated image, you must use `CODEBUILD` credentials.

Possible values:

- `CODEBUILD`
- `SERVICE_ROLE`

`--debug-session-enabled` | `--no-debug-session-enabled` (boolean)

Specifies if session debugging is enabled for this build. For more information, see [Viewing a running build in Session Manager](https://docs.aws.amazon.com/codebuild/latest/userguide/session-manager.html) .

`--fleet-override` (structure)

A ProjectFleet object specified for this build that overrides the one defined in the build project.

fleetArn -> (string)

Specifies the compute fleet ARN for the build project.

Shorthand Syntax:

```
fleetArn=string
```

JSON Syntax:

```
{
  "fleetArn": "string"
}
```

`--auto-retry-limit-override` (integer)

The maximum number of additional automatic retries after a failed build. For example, if the auto-retry limit is set to 2, CodeBuild will call the `RetryBuild` API to automatically retry your build for up to 2 additional times.

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

**To start running a build of an AWS CodeBuild build project.**

The following `start-build` example starts a build for the specified CodeBuild project. The build overrides both the projectâs setting for the number of minutes the build is allowed to be queued before it times out and the projectâs artifact settings.

```
aws codebuild start-build \
    --project-name "my-demo-project" \
    --queued-timeout-in-minutes-override 5 \
    --artifacts-override {"\"type\": \"S3\",\"location\": \"arn:aws:s3:::artifacts-override\",\"overrideArtifactName\":true"}
```

Output:

```
{
    "build": {
        "serviceRole": "arn:aws:iam::123456789012:role/service-role/my-codebuild-service-role",
        "buildStatus": "IN_PROGRESS",
        "buildComplete": false,
        "projectName": "my-demo-project",
        "timeoutInMinutes": 60,
        "source": {
            "insecureSsl": false,
            "type": "S3",
            "location": "codebuild-us-west-2-123456789012-input-bucket/my-source.zip"
        },
        "queuedTimeoutInMinutes": 5,
        "encryptionKey": "arn:aws:kms:us-west-2:123456789012:alias/aws/s3",
        "currentPhase": "QUEUED",
        "startTime": 1556905683.568,
        "environment": {
            "computeType": "BUILD_GENERAL1_MEDIUM",
            "environmentVariables": [],
            "type": "LINUX_CONTAINER",
            "privilegedMode": false,
            "image": "aws/codebuild/standard:1.0",
            "imagePullCredentialsType": "CODEBUILD"
        },
        "phases": [
            {
                "phaseStatus": "SUCCEEDED",
                "startTime": 1556905683.568,
                "phaseType": "SUBMITTED",
                "durationInSeconds": 0,
                "endTime": 1556905684.524
            },
            {
                "startTime": 1556905684.524,
                "phaseType": "QUEUED"
            }
        ],
        "logs": {
            "deepLink": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=null;stream=null"
        },
        "artifacts": {
            "encryptionDisabled": false,
            "location": "arn:aws:s3:::artifacts-override/my-demo-project",
            "overrideArtifactName": true
        },
        "cache": {
            "type": "NO_CACHE"
        },
        "id": "my-demo-project::12345678-a1b2-c3d4-e5f6-11111EXAMPLE",
        "initiator": "my-aws-account-name",
        "arn": "arn:aws:codebuild:us-west-2:123456789012:build/my-demo-project::12345678-a1b2-c3d4-e5f6-11111EXAMPLE"
    }
}
```

For more information, see [Run a Build (AWS CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/run-build.html#run-build-cli) in the *AWS CodeBuild User Guide*.

## Output

build -> (structure)

Information about the build to be run.

id -> (string)

The unique ID for the build.

arn -> (string)

The Amazon Resource Name (ARN) of the build.

buildNumber -> (long)

The number of the build. For each project, the `buildNumber` of its first build is `1` . The `buildNumber` of each subsequent build is incremented by `1` . If a build is deleted, the `buildNumber` of other builds does not change.

startTime -> (timestamp)

When the build process started, expressed in Unix time format.

endTime -> (timestamp)

When the build process ended, expressed in Unix time format.

currentPhase -> (string)

The current build phase.

buildStatus -> (string)

The current status of the build. Valid values include:

- `FAILED` : The build failed.
- `FAULT` : The build faulted.
- `IN_PROGRESS` : The build is still in progress.
- `STOPPED` : The build stopped.
- `SUCCEEDED` : The build succeeded.
- `TIMED_OUT` : The build timed out.

sourceVersion -> (string)

Any version identifier for the version of the source code to be built. If `sourceVersion` is specified at the project level, then this `sourceVersion` (at the build level) takes precedence.

For more information, see [Source Version Sample with CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html) in the *CodeBuild User Guide* .

resolvedSourceVersion -> (string)

An identifier for the version of this buildâs source code.

- For CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.
- For CodePipeline, the source revision provided by CodePipeline.
- For Amazon S3, this does not apply.

projectName -> (string)

The name of the CodeBuild project.

phases -> (list)

Information about all previous build phases that are complete and information about any current build phase that is not yet complete.

(structure)

Information about a stage for a build.

phaseType -> (string)

The name of the build phase. Valid values include:

BUILD

Core build activities typically occur in this build phase.

COMPLETED

The build has been completed.

DOWNLOAD_SOURCE

Source code is being downloaded in this build phase.

FINALIZING

The build process is completing in this build phase.

INSTALL

Installation activities typically occur in this build phase.

POST_BUILD

Post-build activities typically occur in this build phase.

PRE_BUILD

Pre-build activities typically occur in this build phase.

PROVISIONING

The build environment is being set up.

QUEUED

The build has been submitted and is queued behind other submitted builds.

SUBMITTED

The build has been submitted.

UPLOAD_ARTIFACTS

Build output artifacts are being uploaded to the output location.

phaseStatus -> (string)

The current status of the build phase. Valid values include:

FAILED

The build phase failed.

FAULT

The build phase faulted.

IN_PROGRESS

The build phase is still in progress.

STOPPED

The build phase stopped.

SUCCEEDED

The build phase succeeded.

TIMED_OUT

The build phase timed out.

startTime -> (timestamp)

When the build phase started, expressed in Unix time format.

endTime -> (timestamp)

When the build phase ended, expressed in Unix time format.

durationInSeconds -> (long)

How long, in seconds, between the starting and ending times of the buildâs phase.

contexts -> (list)

Additional information about a build phase, especially to help troubleshoot a failed build.

(structure)

Additional information about a build phase that has an error. You can use this information for troubleshooting.

statusCode -> (string)

The status code for the context of the build phase.

message -> (string)

An explanation of the build phaseâs context. This might include a command ID and an exit code.

source -> (structure)

Information about the source code to be built.

type -> (string)

The type of repository that contains the source code to be built. Valid values include:

- `BITBUCKET` : The source code is in a Bitbucket repository.
- `CODECOMMIT` : The source code is in an CodeCommit repository.
- `CODEPIPELINE` : The source code settings are specified in the source action of a pipeline in CodePipeline.
- `GITHUB` : The source code is in a GitHub repository.
- `GITHUB_ENTERPRISE` : The source code is in a GitHub Enterprise Server repository.
- `GITLAB` : The source code is in a GitLab repository.
- `GITLAB_SELF_MANAGED` : The source code is in a self-managed GitLab repository.
- `NO_SOURCE` : The project does not have input source code.
- `S3` : The source code is in an Amazon S3 bucket.

location -> (string)

Information about the location of the source code to be built. Valid values include:

- For source code settings that are specified in the source action of a pipeline in CodePipeline, `location` should not be specified. If it is specified, CodePipeline ignores it. This is because CodePipeline uses the settings in a pipelineâs source action instead of this value.
- For source code in an CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, `https://git-codecommit.<region-ID>.amazonaws.com/v1/repos/<repo-name>` ).
- For source code in an Amazon S3 input bucket, one of the following.
- The path to the ZIP file that contains the source code (for example, `<bucket-name>/<path>/<object-name>.zip` ).
- The path to the folder that contains the source code (for example, `<bucket-name>/<path-to-source-code>/<folder>/` ).
- For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your Amazon Web Services account to your GitHub account. Use the CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page, for **Organization access** , choose **Request access** next to each repository you want to allow CodeBuild to have access to, and then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the CodeBuild console.) To instruct CodeBuild to use this connection, in the `source` object, set the `auth` objectâs `type` value to `OAUTH` .
- For source code in an GitLab or self-managed GitLab repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your Amazon Web Services account to your GitLab account. Use the CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitLab, on the Connections **Authorize application** page, choose **Authorize** . Then on the CodeConnections **Create GitLab connection** page, choose **Connect to GitLab** . (After you have connected to your GitLab account, you do not need to finish creating the build project. You can leave the CodeBuild console.) To instruct CodeBuild to override the default connection and use this connection instead, set the `auth` objectâs `type` value to `CODECONNECTIONS` in the `source` object.
- For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your Amazon Web Services account to your Bitbucket account. Use the CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the CodeBuild console.) To instruct CodeBuild to use this connection, in the `source` object, set the `auth` objectâs `type` value to `OAUTH` .

If you specify `CODEPIPELINE` for the `Type` property, donât specify this property. For all of the other types, you must specify `Location` .

gitCloneDepth -> (integer)

Information about the Git clone depth for the build project.

gitSubmodulesConfig -> (structure)

Information about the Git submodules configuration for the build project.

fetchSubmodules -> (boolean)

Set to true to fetch Git submodules for your CodeBuild build project.

buildspec -> (string)

The buildspec file declaration to use for the builds in this build project.

If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in `CODEBUILD_SRC_DIR` environment variable, or the path to an S3 bucket. The bucket must be in the same Amazon Web Services Region as the build project. Specify the buildspec file using its ARN (for example, `arn:aws:s3:::my-codebuild-sample2/buildspec.yml` ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see [Buildspec File Name and Storage Location](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec-ref-name-storage) .

auth -> (structure)

Information about the authorization settings for CodeBuild to access the source code to be built.

type -> (string)

The authorization type to use. Valid options are OAUTH, CODECONNECTIONS, or SECRETS_MANAGER.

resource -> (string)

The resource value that applies to the specified authorization type.

reportBuildStatus -> (boolean)

Set to true to report the status of a buildâs start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, GitLab, GitLab Self Managed, GitLab, GitLab Self Managed, or Bitbucket. If this is set and you use a different source provider, an `invalidInputException` is thrown.

To be able to report the build status to the source provider, the user associated with the source provider must have write access to the repo. If the user does not have write access, the build status cannot be updated. For more information, see [Source provider access](https://docs.aws.amazon.com/codebuild/latest/userguide/access-tokens.html) in the *CodeBuild User Guide* .

The status of a build triggered by a webhook is always reported to your source provider.

If your projectâs builds are triggered by a webhook, you must push a new commit to the repo for a change to this property to take effect.

buildStatusConfig -> (structure)

Contains information that defines how the build project reports the build status to the source provider. This option is only used when the source provider is `GITHUB` , `GITHUB_ENTERPRISE` , or `BITBUCKET` .

context -> (string)

Specifies the context of the build status CodeBuild sends to the source provider. The usage of this parameter depends on the source provider.

Bitbucket

This parameter is used for the `name` parameter in the Bitbucket commit status. For more information, see [build](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/commit/%7Bnode%7D/statuses/build) in the Bitbucket API documentation.

GitHub/GitHub Enterprise Server

This parameter is used for the `context` parameter in the GitHub commit status. For more information, see [Create a commit status](https://developer.github.com/v3/repos/statuses/#create-a-commit-status) in the GitHub developer guide.

targetUrl -> (string)

Specifies the target url of the build status CodeBuild sends to the source provider. The usage of this parameter depends on the source provider.

Bitbucket

This parameter is used for the `url` parameter in the Bitbucket commit status. For more information, see [build](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/commit/%7Bnode%7D/statuses/build) in the Bitbucket API documentation.

GitHub/GitHub Enterprise Server

This parameter is used for the `target_url` parameter in the GitHub commit status. For more information, see [Create a commit status](https://developer.github.com/v3/repos/statuses/#create-a-commit-status) in the GitHub developer guide.

insecureSsl -> (boolean)

Enable this flag to ignore SSL warnings while connecting to the project source code.

sourceIdentifier -> (string)

An identifier for this project source. The identifier can only contain alphanumeric characters and underscores, and must be less than 128 characters in length.

secondarySources -> (list)

An array of `ProjectSource` objects.

(structure)

Information about the build input source code for the build project.

type -> (string)

The type of repository that contains the source code to be built. Valid values include:

- `BITBUCKET` : The source code is in a Bitbucket repository.
- `CODECOMMIT` : The source code is in an CodeCommit repository.
- `CODEPIPELINE` : The source code settings are specified in the source action of a pipeline in CodePipeline.
- `GITHUB` : The source code is in a GitHub repository.
- `GITHUB_ENTERPRISE` : The source code is in a GitHub Enterprise Server repository.
- `GITLAB` : The source code is in a GitLab repository.
- `GITLAB_SELF_MANAGED` : The source code is in a self-managed GitLab repository.
- `NO_SOURCE` : The project does not have input source code.
- `S3` : The source code is in an Amazon S3 bucket.

location -> (string)

Information about the location of the source code to be built. Valid values include:

- For source code settings that are specified in the source action of a pipeline in CodePipeline, `location` should not be specified. If it is specified, CodePipeline ignores it. This is because CodePipeline uses the settings in a pipelineâs source action instead of this value.
- For source code in an CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, `https://git-codecommit.<region-ID>.amazonaws.com/v1/repos/<repo-name>` ).
- For source code in an Amazon S3 input bucket, one of the following.
- The path to the ZIP file that contains the source code (for example, `<bucket-name>/<path>/<object-name>.zip` ).
- The path to the folder that contains the source code (for example, `<bucket-name>/<path-to-source-code>/<folder>/` ).
- For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your Amazon Web Services account to your GitHub account. Use the CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page, for **Organization access** , choose **Request access** next to each repository you want to allow CodeBuild to have access to, and then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the CodeBuild console.) To instruct CodeBuild to use this connection, in the `source` object, set the `auth` objectâs `type` value to `OAUTH` .
- For source code in an GitLab or self-managed GitLab repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your Amazon Web Services account to your GitLab account. Use the CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitLab, on the Connections **Authorize application** page, choose **Authorize** . Then on the CodeConnections **Create GitLab connection** page, choose **Connect to GitLab** . (After you have connected to your GitLab account, you do not need to finish creating the build project. You can leave the CodeBuild console.) To instruct CodeBuild to override the default connection and use this connection instead, set the `auth` objectâs `type` value to `CODECONNECTIONS` in the `source` object.
- For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your Amazon Web Services account to your Bitbucket account. Use the CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the CodeBuild console.) To instruct CodeBuild to use this connection, in the `source` object, set the `auth` objectâs `type` value to `OAUTH` .

If you specify `CODEPIPELINE` for the `Type` property, donât specify this property. For all of the other types, you must specify `Location` .

gitCloneDepth -> (integer)

Information about the Git clone depth for the build project.

gitSubmodulesConfig -> (structure)

Information about the Git submodules configuration for the build project.

fetchSubmodules -> (boolean)

Set to true to fetch Git submodules for your CodeBuild build project.

buildspec -> (string)

The buildspec file declaration to use for the builds in this build project.

If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in `CODEBUILD_SRC_DIR` environment variable, or the path to an S3 bucket. The bucket must be in the same Amazon Web Services Region as the build project. Specify the buildspec file using its ARN (for example, `arn:aws:s3:::my-codebuild-sample2/buildspec.yml` ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see [Buildspec File Name and Storage Location](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec-ref-name-storage) .

auth -> (structure)

Information about the authorization settings for CodeBuild to access the source code to be built.

type -> (string)

The authorization type to use. Valid options are OAUTH, CODECONNECTIONS, or SECRETS_MANAGER.

resource -> (string)

The resource value that applies to the specified authorization type.

reportBuildStatus -> (boolean)

Set to true to report the status of a buildâs start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, GitLab, GitLab Self Managed, GitLab, GitLab Self Managed, or Bitbucket. If this is set and you use a different source provider, an `invalidInputException` is thrown.

To be able to report the build status to the source provider, the user associated with the source provider must have write access to the repo. If the user does not have write access, the build status cannot be updated. For more information, see [Source provider access](https://docs.aws.amazon.com/codebuild/latest/userguide/access-tokens.html) in the *CodeBuild User Guide* .

The status of a build triggered by a webhook is always reported to your source provider.

If your projectâs builds are triggered by a webhook, you must push a new commit to the repo for a change to this property to take effect.

buildStatusConfig -> (structure)

Contains information that defines how the build project reports the build status to the source provider. This option is only used when the source provider is `GITHUB` , `GITHUB_ENTERPRISE` , or `BITBUCKET` .

context -> (string)

Specifies the context of the build status CodeBuild sends to the source provider. The usage of this parameter depends on the source provider.

Bitbucket

This parameter is used for the `name` parameter in the Bitbucket commit status. For more information, see [build](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/commit/%7Bnode%7D/statuses/build) in the Bitbucket API documentation.

GitHub/GitHub Enterprise Server

This parameter is used for the `context` parameter in the GitHub commit status. For more information, see [Create a commit status](https://developer.github.com/v3/repos/statuses/#create-a-commit-status) in the GitHub developer guide.

targetUrl -> (string)

Specifies the target url of the build status CodeBuild sends to the source provider. The usage of this parameter depends on the source provider.

Bitbucket

This parameter is used for the `url` parameter in the Bitbucket commit status. For more information, see [build](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/commit/%7Bnode%7D/statuses/build) in the Bitbucket API documentation.

GitHub/GitHub Enterprise Server

This parameter is used for the `target_url` parameter in the GitHub commit status. For more information, see [Create a commit status](https://developer.github.com/v3/repos/statuses/#create-a-commit-status) in the GitHub developer guide.

insecureSsl -> (boolean)

Enable this flag to ignore SSL warnings while connecting to the project source code.

sourceIdentifier -> (string)

An identifier for this project source. The identifier can only contain alphanumeric characters and underscores, and must be less than 128 characters in length.

secondarySourceVersions -> (list)

An array of `ProjectSourceVersion` objects. Each `ProjectSourceVersion` must be one of:

- For CodeCommit: the commit ID, branch, or Git tag to use.
- For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format `pr/pull-request-ID` (for example, `pr/25` ). If a branch name is specified, the branchâs HEAD commit ID is used. If not specified, the default branchâs HEAD commit ID is used.
- For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branchâs HEAD commit ID is used. If not specified, the default branchâs HEAD commit ID is used.
- For Amazon S3: the version ID of the object that represents the build input ZIP file to use.

(structure)

A source identifier and its corresponding version.

sourceIdentifier -> (string)

An identifier for a source in the build project. The identifier can only contain alphanumeric characters and underscores, and must be less than 128 characters in length.

sourceVersion -> (string)

The source version for the corresponding source identifier. If specified, must be one of:

- For CodeCommit: the commit ID, branch, or Git tag to use.
- For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format `pr/pull-request-ID` (for example, `pr/25` ). If a branch name is specified, the branchâs HEAD commit ID is used. If not specified, the default branchâs HEAD commit ID is used.
- For GitLab: the commit ID, branch, or Git tag to use.
- For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branchâs HEAD commit ID is used. If not specified, the default branchâs HEAD commit ID is used.
- For Amazon S3: the version ID of the object that represents the build input ZIP file to use.

For more information, see [Source Version Sample with CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html) in the *CodeBuild User Guide* .

artifacts -> (structure)

Information about the output artifacts for the build.

location -> (string)

Information about the location of the build artifacts.

sha256sum -> (string)

The SHA-256 hash of the build artifact.

You can use this hash along with a checksum tool to confirm file integrity and authenticity.

### Note

This value is available only if the build projectâs `packaging` value is set to `ZIP` .

md5sum -> (string)

The MD5 hash of the build artifact.

You can use this hash along with a checksum tool to confirm file integrity and authenticity.

### Note

This value is available only if the build projectâs `packaging` value is set to `ZIP` .

overrideArtifactName -> (boolean)

If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.

encryptionDisabled -> (boolean)

Information that tells you if encryption for build artifacts is disabled.

artifactIdentifier -> (string)

An identifier for this artifact definition.

bucketOwnerAccess -> (string)

Specifies the bucket ownerâs access for objects that another account uploads to their Amazon S3 bucket. By default, only the account that uploads the objects to the bucket has access to these objects. This property allows you to give the bucket owner access to these objects.

### Note

To use this property, your CodeBuild service role must have the `s3:PutBucketAcl` permission. This permission allows CodeBuild to modify the access control list for the bucket.

This property can be one of the following values:

NONE

The bucket owner does not have access to the objects. This is the default.

READ_ONLY

The bucket owner has read-only access to the objects. The uploading account retains ownership of the objects.

FULL

The bucket owner has full access to the objects. Object ownership is determined by the following criteria:

- If the bucket is configured with the **Bucket owner preferred** setting, the bucket owner owns the objects. The uploading account will have object access as specified by the bucketâs policy.
- Otherwise, the uploading account retains ownership of the objects.

For more information about Amazon S3 object ownership, see [Controlling ownership of uploaded objects using S3 Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon Simple Storage Service User Guide* .

secondaryArtifacts -> (list)

An array of `ProjectArtifacts` objects.

(structure)

Information about build output artifacts.

location -> (string)

Information about the location of the build artifacts.

sha256sum -> (string)

The SHA-256 hash of the build artifact.

You can use this hash along with a checksum tool to confirm file integrity and authenticity.

### Note

This value is available only if the build projectâs `packaging` value is set to `ZIP` .

md5sum -> (string)

The MD5 hash of the build artifact.

You can use this hash along with a checksum tool to confirm file integrity and authenticity.

### Note

This value is available only if the build projectâs `packaging` value is set to `ZIP` .

overrideArtifactName -> (boolean)

If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.

encryptionDisabled -> (boolean)

Information that tells you if encryption for build artifacts is disabled.

artifactIdentifier -> (string)

An identifier for this artifact definition.

bucketOwnerAccess -> (string)

Specifies the bucket ownerâs access for objects that another account uploads to their Amazon S3 bucket. By default, only the account that uploads the objects to the bucket has access to these objects. This property allows you to give the bucket owner access to these objects.

### Note

To use this property, your CodeBuild service role must have the `s3:PutBucketAcl` permission. This permission allows CodeBuild to modify the access control list for the bucket.

This property can be one of the following values:

NONE

The bucket owner does not have access to the objects. This is the default.

READ_ONLY

The bucket owner has read-only access to the objects. The uploading account retains ownership of the objects.

FULL

The bucket owner has full access to the objects. Object ownership is determined by the following criteria:

- If the bucket is configured with the **Bucket owner preferred** setting, the bucket owner owns the objects. The uploading account will have object access as specified by the bucketâs policy.
- Otherwise, the uploading account retains ownership of the objects.

For more information about Amazon S3 object ownership, see [Controlling ownership of uploaded objects using S3 Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon Simple Storage Service User Guide* .

cache -> (structure)

Information about the cache for the build.

type -> (string)

The type of cache used by the build project. Valid values include:

- `NO_CACHE` : The build project does not use any cache.
- `S3` : The build project reads and writes from and to S3.
- `LOCAL` : The build project stores a cache locally on a build host that is only available to that build host.

location -> (string)

Information about the cache location:

- `NO_CACHE` or `LOCAL` : This value is ignored.
- `S3` : This is the S3 bucket name/prefix.

modes -> (list)

An array of strings that specify the local cache modes. You can use one or more local cache modes at the same time. This is only used for `LOCAL` cache types.

Possible values are:

LOCAL_SOURCE_CACHE

Caches Git metadata for primary and secondary sources. After the cache is created, subsequent builds pull only the change between commits. This mode is a good choice for projects with a clean working directory and a source that is a large Git repository. If you choose this option and your project does not use a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

LOCAL_DOCKER_LAYER_CACHE

Caches existing Docker layers. This mode is a good choice for projects that build or pull large Docker images. It can prevent the performance issues caused by pulling large Docker images down from the network.

### Note

- You can use a Docker layer cache in the Linux environment only.
- The `privileged` flag must be set so that your project has the required Docker permissions.
- You should consider the security implications before you use a Docker layer cache.

LOCAL_CUSTOM_CACHE

Caches directories you specify in the buildspec file. This mode is a good choice if your build scenario is not suited to one of the other three local cache modes. If you use a custom cache:

- Only directories can be specified for caching. You cannot specify individual files.
- Symlinks are used to reference cached directories.
- Cached directories are linked to your build before it downloads its project sources. Cached items are overridden if a source item has the same name. Directories are specified using cache paths in the buildspec file.

(string)

cacheNamespace -> (string)

Defines the scope of the cache. You can use this namespace to share a cache across multiple projects. For more information, see [Cache sharing between projects](https://docs.aws.amazon.com/codebuild/latest/userguide/caching-s3.html#caching-s3-sharing) in the *CodeBuild User Guide* .

environment -> (structure)

Information about the build environment for this build.

type -> (string)

The type of build environment to use for related builds.

### Note

If youâre using compute fleets during project creation, `type` will be ignored.

For more information, see [Build environment compute types](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html) in the *CodeBuild user guide* .

image -> (string)

The image tag or image digest that identifies the Docker image to use for this build project. Use the following formats:

- For an image tag: `<registry>/<repository>:<tag>` . For example, in the Docker repository that CodeBuild uses to manage its Docker images, this would be `aws/codebuild/standard:4.0` .
- For an image digest: `<registry>/<repository>@<digest>` . For example, to specify an image with the digest âsha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf,â use `<registry>/<repository>@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf` .

For more information, see [Docker images provided by CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available.html) in the *CodeBuild user guide* .

computeType -> (string)

Information about the compute resources the build project uses. Available values include:

- `ATTRIBUTE_BASED_COMPUTE` : Specify the amount of vCPUs, memory, disk space, and the type of machine.

### Note

If you use `ATTRIBUTE_BASED_COMPUTE` , you must define your attributes by using `computeConfiguration` . CodeBuild will select the cheapest instance that satisfies your specified attributes. For more information, see [Reserved capacity environment types](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html#environment-reserved-capacity.types) in the *CodeBuild User Guide* .

- `BUILD_GENERAL1_SMALL` : Use up to 4 GiB memory and 2 vCPUs for builds.
- `BUILD_GENERAL1_MEDIUM` : Use up to 8 GiB memory and 4 vCPUs for builds.
- `BUILD_GENERAL1_LARGE` : Use up to 16 GiB memory and 8 vCPUs for builds, depending on your environment type.
- `BUILD_GENERAL1_XLARGE` : Use up to 72 GiB memory and 36 vCPUs for builds, depending on your environment type.
- `BUILD_GENERAL1_2XLARGE` : Use up to 144 GiB memory, 72 vCPUs, and 824 GB of SSD storage for builds. This compute type supports Docker images up to 100 GB uncompressed.
- `BUILD_LAMBDA_1GB` : Use up to 1 GiB memory for builds. Only available for environment type `LINUX_LAMBDA_CONTAINER` and `ARM_LAMBDA_CONTAINER` .
- `BUILD_LAMBDA_2GB` : Use up to 2 GiB memory for builds. Only available for environment type `LINUX_LAMBDA_CONTAINER` and `ARM_LAMBDA_CONTAINER` .
- `BUILD_LAMBDA_4GB` : Use up to 4 GiB memory for builds. Only available for environment type `LINUX_LAMBDA_CONTAINER` and `ARM_LAMBDA_CONTAINER` .
- `BUILD_LAMBDA_8GB` : Use up to 8 GiB memory for builds. Only available for environment type `LINUX_LAMBDA_CONTAINER` and `ARM_LAMBDA_CONTAINER` .
- `BUILD_LAMBDA_10GB` : Use up to 10 GiB memory for builds. Only available for environment type `LINUX_LAMBDA_CONTAINER` and `ARM_LAMBDA_CONTAINER` .

If you use `BUILD_GENERAL1_SMALL` :

- For environment type `LINUX_CONTAINER` , you can use up to 4 GiB memory and 2 vCPUs for builds.
- For environment type `LINUX_GPU_CONTAINER` , you can use up to 16 GiB memory, 4 vCPUs, and 1 NVIDIA A10G Tensor Core GPU for builds.
- For environment type `ARM_CONTAINER` , you can use up to 4 GiB memory and 2 vCPUs on ARM-based processors for builds.

If you use `BUILD_GENERAL1_LARGE` :

- For environment type `LINUX_CONTAINER` , you can use up to 16 GiB memory and 8 vCPUs for builds.
- For environment type `LINUX_GPU_CONTAINER` , you can use up to 255 GiB memory, 32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.
- For environment type `ARM_CONTAINER` , you can use up to 16 GiB memory and 8 vCPUs on ARM-based processors for builds.

For more information, see [On-demand environment types](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html#environment.types) in the *CodeBuild User Guide.*

computeConfiguration -> (structure)

The compute configuration of the build project. This is only required if `computeType` is set to `ATTRIBUTE_BASED_COMPUTE` .

vCpu -> (long)

The number of vCPUs of the instance type included in your fleet.

memory -> (long)

The amount of memory of the instance type included in your fleet.

disk -> (long)

The amount of disk space of the instance type included in your fleet.

machineType -> (string)

The machine type of the instance type included in your fleet.

instanceType -> (string)

The EC2 instance type to be launched in your fleet.

fleet -> (structure)

A ProjectFleet object to use for this build project.

fleetArn -> (string)

Specifies the compute fleet ARN for the build project.

environmentVariables -> (list)

A set of environment variables to make available to builds for this build project.

(structure)

Information about an environment variable for a build project or a build.

name -> (string)

The name or key of the environment variable.

value -> (string)

The value of the environment variable.

### Warning

We strongly discourage the use of `PLAINTEXT` environment variables to store sensitive values, especially Amazon Web Services secret key IDs. `PLAINTEXT` environment variables can be displayed in plain text using the CodeBuild console and the CLI. For sensitive values, we recommend you use an environment variable of type `PARAMETER_STORE` or `SECRETS_MANAGER` .

type -> (string)

The type of environment variable. Valid values include:

- `PARAMETER_STORE` : An environment variable stored in Systems Manager Parameter Store. For environment variables of this type, specify the name of the parameter as the `value` of the EnvironmentVariable. The parameter value will be substituted for the name at runtime. You can also define Parameter Store environment variables in the buildspec. To learn how to do so, see [env/parameter-store](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec.env.parameter-store) in the *CodeBuild User Guide* .
- `PLAINTEXT` : An environment variable in plain text format. This is the default value.
- `SECRETS_MANAGER` : An environment variable stored in Secrets Manager. For environment variables of this type, specify the name of the secret as the `value` of the EnvironmentVariable. The secret value will be substituted for the name at runtime. You can also define Secrets Manager environment variables in the buildspec. To learn how to do so, see [env/secrets-manager](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec.env.secrets-manager) in the *CodeBuild User Guide* .

privilegedMode -> (boolean)

Enables running the Docker daemon inside a Docker container. Set to true only if the build project is used to build Docker images. Otherwise, a build that attempts to interact with the Docker daemon fails. The default setting is `false` .

You can initialize the Docker daemon during the install phase of your build by adding one of the following sets of commands to the install phase of your buildspec file:

If the operating systemâs base image is Ubuntu Linux:

`- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&`

`- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"`

If the operating systemâs base image is Alpine Linux and the previous command does not work, add the `-t` argument to `timeout` :

`- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&`

`- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"`

certificate -> (string)

The ARN of the Amazon S3 bucket, path prefix, and object key that contains the PEM-encoded certificate for the build project. For more information, see [certificate](https://docs.aws.amazon.com/codebuild/latest/userguide/create-project-cli.html#cli.environment.certificate) in the *CodeBuild User Guide* .

registryCredential -> (structure)

The credentials for access to a private registry.

credential -> (string)

The Amazon Resource Name (ARN) or name of credentials created using Secrets Manager.

### Note

The `credential` can use the name of the credentials only if they exist in your current Amazon Web Services Region.

credentialProvider -> (string)

The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for Secrets Manager.

imagePullCredentialsType -> (string)

The type of credentials CodeBuild uses to pull images in your build. There are two valid values:

- `CODEBUILD` specifies that CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust CodeBuild service principal.
- `SERVICE_ROLE` specifies that CodeBuild uses your build projectâs service role.

When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an CodeBuild curated image, you must use CODEBUILD credentials.

dockerServer -> (structure)

A DockerServer object to use for this build project.

computeType -> (string)

Information about the compute resources the docker server uses. Available values include:

- `BUILD_GENERAL1_SMALL` : Use up to 4 GiB memory and 2 vCPUs for your docker server.
- `BUILD_GENERAL1_MEDIUM` : Use up to 8 GiB memory and 4 vCPUs for your docker server.
- `BUILD_GENERAL1_LARGE` : Use up to 16 GiB memory and 8 vCPUs for your docker server.
- `BUILD_GENERAL1_XLARGE` : Use up to 64 GiB memory and 32 vCPUs for your docker server.
- `BUILD_GENERAL1_2XLARGE` : Use up to 128 GiB memory and 64 vCPUs for your docker server.

securityGroupIds -> (list)

A list of one or more security groups IDs.

### Note

Security groups configured for Docker servers should allow ingress network traffic from the VPC configured in the project. They should allow ingress on port 9876.

(string)

status -> (structure)

A DockerServerStatus object to use for this docker server.

status -> (string)

The status of the docker server.

message -> (string)

A message associated with the status of a docker server.

serviceRole -> (string)

The name of a service role used for this build.

logs -> (structure)

Information about the buildâs logs in CloudWatch Logs.

groupName -> (string)

The name of the CloudWatch Logs group for the build logs.

streamName -> (string)

The name of the CloudWatch Logs stream for the build logs.

deepLink -> (string)

The URL to an individual build log in CloudWatch Logs. The log stream is created during the PROVISIONING phase of a build and the `deeplink` will not be valid until it is created.

s3DeepLink -> (string)

The URL to a build log in an S3 bucket.

cloudWatchLogsArn -> (string)

The ARN of the CloudWatch Logs stream for a build execution. Its format is `arn:${Partition}:logs:${Region}:${Account}:log-group:${LogGroupName}:log-stream:${LogStreamName}` . The CloudWatch Logs stream is created during the PROVISIONING phase of a build and the ARN will not be valid until it is created. For more information, see [Resources Defined by CloudWatch Logs](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatchlogs.html#amazoncloudwatchlogs-resources-for-iam-policies) .

s3LogsArn -> (string)

The ARN of S3 logs for a build project. Its format is `arn:${Partition}:s3:::${BucketName}/${ObjectName}` . For more information, see [Resources Defined by Amazon S3](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html#amazons3-resources-for-iam-policies) .

cloudWatchLogs -> (structure)

Information about CloudWatch Logs for a build project.

status -> (string)

The current status of the logs in CloudWatch Logs for a build project. Valid values are:

- `ENABLED` : CloudWatch Logs are enabled for this build project.
- `DISABLED` : CloudWatch Logs are not enabled for this build project.

groupName -> (string)

The group name of the logs in CloudWatch Logs. For more information, see [Working with Log Groups and Log Streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) .

streamName -> (string)

The prefix of the stream name of the CloudWatch Logs. For more information, see [Working with Log Groups and Log Streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) .

s3Logs -> (structure)

Information about S3 logs for a build project.

status -> (string)

The current status of the S3 build logs. Valid values are:

- `ENABLED` : S3 build logs are enabled for this build project.
- `DISABLED` : S3 build logs are not enabled for this build project.

location -> (string)

The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is `my-bucket` , and your path prefix is `build-log` , then acceptable formats are `my-bucket/build-log` or `arn:aws:s3:::my-bucket/build-log` .

encryptionDisabled -> (boolean)

Set to true if you do not want your S3 build log output encrypted. By default S3 build logs are encrypted.

bucketOwnerAccess -> (string)

Specifies the bucket ownerâs access for objects that another account uploads to their Amazon S3 bucket. By default, only the account that uploads the objects to the bucket has access to these objects. This property allows you to give the bucket owner access to these objects.

### Note

To use this property, your CodeBuild service role must have the `s3:PutBucketAcl` permission. This permission allows CodeBuild to modify the access control list for the bucket.

This property can be one of the following values:

NONE

The bucket owner does not have access to the objects. This is the default.

READ_ONLY

The bucket owner has read-only access to the objects. The uploading account retains ownership of the objects.

FULL

The bucket owner has full access to the objects. Object ownership is determined by the following criteria:

- If the bucket is configured with the **Bucket owner preferred** setting, the bucket owner owns the objects. The uploading account will have object access as specified by the bucketâs policy.
- Otherwise, the uploading account retains ownership of the objects.

For more information about Amazon S3 object ownership, see [Controlling ownership of uploaded objects using S3 Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon Simple Storage Service User Guide* .

timeoutInMinutes -> (integer)

How long, in minutes, from 5 to 2160 (36 hours), for CodeBuild to wait before timing out this build if it does not get marked as completed.

queuedTimeoutInMinutes -> (integer)

The number of minutes a build is allowed to be queued before it times out.

buildComplete -> (boolean)

Whether the build is complete. True if complete; otherwise, false.

initiator -> (string)

The entity that started the build. Valid values include:

- If CodePipeline started the build, the pipelineâs name (for example, `codepipeline/my-demo-pipeline` ).
- If a user started the build, the userâs name (for example, `MyUserName` ).
- If the Jenkins plugin for CodeBuild started the build, the string `CodeBuild-Jenkins-Plugin` .

vpcConfig -> (structure)

If your CodeBuild project accesses resources in an Amazon VPC, you provide this parameter that identifies the VPC ID and the list of security group IDs and subnet IDs. The security groups and subnets must belong to the same VPC. You must provide at least one security group and one subnet ID.

vpcId -> (string)

The ID of the Amazon VPC.

subnets -> (list)

A list of one or more subnet IDs in your Amazon VPC.

(string)

securityGroupIds -> (list)

A list of one or more security groups IDs in your Amazon VPC.

(string)

networkInterface -> (structure)

Describes a network interface.

subnetId -> (string)

The ID of the subnet.

networkInterfaceId -> (string)

The ID of the network interface.

encryptionKey -> (string)

The Key Management Service customer master key (CMK) to be used for encrypting the build output artifacts.

### Note

You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.

You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMKâs alias (using the format `alias/<alias-name>` ).

exportedEnvironmentVariables -> (list)

A list of exported environment variables for this build.

Exported environment variables are used in conjunction with CodePipeline to export environment variables from the current build stage to subsequent stages in the pipeline. For more information, see [Working with variables](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-variables.html) in the *CodePipeline User Guide* .

(structure)

Contains information about an exported environment variable.

Exported environment variables are used in conjunction with CodePipeline to export environment variables from the current build stage to subsequent stages in the pipeline. For more information, see [Working with variables](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-variables.html) in the *CodePipeline User Guide* .

### Note

During a build, the value of a variable is available starting with the `install` phase. It can be updated between the start of the `install` phase and the end of the `post_build` phase. After the `post_build` phase ends, the value of exported variables cannot change.

name -> (string)

The name of the exported environment variable.

value -> (string)

The value assigned to the exported environment variable.

reportArns -> (list)

An array of the ARNs associated with this buildâs reports.

(string)

fileSystemLocations -> (list)

An array of `ProjectFileSystemLocation` objects for a CodeBuild build project. A `ProjectFileSystemLocation` object specifies the `identifier` , `location` , `mountOptions` , `mountPoint` , and `type` of a file system created using Amazon Elastic File System.

(structure)

Information about a file system created by Amazon Elastic File System (EFS). For more information, see [What Is Amazon Elastic File System?](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)

type -> (string)

The type of the file system. The one supported type is `EFS` .

location -> (string)

A string that specifies the location of the file system created by Amazon EFS. Its format is `efs-dns-name:/directory-path` . You can find the DNS name of file system when you view it in the Amazon EFS console. The directory path is a path to a directory in the file system that CodeBuild mounts. For example, if the DNS name of a file system is `fs-abcd1234.efs.us-west-2.amazonaws.com` , and its mount directory is `my-efs-mount-directory` , then the `location` is `fs-abcd1234.efs.us-west-2.amazonaws.com:/my-efs-mount-directory` .

The directory path in the format `efs-dns-name:/directory-path` is optional. If you do not specify a directory path, the location is only the DNS name and CodeBuild mounts the entire file system.

mountPoint -> (string)

The location in the container where you mount the file system.

identifier -> (string)

The name used to access a file system created by Amazon EFS. CodeBuild creates an environment variable by appending the `identifier` in all capital letters to `CODEBUILD_` . For example, if you specify `my_efs` for `identifier` , a new environment variable is create named `CODEBUILD_MY_EFS` .

The `identifier` is used to mount your file system.

mountOptions -> (string)

The mount options for a file system created by Amazon EFS. The default mount options used by CodeBuild are `nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2` . For more information, see [Recommended NFS Mount Options](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-nfs-mount-settings.html) .

debugSession -> (structure)

Contains information about the debug session for this build.

sessionEnabled -> (boolean)

Specifies if session debugging is enabled for this build.

sessionTarget -> (string)

Contains the identifier of the Session Manager session used for the build. To work with the paused build, you open this session to examine, control, and resume the build.

buildBatchArn -> (string)

The ARN of the batch build that this build is a member of, if applicable.

autoRetryConfig -> (structure)

Information about the auto-retry configuration for the build.

autoRetryLimit -> (integer)

The maximum number of additional automatic retries after a failed build. For example, if the auto-retry limit is set to 2, CodeBuild will call the `RetryBuild` API to automatically retry your build for up to 2 additional times.

autoRetryNumber -> (integer)

The number of times that the build has been retried. The initial build will have an auto-retry number of 0.

nextAutoRetry -> (string)

The build ARN of the auto-retried build triggered by the current build. The next auto-retry will be `null` for builds that donât trigger an auto-retry.

previousAutoRetry -> (string)

The build ARN of the build that triggered the current auto-retry build. The previous auto-retry will be `null` for the initial build.