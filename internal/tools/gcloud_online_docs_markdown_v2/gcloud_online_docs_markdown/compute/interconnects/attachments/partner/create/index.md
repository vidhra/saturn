# gcloud compute interconnects attachments partner create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/create](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/create)*

**NAME**

: **gcloud compute interconnects attachments partner create - create a Compute Engine partner interconnect attachment**

**SYNOPSIS**

: **`gcloud compute interconnects attachments partner create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/create#NAME)` `[--edge-availability-domain](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/create#--edge-availability-domain)`=`AVAILABILITY_DOMAIN` `[--router](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/create#--router)`=`ROUTER` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/create#--description)`=`DESCRIPTION`] [`[--enable-admin](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/create#--enable-admin)`] [`[--encryption](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/create#--encryption)`=`ENCRYPTION`] [`[--ipsec-internal-addresses](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/create#--ipsec-internal-addresses)`=[`ADDRESSES`]] [`[--mtu](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/create#--mtu)`=`MTU`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/create#--region)`=`REGION`] [`[--stack-type](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/create#--stack-type)`=`STACK_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute interconnects attachments partner create` is used to
create partner interconnect attachments. A partner interconnect attachment binds
the underlying connectivity of a provider's Interconnect to a path into and out
of the customer's cloud network.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the interconnect attachment to create.

**REQUIRED FLAGS**

: **--edge-availability-domain**:
Desired edge availability domain for this attachment:
`availability-domain-1`, `availability-domain-2`,
`any`.
In each metro where the Partner can connect to Google, there are two sets of
redundant hardware. These sets are described as edge availability domain 1 and
2. Within a metro, Google will only schedule maintenance in one availability
domain at a time. This guarantee does not apply to availability domains outside
the metro; Google may perform maintenance in (say) New York availability domain
1 at the same time as Chicago availability domain 1.
`AVAILABILITY_DOMAIN` must be one of:

**`any`**:
Any Availability Domain

**`availability-domain-1`**:
Edge Availability Domain 1

**`availability-domain-2`**:
Edge Availability Domain 2

**--router**:
The Google Cloud Router to use for dynamic routing.

**OPTIONAL FLAGS**

: **--description**:
Human-readable plain-text description of attachment.

**--enable-admin**:
Administrative status of the interconnect attachment. If not provided on
creation, defaults to disabled. When this is enabled, the attachment is
operational and will carry traffic. Use --no-enable-admin to disable it.

**--encryption**:
Indicates the user-supplied encryption option for this interconnect attachment
(VLAN attachment).
Possible values are:
`NONE` - This is the default value, which means the interconnect
attachment carries unencrypted traffic. VMs can send traffic to or receive
traffic from such interconnect attachment.
`IPSEC` - The interconnect attachment carries only traffic that is
encrypted by an IPsec device; for example, an HA VPN gateway or third-party
IPsec VPN. VMs cannot directly send traffic to or receive traffic from such an
interconnect attachment. To use HA VPN over Cloud Interconnect, the interconnect
attachment must be created with this option.
`ENCRYPTION` must be one of: `IPSEC`,
`NONE`.

**--ipsec-internal-addresses**:
List of IP address range names that have been reserved for the interconnect
attachment (VLAN attachment). Use this option only for an interconnect
attachment that has its encryption option set as IPSEC. Currently only one
internal IP address range can be specified for each attachment. When creating an
HA VPN gateway for the interconnect attachment, if the attachment is configured
to use a regional internal IP address, then the VPN gateway's IP address is
allocated from the IP address range specified here. If this field is not
specified when creating the interconnect attachment, then when creating any HA
VPN gateways for this interconnect attachment, the HA VPN gateway's IP address
is allocated from a regional external IP address pool.

**--mtu**:
Maximum transmission unit (MTU) is the size of the largest IP packet passing
through this interconnect attachment. Must be one of 1440, 1460, 1500, or 8896.
If not specified, the value will default to 1440.

**--region**:
Region of the interconnect attachment to create. If not specified, you might be
prompted to select a region (interactive mode only).
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

**--stack-type**:
Stack type of the protocol(s) enabled on this interconnect attachment.
`STACK_TYPE` must be one of:

**`IPV4_IPV6`**:
Both IPv4 and IPv6 protocols are enabled on this attachment.

**`IPV4_ONLY`**:
Only IPv4 protocol is enabled on this attachment.

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
gcloud alpha compute interconnects attachments partner create
```

```
gcloud beta compute interconnects attachments partner create
```