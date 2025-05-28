# gcloud projects delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/projects/delete](https://cloud.google.com/sdk/gcloud/reference/projects/delete)*

**NAME**

: **gcloud projects delete - delete a project**

**SYNOPSIS**

: **`gcloud projects delete` `[PROJECT_ID_OR_NUMBER](https://cloud.google.com/sdk/gcloud/reference/projects/delete#PROJECT_ID_OR_NUMBER)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/projects/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Deletes the project with the given project ID.
This command can fail for the following reasons:

- The project specified does not exist.
- The active account does not have IAM role `role/owner` or another IAM
role with the `resourcemanager.projects.delete` permission for the
given project.

See [Access
control for projects using IAM](https://cloud.google.com/resource-manager/docs/access-control-proj) for more information.

**EXAMPLES**

: The following command deletes the project with the ID
`example-foo-bar-1`:

```
gcloud projects delete example-foo-bar-1
```

**POSITIONAL ARGUMENTS**

: **`PROJECT_ID_OR_NUMBER`**:
ID or number for the project you want to delete.

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

**SEE ALSO**

: See [https://support.google.com/cloud/answer/6251787](https://support.google.com/cloud/answer/6251787)
for information on creating or deleting projects from the Google Cloud Platform
Console.

**NOTES**

: These variants are also available:

```
gcloud alpha projects delete
```

```
gcloud beta projects delete
```