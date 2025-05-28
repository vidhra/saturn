# gcloud compute routers add-bgp-peer  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer)*

**NAME**

: **gcloud compute routers add-bgp-peer - add a BGP peer to a Compute Engine router**

**SYNOPSIS**

: **`gcloud compute routers add-bgp-peer` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#NAME)` `[--interface](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--interface)`=`INTERFACE` `[--peer-asn](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--peer-asn)`=`PEER_ASN` `[--peer-name](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--peer-name)`=`PEER_NAME` [`[--advertised-route-priority](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--advertised-route-priority)`=`ADVERTISED_ROUTE_PRIORITY`] [`[--advertisement-mode](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--advertisement-mode)`=`MODE`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--async)`] [`[--custom-learned-route-priority](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--custom-learned-route-priority)`=`PRIORITY`] [`[--[no-]enable-ipv4](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--[no-]enable-ipv4)`] [`[--[no-]enable-ipv6](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--[no-]enable-ipv6)`] [`[--[no-]enabled](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--[no-]enabled)`] [`[--export-policies](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--export-policies)`=[`EXPORT_POLICY`,…]] [`[--import-policies](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--import-policies)`=[`IMPORT_POLICY`,…]] [`[--instance](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--instance)`=`INSTANCE`] [`[--instance-zone](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--instance-zone)`=`INSTANCE_ZONE`] [`[--ipv4-nexthop-address](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--ipv4-nexthop-address)`=`IPV4_NEXTHOP_ADDRESS`] [`[--ipv6-nexthop-address](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--ipv6-nexthop-address)`=`IPV6_NEXTHOP_ADDRESS`] [`[--md5-authentication-key](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--md5-authentication-key)`=`MD5_AUTHENTICATION_KEY`] [`[--peer-ip-address](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--peer-ip-address)`=`PEER_IP_ADDRESS`] [`[--peer-ipv4-nexthop-address](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--peer-ipv4-nexthop-address)`=`PEER_IPV4_NEXTHOP_ADDRESS`] [`[--peer-ipv6-nexthop-address](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--peer-ipv6-nexthop-address)`=`PEER_IPV6_NEXTHOP_ADDRESS`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--region)`=`REGION`] [`[--set-advertisement-groups](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--set-advertisement-groups)`=[`GROUP`,…]] [`[--set-advertisement-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--set-advertisement-ranges)`=[`CIDR_RANGE`=`DESC`,…]] [`[--set-custom-learned-route-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--set-custom-learned-route-ranges)`=[`CIDR_RANGE`,…]] [`[--bfd-min-receive-interval](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--bfd-min-receive-interval)`=`BFD_MIN_RECEIVE_INTERVAL` `[--bfd-min-transmit-interval](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--bfd-min-transmit-interval)`=`BFD_MIN_TRANSMIT_INTERVAL` `[--bfd-multiplier](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--bfd-multiplier)`=`BFD_MULTIPLIER` `[--bfd-session-initialization-mode](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#--bfd-session-initialization-mode)`=`BFD_SESSION_INITIALIZATION_MODE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Add a BGP peer to a Compute Engine router.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the router to operate on.

**REQUIRED FLAGS**

: **--interface**:
The name of the interface for this BGP peer.

**--peer-asn**:
The BGP autonomous system number (ASN) for this BGP peer. Must be a 16-bit or
32-bit private ASN as defined in https://tools.ietf.org/html/rfc6996, for
example `--asn=64512`.

**--peer-name**:
The name of the new BGP peer being added.

**OPTIONAL FLAGS**

: **--advertised-route-priority**:
The priority of routes advertised to this BGP peer. In the case where there is
more than one matching route of maximum length, the routes with lowest priority
value win. 0 <= priority <= 65535. If not specified, will use
Google-managed priorities.

**--advertisement-mode**:
The new advertisement mode for this peer. `MODE` must be
one of:

**`CUSTOM`**:
Custom (user-configured) BGP advertisements.

**`DEFAULT`**:
Default (Google-managed) BGP advertisements.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--custom-learned-route-priority**:
An integral value `0` <= priority <= `65535`, to be
applied to all custom learned route IP address ranges for this peer. If not
specified, a Google-managed priority value of 100 is used. The routes with the
lowest priority value win.

**--[no-]enable-ipv4**:
If IPv4 is enabled, the peer connection can be established with IPv4 route
exchange. If disabled, no IPv4 route exchange is allowed on any active session.
By default enabled for IPv4-based BGP sessions. Use `--enable-ipv4`
to enable and `--no-enable-ipv4` to disable.

**--[no-]enable-ipv6**:
If IPv6 is enabled, the peer connection can be established with IPv6 route
exchange. If disabled, no IPv6 route exchange is allowed on any active session.
Disabled by default. Use `--enable-ipv6` to enable and
`--no-enable-ipv6` to disable.

**--[no-]enabled**:
If enabled, the peer connection can be established with routing information. If
disabled, any active session with the peer is terminated and all associated
routing information is removed. Enabled by default. Use `--enabled`
to enable and `--no-enabled` to disable.

**--export-policies**:
Comma-separated list of export policies. Passing an empty string removes all
export policies.

**--import-policies**:
Comma-separated list of import policies. Passing an empty string removes all
import policies.

**--instance**:
Router appliance instance of the BGP peer being added.

**--instance-zone**:
Zone of the instance to operate on. If not specified, you might be prompted to
select a zone (interactive mode only). `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` attempts to identify the
appropriate zone by searching for resources in your currently active project. If
the zone cannot be determined, `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with
all available Google Cloud Platform zones.
To avoid prompting when this flag is omitted, the user can set the
``compute/zone`` property:

```
gcloud config set compute/zone ZONE
```

A list of zones can be fetched by running:

```
gcloud compute zones list
```

To unset the property, run:

```
gcloud config unset compute/zone
```

Alternatively, the zone can be stored in the environment variable
``CLOUDSDK_COMPUTE_ZONE``.

**--ipv4-nexthop-address**:
If IPv4 route exchange is enabled for IPv6-based BGP, the IPv4 next hop address
of the Cloud Router interface for this BGP peer. Ignored otherwise. Must be a
Google owned link-local IPv4 address in the range 169.254.0.0/16 and must belong
to the same subnet as the interface address of the peer router.

**--ipv6-nexthop-address**:
If IPv6 route exchange is enabled for IPv4-based BGP, the IPv6 next hop address
of the Cloud Router interface for this BGP peer. Ignored otherwise. Must be a
Google owned global unicast IPv6 address belonging to the range
2600:2d00:0:2:0:0:0:0/64 or 2600:2d00:0:3:0:0:0:0/64 and must belong to same
subnet as the interface address of the peer router.

**--md5-authentication-key**:
The MD5 authentication key for this BGP peer. Maximum length is 80 characters.
Can contain only printable ASCII characters.

**--peer-ip-address**:
The address of the peer router. Must be a link-local IPv4 address in the range
169.254.0.0/16 or an ULA IPv6 address in the range fdff:1::/64.

**--peer-ipv4-nexthop-address**:
If IPv4 route exchange is enabled for IPv6-based BGP, the IPv4 next hop address
of the peer router. Ignored otherwise. Must be a Google owned link-local IPv4
address in the range 169.254.0.0/16.

**--peer-ipv6-nexthop-address**:
If IPv6 route exchange is enabled for IPv4-based BGP, the IPv6 next hop address
of the peer router. Ignored otherwise. Must be a Google owned global unicast
IPv6 address belonging to the range 2600:2d00:0:2:0:0:0:0/64 or
2600:2d00:0:3:0:0:0:0/64.

**--region**:
Region of the router to operate on. If not specified, you might be prompted to
select a region (interactive mode only).
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

**--set-advertisement-groups**:
The list of pre-defined groups of IP ranges to dynamically advertise on this
peer. This list can only be specified in custom advertisement mode.
`GROUP` must be (only one value is supported):

**`ALL_SUBNETS`**:
Automatically advertise all available subnets. This excludes any routes learned
for subnets that use VPC Network Peering.

**--set-advertisement-ranges**:
The list of individual IP ranges, in CIDR format, to dynamically advertise on
this peer. Each IP range can (optionally) be given a text description DESC. For
example, to advertise a specific range, use
`--set-advertisement-ranges=192.168.10.0/24`. To store a description
with the range, use
`--set-advertisement-ranges=192.168.10.0/24=my-networks`. This list
can only be specified in custom advertisement mode.

**--set-custom-learned-route-ranges**:
The list of user-defined custom learned route IP address ranges for this peer.
This list is a comma separated IP address ranges such as
`1.2.3.4`,`6.7.0.0/16`,`2001:db8:abcd:12::/64`
where each IP address range must be a valid CIDR-formatted prefix. If an IP
address is provided without a subnet mask, it is interpreted as a /32 singular
IP address range for IPv4, and /128 for IPv6.

**--bfd-min-receive-interval**

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
gcloud alpha compute routers add-bgp-peer
```

```
gcloud beta compute routers add-bgp-peer
```