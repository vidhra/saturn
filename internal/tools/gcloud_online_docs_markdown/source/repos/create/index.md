# gcloud source repos create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/source/repos/create](https://cloud.google.com/sdk/gcloud/reference/source/repos/create)*

**NAME**

: **gcloud source repos create - create a cloud source repository**

**SYNOPSIS**

: **`gcloud source repos create` `[REPOSITORY_NAME](https://cloud.google.com/sdk/gcloud/reference/source/repos/create#REPOSITORY_NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/source/repos/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command creates a named git repository for the currently active Google
Cloud Platform project.

**EXAMPLES**

: To create a named repository in the current project issue the following
commands:

```
gcloud init
```

```
gcloud source repos create REPOSITORY_NAME
```

Once you push contents to it, they can be browsed in the Developers Console.

**POSITIONAL ARGUMENTS**

: **`REPOSITORY_NAME`**:
Name of the repository. May contain between 3 and 63 (inclusive) lowercase
letters, digits, and hyphens. Must start with a letter, and may not end with a
hyphen.

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
gcloud alpha source repos create
```

```
gcloud beta source repos create
```