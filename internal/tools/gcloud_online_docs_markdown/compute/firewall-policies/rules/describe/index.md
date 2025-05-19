# gcloud compute firewall-policies rules describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/rules/describe](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/rules/describe)*

**NAME**

: **gcloud compute firewall-policies rules describe - describes a Compute Engine organization firewall policy rule**

**SYNOPSIS**

: **`gcloud compute firewall-policies rules describe` `[PRIORITY](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/rules/describe#PRIORITY)` `[--firewall-policy](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/rules/describe#--firewall-policy)`=`FIREWALL_POLICY` [`[--organization](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/rules/describe#--organization)`=`ORGANIZATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/rules/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute firewall-policies rules describe` is used to describe
organization firewall policy rules.

**EXAMPLES**

: To describe a rule with priority ``10" in an organization firewall policy with
ID ``123456789", run:

```
gcloud compute firewall-policies rules describe 10 --firewall-policy=123456789
```

**POSITIONAL ARGUMENTS**

: **`PRIORITY`**:
Priority of the firewall policy rule to describe.

**REQUIRED FLAGS**

: **--firewall-policy**:
Short name of the firewall policy into which the rule should be described.

**OPTIONAL FLAGS**

: **--organization**:
Organization which the organization firewall policy belongs to. Must be set if
FIREWALL_POLICY is short name.

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
gcloud alpha compute firewall-policies rules describe
```

```
gcloud beta compute firewall-policies rules describe
```