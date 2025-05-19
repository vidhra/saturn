# gcloud alpha anthos apply  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/apply](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/apply)*

**NAME**

: **gcloud alpha anthos apply - apply configuration changes for Anthos infrastructure**

**SYNOPSIS**

: **`gcloud alpha anthos apply` `[LOCAL_DIR](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/apply#LOCAL_DIR)` [`[--project](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/apply#--project)`=`PROJECT_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/apply#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Apply configuration changes for Anthos infrastructure.

**EXAMPLES**

: To apply Anthos package to a Google Kubernetes Engine cluster in project
`my-project`:

```
gcloud alpha anthos apply my-config --project=my-project
```

**POSITIONAL ARGUMENTS**

: **`LOCAL_DIR`**:
Directory of package to apply.

**COMMONLY USED FLAGS**

: **--project**:
Project ID. Overrides the default `core/project` property value for
this command invocation.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud beta anthos apply
```