# gcloud identity groups memberships get-membership-graph  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/get-membership-graph](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/get-membership-graph)*

**NAME**

: **gcloud identity groups memberships get-membership-graph - get a membership graph of just a member or both a member and a group**

**SYNOPSIS**

: **`gcloud identity groups memberships get-membership-graph` `[--labels](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/get-membership-graph#--labels)`=`LABELS` `[--member-email](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/get-membership-graph#--member-email)`=`MEMBER_EMAIL` [`[--group-email](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/get-membership-graph#--group-email)`=`GROUP_EMAIL`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/get-membership-graph#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get a membership graph of just a member or both a member and a group.

**EXAMPLES**

: To get a membership graph of just a member.

```
gcloud identity groups memberships get-membership-graph --member-email=eng-discuss@foo.com --labels=cloudidentity.googleapis.com/groups.discussion_forum
```

To get a membership graph between a member and a group.

```
gcloud identity groups memberships get-membership-graph --member-email=eng-discuss@foo.com --group-email=eng@foo.com --labels=cloudidentity.googleapis.com/groups.discussion_forum
```

**REQUIRED FLAGS**

: **--labels**:
The labels of the groups in the membership graph.

**--member-email**:
The email address of the member to get the membership graph for.

**OPTIONAL FLAGS**

: **--group-email**:
The email address of the group to constrain the membership graph with.

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
gcloud alpha identity groups memberships get-membership-graph
```

```
gcloud beta identity groups memberships get-membership-graph
```