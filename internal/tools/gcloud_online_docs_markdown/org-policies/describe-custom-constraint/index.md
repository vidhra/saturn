# gcloud org-policies describe-custom-constraint  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/org-policies/describe-custom-constraint](https://cloud.google.com/sdk/gcloud/reference/org-policies/describe-custom-constraint)*

**NAME**

: **gcloud org-policies describe-custom-constraint - describe a custom constraint**

**SYNOPSIS**

: **`gcloud org-policies describe-custom-constraint` `[CUSTOM_CONSTRAINT](https://cloud.google.com/sdk/gcloud/reference/org-policies/describe-custom-constraint#CUSTOM_CONSTRAINT)` `[--organization](https://cloud.google.com/sdk/gcloud/reference/org-policies/describe-custom-constraint#--organization)`=`ORGANIZATION_ID` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/org-policies/describe-custom-constraint#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describes a custom constraint.

**EXAMPLES**

: To describe the custom constraint 'custom.myCustomConstraint' associated with
the Organization '1234', run:

```
gcloud org-policies describe-custom-constraint custom.myCustomConstraint --organization=1234
```

**POSITIONAL ARGUMENTS**

: **`CUSTOM_CONSTRAINT`**:
Name of the custom constraint.

**REQUIRED FLAGS**

: **--organization**:
Organization ID.

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