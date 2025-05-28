# gcloud iam roles delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/roles/delete](https://cloud.google.com/sdk/gcloud/reference/iam/roles/delete)*

**NAME**

: **gcloud iam roles delete - delete a custom role from an organization or a project**

**SYNOPSIS**

: **`gcloud iam roles delete` `[ROLE_ID](https://cloud.google.com/sdk/gcloud/reference/iam/roles/delete#ROLE_ID)` (`[--organization](https://cloud.google.com/sdk/gcloud/reference/iam/roles/delete#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/iam/roles/delete#--project)`=`PROJECT_ID`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/roles/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command deletes a role.
This command can fail for the following reasons:

- The role specified does not exist.
- The active user does not have permission to access the given role.

**EXAMPLES**

: To delete the role ``ProjectUpdater`` of the
organization ``1234567``, run:

```
gcloud iam roles delete ProjectUpdater --organization=1234567
```

To delete the role ``ProjectUpdater`` of the
project ``myproject``, run:

```
gcloud iam roles delete ProjectUpdater --project=myproject
```

**POSITIONAL ARGUMENTS**

: **`ROLE_ID`**:
ID of the custom role to delete. You must also specify the
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
gcloud alpha iam roles delete
```

```
gcloud beta iam roles delete
```