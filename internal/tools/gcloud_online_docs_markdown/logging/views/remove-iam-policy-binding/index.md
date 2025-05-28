# gcloud logging views remove-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/views/remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/logging/views/remove-iam-policy-binding)*

**NAME**

: **gcloud logging views remove-iam-policy-binding - remove IAM policy binding to a log view**

**SYNOPSIS**

: **`gcloud logging views remove-iam-policy-binding` `[VIEW_ID](https://cloud.google.com/sdk/gcloud/reference/logging/views/remove-iam-policy-binding#VIEW_ID)` `[--bucket](https://cloud.google.com/sdk/gcloud/reference/logging/views/remove-iam-policy-binding#--bucket)`=`BUCKET` `[--location](https://cloud.google.com/sdk/gcloud/reference/logging/views/remove-iam-policy-binding#--location)`=`LOCATION` `[--member](https://cloud.google.com/sdk/gcloud/reference/logging/views/remove-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/logging/views/remove-iam-policy-binding#--role)`=`ROLE` [`[--all](https://cloud.google.com/sdk/gcloud/reference/logging/views/remove-iam-policy-binding#--all)`     | `[--condition](https://cloud.google.com/sdk/gcloud/reference/logging/views/remove-iam-policy-binding#--condition)`=[`KEY`=`VALUE`,…]     | `[--condition-from-file](https://cloud.google.com/sdk/gcloud/reference/logging/views/remove-iam-policy-binding#--condition-from-file)`=`PATH_TO_FILE`] [`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/logging/views/remove-iam-policy-binding#--billing-account)`=`BILLING_ACCOUNT_ID`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/logging/views/remove-iam-policy-binding#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/logging/views/remove-iam-policy-binding#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/logging/views/remove-iam-policy-binding#--project)`=`PROJECT_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/views/remove-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Remove IAM policy binding to a log view.

**EXAMPLES**

: To remove an IAM policy binding for the role 'roles/my-role' for the user
'my-user@gmail.com' on my-view, run:

```
gcloud logging views remove-iam-policy-binding my-view --member='user:my-user@gmail.com' --role='roles/my-role' --bucket=my-bucket --location=global
```

To remove a binding with a condition, run:

```
gcloud logging views remove-iam-policy-binding my-view --member='user:my-user@gmail.com' --role='roles/my-role' --bucket=my-bucket --location=global --condition=expression=[expression],title=[title],description=[description]
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details about IAM policies and member types.

**POSITIONAL ARGUMENTS**

: **`VIEW_ID`**:
ID of the view that contains the IAM policy.

**REQUIRED FLAGS**

: **--bucket**:
ID of the bucket that contains the view.

**--location**:
Location of the bucket that contains the view.

**--member**:
The principal to remove the binding for. Should be of the form
`user|group|serviceAccount:email` or `domain:domain`.
Examples: `user:test-user@gmail.com`,
`group:admins@example.com`,
`serviceAccount:test123@example.domain.com`, or
`domain:example.domain.com`.
Deleted principals have an additional `deleted:` prefix and a
`?uid=UID` suffix, where ``UID`` is
a unique identifier for the principal. Example:
`deleted:user:test-user@gmail.com?uid=123456789012345678901`.
Some resources also accept the following special values:

- `allUsers` - Special identifier that represents anyone who is on the
internet, with or without a Google account.
- `allAuthenticatedUsers` - Special identifier that represents anyone
who is authenticated with a Google account or a service account.

**--role**:
The role to remove the principal from.

**OPTIONAL FLAGS**

: **--all**

**--billing-account**

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