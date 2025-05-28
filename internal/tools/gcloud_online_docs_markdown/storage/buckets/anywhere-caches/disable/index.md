# gcloud storage buckets anywhere-caches disable  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/disable](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/disable)*

**NAME**

: **gcloud storage buckets anywhere-caches disable - disable Anywhere Cache instances**

**SYNOPSIS**

: **`gcloud storage buckets anywhere-caches disable` `[ID](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/disable#ID)` [`[ID](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/disable#ID)` …] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/disable#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Disables one or more Anywhere Cache instances.
The cache instance will be set to DISABLED state. The existing entries can be
read from the cache but new entries will not be written to the cache. The L4 SSD
cache would not be deleted by the cache manager until the min TTL (1h) has been
reached (cache instance is kept for at least 1h). Google Cloud Storage defines
the min TTL which is applied to all cache instances. Cach disablement could be
canceled by using anywhere-caches resume command before the instance is deleted.

**EXAMPLES**

: The following command disables the anywhere cache instance of bucket
``my-bucket`` having anywhere_cache_id
``my-cache-id``:

```
gcloud storage buckets anywhere-caches disable my-bucket/my-cache-id
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
gcloud alpha storage buckets anywhere-caches disable
```