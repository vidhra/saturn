# gcloud compute firewall-policies delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/delete](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/delete)*

**NAME**

: **gcloud compute firewall-policies delete - delete a Compute Engine organization firewall policy**

**SYNOPSIS**

: **`gcloud compute firewall-policies delete` `[FIREWALL_POLICY](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/delete#FIREWALL_POLICY)` [`[--organization](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/delete#--organization)`=`ORGANIZATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute firewall-policies delete` is used to delete
organization firewall policies. An organization firewall policy is a set of
rules that controls access to various resources.

**EXAMPLES**

: To delete an organization firewall policy with ID ``123456789", run:

```
gcloud compute firewall-policies delete 123456789
```

**POSITIONAL ARGUMENTS**

: **`FIREWALL_POLICY`**:
Short name or ID of the firewall policy to delete.

**FLAGS**

: **--organization**:
Organization in which the organization firewall policy is to be deleted. Must be
set if FIREWALL_POLICY is the short name.

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

**IAM PERMISSIONS**

: To delete a firewall policy, the user must have the following permission:
``compute.firewallPolicies.delete`.
To find predefined roles that contain those permissions, see the [Compute Engine IAM
roles](https://cloud.google.com/compute/docs/access/iam).`

**NOTES**

: These variants are also available:

```
gcloud alpha compute firewall-policies delete
```

```
gcloud beta compute firewall-policies delete
```