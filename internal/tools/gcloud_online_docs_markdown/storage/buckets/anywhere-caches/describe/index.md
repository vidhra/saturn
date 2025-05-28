# gcloud storage buckets anywhere-caches describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/describe](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/describe)*

**NAME**

: **gcloud storage buckets anywhere-caches describe - returns details of Anywhere Cache instance of a bucket**

**SYNOPSIS**

: **`gcloud storage buckets anywhere-caches describe` `[ID](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/describe#ID)` [`[--raw](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/describe#--raw)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Desribes a single Anywhere Cache instance if it exists.

**EXAMPLES**

: The following command describes the anywhere cache instance of bucket
``my-bucket`` having anywhere_cache_id
``my-cache-id``:

```
gcloud storage buckets anywhere-caches describe my-bucket/my-cache-id
```

**POSITIONAL ARGUMENTS**

: **`ID`**:
Identifier for a Anywhere Cache instance. It is a combination of
bucket_name/anywhere_cache_id, For example : test-bucket/my-cache-id.

**FLAGS**

: **--raw**:
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
gcloud alpha storage buckets anywhere-caches describe
```