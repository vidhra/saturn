# gcloud workspace-add-ons deployments delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/workspace-add-ons/deployments/delete](https://cloud.google.com/sdk/gcloud/reference/workspace-add-ons/deployments/delete)*

**NAME**

: **gcloud workspace-add-ons deployments delete - delete a Google Workspace Add-ons deployment**

**SYNOPSIS**

: **`gcloud workspace-add-ons deployments delete` `[DEPLOYMENT](https://cloud.google.com/sdk/gcloud/reference/workspace-add-ons/deployments/delete#DEPLOYMENT)` [`[--etag](https://cloud.google.com/sdk/gcloud/reference/workspace-add-ons/deployments/delete#--etag)`=`ETAG`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/workspace-add-ons/deployments/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Google Workspace Add-ons deployment

**EXAMPLES**

: To delete an deployment called `my-deployment`, run:

```
gcloud workspace-add-ons deployments delete my-deployment
```

**POSITIONAL ARGUMENTS**

: **Deployment resource - Google Workspace Add-ons deployment to delete This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `deployment` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DEPLOYMENT`**:
ID of the deployment or fully qualified identifier for the deployment.
To set the `deployment` attribute:

- provide the argument `deployment` on the command line.**

**FLAGS**

: **--etag**:
etag of the deployment file

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

**API REFERENCE**

: This command uses the `gsuiteaddons/v1` API. The full documentation
for this API can be found at: [https://developers.google.com/workspace/add-ons/guides/alternate-runtimes](https://developers.google.com/workspace/add-ons/guides/alternate-runtimes)