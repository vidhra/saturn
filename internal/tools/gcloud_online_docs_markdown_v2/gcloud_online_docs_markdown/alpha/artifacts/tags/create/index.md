# gcloud alpha artifacts tags create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/create](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/create)*

**NAME**

: **gcloud alpha artifacts tags create - create an Artifact Registry tag**

**SYNOPSIS**

: **`gcloud alpha artifacts tags create` (`[TAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/create#TAG)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/create#--location)`=`LOCATION` `[--package](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/create#--package)`=`PACKAGE` `[--repository](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/create#--repository)`=`REPOSITORY`) `[--version](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/create#--version)`=`VERSION` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a new Artifact Registry tag.
This command can fail for the following reasons:

- A tag with the same name already exists.
- The specified version or package does not exist.
- The active account does not have permission to create tags.
- The specified package format doesn't support tag operations (e.g. maven).

**EXAMPLES**

: To create a tag with the name `my-tag` for version `1.0.0`
of package `my-pkg` under the current project, repository, and
location, run:

```
gcloud alpha artifacts tags create my-tag --version=1.0.0 --package=my-pkg
```

**POSITIONAL ARGUMENTS**

: **Tag resource - The Artifact Registry tag to create. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `tag` on the command line with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TAG`**:
ID of the tag or fully qualified identifier for the tag.
To set the `tag` attribute:

- provide the argument `tag` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the tag. Overrides the default artifacts/location property value for
this command invocation. To configure the default location, use the command:
gcloud config set artifacts/location.
To set the `location` attribute:

- provide the argument `tag` on the command line with a fully specified
name;
- provide the argument `--location` on the command line;
- set the property `artifacts/location`.

**--package**:
The package associated with the tag.
To set the `package` attribute:

- provide the argument `tag` on the command line with a fully specified
name;
- provide the argument `--package` on the command line.

**--repository**:
The repository associated with the tag. Overrides the default
artifacts/repository property value for this command invocation. To configure
the default repository, use the command: gcloud config set artifacts/repository.
To set the `repository` attribute:

- provide the argument `tag` on the command line with a fully specified
name;
- provide the argument `--repository` on the command line;
- set the property `artifacts/repository`.**

**REQUIRED FLAGS**

: **--version**:
The version associated with the tag.

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
gcloud artifacts tags create
```

```
gcloud beta artifacts tags create
```