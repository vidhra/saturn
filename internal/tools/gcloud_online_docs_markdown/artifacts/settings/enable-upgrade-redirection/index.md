# gcloud artifacts settings enable-upgrade-redirection  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/settings/enable-upgrade-redirection](https://cloud.google.com/sdk/gcloud/reference/artifacts/settings/enable-upgrade-redirection)*

**NAME**

: **gcloud artifacts settings enable-upgrade-redirection - enables redirection from Container Registry to Artifact Registry**

**SYNOPSIS**

: **`gcloud artifacts settings enable-upgrade-redirection` [`[--dry-run](https://cloud.google.com/sdk/gcloud/reference/artifacts/settings/enable-upgrade-redirection#--dry-run)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/settings/enable-upgrade-redirection#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Enables redirection from Container Registry to Artifact Registry.

**EXAMPLES**

: To enable redirection for project `my-project`:

```
gcloud artifacts settings enable-upgrade-redirection --project=my-project
```

**FLAGS**

: **--dry-run**:
Validate the project setup, but do not enable redirection

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

**API REFERENCE**

: This command uses the `artifactregistry/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/artifacts/docs/](https://cloud.google.com/artifacts/docs/)

**NOTES**

: These variants are also available:

```
gcloud alpha artifacts settings enable-upgrade-redirection
```

```
gcloud beta artifacts settings enable-upgrade-redirection
```