# gcloud storage managed-folders delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/delete](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/delete)*

**NAME**

: **gcloud storage managed-folders delete - delete managed folders**

**SYNOPSIS**

: **`gcloud storage managed-folders delete` `[URL](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/delete#URL)` [`[URL](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/delete#URL)` …] [`[--additional-headers](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/delete#--additional-headers)`=`HEADER`=`VALUE`] [`[--continue-on-error](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/delete#--continue-on-error)`, `[-c](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/delete#-c)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete managed folders.

**EXAMPLES**

: The following command deletes a managed folder named `folder` in a
bucket called `my-bucket`:

```
gcloud storage managed-folders delete gs://my-bucket/folder/
```

**POSITIONAL ARGUMENTS**

: **`URL` [`URL` …]**:
The URLs of the managed folders to delete.

**FLAGS**

: **--additional-headers**:
Includes arbitrary headers in storage API calls. Accepts a comma separated list
of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides
the default `storage/additional_headers` property value for this
command invocation.

**--continue-on-error**:
If any operations are unsuccessful, the command will exit with a non-zero exit
status after completing the remaining operations. This flag takes effect only in
sequential execution mode (i.e. processor and thread count are set to 1).
Parallelism is default.

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
gcloud alpha storage managed-folders delete
```