# gcloud alpha compute images remove-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/remove-iam-policy-binding)*

**NAME**

: **gcloud alpha compute images remove-iam-policy-binding - remove IAM policy binding from a Compute Engine image**

**SYNOPSIS**

: **`gcloud alpha compute images remove-iam-policy-binding` `[IMAGE](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/remove-iam-policy-binding#IMAGE)` `[--member](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/remove-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/remove-iam-policy-binding#--role)`=`ROLE` [`[--all](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/remove-iam-policy-binding#--all)`     | `[--condition](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/remove-iam-policy-binding#--condition)`=[`KEY`=`VALUE`,…]     | `[--condition-from-file](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/remove-iam-policy-binding#--condition-from-file)`=`PATH_TO_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/remove-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Remove an IAM policy binding from the IAM policy of a
Compute Engine image. One binding consists of a member, a role, and an optional
condition.

**EXAMPLES**

: To remove an IAM policy binding for the role of 'roles/compute.securityAdmin'
for the user 'test-user@gmail.com' with image 'my-image', run:

```
gcloud alpha compute images remove-iam-policy-binding my-image --member='user:test-user@gmail.com' --role='roles/compute.securityAdmin'
```

To remove an IAM policy binding which expires at the end of the year 2018 for
the role of 'roles/compute.securityAdmin' and the user 'test-user@gmail.com'
with image 'my-image', run:

```
gcloud alpha compute images remove-iam-policy-binding my-image --member='user:test-user@gmail.com' --role='roles/compute.securityAdmin' --condition='expression=request.time <
 timestamp("2019-01-01T00:00:00Z"),title=expires_end_of_2018,descrip\
tion=Expires at midnight on 2018-12-31'
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of policy role and member types.

**POSITIONAL ARGUMENTS**

: **Image resource - The image for which to remove IAM policy binding from. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `image` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`IMAGE`**:
ID of the image or fully qualified identifier for the image.
To set the `image` attribute:

- provide the argument `image` on the command line.**

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

**API REFERENCE**

: This command uses the `compute/alpha` API. The full documentation for
this API can be found at: [https://cloud.google.com/compute/](https://cloud.google.com/compute/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute images remove-iam-policy-binding
```

```
gcloud beta compute images remove-iam-policy-binding
```