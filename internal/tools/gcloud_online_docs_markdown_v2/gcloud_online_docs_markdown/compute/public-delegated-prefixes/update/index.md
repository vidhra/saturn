# gcloud compute public-delegated-prefixes update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/update](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/update)*

**NAME**

: **gcloud compute public-delegated-prefixes update - updates a Compute Engine public delegated prefix**

**SYNOPSIS**

: **`gcloud compute public-delegated-prefixes update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/update#NAME)` (`[--announce-prefix](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/update#--announce-prefix)`     | `[--withdraw-prefix](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/update#--withdraw-prefix)`) [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/update#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/update#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To announce a regional v2 public delegated prefix:

```
gcloud compute public-delegated-prefixes update my-pdp --announce-prefix --region=us-central1
```

To withdraw a regional v2 public delegated prefix:

```
gcloud compute public-delegated-prefixes update my-pdp --withdraw-prefix --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the public delegated prefix to operate on.

**REQUIRED FLAGS**

: **--announce-prefix**

**OPTIONAL FLAGS**

: **--region**:
Region of the public delegated prefix to operate on. Overrides the default
`compute/region` property value for this command invocation.

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
gcloud alpha compute public-delegated-prefixes update
```

```
gcloud beta compute public-delegated-prefixes update
```