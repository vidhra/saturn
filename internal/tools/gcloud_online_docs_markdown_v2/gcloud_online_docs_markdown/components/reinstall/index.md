# gcloud components reinstall  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/components/reinstall](https://cloud.google.com/sdk/gcloud/reference/components/reinstall)*

**NAME**

: **gcloud components reinstall - reinstall the Google Cloud CLI with the same components you have now**

**SYNOPSIS**

: **`gcloud components reinstall` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/components/reinstall#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: If your Google Cloud CLI installation becomes corrupt, this command attempts to
fix it by downloading the latest version of the Google Cloud CLI and
reinstalling it. This will replace your existing installation with a fresh one.
The command is the equivalent of deleting your current installation, downloading
a fresh copy of the gcloud CLI, and installing in the same location.

**EXAMPLES**

: To reinstall all components you have installed, run:

```
gcloud components reinstall
```

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