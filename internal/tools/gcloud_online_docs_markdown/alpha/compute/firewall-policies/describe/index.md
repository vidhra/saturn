# gcloud alpha compute firewall-policies describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/describe)*

**NAME**

: **gcloud alpha compute firewall-policies describe - describe a Compute Engine organization firewall policy**

**SYNOPSIS**

: **`gcloud alpha compute firewall-policies describe` `[FIREWALL_POLICY](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/describe#FIREWALL_POLICY)` [`[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/describe#--organization)`=`ORGANIZATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute firewall-policies
describe` is used to describe organization firewall policies. An
organization firewall policy is a set of rules that controls access to various
resources.

**EXAMPLES**

: To describe an organization firewall policy with ID ``123456789", run:

```
gcloud alpha compute firewall-policies describe 123456789
```

**POSITIONAL ARGUMENTS**

: **`FIREWALL_POLICY`**:
Short name or ID of the firewall policy to describe.

**FLAGS**

: **--organization**:
Organization in which the organization firewall policy is to be described. Must
be set if FIREWALL_POLICY is short name.

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

: To describe a firewall policy, the user must have the following permission:
``compute.firewallPolicies.get`.
To find predefined roles that contain those permissions, see the [Compute Engine IAM
roles](https://cloud.google.com/compute/docs/access/iam).`

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute firewall-policies describe
```

```
gcloud beta compute firewall-policies describe
```