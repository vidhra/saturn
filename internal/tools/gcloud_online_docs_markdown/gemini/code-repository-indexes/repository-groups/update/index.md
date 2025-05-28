# gcloud gemini code-repository-indexes repository-groups update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/update](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/update)*

**NAME**

: **gcloud gemini code-repository-indexes repository-groups update - update the configuration of a repository group**

**SYNOPSIS**

: **`gcloud gemini code-repository-indexes repository-groups update` (`[REPOSITORY_GROUP](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/update#REPOSITORY_GROUP)` : `[--code-repository-index](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/update#--code-repository-index)`=`CODE_REPOSITORY_INDEX` `[--location](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/update#--async)`] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/update#--request-id)`=`REQUEST_ID`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/update#--labels)`=[`LABELS`,…]     | `[--update-labels](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/update#--update-labels)`=[`UPDATE_LABELS`,…] `[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/update#--remove-labels)`=[__REMOVE_LABELS,…]] [`[--repositories](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/update#--repositories)`=[`branchPattern`=`BRANCHPATTERN`],[`resource`=`RESOURCE`]     | `[--add-repositories](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/update#--add-repositories)`=[`branchPattern`=`BRANCHPATTERN`],[`resource`=`RESOURCE`] `[--clear-repositories](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/update#--clear-repositories)`     | `[--remove-repositories](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/update#--remove-repositories)`=[`branchPattern`=`BRANCHPATTERN`],[`resource`=`RESOURCE`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the configuration of a repository group.

**EXAMPLES**

: To update repository group `my-repository-group` of code repository
index instance `my-instance` in project `my-project` and
location `us-central1` with a new branch pattern for one of the Git
repositories, run:

```
gcloud gemini code-repository-indexes repository-groups update my-repository-group --code-repository-index=my-instance --project=my-project --location=us-central1 --repositories=branchPattern=new_branch,resource=developerconnect.googleapis.com/projects/<PROJECT>/locations/<LOCATION>/connections/<CONNECTION>/gitRepositoryLinks/<REPOSITORY>
```

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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--request-id**:
An optional request ID to identify requests. Specify a unique request ID so that
if you must retry your request, the server will know to ignore the request if it
has already been completed. The server will guarantee that for at least 60
minutes since the first request.
The request ID must be a valid UUID with the exception that zero UUID is not
supported (00000000-0000-0000-0000-000000000000).

**--labels**

**--repositories**

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