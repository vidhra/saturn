# gcloud alpha compute firewall-rules migrate  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-rules/migrate](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-rules/migrate)*

**NAME**

: **gcloud alpha compute firewall-rules migrate - create a new Network Firewall Policy and move all customer defined firewall rules there**

**SYNOPSIS**

: **`gcloud alpha compute firewall-rules migrate` `[--source-network](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-rules/migrate#--source-network)`=`SOURCE_NETWORK` (`[--bind-tags-to-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-rules/migrate#--bind-tags-to-instances)`     | `[--export-exclusion-patterns](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-rules/migrate#--export-exclusion-patterns)`     | `[--export-tag-mapping](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-rules/migrate#--export-tag-mapping)`     | `[--target-firewall-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-rules/migrate#--target-firewall-policy)`=`TARGET_FIREWALL_POLICY`) [`[--exclusion-patterns-file](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-rules/migrate#--exclusion-patterns-file)`=`EXCLUSION_PATTERNS_FILE`] [`[--export-terraform-script](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-rules/migrate#--export-terraform-script)`] [`[--force](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-rules/migrate#--force)`] [`[--skip-migrate-target-service-accounts-to-tags](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-rules/migrate#--skip-migrate-target-service-accounts-to-tags)`] [`[--tag-mapping-file](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-rules/migrate#--tag-mapping-file)`=`TAG_MAPPING_FILE`] [`[--terraform-script-output-file](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-rules/migrate#--terraform-script-output-file)`=`TERRAFORM_SCRIPT_OUTPUT_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-rules/migrate#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute firewall-rules migrate` is
used to create a new Network Firewall Policy that contain all rules defined in
already existing Network Firewall Policy associated with the given VPC Network
and all customer defined VPC Firewall Rules attached to that VPC Network.

**EXAMPLES**

: To execute the migration for VPC Network 'my-network' which stores the result in
'my-policy' Network Firewall Policy, run:

```
gcloud alpha compute firewall-rules migrate --source-network=my-network --target-firewall-policy=my-policy
```

**REQUIRED FLAGS**

: **--source-network**:
The VPC Network for which the migration should be performed.

**--bind-tags-to-instances**

**OPTIONAL FLAGS**

: **--exclusion-patterns-file**:
Path to a file with exclusion patterns used for VPC Firewall filtering. Each
regular expression describing a single firewall naming pattern must be placed in
a single line. No leading or tailing whitespaces.

**--export-terraform-script**:
If set, migration tool will output a terraform script to create a Firewall
Policy with migrated rules.

**--force**:
If set, migration will succeed even if the tool detects that original rule
evaluation order cannot be preserved.

**--skip-migrate-target-service-accounts-to-tags**:
If set, migration will keep target service accounts as they are and will not try
to replace them with secure tags.

**--tag-mapping-file**:
Path to a JSON file with legacy tags and service accounts to secure tags
mapping.

**--terraform-script-output-file**:
Path to a file where to store generated Terraform script.

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
gcloud beta compute firewall-rules migrate
```