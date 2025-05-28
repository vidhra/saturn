# gcloud pubsub subscriptions modify-push-config  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/modify-push-config](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/modify-push-config)*

**NAME**

: **gcloud pubsub subscriptions modify-push-config - modifies the push configuration of a Cloud Pub/Sub subscription**

**SYNOPSIS**

: **`gcloud pubsub subscriptions modify-push-config` `[SUBSCRIPTION](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/modify-push-config#SUBSCRIPTION)` `[--push-endpoint](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/modify-push-config#--push-endpoint)`=`PUSH_ENDPOINT` [`[--push-auth-service-account](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/modify-push-config#--push-auth-service-account)`=`SERVICE_ACCOUNT_EMAIL`] [`[--push-auth-token-audience](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/modify-push-config#--push-auth-token-audience)`=`OPTIONAL_AUDIENCE_OVERRIDE`] [`[--push-no-wrapper](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/modify-push-config#--push-no-wrapper)` : `[--push-no-wrapper-write-metadata](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/modify-push-config#--push-no-wrapper-write-metadata)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/modify-push-config#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Modifies the push configuration of a Cloud Pub/Sub subscription.

**POSITIONAL ARGUMENTS**

: **Subscription resource - Name of the subscription to modify. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
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

**REQUIRED FLAGS**

: **--push-endpoint**:
A URL to use as the endpoint for this subscription. This will also automatically
set the subscription type to PUSH.

**OPTIONAL FLAGS**

: **--push-auth-service-account**:
Service account email used as the identity for the generated Open ID Connect
token for authenticated push.

**--push-auth-token-audience**:
Audience used in the generated Open ID Connect token for authenticated push. If
not specified, it will be set to the push-endpoint.

**--push-no-wrapper**

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
gcloud alpha pubsub subscriptions modify-push-config
```

```
gcloud beta pubsub subscriptions modify-push-config
```