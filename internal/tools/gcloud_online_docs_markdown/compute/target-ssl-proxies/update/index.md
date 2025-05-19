# gcloud compute target-ssl-proxies update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/update](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/update)*

**NAME**

: **gcloud compute target-ssl-proxies update - update a target SSL proxy**

**SYNOPSIS**

: **`gcloud compute target-ssl-proxies update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/update#NAME)` [`[--backend-service](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/update#--backend-service)`=`BACKEND_SERVICE`] [`[--proxy-header](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/update#--proxy-header)`=`PROXY_HEADER`] [`[--clear-ssl-policy](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/update#--clear-ssl-policy)`     | `[--ssl-policy](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/update#--ssl-policy)`=`SSL_POLICY` `[--global-ssl-policy](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/update#--global-ssl-policy)`     | `[--ssl-policy-region](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/update#--ssl-policy-region)`=`SSL_POLICY_REGION`] [`[--ssl-certificates](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/update#--ssl-certificates)`=`SSL_CERTIFICATE`,[…]     | `[--clear-ssl-certificates](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/update#--clear-ssl-certificates)`     | `[--certificate-map](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/update#--certificate-map)`=`CERTIFICATE_MAP`     | `[--clear-certificate-map](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/update#--clear-certificate-map)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute target-ssl-proxies update` is used to replace the SSL
certificate, backend service, proxy header or SSL policy of existing target SSL
proxies. A target SSL proxy is referenced by one or more forwarding rules which
define which packets the proxy is responsible for routing. The target SSL proxy
in turn points to a backend service which will handle the requests. The target
SSL proxy also points to at most 15 SSL certificates used for server-side
authentication or one certificate map. The target SSL proxy can be associated
with at most one SSL policy.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the target SSL proxy to update.

**FLAGS**

: **--backend-service**:
A backend service that will be used for connections to the target SSL proxy.

**--proxy-header**:
The type of proxy protocol header to be sent to the backend.
`PROXY_HEADER` must be one of:

**`NONE`**:
No proxy header is added.

**`PROXY_V1`**:
Enables PROXY protocol (version 1) for passing client connection information.

**--clear-ssl-policy**

**--ssl-certificates**

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
gcloud alpha compute target-ssl-proxies update
```

```
gcloud beta compute target-ssl-proxies update
```