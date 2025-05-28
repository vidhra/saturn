# gcloud storage buckets notifications describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/describe](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/describe)*

**NAME**

: **gcloud storage buckets notifications describe - show metadata for a notification configuration**

**SYNOPSIS**

: **`gcloud storage buckets notifications describe` `[URL](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/describe#URL)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/notifications/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud storage buckets notifications describe` prints populated
metadata for a notification configuration.

**EXAMPLES**

: Describe a single notification configuration (with ID 3) in the bucket
`example-bucket`:

```
gcloud storage buckets notifications describe projects/_/buckets/example-bucket/notificationConfigs/3
```

**POSITIONAL ARGUMENTS**

: **`URL`**:
The url of the notification configuration

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
gcloud alpha storage buckets notifications describe
```