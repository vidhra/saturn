# gcloud gemini code-repository-indexes repository-groups describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/describe](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/describe)*

**NAME**

: **gcloud gemini code-repository-indexes repository-groups describe - get details of a code repository index instance**

**SYNOPSIS**

: **`gcloud gemini code-repository-indexes repository-groups describe` (`[REPOSITORY_GROUP](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/describe#REPOSITORY_GROUP)` : `[--code-repository-index](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/describe#--code-repository-index)`=`CODE_REPOSITORY_INDEX` `[--location](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get details of a code repository index instance.

**EXAMPLES**

: To get the details of repository group `my-repository-group` of a
code repository index instance `my-instance` in project
`my-project` and location `us-central1`, run:

```
gcloud gemini code-repository-indexes repository-groups describe my-repository-group --code-repository-index=my-instance --project=my-project --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **RepositoryGroup resource - Name of the resource The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
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