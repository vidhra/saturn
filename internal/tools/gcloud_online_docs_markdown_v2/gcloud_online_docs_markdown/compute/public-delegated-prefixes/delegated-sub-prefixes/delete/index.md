# gcloud compute public-delegated-prefixes delegated-sub-prefixes delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/delete](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/delete)*

**NAME**

: **gcloud compute public-delegated-prefixes delegated-sub-prefixes delete - deletes a Compute Engine delegated sub prefix**

**SYNOPSIS**

: **`gcloud compute public-delegated-prefixes delegated-sub-prefixes delete` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/delete#NAME)` `[--public-delegated-prefix](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/delete#--public-delegated-prefix)`=`PUBLIC_DELEGATED_PREFIX` [`[--global-public-delegated-prefix](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/delete#--global-public-delegated-prefix)`     | `[--public-delegated-prefix-region](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/delete#--public-delegated-prefix-region)`=`PUBLIC_DELEGATED_PREFIX_REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Deletes a Compute Engine delegated sub prefix.

**EXAMPLES**

: To delete a delegated sub prefix for a global public delegated prefix:

```
gcloud compute public-delegated-prefixes delegated-sub-prefixes delete my-sub-prefix --public-delegated-prefix=my-pdp --global-public-delegated-prefix
```

To delete a delegated sub prefix for a regional public delegated prefix:

```
gcloud compute public-delegated-prefixes delegated-sub-prefixes delete my-sub-prefix --public-delegated-prefix=my-pdp --public-delegated-prefix-region=us-east1
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the delegated sub prefix to delete.

**REQUIRED FLAGS**

: **--public-delegated-prefix**:
Name of the public delegated prefix to delete the delegate sub prefix for.

**OPTIONAL FLAGS**

: **--global-public-delegated-prefix**

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
gcloud alpha compute public-delegated-prefixes delegated-sub-prefixes delete
```

```
gcloud beta compute public-delegated-prefixes delegated-sub-prefixes delete
```