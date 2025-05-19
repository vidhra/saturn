# gcloud alpha compute firewall-policies move  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/move](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/move)*

**NAME**

: **gcloud alpha compute firewall-policies move - move a Compute Engine organization firewall policy**

**SYNOPSIS**

: **`gcloud alpha compute firewall-policies move` `[FIREWALL_POLICY](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/move#FIREWALL_POLICY)` [`[--folder](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/move#--folder)`=`FOLDER`] [`[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/move#--organization)`=`ORGANIZATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/move#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute firewall-policies move` is
used to move is used to move organization firewall policies to new parent nodes.

**EXAMPLES**

: To move an organization firewall policy under folder with ID ``123456789" to
folder ``987654321", run:

```
gcloud alpha compute firewall-policies move 123456789 --folder=987654321
```

**POSITIONAL ARGUMENTS**

: **`FIREWALL_POLICY`**:
Short name or ID of the firewall policy to move.

**FLAGS**

: **--folder**:
Folder to which the organization firewall policy is to be moved.

**--organization**:
Organization in which the organization firewall policy is to be moved. Must be
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

**IAM PERMISSIONS**

: To move a firewall policy, the user must have the following permission:
``compute.firewallPolicies.move`.
To find predefined roles that contain those permissions, see the [Compute Engine IAM
roles](https://cloud.google.com/compute/docs/access/iam).`

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute firewall-policies move
```

```
gcloud beta compute firewall-policies move
```