# gcloud workspace-add-ons deployments install  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/workspace-add-ons/deployments/install](https://cloud.google.com/sdk/gcloud/reference/workspace-add-ons/deployments/install)*

**NAME**

: **gcloud workspace-add-ons deployments install - install a Google Workspace Add-ons deployment**

**SYNOPSIS**

: **`gcloud workspace-add-ons deployments install` `[DEPLOYMENT](https://cloud.google.com/sdk/gcloud/reference/workspace-add-ons/deployments/install#DEPLOYMENT)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/workspace-add-ons/deployments/install#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Install a Google Workspace Add-ons deployment

**EXAMPLES**

: To install a deployment called `my-deployment`, run:

```
gcloud workspace-add-ons deployments install my-deployment
```

**POSITIONAL ARGUMENTS**

: **Deployment resource - Google Workspace Add-ons deployment to install This
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