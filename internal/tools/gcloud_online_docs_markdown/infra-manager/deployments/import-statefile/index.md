# gcloud infra-manager deployments import-statefile  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/import-statefile](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/import-statefile)*

**NAME**

: **gcloud infra-manager deployments import-statefile - import a terraform state file**

**SYNOPSIS**

: **`gcloud infra-manager deployments import-statefile` (`[DEPLOYMENT](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/import-statefile#DEPLOYMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/import-statefile#--location)`=`LOCATION`) `[--lock-id](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/import-statefile#--lock-id)`=`LOCK_ID` [`[--file](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/import-statefile#--file)`=`FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/import-statefile#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command generates a signed url to upload a terraform state file.

**EXAMPLES**

: Import state file for `my-deployment` with lock-id
`1658343229583347`:

```
gcloud infra-manager deployments import-statefile projects/p1/locations/us-central1/deployments/my-deployment --lock-id=1658343229583347
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

**REQUIRED FLAGS**

: **--lock-id**:
Lock ID of the lock file to verify person importing owns lock.

**OPTIONAL FLAGS**

: **--file**:
File path for importing statefile into a deployment. It specifies the local file
path of an existing Terraform statefile to directly upload for a deployment.

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