# gcloud alpha compute backend-buckets remove-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/remove-iam-policy-binding)*

**NAME**

: **gcloud alpha compute backend-buckets remove-iam-policy-binding - remove an IAM policy binding from a Compute Engine backend bucket**

**SYNOPSIS**

: **`gcloud alpha compute backend-buckets remove-iam-policy-binding` `[BACKEND_BUCKET](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/remove-iam-policy-binding#BACKEND_BUCKET)` `[--member](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/remove-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/remove-iam-policy-binding#--role)`=`ROLE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/remove-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Remove an IAM policy binding from a Compute Engine backend
bucket.

**EXAMPLES**

: To remove an IAM policy binding for the role of
'roles/compute.loadBalancerServiceUser' for the user 'test-user@gmail.com' with
backend bucket 'my-backend-bucket' run:

```
gcloud alpha compute backend-buckets remove-iam-policy-binding my-backend-bucket --member='user:test-user@gmail.com' --role='roles/compute.loadBalancerServiceUser'
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of policy role and member types.

**POSITIONAL ARGUMENTS**

: **Backend bucket resource - The backend bucket for which to remove the IAM policy
from. This represents a Cloud resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `backend_bucket` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`BACKEND_BUCKET`**:
ID of the backend bucket or fully qualified identifier for the backend bucket.
To set the `backend_bucket` attribute:

- provide the argument `backend_bucket` on the command line.**

**REQUIRED FLAGS**

: **--member**:
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

**API REFERENCE**

: This command uses the `compute/alpha` API. The full documentation for
this API can be found at: [https://cloud.google.com/compute/](https://cloud.google.com/compute/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute backend-buckets remove-iam-policy-binding
```

```
gcloud beta compute backend-buckets remove-iam-policy-binding
```