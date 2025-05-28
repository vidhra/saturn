# gcloud storage buckets anywhere-caches pause  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/pause](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/pause)*

**NAME**

: **gcloud storage buckets anywhere-caches pause - pause Anywhere Cache instances**

**SYNOPSIS**

: **`gcloud storage buckets anywhere-caches pause` `[ID](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/pause#ID)` [`[ID](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/pause#ID)` …] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/pause#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The pause operation can be used to stop the data ingestion of a cache instance
in RUNNING state (read-only cache) until the Resume is invoked.

**EXAMPLES**

: The following command pause the anywhere cache instance of bucket
``my-bucket`` having anywhere_cache_id
``my-cache-id``:

```
gcloud storage buckets anywhere-caches pause my-bucket/my-cache-id
```

**POSITIONAL ARGUMENTS**

: **`ID` [`ID` …]**:
Identifiers for a Anywhere Cache instance. They are combination of
bucket_name/anywhere_cache_id. For example : test-bucket/my-cache-id.

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
gcloud alpha storage buckets anywhere-caches pause
```