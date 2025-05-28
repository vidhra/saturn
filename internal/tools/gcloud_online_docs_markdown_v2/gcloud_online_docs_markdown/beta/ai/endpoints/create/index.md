# gcloud beta ai endpoints create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/create](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/create)*

**NAME**

: **gcloud beta ai endpoints create - create a new Vertex AI endpoint**

**SYNOPSIS**

: **`gcloud beta ai endpoints create` `[--display-name](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/create#--display-name)`=`DISPLAY_NAME` [`[--description](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/create#--description)`=`DESCRIPTION`] [`[--encryption-kms-key-name](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/create#--encryption-kms-key-name)`=`ENCRYPTION_KMS_KEY_NAME`] [`[--endpoint-id](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/create#--endpoint-id)`=`ENDPOINT_ID`] [`[--gdce-zone](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/create#--gdce-zone)`=`GDCE_ZONE`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--network](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/create#--network)`=`NETWORK`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/create#--region)`=`REGION`] [`[--request-response-logging-rate](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/create#--request-response-logging-rate)`=`REQUEST_RESPONSE_LOGGING_RATE` `[--request-response-logging-table](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/create#--request-response-logging-table)`=`REQUEST_RESPONSE_LOGGING_TABLE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/create#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create an endpoint under project ``example``
in region ``us-central1``, run:

```
gcloud beta ai endpoints create --project=example --region=us-central1 --display-name=my_endpoint
```

**REQUIRED FLAGS**

: **--display-name**:
Display name of the endpoint.

**OPTIONAL FLAGS**

: **--description**:
Description of the endpoint.

**--encryption-kms-key-name**:
The Cloud KMS resource identifier of the customer managed encryption key used to
protect a resource. Has the form:
projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key.
The key needs to be in the same region as where the compute resource is created.

**--endpoint-id**:
User-specified ID of the endpoint.

**--gdce-zone**:
The name of the GDCE zone. If set, the endpoint is in GDCE.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--network**:
The full name of the Google Compute Engine network to which the endpoint should
be peered.

**Region resource - Cloud region to create endpoint. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `--region` on the command line with a fully
specified name;
- set the property `ai/region` with a fully specified name;
- choose one from the prompted list of available regions with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--region**:
ID of the region or fully qualified identifier for the region.
To set the `region` attribute:

- provide the argument `--region` on the command line;
- set the property `ai/region`;
- choose one from the prompted list of available regions.**

**--request-response-logging-rate**:
Prediction request & response sampling rate for logging to BigQuery table.

**--request-response-logging-table**:
BigQuery table uri for prediction request & response logging.
You can provide table uri that does not exist, it will be created for you.
Value should be provided in format:
bq://``PROJECT_ID``/``DATASET``/``TABLE``

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

: This command is currently in beta and might change without notice. These
variants are also available:

```
gcloud ai endpoints create
```

```
gcloud alpha ai endpoints create
```