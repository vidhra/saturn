# gcloud developer-connect connections git-repository-links create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links/create](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links/create)*

**NAME**

: **gcloud developer-connect connections git-repository-links create - create a git repository link**

**SYNOPSIS**

: **`gcloud developer-connect connections git-repository-links create` (`[GIT_REPOSITORY_LINK](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links/create#GIT_REPOSITORY_LINK)` : `[--connection](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links/create#--connection)`=`CONNECTION` `[--location](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links/create#--location)`=`LOCATION`) `[--clone-uri](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links/create#--clone-uri)`=`CLONE_URI` [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links/create#--annotations)`=[`ANNOTATIONS`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links/create#--async)`] [`[--etag](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links/create#--etag)`=`ETAG`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links/create#--labels)`=[`LABELS`,…]] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links/create#--request-id)`=`REQUEST_ID`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links/create#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a git repository link.

**EXAMPLES**

: To create a git repository link 'my-git-repository-link' in a connection
`my-connection` in `us-central1` run:

```
gcloud developer-connect connections git-repository-links create my-git-repository-link --clone-uri=https://github.com/my-org/my-repo.git --connection=my-connection --location=us-central1
```

Or run:

```
gcloud developer-connect connections git-repository-links create projects/my-project/locations/us-central1/connections/my-connection/gitRepositoryLinks/my-git-repository-link --clone-uri=https://github.com/my-org/my-repo.git --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **GitRepositoryLink resource - Identifier. Resource name of the repository, in the
format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
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

**REQUIRED FLAGS**

: **--clone-uri**:
Git Clone URI.

**OPTIONAL FLAGS**

: **--annotations**:
Allows clients to store small amounts of arbitrary data.

**`KEY`**:
Sets `KEY` value.

**`VALUE`**:
Sets `VALUE` value.

`Shorthand Example:`

```
--annotations=string=string
```

`JSON Example:`

```
--annotations='{"string": "string"}'
```

`File Example:`

```
--annotations=path_to_file.(yaml|json)
```

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--etag**:
This checksum is computed by the server based on the value of other fields, and
may be sent on update and delete requests to ensure the client has an up-to-date
value before proceeding.

**--labels**:
Labels as key value pairs.

**`KEY`**:
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers.

**`VALUE`**:
Values must contain only hyphens (`-`), underscores (`_`),
lowercase characters, and numbers.

`Shorthand Example:`

```
--labels=string=string
```

`JSON Example:`

```
--labels='{"string": "string"}'
```

`File Example:`

```
--labels=path_to_file.(yaml|json)
```

**--request-id**:
An optional request ID to identify requests. Specify a unique request ID so that
if you must retry your request, the server will know to ignore the request if it
has already been completed. The server will guarantee that for at least 60
minutes since the first request.
For example, consider a situation where you make an initial request and the
request times out. If you make the request again with the same request ID, the
server can check if original operation with the same request ID was received,
and if so, will ignore the second request. This prevents clients from
accidentally creating duplicate commitments.
The request ID must be a valid UUID with the exception that zero UUID is not
supported (00000000-0000-0000-0000-000000000000).

**--validate-only**:
If set, validate the request, but do not actually post it.

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
gcloud alpha developer-connect connections git-repository-links create
```

```
gcloud beta developer-connect connections git-repository-links create
```