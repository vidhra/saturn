# gcloud identity groups update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/identity/groups/update](https://cloud.google.com/sdk/gcloud/reference/identity/groups/update)*

**NAME**

: **gcloud identity groups update - update a group**

**SYNOPSIS**

: **`gcloud identity groups update` `[EMAIL](https://cloud.google.com/sdk/gcloud/reference/identity/groups/update#EMAIL)` [`[--dynamic-user-query](https://cloud.google.com/sdk/gcloud/reference/identity/groups/update#--dynamic-user-query)`=`DYNAMIC_USER_QUERY`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/identity/groups/update#--labels)`=`LABELS`] [`[--clear-description](https://cloud.google.com/sdk/gcloud/reference/identity/groups/update#--clear-description)`     | `[--description](https://cloud.google.com/sdk/gcloud/reference/identity/groups/update#--description)`=`DESCRIPTION`] [`[--clear-display-name](https://cloud.google.com/sdk/gcloud/reference/identity/groups/update#--clear-display-name)`     | `[--display-name](https://cloud.google.com/sdk/gcloud/reference/identity/groups/update#--display-name)`=`DISPLAY_NAME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/identity/groups/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a group.

**EXAMPLES**

: To update a group:

```
gcloud identity groups update eng-discuss@foo.com --display-name="New Engineer Discuss" --description="Group for engineering discussions"
```

**POSITIONAL ARGUMENTS**

: **`EMAIL`**:
The email address of the group to be updated.

**FLAGS**

: **--dynamic-user-query**:
Query that determines the memberships of the dynamic group.
Example of a query:
`--dynamic-user-query="user.organizations.exists(org,org.title=='SWE')"`

**--labels**:
One or more label entries that apply to the group. Currently supported labels
contain a key with an empty value.
Google Groups are the default type of group and have a label with a key of
'cloudidentity.googleapis.com/groups.discussion_forum' and an empty value.
Existing Google Groups can have an additional label with a key of
'cloudidentity.googleapis.com/groups.security' and an empty value added to them.
`This is an immutable change and the security label cannot be removed once
added.`
Dynamic groups have a label with a key of
'cloudidentity.googleapis.com/groups.dynamic'.
Identity-mapped groups for Cloud Search have a label with a key of
'system/groups/external' and an empty value.
Examples: {"cloudidentity.googleapis.com/groups.discussion_forum": ""} or
{"system/groups/external": ""}.

**--clear-description**

**--clear-display-name**

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
gcloud alpha identity groups update
```

```
gcloud beta identity groups update
```