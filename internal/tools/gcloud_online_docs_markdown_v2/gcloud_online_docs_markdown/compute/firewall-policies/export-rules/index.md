# gcloud compute firewall-policies export-rules  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/export-rules](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/export-rules)*

**NAME**

: **gcloud compute firewall-policies export-rules - export Compute Engine organization firewall policy rules**

**SYNOPSIS**

: **`gcloud compute firewall-policies export-rules` `[FIREWALL_POLICY](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/export-rules#FIREWALL_POLICY)` [`[--destination](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/export-rules#--destination)`=`DESTINATION`] [`[--organization](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/export-rules#--organization)`=`ORGANIZATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/export-rules#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Exports Firewall Policy rules configuration to a file.

**EXAMPLES**

: Firewall Policy rules can be exported by running:

```
gcloud compute firewall-policies export-rules FIREWALL_POLICY --destination=<path-to-file> --organization=<organization>
```

**POSITIONAL ARGUMENTS**

: **`FIREWALL_POLICY`**:
Short name or ID of the firewall policy to export rules from.

**FLAGS**

: **--destination**:
Path to a YAML file where the configuration will be exported. Alternatively, you
may omit this flag to write to standard output. For a schema describing the
export/import format, see:
$CLOUDSDKROOT/lib/googlecloudsdk/schemas/compute/v1/FirewallPolicy.yaml.

**--organization**:
Organization in which the organization firewall policy rules export from. Must
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

**NOTES**

: These variants are also available:

```
gcloud alpha compute firewall-policies export-rules
```

```
gcloud beta compute firewall-policies export-rules
```