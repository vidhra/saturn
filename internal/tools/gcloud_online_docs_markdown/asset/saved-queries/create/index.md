# gcloud asset saved-queries create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/asset/saved-queries/create](https://cloud.google.com/sdk/gcloud/reference/asset/saved-queries/create)*

**NAME**

: **gcloud asset saved-queries create - create a Cloud Asset Inventory saved query**

**SYNOPSIS**

: **`gcloud asset saved-queries create` `[QUERY_ID](https://cloud.google.com/sdk/gcloud/reference/asset/saved-queries/create#QUERY_ID)` `[--query-file-path](https://cloud.google.com/sdk/gcloud/reference/asset/saved-queries/create#--query-file-path)`=`QUERY_FILE_PATH` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/asset/saved-queries/create#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/asset/saved-queries/create#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/asset/saved-queries/create#--project)`=`PROJECT_ID`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/asset/saved-queries/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/asset/saved-queries/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/asset/saved-queries/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Cloud Asset Inventory saved query.

**EXAMPLES**

: To create a new saved 'query-id-1' in project 'p1' with the content of the query
stored locally in query.json, run:

```
gcloud asset saved-queries create query-id-1 --project=p1 --query-file-path=./query-content.json --description="This is an example saved query with query id query-id-1" --labels="key1=val1"
```

**POSITIONAL ARGUMENTS**

: **`QUERY_ID`**:
Saved query identifier being created. It must be unique under the specified
parent resource project/folder/organization.

**REQUIRED FLAGS**

: **--query-file-path**:
Path to JSON or YAML file that contains the query.

**--folder**

**OPTIONAL FLAGS**

: **--description**:
A string describing the query.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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
gcloud alpha asset saved-queries create
```

```
gcloud beta asset saved-queries create
```