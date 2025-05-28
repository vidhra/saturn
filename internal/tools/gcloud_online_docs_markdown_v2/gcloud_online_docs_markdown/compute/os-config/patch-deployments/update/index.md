# gcloud compute os-config patch-deployments update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/update](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/update)*

**NAME**

: **gcloud compute os-config patch-deployments update - update patch deployment in a project**

**SYNOPSIS**

: **`gcloud compute os-config patch-deployments update` `[PATCH_DEPLOYMENT_ID](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/update#PATCH_DEPLOYMENT_ID)` `[--file](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/update#--file)`=`FILE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates a patch deployment in a project. To update the patch deployment, you
must specify a configuration file.

**EXAMPLES**

: To update a patch deployment `patch-deployment-1` in the current
project, run:

```
gcloud compute os-config patch-deployments update patch-deployment-1 --file=path_to_config_file
```

**POSITIONAL ARGUMENTS**

: **`PATCH_DEPLOYMENT_ID`**:
Name of the patch deployment to update.
To get a list of patch deployments that are available for update, run the
`gcloud compute os-config patch-deployments list` command.

**REQUIRED FLAGS**

: **--file**:
The JSON or YAML file with the patch deployment to update. For information about
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
gcloud beta compute os-config patch-deployments update
```