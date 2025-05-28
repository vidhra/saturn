# gcloud compute backend-services remove-backend  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/remove-backend](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/remove-backend)*

**NAME**

: **gcloud compute backend-services remove-backend - remove a backend from a backend service**

**SYNOPSIS**

: **`gcloud compute backend-services remove-backend` `[BACKEND_SERVICE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/remove-backend#BACKEND_SERVICE_NAME)` ([`[--instance-group](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/remove-backend#--instance-group)`=`INSTANCE_GROUP` : `[--instance-group-region](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/remove-backend#--instance-group-region)`=`INSTANCE_GROUP_REGION` | `[--instance-group-zone](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/remove-backend#--instance-group-zone)`=`INSTANCE_GROUP_ZONE`]     | [`[--network-endpoint-group](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/remove-backend#--network-endpoint-group)`=`NETWORK_ENDPOINT_GROUP` : `[--global-network-endpoint-group](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/remove-backend#--global-network-endpoint-group)` | `[--network-endpoint-group-region](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/remove-backend#--network-endpoint-group-region)`=`NETWORK_ENDPOINT_GROUP_REGION` | `[--network-endpoint-group-zone](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/remove-backend#--network-endpoint-group-zone)`=`NETWORK_ENDPOINT_GROUP_ZONE`]) [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/remove-backend#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/remove-backend#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/remove-backend#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute backend-services remove-backend` is used to remove a
backend from a backend service.
Before removing a backend, it is a good idea to "drain" the backend first. A
backend can be drained by setting its capacity scaler to zero through 'gcloud
compute backend-services edit'.

**POSITIONAL ARGUMENTS**

: **`BACKEND_SERVICE_NAME`**:
Name of the backend service to operate on.

**REQUIRED FLAGS**

: **--instance-group**

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
gcloud alpha compute backend-services remove-backend
```

```
gcloud beta compute backend-services remove-backend
```