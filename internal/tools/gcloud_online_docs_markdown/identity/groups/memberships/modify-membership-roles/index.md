# gcloud identity groups memberships modify-membership-roles  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/modify-membership-roles](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/modify-membership-roles)*

**NAME**

: **gcloud identity groups memberships modify-membership-roles - add/remove/modify membership roles of a membership in a group**

**SYNOPSIS**

: **`gcloud identity groups memberships modify-membership-roles` `[--group-email](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/modify-membership-roles#--group-email)`=`GROUP_EMAIL` `[--member-email](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/modify-membership-roles#--member-email)`=`MEMBER_EMAIL` [`[--update-roles-params](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/modify-membership-roles#--update-roles-params)`=`UPDATE_ROLES_PARAMS`     | `[--add-roles](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/modify-membership-roles#--add-roles)`=`ADD_ROLES` `[--remove-roles](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/modify-membership-roles#--remove-roles)`=[`REMOVE_ROLES`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/modify-membership-roles#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Add/remove/modify membership roles OR update expiry details of membership in a
group.

**EXAMPLES**

: To add a new membership role to an existing group-member pair.

```
gcloud identity groups memberships modify-membership-roles --group-email="eng-discuss@foo.com" --member-email="user@foo.com" --add-roles=OWNER
```

**REQUIRED FLAGS**

: **--group-email**:
The email address of the group that member-email belongs to.

**--member-email**:
The email address of the group or user that is being updated

**OPTIONAL FLAGS**

: **--update-roles-params**

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
gcloud alpha identity groups memberships modify-membership-roles
```

```
gcloud beta identity groups memberships modify-membership-roles
```