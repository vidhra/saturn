# gcloud pubsub topics create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create)*

**NAME**

: **gcloud pubsub topics create - creates one or more Cloud Pub/Sub topics**

**SYNOPSIS**

: **`gcloud pubsub topics create` `[TOPIC](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#TOPIC)` [`[TOPIC](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#TOPIC)` …] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--message-retention-duration](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--message-retention-duration)`=`MESSAGE_RETENTION_DURATION`] [`[--message-transforms-file](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--message-transforms-file)`=`MESSAGE_TRANSFORMS_FILE`] [`[--ingestion-log-severity](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--ingestion-log-severity)`=`INGESTION_LOG_SEVERITY` `[--aws-msk-ingestion-aws-role-arn](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--aws-msk-ingestion-aws-role-arn)`=`AWS_MSK_INGESTION_AWS_ROLE_ARN` `[--aws-msk-ingestion-cluster-arn](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--aws-msk-ingestion-cluster-arn)`=`AWS_MSK_INGESTION_CLUSTER_ARN` `[--aws-msk-ingestion-service-account](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--aws-msk-ingestion-service-account)`=`AWS_MSK_INGESTION_SERVICE_ACCOUNT` `[--aws-msk-ingestion-topic](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--aws-msk-ingestion-topic)`=`AWS_MSK_INGESTION_TOPIC`     | `[--azure-event-hubs-ingestion-client-id](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--azure-event-hubs-ingestion-client-id)`=`AZURE_EVENT_HUBS_INGESTION_CLIENT_ID` `[--azure-event-hubs-ingestion-event-hub](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--azure-event-hubs-ingestion-event-hub)`=`AZURE_EVENT_HUBS_INGESTION_EVENT_HUB` `[--azure-event-hubs-ingestion-namespace](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--azure-event-hubs-ingestion-namespace)`=`AZURE_EVENT_HUBS_INGESTION_NAMESPACE` `[--azure-event-hubs-ingestion-resource-group](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--azure-event-hubs-ingestion-resource-group)`=`AZURE_EVENT_HUBS_INGESTION_RESOURCE_GROUP` `[--azure-event-hubs-ingestion-service-account](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--azure-event-hubs-ingestion-service-account)`=`AZURE_EVENT_HUBS_INGESTION_SERVICE_ACCOUNT` `[--azure-event-hubs-ingestion-subscription-id](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--azure-event-hubs-ingestion-subscription-id)`=`AZURE_EVENT_HUBS_INGESTION_SUBSCRIPTION_ID` `[--azure-event-hubs-ingestion-tenant-id](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--azure-event-hubs-ingestion-tenant-id)`=`AZURE_EVENT_HUBS_INGESTION_TENANT_ID`     | [`[--cloud-storage-ingestion-bucket](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--cloud-storage-ingestion-bucket)`=`CLOUD_STORAGE_INGESTION_BUCKET` `[--cloud-storage-ingestion-input-format](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--cloud-storage-ingestion-input-format)`=`INPUT_FORMAT` : `[--cloud-storage-ingestion-text-delimiter](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--cloud-storage-ingestion-text-delimiter)`=`CLOUD_STORAGE_INGESTION_TEXT_DELIMITER` `[--cloud-storage-ingestion-minimum-object-create-time](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--cloud-storage-ingestion-minimum-object-create-time)`=`CLOUD_STORAGE_INGESTION_MINIMUM_OBJECT_CREATE_TIME` `[--cloud-storage-ingestion-match-glob](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--cloud-storage-ingestion-match-glob)`=`CLOUD_STORAGE_INGESTION_MATCH_GLOB`]     | `[--confluent-cloud-ingestion-bootstrap-server](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--confluent-cloud-ingestion-bootstrap-server)`=`CONFLUENT_CLOUD_INGESTION_BOOTSTRAP_SERVER` `[--confluent-cloud-ingestion-cluster-id](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--confluent-cloud-ingestion-cluster-id)`=`CONFLUENT_CLOUD_INGESTION_CLUSTER_ID` `[--confluent-cloud-ingestion-identity-pool-id](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--confluent-cloud-ingestion-identity-pool-id)`=`CONFLUENT_CLOUD_INGESTION_IDENTITY_POOL_ID` `[--confluent-cloud-ingestion-service-account](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--confluent-cloud-ingestion-service-account)`=`CONFLUENT_CLOUD_INGESTION_SERVICE_ACCOUNT` `[--confluent-cloud-ingestion-topic](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--confluent-cloud-ingestion-topic)`=`CONFLUENT_CLOUD_INGESTION_TOPIC`     | `[--kinesis-ingestion-consumer-arn](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--kinesis-ingestion-consumer-arn)`=`KINESIS_INGESTION_CONSUMER_ARN` `[--kinesis-ingestion-role-arn](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--kinesis-ingestion-role-arn)`=`KINESIS_INGESTION_ROLE_ARN` `[--kinesis-ingestion-service-account](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--kinesis-ingestion-service-account)`=`KINESIS_INGESTION_SERVICE_ACCOUNT` `[--kinesis-ingestion-stream-arn](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--kinesis-ingestion-stream-arn)`=`KINESIS_INGESTION_STREAM_ARN`] [`[--message-encoding](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--message-encoding)`=`ENCODING` (`[--schema](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--schema)`=`SCHEMA` : `[--schema-project](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--schema-project)`=`SCHEMA_PROJECT`) : `[--first-revision-id](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--first-revision-id)`=`FIRST_REVISION_ID` `[--last-revision-id](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--last-revision-id)`=`LAST_REVISION_ID`] [`[--message-storage-policy-allowed-regions](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--message-storage-policy-allowed-regions)`=[`REGION`,…] : `[--message-storage-policy-enforce-in-transit](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--message-storage-policy-enforce-in-transit)`] [`[--topic-encryption-key](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--topic-encryption-key)`=`TOPIC_ENCRYPTION_KEY` : `[--topic-encryption-key-keyring](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--topic-encryption-key-keyring)`=`TOPIC_ENCRYPTION_KEY_KEYRING` `[--topic-encryption-key-location](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--topic-encryption-key-location)`=`TOPIC_ENCRYPTION_KEY_LOCATION` `[--topic-encryption-key-project](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#--topic-encryption-key-project)`=`TOPIC_ENCRYPTION_KEY_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates one or more Cloud Pub/Sub topics.

**EXAMPLES**

: To create a Cloud Pub/Sub topic, run:

```
gcloud pubsub topics create mytopic
```

**POSITIONAL ARGUMENTS**

: **Topic resource - One or more topics to create. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `topic` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TOPIC` [`TOPIC` …]**:
IDs of the topics or fully qualified identifiers for the topics.
To set the `topic` attribute:

- provide the argument `topic` on the command line.**

**FLAGS**

: **--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--message-retention-duration**:
Indicates the minimum duration to retain a message after it is published to the
topic. If this field is set, messages published to the topic in the last
MESSAGE_RETENTION_DURATION are always available to subscribers. For instance, it
allows any attached subscription to seek to a timestamp that is up to
MESSAGE_RETENTION_DURATION in the past. If this field is not set, message
retention is controlled by settings on individual subscriptions. The minimum is
10 minutes and the maximum is 31 days. Valid values are strings of the form
INTEGER[UNIT], where UNIT is one of "s", "m", "h", and "d" for seconds, minutes,
hours, and days, respectively. If the unit is omitted, seconds is assumed.

**--message-transforms-file**:
Path to YAML or JSON file containing message transforms.

**--ingestion-log-severity**

**--message-encoding**

**--message-storage-policy-allowed-regions**

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
gcloud alpha pubsub topics create
```

```
gcloud beta pubsub topics create
```