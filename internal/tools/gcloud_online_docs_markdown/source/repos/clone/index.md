# gcloud source repos clone  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/source/repos/clone](https://cloud.google.com/sdk/gcloud/reference/source/repos/clone)*

**NAME**

: **gcloud source repos clone - clone a cloud source repository**

**SYNOPSIS**

: **`gcloud source repos clone` `[REPOSITORY_NAME](https://cloud.google.com/sdk/gcloud/reference/source/repos/clone#REPOSITORY_NAME)` [`[DIRECTORY_NAME](https://cloud.google.com/sdk/gcloud/reference/source/repos/clone#DIRECTORY_NAME)`] [`[--dry-run](https://cloud.google.com/sdk/gcloud/reference/source/repos/clone#--dry-run)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/source/repos/clone#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command clones a git repository from the currently active Google Cloud
project into the specified directory or into the current directory if no target
directory is specified.
Each Google Cloud project can have zero or more git repositories associated with
it. To see the available repositories, run:

```
gcloud source repos list
```

The clone operation configures the local clone to use your gcloud credentials to
authenticate future git operations. This command emits a warning if the cloud
source repository is a mirror.

**EXAMPLES**

: The example commands below show a sample workflow.

```
gcloud init
```

```
gcloud source repos clone REPOSITORY_NAME DIRECTORY_NAME
```

```
cd DIRECTORY_NAME … create/edit files and create one or more commits …
```

```
git push origin main
```

**POSITIONAL ARGUMENTS**

: **`REPOSITORY_NAME`**:
Name of the repository.

**[`DIRECTORY_NAME`]**:
Directory name for the cloned repo. Defaults to the repository name.

**FLAGS**

: **--dry-run**:
If provided, prints the command that would be run to standard out instead of
executing it.

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
gcloud alpha source repos clone
```

```
gcloud beta source repos clone
```