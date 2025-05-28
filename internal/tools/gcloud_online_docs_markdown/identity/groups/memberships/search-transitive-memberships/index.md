# gcloud identity groups memberships search-transitive-memberships  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/search-transitive-memberships](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/search-transitive-memberships)*

**NAME**

: **gcloud identity groups memberships search-transitive-memberships - search transitive memberships of a group**

**SYNOPSIS**

: **`gcloud identity groups memberships search-transitive-memberships` `[--group-email](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/search-transitive-memberships#--group-email)`=`GROUP_EMAIL` [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/search-transitive-memberships#--page-size)`=`PAGE_SIZE`] [`[--page-token](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/search-transitive-memberships#--page-token)`=`PAGE_TOKEN`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/search-transitive-memberships#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Search transitive memberships of a group.

**EXAMPLES**

: To search transitive memberships of a group.
```
gcloud identity groups memberships search-transitive-memberships --group-email=eng@foo.com --page-size=10
```

**REQUIRED FLAGS**

: **--group-email**:
The email address of the group to search transitive memberships for.

**OPTIONAL FLAGS**

: **--page-size**:
The maximum number of results to return.

**--page-token**:
The next_page_token value returned from a previous search request, if any.

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

: This command uses the `cloudidentity/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/identity/](https://cloud.google.com/identity/)

**NOTES**

: These variants are also available:

```
gcloud alpha identity groups memberships search-transitive-memberships
```

```
gcloud beta identity groups memberships search-transitive-memberships
```