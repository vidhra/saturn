# gcloud deployment-manager deployments stop  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/stop](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/stop)*

**NAME**

: **gcloud deployment-manager deployments stop - stop a pending or running deployment update or creation**

**SYNOPSIS**

: **`gcloud deployment-manager deployments stop` `[DEPLOYMENT_NAME](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/stop#DEPLOYMENT_NAME)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/stop#--async)`] [`[--fingerprint](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/stop#--fingerprint)`=`FINGERPRINT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/stop#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command will stop a currently running or pending operation on a deployment.

**EXAMPLES**

: To stop a running operation on a deployment, run:

```
gcloud deployment-manager deployments stop my-deployment
```

To issue a stop command without waiting for the operation to complete, run:

```
gcloud deployment-manager deployments stop my-deployment --async
```

To stop a running operation on a deployment providing a fingerprint, run:

```
gcloud deployment-manager deployments stop my-deployment --fingerprint=deployment-fingerprint
```

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
gcloud alpha deployment-manager deployments stop
```

```
gcloud beta deployment-manager deployments stop
```