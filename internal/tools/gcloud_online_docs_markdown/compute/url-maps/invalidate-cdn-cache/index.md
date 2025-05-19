# gcloud compute url-maps invalidate-cdn-cache  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/invalidate-cdn-cache](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/invalidate-cdn-cache)*

**NAME**

: **gcloud compute url-maps invalidate-cdn-cache - invalidate specified objects for a URL map in Cloud CDN caches**

**SYNOPSIS**

: **`gcloud compute url-maps invalidate-cdn-cache` `[URLMAP](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/invalidate-cdn-cache#URLMAP)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/invalidate-cdn-cache#--async)`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/invalidate-cdn-cache#--global)`] [`[--host](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/invalidate-cdn-cache#--host)`=`HOST`] [`[--path](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/invalidate-cdn-cache#--path)`=`PATH`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/invalidate-cdn-cache#--tags)`=`TAGS`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps/invalidate-cdn-cache#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute url-maps invalidate-cdn-cache` requests that Cloud
CDN stop using cached content for resources at a particular URL path or set of
URL paths.
`gcloud compute url-maps invalidate-cdn-cache` may succeed even if no
content is cached for some or all URLs with the given path.

**POSITIONAL ARGUMENTS**

: **`URLMAP`**:
Name of the URL map to operate on.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--global**:
(Default) The URL map is global. Regional URL maps are not supported.

**--host**:
If set, this invalidation will apply only to requests to the specified host.

**--path**:
A path specifying which objects to invalidate. PATH must start with
``/´´ and the only place a ``*´´ is allowed is at the
end following a ``/´´. It will be matched against URL paths, which
do not include scheme, host, or any text after the first ``?´´ or
``#´´ (and those characters are not allowed here). For example, for
the URL
``https://example.com/whatever/x.html?a=b``,
the path is ``/whatever/x.html``.
If PATH ends with ``*´´, the preceding string is a prefix, and all
URLs whose paths begin with it will be invalidated. If PATH doesn't end with
``*´´, then only URLs with exactly that path will be invalidated.
Examples:

- ``´´, ``*´´, anything that doesn't start with
``/´´: error
- ``/´´: just the root URL
- ``/*´´: everything
- ``/x/y´´: ``/x/y´´ only (and not ``/x/y/´´)
- ``/x/y/´´: ``/x/y/´´ only (and not ``/x/y´´)
- ``/x/y/*´´: ``/x/y/´´ and everything under it

**--tags**:
A single tag or a comma-delimited list of tags. When multiple tags are
specified, the invalidation applies them using boolean OR logic.
Example:

- ``--tags=abcd,user123``

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
gcloud alpha compute url-maps invalidate-cdn-cache
```

```
gcloud beta compute url-maps invalidate-cdn-cache
```