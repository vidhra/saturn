# gcloud logging scopes describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/scopes/describe](https://cloud.google.com/sdk/gcloud/reference/logging/scopes/describe)*

**NAME**

: **gcloud logging scopes describe - display information about a log scope**

**SYNOPSIS**

: **`gcloud logging scopes describe` `[LOG_SCOPE_ID](https://cloud.google.com/sdk/gcloud/reference/logging/scopes/describe#LOG_SCOPE_ID)` [`[--folder](https://cloud.google.com/sdk/gcloud/reference/logging/scopes/describe#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/logging/scopes/describe#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/logging/scopes/describe#--project)`=`PROJECT_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/scopes/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Display information about a log scope.

**EXAMPLES**

: To describe a log scope in a project, run:

```
gcloud logging scopes describe my-scope --project=my-project
```

**POSITIONAL ARGUMENTS**

: **`LOG_SCOPE_ID`**:
The ID of the log scope to describe.

**FLAGS**

: **--folder**

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