# gcloud projects describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/projects/describe](https://cloud.google.com/sdk/gcloud/reference/projects/describe)*

**NAME**

: **gcloud projects describe - show metadata for a project**

**SYNOPSIS**

: **`gcloud projects describe` `[PROJECT_ID_OR_NUMBER](https://cloud.google.com/sdk/gcloud/reference/projects/describe#PROJECT_ID_OR_NUMBER)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/projects/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Shows metadata for a project given a valid project ID.
This command can fail for the following reasons:

- The project specified does not exist.
- The active account does not have permission to access the given project.

**EXAMPLES**

: The following command prints metadata for a project with the ID
`example-foo-bar-1`:

```
gcloud projects describe example-foo-bar-1
```

**POSITIONAL ARGUMENTS**

: **`PROJECT_ID_OR_NUMBER`**:
ID or number for the project you want to describe.

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
gcloud alpha projects describe
```

```
gcloud beta projects describe
```