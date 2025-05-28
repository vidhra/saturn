# gcloud pubsub subscriptions set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/set-iam-policy)*

**NAME**

: **gcloud pubsub subscriptions set-iam-policy - set IAM policy for a subscription**

**SYNOPSIS**

: **`gcloud pubsub subscriptions set-iam-policy` `[SUBSCRIPTION](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/set-iam-policy#SUBSCRIPTION)` `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/set-iam-policy#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Set the IAM policy for a Cloud Pub/Sub Subscription.

**EXAMPLES**

: The following command will read an IAM policy from 'policy.json' and set it for
a subscription with 'my-subscription' as the identifier:

```
gcloud pubsub subscriptions set-iam-policy my-subscription policy.json
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of the policy file format and contents.

**POSITIONAL ARGUMENTS**

: **Subscription resource - Name of the subscription to set an IAM policy on. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `subscription` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SUBSCRIPTION`**:
ID of the subscription or fully qualified identifier for the subscription.
To set the `subscription` attribute:

- provide the argument `subscription` on the command line.**

**`POLICY_FILE`**:
JSON or YAML file with the IAM policy

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
gcloud alpha pubsub subscriptions set-iam-policy
```

```
gcloud beta pubsub subscriptions set-iam-policy
```