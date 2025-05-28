# gcloud identity groups create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/identity/groups/create](https://cloud.google.com/sdk/gcloud/reference/identity/groups/create)*

**NAME**

: **gcloud identity groups create - create a new group**

**SYNOPSIS**

: **`gcloud identity groups create` `[EMAIL](https://cloud.google.com/sdk/gcloud/reference/identity/groups/create#EMAIL)` (`[--customer](https://cloud.google.com/sdk/gcloud/reference/identity/groups/create#--customer)`=`CUSTOMER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/identity/groups/create#--organization)`=`ORGANIZATION`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/identity/groups/create#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/identity/groups/create#--display-name)`=`DISPLAY_NAME`] [`[--dynamic-user-query](https://cloud.google.com/sdk/gcloud/reference/identity/groups/create#--dynamic-user-query)`=`DYNAMIC_USER_QUERY`] [`[--with-initial-owner](https://cloud.google.com/sdk/gcloud/reference/identity/groups/create#--with-initial-owner)`=`WITH_INITIAL_OWNER`] [`[--group-type](https://cloud.google.com/sdk/gcloud/reference/identity/groups/create#--group-type)`=`GROUP_TYPE`; default="discussion"     | `[--labels](https://cloud.google.com/sdk/gcloud/reference/identity/groups/create#--labels)`=`LABELS`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/identity/groups/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new group.

**EXAMPLES**

: To quickly create a new Google Groups discussion group with default settings:

```
gcloud identity groups create eng-discuss@example.com --organization="example.com"
```

To create a new Google Groups discussion group with a display name and
descripton:

```
gcloud identity groups create eng-discuss@example.com --organization="example.com" --display-name="Engineer Discuss" --description="Group for engineering discussions"
```

To create a new security group:

```
gcloud identity groups create security-group@example.com --organization="example.com" --group-type="security" --display-name="Security Group" --description="Description of Security Group"
```

**POSITIONAL ARGUMENTS**

: **`EMAIL`**:
The email address of the group to be created.

**REQUIRED FLAGS**

: **--customer**

**OPTIONAL FLAGS**

: **--description**:
An extended description to help users determine the purpose of a Group. For
example, you can include information about who should join the Group, the types
of messages to send to the Group, links to FAQs about the Group, or related
Groups. Maximum length is 4,096 characters.

**--display-name**:
The Group's display name.

**--dynamic-user-query**:
Query that determines the memberships of the dynamic group.
Example of a query:
--dynamic-user-query="user.organizations.exists(org,org.title=='SWE')"

**--with-initial-owner**:
If specified the user making the request will be added as the initial owner of
the group being created. `WITH_INITIAL_OWNER` must be one
of:

**`empty`**:
The creator of the group will not be the owner of the group. This is the default
for dynamic groups.

**`with-initial-owner`**:
The creator of the group will be the owner of the group. This is the default for
non-dynamic groups.

**--group-type**

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
gcloud alpha identity groups create
```

```
gcloud beta identity groups create
```