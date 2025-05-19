# gcloud alpha artifacts print-settings mvn  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/mvn](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/mvn)*

**NAME**

: **gcloud alpha artifacts print-settings mvn - print a snippet to add a Maven repository to the pom.xml file**

**SYNOPSIS**

: **`gcloud alpha artifacts print-settings mvn` [`[--json-key](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/mvn#--json-key)`=`JSON_KEY`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/mvn#--location)`=`LOCATION` `[--repository](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/mvn#--repository)`=`REPOSITORY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/mvn#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Print a snippet to add a Maven repository to the pom.xml
file.

**EXAMPLES**

: To print a snippet for the repository set in the
`artifacts/repository` property in the default location:

```
gcloud alpha artifacts print-settings mvn
```

To print a snippet for repository `my-repository` in the default
location:

```
gcloud alpha artifacts print-settings mvn --repository="my-repository"
```

To print a snippet using service account key:

```
gcloud alpha artifacts print-settings mvn --json-key=path/to/key.json
```

**FLAGS**

: **--json-key**:
Path to service account JSON key. If not specified, current active service
account credentials or a placeholder for gcloud credentials is used.

**Repository resource - The Artifact Registry repository. If not specified, the
current artifacts/repository is used. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--repository` on the command line with a fully
specified name;
- set the property `artifacts/repository` with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--location**:
Location of the repository.
To set the `location` attribute:

- provide the argument `--repository` on the command line with a fully
specified name;
- set the property `artifacts/repository` with a fully specified name;
- provide the argument `--location` on the command line;
- set the property `artifacts/location`.

**--repository**:
ID of the repository or fully qualified identifier for the repository.
To set the `repository` attribute:

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

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud artifacts print-settings mvn
```

```
gcloud beta artifacts print-settings mvn
```