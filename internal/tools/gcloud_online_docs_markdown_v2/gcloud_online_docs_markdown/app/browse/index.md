# gcloud app browse  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/browse](https://cloud.google.com/sdk/gcloud/reference/app/browse)*

**NAME**

: **gcloud app browse - open the current app in a web browser**

**SYNOPSIS**

: **`gcloud app browse` [`[--no-launch-browser](https://cloud.google.com/sdk/gcloud/reference/app/browse#--launch-browser)`] [`[--service](https://cloud.google.com/sdk/gcloud/reference/app/browse#--service)`=`SERVICE`, `[-s](https://cloud.google.com/sdk/gcloud/reference/app/browse#-s)` `[SERVICE](https://cloud.google.com/sdk/gcloud/reference/app/browse#SERVICE)`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/app/browse#--version)`=`VERSION`, `[-v](https://cloud.google.com/sdk/gcloud/reference/app/browse#-v)` `[VERSION](https://cloud.google.com/sdk/gcloud/reference/app/browse#VERSION)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/browse#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Open the current app in a web browser.

**EXAMPLES**

: To open the default service, run:

```
gcloud app browse
```

To open a specific service, run:

```
gcloud app browse --service="myService"
```

To open a specific version, run:

```
gcloud app browse --service="myService" --version="v1"
```

**FLAGS**

: **--launch-browser**:
Launch a browser if possible. When disabled, only displays the URL. Enabled by
default, use `--no-launch-browser` to disable.

**--service**:
The service that should be opened. If not specified, use the default service.
May be used in conjunction with `--version`.

**--version**:
The version of the app that should be opened. If not specified, choose a version
based on the service's traffic split.

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
gcloud beta app browse
```