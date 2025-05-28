# gcloud iam roles undelete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/roles/undelete](https://cloud.google.com/sdk/gcloud/reference/iam/roles/undelete)*

**NAME**

: **gcloud iam roles undelete - undelete a custom role from an organization or a project**

**SYNOPSIS**

: **`gcloud iam roles undelete` `[ROLE_ID](https://cloud.google.com/sdk/gcloud/reference/iam/roles/undelete#ROLE_ID)` (`[--organization](https://cloud.google.com/sdk/gcloud/reference/iam/roles/undelete#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/iam/roles/undelete#--project)`=`PROJECT_ID`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/roles/undelete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command undeletes a role. Roles that have been deleted for certain long
time can't be undeleted.
This command can fail for the following reasons:

- The role specified does not exist.
- The active user does not have permission to access the given role.

**EXAMPLES**

: To undelete the role ``ProjectUpdater`` of the
organization ``1234567``, run:

```
gcloud iam roles undelete ProjectUpdater --organization=1234567
```

To undelete the role ``ProjectUpdater`` of the
project ``myproject``, run:

```
gcloud iam roles undelete ProjectUpdater --project=myproject
```

**POSITIONAL ARGUMENTS**

: **`ROLE_ID`**:
ID of the custom role to undelete. You must also specify the
`--organization` or `--project` flag.

**REQUIRED FLAGS**

: **--organization**

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
gcloud alpha iam roles undelete
```

```
gcloud beta iam roles undelete
```