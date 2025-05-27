# gcloud deployment-manager deployments cancel-preview  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/cancel-preview](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/cancel-preview)*

**NAME**

: **gcloud deployment-manager deployments cancel-preview - cancel a pending or running deployment preview**

**SYNOPSIS**

: **`gcloud deployment-manager deployments cancel-preview` `[DEPLOYMENT_NAME](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/cancel-preview#DEPLOYMENT_NAME)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/cancel-preview#--async)`] [`[--fingerprint](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/cancel-preview#--fingerprint)`=`FINGERPRINT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/cancel-preview#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command will cancel a currently running or pending preview operation on a
deployment.

**EXAMPLES**

: To cancel a running operation on a deployment, run:

```
gcloud deployment-manager deployments cancel-preview my-deployment
```

To issue a cancel preview command without waiting for the operation to complete,
run:

```
gcloud deployment-manager deployments cancel-preview my-deployment --async
```

To cancel a preview command providing a fingerprint:

```
gcloud deployment-manager deployments cancel-preview my-deployment --fingerprint=deployment-fingerprint
```

When a deployment preview is cancelled, the deployment itself is not deleted.

**POSITIONAL ARGUMENTS**

: **`DEPLOYMENT_NAME`**:
Deployment name.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--fingerprint**:
The fingerprint to use in requests to modify a deployment. If not specified, a
get deployment request will be made to fetch the latest fingerprint. A
fingerprint is a randomly generated value that is part of the update, stop, and
cancel-preview request to perform optimistic locking. It is initially generated
by Deployment Manager and changes after every request to modify data. The latest
fingerprint is printed when deployment data is modified.

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
gcloud alpha deployment-manager deployments cancel-preview
```

```
gcloud beta deployment-manager deployments cancel-preview
```