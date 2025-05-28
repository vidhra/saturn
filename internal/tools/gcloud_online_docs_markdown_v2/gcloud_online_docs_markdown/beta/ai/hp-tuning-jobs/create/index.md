# gcloud beta ai hp-tuning-jobs create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/ai/hp-tuning-jobs/create](https://cloud.google.com/sdk/gcloud/reference/beta/ai/hp-tuning-jobs/create)*

**NAME**

: **gcloud beta ai hp-tuning-jobs create - create a hyperparameter tuning job**

**SYNOPSIS**

: **`gcloud beta ai hp-tuning-jobs create` `[--config](https://cloud.google.com/sdk/gcloud/reference/beta/ai/hp-tuning-jobs/create#--config)`=`CONFIG` `[--display-name](https://cloud.google.com/sdk/gcloud/reference/beta/ai/hp-tuning-jobs/create#--display-name)`=`DISPLAY_NAME` [`[--algorithm](https://cloud.google.com/sdk/gcloud/reference/beta/ai/hp-tuning-jobs/create#--algorithm)`=`ALGORITHM`] [`[--enable-dashboard-access](https://cloud.google.com/sdk/gcloud/reference/beta/ai/hp-tuning-jobs/create#--enable-dashboard-access)`] [`[--enable-web-access](https://cloud.google.com/sdk/gcloud/reference/beta/ai/hp-tuning-jobs/create#--enable-web-access)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/beta/ai/hp-tuning-jobs/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--max-trial-count](https://cloud.google.com/sdk/gcloud/reference/beta/ai/hp-tuning-jobs/create#--max-trial-count)`=`MAX_TRIAL_COUNT`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/beta/ai/hp-tuning-jobs/create#--network)`=`NETWORK`] [`[--parallel-trial-count](https://cloud.google.com/sdk/gcloud/reference/beta/ai/hp-tuning-jobs/create#--parallel-trial-count)`=`PARALLEL_TRIAL_COUNT`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/beta/ai/hp-tuning-jobs/create#--region)`=`REGION`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/beta/ai/hp-tuning-jobs/create#--service-account)`=`SERVICE_ACCOUNT`] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/beta/ai/hp-tuning-jobs/create#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/beta/ai/hp-tuning-jobs/create#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/beta/ai/hp-tuning-jobs/create#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/beta/ai/hp-tuning-jobs/create#--kms-project)`=`KMS_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/ai/hp-tuning-jobs/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(BETA)` Create a hyperparameter tuning job.

**EXAMPLES**

: To create a job named ``test`` under project
``example`` in region
``us-central1``, run:

```
gcloud beta ai hp-tuning-jobs create --region=us-central1 --project=example --config=config.yaml --display-name=test
```

**REQUIRED FLAGS**

: **--config**:
Path to the job configuration file. This file should be a YAML document
containing a HyperparameterTuningSpec. If an option is specified both in the
configuration file **and** via command line arguments, the command line
arguments override the configuration file.
Example(YAML):

```
displayName: TestHpTuningJob
maxTrialCount: 1
parallelTrialCount: 1
studySpec:
  metrics:
  - metricId: x
    goal: MINIMIZE
  parameters:
  - parameterId: z
    integerValueSpec:
      minValue: 1
      maxValue: 100
  algorithm: RANDOM_SEARCH
trialJobSpec:
  workerPoolSpecs:
  - machineSpec:
      machineType: n1-standard-4
    replicaCount: 1
    containerSpec:
      imageUri: gcr.io/ucaip-test/ucaip-training-test
```

**--display-name**:
Display name of the hyperparameter tuning job to create.

**OPTIONAL FLAGS**

: **--algorithm**:
Search algorithm specified for the given study.
`ALGORITHM` must be one of:
`algorithm-unspecified`, `grid-search`,
`random-search`.

**--enable-dashboard-access**:
Whether you want Vertex AI to enable dashboard built on the training containers.
If set to ``true``, you can access the
dashboard at the URIs given by CustomJob.web_access_uris or
Trial.web_access_uris (within HyperparameterTuningJob.trials).

**--enable-web-access**:
Whether you want Vertex AI to enable [interactive
shell access](https://cloud.google.com/vertex-ai/docs/training/monitor-debug-interactive-shell) to training containers. If set to
``true``, you can access interactive shells at
the URIs given by CustomJob.web_access_uris or Trial.web_access_uris (within
HyperparameterTuningJob.trials).

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--max-trial-count**:
Desired total number of trials. The default value is 1.

**--network**:
Full name of the Google Compute Engine network to which the Job is peered with.
Private services access must already have been configured. If unspecified, the
Job is not peered with any network.

**--parallel-trial-count**:
Desired number of Trials to run in parallel. The default value is 1.

**Region resource - Cloud region to create a hyperparameter tuning job. This
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

**--service-account**:
The email address of a service account to use when running the training
appplication. You must have the `iam.serviceAccounts.actAs`
permission for the specified service account.

**--kms-key**

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
gcloud ai hp-tuning-jobs create
```

```
gcloud alpha ai hp-tuning-jobs create
```