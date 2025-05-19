# gcloud compute backend-buckets update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update)*

**NAME**

: **gcloud compute backend-buckets update - update a backend bucket**

**SYNOPSIS**

: **`gcloud compute backend-buckets update` `[BACKEND_BUCKET_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#BACKEND_BUCKET_NAME)` [`[--cache-key-include-http-header](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--cache-key-include-http-header)`=[`HEADER_FIELD_NAME`,…]] [`[--cache-key-query-string-whitelist](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--cache-key-query-string-whitelist)`=[`QUERY_STRING`,…]] [`[--cache-mode](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--cache-mode)`=`CACHE_MODE`] [`[--compression-mode](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--compression-mode)`=`COMPRESSION_MODE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--description)`=`DESCRIPTION`] [`[--edge-security-policy](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--edge-security-policy)`=`EDGE_SECURITY_POLICY`] [`[--[no-]enable-cdn](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--[no-]enable-cdn)`] [`[--gcs-bucket-name](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--gcs-bucket-name)`=`GCS_BUCKET_NAME`] [`[--[no-]request-coalescing](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--[no-]request-coalescing)`] [`[--signed-url-cache-max-age](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--signed-url-cache-max-age)`=`SIGNED_URL_CACHE_MAX_AGE`] [`[--bypass-cache-on-request-headers](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--bypass-cache-on-request-headers)`=`BYPASS_CACHE_ON_REQUEST_HEADERS`     | `[--no-bypass-cache-on-request-headers](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--bypass-cache-on-request-headers)`] [`[--client-ttl](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--client-ttl)`=`CLIENT_TTL`     | `[--no-client-ttl](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--client-ttl)`] [`[--custom-response-header](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--custom-response-header)`=`CUSTOM_RESPONSE_HEADER`     | `[--no-custom-response-headers](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--custom-response-headers)`] [`[--default-ttl](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--default-ttl)`=`DEFAULT_TTL`     | `[--no-default-ttl](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--default-ttl)`] [`[--max-ttl](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--max-ttl)`=`MAX_TTL`     | `[--no-max-ttl](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--max-ttl)`] [`[--[no-]negative-caching](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--[no-]negative-caching)`     | `[--no-negative-caching-policies](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--negative-caching-policies)`     | `[--negative-caching-policy](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--negative-caching-policy)`=[[`CODE`=`TTL`],…]] [`[--serve-while-stale](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--serve-while-stale)`=`SERVE_WHILE_STALE`     | `[--no-serve-while-stale](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#--serve-while-stale)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute backend-buckets update` is used to update backend
buckets.

**POSITIONAL ARGUMENTS**

: **`BACKEND_BUCKET_NAME`**:
Name of the backend bucket to update.

**FLAGS**

: **--cache-key-include-http-header**:
Specifies a comma-separated list of HTTP headers, by field name, to include in
cache keys. Only the request URL is included in the cache key by default.

**--cache-key-query-string-whitelist**:
Specifies a comma-separated list of query string parameters to include in cache
keys. Default parameters are always included. '&' and '=' are percent
encoded and not treated as delimiters.

**--cache-mode**:
Specifies the cache setting for all responses from this backend.
`CACHE_MODE` must be one of:

**`CACHE_ALL_STATIC`**:
Automatically cache static content, including common image formats, media (video
and audio), web assets (JavaScript and CSS). Requests and responses that are
marked as uncacheable, as well as dynamic content (including HTML), aren't
cached.

**`FORCE_CACHE_ALL`**:
Cache all content, ignoring any "private", "no-store" or "no-cache" directives
in Cache-Control response headers. Warning: this may result in Cloud CDN caching
private, per-user (user identifiable) content. You should only enable this on
backends that are not serving private or dynamic content, such as storage
buckets.

**`USE_ORIGIN_HEADERS`**:
Require the origin to set valid caching headers to cache content. Responses
without these headers aren't cached at Google's edge, and require a full trip to
the origin on every request, potentially impacting performance and increasing
load on the origin server.

**--compression-mode**:
Compress text responses using Brotli or gzip compression, based on the client's
Accept-Encoding header. Two modes are supported: AUTOMATIC (recommended) -
automatically uses the best compression based on the Accept-Encoding header sent
by the client. In most cases, this will result in Brotli compression being
favored. DISABLED - disables compression. Existing compressed responses cached
by Cloud CDN will not be served to clients.
`COMPRESSION_MODE` must be one of: `DISABLED`,
`AUTOMATIC`.

**--description**:
An optional, textual description for the backend bucket.

**--edge-security-policy**:
The edge security policy that will be set for this backend bucket. To remove the
policy from this backend bucket set the policy to an empty string.

**--[no-]enable-cdn**:
Enable Cloud CDN for the backend bucket. Cloud CDN can cache HTTP responses from
a backend bucket at the edge of the network, close to users. Use
`--enable-cdn` to enable and `--no-enable-cdn` to disable.

**--gcs-bucket-name**:
The name of the Google Cloud Storage bucket to serve from. The storage bucket
must be in the same project.

**--[no-]request-coalescing**:
Enables request coalescing to the backend (recommended).
Request coalescing (or collapsing) combines multiple concurrent cache fill
requests into a small number of requests to the origin. This can improve
performance by putting less load on the origin and backend infrastructure.
However, coalescing adds a small amount of latency when multiple requests to the
same URL are processed, so for latency-critical applications it may not be
desirable.
Defaults to true.
Use `--request-coalescing` to enable and
`--no-request-coalescing` to disable.

**--signed-url-cache-max-age**:
The amount of time up to which the response to a signed URL request will be
cached in the CDN. After this time period, the Signed URL will be revalidated
before being served. Cloud CDN will internally act as though all responses from
this backend had a `Cache-Control: public, max-age=[TTL]` header,
regardless of any existing Cache-Control header. The actual headers served in
responses will not be altered.
For example, specifying `12h` will cause the responses to signed URL
requests to be cached in the CDN up to 12 hours. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.
This flag only affects signed URL requests.

**--bypass-cache-on-request-headers**

**--client-ttl**

**--custom-response-header**

**--default-ttl**

**--max-ttl**

**--[no-]negative-caching**

**--serve-while-stale**

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
gcloud alpha compute backend-buckets update
```

```
gcloud beta compute backend-buckets update
```