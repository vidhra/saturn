# gcloud transfer jobs update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update)*

**NAME**

: **gcloud transfer jobs update - update a Transfer Service transfer job**

**SYNOPSIS**

: **`gcloud transfer jobs update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#NAME)` [`[--status](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--status)`=`STATUS` `[--source](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--source)`=`SOURCE` `[--destination](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--destination)`=`DESTINATION` `[--clear-description](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-description)` `[--clear-source-creds-file](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-source-creds-file)` `[--clear-source-agent-pool](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-source-agent-pool)` `[--clear-destination-agent-pool](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-destination-agent-pool)` `[--clear-intermediate-storage-path](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-intermediate-storage-path)` `[--clear-manifest-file](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-manifest-file)` `[--description](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--description)`=`DESCRIPTION` `[--source-creds-file](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--source-creds-file)`=`SOURCE_CREDS_FILE` `[--source-agent-pool](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--source-agent-pool)`=`SOURCE_AGENT_POOL` `[--destination-agent-pool](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--destination-agent-pool)`=`DESTINATION_AGENT_POOL` `[--intermediate-storage-path](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--intermediate-storage-path)`=`INTERMEDIATE_STORAGE_PATH` `[--manifest-file](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--manifest-file)`=`MANIFEST_FILE`] [`[--event-stream-name](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--event-stream-name)`=`EVENT_STREAM_NAME` `[--event-stream-starts](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--event-stream-starts)`=`EVENT_STREAM_STARTS` `[--event-stream-expires](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--event-stream-expires)`=`EVENT_STREAM_EXPIRES` `[--clear-event-stream](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-event-stream)`] [`[--clear-schedule](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-schedule)` `[--schedule-starts](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--schedule-starts)`=`SCHEDULE_STARTS` `[--schedule-repeats-every](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--schedule-repeats-every)`=`SCHEDULE_REPEATS_EVERY` `[--schedule-repeats-until](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--schedule-repeats-until)`=`SCHEDULE_REPEATS_UNTIL`] [`[--clear-include-prefixes](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-include-prefixes)` `[--clear-exclude-prefixes](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-exclude-prefixes)` `[--clear-include-modified-before-absolute](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-include-modified-before-absolute)` `[--clear-include-modified-after-absolute](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-include-modified-after-absolute)` `[--clear-include-modified-before-relative](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-include-modified-before-relative)` `[--clear-include-modified-after-relative](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-include-modified-after-relative)` `[--include-prefixes](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--include-prefixes)`=[`INCLUDED_PREFIXES`,…] `[--exclude-prefixes](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--exclude-prefixes)`=[`EXCLUDED_PREFIXES`,…] `[--include-modified-before-absolute](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--include-modified-before-absolute)`=`INCLUDE_MODIFIED_BEFORE_ABSOLUTE` `[--include-modified-after-absolute](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--include-modified-after-absolute)`=`INCLUDE_MODIFIED_AFTER_ABSOLUTE` `[--include-modified-before-relative](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--include-modified-before-relative)`=`INCLUDE_MODIFIED_BEFORE_RELATIVE` `[--include-modified-after-relative](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--include-modified-after-relative)`=`INCLUDE_MODIFIED_AFTER_RELATIVE`] [`[--clear-delete-from](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-delete-from)` `[--clear-preserve-metadata](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-preserve-metadata)` `[--clear-custom-storage-class](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-custom-storage-class)` `[--overwrite-when](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--overwrite-when)`=`OVERWRITE_WHEN` `[--delete-from](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--delete-from)`=`DELETE_FROM` `[--preserve-metadata](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--preserve-metadata)`=[`METADATA_FIELDS`,…] `[--custom-storage-class](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--custom-storage-class)`=`CUSTOM_STORAGE_CLASS`] [`[--clear-notification-config](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-notification-config)` `[--clear-notification-event-types](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-notification-event-types)` `[--notification-pubsub-topic](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--notification-pubsub-topic)`=`NOTIFICATION_PUBSUB_TOPIC` `[--notification-event-types](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--notification-event-types)`=[`EVENT_TYPES`,…] `[--notification-payload-format](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--notification-payload-format)`=`NOTIFICATION_PAYLOAD_FORMAT`] [`[--clear-log-config](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-log-config)` `[--[no-]enable-posix-transfer-logs](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--[no-]enable-posix-transfer-logs)` `[--log-actions](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--log-actions)`=[`LOG_ACTIONS`,…] `[--log-action-states](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--log-action-states)`=[`LOG_ACTION_STATES`,…]] [`[--source-endpoint](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--source-endpoint)`=`SOURCE_ENDPOINT` `[--source-signing-region](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--source-signing-region)`=`SOURCE_SIGNING_REGION` `[--source-auth-method](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--source-auth-method)`=`SOURCE_AUTH_METHOD` `[--source-list-api](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--source-list-api)`=`SOURCE_LIST_API` `[--source-network-protocol](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--source-network-protocol)`=`SOURCE_NETWORK_PROTOCOL` `[--source-request-model](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--source-request-model)`=`SOURCE_REQUEST_MODEL` `[--s3-cloudfront-domain](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--s3-cloudfront-domain)`=`S3_CLOUDFRONT_DOMAIN` `[--clear-source-endpoint](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-source-endpoint)` `[--clear-source-signing-region](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-source-signing-region)` `[--clear-source-auth-method](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-source-auth-method)` `[--clear-source-list-api](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-source-list-api)` `[--clear-source-network-protocol](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-source-network-protocol)` `[--clear-source-request-model](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-source-request-model)` `[--clear-s3-cloudfront-domain](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#--clear-s3-cloudfront-domain)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Transfer Service transfer job.

**EXAMPLES**

: To disable transfer job 'foo', run:

```
gcloud transfer jobs update foo --status=disabled
```

To remove the schedule for transfer job 'foo' so that it will only run when you
manually start it, run:

```
gcloud transfer jobs update foo --clear-schedule
```

To clear the values from the `include=prefixes` object condition in
transfer job 'foo', run:

```
gcloud transfer jobs update foo --clear-include-prefixes
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the transfer job you'd like to update.

**FLAGS**

: **--status**

**--event-stream-name**

**--clear-schedule**

**--clear-include-prefixes**

**--clear-delete-from**

**--clear-notification-config**

**--clear-log-config**

**--source-endpoint**

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

: This variant is also available:

```
gcloud alpha transfer jobs update
```