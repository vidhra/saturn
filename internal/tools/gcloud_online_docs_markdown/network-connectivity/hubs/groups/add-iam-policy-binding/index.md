# gcloud network-connectivity hubs groups add-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/add-iam-policy-binding)*

**NAME**

: **gcloud network-connectivity hubs groups add-iam-policy-binding - add an IAM policy binding to the IAM policy of a group resource**

**SYNOPSIS**

: **`gcloud network-connectivity hubs groups add-iam-policy-binding` (`[GROUP](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/add-iam-policy-binding#GROUP)` : `[--hub](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/add-iam-policy-binding#--hub)`=`HUB`) `[--member](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/add-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/add-iam-policy-binding#--role)`=`ROLE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/add-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Add an IAM policy binding to the IAM policy of a group resource. One binding
consists of a member, a role, and an optional condition.

**EXAMPLES**

: To grant a user the
``roles/networkconnectivity.groupUser`` role on
the group called ``my-group`` in the hub called
``my-hub``', run the following command:

```
gcloud network-connectivity hubs groups add-iam-policy-binding my-group --member="user:username@gmail.com" --role="roles/networkconnectivity.groupUser" --hub="my-hub"
```

**POSITIONAL ARGUMENTS**

: **Group resource - The group that you want to update. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `group` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`GROUP`**:
ID of the group or fully qualified identifier for the group.
To set the `group` attribute:

- provide the argument `group` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--hub**:
Id of the hub.
To set the `hub` attribute:

- provide the argument `group` on the command line with a fully
specified name;
- provide the argument `--hub` on the command line.**

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

: This command uses the `networkconnectivity/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest](https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest)

**NOTES**

: This variant is also available:

```
gcloud beta network-connectivity hubs groups add-iam-policy-binding
```