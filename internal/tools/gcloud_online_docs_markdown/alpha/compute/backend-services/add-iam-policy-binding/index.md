# gcloud alpha compute backend-services add-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/add-iam-policy-binding)*

**NAME**

: **gcloud alpha compute backend-services add-iam-policy-binding - add an IAM policy binding to a Compute Engine backend service**

**SYNOPSIS**

: **`gcloud alpha compute backend-services add-iam-policy-binding` `[BACKEND_SERVICE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/add-iam-policy-binding#BACKEND_SERVICE_NAME)` `[--member](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/add-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/add-iam-policy-binding#--role)`=`ROLE` [`[--global](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/add-iam-policy-binding#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/add-iam-policy-binding#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/add-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Add an IAM policy binding to a Compute Engine backend
service.

**EXAMPLES**

: To add an IAM policy binding for the role of 'compute.loadBalancerServiceUser'
for the user 'test-user@gmail.com' with backend service 'my-backend-service' and
region 'REGION', run:

```
gcloud alpha compute backend-services add-iam-policy-binding my-backend-service --region=REGION --member='user:test-user@gmail.com' --role='roles/compute.loadBalancerServiceUser'
```

```
gcloud alpha compute backend-services add-iam-policy-binding my-backend-service --global --member='user:test-user@gmail.com' --role='roles/compute.loadBalancerServiceUser'
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of policy role and member types.

**POSITIONAL ARGUMENTS**

: **`BACKEND_SERVICE_NAME`**:
Name of the backend service to operate on.

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

: **--global**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute backend-services add-iam-policy-binding
```

```
gcloud beta compute backend-services add-iam-policy-binding
```