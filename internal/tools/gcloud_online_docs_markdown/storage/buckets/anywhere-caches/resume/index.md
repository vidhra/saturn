# gcloud storage buckets anywhere-caches resume  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/resume](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/resume)*

**NAME**

: **gcloud storage buckets anywhere-caches resume - resume Anywhere Cache instances**

**SYNOPSIS**

: **`gcloud storage buckets anywhere-caches resume` `[ID](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/resume#ID)` [`[ID](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/resume#ID)` …] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/resume#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Resume operation could be used to revert the Paused and Disabled state. Once a
paused/disabled cache is resumed, the cache will be set to RUNNING/CREATING
state: 1. RUNNING if the cache is active. 2. CREATING if the cache is pending
creation.

**EXAMPLES**

: The following command resume the anywhere cache instance of bucket
``my-bucket`` having anywhere_cache_id
``my-cache-id``:

```
gcloud storage buckets anywhere-caches resume my-bucket/my-cache-id
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
gcloud alpha storage buckets anywhere-caches resume
```