# gcloud artifacts yum import  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/yum/import](https://cloud.google.com/sdk/gcloud/reference/artifacts/yum/import)*

**NAME**

: **gcloud artifacts yum import - import one or more RPM packages into an artifact repository**

**SYNOPSIS**

: **`gcloud artifacts yum import` [[`[REPOSITORY](https://cloud.google.com/sdk/gcloud/reference/artifacts/yum/import#REPOSITORY)`] `[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/yum/import#--location)`=`LOCATION`] `[--gcs-source](https://cloud.google.com/sdk/gcloud/reference/artifacts/yum/import#--gcs-source)`=[`GCS_SOURCE`,…] [`[--async](https://cloud.google.com/sdk/gcloud/reference/artifacts/yum/import#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/yum/import#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud artifacts yum import` imports RPM packages from Google Cloud
Storage into the specified artifact repository.

**EXAMPLES**

: To import the package `my-package.rpm` from Google Cloud Storage into
`my-repo`, run:

```
gcloud artifacts yum import my-repo --location=us-central1 --gcs-source=gs://my-bucket/path/to/my-package.rpm
```

To import the packages `my-package.rpm` and
`other-package.rpm` into `my-repo`, run:

```
gcloud artifacts yum import my-repo --location=us-central1 --gcs-source=gs://my-bucket/path/to/my-package.rpm,gs://my-bucket/path/to/other-package.rpm
```

To import all packages from `my-directory` into `my-repo`,
run:

```
gcloud artifacts yum import my-repo --location=us-central1 --gcs-source=gs://my-bucket/my-directory/*
```

To import all packages in all subdirectories from a Google Cloud Storage bucket
into `my-repo`, run:

```
gcloud artifacts yum import my-repo --location=us-central1 --gcs-source=gs://my-bucket/**
```

**POSITIONAL ARGUMENTS**

: **Repository resource - The Artifact Registry repository. If not specified, the
current artifacts/repository is used. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `repository` on the command line with a fully
specified name;
- set the property `artifacts/repository` with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**[`REPOSITORY`]**:
ID of the repository or fully qualified identifier for the repository.
To set the `repository` attribute:

- provide the argument `repository` on the command line;
- set the property `artifacts/repository`.

**--location**:
Location of the repository.
To set the `location` attribute:

- provide the argument `repository` on the command line with a fully
specified name;
- set the property `artifacts/repository` with a fully specified name;
- provide the argument `--location` on the command line;
- set the property `artifacts/location`.**

**REQUIRED FLAGS**

: **--gcs-source**:
The Google Cloud Storage location of a package to import. To import multiple
packages, use wildcards at the end of the path.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

: These variants are also available:

```
gcloud alpha artifacts yum import
```

```
gcloud beta artifacts yum import
```