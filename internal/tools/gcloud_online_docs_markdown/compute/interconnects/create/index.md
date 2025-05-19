# gcloud compute interconnects create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/create](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/create)*

**NAME**

: **gcloud compute interconnects create - create a Compute Engine interconnect**

**SYNOPSIS**

: **`gcloud compute interconnects create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/create#NAME)` `[--interconnect-type](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/create#--interconnect-type)`=`INTERCONNECT_TYPE` `[--link-type](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/create#--link-type)`=`LINK_TYPE` `[--location](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/create#--location)`=`LOCATION` `[--requested-link-count](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/create#--requested-link-count)`=`REQUESTED_LINK_COUNT` [`[--admin-enabled](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/create#--admin-enabled)`] [`[--customer-name](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/create#--customer-name)`=`CUSTOMER_NAME`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/create#--description)`=`DESCRIPTION`] [`[--noc-contact-email](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/create#--noc-contact-email)`=`NOC_CONTACT_EMAIL`] [`[--remote-location](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/create#--remote-location)`=`REMOTE_LOCATION`] [`[--requested-features](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/create#--requested-features)`=[`FEATURES`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute interconnects create` is used to create
interconnects. An interconnect represents a single specific connection between
Google and the customer.
For an example, refer to the `EXAMPLES` section below.

**EXAMPLES**

: To create an interconnect of type DEDICATED, run:

```
gcloud compute interconnects create example-interconnect --customer-name="Example Customer Name" --interconnect-type=DEDICATED --link-type=LINK_TYPE_ETHERNET_10G_LR --location=example-zone1-1 --requested-link-count=1 --noc-contact-email=noc@example.com --description="Example interconnect"
```

To create a Cross-Cloud Interconnect, run:

```
gcloud compute interconnects create example-cc-interconnect --interconnect-type=DEDICATED --link-type=LINK_TYPE_ETHERNET_10G_LR --location=example-zone1-1 --requested-link-count=1 --remote-location=example-remote-location --noc-contact-email=noc@example.com --description="Example Cross-Cloud Interconnect"
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the interconnect to create.

**REQUIRED FLAGS**

: **--interconnect-type**:
Type of the interconnect. `INTERCONNECT_TYPE` must be one
of:

**`DEDICATED`**:
Dedicated private interconnect.

**`PARTNER`**:
Partner interconnect. Only available to approved partners.

**--link-type**:
Type of the link for the interconnect. `LINK_TYPE` must be
one of:

**`LINK_TYPE_ETHERNET_100G_LR`**:
100Gbps Ethernet, LR Optics.

**`LINK_TYPE_ETHERNET_10G_LR`**:
10Gbps Ethernet, LR Optics.

**`LINK_TYPE_ETHERNET_400G_LR4`**:
400Gbps Ethernet, LR4 Optics.

**--location**:
The location for the interconnect. The locations can be listed by using the
`[gcloud compute
interconnects locations list](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/locations/list)` command to find the appropriate location
to use when creating an interconnect.

**--requested-link-count**:
Target number of physical links in the link bundle.

**OPTIONAL FLAGS**

: **--admin-enabled**:
Administrative status of the interconnect. If not provided on creation, defaults
to enabled. When this is enabled, the interconnect is operational and will carry
traffic across any functioning linked interconnect attachments. Use
--no-admin-enabled to disable it.

**--customer-name**:
Customer name to put in the Letter of Authorization as the party authorized to
request an interconnect. This field is required for most interconnects, however
it is prohibited when creating a Cross-Cloud Interconnect.

**--description**:
An optional, textual description for the interconnect.

**--noc-contact-email**:
Email address to contact the customer NOC for operations and maintenance
notifications regarding this interconnect.

**--remote-location**:
The remote location for a Cross-Cloud Interconnect. The remote locations can be
listed by using the `[gcloud
compute interconnects remote-locations list](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/remote-locations/list)` command to find the
appropriate remote location to use when creating a Cross-Cloud Interconnect.

**--requested-features**:
List of features requested for this interconnect.
`FEATURES` must be one of:

**`CROSS_SITE_NETWORK`**:
If specified then the interconnect is created on Cross-Site Network capable
hardware ports. This parameter can only be provided during interconnect INSERT
and cannot be changed using interconnect PATCH.

**`MACSEC`**:
If specified then the interconnect is created on MACsec capable hardware ports.
If not specified, the interconnect is created on non-MACsec capable ports first,
if available. This parameter can only be provided during interconnect INSERT and
cannot be changed using interconnect PATCH.

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
gcloud alpha compute interconnects create
```

```
gcloud beta compute interconnects create
```