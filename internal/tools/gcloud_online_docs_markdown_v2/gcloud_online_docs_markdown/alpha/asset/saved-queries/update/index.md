# gcloud alpha asset saved-queries update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/asset/saved-queries/update](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/saved-queries/update)*

**NAME**

: **gcloud alpha asset saved-queries update - update an existing Cloud Asset Inventory saved query**

**SYNOPSIS**

: **`gcloud alpha asset saved-queries update` `[QUERY_ID](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/saved-queries/update#QUERY_ID)` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/saved-queries/update#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/saved-queries/update#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/saved-queries/update#--project)`=`PROJECT_ID`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/saved-queries/update#--description)`=`DESCRIPTION`] [`[--query-file-path](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/saved-queries/update#--query-file-path)`=`QUERY_FILE_PATH`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/saved-queries/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/saved-queries/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/saved-queries/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/saved-queries/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update an existing Cloud Asset Inventory saved query.

**EXAMPLES**

: To update the content of an existing saved query, run:

```
gcloud alpha asset saved-queries update query-id-1 --project=p1 --query-file-path=./query-content.json --description="updating a query with query id query-id-1" --update-labels="key1=val1"
```

**POSITIONAL ARGUMENTS**

: **`QUERY_ID`**:
Saved query identifier being updated. It must be unique under the specified
parent resource project/folder/organization.

**REQUIRED FLAGS**

: **--folder**

**OPTIONAL FLAGS**

: **--description**:
A string describing the query.

**--query-file-path**:
Path to JSON or YAML file that contains the query.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud asset saved-queries update
```

```
gcloud beta asset saved-queries update
```