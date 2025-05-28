# gcloud infra-manager deployments export-statefile  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/export-statefile](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/export-statefile)*

**NAME**

: **gcloud infra-manager deployments export-statefile - export a terraform state file**

**SYNOPSIS**

: **`gcloud infra-manager deployments export-statefile` (`[DEPLOYMENT](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/export-statefile#DEPLOYMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/export-statefile#--location)`=`LOCATION`) [`[--draft](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/export-statefile#--draft)`] [`[--file](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/export-statefile#--file)`=`FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/export-statefile#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command generates a signed url to download a terraform state file.

**EXAMPLES**

: Export state file for `my-deployment`:

```
gcloud infra-manager deployments export-statefile projects/p1/locations/us-central1/deployments/my-deployment
```

**POSITIONAL ARGUMENTS**

: **Deployment resource - the deployment to be used as parent. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `DEPLOYMENT` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DEPLOYMENT`**:
ID of the deployment or fully qualified identifier for the deployment.
To set the `deployment` attribute:

- provide the argument `DEPLOYMENT` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The Cloud location for the deployment.
To set the `location` attribute:

- provide the argument `DEPLOYMENT` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `infra-manager/location`.**

**FLAGS**

: **--draft**:
If this flag is set to true, the exported deployment state file will be the
draft state

**--file**:
File name for statefile. It is optional and it specifies the filename or
complete path for the downloaded statefile. If only a file path is provided, the
statefile will be downloaded as "statefile" within that directory. If a filename
is included, the statefile will be downloaded with that name.

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