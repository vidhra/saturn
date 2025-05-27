# gcloud deploy job-runs terminate  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deploy/job-runs/terminate](https://cloud.google.com/sdk/gcloud/reference/deploy/job-runs/terminate)*

**NAME**

: **gcloud deploy job-runs terminate - terminates a Cloud Deploy job run**

**SYNOPSIS**

: **`gcloud deploy job-runs terminate` (`[JOB_RUN](https://cloud.google.com/sdk/gcloud/reference/deploy/job-runs/terminate#JOB_RUN)` : `[--delivery-pipeline](https://cloud.google.com/sdk/gcloud/reference/deploy/job-runs/terminate#--delivery-pipeline)`=`DELIVERY_PIPELINE` `[--region](https://cloud.google.com/sdk/gcloud/reference/deploy/job-runs/terminate#--region)`=`REGION` `[--release](https://cloud.google.com/sdk/gcloud/reference/deploy/job-runs/terminate#--release)`=`RELEASE` `[--rollout](https://cloud.google.com/sdk/gcloud/reference/deploy/job-runs/terminate#--rollout)`=`ROLLOUT`) [`[--override-deploy-policies](https://cloud.google.com/sdk/gcloud/reference/deploy/job-runs/terminate#--override-deploy-policies)`=[`POLICY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deploy/job-runs/terminate#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Terminates a Cloud Deploy job run.

**EXAMPLES**

: To terminate a job run `test-jobrun`, for delivery pipeline
'test-pipeline', release 'test-release', rollout 'test-rollout', in region
'us-central1', run:

```
gcloud deploy job-runs terminate test-jobrun --delivery-pipeline=test-pipeline --release=test-release --rollout=test-rollout --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Job run resource - The name of the Job Run. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `job_run` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`JOB_RUN`**:
ID of the job_run or fully qualified identifier for the job_run.
To set the `name` attribute:

- provide the argument `job_run` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--delivery-pipeline**:
The delivery pipeline associated with the job_run. Alternatively, set the
property [deploy/delivery-pipeline].
To set the `delivery-pipeline` attribute:

- provide the argument `job_run` on the command line with a fully
specified name;
- provide the argument `--delivery-pipeline` on the command line;
- set the property `deploy/delivery_pipeline`.

**--region**:
The Cloud region for the job_run. Alternatively, set the property
[deploy/region].
To set the `region` attribute:

- provide the argument `job_run` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `deploy/region`.

**--release**:
The release associated with the job_run.
To set the `release` attribute:

- provide the argument `job_run` on the command line with a fully
specified name;
- provide the argument `--release` on the command line.

**--rollout**:
The rollout associated with the job_run.
To set the `rollout` attribute:

- provide the argument `job_run` on the command line with a fully
specified name;
- provide the argument `--rollout` on the command line.**

**FLAGS**

: **--override-deploy-policies**:
Deploy policies to override

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
gcloud alpha deploy job-runs terminate
```

```
gcloud beta deploy job-runs terminate
```