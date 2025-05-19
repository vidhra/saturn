# gcloud compute routers update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/routers/update](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update)*

**NAME**

: **gcloud compute routers update - update a Compute Engine router**

**SYNOPSIS**

: **`gcloud compute routers update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update#NAME)` [`[--advertisement-mode](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update#--advertisement-mode)`=`MODE`] [`[--asn](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update#--asn)`=`ASN`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update#--async)`] [`[--bgp-identifier-range](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update#--bgp-identifier-range)`=`BGP_IDENTIFIER_RANGE`] [`[--keepalive-interval](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update#--keepalive-interval)`=`KEEPALIVE_INTERVAL`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update#--region)`=`REGION`] [`[--set-advertisement-groups](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update#--set-advertisement-groups)`=[`GROUP`,…]] [`[--set-advertisement-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update#--set-advertisement-ranges)`=[`CIDR_RANGE`=`DESC`,…]] [`[--add-advertisement-groups](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update#--add-advertisement-groups)`=[`GROUP`,…]     | `[--add-advertisement-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update#--add-advertisement-ranges)`=[`CIDR_RANGE`=`DESC`,…]     | `[--remove-advertisement-groups](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update#--remove-advertisement-groups)`=[`GROUP`,…]     | `[--remove-advertisement-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update#--remove-advertisement-ranges)`=[`CIDR_RANGE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute routers update` is used to update a Compute Engine
router.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the router to update.

**FLAGS**

: **--advertisement-mode**:
The new advertisement mode for this router. `MODE` must be
one of:

**`CUSTOM`**:
Custom (user-configured) BGP advertisements.

**`DEFAULT`**:
Default (Google-managed) BGP advertisements.

**--asn**:
The optional BGP autonomous system number (ASN) for this router. Must be a
16-bit or 32-bit private ASN as defined in https://tools.ietf.org/html/rfc6996,
for example `--asn=64512`.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--bgp-identifier-range**:
The range of valid BGP Identifiers for this Router. Must be a link-local IPv4
range from 169.254.0.0/16, of size at least /30, even if the BGP sessions are
over IPv6. It must not overlap with any IPv4 BGP session ranges. This is
commonly called "router ID" by other vendors.

**--keepalive-interval**:
The interval between BGP keepalive messages that are sent to the peer. If set,
this value must be between 20 and 60 seconds. The default is 20 seconds. See $
[gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.
BGP systems exchange keepalive messages to determine whether a link or host has
failed or is no longer available. Hold time is the length of time in seconds
that the BGP session is considered operational without any activity. After the
hold time expires, the session is dropped.
Hold time is three times the interval at which keepalive messages are sent, and
the hold time is the maximum number of seconds allowed to elapse between
successive keepalive messages that BGP receives from a peer. BGP will use the
smaller of either the local hold time value or the peer's hold time value as the
hold time for the BGP connection between the two peers.

**--region**:
Region of the router to update. If not specified, you might be prompted to
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
router. This list can only be specified in custom advertisement mode.
`GROUP` must be (only one value is supported):

**`ALL_SUBNETS`**:
Automatically advertise all available subnets. This excludes any routes learned
for subnets that use VPC Network Peering.

**--set-advertisement-ranges**:
The list of individual IP ranges, in CIDR format, to dynamically advertise on
this router. Each IP range can (optionally) be given a text description DESC.
For example, to advertise a specific range, use
`--set-advertisement-ranges=192.168.10.0/24`. To store a description
with the range, use
`--set-advertisement-ranges=192.168.10.0/24=my-networks`. This list
can only be specified in custom advertisement mode.

**--add-advertisement-groups**

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
gcloud alpha compute routers update
```

```
gcloud beta compute routers update
```