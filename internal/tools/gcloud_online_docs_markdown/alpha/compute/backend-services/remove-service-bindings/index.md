# gcloud alpha compute backend-services remove-service-bindings  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/remove-service-bindings](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/remove-service-bindings)*

**NAME**

: **gcloud alpha compute backend-services remove-service-bindings - remove service bindings from a backend service**

**SYNOPSIS**

: **`gcloud alpha compute backend-services remove-service-bindings` `[BACKEND_SERVICE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/remove-service-bindings#BACKEND_SERVICE_NAME)` `[--service-bindings](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/remove-service-bindings#--service-bindings)`=`SERVICE_BINDING`,[…] [`[--global](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/remove-service-bindings#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/remove-service-bindings#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/remove-service-bindings#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Remove service bindings from a backend service.

**EXAMPLES**

: To remove a service binding from a backend service, run:

```
gcloud alpha compute backend-services remove-service-bindings NAME --service-bindings=SERVICE_BINDING1 --global
```

**POSITIONAL ARGUMENTS**

: **`BACKEND_SERVICE_NAME`**:
Name of the backend service to operate on.

**REQUIRED FLAGS**

: **--service-bindings**:
List of service binding names to be removed from the backend service.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute backend-services remove-service-bindings
```

```
gcloud beta compute backend-services remove-service-bindings
```