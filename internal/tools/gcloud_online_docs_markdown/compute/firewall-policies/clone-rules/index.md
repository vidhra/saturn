# gcloud compute firewall-policies clone-rules  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/clone-rules](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/clone-rules)*

**NAME**

: **gcloud compute firewall-policies clone-rules - replace the rules of a Compute Engine organization firewall policy with rules from another policy**

**SYNOPSIS**

: **`gcloud compute firewall-policies clone-rules` `[FIREWALL_POLICY](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/clone-rules#FIREWALL_POLICY)` `[--source-firewall-policy](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/clone-rules#--source-firewall-policy)`=`SOURCE_FIREWALL_POLICY` [`[--organization](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/clone-rules#--organization)`=`ORGANIZATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/clone-rules#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute firewall-policies clone-rules` is used to replace the
rules of organization firewall policies. An organization firewall policy is a
set of rules that controls access to various resources.

**EXAMPLES**

: To clone the rules of an organization firewall policy with ID ``123456789", from
another organization firewall policy with ID ``987654321", run:

```
gcloud compute firewall-policies clone-rules 123456789 --source-firewall-policy=987654321
```

**POSITIONAL ARGUMENTS**

: **`FIREWALL_POLICY`**:
Short name or ID of the firewall policy to clone the rules to.

**REQUIRED FLAGS**

: **--source-firewall-policy**:
The URL of the source firewall policy to copy the rules from.

**OPTIONAL FLAGS**

: **--organization**:
Organization in which the organization firewall policy to copy the rules to.
Must be set if firewall-policy is short name.

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

: To clone rules to a firewall policy, the user must have the following
permission: ``compute.firewallPolicies.cloneRules`.
To find predefined roles that contain those permissions, see the [Compute Engine IAM
roles](https://cloud.google.com/compute/docs/access/iam).`

**NOTES**

: These variants are also available:

```
gcloud alpha compute firewall-policies clone-rules
```

```
gcloud beta compute firewall-policies clone-rules
```