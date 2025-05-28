# gcloud identity groups memberships list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/list](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/list)*

**NAME**

: **gcloud identity groups memberships list - list memberships in an existing group**

**SYNOPSIS**

: **`gcloud identity groups memberships list` `[--group-email](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/list#--group-email)`=`GROUP_EMAIL` [`[--page-token](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/list#--page-token)`=`PAGE_TOKEN`] [`[--view](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/list#--view)`=`VIEW`; default="basic"] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List memberships in an existing group.

**EXAMPLES**

: To list memberships of a group:

```
gcloud identity groups memberships list --group-email="eng-discuss@foo.com" --limit=50
```

**REQUIRED FLAGS**

: **--group-email**:
The email address of the group to show members for.

**FLAGS**

: **--page-token**:
The next_page_token value returned from a previous list request, if any.

**--view**:
There are two possible views, 'basic' and 'full', default is 'basic'.
`VIEW` must be one of:

**`basic`**:
Response only basic information of the Groups. (e.g. 'display_name', 'name')

**`full`**:
Response includes all the fields of the Groups

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates `True`, then that item is
listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--limit**:
Maximum number of resources to list. The default is `unlimited`. This
flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--page-size**:
Some services group resource list output into pages. This flag specifies the
maximum number of resources per page. The default is determined by the service
if it supports paging, otherwise it is `unlimited` (no paging).
Paging may be applied before or after `--filter` and
`--limit` depending on the service.

**--sort-by**:
Comma-separated list of resource field key names to sort by. The default order
is ascending. Prefix a field with ``~´´ for descending order on that
field. This flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

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
gcloud alpha identity groups memberships list
```

```
gcloud beta identity groups memberships list
```