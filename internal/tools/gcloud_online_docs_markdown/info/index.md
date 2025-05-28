# gcloud info  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/info](https://cloud.google.com/sdk/gcloud/reference/info)*

**NAME**

: **gcloud info - display information about the current gcloud environment**

**SYNOPSIS**

: **`gcloud info` [`[--anonymize](https://cloud.google.com/sdk/gcloud/reference/info#--anonymize)`] [`[--run-diagnostics](https://cloud.google.com/sdk/gcloud/reference/info#--run-diagnostics)`     | `[--show-log](https://cloud.google.com/sdk/gcloud/reference/info#--show-log)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/info#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Display information about the current gcloud environment.

**EXAMPLES**

: To display information about the current gcloud environment including the Google
Cloud account, project and directory paths for logs, run:

```
gcloud info
```

To check network connectivity and hidden properties, run:

```
gcloud info --run-diagnostics
```

To print the contents of the most recent log file, run:

```
gcloud info --show-log
```

**FLAGS**

: **--anonymize**:
Minimize any personal identifiable information. Use it when sharing output with
others.

**--run-diagnostics**

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