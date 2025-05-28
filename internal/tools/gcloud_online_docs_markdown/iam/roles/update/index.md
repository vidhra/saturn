# gcloud iam roles update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/roles/update](https://cloud.google.com/sdk/gcloud/reference/iam/roles/update)*

**NAME**

: **gcloud iam roles update - update an IAM custom role**

**SYNOPSIS**

: **`gcloud iam roles update` `[ROLE_ID](https://cloud.google.com/sdk/gcloud/reference/iam/roles/update#ROLE_ID)` (`[--organization](https://cloud.google.com/sdk/gcloud/reference/iam/roles/update#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/iam/roles/update#--project)`=`PROJECT_ID`) [`[--file](https://cloud.google.com/sdk/gcloud/reference/iam/roles/update#--file)`=`FILE`] [`[--add-permissions](https://cloud.google.com/sdk/gcloud/reference/iam/roles/update#--add-permissions)`=`ADD_PERMISSIONS` `[--description](https://cloud.google.com/sdk/gcloud/reference/iam/roles/update#--description)`=`DESCRIPTION` `[--permissions](https://cloud.google.com/sdk/gcloud/reference/iam/roles/update#--permissions)`=`PERMISSIONS` `[--remove-permissions](https://cloud.google.com/sdk/gcloud/reference/iam/roles/update#--remove-permissions)`=`REMOVE_PERMISSIONS` `[--stage](https://cloud.google.com/sdk/gcloud/reference/iam/roles/update#--stage)`=`STAGE` `[--title](https://cloud.google.com/sdk/gcloud/reference/iam/roles/update#--title)`=`TITLE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/roles/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command updates an IAM custom role.

**EXAMPLES**

: To update the role ``ProjectUpdater`` from a
YAML file, run:

```
gcloud iam roles update ProjectUpdater --organization=123 --file=role_file_path
```

To update the role ``ProjectUpdater`` with
flags, run:

```
gcloud iam roles update ProjectUpdater --project=myproject --permissions=permission1,permission2
```

**POSITIONAL ARGUMENTS**

: **`ROLE_ID`**:
ID of the custom role to update. You must also specify the
`--organization` or `--project` flag.

**REQUIRED FLAGS**

: **--organization**

**OPTIONAL FLAGS**

: **--file**:
The YAML file you want to use to update a role. Can not be specified with other
flags except role-id.

**--add-permissions**

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
gcloud alpha iam roles update
```

```
gcloud beta iam roles update
```