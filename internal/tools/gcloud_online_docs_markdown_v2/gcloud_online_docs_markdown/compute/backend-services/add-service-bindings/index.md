# gcloud compute backend-services add-service-bindings  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-service-bindings](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-service-bindings)*

**NAME**

: **gcloud compute backend-services add-service-bindings - add service bindings to a backend service**

**SYNOPSIS**

: **`gcloud compute backend-services add-service-bindings` `[BACKEND_SERVICE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-service-bindings#BACKEND_SERVICE_NAME)` `[--service-bindings](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-service-bindings#--service-bindings)`=`SERVICE_BINDING`,[…] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-service-bindings#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-service-bindings#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-service-bindings#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Add service bindings to a backend service.

**EXAMPLES**

: To add a service binding to a backend service, run:

```
gcloud compute backend-services add-service-bindings NAME --service-bindings=SERVICE_BINDING1 --global
```

**POSITIONAL ARGUMENTS**

: **`BACKEND_SERVICE_NAME`**:
Name of the backend service to operate on.

**REQUIRED FLAGS**

: **--service-bindings**:
List of service binding names to be added to the backend service.

**OPTIONAL FLAGS**

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
gcloud alpha compute backend-services add-service-bindings
```

```
gcloud beta compute backend-services add-service-bindings
```