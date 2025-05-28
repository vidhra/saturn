# gcloud compute firewall-policies associations delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/associations/delete](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/associations/delete)*

**NAME**

: **gcloud compute firewall-policies associations delete - delete a Compute Engine organization firewall policy association**

**SYNOPSIS**

: **`gcloud compute firewall-policies associations delete` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/associations/delete#NAME)` `[--firewall-policy](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/associations/delete#--firewall-policy)`=`FIREWALL_POLICY` [`[--organization](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/associations/delete#--organization)`=`ORGANIZATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/associations/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute firewall-policies associations delete` is used to
delete organization firewall policy association.

**EXAMPLES**

: To delete an association with name ``example-association" of an organization
firewall policy with ID ``123456789", run:

```
gcloud compute firewall-policies associations delete example-association --firewall-policy=123456789
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the association to delete.

**REQUIRED FLAGS**

: **--firewall-policy**:
Short name or ID of the firewall policy ID of the association.

**OPTIONAL FLAGS**

: **--organization**:
ID of the organization in which the firewall policy is to be detached. Must be
set if FIREWALL_POLICY is short name.

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
gcloud alpha compute firewall-policies associations delete
```

```
gcloud beta compute firewall-policies associations delete
```