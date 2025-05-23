# update-projectÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/update-project.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/update-project.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codebuild](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/index.html#cli-aws-codebuild) ]

# update-project

## Description

Changes the settings of a build project.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/UpdateProject)

## Synopsis

```
update-project
--name <value>
[--description <value>]
[--source <value>]
[--secondary-sources <value>]
[--source-version <value>]
[--secondary-source-versions <value>]
[--artifacts <value>]
[--secondary-artifacts <value>]
[--cache <value>]
[--environment <value>]
[--service-role <value>]
[--timeout-in-minutes <value>]
[--queued-timeout-in-minutes <value>]
[--encryption-key <value>]
[--tags <value>]
[--vpc-config <value>]
[--badge-enabled | --no-badge-enabled]
[--logs-config <value>]
[--file-system-locations <value>]
[--build-batch-config <value>]
[--concurrent-build-limit <value>]
[--auto-retry-limit <value>]
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

`--name` (string)

The name of the build project.

### Note

You cannot change a build projectâs name.

`--description` (string)

A new or replacement description of the build project.

`--source` (structure)

Information to be changed about the build input source code for the build project.

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
type=string,location=string,gitCloneDepth=integer,gitSubmodulesConfig={fetchSubmodules=boolean},buildspec=string,auth={type=string,resource=string},reportBuildStatus=boolean,buildStatusConfig={context=string,targetUrl=string},insecureSsl=boolean,sourceIdentifier=string
```

JSON Syntax:

```
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
```

`--secondary-sources` (list)

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

`--source-version` (string)

A version of the build input to be built for this project. If not specified, the latest version is used. If specified, it must be one of:

- For CodeCommit: the commit ID, branch, or Git tag to use.
- For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format `pr/pull-request-ID` (for example `pr/25` ). If a branch name is specified, the branchâs HEAD commit ID is used. If not specified, the default branchâs HEAD commit ID is used.
- For GitLab: the commit ID, branch, or Git tag to use.
- For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branchâs HEAD commit ID is used. If not specified, the default branchâs HEAD commit ID is used.
- For Amazon S3: the version ID of the object that represents the build input ZIP file to use.

If `sourceVersion` is specified at the build level, then that version takes precedence over this `sourceVersion` (at the project level).

For more information, see [Source Version Sample with CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html) in the *CodeBuild User Guide* .

`--secondary-source-versions` (list)

An array of `ProjectSourceVersion` objects. If `secondarySourceVersions` is specified at the build level, then they take over these `secondarySourceVersions` (at the project level).

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

`--artifacts` (structure)

Information to be changed about the build output artifacts for the build project.

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

`--secondary-artifacts` (list)

An array of `ProjectArtifact` objects.

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

`--cache` (structure)

Stores recently used information so that it can be quickly accessed at a later time.

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

`--environment` (structure)

Information to be changed about the build environment for the build project.

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

Shorthand Syntax:

```
type=string,image=string,computeType=string,computeConfiguration={vCpu=long,memory=long,disk=long,machineType=string,instanceType=string},fleet={fleetArn=string},environmentVariables=[{name=string,value=string,type=string},{name=string,value=string,type=string}],privilegedMode=boolean,certificate=string,registryCredential={credential=string,credentialProvider=string},imagePullCredentialsType=string,dockerServer={computeType=string,securityGroupIds=[string,string],status={status=string,message=string}}
```

JSON Syntax:

```
{
  "type": "WINDOWS_CONTAINER"|"LINUX_CONTAINER"|"LINUX_GPU_CONTAINER"|"ARM_CONTAINER"|"WINDOWS_SERVER_2019_CONTAINER"|"WINDOWS_SERVER_2022_CONTAINER"|"LINUX_LAMBDA_CONTAINER"|"ARM_LAMBDA_CONTAINER"|"LINUX_EC2"|"ARM_EC2"|"WINDOWS_EC2"|"MAC_ARM",
  "image": "string",
  "computeType": "BUILD_GENERAL1_SMALL"|"BUILD_GENERAL1_MEDIUM"|"BUILD_GENERAL1_LARGE"|"BUILD_GENERAL1_XLARGE"|"BUILD_GENERAL1_2XLARGE"|"BUILD_LAMBDA_1GB"|"BUILD_LAMBDA_2GB"|"BUILD_LAMBDA_4GB"|"BUILD_LAMBDA_8GB"|"BUILD_LAMBDA_10GB"|"ATTRIBUTE_BASED_COMPUTE"|"CUSTOM_INSTANCE_TYPE",
  "computeConfiguration": {
    "vCpu": long,
    "memory": long,
    "disk": long,
    "machineType": "GENERAL"|"NVME",
    "instanceType": "string"
  },
  "fleet": {
    "fleetArn": "string"
  },
  "environmentVariables": [
    {
      "name": "string",
      "value": "string",
      "type": "PLAINTEXT"|"PARAMETER_STORE"|"SECRETS_MANAGER"
    }
    ...
  ],
  "privilegedMode": true|false,
  "certificate": "string",
  "registryCredential": {
    "credential": "string",
    "credentialProvider": "SECRETS_MANAGER"
  },
  "imagePullCredentialsType": "CODEBUILD"|"SERVICE_ROLE",
  "dockerServer": {
    "computeType": "BUILD_GENERAL1_SMALL"|"BUILD_GENERAL1_MEDIUM"|"BUILD_GENERAL1_LARGE"|"BUILD_GENERAL1_XLARGE"|"BUILD_GENERAL1_2XLARGE"|"BUILD_LAMBDA_1GB"|"BUILD_LAMBDA_2GB"|"BUILD_LAMBDA_4GB"|"BUILD_LAMBDA_8GB"|"BUILD_LAMBDA_10GB"|"ATTRIBUTE_BASED_COMPUTE"|"CUSTOM_INSTANCE_TYPE",
    "securityGroupIds": ["string", ...],
    "status": {
      "status": "string",
      "message": "string"
    }
  }
}
```

`--service-role` (string)

The replacement ARN of the IAM role that enables CodeBuild to interact with dependent Amazon Web Services services on behalf of the Amazon Web Services account.

`--timeout-in-minutes` (integer)

The replacement value in minutes, from 5 to 2160 (36 hours), for CodeBuild to wait before timing out any related build that did not get marked as completed.

`--queued-timeout-in-minutes` (integer)

The number of minutes a build is allowed to be queued before it times out.

`--encryption-key` (string)

The Key Management Service customer master key (CMK) to be used for encrypting the build output artifacts.

### Note

You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.

You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMKâs alias (using the format `alias/<alias-name>` ).

`--tags` (list)

An updated list of tag key and value pairs associated with this build project.

These tags are available for use by Amazon Web Services services that support CodeBuild build project tags.

(structure)

A tag, consisting of a key and a value.

This tag is available for use by Amazon Web Services services that support tags in CodeBuild.

key -> (string)

The tagâs key.

value -> (string)

The tagâs value.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
  }
  ...
]
```

`--vpc-config` (structure)

VpcConfig enables CodeBuild to access resources in an Amazon VPC.

vpcId -> (string)

The ID of the Amazon VPC.

subnets -> (list)

A list of one or more subnet IDs in your Amazon VPC.

(string)

securityGroupIds -> (list)

A list of one or more security groups IDs in your Amazon VPC.

(string)

Shorthand Syntax:

```
vpcId=string,subnets=string,string,securityGroupIds=string,string
```

JSON Syntax:

```
{
  "vpcId": "string",
  "subnets": ["string", ...],
  "securityGroupIds": ["string", ...]
}
```

`--badge-enabled` | `--no-badge-enabled` (boolean)

Set this to true to generate a publicly accessible URL for your projectâs build badge.

`--logs-config` (structure)

Information about logs for the build project. A project can create logs in CloudWatch Logs, logs in an S3 bucket, or both.

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

`--file-system-locations` (list)

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

Shorthand Syntax:

```
type=string,location=string,mountPoint=string,identifier=string,mountOptions=string ...
```

JSON Syntax:

```
[
  {
    "type": "EFS",
    "location": "string",
    "mountPoint": "string",
    "identifier": "string",
    "mountOptions": "string"
  }
  ...
]
```

`--build-batch-config` (structure)

Contains configuration information about a batch build project.

serviceRole -> (string)

Specifies the service role ARN for the batch build project.

combineArtifacts -> (boolean)

Specifies if the build artifacts for the batch build should be combined into a single artifact location.

restrictions -> (structure)

A `BatchRestrictions` object that specifies the restrictions for the batch build.

maximumBuildsAllowed -> (integer)

Specifies the maximum number of builds allowed.

computeTypesAllowed -> (list)

An array of strings that specify the compute types that are allowed for the batch build. See [Build environment compute types](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html) in the *CodeBuild User Guide* for these values.

(string)

fleetsAllowed -> (list)

An array of strings that specify the fleets that are allowed for the batch build. See [Run builds on reserved capacity fleets](https://docs.aws.amazon.com/codebuild/latest/userguide/fleets.html) in the *CodeBuild User Guide* for more information.

(string)

timeoutInMins -> (integer)

Specifies the maximum amount of time, in minutes, that the batch build must be completed in.

batchReportMode -> (string)

Specifies how build status reports are sent to the source provider for the batch build. This property is only used when the source provider for your project is Bitbucket, GitHub, or GitHub Enterprise, and your project is configured to report build statuses to the source provider.

REPORT_AGGREGATED_BATCH

(Default) Aggregate all of the build statuses into a single status report.

REPORT_INDIVIDUAL_BUILDS

Send a separate status report for each individual build.

Shorthand Syntax:

```
serviceRole=string,combineArtifacts=boolean,restrictions={maximumBuildsAllowed=integer,computeTypesAllowed=[string,string],fleetsAllowed=[string,string]},timeoutInMins=integer,batchReportMode=string
```

JSON Syntax:

```
{
  "serviceRole": "string",
  "combineArtifacts": true|false,
  "restrictions": {
    "maximumBuildsAllowed": integer,
    "computeTypesAllowed": ["string", ...],
    "fleetsAllowed": ["string", ...]
  },
  "timeoutInMins": integer,
  "batchReportMode": "REPORT_INDIVIDUAL_BUILDS"|"REPORT_AGGREGATED_BATCH"
}
```

`--concurrent-build-limit` (integer)

The maximum number of concurrent builds that are allowed for this project.

New builds are only started if the current number of builds is less than or equal to this limit. If the current build count meets this limit, new builds are throttled and are not run.

To remove this limit, set this value to -1.

`--auto-retry-limit` (integer)

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

**To change an AWS CodeBuild build projectâs settings.**

The following `update-project` example changes the settings of the specified CodeBuild build project named my-demo-project.

```
aws codebuild update-project --name "my-demo-project" \
    --description "This project is updated" \
    --source "{\"type\": \"S3\",\"location\": \"codebuild-us-west-2-123456789012-input-bucket/my-source-2.zip\"}" \
    --artifacts {"\"type\": \"S3\",\"location\": \"codebuild-us-west-2-123456789012-output-bucket-2\""} \
    --environment "{\"type\": \"LINUX_CONTAINER\",\"image\": \"aws/codebuild/standard:1.0\",\"computeType\": \"BUILD_GENERAL1_MEDIUM\"}" \
    --service-role "arn:aws:iam::123456789012:role/service-role/my-codebuild-service-role"
```

The output displays the updated settings.

```
{
    "project": {
        "arn": "arn:aws:codebuild:us-west-2:123456789012:project/my-demo-project",
        "environment": {
            "privilegedMode": false,
            "environmentVariables": [],
            "type": "LINUX_CONTAINER",
            "image": "aws/codebuild/standard:1.0",
            "computeType": "BUILD_GENERAL1_MEDIUM",
            "imagePullCredentialsType": "CODEBUILD"
        },
        "queuedTimeoutInMinutes": 480,
        "description": "This project is updated",
        "artifacts": {
            "packaging": "NONE",
            "name": "my-demo-project",
            "type": "S3",
            "namespaceType": "NONE",
            "encryptionDisabled": false,
            "location": "codebuild-us-west-2-123456789012-output-bucket-2"
        },
        "encryptionKey": "arn:aws:kms:us-west-2:123456789012:alias/aws/s3",
        "badge": {
            "badgeEnabled": false
        },
        "serviceRole": "arn:aws:iam::123456789012:role/service-role/my-codebuild-service-role",
        "lastModified": 1556840545.967,
        "tags": [],
        "timeoutInMinutes": 60,
        "created": 1556839783.274,
        "name": "my-demo-project",
        "cache": {
            "type": "NO_CACHE"
        },
        "source": {
            "type": "S3",
            "insecureSsl": false,
            "location": "codebuild-us-west-2-123456789012-input-bucket/my-source-2.zip"
        }
    }
}
```

For more information, see [Change a Build Projectâs Settings (AWS CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/change-project.html#change-project-cli) in the *AWS CodeBuild User Guide*

## Output

project -> (structure)

Information about the build project that was changed.

name -> (string)

The name of the build project.

arn -> (string)

The Amazon Resource Name (ARN) of the build project.

description -> (string)

A description that makes the build project easy to identify.

source -> (structure)

Information about the build input source code for this build project.

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

sourceVersion -> (string)

A version of the build input to be built for this project. If not specified, the latest version is used. If specified, it must be one of:

- For CodeCommit: the commit ID, branch, or Git tag to use.
- For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format `pr/pull-request-ID` (for example `pr/25` ). If a branch name is specified, the branchâs HEAD commit ID is used. If not specified, the default branchâs HEAD commit ID is used.
- For GitLab: the commit ID, branch, or Git tag to use.
- For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branchâs HEAD commit ID is used. If not specified, the default branchâs HEAD commit ID is used.
- For Amazon S3: the version ID of the object that represents the build input ZIP file to use.

If `sourceVersion` is specified at the build level, then that version takes precedence over this `sourceVersion` (at the project level).

For more information, see [Source Version Sample with CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html) in the *CodeBuild User Guide* .

secondarySourceVersions -> (list)

An array of `ProjectSourceVersion` objects. If `secondarySourceVersions` is specified at the build level, then they take over these `secondarySourceVersions` (at the project level).

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

secondaryArtifacts -> (list)

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

cache -> (structure)

Information about the cache for the build project.

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

Information about the build environment for this build project.

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

The ARN of the IAM role that enables CodeBuild to interact with dependent Amazon Web Services services on behalf of the Amazon Web Services account.

timeoutInMinutes -> (integer)

How long, in minutes, from 5 to 2160 (36 hours), for CodeBuild to wait before timing out any related build that did not get marked as completed. The default is 60 minutes.

queuedTimeoutInMinutes -> (integer)

The number of minutes a build is allowed to be queued before it times out.

encryptionKey -> (string)

The Key Management Service customer master key (CMK) to be used for encrypting the build output artifacts.

### Note

You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.

You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMKâs alias (using the format `alias/<alias-name>` ). If you donât specify a value, CodeBuild uses the managed CMK for Amazon Simple Storage Service (Amazon S3).

tags -> (list)

A list of tag key and value pairs associated with this build project.

These tags are available for use by Amazon Web Services services that support CodeBuild build project tags.

(structure)

A tag, consisting of a key and a value.

This tag is available for use by Amazon Web Services services that support tags in CodeBuild.

key -> (string)

The tagâs key.

value -> (string)

The tagâs value.

created -> (timestamp)

When the build project was created, expressed in Unix time format.

lastModified -> (timestamp)

When the build projectâs settings were last modified, expressed in Unix time format.

webhook -> (structure)

Information about a webhook that connects repository events to a build project in CodeBuild.

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

vpcConfig -> (structure)

Information about the VPC configuration that CodeBuild accesses.

vpcId -> (string)

The ID of the Amazon VPC.

subnets -> (list)

A list of one or more subnet IDs in your Amazon VPC.

(string)

securityGroupIds -> (list)

A list of one or more security groups IDs in your Amazon VPC.

(string)

badge -> (structure)

Information about the build badge for the build project.

badgeEnabled -> (boolean)

Set this to true to generate a publicly accessible URL for your projectâs build badge.

badgeRequestUrl -> (string)

The publicly-accessible URL through which you can access the build badge for your project.

logsConfig -> (structure)

Information about logs for the build project. A project can create logs in CloudWatch Logs, an S3 bucket, or both.

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

buildBatchConfig -> (structure)

A  ProjectBuildBatchConfig object that defines the batch build options for the project.

serviceRole -> (string)

Specifies the service role ARN for the batch build project.

combineArtifacts -> (boolean)

Specifies if the build artifacts for the batch build should be combined into a single artifact location.

restrictions -> (structure)

A `BatchRestrictions` object that specifies the restrictions for the batch build.

maximumBuildsAllowed -> (integer)

Specifies the maximum number of builds allowed.

computeTypesAllowed -> (list)

An array of strings that specify the compute types that are allowed for the batch build. See [Build environment compute types](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html) in the *CodeBuild User Guide* for these values.

(string)

fleetsAllowed -> (list)

An array of strings that specify the fleets that are allowed for the batch build. See [Run builds on reserved capacity fleets](https://docs.aws.amazon.com/codebuild/latest/userguide/fleets.html) in the *CodeBuild User Guide* for more information.

(string)

timeoutInMins -> (integer)

Specifies the maximum amount of time, in minutes, that the batch build must be completed in.

batchReportMode -> (string)

Specifies how build status reports are sent to the source provider for the batch build. This property is only used when the source provider for your project is Bitbucket, GitHub, or GitHub Enterprise, and your project is configured to report build statuses to the source provider.

REPORT_AGGREGATED_BATCH

(Default) Aggregate all of the build statuses into a single status report.

REPORT_INDIVIDUAL_BUILDS

Send a separate status report for each individual build.

concurrentBuildLimit -> (integer)

The maximum number of concurrent builds that are allowed for this project.

New builds are only started if the current number of builds is less than or equal to this limit. If the current build count meets this limit, new builds are throttled and are not run.

projectVisibility -> (string)

Specifies the visibility of the projectâs builds. Possible values are:

PUBLIC_READ

The project builds are visible to the public.

PRIVATE

The project builds are not visible to the public.

publicProjectAlias -> (string)

Contains the project identifier used with the public build APIs.

resourceAccessRole -> (string)

The ARN of the IAM role that enables CodeBuild to access the CloudWatch Logs and Amazon S3 artifacts for the projectâs builds.

autoRetryLimit -> (integer)

The maximum number of additional automatic retries after a failed build. For example, if the auto-retry limit is set to 2, CodeBuild will call the `RetryBuild` API to automatically retry your build for up to 2 additional times.