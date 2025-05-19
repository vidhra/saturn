# gcloud alpha builds triggers create cloud-source-repositories  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/cloud-source-repositories](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/cloud-source-repositories)*

**NAME**

: **gcloud alpha builds triggers create cloud-source-repositories - create a build trigger from a Cloud Source Repository**

**SYNOPSIS**

: **`gcloud alpha builds triggers create cloud-source-repositories` (`[--trigger-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/cloud-source-repositories#--trigger-config)`=`PATH`     | [`[--repo](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/cloud-source-repositories#--repo)`=`REPO` (`[--branch-pattern](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/cloud-source-repositories#--branch-pattern)`=`REGEX` | `[--tag-pattern](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/cloud-source-repositories#--tag-pattern)`=`REGEX`) (`[--build-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/cloud-source-repositories#--build-config)`=`PATH` | `[--inline-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/cloud-source-repositories#--inline-config)`=`PATH` | [`[--dockerfile](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/cloud-source-repositories#--dockerfile)`=`DOCKERFILE` : `[--dockerfile-dir](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/cloud-source-repositories#--dockerfile-dir)`=`DOCKERFILE_DIR`; default="/" `[--dockerfile-image](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/cloud-source-repositories#--dockerfile-image)`=`DOCKERFILE_IMAGE`]) : `[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/cloud-source-repositories#--description)`=`DESCRIPTION` `[--ignored-files](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/cloud-source-repositories#--ignored-files)`=[`GLOB`,…] `[--included-files](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/cloud-source-repositories#--included-files)`=[`GLOB`,…] `[--name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/cloud-source-repositories#--name)`=`NAME` `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/cloud-source-repositories#--region)`=`REGION` `[--[no-]require-approval](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/cloud-source-repositories#--[no-]require-approval)` `[--service-account](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/cloud-source-repositories#--service-account)`=`SERVICE_ACCOUNT` `[--substitutions](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/cloud-source-repositories#--substitutions)`=[`KEY`=`VALUE`,…]]) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/cloud-source-repositories#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a build trigger from a Cloud Source Repository.

**EXAMPLES**

: To create a push trigger for all branches:

```
gcloud alpha builds triggers create cloud-source-repositories --name="my-trigger" --service-account="projects/my-project/serviceAccounts/my-byosa@my-project.iam.gserviceaccount.com" --repo="my-repo" --branch-pattern=".*" --build-config="cloudbuild.yaml"
```

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
gcloud builds triggers create cloud-source-repositories
```

```
gcloud beta builds triggers create cloud-source-repositories
```