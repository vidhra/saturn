# gcloud healthcare dicom-stores delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/delete](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/delete)*

**NAME**

: **gcloud healthcare dicom-stores delete - delete a Cloud Healthcare API DICOM store**

**SYNOPSIS**

: **`gcloud healthcare dicom-stores delete` (`[DICOM_STORE](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/delete#DICOM_STORE)` : `[--dataset](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/delete#--dataset)`=`DATASET` `[--location](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/delete#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Cloud Healthcare API DICOM store.

**EXAMPLES**

: To delete the dicom-store 'test-dicom-store', run:

```
gcloud healthcare dicom-stores delete test-dicom-store --dataset=test-dataset
```

**POSITIONAL ARGUMENTS**

: **DicomStore resource - Cloud Healthcare API DICOM store to delete. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
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
gcloud alpha healthcare dicom-stores delete
```

```
gcloud beta healthcare dicom-stores delete
```