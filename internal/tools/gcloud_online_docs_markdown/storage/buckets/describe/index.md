# gcloud storage buckets describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/buckets/describe](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/describe)*

**NAME**

: **gcloud storage buckets describe - describes Cloud Storage buckets**

**SYNOPSIS**

: **`gcloud storage buckets describe` `[URL](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/describe#URL)` [`[--additional-headers](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/describe#--additional-headers)`=`HEADER`=`VALUE`] [`[--raw](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/describe#--raw)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Cloud Storage bucket.

**EXAMPLES**

: Describe a Google Cloud Storage bucket named "my-bucket":

```
gcloud storage buckets describe gs://my-bucket
```

Describe bucket with JSON formatting, only returning the "name" key:

```
gcloud storage buckets describe gs://my-bucket --format="json(name)"
```

**POSITIONAL ARGUMENTS**

: **`URL`**:
Specifies URL of bucket to describe.

**FLAGS**

: **--additional-headers**:
Includes arbitrary headers in storage API calls. Accepts a comma separated list
of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides
the default `storage/additional_headers` property value for this
command invocation.

**--raw**:
Shows metadata in the format returned by the API instead of standardizing it.

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
gcloud alpha storage buckets describe
```