# gcloud projects undelete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/projects/undelete](https://cloud.google.com/sdk/gcloud/reference/projects/undelete)*

**NAME**

: **gcloud projects undelete - undelete a project**

**SYNOPSIS**

: **`gcloud projects undelete` `[PROJECT_ID_OR_NUMBER](https://cloud.google.com/sdk/gcloud/reference/projects/undelete#PROJECT_ID_OR_NUMBER)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/projects/undelete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Undeletes the project with the given project ID.
This command can fail for the following reasons:

- There is no project with the given ID.
- The active account does not have Owner or Editor permissions for the given
project.

**EXAMPLES**

: The following command undeletes the project with the ID
`example-foo-bar-1`:

```
gcloud projects undelete example-foo-bar-1
```

**POSITIONAL ARGUMENTS**

: **`PROJECT_ID_OR_NUMBER`**:
ID or number for the project you want to undelete.

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
gcloud alpha projects undelete
```

```
gcloud beta projects undelete
```