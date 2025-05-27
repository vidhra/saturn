# gcloud dataplex zones remove-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/remove-iam-policy-binding)*

**NAME**

: **gcloud dataplex zones remove-iam-policy-binding - remove IAM policy binding from a Dataplex zone resource**

**SYNOPSIS**

: **`gcloud dataplex zones remove-iam-policy-binding` (`[ZONE](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/remove-iam-policy-binding#ZONE)` : `[--lake](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/remove-iam-policy-binding#--lake)`=`LAKE` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/remove-iam-policy-binding#--location)`=`LOCATION`) `[--member](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/remove-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/remove-iam-policy-binding#--role)`=`ROLE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/remove-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Remove IAM policy binding from a Dataplex zone resource.

**EXAMPLES**

: To remove an IAM policy binding for the role `roles/dataplex.viewer`
for the user `test-user@gmail.com` from zone `test-zone`
in lake `test-lake` in location `us-central`, run:

```
gcloud dataplex zones remove-iam-policy-binding test-zone --location=us-central1 --lake=test-lake --role=roles/dataplex.viewer --member=user:foo@gmail.com
```

See [https://cloud.google.com/dataplex/docs/iam-roles](https://cloud.google.com/dataplex/docs/iam-roles)
for details of policy role and member types.

**POSITIONAL ARGUMENTS**

: **Zones resource - Arguments and flags that define the Dataplex zone you want to
remove IAM policy binding from. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `zone` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ZONE`**:
ID of the zones or fully qualified identifier for the zones.
To set the `zone` attribute:

- provide the argument `zone` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--lake**:
The identifier of the Dataplex lake resource.
To set the `lake` attribute:

- provide the argument `zone` on the command line with a fully
specified name;
- provide the argument `--lake` on the command line.

**--location**:
The location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `zone` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

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

**NOTES**

: This variant is also available:

```
gcloud alpha dataplex zones remove-iam-policy-binding
```