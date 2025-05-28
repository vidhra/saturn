# gcloud resource-manager org-policies delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/delete](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/delete)*

**NAME**

: **gcloud resource-manager org-policies delete - delete an Organization Policy**

**SYNOPSIS**

: **`gcloud resource-manager org-policies delete` `[ORG_POLICY_ID](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/delete#ORG_POLICY_ID)` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/delete#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/delete#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/delete#--project)`=`PROJECT_ID`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Deletes an Organization Policy associated with the specified resource.

**EXAMPLES**

: The following command clears an Organization Policy for constraint
`serviceuser.services` on project `foo-project`:

```
gcloud resource-manager org-policies delete serviceuser.services --project=foo-project
```

**POSITIONAL ARGUMENTS**

: **`ORG_POLICY_ID`**:
The Org Policy constraint name.

**REQUIRED FLAGS**

: **--folder**

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
gcloud alpha resource-manager org-policies delete
```

```
gcloud beta resource-manager org-policies delete
```