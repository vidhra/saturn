# gcloud compute interconnects attachments partner update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/update](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/update)*

**NAME**

: **gcloud compute interconnects attachments partner update - update a Compute Engine partner interconnect attachment**

**SYNOPSIS**

: **`gcloud compute interconnects attachments partner update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/update#NAME)` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/update#--description)`=`DESCRIPTION`] [`[--enable-admin](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/update#--enable-admin)`] [`[--mtu](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/update#--mtu)`=`MTU`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/update#--region)`=`REGION`] [`[--stack-type](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/update#--stack-type)`=`STACK_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute interconnects attachments partner update` is used to
update partner interconnect attachments. A partner interconnect attachment binds
the underlying connectivity of a provider's Interconnect to a path into and out
of the customer's cloud network.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the interconnect attachment to patch.

**FLAGS**

: **--description**:
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
gcloud alpha compute interconnects attachments partner update
```

```
gcloud beta compute interconnects attachments partner update
```