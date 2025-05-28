# gcloud infra-manager deployments delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/delete](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/delete)*

**NAME**

: **gcloud infra-manager deployments delete - delete deployments**

**SYNOPSIS**

: **`gcloud infra-manager deployments delete` (`[DEPLOYMENT](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/delete#DEPLOYMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/delete#--async)`] [`[--delete-policy](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/delete#--delete-policy)`=`DELETE_POLICY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a deployment

**EXAMPLES**

: To delete the deployment `example-deployment` at location
`us-central1`, run:

```
gcloud infra-manager deployments delete projects/example-project/locations/us-central1/deployments/example-deployment
```

**POSITIONAL ARGUMENTS**

: **Deployment resource - deployments TBD The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `deployment` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DEPLOYMENT`**:
ID of the deployment or fully qualified identifier for the deployment.
To set the `deployment` attribute:

- provide the argument `deployment` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
locations TBD
To set the `location` attribute:

- provide the argument `deployment` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `infra-manager/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--delete-policy**:
Policy on how resources actuated by the deployment should be deleted. The
accepted values are DELETE, ABANDON. DELETE = Delete resources actuated by the
deployment. ABANDON = Abandon resources and only delete deployment metadata.
`DELETE_POLICY` must be one of: `abandon`,
`delete`, `delete-policy-unspecified`.

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

: This command uses the `config/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/infrastructure-manager/docs](https://cloud.google.com/infrastructure-manager/docs)