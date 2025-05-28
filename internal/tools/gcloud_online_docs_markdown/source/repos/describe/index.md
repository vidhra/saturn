# gcloud source repos describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/source/repos/describe](https://cloud.google.com/sdk/gcloud/reference/source/repos/describe)*

**NAME**

: **gcloud source repos describe - describe a cloud source repository**

**SYNOPSIS**

: **`gcloud source repos describe` `[REPOSITORY_NAME](https://cloud.google.com/sdk/gcloud/reference/source/repos/describe#REPOSITORY_NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/source/repos/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command describes a repository from the currently active Google Cloud
Platform project. The description includes the full repository name
(projects/<projectid>/repos/<reponame>), the size (if non-zero), and
the url.

**EXAMPLES**

: To describe a repository named example-repo in the current project issue the
following command:

```
gcloud source repos describe REPOSITORY_NAME
```

**POSITIONAL ARGUMENTS**

: **`REPOSITORY_NAME`**:
Name of the repository.

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
gcloud alpha source repos describe
```

```
gcloud beta source repos describe
```