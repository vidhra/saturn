# gcloud ml-engine models remove-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ml-engine/models/remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/ml-engine/models/remove-iam-policy-binding)*

**NAME**

: **gcloud ml-engine models remove-iam-policy-binding - remove IAM policy binding for a model**

**SYNOPSIS**

: **`gcloud ml-engine models remove-iam-policy-binding` `[MODEL](https://cloud.google.com/sdk/gcloud/reference/ml-engine/models/remove-iam-policy-binding#MODEL)` `[--member](https://cloud.google.com/sdk/gcloud/reference/ml-engine/models/remove-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/ml-engine/models/remove-iam-policy-binding#--role)`=`ROLE` [`[--region](https://cloud.google.com/sdk/gcloud/reference/ml-engine/models/remove-iam-policy-binding#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ml-engine/models/remove-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Removes a policy binding from an AI Platform Model. One binding consists of a
member, a role and an optional condition. See $ [gcloud ml-engine
models get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/ml-engine/models/get-iam-policy) for examples of how to specify a model resource.

**EXAMPLES**

: To remove an IAM policy binding for the role of `roles/ml.admin` for
the user `test-user@gmail.com` on model with identifier
`my_model`, run:

```
gcloud ml-engine models remove-iam-policy-binding my_model --member='user:test-user@gmail.com' --role='roles/ml.admin'
```

To remove an IAM policy binding for the role of `roles/ml.admin` from
all authenticated users on model `my_model`, run:

```
gcloud ml-engine models remove-iam-policy-binding my_model --member='allAuthenticatedUsers' --role='roles/ml.admin'
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of policy role and member types.

**POSITIONAL ARGUMENTS**

: **Model resource - The AI Platform model for which to remove IAM policy binding
from. This represents a Cloud resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `model` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`MODEL`**:
ID of the model or fully qualified identifier for the model.
To set the `name` attribute:

- provide the argument `model` on the command line.**

**REQUIRED FLAGS**

: **--member**:
The principal to remove the binding for. Should be of the form
`user|group|serviceAccount:email` or `domain:domain`.
Examples: `user:test-user@gmail.com`,
`group:admins@example.com`,
`serviceAccount:test123@example.domain.com`, or
`domain:example.domain.com`.
Deleted principals have an additional `deleted:` prefix and a
`?uid=UID` suffix, where ``UID`` is
a unique identifier for the principal. Example:
`deleted:user:test-user@gmail.com?uid=123456789012345678901`.
Some resources also accept the following special values:

- `allUsers` - Special identifier that represents anyone who is on the
internet, with or without a Google account.
- `allAuthenticatedUsers` - Special identifier that represents anyone
who is authenticated with a Google account or a service account.

**--role**:
The role to remove the principal from.

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
gcloud alpha ml-engine models remove-iam-policy-binding
```

```
gcloud beta ml-engine models remove-iam-policy-binding
```