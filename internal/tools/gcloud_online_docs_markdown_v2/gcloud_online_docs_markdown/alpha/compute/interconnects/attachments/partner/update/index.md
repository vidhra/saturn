# gcloud alpha compute interconnects attachments partner update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/partner/update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/partner/update)*

**NAME**

: **gcloud alpha compute interconnects attachments partner update - update a Compute Engine partner interconnect attachment**

**SYNOPSIS**

: **`gcloud alpha compute interconnects attachments partner update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/partner/update#NAME)` [`[--candidate-cloud-router-ipv6-address](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/partner/update#--candidate-cloud-router-ipv6-address)`=`CANDIDATE_CLOUD_ROUTER_IPV6_ADDRESS`] [`[--candidate-customer-router-ipv6-address](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/partner/update#--candidate-customer-router-ipv6-address)`=`CANDIDATE_CUSTOMER_ROUTER_IPV6_ADDRESS`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/partner/update#--description)`=`DESCRIPTION`] [`[--enable-admin](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/partner/update#--enable-admin)`] [`[--mtu](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/partner/update#--mtu)`=`MTU`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/partner/update#--region)`=`REGION`] [`[--stack-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/partner/update#--stack-type)`=`STACK_TYPE`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/partner/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/partner/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/partner/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/partner/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute interconnects attachments
partner update` is used to update partner interconnect attachments. A
partner interconnect attachment binds the underlying connectivity of a
provider's Interconnect to a path into and out of the customer's cloud network.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the interconnect attachment to patch.

**FLAGS**

: **--candidate-cloud-router-ipv6-address**:
Single IPv6 address + prefix length to be configured on the cloud router
interface for this interconnect attachment. Example:
2fff:eec0:3201:0:0:0:0:1/125

**--candidate-customer-router-ipv6-address**:
Single IPv6 address + prefix length to be configured on the customer router
interface for this interconnect attachment. Example:
2fff:eec0:3201:0:0:0:0:2/125

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

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

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
gcloud compute interconnects attachments partner update
```

```
gcloud beta compute interconnects attachments partner update
```