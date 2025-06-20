# gcloud gemini code-repository-indexes repository-groups create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/create](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/create)*

**NAME**

: **gcloud gemini code-repository-indexes repository-groups create - create a repository group for a given code repository index instance**

**SYNOPSIS**

: **`gcloud gemini code-repository-indexes repository-groups create` (`[REPOSITORY_GROUP](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/create#REPOSITORY_GROUP)` : `[--code-repository-index](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/create#--code-repository-index)`=`CODE_REPOSITORY_INDEX` `[--location](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/create#--location)`=`LOCATION`) `[--repositories](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/create#--repositories)`=[`branchPattern`=`BRANCHPATTERN`],[`resource`=`RESOURCE`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/create#--async)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/create#--labels)`=[`LABELS`,…]] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/create#--request-id)`=`REQUEST_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a repository group for a given code repository index instance.

**EXAMPLES**

: To create a repository group `my-repository-group` for a code
repository index instance `my-instance` in project
`my-project` and location `us-central1` with one Developer
Connect repository and branch pattern `.*`, run:

```
gcloud gemini code-repository-indexes repository-groups create my-repository-group --code-repository-index=my-instance --project=my-project --location=us-central1 --repositories=branchPattern=.*,resource=developerconnect.googleapis.com/projects/<PROJECT>/locations/<LOCATION>/connections/<CONNECTION>/gitRepositoryLinks/<REPOSITORY>
```

Developer Connect Git repository resource must already exist. Refer to [Developer
Connect documentation](http://cloud.google.com/developer-connect/docs/connect-repo) for more details.
To create a repository group `my-repository-group` for a code
repository index instance `my-instance` in project
`my-project` and location `us-central1` with a fully
qualified name, run:

```
gcloud gemini code-repository-indexes repository-groups create projects/my-project/locations/us-central1/codeRepositoryIndexes/my-instance/repositoryGroups/my-repository-group --repositories=branchPattern=.*,resource=developerconnect.googleapis.com/projects/<PROJECT>/locations/<LOCATION>/connections/<CONNECTION>/gitRepositoryLinks/<REPOSITORY>
```

Developer Connect Git repository resource must already exist. Refer to [Developer
Connect documentation](http://cloud.google.com/developer-connect/docs/connect-repo) for more details.
To create a repository group `my-repository-group` for a code
repository index instance `my-instance` in project
`my-project` and location `us-central1` with Developer
Connect repositories defined in a separate file, run:

```
gcloud gemini code-repository-indexes repository-groups create my-repository-group --code-repository-index=my-instance --project=my-project --location=us-central1 --repositories=@/path/to/repositories.json
```

Developer Connect Git repository resource must already exist. Refer to [Developer
Connect documentation](http://cloud.google.com/developer-connect/docs/connect-repo) for more details.

**POSITIONAL ARGUMENTS**

: **RepositoryGroup resource - Identifier. name of resource The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `repository_group` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`REPOSITORY_GROUP`**:
ID of the repositoryGroup or fully qualified identifier for the repositoryGroup.
To set the `repository_group` attribute:

- provide the argument `repository_group` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--code-repository-index**:
The codeRepositoryIndex id of the repositoryGroup resource.
To set the `code-repository-index` attribute:

- provide the argument `repository_group` on the command line with a
fully specified name;
- provide the argument `--code-repository-index` on the command line.

**--location**:
The location id of the repositoryGroup resource.
To set the `location` attribute:

- provide the argument `repository_group` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **--repositories**:
Required, List of repositories to group.

**`branchPattern`**:
The Git branch pattern used for indexing in RE2 syntax. See [https://github.com/google/re2/wiki/syntax](https://github.com/google/re2/wiki/syntax)
for syntax.

**`resource`**:
The DeveloperConnect repository full resource name, relative resource name or
resource URL to be indexed.

`Shorthand Example:`

```
--repositories=branchPattern=string,resource=string --repositories=branchPattern=string,resource=string
```

`JSON Example:`

```
--repositories='[{"branchPattern": "string", "resource": "string"}]'
```

`File Example:`

```
--repositories=path_to_file.(yaml|json)
```

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
The request ID must be a valid UUID with the exception that zero UUID is not
supported (00000000-0000-0000-0000-000000000000).

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

: This command uses the `cloudaicompanion/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/gemini](https://cloud.google.com/gemini)