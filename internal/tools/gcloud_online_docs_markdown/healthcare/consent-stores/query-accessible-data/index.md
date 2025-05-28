# gcloud healthcare consent-stores query-accessible-data  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/query-accessible-data](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/query-accessible-data)*

**NAME**

: **gcloud healthcare consent-stores query-accessible-data - queries all accessible data IDs**

**SYNOPSIS**

: **`gcloud healthcare consent-stores query-accessible-data` (`[CONSENT_STORE](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/query-accessible-data#CONSENT_STORE)` : `[--dataset](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/query-accessible-data#--dataset)`=`DATASET` `[--location](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/query-accessible-data#--location)`=`LOCATION`) `[--gcs-uri](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/query-accessible-data#--gcs-uri)`=`GCS_URI` [`[--async](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/query-accessible-data#--async)`] [`[--request-attributes](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/query-accessible-data#--request-attributes)`=[`KEY`=`VALUE`,…]] [`[--resource-attributes](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/query-accessible-data#--resource-attributes)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/query-accessible-data#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Queries all data IDs that are consented for a given use in the given Cloud
Healthcare API consent store and writes them to a specified destination.

**EXAMPLES**

: To query all data IDs in the consent-store 'test-consent-store' that can be used
given request attributes {"organization":"admins", "use_case":"research"} and
resource attributes {"anonymity":"identified"}, and write the result file to
"gs://test-bucket/folder", run:

```
gcloud healthcare consent-stores query-accessible-data test-consent-store --gcs-uri=gs://test-bucket/folder --request-attributes=organization=admins,use_case=research --resource-attributes=anonymity=identified --dataset=test-dataset
```

**POSITIONAL ARGUMENTS**

: **ConsentStore resource - Cloud Healthcare API consent store to retrieve user data
mappings from. The arguments in this group can be used to specify the attributes
of this resource. (NOTE) Some attributes are not given arguments in this group
but can be set in other ways.
To set the `project` attribute:

- provide the argument `consent_store` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CONSENT_STORE`**:
ID of the consentStore or fully qualified identifier for the consentStore.
To set the `consent_store` attribute:

- provide the argument `consent_store` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--dataset**:
Cloud Healthcare dataset.
To set the `dataset` attribute:

- provide the argument `consent_store` on the command line with a fully
specified name;
- provide the argument `--dataset` on the command line.

**--location**:
Google Cloud location.
To set the `location` attribute:

- provide the argument `consent_store` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `healthcare/location`.**

**REQUIRED FLAGS**

: **--gcs-uri**:
The Cloud Storage destination for the result file. The Cloud Healthcare API
service account must have the `roles/storage.objectAdmin` Cloud IAM
role for this Cloud Storage location.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--request-attributes**:
Comma-separated list of request attributes associated with this access request.
Each attribute has the form "KEY=VALUE".

**--resource-attributes**:
Comma-separated list of resources attributes associated with the type of data
being requested. Each attribute has the form "KEY=VALUE". If no values are
specified, then all data types are included in the output.

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
gcloud alpha healthcare consent-stores query-accessible-data
```

```
gcloud beta healthcare consent-stores query-accessible-data
```