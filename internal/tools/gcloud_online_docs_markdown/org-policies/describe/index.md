# gcloud org-policies describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/org-policies/describe](https://cloud.google.com/sdk/gcloud/reference/org-policies/describe)*

**NAME**

: **gcloud org-policies describe - describe an organization policy**

**SYNOPSIS**

: **`gcloud org-policies describe` `[CONSTRAINT](https://cloud.google.com/sdk/gcloud/reference/org-policies/describe#CONSTRAINT)` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/org-policies/describe#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/org-policies/describe#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/org-policies/describe#--project)`=`PROJECT_ID`) [`[--effective](https://cloud.google.com/sdk/gcloud/reference/org-policies/describe#--effective)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/org-policies/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describes an organization policy.

**EXAMPLES**

: To describe the policy associated with the constraint 'gcp.resourceLocations'
and the Project 'foo-project', run:

```
gcloud org-policies describe gcp.resourceLocations --project=foo-project
```

**POSITIONAL ARGUMENTS**

: **`CONSTRAINT`**:
Name of the org policy constraint. The list of available constraints can be
found here: [https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints)

**REQUIRED FLAGS**

: **--folder**

**OPTIONAL FLAGS**

: **--effective**:
Describe the effective policy.

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