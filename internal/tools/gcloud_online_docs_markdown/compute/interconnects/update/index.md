# gcloud compute interconnects update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/update](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/update)*

**NAME**

: **gcloud compute interconnects update - update a Compute Engine interconnect**

**SYNOPSIS**

: **`gcloud compute interconnects update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/update#NAME)` [`[--admin-enabled](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/update#--admin-enabled)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/update#--description)`=`DESCRIPTION`] [`[--noc-contact-email](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/update#--noc-contact-email)`=`NOC_CONTACT_EMAIL`] [`[--requested-link-count](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/update#--requested-link-count)`=`REQUESTED_LINK_COUNT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute interconnects update` is used to update
interconnects. An interconnect represents a single specific connection between
Google and the customer.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the interconnect to update.

**FLAGS**

: **--admin-enabled**:
Administrative status of the interconnect. When this is enabled, the
interconnect is operational and will carry traffic across any functioning linked
interconnect attachments. Use --no-admin-enabled to disable it.

**--description**:
An optional, textual description for the interconnect.

**--noc-contact-email**:
Email address to contact the customer NOC for operations and maintenance
notifications regarding this interconnect.

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

: These variants are also available:

```
gcloud alpha compute interconnects update
```

```
gcloud beta compute interconnects update
```