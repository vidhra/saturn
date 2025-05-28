# gcloud iam service-accounts add-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding)*

**NAME**

: **gcloud iam service-accounts add-iam-policy-binding - add an IAM policy binding to an IAM service account**

**SYNOPSIS**

: **`gcloud iam service-accounts add-iam-policy-binding` `[SERVICE_ACCOUNT](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding#SERVICE_ACCOUNT)` `[--member](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding#--role)`=`ROLE` [`[--condition](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding#--condition)`=[`KEY`=`VALUE`,…]     | `[--condition-from-file](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding#--condition-from-file)`=`PATH_TO_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Add an IAM policy binding to an IAM service account. A binding consists of at
least one member, a role, and an optional condition. Adding a binding to a
service account grants the specified member the specified role on the service
account.
When managing IAM roles, you can treat a service account either as a resource or
as an identity. This command adds an IAM policy binding to a service account
resource. There are other gcloud commands to manage IAM policies for other types
of resources. For example, to manage IAM policies on a project, use the $ [gcloud projects](https://cloud.google.com/sdk/gcloud/reference/projects) commands.
If the service account does not exist, this command returns a
`PERMISSION_DENIED` error.

**EXAMPLES**

: To add an IAM policy binding for the role of 'roles/editor' for the user
'test-user@gmail.com' on a service account with identifier
'my-iam-account@my-project.iam.gserviceaccount.com', run:

```
gcloud iam service-accounts add-iam-policy-binding my-iam-account@my-project.iam.gserviceaccount.com --member='user:test-user@gmail.com' --role='roles/editor'
```

To add an IAM policy binding for the role of 'roles/editor' to the service
account 'test-proj1@example.domain.com', run:

```
gcloud iam service-accounts add-iam-policy-binding test-proj1@example.domain.com --member='serviceAccount:test-proj1@example.domain.com' --role='roles/editor'
```

To add an IAM policy binding for the role of 'roles/editor' for all
authenticated users on a service account with identifier
'my-iam-account@my-project.iam.gserviceaccount.com', run:

```
gcloud iam service-accounts add-iam-policy-binding my-iam-account@my-project.iam.gserviceaccount.com --member='allAuthenticatedUsers' --role='roles/editor'
```

To add an IAM policy binding which expires at the end of the year 2018 for the
role of 'roles/iam.serviceAccountAdmin' and the user 'test-user@gmail.com' on a
service account with identifier
'my-iam-account@my-project.iam.gserviceaccount.com', run:

```
gcloud iam service-accounts add-iam-policy-binding my-iam-account@my-project.iam.gserviceaccount.com --member='user:test-user@gmail.com' --role='roles/iam.serviceAccountAdmin' --condition='expression=request.time <
 timestamp("2019-01-01T00:00:00Z"),title=expires_end_of_2018,descrip\
tion=Expires at midnight on 2018-12-31'
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of policy role and member types.

**POSITIONAL ARGUMENTS**

: **ServiceAccount resource - The service account to which the IAM policy binding is
being added. Note that the user, group or service account in the --member flag
is being granted access to this service account. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `service_account` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SERVICE_ACCOUNT`**:
ID of the serviceAccount or fully qualified identifier for the serviceAccount.
To set the `service_account` attribute:

- provide the argument `service_account` on the command line.**

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

**OPTIONAL FLAGS**

: **--condition**

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

: This command uses the `iam/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/iam/](https://cloud.google.com/iam/)

**NOTES**

: These variants are also available:

```
gcloud alpha iam service-accounts add-iam-policy-binding
```

```
gcloud beta iam service-accounts add-iam-policy-binding
```