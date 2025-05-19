# gcloud app services browse  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/services/browse](https://cloud.google.com/sdk/gcloud/reference/app/services/browse)*

**NAME**

: **gcloud app services browse - open the specified service(s) in a browser**

**SYNOPSIS**

: **`gcloud app services browse` `[SERVICES](https://cloud.google.com/sdk/gcloud/reference/app/services/browse#SERVICES)` [`[SERVICES](https://cloud.google.com/sdk/gcloud/reference/app/services/browse#SERVICES)` …] [`[--no-launch-browser](https://cloud.google.com/sdk/gcloud/reference/app/services/browse#--launch-browser)`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/app/services/browse#--version)`=`VERSION`, `[-v](https://cloud.google.com/sdk/gcloud/reference/app/services/browse#-v)` `[VERSION](https://cloud.google.com/sdk/gcloud/reference/app/services/browse#VERSION)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/services/browse#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Open the specified service(s) in a browser.

**EXAMPLES**

: To show the url for the default service in the browser, run:

```
gcloud app services browse default
```

To show version `v1` of service `myService` in the
browser, run:

```
gcloud app services browse myService --version="v1"
```

To show multiple services side-by-side, run:

```
gcloud app services browse default otherService
```

To show multiple services side-by-side with a specific version, run:

```
gcloud app services browse s1 s2 --version=v1
```

**POSITIONAL ARGUMENTS**

: **`SERVICES` [`SERVICES` …]**:
The services to open (optionally filtered by the --version flag).

**FLAGS**

: **--launch-browser**:
Launch a browser if possible. When disabled, only displays the URL. Enabled by
default, use `--no-launch-browser` to disable.

**--version**:
If specified, open services with a given version. If not specified, use a
version based on the service's traffic split .

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
gcloud beta app services browse
```