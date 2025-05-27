# gcloud dataplex assets add-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/add-iam-policy-binding)*

**NAME**

: **gcloud dataplex assets add-iam-policy-binding - adds IAM policy binding to a Dataplex asset resource**

**SYNOPSIS**

: **`gcloud dataplex assets add-iam-policy-binding` (`[ASSET](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/add-iam-policy-binding#ASSET)` : `[--lake](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/add-iam-policy-binding#--lake)`=`LAKE` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/add-iam-policy-binding#--location)`=`LOCATION` `[--zone](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/add-iam-policy-binding#--zone)`=`ZONE`) `[--member](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/add-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/add-iam-policy-binding#--role)`=`ROLE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/add-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Adds IAM policy binding to a Dataplex asset resource.

**EXAMPLES**

: To add an IAM policy binding for the role of `roles/dataplex.viewer`
for the user `test-user@gmail.com` to asset `test-asset`
within zone `test-zone` in lake `test-lake` in location
`us-central`, run:

```
gcloud dataplex assets add-iam-policy-binding test-asset --location=us-central1 --lake=test-lake --zone=test-zone --role=roles/dataplex.viewer --member=user:foo@gmail.com
```

See [https://cloud.google.com/dataplex/docs/iam-roles](https://cloud.google.com/dataplex/docs/iam-roles)
for details of policy role and member types.

**POSITIONAL ARGUMENTS**

: **Assets resource - Arguments and flags that define the Dataplex asset you want to
add IAM policy binding to. The arguments in this group can be used to specify
the attributes of this resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `asset` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ASSET`**:
ID of the assets or fully qualified identifier for the assets.
To set the `asset` attribute:

- provide the argument `asset` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--lake**:
The identifier of the Dataplex lake resource.
To set the `lake` attribute:

- provide the argument `asset` on the command line with a fully
specified name;
- provide the argument `--lake` on the command line.

**--location**:
The location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `asset` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.

**--zone**:
The identifier of the Dataplex zone resource.
To set the `zone` attribute:

- provide the argument `asset` on the command line with a fully
specified name;
- provide the argument `--zone` on the command line.**

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

**NOTES**

: This variant is also available:

```
gcloud alpha dataplex assets add-iam-policy-binding
```