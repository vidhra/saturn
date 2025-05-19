# gcloud alpha compute interconnects groups create-members  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/create-members](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/create-members)*

**NAME**

: **gcloud alpha compute interconnects groups create-members - create new member interconnects in a Compute Engine interconnect group**

**SYNOPSIS**

: **`gcloud alpha compute interconnects groups create-members` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/create-members#NAME)` `[--interconnect](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/create-members#--interconnect)`=[`INTERCONNECT`,…] [`[--admin-enabled](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/create-members#--admin-enabled)`] [`[--customer-name](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/create-members#--customer-name)`=`CUSTOMER_NAME`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/create-members#--description)`=`DESCRIPTION`] [`[--facility](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/create-members#--facility)`=`FACILITY`] [`[--intent-mismatch-behavior](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/create-members#--intent-mismatch-behavior)`=`INTENT_MISMATCH_BEHAVIOR`] [`[--interconnect-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/create-members#--interconnect-type)`=`INTERCONNECT_TYPE`] [`[--link-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/create-members#--link-type)`=`LINK_TYPE`] [`[--noc-contact-email](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/create-members#--noc-contact-email)`=`NOC_CONTACT_EMAIL`] [`[--requested-features](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/create-members#--requested-features)`=[`FEATURES`,…]] [`[--requested-link-count](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/create-members#--requested-link-count)`=`REQUESTED_LINK_COUNT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/create-members#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute interconnects groups
create-members` is used to create new member interconnects in an
interconnect group.
For an example, refer to the `EXAMPLES` section below.

**EXAMPLES**

: To create interconnects interconnect1 and interconnect2 in interconnect group
example-interconnect-group, run:

```
gcloud alpha compute interconnects groups create-members example-interconnect-group --interconnect-type=DEDICATED --link-type=LINK_TYPE_ETHERNET_10G_LR --requested-link-count=1 --facility=iad-1 --interconnect="name=interconnect1" --interconnect="name=interconnect2"
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the interconnect group to create members.

**REQUIRED FLAGS**

: **--interconnect**:
New member interconnects to create in the interconnect group. To create multiple
interconnects, this flag should be specified multiple times.
Each interconnect takes in the same set of flags as the `gcloud compute
interconnects create` command, except instead of a location, a facility
must be specified. These flags are defined as a comma separated list of
flag=value pairs.
Example: --interconnect name=interconnect1,facility=iad-1,description="my
interconnect",link-type=LINK_TYPE_ETHERNET_10G_LR,requested-link-count=1,
interconnect-type=DEDICATED,admin-enabled,
noc-contact-email=noc@google.com,customer-name=customer-name
requested-features=MACSEC:CROSS_SITE_NETWORK
Note that for multiple requested-features, use a colon (:) as the delimiter, as
the comma is used to separate the flags. Similarly, if you need to use a comma
in another flag value, you should set an alternative delimiter for the
--interconnect flag. Run `[gcloud topic escaping](https://cloud.google.com/sdk/gcloud/reference/topic/escaping)` for
more information.

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

**--facility**:
The facility (zone free location) to create the interconnect in.

**--intent-mismatch-behavior**:
The behavior when the intent of the interconnect group does not match the
topology capability of the member interconnects.
`INTENT_MISMATCH_BEHAVIOR` must be one of:
`REJECT`, `CREATE`.

**--interconnect-type**:
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

**--noc-contact-email**:
Email address to contact the customer NOC for operations and maintenance
notifications regarding this interconnect.

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

**--requested-link-count**:
Target number of physical links in the link bundle.

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
allowlist. These variants are also available:

```
gcloud compute interconnects groups create-members
```

```
gcloud beta compute interconnects groups create-members
```