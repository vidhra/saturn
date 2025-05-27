# gcloud dataplex entries search  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/search](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/search)*

**NAME**

: **gcloud dataplex entries search - searches for Dataplex entries**

**SYNOPSIS**

: **`gcloud dataplex entries search` `[QUERY](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/search#QUERY)` `[--project](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/search#--project)`=`PROJECT` [`[--limit](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/search#--limit)`=`LIMIT`] [`[--order-by](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/search#--order-by)`=`ORDER_BY`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/search#--page-size)`=`PAGE_SIZE`] [`[--scope](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/search#--scope)`=`SCOPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/search#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Searches for entries matching given query and scope.

**EXAMPLES**

: To search project 'my-project' for Dataplex resources that match the simple
predicate 'foo':

```
gcloud dataplex entries search 'foo' --project=my-project
```

**POSITIONAL ARGUMENTS**

: **`QUERY`**:
The query against which entries in scope should be matched.

**REQUIRED FLAGS**

: **--project**:
The project to which the request should be attributed.

**OPTIONAL FLAGS**

: **--limit**:
Maximum number of resources.

**--order-by**:
Specifies the ordering of results, currently supported case-sensitive choices
are:

- `title [asc|desc]`, defaults to ascending if not specified.

**--page-size**:
Maximum number of resources per page. No more than 500.

**--scope**:
The scope under which the search should be operating. Should either be
organizations/<org_id> or projects/<project_ref>. If left
unspecified, it will default to the organization where the project is located.

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

**API REFERENCE**

: This command uses the `dataplex/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/dataplex/docs](https://cloud.google.com/dataplex/docs)

**NOTES**

: This variant is also available:

```
gcloud alpha dataplex entries search
```