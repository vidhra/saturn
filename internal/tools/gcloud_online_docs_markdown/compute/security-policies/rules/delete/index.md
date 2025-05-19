# gcloud compute security-policies rules delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/delete](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/delete)*

**NAME**

: **gcloud compute security-policies rules delete - delete Compute Engine security policy rules**

**SYNOPSIS**

: **`gcloud compute security-policies rules delete` [`[PRIORITY](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/delete#PRIORITY)` …] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/delete#--region)`=`REGION`] [`[--security-policy](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/delete#--security-policy)`=`SECURITY_POLICY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute security-policies rules delete` is used to delete
security policy rules.

**EXAMPLES**

: To delete the rule at priority 1000, run:

```
gcloud compute security-policies rules delete 1000 --security-policy=my-policy
```

**POSITIONAL ARGUMENTS**

: **[`PRIORITY` …]**:
The priority of the rules to delete. Rules are evaluated in order from highest
priority to lowest priority where 0 is the highest priority and 2147483647 is
the lowest priority.

**FLAGS**

: **--region**:
Region of the security policy to delete. If not specified, you might be prompted
to select a region (interactive mode only).
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
gcloud alpha compute security-policies rules delete
```

```
gcloud beta compute security-policies rules delete
```