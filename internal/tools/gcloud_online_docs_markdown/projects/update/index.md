# gcloud projects update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/projects/update](https://cloud.google.com/sdk/gcloud/reference/projects/update)*

**NAME**

: **gcloud projects update - update the name of a project**

**SYNOPSIS**

: **`gcloud projects update` `[PROJECT_ID](https://cloud.google.com/sdk/gcloud/reference/projects/update#PROJECT_ID)` `[--name](https://cloud.google.com/sdk/gcloud/reference/projects/update#--name)`=`NAME` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/projects/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the name of the given project.
This command can fail for the following reasons:

- There is no project with the given ID.
- The active account does not have Owner or Editor permissions for the given
project.

**EXAMPLES**

: The following command updates a project with the ID
`example-foo-bar-1` to have the name `Foo Bar &
Grill`:

```
gcloud projects update example-foo-bar-1 --name="Foo Bar & Grill"
```

**POSITIONAL ARGUMENTS**

: **`PROJECT_ID`**:
ID for the project you want to update.

**REQUIRED FLAGS**

: **--name**:
New name for the project.

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
gcloud alpha projects update
```

```
gcloud beta projects update
```