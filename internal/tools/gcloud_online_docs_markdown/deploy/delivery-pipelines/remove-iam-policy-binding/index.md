# gcloud deploy delivery-pipelines remove-iam-policy-binding  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/remove-iam-policy-binding)*

**NAME**

: **gcloud deploy delivery-pipelines remove-iam-policy-binding - remove an IAM policy binding for a Cloud Deploy delivery pipeline**

**SYNOPSIS**

: **`gcloud deploy delivery-pipelines remove-iam-policy-binding` [[`[DELIVERY_PIPELINE](https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/remove-iam-policy-binding#DELIVERY_PIPELINE)`] `[--region](https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/remove-iam-policy-binding#--region)`=`REGION`] `[--member](https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/remove-iam-policy-binding#--member)`=`PRINCIPAL` `[--role](https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/remove-iam-policy-binding#--role)`=`ROLE` [`[--all](https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/remove-iam-policy-binding#--all)`     | `[--condition](https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/remove-iam-policy-binding#--condition)`=[`KEY`=`VALUE`,…]     | `[--condition-from-file](https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/remove-iam-policy-binding#--condition-from-file)`=`PATH_TO_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/remove-iam-policy-binding#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Removes a policy binding to the IAM policy of a Cloud Deploy delivery pipeline.
One binding consists of a member and a role.
See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of the policy file format and contents.

**EXAMPLES**

: To remove an IAM policy binding for the role of 'roles/clouddeploy.operator' for
the user 'test-user@gmail.com' on 'my-pipeline' with the region 'us-central1',
run:

```
gcloud deploy delivery-pipelines remove-iam-policy-binding my-pipeline --region='us-central1' --member='user:test-user@gmail.com' --role='roles/clouddeploy.operator'
```

**POSITIONAL ARGUMENTS**

: **Delivery pipeline resource - The delivery pipeline for which to remove the IAM
policy binding. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `delivery_pipeline` on the command line with a
fully specified name;
- set the property `deploy/delivery_pipeline` with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**[`DELIVERY_PIPELINE`]**:
ID of the delivery_pipeline or fully qualified identifier for the
delivery_pipeline.
To set the `delivery_pipeline` attribute:

- provide the argument `delivery_pipeline` on the command line;
- set the property `deploy/delivery_pipeline`.

**--region**:
Location of the delivery_pipeline.
To set the `region` attribute:

- provide the argument `delivery_pipeline` on the command line with a
fully specified name;
- set the property `deploy/delivery_pipeline` with a fully specified
name;
- provide the argument `--region` on the command line;
- set the property `deploy/region`.**

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

: **--all**

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
gcloud alpha deploy delivery-pipelines remove-iam-policy-binding
```

```
gcloud beta deploy delivery-pipelines remove-iam-policy-binding
```