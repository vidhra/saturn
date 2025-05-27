# gcloud data-catalog search  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/data-catalog/search](https://cloud.google.com/sdk/gcloud/reference/data-catalog/search)*

**NAME**

: **gcloud data-catalog search - search Data Catalog for resources that match a query**

**SYNOPSIS**

: **`gcloud data-catalog search` `[QUERY](https://cloud.google.com/sdk/gcloud/reference/data-catalog/search#QUERY)` (`[--include-gcp-public-datasets](https://cloud.google.com/sdk/gcloud/reference/data-catalog/search#--include-gcp-public-datasets)` `[--include-organization-ids](https://cloud.google.com/sdk/gcloud/reference/data-catalog/search#--include-organization-ids)`=[`ORGANIZATION`,…] `[--include-project-ids](https://cloud.google.com/sdk/gcloud/reference/data-catalog/search#--include-project-ids)`=[`PROJECT`,…] `[--restricted-locations](https://cloud.google.com/sdk/gcloud/reference/data-catalog/search#--restricted-locations)`=[`LOCATION`,…]) [`[--limit](https://cloud.google.com/sdk/gcloud/reference/data-catalog/search#--limit)`=`LIMIT`] [`[--order-by](https://cloud.google.com/sdk/gcloud/reference/data-catalog/search#--order-by)`=`ORDER_BY`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/data-catalog/search#--page-size)`=`PAGE_SIZE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/data-catalog/search#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` This command is deprecated. Please use `[gcloud dataplex entries
search](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries/search)` instead.
Search Data Catalog for resources that match a query.

**EXAMPLES**

: To search project 'my-project' for Data Catalog resources that match the simple
predicate 'foo':

```
gcloud data-catalog search 'foo' --include-project-ids=my-project
```

To search organization '1234' for Data Catalog resources that match entities
whose names match the predicate 'foo':

```
gcloud data-catalog search 'name:foo' --include-organization-ids=1234
```

**POSITIONAL ARGUMENTS**

: **`QUERY`**:
Query string in search query syntax in Data Catalog. For more information, see:
[https://cloud.google.com/data-catalog/docs/how-to/search-reference](https://cloud.google.com/data-catalog/docs/how-to/search-reference)

**REQUIRED FLAGS**

: **--include-gcp-public-datasets**

**LIST COMMAND FLAGS**

: **--limit**:
Maximum number of resources to list. The default is `unlimited`.

**--order-by**:
Specifies the ordering of results. Defaults to 'relevance'.
Currently supported case-sensitive choices are:

- relevance
- last_access_timestamp [asc|desc]: defaults to descending.
- last_modified_timestamp [asc|desc]: defaults to descending.

To order by last modified timestamp ascending, specify:
`--order-by="last_modified_timestamp desc"`.

**--page-size**:
Some services group resource list output into pages. This flag specifies the
maximum number of resources per page.

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
gcloud alpha data-catalog search
```

```
gcloud beta data-catalog search
```