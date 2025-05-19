# gcloud ai model-monitoring-jobs update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ai/model-monitoring-jobs/update](https://cloud.google.com/sdk/gcloud/reference/ai/model-monitoring-jobs/update)*

**NAME**

: **gcloud ai model-monitoring-jobs update - update an Vertex AI model deployment monitoring job**

**SYNOPSIS**

: **`gcloud ai model-monitoring-jobs update` (`[MONITORING_JOB](https://cloud.google.com/sdk/gcloud/reference/ai/model-monitoring-jobs/update#MONITORING_JOB)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/ai/model-monitoring-jobs/update#--region)`=`REGION`) [`[--analysis-instance-schema](https://cloud.google.com/sdk/gcloud/reference/ai/model-monitoring-jobs/update#--analysis-instance-schema)`=`ANALYSIS_INSTANCE_SCHEMA`] [`[--[no-]anomaly-cloud-logging](https://cloud.google.com/sdk/gcloud/reference/ai/model-monitoring-jobs/update#--[no-]anomaly-cloud-logging)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/ai/model-monitoring-jobs/update#--display-name)`=`DISPLAY_NAME`] [`[--emails](https://cloud.google.com/sdk/gcloud/reference/ai/model-monitoring-jobs/update#--emails)`=[`EMAILS`,…]] [`[--log-ttl](https://cloud.google.com/sdk/gcloud/reference/ai/model-monitoring-jobs/update#--log-ttl)`=`LOG_TTL`] [`[--monitoring-frequency](https://cloud.google.com/sdk/gcloud/reference/ai/model-monitoring-jobs/update#--monitoring-frequency)`=`MONITORING_FREQUENCY`] [`[--notification-channels](https://cloud.google.com/sdk/gcloud/reference/ai/model-monitoring-jobs/update#--notification-channels)`=[`NOTIFICATION_CHANNELS`,…]] [`[--prediction-sampling-rate](https://cloud.google.com/sdk/gcloud/reference/ai/model-monitoring-jobs/update#--prediction-sampling-rate)`=`PREDICTION_SAMPLING_RATE`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/ai/model-monitoring-jobs/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/ai/model-monitoring-jobs/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/ai/model-monitoring-jobs/update#--remove-labels)`=[`KEY`,…]] [`[--monitoring-config-from-file](https://cloud.google.com/sdk/gcloud/reference/ai/model-monitoring-jobs/update#--monitoring-config-from-file)`=`MONITORING_CONFIG_FROM_FILE`     | `[--feature-attribution-thresholds](https://cloud.google.com/sdk/gcloud/reference/ai/model-monitoring-jobs/update#--feature-attribution-thresholds)`=[`KEY`=`VALUE`,…] `[--feature-thresholds](https://cloud.google.com/sdk/gcloud/reference/ai/model-monitoring-jobs/update#--feature-thresholds)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ai/model-monitoring-jobs/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an Vertex AI model deployment monitoring job.

**EXAMPLES**

: To update display name of model deployment monitoring job `123` under
project `example` in region `us-central1`, run:

```
gcloud ai model-monitoring-jobs update 123 --display-name=new-name --project=example --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Monitoring job resource - The model deployment monitoring job to update. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `monitoring_job` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`MONITORING_JOB`**:
ID of the monitoring_job or fully qualified identifier for the monitoring_job.
To set the `name` attribute:

- provide the argument `monitoring_job` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Cloud region for the monitoring_job.
To set the `region` attribute:

- provide the argument `monitoring_job` on the command line with a
fully specified name;
- provide the argument `--region` on the command line;
- set the property `ai/region`;
- choose one from the prompted list of available regions.**

**FLAGS**

: **--analysis-instance-schema**:
YAML schema file uri(Google Cloud Storage) describing the format of a single
instance that you want Tensorflow Data Validation (TFDV) to analyze.

**--[no-]anomaly-cloud-logging**:
If true, anomaly will be sent to Cloud Logging. Use
`--anomaly-cloud-logging` to enable and
`--no-anomaly-cloud-logging` to disable.

**--display-name**:
Display name of the model deployment monitoring job.

**--emails**:
Comma-separated email address list. e.g. --emails=a@gmail.com,b@gmail.com

**--log-ttl**:
TTL of BigQuery tables in user projects which stores logs(Day-based unit).

**--monitoring-frequency**:
Monitoring frequency, unit is 1 hour.

**--notification-channels**:
Comma-separated notification channel list. e.g.
--notification-channels=projects/fake-project/notificationChannels/123,projects/fake-project/notificationChannels/456

**--prediction-sampling-rate**:
Prediction sampling rate.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

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

: These variants are also available:

```
gcloud alpha ai model-monitoring-jobs update
```

```
gcloud beta ai model-monitoring-jobs update
```