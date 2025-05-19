# gcloud compute target-grpc-proxies create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/target-grpc-proxies/create](https://cloud.google.com/sdk/gcloud/reference/compute/target-grpc-proxies/create)*

**NAME**

: **gcloud compute target-grpc-proxies create - create a target gRPC proxy**

**SYNOPSIS**

: **`gcloud compute target-grpc-proxies create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/target-grpc-proxies/create#NAME)` `[--url-map](https://cloud.google.com/sdk/gcloud/reference/compute/target-grpc-proxies/create#--url-map)`=`URL_MAP` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/target-grpc-proxies/create#--description)`=`DESCRIPTION`] [`[--validate-for-proxyless](https://cloud.google.com/sdk/gcloud/reference/compute/target-grpc-proxies/create#--validate-for-proxyless)`] [`[--global-url-map](https://cloud.google.com/sdk/gcloud/reference/compute/target-grpc-proxies/create#--global-url-map)`     | `[--url-map-region](https://cloud.google.com/sdk/gcloud/reference/compute/target-grpc-proxies/create#--url-map-region)`=`URL_MAP_REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/target-grpc-proxies/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute target-grpc-proxies create` is used to create target
gRPC proxies. A target gRPC proxy is a component of load balancers intended for
load balancing gRPC traffic. Global forwarding rules reference a target gRPC
proxy. The Target gRPC proxy references a URL map which specifies how traffic
routes to gRPC backend services.

**EXAMPLES**

: If there is an already-created URL map with the name URL_MAP, create a global
target gRPC proxy pointing to this map by running:

```
gcloud compute target-grpc-proxies create PROXY_NAME --url-map=URL_MAP
```

To create a proxy with a textual description, run:

```
gcloud compute target-grpc-proxies create PROXY_NAME --url-map=URL_MAP --description="default proxy"
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the target gRPC proxy to create.

**REQUIRED FLAGS**

: **--url-map**:
A reference to a URL map resource. A URL map defines the mapping of URLs to
backend services. Before you can refer to a URL map, you must create the URL
map. To delete a URL map that a target proxy is referring to, you must first
delete the target gRPC proxy.

**OPTIONAL FLAGS**

: **--description**:
An optional, textual description for the target gRPC proxy.

**--validate-for-proxyless**:
If specified, configuration in the associated urlMap and the BackendServices is
checked to allow only the features that are supported in the latest release of
gRPC.
If unspecified, no such configuration checks are performed. This may cause
unexpected behavior in gRPC applications if unsupported features are configured.

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
gcloud alpha compute target-grpc-proxies create
```

```
gcloud beta compute target-grpc-proxies create
```