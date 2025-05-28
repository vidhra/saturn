# gcloud alpha compute instances network-interfaces add  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add)*

**NAME**

: **gcloud alpha compute instances network-interfaces add - add a dynamic network interface to a Compute Engine instance**

**SYNOPSIS**

: **`gcloud alpha compute instances network-interfaces add` `[INSTANCE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#INSTANCE_NAME)` [`[--aliases](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#--aliases)`=`ALIASES`] [`[--external-ipv6-address](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#--external-ipv6-address)`=`EXTERNAL_IPV6_ADDRESS`] [`[--external-ipv6-prefix-length](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#--external-ipv6-prefix-length)`=`EXTERNAL_IPV6_PREFIX_LENGTH`] [`[--igmp-query](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#--igmp-query)`=`IGMP_QUERY`] [`[--internal-ipv6-address](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#--internal-ipv6-address)`=`INTERNAL_IPV6_ADDRESS`] [`[--internal-ipv6-prefix-length](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#--internal-ipv6-prefix-length)`=`INTERNAL_IPV6_PREFIX_LENGTH`] [`[--ipv6-address](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#--ipv6-address)`=`IPV6_ADDRESS`] [`[--ipv6-network-tier](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#--ipv6-network-tier)`=`IPV6_NETWORK_TIER`] [`[--ipv6-prefix-length](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#--ipv6-prefix-length)`=`IPV6_PREFIX_LENGTH`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#--network)`=`NETWORK`] [`[--network-attachment](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#--network-attachment)`=`NETWORK_ATTACHMENT`] [`[--network-tier](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#--network-tier)`=`NETWORK_TIER`] [`[--parent-nic-name](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#--parent-nic-name)`=`PARENT_NIC_NAME`] [`[--private-network-ip](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#--private-network-ip)`=`PRIVATE_NETWORK_IP`] [`[--stack-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#--stack-type)`=`STACK_TYPE`] [`[--subnetwork](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#--subnetwork)`=`SUBNETWORK`] [`[--vlan](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#--vlan)`=`VLAN`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#--zone)`=`ZONE`] [`[--address](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#--address)`=`ADDRESS`     | `[--no-address](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#--address)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instances network-interfaces
add` adds a dynamic network interface to a Compute Engine instance. For
example:

```
gcloud alpha compute instances network-interfaces add instance-name --parent-nic-name nic1 --vlan 2
--network network-1 --subnetwork subnetwork-1
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAME`**:
Name of the instance to operate on. For details on valid instance names, refer
to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**FLAGS**

: **--aliases**:
The IP alias ranges to allocate for this interface. If there are multiple IP
alias ranges, they are separated by semicolons.
For example:

```
--aliases="10.128.1.0/24;range1:/32"
```

Each IP alias range consists of a range name and an IP range separated by a
colon, or just the IP range. The range name is the name of the range within the
network interface's subnet from which to allocate an IP alias range. If
unspecified, it defaults to the primary IP range of the subnet. The IP range can
be a CIDR range (e.g. `192.168.100.0/24`), a single IP address (e.g.
`192.168.100.1`), or a netmask in CIDR format (e.g.
`/24`). If the IP range is specified by CIDR range or single IP
address, it must belong to the CIDR range specified by the range name on the
subnet. If the IP range is specified by netmask, the IP allocator will pick an
available range with the specified netmask and allocate it to this network
interface.

**--external-ipv6-address**:
Assigns the given external IPv6 address to an instance. The address must be the
first IP in the range. This option is applicable only to dual-stack instances
with stack-type=IPV4_ONLY.

**--external-ipv6-prefix-length**:
The prefix length of the external IPv6 address range. This flag should be used
together with `--external-ipv6-address`. Currently only
`/96` is supported and the default value is `96`.

**--igmp-query**:
Determines if the Compute Engine instance can receive and respond to IGMP query
packets on the specified network interface. `IGMP_QUERY`
must be one of:

**`IGMP_QUERY_DISABLED`**:
IGMP Query on the network interface is disabled.

**`IGMP_QUERY_V2`**:
IGMP Query V2 on the network interface is enabled.

**--internal-ipv6-address**:
Assigns the given internal IPv6 address or range to an instance. The address
must be the first IP address in the range or a /96 IP address range. This option
can only be used on a dual stack instance network interface.

**--internal-ipv6-prefix-length**:
Optional field that indicates the prefix length of the internal IPv6 address
range, should be used together with `--internal-ipv6-address=fd20::`.
Only /96 IP address range is supported and the default value is 96. If not set,
then either the prefix length from
`--internal-ipv6-address=fd20::/96` will be used or the default value
of 96 will be assigned.

**--ipv6-address**:
Assigns the given external IPv6 address to an instance. The address must be the
first IP in the range. This option is applicable only to dual-stack instances
with stack-type=IPV4_ONLY.

**--ipv6-network-tier**:
Specifies the IPv6 network tier that will be used to configure the instance
network interface IPv6 access config. `IPV6_NETWORK_TIER`
must be (only one value is supported):

**`PREMIUM`**:
High quality, Google-grade network tier.

**--ipv6-prefix-length**:
The prefix length of the external IPv6 address range. This flag should be used
together with `--ipv6-address`. Currently only `/96` is
supported and the default value is `96`.

**--network**:
Specifies the network this network interface belongs to.

**--network-attachment**:
The network attachment URL this network interface should connect to.

**--network-tier**:
Specifies the network tier that will be used to configure the instance network
interface. ``NETWORK_TIER`` must be one of:
`PREMIUM`, `STANDARD`, `FIXED_STANDARD`. The
default value is `PREMIUM`. `NETWORK_TIER` must
be one of:

**`FIXED_STANDARD`**:
Public internet quality with fixed bandwidth.

**`PREMIUM`**:
High quality, Google-grade network tier.

**`STANDARD`**:
Public internet quality.

**--parent-nic-name**:
Name of the parent network interface of a dynamic network interface.

**--private-network-ip**:
Specifies the RFC1918 IP to assign to the network interface. The IP should be in
the subnet IP range.

**--stack-type**:
The stack type for the default network interface. Determines if IPv6 is enabled
on the default network interface. `STACK_TYPE` must be one
of:

**`IPV4_IPV6`**:
The network interface can have both IPv4 and IPv6 addresses.

**`IPV4_ONLY`**:
The network interface will be assigned IPv4 addresses.

**--subnetwork**:
Specifies the subnetwork this network interface belongs to.

**--vlan**:
VLAN tag of a dynamic network interface, must be in range from 2 to 4094
inclusively.

**--zone**:
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

**--address**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud beta compute instances network-interfaces add
```