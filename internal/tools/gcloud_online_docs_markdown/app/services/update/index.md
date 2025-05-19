# gcloud app services update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/services/update](https://cloud.google.com/sdk/gcloud/reference/app/services/update)*

**NAME**

: **gcloud app services update - update service-level settings**

**SYNOPSIS**

: **`gcloud app services update` [`[SERVICES](https://cloud.google.com/sdk/gcloud/reference/app/services/update#SERVICES)` …] `[--ingress](https://cloud.google.com/sdk/gcloud/reference/app/services/update#--ingress)`=`INGRESS` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/services/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update ingress traffic settings for an app.

**EXAMPLES**

: To update ingress traffic settings for the default service, run:

```
gcloud app services update default --ingress=internal-only
```

**POSITIONAL ARGUMENTS**

: **[`SERVICES` …]**:
The services to modify.

**REQUIRED FLAGS**

: **--ingress**:
Control what traffic can reach the app. `INGRESS` must be
one of: `all`, `internal-only`,
`internal-and-cloud-load-balancing`.

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

: This variant is also available:

```
gcloud beta app services update
```