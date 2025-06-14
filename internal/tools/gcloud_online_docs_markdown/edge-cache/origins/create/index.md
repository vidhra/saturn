# gcloud edge-cache origins create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/create](https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/create)*

**NAME**

: **gcloud edge-cache origins create - create an EdgeCacheOrigin resource**

**SYNOPSIS**

: **`gcloud edge-cache origins create` (`[ORIGIN](https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/create#ORIGIN)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/create#--location)`=`LOCATION`) `[--origin-address](https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/create#--origin-address)`=`ORIGIN_ADDRESS` [`[--async](https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/create#--description)`=`DESCRIPTION`] [`[--failover-origin](https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/create#--failover-origin)`=`FAILOVER_ORIGIN`] [`[--flex-shielding](https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/create#--flex-shielding)`=`FLEX_SHIELDING`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--max-attempts](https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/create#--max-attempts)`=`MAX_ATTEMPTS`] [`[--port](https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/create#--port)`=`PORT`] [`[--protocol](https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/create#--protocol)`=`PROTOCOL`] [`[--response-timeout](https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/create#--response-timeout)`=`RESPONSE_TIMEOUT`] [`[--retry-conditions](https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/create#--retry-conditions)`=[`RETRY_CONDITIONS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new EdgeCacheOrigin resource.

**EXAMPLES**

: To create a EdgeCacheOrigin resource called 'my-origin', run:

```
gcloud edge-cache origins create my-origin --origin-address="origin.example.com"
```

**POSITIONAL ARGUMENTS**

: **Origin resource - The name of the EdgeCacheOrigin resource to create. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `origin` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ORIGIN`**:
ID of the origin or fully qualified identifier for the origin.
To set the `origin` attribute:

- provide the argument `origin` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location Id.
To set the `location` attribute:

- provide the argument `origin` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- use global location.**

**REQUIRED FLAGS**

: **--origin-address**:
A fully qualified domain name (FQDN) or IP address reachable over the public
Internet, or the address of a Google Cloud Storage bucket.
This address will be used as the origin for cache requests - e.g.

- FQDN: media-backend.example.com
- IPv4: 35.218.1.1
- IPv6: [2607:f8b0:4012:809::200e]
- Cloud Storage: gs://bucketname

When providing an FQDN (hostname), it must be publicly resolvable (e.g. via
Google public DNS) and IP addresses must be publicly routable. If a Cloud
Storage bucket is provided, it must be in the canonical "gs://bucketname"
format. Other forms, such as "storage.googleapis.com", will be rejected.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Human-readable description of the resource.

**--failover-origin**:
Origin resource to try when the current origin cannot be reached. After
maxAttempts is reached, the configured failoverOrigin will be used to fulfil the
request.
For example, the following are both valid URLs to an EdgeCacheOrigin resource:

- /projects/PROJECT/locations/global/edgeCacheOrigins/yourOrigin
- yourOrigin

The value of timeout.maxAttemptsTimeout dictates the timeout across all origins.

**--flex-shielding**:
Whenever possible, content will be fetched from origin and cached in or near the
specified region. Best effort.
Defaults to default global origin shielding. You may specify at most one region.
An empty flag turns off flex shielding.
`FLEX_SHIELDING` must be one of:

******:
Turn off flexible shielding and use the default global origin shielding.

**`africa_south1`**:
Origin fetch from near africa-south1.

**`me_central1`**:
Origin fetch from near me-central1.

**--labels**:
List of KEY=VALUE labels to attach to this resource.

**--max-attempts**:
Maximum number of attempts to cache fill from this origin. Another attempt is
made when a cache fill fails with one of the retry_conditions.
Once max_attempts to this origin have failed the failover_origin will be used,
if one is specified. That failover_origin may specify its own max_attempts,
retry_conditions and failover_origin to control its own cache fill failures.
The total number of allowed attempts to cache fill across this and failover
origins is limited to four. The total time allowed for cache fill attempts
across this and failover origins can be controlled with max_attempts_timeout.
The last valid response from an origin will be returned to the client. If no
origin returns a valid response, an HTTP 503 will be returned to the client.
Defaults to 1. Must be a value greater than 0 and less than 4.

**--port**:
Port to connect to the origin on. Defaults to port 443 for HTTP2 and HTTPS
protocols, and port 80 for HTTP.

**--protocol**:
Protocol to use to connect to the configured origin. Defaults to HTTP2, and it
is strongly recommended that users use HTTP2 for both security &
performance.
When using HTTP2 or HTTPS as the protocol, a valid, publicly-signed, unexpired
TLS (SSL) certificate must be presented by the origin server.
`PROTOCOL` must be one of:

**`http`**:
HTTP without TLS (SSL). This is not recommended, as communication outside of
Google's network will be unencrypted to the public endpoint (origin).

**`http2`**:
HTTP/2 protocol. HTTP/2 refers to "h2", which requires TLS (HTTPS). Requires a
valid (public, unexpired) TLS certificate to be present on the origin.

**`https`**:
HTTP/1.1 with TLS (SSL). Requires a valid (public, unexpired) TLS certificate to
be present on the origin.

**--response-timeout**:
Maximum duration to wait for data to arrive when reading from the HTTP
connection/stream.
Defaults to 5 seconds. The timeout must be a value between 1s and 30s.

**--retry-conditions**:
Specifies one or more retry conditions for the configured origin.
If the failure mode during a connection attempt to the origin matches the
configured retryCondition(s), the origin request will be retried up to
maxAttempts times. The failoverOrigin, if configured, will then be used to
satisfy the request.
The default retryCondition is "connect-failure".
retryConditions apply to this origin, and not subsequent failoverOrigin(s),
which may specify their own retryConditions and maxAttempts.
Valid values are:

- connect-failure: Retry on failures connecting to origins, for example due to
connection timeouts.
- http-5xx: Retry if the origin responds with any 5xx response code, or if the
origin does not respond at all, example: disconnects, reset, read timeout,
connection failure, and refused streams.
- gateway-error: Similar to 5xx, but only applies to response codes 502, 503 or
504.
- retriable-4xx: Retry for retriable 4xx response codes, which include HTTP 409
(Conflict) and HTTP 429 (Too Many Requests)
- not-found: Retry if the origin returns a HTTP 404 (Not Found). This can be
useful when generating video content, and the segment is not available yet.

`RETRY_CONDITIONS` must be one of:
`connect-failure`, `forbidden`,
`gateway-error`, `http-5xx`, `not-found`,
`retriable-4xx`, `retry-conditions-unspecified`.

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

**API REFERENCE**

: This command uses the `networkservices/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/networking](https://cloud.google.com/networking)

**NOTES**

: This variant is also available:

```
gcloud alpha edge-cache origins create
```