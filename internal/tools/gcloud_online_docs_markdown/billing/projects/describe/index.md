# gcloud billing projects describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/billing/projects/describe](https://cloud.google.com/sdk/gcloud/reference/billing/projects/describe)*

**NAME**

: **gcloud billing projects describe - show detailed billing information for a project**

**SYNOPSIS**

: **`gcloud billing projects describe` `[PROJECT_ID](https://cloud.google.com/sdk/gcloud/reference/billing/projects/describe#PROJECT_ID)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/billing/projects/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command shows billing info for a project, given its ID.
This call can fail for the following reasons:

- The project specified does not exist.
- The active user does not have permission to access the given project.

**EXAMPLES**

: To see detailed billing information for a project `my-project`, run:

```
gcloud billing projects describe my-project
```

**POSITIONAL ARGUMENTS**

: **`PROJECT_ID`**:
Specify a project id.

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

: This command uses the `cloudbilling/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/billing/v1/getting-started](https://cloud.google.com/billing/v1/getting-started)

**NOTES**

: These variants are also available:

```
gcloud alpha billing projects describe
```

```
gcloud beta billing projects describe
```