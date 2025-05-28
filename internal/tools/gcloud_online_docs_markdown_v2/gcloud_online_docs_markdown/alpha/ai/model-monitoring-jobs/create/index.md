# gcloud alpha ai model-monitoring-jobs create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create)*

**NAME**

: **gcloud alpha ai model-monitoring-jobs create - create a new Vertex AI model monitoring job**

**SYNOPSIS**

: **`gcloud alpha ai model-monitoring-jobs create` `[--display-name](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--display-name)`=`DISPLAY_NAME` `[--emails](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--emails)`=[`EMAILS`,…] `[--endpoint](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--endpoint)`=`ENDPOINT` `[--prediction-sampling-rate](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--prediction-sampling-rate)`=`PREDICTION_SAMPLING_RATE` [`[--analysis-instance-schema](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--analysis-instance-schema)`=`ANALYSIS_INSTANCE_SCHEMA`] [`[--[no-]anomaly-cloud-logging](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--[no-]anomaly-cloud-logging)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--log-ttl](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--log-ttl)`=`LOG_TTL`] [`[--monitoring-frequency](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--monitoring-frequency)`=`MONITORING_FREQUENCY`; default=24] [`[--notification-channels](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--notification-channels)`=[`NOTIFICATION_CHANNELS`,…]] [`[--predict-instance-schema](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--predict-instance-schema)`=`PREDICT_INSTANCE_SCHEMA`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--region)`=`REGION`] [`[--sample-predict-request](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--sample-predict-request)`=`SAMPLE_PREDICT_REQUEST`] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--kms-project)`=`KMS_PROJECT`] [`[--monitoring-config-from-file](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--monitoring-config-from-file)`=`MONITORING_CONFIG_FROM_FILE`     | `[--feature-attribution-thresholds](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--feature-attribution-thresholds)`=[`KEY`=`VALUE`,…] `[--feature-thresholds](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--feature-thresholds)`=[`KEY`=`VALUE`,…] `[--target-field](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--target-field)`=`TARGET_FIELD` `[--training-sampling-rate](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--training-sampling-rate)`=`TRAINING_SAMPLING_RATE`; default=1.0 `[--bigquery-uri](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--bigquery-uri)`=`BIGQUERY_URI`     | `[--dataset](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--dataset)`=`DATASET`     | `[--data-format](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--data-format)`=`DATA_FORMAT` `[--gcs-uris](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#--gcs-uris)`=[`GCS_URIS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/model-monitoring-jobs/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a new Vertex AI model monitoring job.

**EXAMPLES**

: To create a model deployment monitoring job under project
``example`` in region
``us-central1`` for endpoint
``123``, run:

```
gcloud alpha ai model-monitoring-jobs create --project=example --region=us-central1 --display-name=my_monitoring_job --emails=a@gmail.com,b@gmail.com --endpoint=123 --prediction-sampling-rate=0.2
```

To create a model deployment monitoring job with drift detection for all the
deployed models under the endpoint ``123``,
run:

```
gcloud alpha ai model-monitoring-jobs create --project=example --region=us-central1 --display-name=my_monitoring_job --emails=a@gmail.com,b@gmail.com --endpoint=123 --prediction-sampling-rate=0.2 --feature-thresholds=feat1=0.1,feat2=0.2,feat3=0.2,feat4=0.3
```

To create a model deployment monitoring job with skew detection for all the
deployed models under the endpoint ``123``,
with training dataset from Google Cloud Storage, run:

```
gcloud alpha ai model-monitoring-jobs create --project=example --region=us-central1 --display-name=my_monitoring_job --emails=a@gmail.com,b@gmail.com --endpoint=123 --prediction-sampling-rate=0.2 --feature-thresholds=feat1=0.1,feat2=0.2,feat3=0.2,feat4=0.3 --target-field=price --data-format=csv --gcs-uris=gs://test-bucket/dataset.csv
```

To create a model deployment monitoring job with skew detection for all the
deployed models under the endpoint ``123``,
with training dataset from Vertex AI dataset
``456``, run:

```
gcloud alpha ai model-monitoring-jobs create --project=example --region=us-central1 --display-name=my_monitoring_job --emails=a@gmail.com,b@gmail.com --endpoint=123 --prediction-sampling-rate=0.2 --feature-thresholds=feat1=0.1,feat2=0.2,feat3=0.2,feat4=0.3 --target-field=price --dataset=456
```

To create a model deployment monitoring job with different drift detection or
skew detection for different deployed models, run:

```
gcloud alpha ai model-monitoring-jobs create --project=example --region=us-central1 --display-name=my_monitoring_job --emails=a@gmail.com,b@gmail.com --endpoint=123 --prediction-sampling-rate=0.2 --monitoring-config-from-file=your_objective_config.yaml
```

After creating the monitoring job, be sure to send some predict requests. It
will be used to generate some metadata for analysis purpose, like predict and
analysis instance schema.

**REQUIRED FLAGS**

: **--display-name**:
Display name of the model deployment monitoring job.

**--emails**:
Comma-separated email address list. e.g. --emails=a@gmail.com,b@gmail.com

**--endpoint**:
Id of the endpoint.

**--prediction-sampling-rate**:
Prediction sampling rate.

**OPTIONAL FLAGS**

: **--analysis-instance-schema**:
YAML schema file uri(Google Cloud Storage) describing the format of a single
instance that you want Tensorflow Data Validation (TFDV) to analyze.

**--[no-]anomaly-cloud-logging**:
If true, anomaly will be sent to Cloud Logging. Use
`--anomaly-cloud-logging` to enable and
`--no-anomaly-cloud-logging` to disable.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--log-ttl**:
TTL of BigQuery tables in user projects which stores logs(Day-based unit).

**--monitoring-frequency**:
Monitoring frequency, unit is 1 hour.

**--notification-channels**:
Comma-separated notification channel list. e.g.
--notification-channels=projects/fake-project/notificationChannels/123,projects/fake-project/notificationChannels/456

**--predict-instance-schema**:
YAML schema file uri(Google Cloud Storage) describing the format of a single
instance, which are given to format this Endpoint's prediction. If not set,
predict schema will be generated from collected predict requests.

**Region resource - Cloud region to create model deployment monitoring job. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
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

**--sample-predict-request**:
Path to a local file containing the body of a JSON object. Same format as
[PredictRequest.instances][], this can be set as a replacement of
predict-instance-schema. If not set, predict schema will be generated from
collected predict requests.
An example of a JSON request:

```
{"x": [1, 2], "y": [3, 4]}
```

**--kms-key**

**--monitoring-config-from-file**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud ai model-monitoring-jobs create
```

```
gcloud beta ai model-monitoring-jobs create
```