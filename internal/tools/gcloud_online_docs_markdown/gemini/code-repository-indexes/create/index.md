# gcloud gemini code-repository-indexes create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/create](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/create)*

**NAME**

: **gcloud gemini code-repository-indexes create - create a code repository index instance**

**SYNOPSIS**

: **`gcloud gemini code-repository-indexes create` (`[CODE_REPOSITORY_INDEX](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/create#CODE_REPOSITORY_INDEX)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/create#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/create#--async)`] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/create#--kms-key)`=`KMS_KEY`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/create#--labels)`=[`LABELS`,…]] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/create#--request-id)`=`REQUEST_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a code repository index instance.
The instance will be created in the specified project and location.

**EXAMPLES**

: To create a code repository index instance `my-instance` in project
`my-project` and location `us-central1`, run:

```
gcloud gemini code-repository-indexes create my-instance --project=my-project --location=us-central1
```

To create a code repository index instance `my-instance` in project
`my-project`, location `us-central1` with your managed
encryption key run:

```
gcloud gemini code-repository-indexes create my-instance --project=my-project --location=us-central1 --kms-key=projects/*/locations/*/keyRings/*/cryptoKeys/*
```

Note: --kms-key can be only passed during index creation and can not be used
during update.

**POSITIONAL ARGUMENTS**

: **CodeRepositoryIndex resource - Identifier. name of resource The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `code_repository_index` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CODE_REPOSITORY_INDEX`**:
ID of the codeRepositoryIndex or fully qualified identifier for the
codeRepositoryIndex.
To set the `code_repository_index` attribute:

- provide the argument `code_repository_index` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location id of the codeRepositoryIndex resource.
To set the `location` attribute:

- provide the argument `code_repository_index` on the command line with
a fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--kms-key**:
Customer-managed encryption key name, in the format
projects/*/locations/*/keyRings/*/cryptoKeys/*.

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