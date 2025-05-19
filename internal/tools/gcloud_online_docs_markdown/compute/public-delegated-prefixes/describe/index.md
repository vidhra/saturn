# gcloud compute public-delegated-prefixes describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/describe](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/describe)*

**NAME**

: **gcloud compute public-delegated-prefixes describe - describes a Compute Engine public delegated prefix**

**SYNOPSIS**

: **`gcloud compute public-delegated-prefixes describe` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/describe#NAME)` [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/describe#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/describe#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/describe#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To describe a public delegated prefix:

```
gcloud compute public-delegated-prefixes describe my-public-delegated-prefix --global
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the public delegated prefix to operate on.

**FLAGS**

: **--global**

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

: These variants are also available:

```
gcloud alpha compute public-delegated-prefixes describe
```

```
gcloud beta compute public-delegated-prefixes describe
```