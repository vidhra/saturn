# gcloud dns project-info describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/project-info/describe](https://cloud.google.com/sdk/gcloud/reference/dns/project-info/describe)*

**NAME**

: **gcloud dns project-info describe - view Cloud DNS related information for a project**

**SYNOPSIS**

: **`gcloud dns project-info describe` `[PROJECT_ID](https://cloud.google.com/sdk/gcloud/reference/dns/project-info/describe#PROJECT_ID)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/project-info/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command displays Cloud DNS related information for your project including
quotas for various resources and operations.

**EXAMPLES**

: To display Cloud DNS related information for your project, run:

```
gcloud dns project-info describe my_project_id
```

**POSITIONAL ARGUMENTS**

: **`PROJECT_ID`**:
The identifier for the project you want DNS related info for.

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
gcloud alpha dns project-info describe
```

```
gcloud beta dns project-info describe
```