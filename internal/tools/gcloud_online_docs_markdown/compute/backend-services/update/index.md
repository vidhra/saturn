# gcloud compute backend-services update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update)*

**NAME**

: **gcloud compute backend-services update - update a backend service**

**SYNOPSIS**

: **`gcloud compute backend-services update` `[BACKEND_SERVICE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#BACKEND_SERVICE_NAME)` [`[--affinity-cookie-name](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--affinity-cookie-name)`=`AFFINITY_COOKIE_NAME`] [`[--affinity-cookie-path](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--affinity-cookie-path)`=`AFFINITY_COOKIE_PATH`] [`[--affinity-cookie-ttl](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--affinity-cookie-ttl)`=`AFFINITY_COOKIE_TTL`] [`[--cache-key-include-host](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--cache-key-include-host)`] [`[--cache-key-include-http-header](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--cache-key-include-http-header)`=[`HEADER_FIELD_NAME`,…]] [`[--cache-key-include-named-cookie](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--cache-key-include-named-cookie)`=[`NAMED_COOKIE`,…]] [`[--cache-key-include-protocol](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--cache-key-include-protocol)`] [`[--cache-key-include-query-string](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--cache-key-include-query-string)`] [`[--cache-mode](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--cache-mode)`=`CACHE_MODE`] [`[--compression-mode](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--compression-mode)`=`COMPRESSION_MODE`] [`[--connection-drain-on-failover](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--connection-drain-on-failover)`] [`[--connection-draining-timeout](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--connection-draining-timeout)`=`CONNECTION_DRAINING_TIMEOUT`] [`[--connection-persistence-on-unhealthy-backends](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--connection-persistence-on-unhealthy-backends)`=`CONNECTION_PERSISTENCE_ON_UNHEALTHY_BACKENDS`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--description)`=`DESCRIPTION`] [`[--drop-traffic-if-unhealthy](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--drop-traffic-if-unhealthy)`] [`[--edge-security-policy](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--edge-security-policy)`=`EDGE_SECURITY_POLICY`] [`[--[no-]enable-cdn](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--[no-]enable-cdn)`] [`[--[no-]enable-logging](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--[no-]enable-logging)`] [`[--[no-]enable-strong-affinity](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--[no-]enable-strong-affinity)`] [`[--external-managed-migration-testing-percentage](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--external-managed-migration-testing-percentage)`=`EXTERNAL_MANAGED_MIGRATION_TESTING_PERCENTAGE`] [`[--failover-ratio](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--failover-ratio)`=`FAILOVER_RATIO`] [`[--health-checks](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--health-checks)`=`HEALTH_CHECK`,[…]] [`[--no-health-checks](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--health-checks)`] [`[--http-health-checks](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--http-health-checks)`=`HTTP_HEALTH_CHECK`,[…]] [`[--https-health-checks](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--https-health-checks)`=`HTTPS_HEALTH_CHECK`,[…]] [`[--iap](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--iap)`=`disabled`|`enabled`,[`oauth2-client-id`=`OAUTH2-CLIENT-ID`,`oauth2-client-secret`=`OAUTH2-CLIENT-SECRET`]] [`[--idle-timeout-sec](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--idle-timeout-sec)`=`IDLE_TIMEOUT_SEC`] [`[--ip-address-selection-policy](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--ip-address-selection-policy)`=`IP_ADDRESS_SELECTION_POLICY`] [`[--load-balancing-scheme](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--load-balancing-scheme)`=`LOAD_BALANCING_SCHEME`] [`[--locality-lb-policy](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--locality-lb-policy)`=`LOCALITY_LB_POLICY`] [`[--logging-optional](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--logging-optional)`=`LOGGING_OPTIONAL`] [`[--logging-optional-fields](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--logging-optional-fields)`=[`LOGGING_OPTIONAL_FIELDS`,…]] [`[--logging-sample-rate](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--logging-sample-rate)`=`LOGGING_SAMPLE_RATE`] [`[--port-name](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--port-name)`=`PORT_NAME`] [`[--protocol](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--protocol)`=`PROTOCOL`] [`[--[no-]request-coalescing](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--[no-]request-coalescing)`] [`[--security-policy](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--security-policy)`=`SECURITY_POLICY`] [`[--session-affinity](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--session-affinity)`=`SESSION_AFFINITY`] [`[--signed-url-cache-max-age](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--signed-url-cache-max-age)`=`SIGNED_URL_CACHE_MAX_AGE`] [`[--subsetting-policy](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--subsetting-policy)`=`SUBSETTING_POLICY`; default="NONE"] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--timeout)`=`TIMEOUT`] [`[--tracking-mode](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--tracking-mode)`=`TRACKING_MODE`] [`[--bypass-cache-on-request-headers](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--bypass-cache-on-request-headers)`=`BYPASS_CACHE_ON_REQUEST_HEADERS`     | `[--no-bypass-cache-on-request-headers](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--bypass-cache-on-request-headers)`] [`[--cache-key-query-string-blacklist](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--cache-key-query-string-blacklist)`=[`QUERY_STRING`,…]     | `[--cache-key-query-string-whitelist](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--cache-key-query-string-whitelist)`=`QUERY_STRING`,[…]] [`[--clear-custom-metrics](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--clear-custom-metrics)`     | `[--custom-metrics](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--custom-metrics)`=[`CUSTOM_METRICS`,…]     | `[--custom-metrics-file](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--custom-metrics-file)`=[`CUSTOM_METRICS`,…]] [`[--clear-external-managed-migration-state](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--clear-external-managed-migration-state)`     | `[--external-managed-migration-state](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--external-managed-migration-state)`=`EXTERNAL_MANAGED_MIGRATION_STATE`] [`[--client-ttl](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--client-ttl)`=`CLIENT_TTL`     | `[--no-client-ttl](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--client-ttl)`] [`[--custom-request-header](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--custom-request-header)`=`CUSTOM_REQUEST_HEADER`     | `[--no-custom-request-headers](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--custom-request-headers)`] [`[--custom-response-header](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--custom-response-header)`=`CUSTOM_RESPONSE_HEADER`     | `[--no-custom-response-headers](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--custom-response-headers)`] [`[--default-ttl](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--default-ttl)`=`DEFAULT_TTL`     | `[--no-default-ttl](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--default-ttl)`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--region)`=`REGION`] [`[--global-health-checks](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--global-health-checks)`     | `[--health-checks-region](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--health-checks-region)`=`HEALTH_CHECKS_REGION`] [`[--max-ttl](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--max-ttl)`=`MAX_TTL`     | `[--no-max-ttl](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--max-ttl)`] [`[--[no-]negative-caching](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--[no-]negative-caching)`     | `[--no-negative-caching-policies](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--negative-caching-policies)`     | `[--negative-caching-policy](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--negative-caching-policy)`=[[`CODE`=`TTL`],…]] [`[--serve-while-stale](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--serve-while-stale)`=`SERVE_WHILE_STALE`     | `[--no-serve-while-stale](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--serve-while-stale)`] [`[--service-bindings](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--service-bindings)`=`SERVICE_BINDING`,[…]     | `[--no-service-bindings](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--service-bindings)`] [`[--service-lb-policy](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--service-lb-policy)`=`SERVICE_LOAD_BALANCING_POLICY`     | `[--no-service-lb-policy](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--service-lb-policy)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute backend-services update` is used to update backend
services.

**POSITIONAL ARGUMENTS**

: **`BACKEND_SERVICE_NAME`**:
Name of the backend service to update.

**FLAGS**

: **--affinity-cookie-name**:
If `--session-affinity` is set to `HTTP_COOKIE` or
`STRONG_COOKIE_AFFINITY`, this flag sets the name of the cookie.

**--affinity-cookie-path**:
If `--session-affinity` is set to `HTTP_COOKIE` or
`STRONG_COOKIE_AFFINITY`, this flag sets the path of the cookie.

**--affinity-cookie-ttl**:
If `--session-affinity` is set to `GENERATED_COOKIE`,
`HTTP_COOKIE`, or `STRONG_COOKIE_AFFINITY`, this flag sets
the TTL, in seconds, of the resulting cookie. A setting of 0 indicates that the
cookie should be a session cookie. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

**--cache-key-include-host**:
Enable including host in cache key. If enabled, requests to different hosts will
be cached separately. Can only be applied for global resources.

**--cache-key-include-http-header**:
Specifies a comma-separated list of HTTP headers, by field name, to include in
cache keys. Only the request URL is included in the cache key by default.

**--cache-key-include-named-cookie**:
Specifies a comma-separated list of HTTP cookie names to include in cache keys.
The name=value pair are used in the cache key Cloud CDN generates. Cookies are
not included in cache keys by default.

**--cache-key-include-protocol**:
Enable including protocol in cache key. If enabled, http and https requests will
be cached separately. Can only be applied for global resources.

**--cache-key-include-query-string**:
Enable including query string in cache key. If enabled, the query string
parameters will be included according to --cache-key-query-string-whitelist and
--cache-key-query-string-blacklist. If disabled, the entire query string will be
excluded. Use "--cache-key-query-string-blacklist=" (sets the blacklist to the
empty list) to include the entire query string. Can only be applied for global
resources.

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

**--connection-drain-on-failover**:
Applicable only for backend service-based external and internal passthrough
Network Load Balancers as part of a connection tracking policy. Only applicable
when the backend service protocol is TCP. Not applicable to any other load
balancer. Enabled by default, this option instructs the load balancer to allow
established TCP connections to persist for up to 300 seconds on instances or
endpoints in primary backends during failover, and on instances or endpoints in
failover backends during failback. For details, see: [Connection
draining on failover and failback for internal passthrough Network Load
Balancers](https://cloud.google.com/load-balancing/docs/internal/failover-overview#connection_draining) and [Connection
draining on failover and failback for external passthrough Network Load
Balancers](https://cloud.google.com/load-balancing/docs/network/networklb-failover-overview#connection_draining).

**--connection-draining-timeout**:
Connection draining timeout to be used during removal of VMs from instance
groups. This guarantees that for the specified time all existing connections to
a VM will remain untouched, but no new connections will be accepted. Set timeout
to zero to disable connection draining. Enable feature by specifying a timeout
of up to one hour. If the flag is omitted API default value (0s) will be used.
See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)
for information on duration formats.

**--connection-persistence-on-unhealthy-backends**:
Specifies connection persistence when backends are unhealthy. The default value
is DEFAULT_FOR_PROTOCOL.
`CONNECTION_PERSISTENCE_ON_UNHEALTHY_BACKENDS` must be one
of: `DEFAULT_FOR_PROTOCOL`, `NEVER_PERSIST`,
`ALWAYS_PERSIST`.

**--description**:
An optional, textual description for the backend service.

**--drop-traffic-if-unhealthy**:
Applicable only for backend service-based external and internal passthrough
Network Load Balancers as part of a connection tracking policy. Not applicable
to any other load balancer. This option instructs the load balancer to drop
packets when all instances or endpoints in primary and failover backends do not
pass their load balancer health checks. For details, see: [Dropping
traffic when all backend VMs are unhealthy for internal passthrough Network Load
Balancers](https://cloud.google.com/load-balancing/docs/internal/failover-overview#drop_traffic) and [Dropping
traffic when all backend VMs are unhealthy for external passthrough Network Load
Balancers](https://cloud.google.com/load-balancing/docs/network/networklb-failover-overview#drop_traffic).

**--edge-security-policy**:
The edge security policy that will be set for this backend service. To remove
the policy from this backend service set the policy to an empty string.

**--[no-]enable-cdn**:
Enable or disable Cloud CDN for the backend service. Only available for backend
services with --load-balancing-scheme=EXTERNAL that use a --protocol of HTTP,
HTTPS, HTTP2 or H2C. Cloud CDN caches HTTP responses at the edge of Google's
network. Cloud CDN is disabled by default. Use `--enable-cdn` to
enable and `--no-enable-cdn` to disable.

**--[no-]enable-logging**:
The logging options for the load balancer traffic served by this backend
service. If logging is enabled, logs will be exported to Cloud Logging. Disabled
by default. This field cannot be specified for global external proxy Network
Load Balancers. Use `--enable-logging` to enable and
`--no-enable-logging` to disable.

**--[no-]enable-strong-affinity**:
Enable or disable strong session affinity. This is only available for
loadbalancingScheme EXTERNAL. Use `--enable-strong-affinity` to
enable and `--no-enable-strong-affinity` to disable.

**--external-managed-migration-testing-percentage**:
Determines the fraction of requests that should be processed by the Global
external Application Load Balancer.
The value of this field must be in the range [0, 100].

**--failover-ratio**:
Applicable only to backend service-based external passthrough Network load
balancers and internal passthrough Network load balancers as part of a failover
policy. Not applicable to any other load balancer. This option defines the ratio
used to control when failover and failback occur. For details, see: [Failover
ratio for internal passthrough Network Load Balancers](https://cloud.google.com/load-balancing/docs/internal/failover-overview#failover_ratio) and [Failover
ratio for external passthrough Network Load Balancer overview](https://cloud.google.com/load-balancing/docs/network/networklb-failover-overview#failover_ratio).

**--health-checks**:
Specifies a list of health check objects for checking the health of the backend
service. Currently at most one health check can be specified. Health checks need
not be for the same protocol as that of the backend service.

**--no-health-checks**:
Removes all health checks for the backend service if the backend service has no
backends attached.

**--http-health-checks**:
Specifies a list of legacy HTTP health check objects for checking the health of
the backend service.
Legacy health checks are not recommended for backend services. It is possible to
use a legacy health check on a backend service for an Application Load Balancer
if that backend service uses instance groups. For more information, refer to
this guide: [https://cloud.google.com/load-balancing/docs/health-check-concepts#lb_guide](https://cloud.google.com/load-balancing/docs/health-check-concepts#lb_guide).

**--https-health-checks**:
Specifies a list of legacy HTTPS health check objects for checking the health of
the backend service.
Legacy health checks are not recommended for backend services. It is possible to
use a legacy health check on a backend service for an Application Load Balancer
if that backend service uses instance groups. For more information, refer to
this guide: [https://cloud.google.com/load-balancing/docs/health-check-concepts#lb_guide](https://cloud.google.com/load-balancing/docs/health-check-concepts#lb_guide).

**--iap**:
Change the Identity Aware Proxy (IAP) service configuration for the backend
service. You can set IAP to 'enabled' or 'disabled', or modify the OAuth2 client
configuration (oauth2-client-id and oauth2-client-secret) used by IAP. If any
fields are unspecified, their values will not be modified. For instance, if IAP
is enabled, '--iap=disabled' will disable IAP, and a subsequent '--iap=enabled'
will then enable it with the same OAuth2 client configuration as the first time
it was enabled. See [https://cloud.google.com/iap/](https://cloud.google.com/iap/) for more
information about this feature.

**--idle-timeout-sec**:
Specifies how long to keep a connection tracking table entry while there is no
matching traffic (in seconds). Applicable only for backend service-based
external and internal passthrough Network Load Balancers as part of a connection
tracking policy.

**--ip-address-selection-policy**:
Specifies a preference for traffic sent from the proxy to the backend (or from
the client to the backend for proxyless gRPC).
Can only be set if load balancing scheme is INTERNAL_SELF_MANAGED,
INTERNAL_MANAGED or EXTERNAL_MANAGED.
The possible values are:

```
IPV4_ONLY
  Only send IPv4 traffic to the backends of the backend service,
  regardless of traffic from the client to the proxy. Only IPv4
  health checks are used to check the health of the backends.
```

```
PREFER_IPV6
  Prioritize the connection to the endpoint's IPv6 address over its IPv4
  address (provided there is a healthy IPv6 address).
```

```
IPV6_ONLY
  Only send IPv6 traffic to the backends of the backend service,
  regardless of traffic from the client to the proxy. Only IPv6
  health checks are used to check the health of the backends.
```

`IP_ADDRESS_SELECTION_POLICY` must be one of:
`IPV4_ONLY`, `PREFER_IPV6`, `IPV6_ONLY`.

**--load-balancing-scheme**:
Only for the Global external Application Load Balancer migration.
The value of this field must be EXTERNAL or EXTERNAL_MANAGED.
`LOAD_BALANCING_SCHEME` must be one of:
`EXTERNAL`, `EXTERNAL_MANAGED`.

**--locality-lb-policy**:
The load balancing algorithm used within the scope of the locality.
`LOCALITY_LB_POLICY` must be one of:
`INVALID_LB_POLICY`, `ROUND_ROBIN`,
`LEAST_REQUEST`, `RING_HASH`, `RANDOM`,
`ORIGINAL_DESTINATION`, `MAGLEV`,
`WEIGHTED_MAGLEV`, `WEIGHTED_ROUND_ROBIN`.

**--logging-optional**:
This field can only be specified if logging is enabled for the backend service.
Configures whether all, none, or a subset of optional fields should be added to
the reported logs. Default is EXCLUDE_ALL_OPTIONAL. This field can only be
specified for internal and external passthrough Network Load Balancers.
`LOGGING_OPTIONAL` must be one of:
`EXCLUDE_ALL_OPTIONAL`, `INCLUDE_ALL_OPTIONAL`,
`CUSTOM`.

**--logging-optional-fields**:
This field can only be specified if logging is enabled for the backend service
and "--logging-optional" was set to CUSTOM. Contains a comma-separated list of
optional fields you want to include in the logs. For example: serverInstance,
serverGkeDetails.cluster, serverGkeDetails.pod.podNamespace. This can only be
specified for internal and external passthrough Network Load Balancers.

**--logging-sample-rate**:
This field can only be specified if logging is enabled for the backend service.
The value of the field must be a float in the range [0, 1]. This configures the
sampling rate of requests to the load balancer where 1.0 means all logged
requests are reported and 0.0 means no logged requests are reported. The default
value is 1.0 when logging is enabled and 0.0 otherwise.

**--port-name**:
Backend services for Application Load Balancers and proxy Network Load Balancers
must reference exactly one named port if using instance group backends.
Each instance group backend exports one or more named ports, which map a
user-configurable name to a port number. The backend service's named port
subscribes to one named port on each instance group. The resolved port number
can differ among instance group backends, based on each instance group's named
port list.
When omitted, a backend service subscribes to a named port called http.
The named port for a backend service is either ignored or cannot be set for
these load balancing configurations:

- For any load balancer, if the backends are not instance groups (for example,
GCE_VM_IP_PORT NEGs).
- For any type of backend on a backend service for internal or external
passthrough Network Load Balancers.

See also [https://cloud.google.com/load-balancing/docs/backend-service#named_ports](https://cloud.google.com/load-balancing/docs/backend-service#named_ports).

**--protocol**:
Protocol for incoming requests.
If the `load-balancing-scheme` is `INTERNAL` (Internal
passthrough Network Load Balancer), the protocol must be one of: TCP, UDP,
UNSPECIFIED.
If the `load-balancing-scheme` is `INTERNAL_SELF_MANAGED`
(Traffic Director), the protocol must be one of: HTTP, HTTPS, HTTP2, GRPC, H2C.
If the `load-balancing-scheme` is `INTERNAL_MANAGED`
(Internal Application Load Balancer), the protocol must be one of: HTTP, HTTPS,
HTTP2, H2C.
If the `load-balancing-scheme` is `INTERNAL_MANAGED`
(Internal proxy Network Load Balancer), the protocol must be only TCP.
If the `load-balancing-scheme` is `EXTERNAL` and
`region` is not set (Classic Application Load Balancer and Classic
proxy Network Load Balancer), the protocol must be one of: HTTP, HTTPS, HTTP2,
TCP, SSL.
If the `load-balancing-scheme` is `EXTERNAL` and
`region` is set (External passthrough Network Load Balancer), the
protocol must be one of: TCP, UDP, UNSPECIFIED.
If the `load-balancing-scheme` is `EXTERNAL_MANAGED`
(Global external Application Load Balancer and regional external Application
Load Balancer), the protocol must be one of: HTTP, HTTPS, HTTP2, H2C.
If the `load-balancing-scheme` is `EXTERNAL_MANAGED`
(Global external proxy Network Load Balancer), the protocol must be one of: TCP,
SSL.
If the `load-balancing-scheme` is `EXTERNAL_MANAGED`
(Regional external proxy Network Load Balancer), the protocol must be only TCP.

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

**--security-policy**:
The security policy that will be set for this backend service.

**--session-affinity**:
The type of session affinity to use. Supports both TCP and UDP.
`SESSION_AFFINITY` must be one of:

**`CLIENT_IP`**:
Route requests to instances based on the hash of the client's IP address.

**`CLIENT_IP_NO_DESTINATION`**:
Directs a particular client's request to the same backend VM based on a hash
created on the client's IP address only. This is used in L4 ILB as Next-Hop
scenarios. It differs from the Client-IP option in that Client-IP uses a hash
based on both client-IP's address and destination address.

**`CLIENT_IP_PORT_PROTO`**:
(Applicable if `--load-balancing-scheme` is `INTERNAL`)
Connections from the same client IP with the same IP protocol and port will go
to the same backend VM while that VM remains healthy.

**`CLIENT_IP_PROTO`**:
(Applicable if `--load-balancing-scheme` is `INTERNAL`)
Connections from the same client IP with the same IP protocol will go to the
same backend VM while that VM remains healthy.

**`GENERATED_COOKIE`**:
(Applicable if `--load-balancing-scheme` is
`INTERNAL_MANAGED`, `INTERNAL_SELF_MANAGED`,
`EXTERNAL_MANAGED`, or `EXTERNAL`) If the
`--load-balancing-scheme` is `EXTERNAL` or
`EXTERNAL_MANAGED`, routes requests to backend VMs or endpoints in a
NEG, based on the contents of the `GCLB` cookie set by the load
balancer. Only applicable when `--protocol` is HTTP, HTTPS,HTTP2 or
H2C. If the `--load-balancing-scheme` is
`INTERNAL_MANAGED` or `INTERNAL_SELF_MANAGED`, routes
requests to backend VMs or endpoints in a NEG, based on the contents of the
`GCILB` cookie set by the proxy. (If no cookie is present, the proxy
chooses a backend VM or endpoint and sends a `Set-Cookie` response
for future requests.) If the `--load-balancing-scheme` is
`INTERNAL_SELF_MANAGED`, routes requests to backend VMs or endpoints
in a NEG, based on the contents of a cookie set by Traffic Director. This
session affinity is only valid if the load balancing locality policy is either
`RING_HASH` or `MAGLEV`.

**`HEADER_FIELD`**:
(Applicable if `--load-balancing-scheme` is
`INTERNAL_MANAGED`, `EXTERNAL_MANAGED`, or
`INTERNAL_SELF_MANAGED`) Route requests to backend VMs or endpoints
in a NEG based on the value of the HTTP header named in the
`--custom-request-header` flag. This session affinity is only valid
if the load balancing locality policy is either `RING_HASH` or
`MAGLEV` and the backend service's consistent hash specifies the name
of the HTTP header.

**`HTTP_COOKIE`**:
(Applicable if `--load-balancing-scheme` is
`INTERNAL_MANAGED`, `EXTERNAL_MANAGED` or
`INTERNAL_SELF_MANAGED`) Route requests to backend VMs or endpoints
in a NEG, based on an HTTP cookie in the `--affinity-cookie-name`
flag (with the optional `--affinity-cookie-ttl` flag). If the client
has not provided the cookie, the proxy generates the cookie and returns it to
the client in a `Set-Cookie` header. This session affinity is only
valid if the load balancing locality policy is either `RING_HASH` or
`MAGLEV` and the backend service's consistent hash specifies the HTTP
cookie.

**`NONE`**:
Session affinity is disabled.

**`STRONG_COOKIE_AFFINITY`**:
(Applicable if `--load-balancing-scheme` is
`INTERNAL_MANAGED` or `EXTERNAL_MANAGED`) Strong
cookie-based affinity, based on an HTTP cookie named in the
`--affinity-cookie-name` flag (with the optional
`--affinity-cookie-ttl` flag). Connections bearing the same cookie
will be served by the same backend VM while that VM remains healthy, as long as
the cookie has not expired. If the `--affinity-cookie-ttl` flag is
set to 0, the cookie will be treated as a session cookie.

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

**--subsetting-policy**:
Specifies the algorithm used for subsetting. Default value is NONE which implies
that subsetting is disabled. For Layer 4 Internal Load Balancing, if subsetting
is enabled, only the algorithm CONSISTENT_HASH_SUBSETTING can be specified.
`SUBSETTING_POLICY` must be one of: `NONE`,
`CONSISTENT_HASH_SUBSETTING`.

**--timeout**:
Applicable to all load balancing products except passthrough Network Load
Balancers. For internal passthrough Network Load Balancers
(``load-balancing-scheme`` set to INTERNAL) and
external passthrough Network Load Balancers
(``global`` not set and
``load-balancing-scheme`` set to EXTERNAL),
``timeout`` is ignored.
If the ``protocol`` is HTTP, HTTPS, HTTP2 or
H2C, ``timeout`` is a request/response timeout
for HTTP(S) traffic, meaning the amount of time that the load balancer waits for
a backend to return a full response to a request. If WebSockets traffic is
supported, the ``timeout`` parameter sets the
maximum amount of time that a WebSocket can be open (idle or not).
For example, for HTTP, HTTPS, HTTP2 or H2C traffic, specifying a
``timeout`` of 10s means that backends have 10
seconds to respond to the load balancer's requests. The load balancer retries
the HTTP GET request one time if the backend closes the connection or times out
before sending response headers to the load balancer. If the backend sends
response headers or if the request sent to the backend is not an HTTP GET
request, the load balancer does not retry. If the backend does not reply at all,
the load balancer returns a 502 Bad Gateway error to the client.
If the ``protocol`` is SSL or TCP,
``timeout`` is an idle timeout.
The full range of timeout values allowed is 1 - 2,147,483,647 seconds.

**--tracking-mode**:
Specifies the connection key used for connection tracking. The default value is
PER_CONNECTION. Applicable only for backend service-based external and internal
passthrough Network Load Balancers as part of a connection tracking policy. For
details, see: [Connection
tracking mode for internal passthrough Network Load Balancers balancing](https://cloud.google.com/load-balancing/docs/internal#tracking-mode) and
[Connection
tracking mode for external passthrough Network Load Balancers](https://cloud.google.com/load-balancing/docs/network/networklb-backend-service#tracking-mode).
`TRACKING_MODE` must be one of:
`PER_CONNECTION`, `PER_SESSION`.

**--bypass-cache-on-request-headers**

**--cache-key-query-string-blacklist**

**--clear-custom-metrics**

**--clear-external-managed-migration-state**

**--client-ttl**

**--custom-request-header**

**--custom-response-header**

**--default-ttl**

**--global**

**--global-health-checks**

**--max-ttl**

**--[no-]negative-caching**

**--serve-while-stale**

**--service-bindings**

**--service-lb-policy**

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
gcloud alpha compute backend-services update
```

```
gcloud beta compute backend-services update
```