# gcloud compute forwarding-rules set-target  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target)*

**NAME**

: **gcloud compute forwarding-rules set-target - modify a forwarding rule to direct network traffic to a new target**

**SYNOPSIS**

: **`gcloud compute forwarding-rules set-target` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#NAME)` (`[--backend-service](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--backend-service)`=`BACKEND_SERVICE`     | `[--target-grpc-proxy](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--target-grpc-proxy)`=`TARGET_GRPC_PROXY`     | `[--target-http-proxy](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--target-http-proxy)`=`TARGET_HTTP_PROXY`     | `[--target-https-proxy](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--target-https-proxy)`=`TARGET_HTTPS_PROXY`     | `[--target-instance](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--target-instance)`=`TARGET_INSTANCE`     | `[--target-pool](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--target-pool)`=`TARGET_POOL`     | `[--target-ssl-proxy](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--target-ssl-proxy)`=`TARGET_SSL_PROXY`     | `[--target-tcp-proxy](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--target-tcp-proxy)`=`TARGET_TCP_PROXY`     | `[--target-vpn-gateway](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--target-vpn-gateway)`=`TARGET_VPN_GATEWAY`) [`[--load-balancing-scheme](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--load-balancing-scheme)`=`LOAD_BALANCING_SCHEME`; default="EXTERNAL"] [`[--network](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--network)`=`NETWORK`] [`[--subnet](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--subnet)`=`SUBNET`] [`[--subnet-region](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--subnet-region)`=`SUBNET_REGION`] [`[--target-instance-zone](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--target-instance-zone)`=`TARGET_INSTANCE_ZONE`] [`[--target-pool-region](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--target-pool-region)`=`TARGET_POOL_REGION`] [`[--target-vpn-gateway-region](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--target-vpn-gateway-region)`=`TARGET_VPN_GATEWAY_REGION`] [`[--backend-service-region](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--backend-service-region)`=`BACKEND_SERVICE_REGION`     | `[--global-backend-service](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--global-backend-service)`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--region)`=`REGION`] [`[--global-target-http-proxy](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--global-target-http-proxy)`     | `[--target-http-proxy-region](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--target-http-proxy-region)`=`TARGET_HTTP_PROXY_REGION`] [`[--global-target-https-proxy](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--global-target-https-proxy)`     | `[--target-https-proxy-region](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--target-https-proxy-region)`=`TARGET_HTTPS_PROXY_REGION`] [`[--global-target-tcp-proxy](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--global-target-tcp-proxy)`     | `[--target-tcp-proxy-region](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#--target-tcp-proxy-region)`=`TARGET_TCP_PROXY_REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute forwarding-rules set-target` is used to set a new
target for a forwarding rule. A forwarding rule directs traffic that matches a
destination IP address (and possibly a TCP or UDP port) to a forwarding target
(load balancer, VPN gateway or VM instance).
Forwarding rules can be either global or regional, specified with the
``--global`` or
``--region=REGION`` flags. For more information
about the scope of a forwarding rule, refer to [https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts).
Forwarding rules can be external, internal, internal managed, or internal
self-managed, specified with the
``--load-balancing-scheme=[EXTERNAL|EXTERNAL_MANAGED|INTERNAL|INTERNAL_MANAGED|INTERNAL_SELF_MANAGED]``
flag. External forwarding rules are accessible from the internet, while internal
forwarding rules are only accessible from within their VPC networks. You can
specify a reserved static external or internal IP address with the
``--address=ADDRESS`` flag for the forwarding
rule. Otherwise, if the flag is unspecified, an ephemeral IP address is
automatically assigned (global IP addresses for global forwarding rules and
regional IP addresses for regional forwarding rules); an internal forwarding
rule is automatically assigned an ephemeral internal IP address from the subnet
specified with the ``--subnet`` flag. You must
provide an IP address for an internal self-managed forwarding rule.
Different types of load balancers work at different layers of the OSI networking
model (http://en.wikipedia.org/wiki/Network_layer). Layer 3/4 targets include
target pools, target SSL proxies, target TCP proxies, and backend services.
Layer 7 targets include target HTTP proxies and target HTTPS proxies. For more
information, refer to [https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts).

```
When creating a forwarding rule, exactly one of  `_--target-instance_`,
`_--target-pool_`, `_--target-http-proxy_`, `_--target-https-proxy_`,
`_--target-grpc-proxy_`, `_--target-ssl-proxy_`,
`_--target-tcp-proxy_` or `_--target-vpn-gateway_`
must be specified.
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the forwarding rule to operate on.

**REQUIRED FLAGS**

: **--backend-service**

**OPTIONAL FLAGS**

: **--load-balancing-scheme**:
(DEPRECATED) This defines the forwarding rule's load balancing scheme.
The --load-balancing-scheme option is deprecated and will be removed in an
upcoming release. If you're currently using this argument, you should remove it
from your workflows. `LOAD_BALANCING_SCHEME` must be one
of:

**`EXTERNAL`**:
Classic Application Load Balancers, global external proxy Network Load
Balancers, external passthrough Network Load Balancers or protocol forwarding,
used with one of --target-http-proxy, --target-https-proxy, --target-tcp-proxy,
--target-ssl-proxy, --target-pool, --target-vpn-gateway, --target-instance.

**`EXTERNAL_MANAGED`**:
Global and regional external Application Load Balancers, and regional external
proxy Network Load Balancers, used with --target-http-proxy,
--target-https-proxy, --target-tcp-proxy.

**`INTERNAL`**:
Internal passthrough Network Load Balancers or protocol forwarding, used with
--backend-service.

**`INTERNAL_MANAGED`**:
Internal Application Load Balancers and internal proxy Network Load Balancers,
used with --target-http-proxy, --target-https-proxy, --target-tcp-proxy.

**`INTERNAL_SELF_MANAGED`**:
Traffic Director, used with --target-http-proxy, --target-https-proxy,
--target-grpc-proxy, --target-tcp-proxy.

**--network**:
(DEPRECATED) Only for --load-balancing-scheme=INTERNAL or
--load-balancing-scheme=INTERNAL_SELF_MANAGED or
--load-balancing-scheme=EXTERNAL_MANAGED (regional) or
--load-balancing-scheme=INTERNAL_MANAGED) Network that this forwarding rule
applies to. If this field is not specified, the default network is used. In the
absence of the default network, this field must be specified.
The --network option is deprecated and will be removed in an upcoming release.
If you're currently using this argument, you should remove it from your
workflows.

**--subnet**:
(DEPRECATED) Only for --load-balancing-scheme=INTERNAL and
--load-balancing-scheme=INTERNAL_MANAGED) Subnetwork that this forwarding rule
applies to. If the network is auto mode, this flag is optional. If the network
is custom mode, this flag is required.
The --subnet option is deprecated and will be removed in an upcoming release. If
you're currently using this argument, you should remove it from your workflows.

**--subnet-region**:
(DEPRECATED) Region of the subnetwork to operate on. If not specified, the
region is set to the region of the forwarding rule. Overrides the default
compute/region property value for this command invocation.
The --subnet-region option is deprecated and will be removed in an upcoming
release. If you're currently using this argument, you should remove it from your
workflows.

**--target-instance-zone**:
Zone of the target instance to operate on. Overrides the default
`compute/zone` property value for this command invocation.

**--target-pool-region**:
Region of the target pool to operate on. If not specified, the region is set to
the region of the forwarding rule. Overrides the default
`compute/region` property value for this command invocation.

**--target-vpn-gateway-region**:
Region of the VPN gateway to operate on. If not specified, the region is set to
the region of the forwarding rule. Overrides the default
`compute/region` property value for this command invocation.

**--backend-service-region**

**--global**

**--global-target-http-proxy**

**--global-target-https-proxy**

**--global-target-tcp-proxy**

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
gcloud alpha compute forwarding-rules set-target
```

```
gcloud beta compute forwarding-rules set-target
```