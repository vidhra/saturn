# gcloud compute target-tcp-proxies update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies/update](https://cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies/update)*

**NAME**

: **gcloud compute target-tcp-proxies update - update a target TCP proxy**

**SYNOPSIS**

: **`gcloud compute target-tcp-proxies update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies/update#NAME)` [`[--backend-service](https://cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies/update#--backend-service)`=`BACKEND_SERVICE`] [`[--proxy-header](https://cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies/update#--proxy-header)`=`PROXY_HEADER`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute target-tcp-proxies update` is used to change the
backend service or proxy header of existing target TCP proxies. A target TCP
proxy is referenced by one or more forwarding rules which define which packets
the proxy is responsible for routing. The target TCP proxy in turn points to a
backend service which will handle the requests.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the target TCP proxy to update.

**FLAGS**

: **--backend-service**:
A backend service that will be used for connections to the target TCP proxy.

**--proxy-header**:
The type of proxy protocol header to be sent to the backend.
`PROXY_HEADER` must be one of:

**`NONE`**:
No proxy header is added.

**`PROXY_V1`**:
Enables PROXY protocol (version 1) for passing client connection information.

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
gcloud alpha compute target-tcp-proxies update
```

```
gcloud beta compute target-tcp-proxies update
```