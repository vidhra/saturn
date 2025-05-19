# gcloud compute security-policies rules describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/describe](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/describe)*

**NAME**

: **gcloud compute security-policies rules describe - describe a Compute Engine security policy rule**

**SYNOPSIS**

: **`gcloud compute security-policies rules describe` `[PRIORITY](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/describe#PRIORITY)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/describe#--region)`=`REGION`] [`[--security-policy](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/describe#--security-policy)`=`SECURITY_POLICY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute security-policies rules describe` displays all data
associated with a security policy rule.

**EXAMPLES**

: To describe the rule at priority 1000, run:

```
gcloud compute security-policies rules describe 1000 --security-policy=my-policy
```

**POSITIONAL ARGUMENTS**

: **`PRIORITY`**:
The priority of the rule to describe. Rules are evaluated in order from highest
priority to lowest priority where 0 is the highest priority and 2147483647 is
the lowest priority.

**FLAGS**

: **--region**:
Region of the security policy to describe. If not specified, you might be
prompted to select a region (interactive mode only).
A list of regions can be fetched by running:

```
gcloud compute regions list
```

Overrides the default `compute/region` property value for this
command invocation.

**--security-policy**:
The security policy that this rule belongs to.

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
gcloud alpha compute security-policies rules describe
```

```
gcloud beta compute security-policies rules describe
```