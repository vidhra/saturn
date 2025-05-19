# gcloud app open-console  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/open-console](https://cloud.google.com/sdk/gcloud/reference/app/open-console)*

**NAME**

: **gcloud app open-console - open the App Engine dashboard, or log viewer, in a web browser**

**SYNOPSIS**

: **`gcloud app open-console` [`[--logs](https://cloud.google.com/sdk/gcloud/reference/app/open-console#--logs)`, `[-l](https://cloud.google.com/sdk/gcloud/reference/app/open-console#-l)`] [`[--service](https://cloud.google.com/sdk/gcloud/reference/app/open-console#--service)`=`SERVICE`, `[-s](https://cloud.google.com/sdk/gcloud/reference/app/open-console#-s)` `[SERVICE](https://cloud.google.com/sdk/gcloud/reference/app/open-console#SERVICE)`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/app/open-console#--version)`=`VERSION`, `[-v](https://cloud.google.com/sdk/gcloud/reference/app/open-console#-v)` `[VERSION](https://cloud.google.com/sdk/gcloud/reference/app/open-console#VERSION)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/open-console#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Open the App Engine dashboard, or log viewer, in a web browser.

**EXAMPLES**

: Open the App Engine dashboard for the default service:

```
gcloud app open-console
```

Open the service specific dashboard view:

```
gcloud app open-console --service="myService"
```

Open the version specific dashboard view:

```
gcloud app open-console --service="myService" --version="v1"
```

Open the log viewer for the default service:

```
gcloud app open-console --logs
```

**FLAGS**

: **--logs**:
Open the log viewer instead of the App Engine dashboard.

**--service**:
The service to consider. If not specified, use the default service.

**--version**:
The version to consider. If not specified, all versions for the given service
are considered.

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
gcloud beta app open-console
```