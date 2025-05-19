# gcloud app update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/update](https://cloud.google.com/sdk/gcloud/reference/app/update)*

**NAME**

: **gcloud app update - updates an App Engine application**

**SYNOPSIS**

: **`gcloud app update` [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/app/update#--service-account)`=`SERVICE_ACCOUNT`] [`[--[no-]split-health-checks](https://cloud.google.com/sdk/gcloud/reference/app/update#--[no-]split-health-checks)`] [`[--ssl-policy](https://cloud.google.com/sdk/gcloud/reference/app/update#--ssl-policy)`=`SSL_POLICY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command is used to update settings on an app engine application.

**EXAMPLES**

: To enable split health checks on an application:

```
gcloud app update --split-health-checks
```

To update the app-level service account on an application:

```
gcloud app update --service-account=SERVICE_ACCOUNT
```

To update the app-level minimum SSL policy of the application:

```
gcloud app update --ssl-policy=TLS_VERSION_1_2
```

**FLAGS**

: **--service-account**:
The app-level default service account to update the app with.

**--[no-]split-health-checks**:
Enables/disables split health checks by default on new deployments. Use
`--split-health-checks` to enable and
`--no-split-health-checks` to disable.

**--ssl-policy**:
The app-level SSL policy to update the app with.
`SSL_POLICY` must be one of: `TLS_VERSION_1_0`,
`TLS_VERSION_1_2`.

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
gcloud alpha app update
```

```
gcloud beta app update
```