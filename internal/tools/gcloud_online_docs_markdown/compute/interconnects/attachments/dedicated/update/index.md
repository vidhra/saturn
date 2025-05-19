# gcloud compute interconnects attachments dedicated update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/update](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/update)*

**NAME**

: **gcloud compute interconnects attachments dedicated update - update a Compute Engine dedicated interconnect attachment**

**SYNOPSIS**

: **`gcloud compute interconnects attachments dedicated update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/update#NAME)` [`[--bandwidth](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/update#--bandwidth)`=`BANDWIDTH`] [`[--candidate-ipv6-subnets](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/update#--candidate-ipv6-subnets)`=[`IPV6_SUBNET`,…]] [`[--cloud-router-ipv6-interface-id](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/update#--cloud-router-ipv6-interface-id)`=`INTERFACE_ID`] [`[--customer-router-ipv6-interface-id](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/update#--customer-router-ipv6-interface-id)`=`PEER_INTERFACE_ID`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/update#--description)`=`DESCRIPTION`] [`[--enable-admin](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/update#--enable-admin)`] [`[--mtu](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/update#--mtu)`=`MTU`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/update#--region)`=`REGION`] [`[--stack-type](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/update#--stack-type)`=`STACK_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute interconnects attachments dedicated update` is used
to update interconnect attachments. An interconnect attachment is what binds the
underlying connectivity of an interconnect to a path into and out of the
customer's cloud network.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the interconnect attachment to patch.

**FLAGS**

: **--bandwidth**:
Provisioned capacity of the attachment. `BANDWIDTH` must
be one of:

**`50m`**:
50 Mbit/s

**`100m`**:
100 Mbit/s

**`200m`**:
200 Mbit/s

**`300m`**:
300 Mbit/s

**`400m`**:
400 Mbit/s

**`500m`**:
500 Mbit/s

**`1g`**:
1 Gbit/s

**`2g`**:
2 Gbit/s

**`5g`**:
5 Gbit/s

**`10g`**:
10 Gbit/s

**`20g`**:
20 Gbit/s

**`50g`**:
50 Gbit/s

**`100g`**:
100 Gbit/s

**--candidate-ipv6-subnets**:
The `candididate-ipv6-subnets` field is not available.

**--cloud-router-ipv6-interface-id**:
`cloud-router-ipv6-interface-id` field is not available.

**--customer-router-ipv6-interface-id**:
`customer-router-ipv6-interface-id` field is not available.

**--description**:
Human-readable plain-text description of attachment.

**--enable-admin**:
Administrative status of the interconnect attachment. When this is enabled, the
attachment is operational and will carry traffic. Use --no-enable-admin to
disable it.

**--mtu**:
Maximum transmission unit (MTU) is the size of the largest IP packet passing
through this interconnect attachment. Must be one of 1440, 1460, 1500, or 8896.
If not specified, the value will default to 1440.

**--region**:
Region of the interconnect attachment to patch. If not specified, you might be
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
gcloud alpha compute interconnects attachments dedicated update
```

```
gcloud beta compute interconnects attachments dedicated update
```