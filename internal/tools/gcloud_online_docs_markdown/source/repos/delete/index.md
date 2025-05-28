# gcloud source repos delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/source/repos/delete](https://cloud.google.com/sdk/gcloud/reference/source/repos/delete)*

**NAME**

: **gcloud source repos delete - delete a cloud source repository**

**SYNOPSIS**

: **`gcloud source repos delete` `[REPOSITORY_NAME](https://cloud.google.com/sdk/gcloud/reference/source/repos/delete#REPOSITORY_NAME)` [`[--force](https://cloud.google.com/sdk/gcloud/reference/source/repos/delete#--force)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/source/repos/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command deletes a named git repository from the currently active Google
Cloud Platform project.

**EXAMPLES**

: To delete a named repository in the current project issue the following
commands:

```
gcloud init
```

```
gcloud source repos delete REPOSITORY_NAME
```

**POSITIONAL ARGUMENTS**

: **`REPOSITORY_NAME`**:
Name of the repository.

**FLAGS**

: **--force**:
(REMOVED) If provided, skip the delete confirmation prompt.
The --force option has been removed; use --quiet to suppress prompting.

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
gcloud alpha source repos delete
```

```
gcloud beta source repos delete
```