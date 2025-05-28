# gcloud compute os-config patch-deployments create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/create](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/create)*

**NAME**

: **gcloud compute os-config patch-deployments create - create a patch deployment for a project**

**SYNOPSIS**

: **`gcloud compute os-config patch-deployments create` `[PATCH_DEPLOYMENT_ID](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/create#PATCH_DEPLOYMENT_ID)` `[--file](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/create#--file)`=`FILE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute os-config patch-deployments create` creates a patch
deployment in a project from a specified file. A patch deployment triggers a
patch job to run at specific time(s) according to a schedule, and applies
instance filters and other patch configurations to the patch job at run time.
Alternatively, to run a patch job on-demand, see `$ [gcloud](https://cloud.google.com/sdk/gcloud/reference)` `compute os-config
patch-jobs execute`.

**EXAMPLES**

: To create a patch deployment `patch-deployment-1` in the current
project, run:

```
gcloud compute os-config patch-deployments create patch-deployment-1 --file=path_to_config_file
```

**POSITIONAL ARGUMENTS**

: **`PATCH_DEPLOYMENT_ID`**:
Name of the patch deployment to create.
This name must contain only lowercase letters, numbers, and hyphens, start with
a letter, end with a number or a letter, be between 1-63 characters, and unique
within the project.

**REQUIRED FLAGS**

: **--file**:
The JSON or YAML file with the patch deployment to create. For information about
the patch deployment format, see [https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments).

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

: This variant is also available:

```
gcloud beta compute os-config patch-deployments create
```