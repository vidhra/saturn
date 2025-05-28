# gcloud storage buckets anywhere-caches update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/update](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/update)*

**NAME**

: **gcloud storage buckets anywhere-caches update - update Anywhere Cache instances**

**SYNOPSIS**

: **`gcloud storage buckets anywhere-caches update` `[ID](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/update#ID)` [`[ID](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/update#ID)` …] [`[--admission-policy](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/update#--admission-policy)`=`ADMISSION_POLICY`] [`[--ttl](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/update#--ttl)`=`TTL`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update one or more Anywhere Cache instances. A cache instance can be updated if
its state is created or pending creation.

**EXAMPLES**

: The following command updates cache entry's ttl, and admisson policy of anywhere
cache instance in bucket ``my-bucket`` having
anywhere_cache_id ``my-cache-id``:

```
gcloud storage buckets anywhere-caches update my-bucket/my-cache-id --ttl=6h --admission-policy='ADMIT_ON_SECOND_MISS'
```

The following command updates cache entry's ttl of anywhere cache instances in
bucket ``bucket-1`` and
``bucket-2`` having anywhere_cache_id
``my-cache-id-1``, and
``my-cache-id-2`` respectively:

```
gcloud storage buckets anywhere-caches update bucket-1/my-cache-id-1 bucket-2/my-cache-id-2 --ttl=6h
```

**POSITIONAL ARGUMENTS**

: **`ID` [`ID` …]**:
Identifiers for a Anywhere Cache Instance.They are combination of
bucket_name/anywhere_cache_id. For example : test-bucket/my-cache-id.

**FLAGS**

: **--admission-policy**:
The cache admission policy decides for each cache miss, whether to insert the
missed block or not. `ADMISSION_POLICY` must be one of:
`ADMIT_ON_FIRST_MISS`, `ADMIT_ON_SECOND_MISS`.

**--ttl**:
Cache entry time-to-live. Default to 24h if not provided.

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
gcloud alpha storage buckets anywhere-caches update
```