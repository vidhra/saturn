# gcloud ai-platform models add-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ai-platform/models/add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/ai-platform/models/add-iam-policy-binding)*

**NAME**

: **gcloud ai-platform models add-iam-policy-binding - add IAM policy binding for a model**

**SYNOPSIS**

: **`gcloud ai-platform models add-iam-policy-binding` `[MODEL](https://cloud.google.com/sdk/gcloud/reference/ai-platform/models/add-iam-policy-binding#MODEL)` `[--member](https://cloud.google.com/sdk/gcloud/reference/ai-platform/models/add-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/ai-platform/models/add-iam-policy-binding#--role)`=`ROLE` [`[--region](https://cloud.google.com/sdk/gcloud/reference/ai-platform/models/add-iam-policy-binding#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ai-platform/models/add-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Add IAM policy binding to a model.

**EXAMPLES**

: To add an IAM policy binding for the role of `roles/ml.admin` for the
user `test-user@gmail.com` on a model with identifier
`my_model`, run:

```
gcloud ai-platform models add-iam-policy-binding my_model --member='user:test-user@gmail.com' --role='roles/ml.admin'
```

To add an IAM policy binding for the role of `roles/ml.admin` to the
service account `test-proj1@example.domain.com`, run:

```
gcloud ai-platform models add-iam-policy-binding my_model --member='serviceAccount:test-proj1@example.domain.com' --role='roles/ml.admin'
```

To add an IAM policy binding for the role of `roles/ml.admin` for all
authenticated users on a model with identifier `my_model`, run:

```
gcloud ai-platform models add-iam-policy-binding my_model --member='allAuthenticatedUsers' --role='roles/ml.admin'
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of policy role and principal types.

**POSITIONAL ARGUMENTS**

: **`MODEL`**:
Name of the model.

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

: **--region**:
Google Cloud region of the regional endpoint to use for this command. For the
global endpoint, the region needs to be specified as `global`.
Learn more about regional endpoints and see a list of available regions: [https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints](https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints)
`REGION` must be one of: `global`,
`asia-east1`, `asia-northeast1`,
`asia-southeast1`, `australia-southeast1`,
`europe-west1`, `europe-west2`, `europe-west3`,
`europe-west4`, `northamerica-northeast1`,
`us-central1`, `us-east1`, `us-east4`,
`us-west1`.

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
gcloud alpha ai-platform models add-iam-policy-binding
```

```
gcloud beta ai-platform models add-iam-policy-binding
```