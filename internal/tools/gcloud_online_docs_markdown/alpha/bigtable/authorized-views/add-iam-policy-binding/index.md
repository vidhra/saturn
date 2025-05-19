# gcloud alpha bigtable authorized-views add-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/add-iam-policy-binding)*

**NAME**

: **gcloud alpha bigtable authorized-views add-iam-policy-binding - add an IAM policy binding to a Cloud Bigtable authorized view**

**SYNOPSIS**

: **`gcloud alpha bigtable authorized-views add-iam-policy-binding` (`[AUTHORIZED_VIEW](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/add-iam-policy-binding#AUTHORIZED_VIEW)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/add-iam-policy-binding#--instance)`=`INSTANCE` `[--table](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/add-iam-policy-binding#--table)`=`TABLE`) `[--member](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/add-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/add-iam-policy-binding#--role)`=`ROLE` [`[--condition](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/add-iam-policy-binding#--condition)`=[`KEY`=`VALUE`,…]     | `[--condition-from-file](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/add-iam-policy-binding#--condition-from-file)`=`PATH_TO_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/add-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Add an IAM policy binding to a Cloud Bigtable authorized
view. One binding consists of a member, a role, and an optional condition.

**EXAMPLES**

: To add an IAM policy binding for the role of 'roles/editor' for the user
'test-user@gmail.com' with authorized view 'my-authorized-view' in instance
'my-instance' and table 'my-table', run:

```
gcloud alpha bigtable authorized-views add-iam-policy-binding my-authorized-view --instance='my-instance' --table='my-table' --member='user:test-user@gmail.com' --role='roles/editor'
```

To add an IAM policy binding which expires at the end of the year 2020 for the
role of 'roles/bigtable.admin' and the user 'test-user@gmail.com' with
authorized view 'my-authorized-view' in instance 'my-instance' and table
'my-table', run:

```
gcloud alpha bigtable authorized-views add-iam-policy-binding my-authorized-view --instance='my-instance' --table='my-table' --member='user:test-user@gmail.com' --role='roles/bigtable.admin' --condition='expression=request.time <
 timestamp("2021-01-01T00:00:00Z"),title=expires_end_of_2020,descrip\
tion=Expires at midnight on 2020-12-31'
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of policy role and member types.

**POSITIONAL ARGUMENTS**

: **Authorized view resource - Cloud Bigtable authorized view to add the IAM policy
binding to. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `authorized_view` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`AUTHORIZED_VIEW`**:
ID of the authorized-view or fully qualified identifier for the authorized-view.
To set the `authorized_view` attribute:

- provide the argument `authorized_view` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--instance**:
Name of the Cloud Bigtable instance.
To set the `instance` attribute:

- provide the argument `authorized_view` on the command line with a
fully specified name;
- provide the argument `--instance` on the command line.

**--table**:
Name of the Cloud Bigtable table.
To set the `table` attribute:

- provide the argument `authorized_view` on the command line with a
fully specified name;
- provide the argument `--table` on the command line.**

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

**API REFERENCE**

: This command uses the `bigtableadmin/v2` API. The full documentation
for this API can be found at: [https://cloud.google.com/bigtable/](https://cloud.google.com/bigtable/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud bigtable authorized-views add-iam-policy-binding
```

```
gcloud beta bigtable authorized-views add-iam-policy-binding
```