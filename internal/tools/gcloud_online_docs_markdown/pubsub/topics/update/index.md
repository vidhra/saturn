# gcloud pubsub topics update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update)*

**NAME**

: **gcloud pubsub topics update - updates an existing Cloud Pub/Sub topic**

**SYNOPSIS**

: **`gcloud pubsub topics update` `[TOPIC](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#TOPIC)` [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-ingestion-data-source-settings](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--clear-ingestion-data-source-settings)`     | `[--ingestion-log-severity](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--ingestion-log-severity)`=`INGESTION_LOG_SEVERITY` `[--aws-msk-ingestion-aws-role-arn](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--aws-msk-ingestion-aws-role-arn)`=`AWS_MSK_INGESTION_AWS_ROLE_ARN` `[--aws-msk-ingestion-cluster-arn](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--aws-msk-ingestion-cluster-arn)`=`AWS_MSK_INGESTION_CLUSTER_ARN` `[--aws-msk-ingestion-service-account](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--aws-msk-ingestion-service-account)`=`AWS_MSK_INGESTION_SERVICE_ACCOUNT` `[--aws-msk-ingestion-topic](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--aws-msk-ingestion-topic)`=`AWS_MSK_INGESTION_TOPIC`     | `[--azure-event-hubs-ingestion-client-id](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--azure-event-hubs-ingestion-client-id)`=`AZURE_EVENT_HUBS_INGESTION_CLIENT_ID` `[--azure-event-hubs-ingestion-event-hub](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--azure-event-hubs-ingestion-event-hub)`=`AZURE_EVENT_HUBS_INGESTION_EVENT_HUB` `[--azure-event-hubs-ingestion-namespace](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--azure-event-hubs-ingestion-namespace)`=`AZURE_EVENT_HUBS_INGESTION_NAMESPACE` `[--azure-event-hubs-ingestion-resource-group](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--azure-event-hubs-ingestion-resource-group)`=`AZURE_EVENT_HUBS_INGESTION_RESOURCE_GROUP` `[--azure-event-hubs-ingestion-service-account](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--azure-event-hubs-ingestion-service-account)`=`AZURE_EVENT_HUBS_INGESTION_SERVICE_ACCOUNT` `[--azure-event-hubs-ingestion-subscription-id](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--azure-event-hubs-ingestion-subscription-id)`=`AZURE_EVENT_HUBS_INGESTION_SUBSCRIPTION_ID` `[--azure-event-hubs-ingestion-tenant-id](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--azure-event-hubs-ingestion-tenant-id)`=`AZURE_EVENT_HUBS_INGESTION_TENANT_ID`     | [`[--cloud-storage-ingestion-bucket](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--cloud-storage-ingestion-bucket)`=`CLOUD_STORAGE_INGESTION_BUCKET` `[--cloud-storage-ingestion-input-format](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--cloud-storage-ingestion-input-format)`=`INPUT_FORMAT` : `[--cloud-storage-ingestion-text-delimiter](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--cloud-storage-ingestion-text-delimiter)`=`CLOUD_STORAGE_INGESTION_TEXT_DELIMITER` `[--cloud-storage-ingestion-minimum-object-create-time](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--cloud-storage-ingestion-minimum-object-create-time)`=`CLOUD_STORAGE_INGESTION_MINIMUM_OBJECT_CREATE_TIME` `[--cloud-storage-ingestion-match-glob](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--cloud-storage-ingestion-match-glob)`=`CLOUD_STORAGE_INGESTION_MATCH_GLOB`]     | `[--confluent-cloud-ingestion-bootstrap-server](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--confluent-cloud-ingestion-bootstrap-server)`=`CONFLUENT_CLOUD_INGESTION_BOOTSTRAP_SERVER` `[--confluent-cloud-ingestion-cluster-id](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--confluent-cloud-ingestion-cluster-id)`=`CONFLUENT_CLOUD_INGESTION_CLUSTER_ID` `[--confluent-cloud-ingestion-identity-pool-id](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--confluent-cloud-ingestion-identity-pool-id)`=`CONFLUENT_CLOUD_INGESTION_IDENTITY_POOL_ID` `[--confluent-cloud-ingestion-service-account](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--confluent-cloud-ingestion-service-account)`=`CONFLUENT_CLOUD_INGESTION_SERVICE_ACCOUNT` `[--confluent-cloud-ingestion-topic](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--confluent-cloud-ingestion-topic)`=`CONFLUENT_CLOUD_INGESTION_TOPIC`     | `[--kinesis-ingestion-consumer-arn](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--kinesis-ingestion-consumer-arn)`=`KINESIS_INGESTION_CONSUMER_ARN` `[--kinesis-ingestion-role-arn](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--kinesis-ingestion-role-arn)`=`KINESIS_INGESTION_ROLE_ARN` `[--kinesis-ingestion-service-account](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--kinesis-ingestion-service-account)`=`KINESIS_INGESTION_SERVICE_ACCOUNT` `[--kinesis-ingestion-stream-arn](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--kinesis-ingestion-stream-arn)`=`KINESIS_INGESTION_STREAM_ARN`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--remove-labels)`=[`KEY`,…]] [`[--clear-message-retention-duration](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--clear-message-retention-duration)`     | `[--message-retention-duration](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--message-retention-duration)`=`MESSAGE_RETENTION_DURATION`] [`[--clear-message-transforms](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--clear-message-transforms)`     | `[--message-transforms-file](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--message-transforms-file)`=`MESSAGE_TRANSFORMS_FILE`] [`[--clear-schema-settings](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--clear-schema-settings)`     | [`[--message-encoding](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--message-encoding)`=`ENCODING` (`[--schema](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--schema)`=`SCHEMA` : `[--schema-project](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--schema-project)`=`SCHEMA_PROJECT`) : `[--first-revision-id](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--first-revision-id)`=`FIRST_REVISION_ID` `[--last-revision-id](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--last-revision-id)`=`LAST_REVISION_ID`]] [`[--recompute-message-storage-policy](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--recompute-message-storage-policy)`     | [`[--message-storage-policy-allowed-regions](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--message-storage-policy-allowed-regions)`=[`REGION`,…] : `[--message-storage-policy-enforce-in-transit](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--message-storage-policy-enforce-in-transit)`]] [`[--topic-encryption-key](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--topic-encryption-key)`=`TOPIC_ENCRYPTION_KEY` : `[--topic-encryption-key-keyring](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--topic-encryption-key-keyring)`=`TOPIC_ENCRYPTION_KEY_KEYRING` `[--topic-encryption-key-location](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--topic-encryption-key-location)`=`TOPIC_ENCRYPTION_KEY_LOCATION` `[--topic-encryption-key-project](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#--topic-encryption-key-project)`=`TOPIC_ENCRYPTION_KEY_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates an existing Cloud Pub/Sub topic.

**EXAMPLES**

: To update existing labels on a Cloud Pub/Sub topic, run:

```
gcloud pubsub topics update mytopic --update-labels=KEY1=VAL1,KEY2=VAL2
```

To clear all labels on a Cloud Pub/Sub topic, run:

```
gcloud pubsub topics update mytopic --clear-labels
```

To remove an existing label on a Cloud Pub/Sub topic, run:

```
gcloud pubsub topics update mytopic --remove-labels=KEY1,KEY2
```

To enable customer-managed encryption for a Cloud Pub/Sub topic by protecting
message data with a Cloud KMS CryptoKey, run:

```
gcloud pubsub topics update mytopic --topic-encryption-key=projects/PROJECT_ID/locations/KMS_LOCATION/keyRings/KEYRING/cryptoKeys/KEY
```

To enable or update retention on a Cloud Pub/Sub topic, run:

```
gcloud pubsub topics update mytopic --message-retention-duration=MESSAGE_RETENTION_DURATION
```

To disable retention on a Cloud Pub/Sub topic, run:

```
gcloud pubsub topics update mytopic --clear-message-retention-duration
```

To update a Cloud Pub/Sub topic's message storage policy, run:

```
gcloud pubsub topics update mytopic --message-storage-policy-allowed-regions=some-cloud-region1,some-cloud-region2
```

To recompute a Cloud Pub/Sub topic's message storage policy based on your
organization's "Resource Location Restriction" policy, run:

```
gcloud pubsub topics update mytopic --recompute-message-storage-policy
```

To enforce both at-rest and in-transit guarantees for messages published to the
topic, run:

```
gcloud pubsub topics update mytopic --message-storage-policy-allowed-regions=some-cloud-region1,some-cloud-region2 --message-storage-policy-enforce-in-transit
```

**POSITIONAL ARGUMENTS**

: **Topic resource - Name of the topic to update. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `topic` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TOPIC`**:
ID of the topic or fully qualified identifier for the topic.
To set the `topic` attribute:

- provide the argument `topic` on the command line.**

**FLAGS**

: **--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-ingestion-data-source-settings**

**--clear-labels**

**--clear-message-retention-duration**

**--clear-message-transforms**

**--clear-schema-settings**

**--recompute-message-storage-policy**

**--topic-encryption-key**

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
gcloud alpha pubsub topics update
```

```
gcloud beta pubsub topics update
```