# gcloud transfer jobs create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create)*

**NAME**

: **gcloud transfer jobs create - create a Transfer Service transfer job**

**SYNOPSIS**

: **`gcloud transfer jobs create` `[SOURCE](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#SOURCE)` `[DESTINATION](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#DESTINATION)` [`[--name](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--name)`=`NAME` `[--description](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--description)`=`DESCRIPTION` `[--source-creds-file](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--source-creds-file)`=`SOURCE_CREDS_FILE` `[--source-agent-pool](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--source-agent-pool)`=`SOURCE_AGENT_POOL` `[--destination-agent-pool](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--destination-agent-pool)`=`DESTINATION_AGENT_POOL` `[--intermediate-storage-path](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--intermediate-storage-path)`=`INTERMEDIATE_STORAGE_PATH` `[--manifest-file](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--manifest-file)`=`MANIFEST_FILE`] [`[--event-stream-name](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--event-stream-name)`=`EVENT_STREAM_NAME` `[--event-stream-starts](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--event-stream-starts)`=`EVENT_STREAM_STARTS` `[--event-stream-expires](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--event-stream-expires)`=`EVENT_STREAM_EXPIRES`] [`[--do-not-run](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--do-not-run)` `[--schedule-starts](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--schedule-starts)`=`SCHEDULE_STARTS` `[--schedule-repeats-every](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--schedule-repeats-every)`=`SCHEDULE_REPEATS_EVERY` `[--schedule-repeats-until](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--schedule-repeats-until)`=`SCHEDULE_REPEATS_UNTIL`] [`[--include-prefixes](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--include-prefixes)`=[`INCLUDED_PREFIXES`,…] `[--exclude-prefixes](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--exclude-prefixes)`=[`EXCLUDED_PREFIXES`,…] `[--include-modified-before-absolute](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--include-modified-before-absolute)`=`INCLUDE_MODIFIED_BEFORE_ABSOLUTE` `[--include-modified-after-absolute](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--include-modified-after-absolute)`=`INCLUDE_MODIFIED_AFTER_ABSOLUTE` `[--include-modified-before-relative](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--include-modified-before-relative)`=`INCLUDE_MODIFIED_BEFORE_RELATIVE` `[--include-modified-after-relative](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--include-modified-after-relative)`=`INCLUDE_MODIFIED_AFTER_RELATIVE`] [`[--overwrite-when](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--overwrite-when)`=`OVERWRITE_WHEN` `[--delete-from](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--delete-from)`=`DELETE_FROM` `[--preserve-metadata](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--preserve-metadata)`=[`METADATA_FIELDS`,…] `[--custom-storage-class](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--custom-storage-class)`=`CUSTOM_STORAGE_CLASS`] [`[--notification-pubsub-topic](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--notification-pubsub-topic)`=`NOTIFICATION_PUBSUB_TOPIC` `[--notification-event-types](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--notification-event-types)`=[`EVENT_TYPES`,…] `[--notification-payload-format](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--notification-payload-format)`=`NOTIFICATION_PAYLOAD_FORMAT`] [`[--[no-]enable-posix-transfer-logs](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--[no-]enable-posix-transfer-logs)` `[--log-actions](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--log-actions)`=[`LOG_ACTIONS`,…] `[--log-action-states](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--log-action-states)`=[`LOG_ACTION_STATES`,…]] [`[--source-endpoint](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--source-endpoint)`=`SOURCE_ENDPOINT` `[--source-signing-region](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--source-signing-region)`=`SOURCE_SIGNING_REGION` `[--source-auth-method](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--source-auth-method)`=`SOURCE_AUTH_METHOD` `[--source-list-api](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--source-list-api)`=`SOURCE_LIST_API` `[--source-network-protocol](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--source-network-protocol)`=`SOURCE_NETWORK_PROTOCOL` `[--source-request-model](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--source-request-model)`=`SOURCE_REQUEST_MODEL` `[--s3-cloudfront-domain](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--s3-cloudfront-domain)`=`S3_CLOUDFRONT_DOMAIN`] [`[--no-async](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Transfer Service transfer job, allowing you to transfer data to Google
Cloud Storage on a one-time or recurring basis.

**EXAMPLES**

: To create a one-time, immediate transfer job to move data from Google Cloud
Storage bucket "foo" into the "baz" folder in Cloud Storage bucket "bar", run:

```
gcloud transfer jobs create gs://foo gs://bar/baz/
```

To create a transfer job to move data from an Amazon S3 bucket called "foo" to a
Google Cloud Storage bucket named "bar" that runs every day with custom name
"my-test-job", run:

```
gcloud transfer jobs create s3://foo gs://bar --name=my-test-job --source-creds-file=/examplefolder/creds.txt --schedule-repeats-every=1d
```

To create a one-time, immediate transfer job to move data between Google Cloud
Storage buckets "foo" and "bar" with filters to include objects that start with
prefixes "baz" and "qux"; and objects modified in the 24 hours before the
transfer started, run:

```
gcloud transfer jobs create gs://foo gs://bar/ --include-prefixes=baz,qux --include-modified-after-relative=1d
```

To create a one-time, immediate transfer job to move data from a directory with
absolute path "/foo/bar/" in the filesystem associated with agent pool "my-pool"
into Google Cloud Storage bucket "example-bucket", run:

```
gcloud transfer jobs create posix:///foo/bar/ gs://example-bucket --source-agent-pool=my-pool
```

**POSITIONAL ARGUMENTS**

: **`SOURCE`**:
The source of your data. Available sources and formatting information:
Public clouds -

- [Google Cloud Storage] gs://example-bucket/example-folder/
- [Amazon S3] s3://examplebucket/example-folder
- [Azure Blob Storage or Data Lake Storage] [http://examplestorageaccount.blob.core.windows.net/examplecontainer/examplefolder](http://examplestorageaccount.blob.core.windows.net/examplecontainer/examplefolder)

POSIX filesystem - Specify the `posix://` scheme followed by the
absolute path to the desired directory, starting from the root of the host
machine (denoted by a leading slash). For example:

- posix:///path/directory/

A file transfer agent must be installed on the POSIX filesystem, and you need an
agent pool flag on this `jobs` command to activate the agent.
Hadoop Distributed File System (HDFS) - Specify the `hdfs://` scheme
followed by the absolute path to the desired directory, starting from the root
of the file system (denoted by a leading slash). For example:

- hdfs:///path/directory/

Namenode details should not be included in the path specification, as they are
required separately during the agent installation process.
A file transfer agent must be installed, and you need an agent pool flag on this
`jobs` command to activate the agent.
Publicly-accessible objects - Specify the URL of a TSV file containing a list of
URLs of publicly-accessible objects. For example:

- [http://example.com/tsvfile](http://example.com/tsvfile)

**`DESTINATION`**:
The destination of your transferred data. Available destinations and formatting
information:
Google Cloud Storage - Specify the `gs://` scheme; name of the
bucket; and, if transferring to a folder, the path to the folder. For example:

- gs://example-bucket/example-folder/

POSIX filesystem - Specify the `posix://` scheme followed by the
absolute path to the desired directory, starting from the root of the host
machine (denoted by a leading slash). For example:

- posix:///path/directory/

A file transfer agent must be installed on the POSIX filesystem, and you need an
agent pool flag on this `jobs` command to activate the agent.

**FLAGS**

: **--name**

**--event-stream-name**

**--do-not-run**

**--include-prefixes**

**--overwrite-when**

**--notification-pubsub-topic**

**--[no-]enable-posix-transfer-logs**

**--source-endpoint**

**--no-async**

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
gcloud alpha transfer jobs create
```