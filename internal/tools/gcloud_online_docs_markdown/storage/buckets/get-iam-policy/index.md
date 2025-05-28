# gcloud storage buckets get-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/buckets/get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/get-iam-policy)*

**NAME**

: **gcloud storage buckets get-iam-policy - get the IAM policy for a bucket**

**SYNOPSIS**

: **`gcloud storage buckets get-iam-policy` `[URL](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/get-iam-policy#URL)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/get-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get the IAM policy for a bucket. For more information, see [Cloud Identity
and Access Management](https://cloud.google.com/storage/docs/access-control/iam).

**EXAMPLES**

: To get the IAM policy for BUCKET:

```
gcloud storage buckets get-iam-policy gs://BUCKET
```

To output the IAM policy for BUCKET to a file:

```
gcloud storage buckets get-iam-policy gs://BUCKET > policy.txt
```

**POSITIONAL ARGUMENTS**

: **`URL`**:
Request IAM policy for this bucket.

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
gcloud alpha storage buckets get-iam-policy
```