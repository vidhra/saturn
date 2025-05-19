# gcloud compute os-config patch-deployments resume  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/resume](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/resume)*

**NAME**

: **gcloud compute os-config patch-deployments resume - resume patch deployment in a project**

**SYNOPSIS**

: **`gcloud compute os-config patch-deployments resume` `[PATCH_DEPLOYMENT](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/resume#PATCH_DEPLOYMENT)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/resume#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Resume patch deployment in a project.

**EXAMPLES**

: To resume the patch deployment `patch-deployment-1` in the current
project, run:

```
gcloud compute os-config patch-deployments resume patch-deployment-1
```

**POSITIONAL ARGUMENTS**

: **Patch deployment resource - Patch deployment to resume. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `patch_deployment` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`PATCH_DEPLOYMENT`**:
ID of the patch_deployment or fully qualified identifier for the
patch_deployment.
To set the `patch_deployment` attribute:

- provide the argument `patch_deployment` on the command line.**

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
gcloud beta compute os-config patch-deployments resume
```