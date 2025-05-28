# gcloud endpoints services add-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/endpoints/services/add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/add-iam-policy-binding)*

**NAME**

: **gcloud endpoints services add-iam-policy-binding - add IAM policy binding to a service**

**SYNOPSIS**

: **`gcloud endpoints services add-iam-policy-binding` `[SERVICE](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/add-iam-policy-binding#SERVICE)` `[--member](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/add-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/add-iam-policy-binding#--role)`=`ROLE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/add-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Add an IAM policy binding to a service.
Note: The 'roles/servicemanagement.serviceConsumer' role can only be added to a
member which is a user, group, or service account.

**EXAMPLES**

: To add an IAM policy binding with the role of
'roles/servicemanagement.serviceConsumer' for the user 'test-user@example.com'
on the service 'my-service', run:

```
gcloud endpoints services add-iam-policy-binding my-service --member='user:test-user@example.com' --role='roles/servicemanagement.serviceConsumer'
```

To add an IAM policy binding with the role of
'roles/servicemanagement.serviceConsumer' for the service account
'my-iam-account@my-project.iam.gserviceaccount.com' on the service 'my-service',
run:

```
gcloud endpoints services add-iam-policy-binding my-service --member='serviceAccount:my-iam-account@my-project.iam.gserviceaccount.com' --role='roles/servicemanagement.serviceConsumer'
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of policy role and member types.

**POSITIONAL ARGUMENTS**

: **Service resource - The service for which to add IAM policy binding to. This
represents a Cloud resource.
This must be specified.

**`SERVICE`**:
ID of the service or fully qualified identifier for the service.
To set the `service` attribute:

- provide the argument `service` on the command line.**

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

**API REFERENCE**

: This command uses the `servicemanagement/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/service-management/](https://cloud.google.com/service-management/)

**NOTES**

: These variants are also available:

```
gcloud alpha endpoints services add-iam-policy-binding
```

```
gcloud beta endpoints services add-iam-policy-binding
```