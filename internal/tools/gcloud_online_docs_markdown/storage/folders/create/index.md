# gcloud storage folders create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/folders/create](https://cloud.google.com/sdk/gcloud/reference/storage/folders/create)*

**NAME**

: **gcloud storage folders create - create folders for hierarchical namespace bucket**

**SYNOPSIS**

: **`gcloud storage folders create` `[URL](https://cloud.google.com/sdk/gcloud/reference/storage/folders/create#URL)` [`[URL](https://cloud.google.com/sdk/gcloud/reference/storage/folders/create#URL)` …] [`[--additional-headers](https://cloud.google.com/sdk/gcloud/reference/storage/folders/create#--additional-headers)`=`HEADER`=`VALUE`] [`[--recursive](https://cloud.google.com/sdk/gcloud/reference/storage/folders/create#--recursive)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/folders/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create folders.

**EXAMPLES**

: The following command creates a folder called `folder/` in a bucket
named `my-bucket`:

```
gcloud storage folders create gs://my-bucket/folder/
```

The following command creates all folders in the path `A/B/C/D` in a
bucket named `my-bucket`:

```
gcloud storage folders create --recursive gs://my-bucket/folder/A/B/C/D
```

**POSITIONAL ARGUMENTS**

: **`URL` [`URL` …]**:
The URLs of the folders to create.

**FLAGS**

: **--additional-headers**:
Includes arbitrary headers in storage API calls. Accepts a comma separated list
of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides
the default `storage/additional_headers` property value for this
command invocation.

**--recursive**:
Recursively create all folders in a given path if they do not alraedy exist.

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

: This variant is also available:

```
gcloud alpha storage folders create
```