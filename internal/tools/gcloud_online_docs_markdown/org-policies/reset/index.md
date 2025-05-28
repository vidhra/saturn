# gcloud org-policies reset  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/org-policies/reset](https://cloud.google.com/sdk/gcloud/reference/org-policies/reset)*

**NAME**

: **gcloud org-policies reset - reset the policy to the default for the constraint**

**SYNOPSIS**

: **`gcloud org-policies reset` `[CONSTRAINT](https://cloud.google.com/sdk/gcloud/reference/org-policies/reset#CONSTRAINT)` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/org-policies/reset#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/org-policies/reset#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/org-policies/reset#--project)`=`PROJECT_ID`) [`[--update-mask](https://cloud.google.com/sdk/gcloud/reference/org-policies/reset#--update-mask)`=`UPDATE_MASK`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/org-policies/reset#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Resets the policy to the default for the constraint.

**EXAMPLES**

: To reset the policy associated with the constraint 'gcp.resourceLocations' and
the Project 'foo-project', run:

```
gcloud org-policies reset gcp.resourceLocations --project=foo-project
```

**POSITIONAL ARGUMENTS**

: **`CONSTRAINT`**:
Name of the org policy constraint. The list of available constraints can be
found here: [https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints)

**REQUIRED FLAGS**

: **--folder**

**OPTIONAL FLAGS**

: **--update-mask**:
Field mask used to specify the fields to be overwritten in the policy by the
set. The fields specified in the update_mask are relative to the policy, not the
full request. The update-mask flag can be empty, or have values
`policy.spec`, `policy.dry_run_spec` or `*`. If
the policy does not contain the dry_run_spec and update-mask flag is not
provided, then it defaults to `policy.spec`.

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