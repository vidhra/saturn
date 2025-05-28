# gcloud identity groups memberships search-transitive-groups  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/search-transitive-groups](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/search-transitive-groups)*

**NAME**

: **gcloud identity groups memberships search-transitive-groups - search transitive groups of a member**

**SYNOPSIS**

: **`gcloud identity groups memberships search-transitive-groups` `[--labels](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/search-transitive-groups#--labels)`=`LABELS` `[--member-email](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/search-transitive-groups#--member-email)`=`MEMBER_EMAIL` [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/search-transitive-groups#--page-size)`=`PAGE_SIZE`] [`[--page-token](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/search-transitive-groups#--page-token)`=`PAGE_TOKEN`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/search-transitive-groups#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Search transitive groups of a member.

**EXAMPLES**

: To search transitive groups of a member.

```
gcloud identity groups memberships search-transitive-groups --labels=cloudidentity.googleapis.com/groups.discussion_forum --member-email=eng-discuss@foo.com --page-size=10
```

**REQUIRED FLAGS**

: **--labels**:
The labels of the transitive groups.

**--member-email**:
The email address of the member to search transitive groups for.

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
gcloud alpha identity groups memberships search-transitive-groups
```

```
gcloud beta identity groups memberships search-transitive-groups
```