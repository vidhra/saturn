# gcloud asset analyze-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy)*

**NAME**

: **gcloud asset analyze-iam-policy - analyzes IAM policies that match a request**

**SYNOPSIS**

: **`gcloud asset analyze-iam-policy` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy#--project)`=`PROJECT_ID`) [`[--access-time](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy#--access-time)`=`ACCESS_TIME`] [`[--full-resource-name](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy#--full-resource-name)`=`FULL_RESOURCE_NAME`] [`[--identity](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy#--identity)`=`IDENTITY`] [`[--saved-analysis-query](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy#--saved-analysis-query)`=`SAVED_ANALYSIS_QUERY`] [`[--analyze-service-account-impersonation](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy#--analyze-service-account-impersonation)` `[--execution-timeout](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy#--execution-timeout)`=`EXECUTION_TIMEOUT` `[--expand-groups](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy#--expand-groups)` `[--expand-resources](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy#--expand-resources)` `[--expand-roles](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy#--expand-roles)` `[--output-group-edges](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy#--output-group-edges)` `[--output-resource-edges](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy#--output-resource-edges)` `[--show-response](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy#--show-response)`] [`[--permissions](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy#--permissions)`=[`PERMISSIONS`,…] `[--roles](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy#--roles)`=[`ROLES`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Analyzes IAM policies that match a request.

**EXAMPLES**

: To find out which users have been granted the iam.serviceAccounts.actAs
permission on a service account, run:

```
gcloud asset analyze-iam-policy --organization=YOUR_ORG_ID --full-resource-name=YOUR_SERVICE_ACCOUNT_FULL_RESOURCE_NAME --permissions='iam.serviceAccounts.actAs'
```

To find out which resources a user can access, run:

```
gcloud asset analyze-iam-policy --organization=YOUR_ORG_ID --identity='user:u1@foo.com'
```

To find out which roles or permissions a user has been granted on a project,
run:

```
gcloud asset analyze-iam-policy --organization=YOUR_ORG_ID --full-resource-name=YOUR_PROJECT_FULL_RESOURCE_NAME --identity='user:u1@foo.com'
```

To find out which users have been granted the iam.serviceAccounts.actAs
permission on any applicable resources, run:

```
gcloud asset analyze-iam-policy --organization=YOUR_ORG_ID --permissions='iam.serviceAccounts.actAs'
```

**REQUIRED FLAGS**

: **--folder**

**OPTIONAL FLAGS**

: **--access-time**

**--full-resource-name**

**--identity**

**--saved-analysis-query**

**--analyze-service-account-impersonation**

**--permissions**

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
gcloud alpha asset analyze-iam-policy
```

```
gcloud beta asset analyze-iam-policy
```