# gcloud compute target-http-proxies create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/create](https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/create)*

**NAME**

: **gcloud compute target-http-proxies create - create a target HTTP proxy**

**SYNOPSIS**

: **`gcloud compute target-http-proxies create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/create#NAME)` `[--url-map](https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/create#--url-map)`=`URL_MAP` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/create#--description)`=`DESCRIPTION`] [`[--http-keep-alive-timeout-sec](https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/create#--http-keep-alive-timeout-sec)`=`HTTP_KEEP_ALIVE_TIMEOUT_SEC`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/create#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/create#--region)`=`REGION`] [`[--global-url-map](https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/create#--global-url-map)`     | `[--url-map-region](https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/create#--url-map-region)`=`URL_MAP_REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute target-http-proxies create` is used to create target
HTTP proxies. A target HTTP proxy is referenced by one or more forwarding rules
which specify the network traffic that the proxy is responsible for routing. The
target HTTP proxy points to a URL map that defines the rules for routing the
requests. The URL map's job is to map URLs to backend services which handle the
actual requests.

**EXAMPLES**

: If there is an already-created URL map with the name URL_MAP, create a global
target HTTP proxy pointing to this map by running:

```
gcloud compute target-http-proxies create PROXY_NAME --url-map=URL_MAP
```

Create a regional target HTTP proxy by running:

```
gcloud compute target-http-proxies create PROXY_NAME --url-map=URL_MAP --region=REGION_NAME
```

To create a proxy with a textual description, run:

```
gcloud compute target-http-proxies create PROXY_NAME --url-map=URL_MAP --description="default proxy"
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the target HTTP proxy to create.

**REQUIRED FLAGS**

: **--url-map**:
A reference to a URL map resource. A URL map defines the mapping of URLs to
backend services. Before you can refer to a URL map, you must create the URL
map. To delete a URL map that a target proxy is referring to, you must first
delete the target HTTP proxy.

**OPTIONAL FLAGS**

: **--description**:
An optional, textual description for the target HTTP proxy.

**--http-keep-alive-timeout-sec**:
Represents the maximum amount of time that a TCP connection can be idle between
the (downstream) client and the target HTTP proxy. If an HTTP keepalive timeout
is not specified, the default value is 610 seconds. For global external
Application Load Balancers, the minimum allowed value is 5 seconds and the
maximum allowed value is 1200 seconds.

**--global**

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
gcloud alpha compute target-http-proxies create
```

```
gcloud beta compute target-http-proxies create
```