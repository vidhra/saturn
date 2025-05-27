# gcloud deployment-manager deployments delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/delete](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/delete)*

**NAME**

: **gcloud deployment-manager deployments delete - delete a deployment**

**SYNOPSIS**

: **`gcloud deployment-manager deployments delete` `[DEPLOYMENT_NAME](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/delete#DEPLOYMENT_NAME)` [`[DEPLOYMENT_NAME](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/delete#DEPLOYMENT_NAME)` …] [`[--async](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/delete#--async)`] [`[--delete-policy](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/delete#--delete-policy)`=`DELETE_POLICY`; default="delete"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command deletes a deployment and deletes all associated resources.

**EXAMPLES**

: To delete a deployment, run:

```
gcloud deployment-manager deployments delete my-deployment
```

To issue a delete command without waiting for the operation to complete, run:

```
gcloud deployment-manager deployments delete my-deployment --async
```

To delete several deployments, run:

```
gcloud deployment-manager deployments delete my-deployment-one my-deployment-two my-deployment-three
```

To disable the confirmation prompt on delete, run:

```
gcloud deployment-manager deployments delete my-deployment -q
```

**POSITIONAL ARGUMENTS**

: **`DEPLOYMENT_NAME` [`DEPLOYMENT_NAME` …]**:
Deployment name.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--delete-policy**:
Delete policy for resources that will change as part of an update or delete.
`delete` deletes the resource while `abandon` just removes
the resource reference from the deployment.
`DELETE_POLICY` must be one of: `abandon`,
`delete`.

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

: These variants are also available:

```
gcloud alpha deployment-manager deployments delete
```

```
gcloud beta deployment-manager deployments delete
```