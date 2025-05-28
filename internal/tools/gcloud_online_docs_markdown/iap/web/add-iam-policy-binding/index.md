# gcloud iap web add-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iap/web/add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/iap/web/add-iam-policy-binding)*

**NAME**

: **gcloud iap web add-iam-policy-binding - add IAM policy binding to an IAP IAM resource**

**SYNOPSIS**

: **`gcloud iap web add-iam-policy-binding` `[--member](https://cloud.google.com/sdk/gcloud/reference/iap/web/add-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/iap/web/add-iam-policy-binding#--role)`=`ROLE` [`[--condition](https://cloud.google.com/sdk/gcloud/reference/iap/web/add-iam-policy-binding#--condition)`=[`KEY`=`VALUE`,…]     | `[--condition-from-file](https://cloud.google.com/sdk/gcloud/reference/iap/web/add-iam-policy-binding#--condition-from-file)`=`PATH_TO_FILE`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/iap/web/add-iam-policy-binding#--region)`=`REGION` `[--resource-type](https://cloud.google.com/sdk/gcloud/reference/iap/web/add-iam-policy-binding#--resource-type)`=`RESOURCE_TYPE` `[--service](https://cloud.google.com/sdk/gcloud/reference/iap/web/add-iam-policy-binding#--service)`=`SERVICE` `[--version](https://cloud.google.com/sdk/gcloud/reference/iap/web/add-iam-policy-binding#--version)`=`VERSION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iap/web/add-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Adds a policy binding to the IAM policy of an IAP IAM resource. One binding
consists of a member, a role, and an optional condition. See $ [gcloud iap web
get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/iap/web/get-iam-policy) for examples of how to specify an IAP IAM resource.

**EXAMPLES**

: See $ [gcloud iap web
get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/iap/web/get-iam-policy) for examples of how to specify an IAP IAM resource.
To add an IAM policy binding for the role of 'roles/editor' for the user
'test-user@gmail.com' on IAP IAM resource IAP_IAM_RESOURCE, run:

```
gcloud iap web add-iam-policy-binding --resource-type=IAP_IAM_RESOURCE --member='user:test-user@gmail.com' --role='roles/editor'
```

To add an IAM policy binding for the role of 'roles/editor' for the user
'test-user@gmail.com' on regional IAP IAM resource IAP_IAM_RESOURCE, run:

```
gcloud iap web add-iam-policy-binding --resource-type=IAP_IAM_RESOURCE --member='user:test-user@gmail.com' --role='roles/editor' --region=REGION
```

To add an IAM policy binding for the role of 'roles/editor' for all
authenticated users on IAP IAM resource IAP_IAM_RESOURCE, run:

```
gcloud iap web add-iam-policy-binding --resource-type=IAP_IAM_RESOURCE --member='allAuthenticatedUsers' --role='roles/editor'
```

To add an IAM policy binding which expires at the end of the year 2018 for the
role of 'roles/browser' and the user 'test-user@gmail.com' on IAP IAM resource
IAP_IAM_RESOURCE, run:

```
gcloud iap web add-iam-policy-binding --resource-type=IAP_IAM_RESOURCE --member='user:test-user@gmail.com' --role='roles/browser' --condition='expression=request.time <
    timestamp("2019-01-01T00:00:00Z"),title=expires_end_of_2018,
    description=Expires at midnight on 2018-12-31'
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of policy role and member types.

**REQUIRED FLAGS**

: **--member**:
The principal to add the binding for. Should be of the form
`user|group|serviceAccount:email` or `domain:domain`.
Examples: `user:test-user@gmail.com`,
`group:admins@example.com`,
`serviceAccount:test123@example.domain.com`, or
`domain:example.domain.com`.
Some resources also accept the following special values:

- `allUsers` - Special identifier that represents anyone who is on the
internet, with or without a Google account.
- `allAuthenticatedUsers` - Special identifier that represents anyone
who is authenticated with a Google account or a service account.

**--role**:
Role name to assign to the principal. The role name is the complete path of a
predefined role, such as `roles/logging.viewer`, or the role ID for a
custom role, such as
`organizations/{ORGANIZATION_ID}/roles/logging.viewer`.

**OPTIONAL FLAGS**

: **--condition**

**--region**:
Region name. Should only be specified with
`--resource-type=backend-services` if it is a regional scoped. Not
applicable for global scoped backend services.

**--resource-type**:
Resource type of the IAP resource. `RESOURCE_TYPE` must be
one of: `app-engine`, `backend-services`,
`forwarding-rule`.

**--service**:
Service name.

**--version**:
Service version. Should only be specified with
`--resource-type=app-engine`.

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
gcloud alpha iap web add-iam-policy-binding
```

```
gcloud beta iap web add-iam-policy-binding
```