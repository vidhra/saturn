# gcloud compute target-http-proxies update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/update](https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/update)*

**NAME**

: **gcloud compute target-http-proxies update - update a target HTTP proxy**

**SYNOPSIS**

: **`gcloud compute target-http-proxies update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/update#NAME)` `[--url-map](https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/update#--url-map)`=`URL_MAP` [`[--clear-http-keep-alive-timeout-sec](https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/update#--clear-http-keep-alive-timeout-sec)`     | `[--http-keep-alive-timeout-sec](https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/update#--http-keep-alive-timeout-sec)`=`HTTP_KEEP_ALIVE_TIMEOUT_SEC`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/update#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/update#--region)`=`REGION`] [`[--global-url-map](https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/update#--global-url-map)`     | `[--url-map-region](https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/update#--url-map-region)`=`URL_MAP_REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute target-http-proxies update` is used to change the URL
map of existing target HTTP proxies. A target HTTP proxy is referenced by one or
more forwarding rules which specify the network traffic that the proxy is
responsible for routing. The target HTTP proxy points to a URL map that defines
the rules for routing the requests. The URL map's job is to map URLs to backend
services which handle the actual requests.

**EXAMPLES**

: If there is an already-created URL map with the name URL_MAP, update a global
target HTTP proxy pointing to this map by running:

```
gcloud compute target-http-proxies update PROXY_NAME --url-map=URL_MAP
```

Update a regional target HTTP proxy by running:

```
gcloud compute target-http-proxies update PROXY_NAME --url-map=URL_MAP --region=REGION_NAME
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the target HTTP proxy to update.

**REQUIRED FLAGS**

: **--url-map**:
A reference to a URL map resource. A URL map defines the mapping of URLs to
backend services. Before you can refer to a URL map, you must create the URL
map. To delete a URL map that a target proxy is referring to, you must first
delete the target HTTP proxy.

**OPTIONAL FLAGS**

: **--clear-http-keep-alive-timeout-sec**

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
gcloud alpha compute target-http-proxies update
```

```
gcloud beta compute target-http-proxies update
```