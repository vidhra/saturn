# gcloud iap tcp dest-groups remove-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/remove-iam-policy-binding)*

**NAME**

: **gcloud iap tcp dest-groups remove-iam-policy-binding - remove IAM policy binding from an IAP TCP Destination Group resource**

**SYNOPSIS**

: **`gcloud iap tcp dest-groups remove-iam-policy-binding` `[--dest-group](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/remove-iam-policy-binding#--dest-group)`=`DEST_GROUP` `[--member](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/remove-iam-policy-binding#--member)`=`PRINCIPAL` `[--region](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/remove-iam-policy-binding#--region)`=`REGION` `[--role](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/remove-iam-policy-binding#--role)`=`ROLE` [`[--all](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/remove-iam-policy-binding#--all)`     | `[--condition](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/remove-iam-policy-binding#--condition)`=[`KEY`=`VALUE`,…]     | `[--condition-from-file](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/remove-iam-policy-binding#--condition-from-file)`=`PATH_TO_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/remove-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Removes a policy binding from the IAM policy of an IAP TCP Destination Group
resource. One binding consists of a member, a role and an optional condition.

**EXAMPLES**

: To remove an IAM policy binding for the role of
'roles/iap.tunnelResourceAccessor' for the user 'test-user@gmail.com' in the
group 'my-group' located in the region 'us-west1', run:

```
gcloud iap tcp dest-groups remove-iam-policy-binding --member='user:test-user@gmail.com' --role='roles/iap.tunnelResourceAccessor' --dest-group='my-group' --region='us-west1'
```

To remove an IAM policy binding for the role of
'roles/iap.tunnelResourceAccessor' from all authenticated users in the group
'my-group' located in the region 'us-west1', run:

```
gcloud iap tcp dest-groups remove-iam-policy-binding --member='allAuthenticatedUsers' --role='roles/iap.tunnelResourceAccessor' --dest-group='my-group' --region='us-west1'
```

To remove an IAM policy binding which expires at the end of the year 2018 for
the role of 'roles/iap.tunnelResourceAccessor' for the user
'test-user@gmail.com' in the group 'my-group' located in the region 'us-west1',
run:

```
gcloud iap tcp dest-groups remove-iam-policy-binding --member='user:test-user@gmail.com' --role='roles/iap.tunnelResourceAccessor' --condition='expression=request.time <
 timestamp("2019-01-01T00:00:00Z"),title=expires_end_of_2018,
 description=Expires at midnight on 2018-12-31' \
    --dest-group='my-group' --region='us-west1'
```

To remove all IAM policy bindings regardless of the condition for the role of
'roles/iap.tunnelResourceAccessor' and for the user 'test-user@gmail.com' in the
group 'my-group' located in the region 'us-west1', run:

```
gcloud iap tcp dest-groups remove-iam-policy-binding --member='user:test-user@gmail.com' --role='roles/iap.tunnelResourceAccessor' --dest-group='my-group' --region='us-west1'
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of policy role and member types.

**REQUIRED FLAGS**

: **--dest-group**:
Name of the Destination Group.

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

**--region**:
Region of the Destination Group.

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
gcloud alpha iap tcp dest-groups remove-iam-policy-binding
```

```
gcloud beta iap tcp dest-groups remove-iam-policy-binding
```