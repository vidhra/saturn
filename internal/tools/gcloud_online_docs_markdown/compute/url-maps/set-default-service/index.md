# gcloud compute url-maps set-default-service  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/set-default-service](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/set-default-service)*

**NAME**

: **gcloud compute url-maps set-default-service - change the default service or default bucket of a URL map**

**SYNOPSIS**

: **`gcloud compute url-maps set-default-service` `[URL_MAP](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/set-default-service#URL_MAP)` (`[--default-backend-bucket](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/set-default-service#--default-backend-bucket)`=`DEFAULT_BACKEND_BUCKET`     | `[--default-service](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/set-default-service#--default-service)`=`DEFAULT_SERVICE`) [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/set-default-service#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/set-default-service#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/set-default-service#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute url-maps set-default-service` is used to change the
default service or default bucket of a URL map. The default service or default
bucket is used for any requests for which there is no mapping in the URL map.

**POSITIONAL ARGUMENTS**

: **`URL_MAP`**:
Name of the URL map to operate on.

**REQUIRED FLAGS**

: **--default-backend-bucket**

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
gcloud alpha compute url-maps set-default-service
```

```
gcloud beta compute url-maps set-default-service
```