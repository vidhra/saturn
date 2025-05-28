# gcloud compute networks create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/networks/create](https://cloud.google.com/sdk/gcloud/reference/compute/networks/create)*

**NAME**

: **gcloud compute networks create - create a Compute Engine network**

**SYNOPSIS**

: **`gcloud compute networks create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/networks/create#NAME)` [`[--bgp-routing-mode](https://cloud.google.com/sdk/gcloud/reference/compute/networks/create#--bgp-routing-mode)`=`MODE`; default="regional"] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/networks/create#--description)`=`DESCRIPTION`] [`[--[no-]enable-ula-internal-ipv6](https://cloud.google.com/sdk/gcloud/reference/compute/networks/create#--[no-]enable-ula-internal-ipv6)`] [`[--internal-ipv6-range](https://cloud.google.com/sdk/gcloud/reference/compute/networks/create#--internal-ipv6-range)`=`INTERNAL_IPV6_RANGE`] [`[--mtu](https://cloud.google.com/sdk/gcloud/reference/compute/networks/create#--mtu)`=`MTU`] [`[--network-firewall-policy-enforcement-order](https://cloud.google.com/sdk/gcloud/reference/compute/networks/create#--network-firewall-policy-enforcement-order)`=`NETWORK_FIREWALL_POLICY_ENFORCEMENT_ORDER`] [`[--network-profile](https://cloud.google.com/sdk/gcloud/reference/compute/networks/create#--network-profile)`=`NETWORK_PROFILE`] [`[--range](https://cloud.google.com/sdk/gcloud/reference/compute/networks/create#--range)`=`RANGE`] [`[--subnet-mode](https://cloud.google.com/sdk/gcloud/reference/compute/networks/create#--subnet-mode)`=`MODE`] [`[--bgp-best-path-selection-mode](https://cloud.google.com/sdk/gcloud/reference/compute/networks/create#--bgp-best-path-selection-mode)`=`BGP_BEST_PATH_SELECTION_MODE` `[--[no-]bgp-bps-always-compare-med](https://cloud.google.com/sdk/gcloud/reference/compute/networks/create#--[no-]bgp-bps-always-compare-med)` `[--bgp-bps-inter-region-cost](https://cloud.google.com/sdk/gcloud/reference/compute/networks/create#--bgp-bps-inter-region-cost)`=`BGP_BPS_INTER_REGION_COST`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/networks/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute networks create` is used to create virtual networks.
A network performs the same function that a router does in a home network: it
describes the network range and gateway IP address, handles communication
between instances, and serves as a gateway between instances and callers outside
the network.

**EXAMPLES**

: To create a regional auto subnet mode network with the name 'network-name', run:

```
gcloud compute networks create network-name
```

To create a global custom subnet mode network with the name 'network-name', run:

```
gcloud compute networks create network-name --bgp-routing-mode=global --subnet-mode=custom
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the network to create.

**FLAGS**

: **--bgp-routing-mode**:
The BGP routing mode for this network. If not specified, defaults to regional.
`MODE` must be one of:

**`global`**:
Cloud Routers in this network advertise subnetworks from all regions to their
BGP peers, and program instances in all regions with the router's best learned
BGP routes.

**`regional`**:
Cloud Routers in this network advertise subnetworks from their local region only
to their BGP peers, and program instances in their local region only with the
router's best learned BGP routes.

**--description**:
An optional, textual description for the network.

**--[no-]enable-ula-internal-ipv6**:
Enable/disable ULA internal IPv6 on this network. Enabling this feature will
assign a /48 from google defined ULA prefix fd20::/20.
Use `--enable-ula-internal-ipv6` to enable and
`--no-enable-ula-internal-ipv6` to disable.

**--internal-ipv6-range**:
When enabling ULA internal IPv6, caller can optionally specify the /48 range
they want from the google defined ULA prefix fd20::/20. ULA_IPV6_RANGE must be a
valid /48 ULA IPv6 address and within the fd20::/20. Operation will fail if the
speficied /48 is already in used by another resource. If the field is not
speficied, then a /48 range will be randomly allocated from fd20::/20 and
returned via this field.

**--mtu**:
Maximum transmission unit (MTU) is the size of the largest IP packet that can be
transmitted on this network. Default value is 1460 bytes. The minimum value is
1300 bytes and the maximum value is 8896 bytes. The MTU advertised via DHCP to
all instances attached to this network.

**--network-firewall-policy-enforcement-order**:
The Network Firewall Policy enforcement order of this network. If not specified,
defaults to AFTER_CLASSIC_FIREWALL.
`NETWORK_FIREWALL_POLICY_ENFORCEMENT_ORDER` must be one
of:

**`AFTER_CLASSIC_FIREWALL`**:
Network Firewall Policy is enforced after classic firewall.

**`BEFORE_CLASSIC_FIREWALL`**:
Network Firewall Policy is enforced before classic firewall.

**--network-profile**:
The network profile to apply to this network.

**--range**:
Specifies the IPv4 address range of legacy mode networks. The range must be
specified in CIDR format: [http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
This flag only works if mode is [legacy](https://cloud.google.com/compute/docs/vpc/legacy).
Using legacy networks is **DEPRECATED**, given that many newer Google Cloud
Platform features are not supported on legacy networks. Please be advised that
legacy networks may not be supported in the future.

**--subnet-mode**:
The subnet mode of the network. If not specified, defaults to AUTO.
`MODE` must be one of:

**`auto`**:
Subnets are created automatically. This is the recommended selection.

**`custom`**:
Create subnets manually.

**`legacy`**:
[Deprecated] Create an old style network that has a range and cannot have
subnets. This is not recommended for new networks.

**--bgp-best-path-selection-mode**

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
gcloud alpha compute networks create
```

```
gcloud beta compute networks create
```