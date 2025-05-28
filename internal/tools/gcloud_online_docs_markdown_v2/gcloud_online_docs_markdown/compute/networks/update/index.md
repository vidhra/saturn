# gcloud compute networks update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/networks/update](https://cloud.google.com/sdk/gcloud/reference/compute/networks/update)*

**NAME**

: **gcloud compute networks update - update a Compute Engine network**

**SYNOPSIS**

: **`gcloud compute networks update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/networks/update#NAME)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/networks/update#--async)`] [`[--[no-]enable-ula-internal-ipv6](https://cloud.google.com/sdk/gcloud/reference/compute/networks/update#--[no-]enable-ula-internal-ipv6)`] [`[--internal-ipv6-range](https://cloud.google.com/sdk/gcloud/reference/compute/networks/update#--internal-ipv6-range)`=`INTERNAL_IPV6_RANGE`] [`[--mtu](https://cloud.google.com/sdk/gcloud/reference/compute/networks/update#--mtu)`=`MTU`] [`[--network-firewall-policy-enforcement-order](https://cloud.google.com/sdk/gcloud/reference/compute/networks/update#--network-firewall-policy-enforcement-order)`=`NETWORK_FIREWALL_POLICY_ENFORCEMENT_ORDER`] [`[--bgp-best-path-selection-mode](https://cloud.google.com/sdk/gcloud/reference/compute/networks/update#--bgp-best-path-selection-mode)`=`BGP_BEST_PATH_SELECTION_MODE` `[--[no-]bgp-bps-always-compare-med](https://cloud.google.com/sdk/gcloud/reference/compute/networks/update#--[no-]bgp-bps-always-compare-med)` `[--bgp-bps-inter-region-cost](https://cloud.google.com/sdk/gcloud/reference/compute/networks/update#--bgp-bps-inter-region-cost)`=`BGP_BPS_INTER_REGION_COST`] [`[--bgp-routing-mode](https://cloud.google.com/sdk/gcloud/reference/compute/networks/update#--bgp-routing-mode)`=`MODE`     | `[--switch-to-custom-subnet-mode](https://cloud.google.com/sdk/gcloud/reference/compute/networks/update#--switch-to-custom-subnet-mode)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/networks/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute networks update` is used to update Compute Engine
networks.

**EXAMPLES**

: To update regional network with the name 'network-name' to global, run:

```
gcloud compute networks update network-name --bgp-routing-mode=global
```

To update an auto subnet mode network with the name 'network-name' to custom
subnet mode, run:

```
gcloud compute networks update network-name --switch-to-custom-subnet-mode
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the network to operate on.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

**--bgp-best-path-selection-mode**

**--bgp-routing-mode**

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
gcloud alpha compute networks update
```

```
gcloud beta compute networks update
```