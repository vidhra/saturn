# gcloud alpha builds triggers update gitlab  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab)*

**NAME**

: **gcloud alpha builds triggers update gitlab - updates GitLab trigger used by Cloud Build**

**SYNOPSIS**

: **`gcloud alpha builds triggers update gitlab` (`[TRIGGER](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#TRIGGER)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#--region)`=`REGION`) (`[--trigger-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#--trigger-config)`=`PATH`     | `[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#--description)`=`DESCRIPTION` `[--ignored-files](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#--ignored-files)`=[`GLOB`,…] `[--included-files](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#--included-files)`=[`GLOB`,…] `[--repository](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#--repository)`=`REPOSITORY` `[--[no-]require-approval](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#--[no-]require-approval)` `[--service-account](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#--service-account)`=`SERVICE_ACCOUNT` `[--branch-pattern](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#--branch-pattern)`=`REGEX`     | `[--tag-pattern](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#--tag-pattern)`=`REGEX`     | `[--comment-control](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#--comment-control)`=`COMMENT_CONTROL` `[--pull-request-pattern](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#--pull-request-pattern)`=`REGEX` `[--build-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#--build-config)`=`PATH`     | `[--inline-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#--inline-config)`=`PATH`     | [`[--dockerfile](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#--dockerfile)`=`DOCKERFILE` `[--dockerfile-image](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#--dockerfile-image)`=`DOCKERFILE_IMAGE` : `[--dockerfile-dir](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#--dockerfile-dir)`=`DOCKERFILE_DIR`] `[--clear-substitutions](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#--clear-substitutions)`     | `[--remove-substitutions](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#--remove-substitutions)`=[`KEY`,…]     | `[--update-substitutions](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#--update-substitutions)`=[`KEY`=`VALUE`,…]) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/gitlab#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Updates GitLab trigger used by Cloud Build.

**EXAMPLES**

: To update the branch pattern of the trigger:

```
gcloud alpha builds triggers update gitlab my-trigger --branch-pattern=".*"
```

To update the build config of the trigger:

```
gcloud alpha builds triggers update gitlab my-trigger --build-config="cloudbuild.yaml"
```

To update the substitutions of the trigger:

```
gcloud alpha builds triggers update gitlab my-trigger --update-substitutions=_REPO_NAME=my-repo,_BRANCH_NAME=master
```

To update the 2nd-gen repository resource of the trigger:

```
gcloud alpha builds triggers update gitlab my-trigger --repository=projects/my-project/locations/us-west1/connections/my-conn/repositories/my-repo
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
gcloud builds triggers update gitlab
```

```
gcloud beta builds triggers update gitlab
```