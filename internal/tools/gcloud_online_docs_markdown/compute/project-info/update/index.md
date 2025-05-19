# gcloud compute project-info update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/project-info/update](https://cloud.google.com/sdk/gcloud/reference/compute/project-info/update)*

**NAME**

: **gcloud compute project-info update - update a Compute Engine project resource**

**SYNOPSIS**

: **`gcloud compute project-info update` [`[--cloud-armor-tier](https://cloud.google.com/sdk/gcloud/reference/compute/project-info/update#--cloud-armor-tier)`=`CLOUD_ARMOR_TIER`] [`[--default-network-tier](https://cloud.google.com/sdk/gcloud/reference/compute/project-info/update#--default-network-tier)`=`DEFAULT_NETWORK_TIER`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/project-info/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute project-info update` is used to update a Compute
Engine project resource.

**FLAGS**

: **--cloud-armor-tier**:
Cloud armor tier to assign to the project.
`CLOUD_ARMOR_TIER` must be one of:
`CA_STANDARD`, `CA_ENTERPRISE_PAYGO`,
`CA_ENTERPRISE_ANNUAL`.

**--default-network-tier**:
The default network tier to assign to the project.
`DEFAULT_NETWORK_TIER` must be one of:
`PREMIUM`, `STANDARD`.

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
gcloud alpha compute project-info update
```

```
gcloud beta compute project-info update
```