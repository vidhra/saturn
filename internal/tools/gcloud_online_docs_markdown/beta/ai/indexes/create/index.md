# gcloud beta ai indexes create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/ai/indexes/create](https://cloud.google.com/sdk/gcloud/reference/beta/ai/indexes/create)*

**NAME**

: **gcloud beta ai indexes create - create a new Vertex AI index**

**SYNOPSIS**

: **`gcloud beta ai indexes create` `[--display-name](https://cloud.google.com/sdk/gcloud/reference/beta/ai/indexes/create#--display-name)`=`DISPLAY_NAME` `[--metadata-file](https://cloud.google.com/sdk/gcloud/reference/beta/ai/indexes/create#--metadata-file)`=`METADATA_FILE` [`[--description](https://cloud.google.com/sdk/gcloud/reference/beta/ai/indexes/create#--description)`=`DESCRIPTION`] [`[--encryption-kms-key-name](https://cloud.google.com/sdk/gcloud/reference/beta/ai/indexes/create#--encryption-kms-key-name)`=`ENCRYPTION_KMS_KEY_NAME`] [`[--index-update-method](https://cloud.google.com/sdk/gcloud/reference/beta/ai/indexes/create#--index-update-method)`=`INDEX_UPDATE_METHOD`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/beta/ai/indexes/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--metadata-schema-uri](https://cloud.google.com/sdk/gcloud/reference/beta/ai/indexes/create#--metadata-schema-uri)`=`METADATA_SCHEMA_URI`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/beta/ai/indexes/create#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/ai/indexes/create#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create an index under project `example` in region
`us-central1`, encrypted with KMS key `kms-key-name`, run:

```
gcloud beta ai indexes create --display-name=index --description=test --metadata-file=path/to/your/metadata.json --project=example --region=us-central1 --encryption-kms-key-name=kms-key-name
```

**REQUIRED FLAGS**

: **--display-name**:
Display name of the index.

**--metadata-file**:
Path to a local JSON file that contains the additional metadata information
about the index.

**OPTIONAL FLAGS**

: **--description**:
Description of the index.

**--encryption-kms-key-name**:
The Cloud KMS resource identifier of the customer managed encryption key used to
protect a resource. Has the form:
projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key.
The key needs to be in the same region as where the compute resource is created.

**--index-update-method**:
The update method to use with this index. Choose `stream-update` or
`batch-update` (case insensitive). If not set, batch update will be
used by default. `INDEX_UPDATE_METHOD` must be one of:

**`batch-update`**:
can update index with `[gcloud ai indexes
update](https://cloud.google.com/sdk/gcloud/reference/ai/indexes/update)` usingdatapoints files on Cloud Storage.

**`stream-update`**:
can update datapoints with `upsert-datapoints`
and`delete-datapoints`and will be applied nearly real-time.`

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.`

**--metadata-schema-uri**:
Points to a YAML file stored on Google Cloud Storage describing additional
information about index.

**Region resource - Cloud region to create index. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the project`attribute:

- provide the argument`--region`on the command line with a fully
specified name;

set the property`ai/region`with a fully specified name;

choose one from the prompted list of available regions with a fully specified
name;
provide the argument`--project`on the command line;

set the property`core/project`.

**--region**:
ID of the region or fully qualified identifier for the region.
To set the`region`attribute:

- provide the argument`--region`on the command line;

set the property`ai/region`;

choose one from the prompted list of available regions.`**