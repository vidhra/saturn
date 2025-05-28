# gcloud iam roles copy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/roles/copy](https://cloud.google.com/sdk/gcloud/reference/iam/roles/copy)*

**NAME**

: **gcloud iam roles copy - create a role from an existing role**

**SYNOPSIS**

: **`gcloud iam roles copy` [`[--dest-organization](https://cloud.google.com/sdk/gcloud/reference/iam/roles/copy#--dest-organization)`=`DEST_ORGANIZATION`] [`[--dest-project](https://cloud.google.com/sdk/gcloud/reference/iam/roles/copy#--dest-project)`=`DEST_PROJECT`] [`[--destination](https://cloud.google.com/sdk/gcloud/reference/iam/roles/copy#--destination)`=`DESTINATION`] [`[--source](https://cloud.google.com/sdk/gcloud/reference/iam/roles/copy#--source)`=`SOURCE`] [`[--source-organization](https://cloud.google.com/sdk/gcloud/reference/iam/roles/copy#--source-organization)`=`SOURCE_ORGANIZATION`] [`[--source-project](https://cloud.google.com/sdk/gcloud/reference/iam/roles/copy#--source-project)`=`SOURCE_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/roles/copy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command creates a role from an existing role.

**EXAMPLES**

: To create a copy of an existing role
``spanner.databaseAdmin`` into an organization
with ``1234567``, run:

```
gcloud iam roles copy --source="roles/spanner.databaseAdmin" --destination=CustomViewer --dest-organization=1234567
```

To create a copy of an existing role
``spanner.databaseAdmin`` into a project with
``PROJECT_ID``, run:

```
gcloud iam roles copy --source="roles/spanner.databaseAdmin" --destination=CustomSpannerDbAdmin --dest-project=PROJECT_ID
```

To modify the newly created role see the roles update command.

**FLAGS**

: **--dest-organization**:
The organization of the destination role.

**--dest-project**:
The project of the destination role.

**--destination**:
The destination role ID for the new custom role. For example: viewer.

**--source**:
The source role ID. For predefined roles, for example: roles/viewer. For custom
roles, for example: myCompanyAdmin.

**--source-organization**:
The organization of the source role if it is an custom role.

**--source-project**:
The project of the source role if it is an custom role.

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
gcloud alpha iam roles copy
```

```
gcloud beta iam roles copy
```