# gcloud storage buckets delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/buckets/delete](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/delete)*

**NAME**

: **gcloud storage buckets delete - deletes Cloud Storage buckets**

**SYNOPSIS**

: **`gcloud storage buckets delete` `[URLS](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/delete#URLS)` [`[URLS](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/delete#URLS)` …] [`[--additional-headers](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/delete#--additional-headers)`=`HEADER`=`VALUE`] [`[--continue-on-error](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/delete#--continue-on-error)`, `[-c](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/delete#-c)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Deletes one or more Cloud Storage buckets.

**EXAMPLES**

: Delete a Google Cloud Storage bucket named "my-bucket":

```
gcloud storage buckets delete gs://my-bucket
```

Delete two buckets:

```
gcloud storage buckets delete gs://my-bucket gs://my-other-bucket
```

**POSITIONAL ARGUMENTS**

: **`URLS` [`URLS` …]**:
Specifies the URLs of the buckets to delete.

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
gcloud alpha storage buckets delete
```