# gcloud deploy rollouts retry-job  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/retry-job](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/retry-job)*

**NAME**

: **gcloud deploy rollouts retry-job - retries a specified job, phase combination on a rollout**

**SYNOPSIS**

: **`gcloud deploy rollouts retry-job` (`[ROLLOUT](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/retry-job#ROLLOUT)` : `[--delivery-pipeline](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/retry-job#--delivery-pipeline)`=`DELIVERY_PIPELINE` `[--region](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/retry-job#--region)`=`REGION` `[--release](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/retry-job#--release)`=`RELEASE`) `[--job-id](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/retry-job#--job-id)`=`JOB_ID` `[--phase-id](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/retry-job#--phase-id)`=`PHASE_ID` [`[--override-deploy-policies](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/retry-job#--override-deploy-policies)`=[`POLICY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deploy/rollouts/retry-job#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Retries a specified job, phase combination on a rollout.

**EXAMPLES**

: To retry a job 'test-job' in phase 'test-phase' on a rollout 'test-rollout' for
delivery pipeline 'test-pipeline', release 'test-release' in region
'us-central1', run:

```
gcloud deploy rollouts retry-job test-rollout --job-id=test-job --phase-id=test-phase --delivery-pipeline=test-pipeline --release=test-release --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Rollout resource - The name of the Rollout. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `rollout` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ROLLOUT`**:
ID of the rollout or fully qualified identifier for the rollout.
To set the `rollout` attribute:

- provide the argument `rollout` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--delivery-pipeline**:
The delivery pipeline associated with the rollout. Alternatively, set the
property [deploy/delivery-pipeline].
To set the `delivery-pipeline` attribute:

- provide the argument `rollout` on the command line with a fully
specified name;
- provide the argument `--delivery-pipeline` on the command line;
- set the property `deploy/delivery_pipeline`.

**--region**:
The Cloud region for the rollout. Alternatively, set the property
[deploy/region].
To set the `region` attribute:

- provide the argument `rollout` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `deploy/region`.

**--release**:
The release associated with the rollout.
To set the `release` attribute:

- provide the argument `rollout` on the command line with a fully
specified name;
- provide the argument `--release` on the command line.**

**REQUIRED FLAGS**

: **--job-id**:
Job ID on a rollout resource

**--phase-id**:
Phase ID on a rollout resource

**OPTIONAL FLAGS**

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
gcloud alpha deploy rollouts retry-job
```

```
gcloud beta deploy rollouts retry-job
```