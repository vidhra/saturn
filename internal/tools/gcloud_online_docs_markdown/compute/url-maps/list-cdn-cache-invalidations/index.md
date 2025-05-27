# gcloud compute url-maps list-cdn-cache-invalidations  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/list-cdn-cache-invalidations](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/list-cdn-cache-invalidations)*

**NAME**

: **gcloud compute url-maps list-cdn-cache-invalidations - list Cloud CDN cache invalidations for a URL map**

**SYNOPSIS**

: **`gcloud compute url-maps list-cdn-cache-invalidations` `[URL_MAP](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/list-cdn-cache-invalidations#URL_MAP)` [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/list-cdn-cache-invalidations#--global)`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/list-cdn-cache-invalidations#--limit)`=`LIMIT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/list-cdn-cache-invalidations#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List Cloud CDN cache invalidations for a URL map. A cache invalidation instructs
Cloud CDN to stop using cached content. You can list invalidations to check
which have completed.

**POSITIONAL ARGUMENTS**

: **`URL_MAP`**:
Name of the URL map to describe.

**FLAGS**

: **--global**:
(Default) The URL map is global. Regional URL maps are not supported.

**--limit**:
The maximum number of invalidations to list. This has an upper limit of 1000.
For more results, use Cloud Logging.

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
gcloud alpha compute url-maps list-cdn-cache-invalidations
```

```
gcloud beta compute url-maps list-cdn-cache-invalidations
```