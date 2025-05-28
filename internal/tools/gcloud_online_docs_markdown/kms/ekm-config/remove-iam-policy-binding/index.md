# gcloud kms ekm-config remove-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/kms/ekm-config/remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-config/remove-iam-policy-binding)*

**NAME**

: **gcloud kms ekm-config remove-iam-policy-binding - remove IAM policy binding from an EkmConfig**

**SYNOPSIS**

: **`gcloud kms ekm-config remove-iam-policy-binding` `[--location](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-config/remove-iam-policy-binding#--location)`=`LOCATION` `[--member](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-config/remove-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-config/remove-iam-policy-binding#--role)`=`ROLE` [`[--all](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-config/remove-iam-policy-binding#--all)`     | `[--condition](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-config/remove-iam-policy-binding#--condition)`=[`KEY`=`VALUE`,…]     | `[--condition-from-file](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-config/remove-iam-policy-binding#--condition-from-file)`=`PATH_TO_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/kms/ekm-config/remove-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Removes a policy binding from the IAM policy of a kms EkmConfig. A binding
consists of at least one member, a role, and an optional condition.

**EXAMPLES**

: To remove an IAM policy binding for the role of 'roles/editor' for the user
'test-user@gmail.com' on the EkmConfig with location us-central1, run:

```
gcloud kms ekm-config remove-iam-policy-binding --location='us-central1' --member='user:test-user@gmail.com' --role='roles/editor'
```

To remove an IAM policy binding with a condition of expression='request.time
< timestamp("2023-01-01T00:00:00Z")', title='expires_end_of_2022', and
description='Expires at midnight on 2022-12-31' for the role of 'roles/editor'
for the user 'test-user@gmail.com' on the EkmConfig with location us-central1,
run:

```
gcloud kms ekm-config remove-iam-policy-binding --location='us-central1' --member='user:test-user@gmail.com' --role='roles/editor' --condition='expression=request.time <
timestamp("2023-01-01T00:00:00Z"),title=expires_end_of_2022,description=Expires
at midnight on 2022-12-31'
```

To remove all IAM policy bindings regardless of the condition for the role of
'roles/editor' and for the user 'test-user@gmail.com' on the EkmConfig with
location us-central1, run:

```
gcloud kms ekm-config remove-iam-policy-binding laplace --location='us-central1' --member='user:test-user@gmail.com' --role='roles/editor' --all
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of policy role and member types.

**REQUIRED FLAGS**

: **Location resource - The KMS location resource. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- set the property `core/project`.

This must be specified.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line.**

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
gcloud alpha kms ekm-config remove-iam-policy-binding
```

```
gcloud beta kms ekm-config remove-iam-policy-binding
```