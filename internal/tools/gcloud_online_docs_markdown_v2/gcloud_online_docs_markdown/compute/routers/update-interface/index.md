# gcloud compute routers update-interface  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-interface](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-interface)*

**NAME**

: **gcloud compute routers update-interface - update an interface on a Compute Engine router**

**SYNOPSIS**

: **`gcloud compute routers update-interface` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-interface#NAME)` `[--interface-name](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-interface#--interface-name)`=`INTERFACE_NAME` [`[--ip-address](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-interface#--ip-address)`=`IP_ADDRESS`] [`[--ip-version](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-interface#--ip-version)`=`IP_VERSION`] [`[--mask-length](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-interface#--mask-length)`=`MASK_LENGTH`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-interface#--region)`=`REGION`] [`[--interconnect-attachment](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-interface#--interconnect-attachment)`=`INTERCONNECT_ATTACHMENT`     | `[--interconnect-attachment-region](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-interface#--interconnect-attachment-region)`=`INTERCONNECT_ATTACHMENT_REGION`     | `[--vpn-tunnel](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-interface#--vpn-tunnel)`=`VPN_TUNNEL`     | `[--vpn-tunnel-region](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-interface#--vpn-tunnel-region)`=`VPN_TUNNEL_REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-interface#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute routers update-interface` is used to update an
interface on a Compute Engine router.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the router to update.

**REQUIRED FLAGS**

: **--interface-name**:
The name of the interface being updated.

**OPTIONAL FLAGS**

: **--ip-address**:
The link local (IPv4) or ULA (IPv6) address of the router for this interface.

**--ip-version**:
IP version of the interface. Possible values are IPV4 and IPV6. Defaults to
IPV4. `IP_VERSION` must be one of:

**`IPV4`**:
Interface with IPv4-based BGP.

**`IPV6`**:
Interface with IPv6-based BGP.

**--mask-length**:
The subnet mask for the IP range of the interface. The interface IP address and
BGP peer IP address must be selected from the subnet defined by this range.

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

**--interconnect-attachment**

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
gcloud alpha compute routers update-interface
```

```
gcloud beta compute routers update-interface
```