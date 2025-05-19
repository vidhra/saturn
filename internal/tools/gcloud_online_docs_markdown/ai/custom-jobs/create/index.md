# gcloud ai custom-jobs create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/create](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/create)*

**NAME**

: **gcloud ai custom-jobs create - create a new custom job**

**SYNOPSIS**

: **`gcloud ai custom-jobs create` `[--display-name](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/create#--display-name)`=`DISPLAY_NAME` (`[--config](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/create#--config)`=`CONFIG` `[--worker-pool-spec](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/create#--worker-pool-spec)`=[`WORKER_POOL_SPEC`,…]) [`[--args](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/create#--args)`=[`ARG`,…]] [`[--command](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/create#--command)`=[`COMMAND`,…]] [`[--enable-dashboard-access](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/create#--enable-dashboard-access)`] [`[--enable-web-access](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/create#--enable-web-access)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--network](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/create#--network)`=`NETWORK`] [`[--persistent-resource-id](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/create#--persistent-resource-id)`=`PERSISTENT_RESOURCE_ID`] [`[--python-package-uris](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/create#--python-package-uris)`=[`PYTHON_PACKAGE_URIS`,…]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/create#--region)`=`REGION`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/create#--service-account)`=`SERVICE_ACCOUNT`] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/create#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/create#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/create#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/create#--kms-project)`=`KMS_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command will attempt to run the custom job immediately upon creation.

**EXAMPLES**

: To create a job under project ``example`` in
region ``us-central1``, run:

```
gcloud ai custom-jobs create --region=us-central1 --project=example --worker-pool-spec=replica-count=1,machine-type='n1-highmem-2',container-image-uri='gcr.io/ucaip-test/ucaip-training-test' --display-name=test
```

**REQUIRED FLAGS**

: **--display-name**:
Display name of the custom job to create.

**--config**

**OPTIONAL FLAGS**

: **--args**:
Comma-separated arguments passed to containers or python tasks.

**--command**:
Command to be invoked when containers are started. It overrides the entrypoint
instruction in Dockerfile when provided.

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

**--network**:
Full name of the Google Compute Engine network to which the Job is peered with.
Private services access must already have been configured. If unspecified, the
Job is not peered with any network.

**--persistent-resource-id**:
The name of the persistent resource from the same project and region on which to
run this custom job.
If this is specified, the job will be run on existing machines held by the
PersistentResource instead of on-demand short-lived machines. The network and
CMEK configs on the job should be consistent with those on the
PersistentResource, otherwise, the job will be rejected.

**--python-package-uris**:
The common Python package URIs to be used for training with a pre-built
container image. e.g. `--python-package-uri=path1,path2` If you are
using multiple worker pools and want to specify a different Python packag fo
reach pool, use `--config` instead.

**Region resource - Cloud region to create a custom job. This represents a Cloud
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

: These variants are also available:

```
gcloud alpha ai custom-jobs create
```

```
gcloud beta ai custom-jobs create
```