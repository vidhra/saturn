# gcloud alpha artifacts repositories update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories/update](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories/update)*

**NAME**

: **gcloud alpha artifacts repositories update - update an Artifact Registry repository**

**SYNOPSIS**

: **`gcloud alpha artifacts repositories update` (`[REPOSITORY](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories/update#REPOSITORY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories/update#--location)`=`LOCATION`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories/update#--description)`=`DESCRIPTION`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update the description or labels for an Artifact Registry
repository.
This command can fail for the following reasons:

- A repository with this name does not exist.
- The active account does not have permission to update repositories.

**EXAMPLES**

: To update a repository with the name `my-repo` under the current
project, run:

```
gcloud alpha artifacts repositories update my-repo --description="New description"
```

**POSITIONAL ARGUMENTS**

: **Repository resource - The Artifact Registry repository to update. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `repository` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`REPOSITORY`**:
ID of the repository or fully qualified identifier for the repository.
To set the `repository` attribute:

- provide the argument `repository` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the repository. Overrides the default artifacts/location property
value for this command invocation. To configure the default location, use the
command: gcloud config set artifacts/location.
To set the `location` attribute:

- provide the argument `repository` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `artifacts/location`.**

**FLAGS**

: **--description**:
Description for the repository.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

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

: This command uses the `artifactregistry/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/artifacts/docs/](https://cloud.google.com/artifacts/docs/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud artifacts repositories update
```

```
gcloud beta artifacts repositories update
```