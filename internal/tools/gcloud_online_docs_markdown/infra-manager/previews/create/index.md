# gcloud infra-manager previews create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create)*

**NAME**

: **gcloud infra-manager previews create - create a preview**

**SYNOPSIS**

: **`gcloud infra-manager previews create` [`[PREVIEW](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create#PREVIEW)`] [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create#--annotations)`=[`KEY`=`VALUE`,…]] [`[--artifacts-gcs-bucket](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create#--artifacts-gcs-bucket)`=`ARTIFACTS_GCS_BUCKET`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create#--async)`] [`[--deployment](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create#--deployment)`=`DEPLOYMENT`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--location](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create#--location)`=`LOCATION`] [`[--preview-mode](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create#--preview-mode)`=`PREVIEW_MODE`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create#--service-account)`=`SERVICE_ACCOUNT`] [`[--worker-pool](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create#--worker-pool)`=`WORKER_POOL`] [`[--gcs-source](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create#--gcs-source)`=`GCS_SOURCE`     | `[--git-source-directory](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create#--git-source-directory)`=`GIT_SOURCE_DIRECTORY` `[--git-source-ref](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create#--git-source-ref)`=`GIT_SOURCE_REF` `[--git-source-repo](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create#--git-source-repo)`=`GIT_SOURCE_REPO`     | `[--ignore-file](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create#--ignore-file)`=`IGNORE_FILE` `[--local-source](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create#--local-source)`=`LOCAL_SOURCE` `[--input-values](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create#--input-values)`=[`KEY`=`VALUE`,…]     | `[--inputs-file](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create#--inputs-file)`=`INPUTS_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/infra-manager/previews/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command creates a preview.

**EXAMPLES**

: Create a preview named `my-preview` from a storage
`my-bucket`:

```
gcloud infra-manager previews create projects/p1/locations/us-central1/previews/my-preview --gcs-source="gs://my-bucket" --input-values="project=p1,region=us-central1"
```

Create a preview named `my-preview` from git repo
"https://github.com/examples/repository.git", "staging/compute" folder,
"mainline" branch:

```
gcloud infra-manager previews create projects/p1/locations/us-central1/previews/my-preview --git-source-repo="https://github.com/examples/repository.git" --git-source-directory="staging/compute" --git-source-ref="mainline"
```

**POSITIONAL ARGUMENTS**

: **Preview resource - the preview to be used as parent. It is optional and will be
generated if not specified with a fully specified name. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `PREVIEW` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `PREVIEW` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `infra-manager/location`.

**`PREVIEW`**:
ID of the preview or fully qualified identifier for the preview.
To set the `preview` attribute:

- provide the argument `PREVIEW` on the command line.**

**FLAGS**

: **--annotations**:
Preview annotations cannot be updated after creation.

**--artifacts-gcs-bucket**:
user-defined location of Cloud Build logs, artifacts, and Terraform state files
in Google Cloud Storage. Format: `gs://{bucket}/{folder}` A default
bucket will be bootstrapped if the field is not set or empty

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--deployment**:
Deployment reference for preview.

**--labels**:
Preview labels cannot be updated after creation.

**Location resource - the location to be used as parent. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- set the property `infra-manager/location` with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line;
- set the property `infra-manager/location`.**

**--preview-mode**:
Preview mode to set it to either default or delete.

**--service-account**:
User-specified Service Account (SA) to be used as credential to manage
resources. Format:
`projects/{projectID}/serviceAccounts/{serviceAccount}`

**--worker-pool**:
User-specified Worker Pool resource in which the Cloud Build job will execute.
Format: projects/{project}/locations/{location}/workerPools/{workerPoolId}

**--gcs-source**

**--input-values**

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