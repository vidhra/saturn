# gcloud api-gateway apis add-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/add-iam-policy-binding)*

**NAME**

: **gcloud api-gateway apis add-iam-policy-binding - add IAM policy binding to a gateway**

**SYNOPSIS**

: **`gcloud api-gateway apis add-iam-policy-binding` `[API](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/add-iam-policy-binding#API)` `[--member](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/add-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/add-iam-policy-binding#--role)`=`ROLE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/add-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Add IAM policy binding to a gateway.

**EXAMPLES**

: To add an IAM policy binding for the role of 'roles/editor' for the user
'test-user@gmail.com' on the API 'my-api', run:

```
gcloud api-gateway apis add-iam-policy-binding my-api --member='user:test-user@gmail.com' --role='roles/editor
```

**POSITIONAL ARGUMENTS**

: **Api resource - Name for API which IAM policy binding will be added to. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `api` on the command line with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `api` on the command line with a fully specified
name;
- Location for API and API Configs. Defaults to global.

This must be specified.

**`API`**:
ID of the api or fully qualified identifier for the api.
To set the `api` attribute:

- provide the argument `api` on the command line.**

**REQUIRED FLAGS**

: **--member**:
The principal to add the binding for. Should be of the form
`user|group|serviceAccount:email` or `domain:domain`.
Examples: `user:test-user@gmail.com`,
`group:admins@example.com`,
`serviceAccount:test123@example.domain.com`, or
`domain:example.domain.com`.
Some resources also accept the following special values:

- `allUsers` - Special identifier that represents anyone who is on the
internet, with or without a Google account.
- `allAuthenticatedUsers` - Special identifier that represents anyone
who is authenticated with a Google account or a service account.

**--role**:
Role name to assign to the principal. The role name is the complete path of a
predefined role, such as `roles/logging.viewer`, or the role ID for a
custom role, such as
`organizations/{ORGANIZATION_ID}/roles/logging.viewer`.

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

**NOTES**

: These variants are also available:

```
gcloud alpha api-gateway apis add-iam-policy-binding
```

```
gcloud beta api-gateway apis add-iam-policy-binding
```