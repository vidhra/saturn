# gcloud deploy deploy-policies add-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deploy/deploy-policies/add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/deploy/deploy-policies/add-iam-policy-binding)*

**NAME**

: **gcloud deploy deploy-policies add-iam-policy-binding - add IAM policy binding for a Cloud Deploy Policy**

**SYNOPSIS**

: **`gcloud deploy deploy-policies add-iam-policy-binding` (`[DEPLOY_POLICY](https://cloud.google.com/sdk/gcloud/reference/deploy/deploy-policies/add-iam-policy-binding#DEPLOY_POLICY)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/deploy/deploy-policies/add-iam-policy-binding#--region)`=`REGION`) `[--member](https://cloud.google.com/sdk/gcloud/reference/deploy/deploy-policies/add-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/deploy/deploy-policies/add-iam-policy-binding#--role)`=`ROLE` [`[--condition](https://cloud.google.com/sdk/gcloud/reference/deploy/deploy-policies/add-iam-policy-binding#--condition)`=[`KEY`=`VALUE`,…]     | `[--condition-from-file](https://cloud.google.com/sdk/gcloud/reference/deploy/deploy-policies/add-iam-policy-binding#--condition-from-file)`=`PATH_TO_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deploy/deploy-policies/add-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Adds a policy binding to the IAM policy of a Cloud Deploy Policy. One binding
consists of a member and a role.
See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of the policy file format and contents.

**EXAMPLES**

: To add an IAM policy binding for the role of
`roles/clouddeploy.policyAdmin` for the user
`test-user@gmail.com` on `holiday-policy` with the region
`us-central1`, run:

```
gcloud deploy deploy-policies add-iam-policy-binding holiday-policy --region='us-central1' --member='user:test-user@gmail.com' --role='roles/clouddeploy.policyAdmin'
```

**POSITIONAL ARGUMENTS**

: **Deploy policy resource - The deploy policy for which to add the IAM policy
binding. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `deploy_policy` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DEPLOY_POLICY`**:
ID of the deploy policy or fully qualified identifier for the deploy policy.
To set the `deploy_policy` attribute:

- provide the argument `deploy_policy` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Location of the deploy policy.
To set the `region` attribute:

- provide the argument `deploy_policy` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `deploy/region`.**

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

: This command uses the `clouddeploy/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/deploy/](https://cloud.google.com/deploy/)

**NOTES**

: These variants are also available:

```
gcloud alpha deploy deploy-policies add-iam-policy-binding
```

```
gcloud beta deploy deploy-policies add-iam-policy-binding
```