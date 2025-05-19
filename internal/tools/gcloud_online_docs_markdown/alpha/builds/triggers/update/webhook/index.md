# gcloud alpha builds triggers update webhook  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook)*

**NAME**

: **gcloud alpha builds triggers update webhook - update a Webhook trigger used by Cloud Build**

**SYNOPSIS**

: **`gcloud alpha builds triggers update webhook` (`[TRIGGER](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#TRIGGER)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--region)`=`REGION`) (`[--trigger-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--trigger-config)`=`PATH`     | `[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--description)`=`DESCRIPTION` `[--[no-]require-approval](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--[no-]require-approval)` `[--secret](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--secret)`=`SECRET` `[--service-account](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--service-account)`=`SERVICE_ACCOUNT` `[--subscription-filter](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--subscription-filter)`=`SUBSCRIPTION_FILTER` `[--clear-substitutions](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--clear-substitutions)`     | `[--remove-substitutions](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--remove-substitutions)`=[`KEY`,…]     | `[--update-substitutions](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--update-substitutions)`=[`KEY`=`VALUE`,…] `[--inline-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--inline-config)`=`PATH`     | [`[--dockerfile](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--dockerfile)`=`DOCKERFILE` : `[--dockerfile-dir](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--dockerfile-dir)`=`DOCKERFILE_DIR` `[--dockerfile-image](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--dockerfile-image)`=`DOCKERFILE_IMAGE`]     | `[--git-file-source-branch](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--git-file-source-branch)`=`GIT_FILE_SOURCE_BRANCH`     | `[--git-file-source-tag](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--git-file-source-tag)`=`GIT_FILE_SOURCE_TAG` `[--git-file-source-github-enterprise-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--git-file-source-github-enterprise-config)`=`GIT_FILE_SOURCE_GITHUB_ENTERPRISE_CONFIG` `[--git-file-source-path](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--git-file-source-path)`=`PATH` `[--git-file-source-repo-type](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--git-file-source-repo-type)`=`GIT_FILE_SOURCE_REPO_TYPE` `[--git-file-source-uri](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--git-file-source-uri)`=`URL` `[--source-to-build-branch](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--source-to-build-branch)`=`SOURCE_TO_BUILD_BRANCH`     | `[--source-to-build-tag](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--source-to-build-tag)`=`SOURCE_TO_BUILD_TAG` `[--source-to-build-github-enterprise-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--source-to-build-github-enterprise-config)`=`SOURCE_TO_BUILD_GITHUB_ENTERPRISE_CONFIG` `[--source-to-build-repo-type](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--source-to-build-repo-type)`=`SOURCE_TO_BUILD_REPO_TYPE` `[--source-to-build-uri](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#--source-to-build-uri)`=`SOURCE_TO_BUILD_URI`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/update/webhook#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update a Webhook trigger used by Cloud Build.

**EXAMPLES**

: To update the branch from which the trigger clones:

```
gcloud alpha builds triggers update webhook my-webhook-trigger --source-to-build-branch=my-branch
```

To update the webhook secret:

```
gcloud alpha builds triggers update webhook my-webhook-trigger --secret=projects/my-project/secrets/my-secret/versions/2
```

To update the substitutions of the trigger:
```
gcloud alpha builds triggers update webhook my-trigger --update-substitutions=_REPO_NAME=my-repo,_BRANCH_NAME=master
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
gcloud builds triggers update webhook
```

```
gcloud beta builds triggers update webhook
```