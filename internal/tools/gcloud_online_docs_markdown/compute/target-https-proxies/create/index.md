# gcloud compute target-https-proxies create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create)*

**NAME**

: **gcloud compute target-https-proxies create - create a target HTTPS proxy**

**SYNOPSIS**

: **`gcloud compute target-https-proxies create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create#NAME)` `[--url-map](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create#--url-map)`=`URL_MAP` [`[--certificate-map](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create#--certificate-map)`=`CERTIFICATE_MAP`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create#--description)`=`DESCRIPTION`] [`[--http-keep-alive-timeout-sec](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create#--http-keep-alive-timeout-sec)`=`HTTP_KEEP_ALIVE_TIMEOUT_SEC`] [`[--quic-override](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create#--quic-override)`=`QUIC_OVERRIDE`; default="NONE"] [`[--server-tls-policy](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create#--server-tls-policy)`=`SERVER_TLS_POLICY`] [`[--ssl-policy](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create#--ssl-policy)`=`SSL_POLICY`] [`[--tls-early-data](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create#--tls-early-data)`=`TLS_EARLY_DATA`] [`[--certificate-manager-certificates](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create#--certificate-manager-certificates)`=[`CERTIFICATE_MANAGER_CERTIFICATES`,…]     | `[--ssl-certificates](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create#--ssl-certificates)`=`SSL_CERTIFICATE`,[…]] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create#--region)`=`REGION`] [`[--global-ssl-certificates](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create#--global-ssl-certificates)`     | `[--ssl-certificates-region](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create#--ssl-certificates-region)`=`SSL_CERTIFICATES_REGION`] [`[--global-ssl-policy](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create#--global-ssl-policy)`     | `[--ssl-policy-region](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create#--ssl-policy-region)`=`SSL_POLICY_REGION`] [`[--global-url-map](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create#--global-url-map)`     | `[--url-map-region](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create#--url-map-region)`=`URL_MAP_REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute target-https-proxies create` is used to create target
HTTPS proxies. A target HTTPS proxy is referenced by one or more forwarding
rules which specify the network traffic that the proxy is responsible for
routing. The target HTTPS proxy points to a URL map that defines the rules for
routing the requests. The URL map's job is to map URLs to backend services which
handle the actual requests. The target HTTPS proxy also points to at most 15 SSL
certificates used for server-side authentication. The target HTTPS proxy can be
associated with at most one SSL policy.

**EXAMPLES**

: If there is an already-created URL map with the name URL_MAP and a SSL
certificate named SSL_CERTIFICATE, create a global target HTTPS proxy pointing
to this map by running:

```
gcloud compute target-https-proxies create PROXY_NAME --url-map=URL_MAP --ssl-certificates=SSL_CERTIFICATE
```

Create a regional target HTTPS proxy by running:

```
gcloud compute target-https-proxies create PROXY_NAME --url-map=URL_MAP --ssl-certificates=SSL_CERTIFICATE --region=REGION_NAME
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the target HTTPS proxy to create.

**REQUIRED FLAGS**

: **--url-map**:
A reference to a URL map resource. A URL map defines the mapping of URLs to
backend services. Before you can refer to a URL map, you must create the URL
map. To delete a URL map that a target proxy is referring to, you must first
delete the target HTTPS proxy.

**OPTIONAL FLAGS**

: **Certificate map resource - The certificate map to attach. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `--certificate-map` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--certificate-map` on the command line with a
fully specified name;
- default value of location is [global].

**--certificate-map**:
ID of the certificate map or fully qualified identifier for the certificate map.
To set the `map` attribute:

- provide the argument `--certificate-map` on the command line.**

**--description**:
An optional, textual description for the target HTTPS proxy.

**--http-keep-alive-timeout-sec**:
Represents the maximum amount of time that a TCP connection can be idle between
the (downstream) client and the target HTTP proxy. If an HTTP keepalive timeout
is not specified, the default value is 610 seconds. For global external
Application Load Balancers, the minimum allowed value is 5 seconds and the
maximum allowed value is 1200 seconds.

**--quic-override**:
Controls whether load balancer may negotiate QUIC with clients. QUIC is a new
transport which reduces latency compared to that of TCP. See [https://www.chromium.org/quic](https://www.chromium.org/quic) for more
details. `QUIC_OVERRIDE` must be one of:

**`DISABLE`**:
Disallows load balancer to negotiate QUIC with clients.

**`ENABLE`**:
Allows load balancer to negotiate QUIC with clients.

**`NONE`**:
Allows Google to control when QUIC is rolled out.

**Server tls policy resource - The server TLS policy to attach. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `--server-tls-policy` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--server-tls-policy` on the command line with a
fully specified name;
- provide the argument `--region` on the command line;
- default value of location is [global].

**--server-tls-policy**:
ID of the server_tls_policy or fully qualified identifier for the
server_tls_policy.
To set the `server_tls_policy` attribute:

- provide the argument `--server-tls-policy` on the command line.**

**--ssl-policy**:
A reference to an SSL policy resource that defines the server-side support for
SSL features and affects the connections between clients and load balancers that
are using the HTTPS proxy. The SSL policy must exist and cannot be deleted while
referenced by a target HTTPS proxy.

**--tls-early-data**:
TLS 1.3 Early Data ("0-RTT" or "zero round trip") allows clients to include HTTP
request data alongside a TLS handshake. This can improve application
performance, especially on networks where connection interruptions may be
common, such as on mobile. This applies to both HTTP over TCP (ie: HTTP/1.1 and
HTTP/2) and HTTP/3 over QUIC. `TLS_EARLY_DATA` must be one
of:

**`DISABLED`**:
TLS 1.3 Early Data is not advertised, and any (invalid) attempts to send Early
Data will be rejected.

**`PERMISSIVE`**:
Enables TLS 1.3 Early Data for requests with safe HTTP methods (GET, HEAD,
OPTIONS, TRACE). This mode does not enforce any other limitations for requests
with Early Data. The application owner should validate that Early Data is
acceptable for a given request path.

**`STRICT`**:
Enables TLS 1.3 Early Data for requests with safe HTTP methods, and HTTP
requests that do not have query parameters. Requests that send Early Data
containing non-idempotent HTTP methods or with query parameters will be rejected
with a HTTP 425.

**At most one of these can be specified:

**Certificate resource - certificate-manager-certificates to attach. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--certificate-manager-certificates` on the
command line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--certificate-manager-certificates` on the
command line with a fully specified name;
- default value of location is [global].

**--certificate-manager-certificates**:
IDs of the certificates or fully qualified identifiers for the certificates.
To set the `certificate` attribute:

- provide the argument `--certificate-manager-certificates` on the
command line.**

**--ssl-certificates**:
References to at most 15 SSL certificate resources that are used for server-side
authentication. The first SSL certificate in this list is considered the primary
SSL certificate associated with the load balancer. The SSL certificates must
exist and cannot be deleted while referenced by a target HTTPS proxy.**

**--global**

**--global-ssl-certificates**

**--global-ssl-policy**

**--global-url-map**

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
gcloud alpha compute target-https-proxies create
```

```
gcloud beta compute target-https-proxies create
```