# gcloud alpha bigtable authorized-views set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/set-iam-policy)*

**NAME**

: **gcloud alpha bigtable authorized-views set-iam-policy - set an IAM policy on a Cloud Bigtable authorized view**

**SYNOPSIS**

: **`gcloud alpha bigtable authorized-views set-iam-policy` (`[AUTHORIZED_VIEW](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/set-iam-policy#AUTHORIZED_VIEW)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/set-iam-policy#--instance)`=`INSTANCE` `[--table](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/set-iam-policy#--table)`=`TABLE`) `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/set-iam-policy#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/authorized-views/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Set an IAM policy on a Cloud Bigtable authorized view.

**EXAMPLES**

: To set the IAM policy from file 'my-policy' on the authorized view
'my-authorized-view' in instance 'my-instance' and table 'my-table', run:

```
gcloud alpha bigtable authorized-views set-iam-policy my-authorized-view --instance='my-instance' --table='my-table' my-policy
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for more information.

**POSITIONAL ARGUMENTS**

: **Authorized view resource - Cloud Bigtable authorized view to set the IAM policy
on. The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
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

**`POLICY_FILE`**:
Path to a local JSON or YAML formatted file containing a valid policy.
The output of the `get-iam-policy` command is a valid file, as is any
JSON or YAML file conforming to the structure of a [Policy](https://cloud.google.com/iam/reference/rest/v1/Policy).

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
gcloud bigtable authorized-views set-iam-policy
```

```
gcloud beta bigtable authorized-views set-iam-policy
```