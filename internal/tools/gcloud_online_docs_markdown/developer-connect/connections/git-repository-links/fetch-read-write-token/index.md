# gcloud developer-connect connections git-repository-links fetch-read-write-token  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links/fetch-read-write-token](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links/fetch-read-write-token)*

**NAME**

: **gcloud developer-connect connections git-repository-links fetch-read-write-token - fetch the read/write token of a given gitRepositoryLink**

**SYNOPSIS**

: **`gcloud developer-connect connections git-repository-links fetch-read-write-token` (`[GIT_REPOSITORY_LINK](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links/fetch-read-write-token#GIT_REPOSITORY_LINK)` : `[--connection](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links/fetch-read-write-token#--connection)`=`CONNECTION` `[--location](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links/fetch-read-write-token#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links/fetch-read-write-token#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Fetch the read/write token of a given gitRepositoryLink.

**EXAMPLES**

: To get the read/write token of a GitRepositoryLink named
"my-git-repository-link" in a Connection named "my-connection":

```
gcloud developer-connect connections git-repository-links fetch-read-write-token fetch-read-write-token my-git-repository-link --connection=my-connection --location=us-central1 --project=my-project
```

**POSITIONAL ARGUMENTS**

: **GitRepositoryLink resource - Developer Connect GitRepositoryLink from which to
fetch the read/write token. The arguments in this group can be used to specify
the attributes of this resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `git_repository_link` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`GIT_REPOSITORY_LINK`**:
ID of the gitRepositoryLink or fully qualified identifier for the
gitRepositoryLink.
To set the `git_repository_link` attribute:

- provide the argument `git_repository_link` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--connection**:
The connection id of the gitRepositoryLink resource.
To set the `connection` attribute:

- provide the argument `git_repository_link` on the command line with a
fully specified name;
- provide the argument `--connection` on the command line.

**--location**:
The location id of the gitRepositoryLink resource.
To set the `location` attribute:

- provide the argument `git_repository_link` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.**

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

: This command uses the `developerconnect/v1` API. The full
documentation for this API can be found at: [http://cloud.google.com/developer-connect/docs/overview](http://cloud.google.com/developer-connect/docs/overview)

**NOTES**

: These variants are also available:

```
gcloud alpha developer-connect connections git-repository-links fetch-read-write-token
```

```
gcloud beta developer-connect connections git-repository-links fetch-read-write-token
```