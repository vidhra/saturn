# gcloud storage folders delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/folders/delete](https://cloud.google.com/sdk/gcloud/reference/storage/folders/delete)*

**NAME**

: **gcloud storage folders delete - delete folders**

**SYNOPSIS**

: **`gcloud storage folders delete` `[URLS](https://cloud.google.com/sdk/gcloud/reference/storage/folders/delete#URLS)` [`[URLS](https://cloud.google.com/sdk/gcloud/reference/storage/folders/delete#URLS)` …] [`[--additional-headers](https://cloud.google.com/sdk/gcloud/reference/storage/folders/delete#--additional-headers)`=`HEADER`=`VALUE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/folders/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete folders.

**EXAMPLES**

: The following command deletes a folder named `folder` in a
hierarchical namesapce bucket called `my-bucket`:

```
gcloud storage folders delete gs://my-bucket/folder/
```

**POSITIONAL ARGUMENTS**

: **`URLS` [`URLS` …]**:
The URLs of the folders to delete.

**FLAGS**

: **--additional-headers**:
Includes arbitrary headers in storage API calls. Accepts a comma separated list
of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides
the default `storage/additional_headers` property value for this
command invocation.

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
gcloud alpha storage folders delete
```