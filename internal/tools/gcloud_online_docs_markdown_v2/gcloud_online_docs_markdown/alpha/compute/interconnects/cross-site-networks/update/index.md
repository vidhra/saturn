# gcloud alpha compute interconnects cross-site-networks update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/cross-site-networks/update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/cross-site-networks/update)*

**NAME**

: **gcloud alpha compute interconnects cross-site-networks update - update a Compute Engine cross site network**

**SYNOPSIS**

: **`gcloud alpha compute interconnects cross-site-networks update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/cross-site-networks/update#NAME)` [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/cross-site-networks/update#--description)`=`DESCRIPTION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/cross-site-networks/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute interconnects
cross-site-networks update` is used to update cross site networks. A cross
site network encapsulates wire groups.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the crossSiteNetwork to update.

**FLAGS**

: **--description**:
An optional, textual description for the cross site network.

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
gcloud beta compute interconnects cross-site-networks update
```