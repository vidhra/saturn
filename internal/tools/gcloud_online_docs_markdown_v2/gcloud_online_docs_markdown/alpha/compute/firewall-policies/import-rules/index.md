# gcloud alpha compute firewall-policies import-rules  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/import-rules](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/import-rules)*

**NAME**

: **gcloud alpha compute firewall-policies import-rules - import Compute Engine organization firewall policy rules**

**SYNOPSIS**

: **`gcloud alpha compute firewall-policies import-rules` `[FIREWALL_POLICY](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/import-rules#FIREWALL_POLICY)` [`[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/import-rules#--organization)`=`ORGANIZATION`] [`[--source](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/import-rules#--source)`=`SOURCE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/import-rules#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Imports Firewall Policy rules configuration from a file.

**EXAMPLES**

: Firewall Policy rules can be imported by running:

```
gcloud alpha compute firewall-policies import-rules FIREWALL_POLICY --source=<path-to-file> --organization=<organization>
```

**POSITIONAL ARGUMENTS**

: **`FIREWALL_POLICY`**:
Short name or ID of the firewall policy to imports rules to.

**FLAGS**

: **--organization**:
Organization in which the organization firewall policy rules import to. Must be
set if FIREWALL_POLICY is short name.

**--source**:
Path to a YAML file containing configuration export data. Alternatively, you may
omit this flag to read from standard input.For a schema describing the
export/import format, see:
$CLOUDSDKROOT/lib/googlecloudsdk/schemas/compute/alpha/FirewallPolicy.yaml.

```
Note: $CLOUDSDKROOT represents the Google Cloud CLI's installation directory.
```

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
allowlist. These variants are also available:

```
gcloud compute firewall-policies import-rules
```

```
gcloud beta compute firewall-policies import-rules
```