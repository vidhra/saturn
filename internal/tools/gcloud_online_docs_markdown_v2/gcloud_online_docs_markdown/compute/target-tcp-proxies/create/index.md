# gcloud compute target-tcp-proxies create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies/create](https://cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies/create)*

**NAME**

: **gcloud compute target-tcp-proxies create - create a target TCP proxy**

**SYNOPSIS**

: **`gcloud compute target-tcp-proxies create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies/create#NAME)` `[--backend-service](https://cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies/create#--backend-service)`=`BACKEND_SERVICE` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies/create#--description)`=`DESCRIPTION`] [`[--[no-]proxy-bind](https://cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies/create#--[no-]proxy-bind)`] [`[--proxy-header](https://cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies/create#--proxy-header)`=`PROXY_HEADER`; default="NONE"] [`[--backend-service-region](https://cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies/create#--backend-service-region)`=`BACKEND_SERVICE_REGION`     | `[--global-backend-service](https://cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies/create#--global-backend-service)`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies/create#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies/create#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute target-tcp-proxies create` is used to create target
TCP proxies. A target TCP proxy is referenced by one or more forwarding rules
which define which packets the proxy is responsible for routing. The target TCP
proxy points to a backend service which handle the actual requests.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the target TCP proxy to create.

**REQUIRED FLAGS**

: **--backend-service**:
A backend service that will be used for connections to the target TCP proxy.

**OPTIONAL FLAGS**

: **--description**:
An optional, textual description for the target TCP proxy.

**--[no-]proxy-bind**:
This field only applies when the forwarding rule that references this target
proxy has a `--load-balancing-scheme` set to
`INTERNAL_SELF_MANAGED`.
When this field is set to `true`, Envoy proxies set up inbound
traffic interception and bind to the IP address and port specified in the
forwarding rule. This is generally useful when using Traffic Director to
configure Envoy as a gateway or middle proxy (in other words, not a sidecar
proxy). The Envoy proxy listens for inbound requests and handles requests when
it receives them.
Use `--proxy-bind` to enable and `--no-proxy-bind` to
disable.

**--proxy-header**:
The type of proxy protocol header to be sent to the backend.
`PROXY_HEADER` must be one of:

**`NONE`**:
No proxy header is added.

**`PROXY_V1`**:
Enables PROXY protocol (version 1) for passing client connection information.

**--backend-service-region**

**--global**

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
gcloud alpha compute target-tcp-proxies create
```

```
gcloud beta compute target-tcp-proxies create
```