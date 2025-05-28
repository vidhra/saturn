# gcloud resource-manager org-policies allow  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/allow](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/allow)*

**NAME**

: **gcloud resource-manager org-policies allow - add values to an Organization Policy allowed_values list policy**

**SYNOPSIS**

: **`gcloud resource-manager org-policies allow` `[ORG_POLICY_ID](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/allow#ORG_POLICY_ID)` `[ALLOWED_VALUE](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/allow#ALLOWED_VALUE)` [`[ALLOWED_VALUE](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/allow#ALLOWED_VALUE)` …] (`[--folder](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/allow#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/allow#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/allow#--project)`=`PROJECT_ID`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/allow#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Adds one or more values to the specified Organization Policy allowed_values list
policy associated with the specified resource.

**EXAMPLES**

: The following command adds `devEnv` and `prodEnv` to an
Organization Policy allowed_values list policy for constraint
`serviceuser.services` on project `foo-project`:

```
gcloud resource-manager org-policies allow serviceuser.services --project=foo-project devEnv prodEnv
```

**POSITIONAL ARGUMENTS**

: **`ORG_POLICY_ID`**:
The Org Policy constraint name.

**`ALLOWED_VALUE` [`ALLOWED_VALUE` …]**:
The values to add to the allowed_values list policy.

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
gcloud alpha resource-manager org-policies allow
```

```
gcloud beta resource-manager org-policies allow
```