# gcloud artifacts repositories update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/update](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/update)*

**NAME**

: **gcloud artifacts repositories update - update an Artifact Registry repository**

**SYNOPSIS**

: **`gcloud artifacts repositories update` (`[REPOSITORY](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/update#REPOSITORY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/update#--location)`=`LOCATION`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/update#--description)`=`DESCRIPTION`] [`[--disable-remote-validation](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/update#--disable-remote-validation)`] [`[--immutable-tags](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/update#--immutable-tags)`] [`[--remote-password-secret-version](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/update#--remote-password-secret-version)`=`REMOTE_PASSWORD_SECRET_VERSION`] [`[--remote-username](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/update#--remote-username)`=`REMOTE_USERNAME`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--upstream-policy-file](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/update#--upstream-policy-file)`=`FILE`] [`[--allow-vulnerability-scanning](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/update#--allow-vulnerability-scanning)`     | `[--disable-vulnerability-scanning](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/update#--disable-vulnerability-scanning)`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the description or labels for an Artifact Registry repository.
This command can fail for the following reasons:

- A repository with this name does not exist.
- The active account does not have permission to update repositories.

**EXAMPLES**

: To update a repository with the name `my-repo` under the current
project, run:

```
gcloud artifacts repositories update my-repo --description="New description"
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

**--disable-remote-validation**:
Do not make an HTTP request to validate the remote upstream. Not recommended
when setting a custom remote upstream unless you are absolutely sure your
upstream URI and any auth is valid.

**--immutable-tags**:
(Docker only) Prevent changes to tagged images in the repository. Tags cannot be
deleted or moved to a different image digest, and tagged images cannot be
deleted.

**--remote-password-secret-version**:
Secret Manager secret version that contains password for the remote repository
upstream.

**--remote-username**:
Remote Repository upstream registry username.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--upstream-policy-file**:
(Virtual Repositories only) is the upstreams for the Virtual Repository. Example
of the file contents: [ { "id": "test1", "repository":
"projects/p1/locations/us-central1/repositories/repo1", "priority": 1 }, { "id":
"test2", "repository": "projects/p2/locations/us-west2/repositories/repo2",
"priority": 2 } ]

**--allow-vulnerability-scanning**

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

: These variants are also available:

```
gcloud alpha artifacts repositories update
```

```
gcloud beta artifacts repositories update
```