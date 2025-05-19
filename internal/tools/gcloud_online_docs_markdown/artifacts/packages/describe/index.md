# gcloud artifacts packages describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/describe](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/describe)*

**NAME**

: **gcloud artifacts packages describe - describe an Artifact Registry package**

**SYNOPSIS**

: **`gcloud artifacts packages describe` (`[PACKAGE](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/describe#PACKAGE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/describe#--location)`=`LOCATION` `[--repository](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/describe#--repository)`=`REPOSITORY`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe an Artifact Registry package.
This command can fail for the following reasons:

- The specified package does not exist.
- The active account does not have permission to view packages.

**EXAMPLES**

: To describe a package named `my-pkg` under the current project,
repository, and location, run:

```
gcloud artifacts packages describe my-pkg
```

**POSITIONAL ARGUMENTS**

: **Package resource - The Artifact Registry package to describe. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `package` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`PACKAGE`**:
ID of the package or fully qualified identifier for the package.
To set the `package` attribute:

- provide the argument `package` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the package. Overrides the default artifacts/location property value
for this command invocation. To configure the default location, use the command:
gcloud config set artifacts/location.
To set the `location` attribute:

- provide the argument `package` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `artifacts/location`.

**--repository**:
The repository associated with the package. Overrides the default
artifacts/repository property value for this command invocation. To configure
the default repository, use the command: gcloud config set artifacts/repository.
To set the `repository` attribute:

- provide the argument `package` on the command line with a fully
specified name;
- provide the argument `--repository` on the command line;
- set the property `artifacts/repository`.**

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