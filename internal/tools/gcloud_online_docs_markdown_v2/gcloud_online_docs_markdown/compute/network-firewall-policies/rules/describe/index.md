# gcloud compute network-firewall-policies rules describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/rules/describe](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/rules/describe)*

**NAME**

: **gcloud compute network-firewall-policies rules describe - describes a Compute Engine network firewall policy rule**

**SYNOPSIS**

: **`gcloud compute network-firewall-policies rules describe` `[PRIORITY](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/rules/describe#PRIORITY)` `[--firewall-policy](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/rules/describe#--firewall-policy)`=`FIREWALL_POLICY` [`[--firewall-policy-region](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/rules/describe#--firewall-policy-region)`=`FIREWALL_POLICY_REGION`     | `[--global-firewall-policy](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/rules/describe#--global-firewall-policy)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/rules/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute network-firewall-policies rules describe` is used to
describe network firewall policy rules.

**EXAMPLES**

: To describe a rule with priority ``10`` in a
global network firewall policy with name
``my-policy``, run:

```
gcloud compute network-firewall-policies rules describe 10 --firewall-policy=my-policy --global-firewall-policy
```

To describe a rule with priority ``10`` in a
regional network firewall policy with name
``my-policy``, in region
``region-a``, run:

```
gcloud compute network-firewall-policies rules describe 10 --firewall-policy=my-policy --firewall-policy-region=region-a
```

**POSITIONAL ARGUMENTS**

: **`PRIORITY`**:
Priority of the rule to be described. Valid in [0, 65535].

**REQUIRED FLAGS**

: **--firewall-policy**:
Firewall policy ID with which to describe rule.

**OPTIONAL FLAGS**

: **--firewall-policy-region**

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
gcloud alpha compute network-firewall-policies rules describe
```

```
gcloud beta compute network-firewall-policies rules describe
```