# gcloud compute forwarding-rules create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create)*

**NAME**

: **gcloud compute forwarding-rules create - create a forwarding rule to direct network traffic to a load balancer**

**SYNOPSIS**

: **`gcloud compute forwarding-rules create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#NAME)` (`[--backend-service](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--backend-service)`=`BACKEND_SERVICE`     | `[--target-google-apis-bundle](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--target-google-apis-bundle)`=`TARGET_GOOGLE_APIS_BUNDLE`     | `[--target-grpc-proxy](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--target-grpc-proxy)`=`TARGET_GRPC_PROXY`     | `[--target-http-proxy](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--target-http-proxy)`=`TARGET_HTTP_PROXY`     | `[--target-https-proxy](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--target-https-proxy)`=`TARGET_HTTPS_PROXY`     | `[--target-instance](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--target-instance)`=`TARGET_INSTANCE`     | `[--target-pool](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--target-pool)`=`TARGET_POOL`     | `[--target-service-attachment](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--target-service-attachment)`=`TARGET_SERVICE_ATTACHMENT`     | `[--target-ssl-proxy](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--target-ssl-proxy)`=`TARGET_SSL_PROXY`     | `[--target-tcp-proxy](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--target-tcp-proxy)`=`TARGET_TCP_PROXY`     | `[--target-vpn-gateway](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--target-vpn-gateway)`=`TARGET_VPN_GATEWAY`) [`[--address](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--address)`=`ADDRESS`] [`[--allow-global-access](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--allow-global-access)`] [`[--allow-psc-global-access](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--allow-psc-global-access)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--description)`=`DESCRIPTION`] [`[--disable-automate-dns-zone](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--disable-automate-dns-zone)`] [`[--ip-collection](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--ip-collection)`=`IP_COLLECTION`] [`[--ip-collection-region](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--ip-collection-region)`=`IP_COLLECTION_REGION`] [`[--ip-protocol](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--ip-protocol)`=`IP_PROTOCOL`] [`[--ip-version](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--ip-version)`=`IP_VERSION`] [`[--is-mirroring-collector](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--is-mirroring-collector)`] [`[--load-balancing-scheme](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--load-balancing-scheme)`=`LOAD_BALANCING_SCHEME`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--network)`=`NETWORK`] [`[--network-tier](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--network-tier)`=`NETWORK_TIER`] [`[--service-directory-registration](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--service-directory-registration)`=`SERVICE_DIRECTORY_REGISTRATION`] [`[--service-label](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--service-label)`=`SERVICE_LABEL`] [`[--source-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--source-ip-ranges)`=`SOURCE_IP_RANGE`,[…]] [`[--subnet](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--subnet)`=`SUBNET`] [`[--subnet-region](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--subnet-region)`=`SUBNET_REGION`] [`[--target-instance-zone](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--target-instance-zone)`=`TARGET_INSTANCE_ZONE`] [`[--target-pool-region](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--target-pool-region)`=`TARGET_POOL_REGION`] [`[--target-service-attachment-region](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--target-service-attachment-region)`=`TARGET_SERVICE_ATTACHMENT_REGION`] [`[--target-vpn-gateway-region](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--target-vpn-gateway-region)`=`TARGET_VPN_GATEWAY_REGION`] [`[--address-region](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--address-region)`=`ADDRESS_REGION`     | `[--global-address](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--global-address)`] [`[--backend-service-region](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--backend-service-region)`=`BACKEND_SERVICE_REGION`     | `[--global-backend-service](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--global-backend-service)`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--region)`=`REGION`] [`[--global-target-http-proxy](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--global-target-http-proxy)`     | `[--target-http-proxy-region](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--target-http-proxy-region)`=`TARGET_HTTP_PROXY_REGION`] [`[--global-target-https-proxy](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--global-target-https-proxy)`     | `[--target-https-proxy-region](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--target-https-proxy-region)`=`TARGET_HTTPS_PROXY_REGION`] [`[--global-target-tcp-proxy](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--global-target-tcp-proxy)`     | `[--target-tcp-proxy-region](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--target-tcp-proxy-region)`=`TARGET_TCP_PROXY_REGION`] [`[--port-range](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--port-range)`=[`PORT` | `START_PORT-END_PORT`]     | `[--ports](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#--ports)`=`ALL`     | [`[PORT](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#PORT)` | `START_PORT-END_PORT`],[…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute forwarding-rules create` is used to create a
forwarding rule. A forwarding rule directs traffic that matches a destination IP
address (and possibly a TCP or UDP port) to a forwarding target (load balancer,
VPN gateway or VM instance).
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
When creating a forwarding rule, exactly one of
``--target-instance``,
``--target-pool``,
``--target-http-proxy``,
``--target-https-proxy``,
``--target-grpc-proxy``,
``--target-ssl-proxy``,
``--target-tcp-proxy``,
``--target-vpn-gateway``,
``--backend-service`` or
``--target-google-apis-bundle`` must be
specified.

**EXAMPLES**

: To create a global forwarding rule that will forward all traffic on port 8080
for IP address ADDRESS to a target http proxy PROXY, run:

```
gcloud compute forwarding-rules create RULE_NAME --global --target-http-proxy=PROXY --ports=8080 --address=ADDRESS
```

To create a regional forwarding rule for the subnet SUBNET_NAME on the default
network that will forward all traffic on ports 80-82 to a backend service
SERVICE_NAME, run:

```
gcloud compute forwarding-rules create RULE_NAME --load-balancing-scheme=INTERNAL --backend-service=SERVICE_NAME --subnet=SUBNET_NAME --network=default --region=REGION --ports=80-82
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the forwarding rule to create.

**REQUIRED FLAGS**

: **--backend-service**

**OPTIONAL FLAGS**

: **--address**:
The IP address that the forwarding rule serves. When a client sends traffic to
this IP address, the forwarding rule directs the traffic to the target that you
specify in the forwarding rule.
If you don't specify a reserved IP address, an ephemeral IP address is assigned.
You can specify the IP address as a literal IP address or as a reference to an
existing Address resource. The following examples are all valid:

- 100.1.2.3
- 2600:1901::/96
- [https://compute.googleapis.com/compute/v1/projects/project-1/regions/us-central1/addresses/address-1](https://compute.googleapis.com/compute/v1/projects/project-1/regions/us-central1/addresses/address-1)
- projects/project-1/regions/us-central1/addresses/address-1
- regions/us-central1/addresses/address-1
- global/addresses/address-1
- address-1

The load-balancing-scheme (EXTERNAL, EXTERNAL_MANAGED, INTERNAL,
INTERNAL_SELF_MANAGED, INTERNAL_MANAGED) and the target of the forwarding rule
determine the type of IP address that you can use. The address type must be
external for load-balancing-scheme EXTERNAL or EXTERNAL_MANAGED. For other
load-balancing-schemes, the address type must be internal. For detailed
information, refer to [https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts#ip_address_specifications](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts#ip_address_specifications).

**--allow-global-access**:
If True, then clients from all regions can access this internal forwarding rule.
This can only be specified for forwarding rules with the LOAD_BALANCING_SCHEME
set to INTERNAL or INTERNAL_MANAGED. For forwarding rules of type INTERNAL, the
target must be either a backend service or a target instance.

**--allow-psc-global-access**:
If specified, clients from all regions can access this Private Service Connect
forwarding rule. This can only be specified if the forwarding rule's target is a
service attachment (--target-service-attachment).

**--description**:
Optional textual description for the forwarding rule.

**--disable-automate-dns-zone**:
If specified, then a DNS zone will not be auto-generated for this Private
Service Connect forwarding rule. This can only be specified if the forwarding
rule's target is a service attachment
(`--target-service-attachment=SERVICE_ATTACHMENT`) or Google APIs
bundle (`--target-google-apis-bundle=API_BUNDLE`)

**--ip-collection**:
Resource reference to a public delegated prefix. The PublicDelegatedPrefix (PDP)
must be a sub-prefix in EXTERNAL_IPV6_FORWARDING_RULE_CREATION mode.

**--ip-collection-region**:
Region of the public delegated prefix to operate on. If not specified, the
region is set to the region of the forwarding rule. Overrides the default
`compute/region` property value for this command invocation.

**--ip-protocol**:
IP protocol that the rule will serve. The default is `TCP`.
Note that if the load-balancing scheme is `INTERNAL`, the protocol
must be one of: `TCP`, `UDP`, `L3_DEFAULT`.
For a load-balancing scheme that is `EXTERNAL`, all IP_PROTOCOL
options are valid.
`IP_PROTOCOL` must be one of: `AH`,
`ESP`, `ICMP`, `SCTP`, `TCP`,
`UDP`, `L3_DEFAULT`.

**--ip-version**:
Version of the IP address to be allocated or assigned. The default is IPv4.
`IP_VERSION` must be one of: `IPV4`,
`IPV6`.

**--is-mirroring-collector**:
If set, this forwarding rule can be used as a collector for packet mirroring.
This can only be specified for forwarding rules with the LOAD_BALANCING_SCHEME
set to INTERNAL.

**--load-balancing-scheme**:
This defines the forwarding rule's load balancing scheme. Note that it defaults
to EXTERNAL and is not applicable for Private Service Connect forwarding rules.
`LOAD_BALANCING_SCHEME` must be one of:

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
(Only for --load-balancing-scheme=INTERNAL or
--load-balancing-scheme=INTERNAL_SELF_MANAGED or
--load-balancing-scheme=EXTERNAL_MANAGED (regional) or
--load-balancing-scheme=INTERNAL_MANAGED) Network that this forwarding rule
applies to. If this field is not specified, the default network is used. In the
absence of the default network, this field must be specified.

**--network-tier**:
Network tier to assign to the forwarding rules.
``NETWORK_TIER`` must be one of:
`PREMIUM`, `STANDARD`. The default value is
`PREMIUM`.

**--service-directory-registration**:
The Service Directory service in which to register this forwarding rule as an
endpoint. The Service Directory service must be in the same project and region
as the forwarding rule you are creating.

**--service-label**:
(Only for Internal Load Balancing): [https://cloud.google.com/load-balancing/docs/dns-names/](https://cloud.google.com/load-balancing/docs/dns-names/)
The DNS label to use as the prefix of the fully qualified domain name for this
forwarding rule. The full name will be internally generated and output as
dnsName. If this field is not specified, no DNS record will be generated and no
DNS name will be output. You cannot use the `--service-label` flag if
the forwarding rule references an internal IP address that has the
`--purpose=SHARED_LOADBALANCER_VIP` flag set.

**--source-ip-ranges**:
List of comma-separated IP addresses or IP ranges. If set, this forwarding rule
only forwards traffic when the packet's source IP address matches one of the IP
ranges set here.

**--subnet**:
(Only for --load-balancing-scheme=INTERNAL and
--load-balancing-scheme=INTERNAL_MANAGED) Subnetwork that this forwarding rule
applies to. If the network is auto mode, this flag is optional. If the network
is custom mode, this flag is required.

**--subnet-region**:
Region of the subnetwork to operate on. If not specified, the region is set to
the region of the forwarding rule. Overrides the default
`compute/region` property value for this command invocation.

**--target-instance-zone**:
Zone of the target instance to operate on. Overrides the default
`compute/zone` property value for this command invocation.

**--target-pool-region**:
Region of the target pool to operate on. If not specified, the region is set to
the region of the forwarding rule. Overrides the default
`compute/region` property value for this command invocation.

**--target-service-attachment-region**:
Region of the target service attachment to operate on. If not specified, you
might be prompted to select a region (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/region`` property:

```
gcloud config set compute/region REGION
```

A list of regions can be fetched by running:

```
gcloud compute regions list
```

To unset the property, run:

```
gcloud config unset compute/region
```

Alternatively, the region can be stored in the environment variable
``CLOUDSDK_COMPUTE_REGION``.

**--target-vpn-gateway-region**:
Region of the VPN gateway to operate on. If not specified, the region is set to
the region of the forwarding rule. Overrides the default
`compute/region` property value for this command invocation.

**--address-region**

**--backend-service-region**

**--global**

**--global-target-http-proxy**

**--global-target-https-proxy**

**--global-target-tcp-proxy**

**--port-range**

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
gcloud alpha compute forwarding-rules create
```

```
gcloud beta compute forwarding-rules create
```