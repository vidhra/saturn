# gcloud compute snapshots add-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/add-iam-policy-binding)*

**NAME**

: **gcloud compute snapshots add-iam-policy-binding - add IAM policy binding to a Compute Engine snapshot**

**SYNOPSIS**

: **`gcloud compute snapshots add-iam-policy-binding` `[SNAPSHOT_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/add-iam-policy-binding#SNAPSHOT_NAME)` `[--member](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/add-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/add-iam-policy-binding#--role)`=`ROLE` [`[--condition](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/add-iam-policy-binding#--condition)`=[`KEY`=`VALUE`,…]     | `[--condition-from-file](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/add-iam-policy-binding#--condition-from-file)`=`PATH_TO_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/add-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Add an IAM policy binding to the IAM policy of a Compute Engine snapshot. One
binding consists of a member, a role, and an optional condition.

**EXAMPLES**

: To add an IAM policy binding for the role of 'roles/compute.securityAdmin' for
the user 'test-user@gmail.com' with snapshot 'my-snapshot', run:

```
gcloud compute snapshots add-iam-policy-binding my-snapshot --member='user:test-user@gmail.com' --role='roles/compute.securityAdmin'
```

To add an IAM policy binding which expires at the end of the year 2018 for the
role of 'roles/compute.securityAdmin' and the user 'test-user@gmail.com' with
snapshot 'my-snapshot', run:

```
gcloud compute snapshots add-iam-policy-binding my-snapshot --member='user:test-user@gmail.com' --role='roles/compute.securityAdmin' --condition='expression=request.time <
 timestamp("2019-01-01T00:00:00Z"),title=expires_end_of_2018,descrip\
tion=Expires at midnight on 2018-12-31'
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of policy role and member types.

**POSITIONAL ARGUMENTS**

: **Snapshot resource - The snapshot for which to add IAM policy binding to. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `snapshot_name` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SNAPSHOT_NAME`**:
ID of the snapshot or fully qualified identifier for the snapshot.
To set the `snapshot_name` attribute:

- provide the argument `snapshot_name` on the command line.**

**REQUIRED FLAGS**

: **--member**:
The principal to add the binding for. Should be of the form
`user|group|serviceAccount:email` or `domain:domain`.
Examples: `user:test-user@gmail.com`,
`group:admins@example.com`,
`serviceAccount:test123@example.domain.com`, or
`domain:example.domain.com`.

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

: This command uses the `compute/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/compute/](https://cloud.google.com/compute/)

**NOTES**

: These variants are also available:

```
gcloud alpha compute snapshots add-iam-policy-binding
```

```
gcloud beta compute snapshots add-iam-policy-binding
```