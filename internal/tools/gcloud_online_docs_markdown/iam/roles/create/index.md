# gcloud iam roles create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/roles/create](https://cloud.google.com/sdk/gcloud/reference/iam/roles/create)*

**NAME**

: **gcloud iam roles create - create a custom role for a project or an organization**

**SYNOPSIS**

: **`gcloud iam roles create` `[ROLE_ID](https://cloud.google.com/sdk/gcloud/reference/iam/roles/create#ROLE_ID)` (`[--organization](https://cloud.google.com/sdk/gcloud/reference/iam/roles/create#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/iam/roles/create#--project)`=`PROJECT_ID`) [`[--file](https://cloud.google.com/sdk/gcloud/reference/iam/roles/create#--file)`=`FILE`     | `[--description](https://cloud.google.com/sdk/gcloud/reference/iam/roles/create#--description)`=`DESCRIPTION` `[--permissions](https://cloud.google.com/sdk/gcloud/reference/iam/roles/create#--permissions)`=`PERMISSIONS` `[--stage](https://cloud.google.com/sdk/gcloud/reference/iam/roles/create#--stage)`=`STAGE` `[--title](https://cloud.google.com/sdk/gcloud/reference/iam/roles/create#--title)`=`TITLE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/roles/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command creates a custom role with the provided information.

**EXAMPLES**

: To create a custom role ``ProjectUpdater`` from
a YAML file, run:

```
gcloud iam roles create ProjectUpdater --organization=12345 --file=role_file_path
```

To create a custom role ``ProjectUpdater`` with
flags, run:

```
gcloud iam roles create ProjectUpdater --project=myproject --title=ProjectUpdater --description="Have access to get and update the project" --permissions=resourcemanager.projects.get,resourcemanager.projects.update
```

**POSITIONAL ARGUMENTS**

: **`ROLE_ID`**:
ID of the custom role to create. You must also specify the
`--organization` or `--project` flag.

**REQUIRED FLAGS**

: **--organization**

**OPTIONAL FLAGS**

: **--file**

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
gcloud alpha iam roles create
```

```
gcloud beta iam roles create
```