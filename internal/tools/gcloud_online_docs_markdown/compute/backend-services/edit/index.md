# gcloud compute backend-services edit  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/edit](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/edit)*

**NAME**

: **gcloud compute backend-services edit - modify a backend service**

**SYNOPSIS**

: **`gcloud compute backend-services edit` `[BACKEND_SERVICE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/edit#BACKEND_SERVICE_NAME)` [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/edit#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/edit#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/edit#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute backend-services edit` modifies a backend service of
a Google Cloud load balancer or Traffic Director. The backend service resource
is fetched from the server and presented in a text editor that displays the
configurable fields.
The specific editor is defined by the
``EDITOR`` environment variable.
The name of each backend corresponds to the name of an instance group, zonal
NEG, serverless NEG, or internet NEG.
To add, remove, or swap backends, use the `gcloud compute backend-services
remove-backend` and `[gcloud compute
backend-services add-backend](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend)` commands.

**POSITIONAL ARGUMENTS**

: **`BACKEND_SERVICE_NAME`**:
Name of the backend service to operate on.

**FLAGS**

: **--global**

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
gcloud alpha compute backend-services edit
```

```
gcloud beta compute backend-services edit
```