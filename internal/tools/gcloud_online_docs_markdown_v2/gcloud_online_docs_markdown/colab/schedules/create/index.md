# gcloud colab schedules create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/colab/schedules/create](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/create)*

**NAME**

: **gcloud colab schedules create - create a schedule**

**SYNOPSIS**

: **`gcloud colab schedules create` (`[--cron-schedule](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/create#--cron-schedule)`=`CRON_SCHEDULE` `[--display-name](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/create#--display-name)`=`DISPLAY_NAME` (`[--execution-display-name](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/create#--execution-display-name)`=`EXECUTION_DISPLAY_NAME` `[--gcs-output-uri](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/create#--gcs-output-uri)`=`GCS_OUTPUT_URI` `[--notebook-runtime-template](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/create#--notebook-runtime-template)`=`NOTEBOOK_RUNTIME_TEMPLATE` ([`[--dataform-repository-name](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/create#--dataform-repository-name)`=`DATAFORM_REPOSITORY_NAME` : `[--commit-sha](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/create#--commit-sha)`=`COMMIT_SHA`] | [`[--gcs-notebook-uri](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/create#--gcs-notebook-uri)`=`GCS_NOTEBOOK_URI` : `[--generation](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/create#--generation)`=`GENERATION`]) (`[--service-account](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/create#--service-account)`=`SERVICE_ACCOUNT` | `[--user-email](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/create#--user-email)`=`USER_EMAIL`) : `[--execution-timeout](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/create#--execution-timeout)`=`EXECUTION_TIMEOUT`; default="24h") : `[--enable-queueing](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/create#--enable-queueing)` `[--end-time](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/create#--end-time)`=`END_TIME` `[--max-concurrent-runs](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/create#--max-concurrent-runs)`=`MAX_CONCURRENT_RUNS`; default=1 `[--max-runs](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/create#--max-runs)`=`MAX_RUNS` `[--start-time](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/create#--start-time)`=`START_TIME`) [`[--region](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/create#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/colab/schedules/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a schedule to run a Colab Enterprise notebook execution job.

**EXAMPLES**

: To create a schedule in region `us-central1` with the following
schedule properties:

- display name: `my-schedule`,
- cron schedule: `TZ=America/Los_Angeles * * * * *`,
- maximum concurrent runs allowed: 1,
- start time: 2025-01-01T00:00:00-06:00,

for a notebook execution job:

- with display name `my-execution`,
- running notebook file from Cloud Storage URI
`gs://my-bucket/my-notebook.ipynb`,
- compute configured from runtime template `my-runtime-template-id`,
- running with service account
`my-service-account@my-project.iam.gserviceaccount.com`,
- with results uploaded to Cloud Storage bucket
`gs://my-bucket/results`

Run the following command:
```
gcloud colab schedules create --region=us-central1 --display-name=my-schedule --cron-schedule='TZ=America/Los_Angeles * * * * *' --max-concurrent-runs=1 --start-time=2025-01-01T00:00:00-06:00 --execution-display-name=my-execution --notebook-runtime-template=my-runtime-template-id --gcs-notebook-uri=gs://my-bucket/my-notebook.ipynb --service-account=my-service-account@my-project.iam.gserviceaccount.com --gcs-output-uri=gs://my-bucket/results
```

**REQUIRED FLAGS**

: **--cron-schedule**

**OPTIONAL FLAGS**

: **Region resource - Cloud region to create. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `--region` on the command line with a fully
specified name;
- set the property `colab/region` with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--region**:
ID of the region or fully qualified identifier for the region.
To set the `region` attribute:

- provide the argument `--region` on the command line;
- set the property `colab/region`.**

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
gcloud beta colab schedules create
```