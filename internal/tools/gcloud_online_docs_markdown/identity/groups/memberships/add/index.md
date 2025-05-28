# gcloud identity groups memberships add  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/add](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/add)*

**NAME**

: **gcloud identity groups memberships add - create a new membership in an existing group**

**SYNOPSIS**

: **`gcloud identity groups memberships add` `[--group-email](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/add#--group-email)`=`GROUP_EMAIL` `[--member-email](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/add#--member-email)`=`MEMBER_EMAIL` [`[--expiration](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/add#--expiration)`=`EXPIRATION`] [`[--roles](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/add#--roles)`=[`ROLES`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/add#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new membership in an existing group.

**EXAMPLES**

: To create a new membership in a group:

```
gcloud identity groups memberships add --group-email="eng-discuss@foo.com" --member-email="user@foo.com"
```

**REQUIRED FLAGS**

: **--group-email**:
The email address of the group the new membership is being added to.

**--member-email**:
The email address of the group or user being added to a group.

**OPTIONAL FLAGS**

: **--expiration**:
Optional time of expiration for the membership. This is given as a duration from
now, for example '30d', '6m', '3y' for 30 days, 6 months, or 3 years
respectively.

**--roles**:
A comma-separated list of roles for a member within the Group. If not specified,
MEMBER will be used as a default value.

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
gcloud alpha identity groups memberships add
```

```
gcloud beta identity groups memberships add
```