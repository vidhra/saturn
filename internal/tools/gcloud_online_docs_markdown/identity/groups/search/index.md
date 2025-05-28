# gcloud identity groups search  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/identity/groups/search](https://cloud.google.com/sdk/gcloud/reference/identity/groups/search)*

**NAME**

: **gcloud identity groups search - searches for Groups matching a specified query**

**SYNOPSIS**

: **`gcloud identity groups search` `[--labels](https://cloud.google.com/sdk/gcloud/reference/identity/groups/search#--labels)`=`LABELS` (`[--customer](https://cloud.google.com/sdk/gcloud/reference/identity/groups/search#--customer)`=`CUSTOMER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/identity/groups/search#--organization)`=`ORGANIZATION`) [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/identity/groups/search#--page-size)`=`PAGE_SIZE`] [`[--page-token](https://cloud.google.com/sdk/gcloud/reference/identity/groups/search#--page-token)`=`PAGE_TOKEN`] [`[--view](https://cloud.google.com/sdk/gcloud/reference/identity/groups/search#--view)`=`VIEW`; default="basic"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/identity/groups/search#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Searches for Groups matching a specified query.

**EXAMPLES**

: To Search groups:

```
gcloud identity groups search --organization="5149234212" --labels="cloudidentity.googleapis.com/groups.discussion_forum" --page-size=3 --page-token="ala9glealanal908"
```

**REQUIRED FLAGS**

: **--labels**:
One or more label entries that apply to the Group. Currently supported labels
contain a key with an empty value.
Google Groups are the default type of group and have a label with a key of
'cloudidentity.googleapis.com/groups.discussion_forum' and an empty value.
Existing Google Groups can have an additional label with a key of
'cloudidentity.googleapis.com/groups.security' and an empty value added to them.
`This is an immutable change and the security label cannot be removed once
added.`
POSIX groups have a label with a key of
'cloudidentity.googleapis.com/groups.posix'.
Dynamic groups have a label with a key of
'cloudidentity.googleapis.com/groups.dynamic'.
Identity-mapped groups for Cloud Search have a label with a key of
'system/groups/external' and an empty value.
Examples: {"cloudidentity.googleapis.com/groups.discussion_forum": ""} or
{"system/groups/external": ""}.

**--customer**

**OPTIONAL FLAGS**

: **--page-size**:
The maximum number of results to return.
Note that the number of results returned may be less than this value even if
there are more available results. To fetch all results, clients must continue
calling this method repeatedly until the response no longer contains a
nextPageToken.
If unspecified, defaults to 200 'basic' view and to 50 for 'full' view.
Must not be greater than 1000 for 'basic' view or 500 for 'full' view.

**--page-token**:
The nextPageToken value returned from a previous search request, if any.

**--view**:
The level of detail to be returned. There are two possible views: 'basic' and
'full'. If unspecified, default to 'basic'. `VIEW` must be
one of:

**`basic`**:
Default. Only basic group information is returned.

**`full`**:
All group information is returned.

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
gcloud alpha identity groups search
```

```
gcloud beta identity groups search
```