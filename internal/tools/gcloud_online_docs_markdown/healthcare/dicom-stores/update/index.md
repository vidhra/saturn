# gcloud healthcare dicom-stores update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/update](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/update)*

**NAME**

: **gcloud healthcare dicom-stores update - update a Cloud Healthcare API DICOM store**

**SYNOPSIS**

: **`gcloud healthcare dicom-stores update` (`[DICOM_STORE](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/update#DICOM_STORE)` : `[--dataset](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/update#--dataset)`=`DATASET` `[--location](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/update#--location)`=`LOCATION`) [`[--pubsub-topic](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/update#--pubsub-topic)`=`PUBSUB_TOPIC`] [`[--send-for-bulk-import](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/update#--send-for-bulk-import)`] [`[--stream-configs](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/update#--stream-configs)`=`STREAM_CONFIGS`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Cloud Healthcare API DICOM store.

**EXAMPLES**

: To update the Cloud Pub/Sub topic on a dicom store 'test-dicom-store', run:

```
gcloud healthcare dicom-stores update test-dicom-store --pubsub-topic=projects/my-project/topics/test-pubsub-topic --dataset=test-dataset
```

**POSITIONAL ARGUMENTS**

: **DicomStore resource - Cloud Healthcare API DICOM to update. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `dicom_store` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DICOM_STORE`**:
ID of the dicomStore or fully qualified identifier for the dicomStore.
To set the `dicom_store` attribute:

- provide the argument `dicom_store` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--dataset**:
Cloud Healthcare dataset.
To set the `dataset` attribute:

- provide the argument `dicom_store` on the command line with a fully
specified name;
- provide the argument `--dataset` on the command line.

**--location**:
Google Cloud location.
To set the `location` attribute:

- provide the argument `dicom_store` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `healthcare/location`.**

**FLAGS**

: **--pubsub-topic**:
Google Cloud Pub/Sub topic to send updates to.
Note: A topic must be created before publishing or subscribing to it. For
instructions on creating topics, refer to: [https://cloud.google.com/pubsub/docs/admin#create_a_topic](https://cloud.google.com/pubsub/docs/admin#create_a_topic)

**--send-for-bulk-import**:
Indicates whether or not to send Cloud Pub/Sub notifications on bulk import.
Only supported for DICOM imports.

**--stream-configs**:
Configuration that indicates the BigQuery destinations for streaming instances
of a DICOM store. To specify StreamConfigs, list all BigQuery destinations into
one string separated by comma. (e.g., --stream-configs
bq://{bigqueryProjectId1}.{bigqueryDatasetId1}.{bigqueryTableId1},bq://{bigqueryProjectId2}.{bigqueryDatasetId2}.{bigqueryTableId2}).

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

: This command uses the `healthcare/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/healthcare](https://cloud.google.com/healthcare)

**NOTES**

: These variants are also available:

```
gcloud alpha healthcare dicom-stores update
```

```
gcloud beta healthcare dicom-stores update
```