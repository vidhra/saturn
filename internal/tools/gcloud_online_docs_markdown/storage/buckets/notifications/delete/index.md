# gcloud storage buckets notifications delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/delete](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/delete)*

**NAME**

: **gcloud storage buckets notifications delete - delete notification configurations from a bucket**

**SYNOPSIS**

: **`gcloud storage buckets notifications delete` `[URLS](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/delete#URLS)` [`[URLS](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/delete#URLS)` …] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud storage buckets notifications delete` deletes notification
configurations from a bucket. If a notification configuration name is passed as
a parameter, that configuration alone is deleted. If a bucket name is passed,
all notification configurations associated with the bucket are deleted.
Cloud Pub/Sub topics associated with this notification configuration are not
deleted by this command. Those must be deleted separately, for example with the
command "gcloud pubsub topics delete".

**EXAMPLES**

: Delete a single notification configuration (with ID 3) in the bucket
`example-bucket`:

```
gcloud storage buckets notifications delete projects/_/buckets/example-bucket/notificationConfigs/3
```

Delete all notification configurations in the bucket
`example-bucket`:

```
gcloud storage buckets notifications delete gs://example-bucket
```

**POSITIONAL ARGUMENTS**

: **`URLS` [`URLS` …]**:
Specifies notification configuration names or buckets.

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
gcloud alpha storage buckets notifications delete
```