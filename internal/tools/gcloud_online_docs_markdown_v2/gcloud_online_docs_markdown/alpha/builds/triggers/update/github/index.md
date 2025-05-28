# gcloud alpha builds triggers update github  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github)*

**NAME**

: **gcloud alpha builds triggers update github - update GitHub trigger used by Cloud Build**

**SYNOPSIS**

: **`gcloud alpha builds triggers update github` (`[TRIGGER](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#TRIGGER)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--region)`=`REGION`) (`[--trigger-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--trigger-config)`=`PATH`     | `[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--description)`=`DESCRIPTION` `[--ignored-files](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--ignored-files)`=[`GLOB`,…] `[--include-logs-with-status](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--include-logs-with-status)` `[--included-files](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--included-files)`=[`GLOB`,…] `[--[no-]require-approval](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--[no-]require-approval)` `[--service-account](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--service-account)`=`SERVICE_ACCOUNT` `[--branch-pattern](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--branch-pattern)`=`REGEX`     | `[--tag-pattern](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--tag-pattern)`=`REGEX`     | `[--comment-control](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--comment-control)`=`COMMENT_CONTROL`; default=`"COMMENTS_ENABLED"` `[--pull-request-pattern](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--pull-request-pattern)`=`REGEX` `[--build-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--build-config)`=`PATH`     | `[--inline-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--inline-config)`=`PATH`     | [`[--dockerfile](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--dockerfile)`=`DOCKERFILE` `[--dockerfile-image](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--dockerfile-image)`=`DOCKERFILE_IMAGE` : `[--dockerfile-dir](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--dockerfile-dir)`=`DOCKERFILE_DIR`] `[--clear-substitutions](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--clear-substitutions)`     | `[--remove-substitutions](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--remove-substitutions)`=[`KEY`,…]     | `[--update-substitutions](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--update-substitutions)`=[`KEY`=`VALUE`,…] `[--repository](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--repository)`=`REPOSITORY`     | `[--enterprise-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--enterprise-config)`=`ENTERPRISE_CONFIG` `[--repo-name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--repo-name)`=`REPO_NAME` `[--repo-owner](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#--repo-owner)`=`REPO_OWNER`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/github#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update GitHub trigger used by Cloud Build.

**EXAMPLES**

: To update the branch pattern of the trigger:

```
gcloud alpha builds triggers update github my-trigger --branch-pattern=".*"
```

To update the build config of the trigger:

```
gcloud alpha builds triggers update github my-trigger --build-config="cloudbuild.yaml"
```

To update the substitutions of the trigger:

```
gcloud alpha builds triggers update github my-trigger --update-substitutions=_REPO_NAME=my-repo,_BRANCH_NAME=master
```

**POSITIONAL ARGUMENTS**

: **Trigger resource - Build Trigger. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `TRIGGER` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TRIGGER`**:
ID of the trigger or fully qualified identifier for the trigger.
To set the `trigger` attribute:

- provide the argument `TRIGGER` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The Cloud location for the trigger.
To set the `region` attribute:

- provide the argument `TRIGGER` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `builds/region`.**

**REQUIRED FLAGS**

: **--trigger-config**

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud builds triggers update github
```

```
gcloud beta builds triggers update github
```