# gcloud identity groups memberships describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/describe](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/describe)*

**NAME**

: **gcloud identity groups memberships describe - describe a membership in a group**

**SYNOPSIS**

: **`gcloud identity groups memberships describe` `[--group-email](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/describe#--group-email)`=`GROUP_EMAIL` `[--member-email](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/describe#--member-email)`=`MEMBER_EMAIL` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/identity/groups/memberships/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a membership in a group.

**EXAMPLES**

: To describe a membership in a group:

```
gcloud identity groups memberships describe --group-email="eng-discuss@foo.com" --member-email="user@foo.com"
```

**REQUIRED FLAGS**

: **--group-email**:
The email address of the group whose membership is being described.

**--member-email**:
The email address of the member whose membership is being described.

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
gcloud alpha identity groups memberships describe
```

```
gcloud beta identity groups memberships describe
```