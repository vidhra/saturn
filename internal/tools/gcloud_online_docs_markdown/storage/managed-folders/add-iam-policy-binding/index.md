# gcloud storage managed-folders add-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/add-iam-policy-binding)*

**NAME**

: **gcloud storage managed-folders add-iam-policy-binding - add an IAM policy binding to a managed folder**

**SYNOPSIS**

: **`gcloud storage managed-folders add-iam-policy-binding` `[URL](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/add-iam-policy-binding#URL)` `[--member](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/add-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/add-iam-policy-binding#--role)`=`ROLE` [`[--condition](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/add-iam-policy-binding#--condition)`=[`KEY`=`VALUE`,…]     | `[--condition-from-file](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/add-iam-policy-binding#--condition-from-file)`=`PATH_TO_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders/add-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Add an IAM policy binding to a managed folder. For more information, see [Cloud Identity
and Access Management](https://cloud.google.com/storage/docs/access-control/iam).

**EXAMPLES**

: To grant a single role to a single principal for a managed folder
`managed-folder` in a bucket `bucket`:

```
gcloud storage managed-folders add-iam-policy-binding gs://bucket/managed-folder --member=user:john.doe@example.com --role=roles/storage.objectCreator
```

To make objects in `gs://bucket/managed-folder` publicly readable:

```
gcloud storage managed-folders add-iam-policy-binding gs://bucket/managed-folder --member=allUsers --role=roles/storage.objectViewer
```

To specify a custom role for a principal on
`gs://bucket/managed-folder`:

```
gcloud storage managed-folders add-iam-policy-binding gs://bucket/managed-folder --member=user:john.doe@example.com --role=roles/customRoleName
```

**POSITIONAL ARGUMENTS**

: **`URL`**:
URL of the managed folder to add IAM policy binding to.

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

: This variant is also available:

```
gcloud alpha storage managed-folders add-iam-policy-binding
```