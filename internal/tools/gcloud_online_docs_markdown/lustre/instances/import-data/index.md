# gcloud lustre instances import-data  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/lustre/instances/import-data](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/import-data)*

**NAME**

: **gcloud lustre instances import-data - imports data from Cloud Storage to Managed Lustre instance**

**SYNOPSIS**

: **`gcloud lustre instances import-data` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/import-data#INSTANCE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/import-data#--location)`=`LOCATION`) `[--gcs-path-uri](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/import-data#--gcs-path-uri)`=`GCS_PATH_URI` [`[--async](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/import-data#--async)`] [`[--lustre-path](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/import-data#--lustre-path)`=`LUSTRE_PATH`] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/import-data#--request-id)`=`REQUEST_ID`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/import-data#--service-account)`=`SERVICE_ACCOUNT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/lustre/instances/import-data#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Imports data from Cloud Storage to Managed Lustre instance.

**EXAMPLES**

: To import data from `gs://my-bucket` storage to
`my-instance` run:

```
gcloud lustre instances import-data my-instance --location=us-central-a --gcs-path-uri=gs://my_bucket --lustre-path='/path/to/lustre/dir'
```

**POSITIONAL ARGUMENTS**

: **Instance resource - Name of the resource. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `instance` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location id of the instance resource.
To set the `location` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **--gcs-path-uri**:
The URI to a Cloud Storage bucket, or a path within a bucket, using the format
`gs://<bucket_name>/<optional_path_inside_bucket>/`. If a
path inside the bucket is specified, it must end with a forward slash
(`/`).

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--lustre-path**:
The root directory path to the Managed Lustre file system. Must start with
`/`. Default is `/`. If you're importing data into Managed
Lustre, any path other than the default must already exist on the file system.

**--request-id**:
UUID to identify requests.

**ServiceAccount resource - User-specified service account used to perform the
transfer. If unspecified, the default Managed Lustre service agent will be used.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--service-account` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--service-account**:
ID of the serviceAccount or fully qualified identifier for the serviceAccount.
To set the `service-account` attribute:

- provide the argument `--service-account` on the command line.**

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

: This command uses the `lustre/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/managed-lustre/](https://cloud.google.com/managed-lustre/)

**NOTES**

: This variant is also available:

```
gcloud alpha lustre instances import-data
```