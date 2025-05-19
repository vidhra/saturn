# gcloud app versions browse  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/versions/browse](https://cloud.google.com/sdk/gcloud/reference/app/versions/browse)*

**NAME**

: **gcloud app versions browse - open the specified versions in a browser**

**SYNOPSIS**

: **`gcloud app versions browse` `[VERSIONS](https://cloud.google.com/sdk/gcloud/reference/app/versions/browse#VERSIONS)` [`[VERSIONS](https://cloud.google.com/sdk/gcloud/reference/app/versions/browse#VERSIONS)` …] [`[--no-launch-browser](https://cloud.google.com/sdk/gcloud/reference/app/versions/browse#--launch-browser)`] [`[--service](https://cloud.google.com/sdk/gcloud/reference/app/versions/browse#--service)`=`SERVICE`, `[-s](https://cloud.google.com/sdk/gcloud/reference/app/versions/browse#-s)` `[SERVICE](https://cloud.google.com/sdk/gcloud/reference/app/versions/browse#SERVICE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/versions/browse#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Open the specified versions in a browser.

**EXAMPLES**

: To show version `v1` for the default service in the browser, run:

```
gcloud app versions browse v1
```

To show version `v1` of a specific service in the browser, run:

```
gcloud app versions browse v1 --service="myService"
```

To show multiple versions side-by-side, run:

```
gcloud app versions browse v1 v2 --service="myService"
```

**POSITIONAL ARGUMENTS**

: **`VERSIONS` [`VERSIONS` …]**:
The versions to open (optionally filtered by the --service flag).

**FLAGS**

: **--launch-browser**:
Launch a browser if possible. When disabled, only displays the URL. Enabled by
default, use `--no-launch-browser` to disable.

**--service**:
If specified, only open versions from the given service. If not specified, use
the default service.

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
gcloud beta app versions browse
```