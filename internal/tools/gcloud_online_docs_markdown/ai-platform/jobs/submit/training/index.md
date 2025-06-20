# gcloud ai-platform jobs submit training  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training)*

**NAME**

: **gcloud ai-platform jobs submit training - submit an AI Platform training job**

**SYNOPSIS**

: **`gcloud ai-platform jobs submit training` `[JOB](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#JOB)` [`[--config](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--config)`=`CONFIG`] [`[--enable-web-access](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--enable-web-access)`] [`[--job-dir](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--job-dir)`=`JOB_DIR`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--labels)`=[`KEY`=`VALUE`,…]] [`[--master-accelerator](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--master-accelerator)`=[`count`=`COUNT`],[`type`=`TYPE`]] [`[--master-image-uri](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--master-image-uri)`=`MASTER_IMAGE_URI`] [`[--master-machine-type](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--master-machine-type)`=`MASTER_MACHINE_TYPE`] [`[--module-name](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--module-name)`=`MODULE_NAME`] [`[--package-path](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--package-path)`=`PACKAGE_PATH`] [`[--packages](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--packages)`=[`PACKAGE`,…]] [`[--parameter-server-accelerator](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--parameter-server-accelerator)`=[`count`=`COUNT`],[`type`=`TYPE`]] [`[--parameter-server-image-uri](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--parameter-server-image-uri)`=`PARAMETER_SERVER_IMAGE_URI`] [`[--python-version](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--python-version)`=`PYTHON_VERSION`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--region)`=`REGION`] [`[--runtime-version](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--runtime-version)`=`RUNTIME_VERSION`] [`[--scale-tier](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--scale-tier)`=`SCALE_TIER`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--service-account)`=`SERVICE_ACCOUNT`] [`[--staging-bucket](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--staging-bucket)`=`STAGING_BUCKET`] [`[--use-chief-in-tf-config](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--use-chief-in-tf-config)`=`USE_CHIEF_IN_TF_CONFIG`] [`[--worker-accelerator](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--worker-accelerator)`=[`count`=`COUNT`],[`type`=`TYPE`]] [`[--worker-image-uri](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--worker-image-uri)`=`WORKER_IMAGE_URI`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--async)`     | `[--stream-logs](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--stream-logs)`] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--kms-project)`=`KMS_PROJECT`] [`[--parameter-server-count](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--parameter-server-count)`=`PARAMETER_SERVER_COUNT` `[--parameter-server-machine-type](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--parameter-server-machine-type)`=`PARAMETER_SERVER_MACHINE_TYPE`] [`[--worker-count](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--worker-count)`=`WORKER_COUNT` `[--worker-machine-type](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#--worker-machine-type)`=`WORKER_MACHINE_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#GCLOUD-WIDE-FLAGS) …`] [-- `[USER_ARGS](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training#USER_ARGS)` …]**

**DESCRIPTION**

: Submit an AI Platform training job.
This creates temporary files and executes Python code staged by a user on Cloud
Storage. Model code can either be specified with a path, e.g.:

```
gcloud ai-platform jobs submit training my_job --module-name trainer.task --staging-bucket gs://my-bucket --package-path /my/code/path/trainer --packages additional-dep1.tar.gz,dep2.whl
```

Or by specifying an already built package:

```
gcloud ai-platform jobs submit training my_job --module-name trainer.task --staging-bucket gs://my-bucket --packages trainer-0.0.1.tar.gz,additional-dep1.tar.gz,dep2.whl
```

If `--package-path=/my/code/path/trainer` is specified and there is a
`setup.py` file at `/my/code/path/setup.py`, the setup
file will be invoked with `sdist` and the generated tar files will be
uploaded to Cloud Storage. Otherwise, a temporary `setup.py` file
will be generated for the build.
By default, this command runs asynchronously; it exits once the job is
successfully submitted.
To follow the progress of your job, pass the `--stream-logs` flag
(note that even with the `--stream-logs` flag, the job will continue
to run after this command exits and must be cancelled with `gcloud
ai-platform jobs cancel JOB_ID`).
For more information, see: [https://cloud.google.com/ai-platform/training/docs/overview](https://cloud.google.com/ai-platform/training/docs/overview)

**POSITIONAL ARGUMENTS**

: **`JOB`**:
Name of the job.

**[-- `USER_ARGS` …]**:
Additional user arguments to be forwarded to user code
The '--' argument must be specified between gcloud specific args on the left and
USER_ARGS on the right.

**FLAGS**

: **--config**:
Path to the job configuration file. This file should be a YAML document (JSON
also accepted) containing a Job resource as defined in the API (all fields are
optional): [https://cloud.google.com/ml/reference/rest/v1/projects.jobs](https://cloud.google.com/ml/reference/rest/v1/projects.jobs)
EXAMPLES:
JSON:

```
{
  "jobId": "my_job",
  "labels": {
    "type": "prod",
    "owner": "alice"
  },
  "trainingInput": {
    "scaleTier": "BASIC",
    "packageUris": [
      "gs://my/package/path"
    ],
    "region": "us-east1"
  }
}
```

YAML:

```
jobId: my_job
labels:
  type: prod
  owner: alice
trainingInput:
  scaleTier: BASIC
  packageUris:
  - gs://my/package/path
  region: us-east1
```

If an option is specified both in the configuration file **and** via command
line arguments, the command line arguments override the configuration file.

**--enable-web-access**:
Whether you want AI Platform Training to enable [interactive shell access]
(https://cloud.google.com/ai-platform/training/docs/monitor-debug-interactive-shell)
to training containers. If set to `true`, you can access interactive
shells at the URIs given by TrainingOutput.web_access_uris or
HyperparameterOutput.web_access_uris (within TrainingOutput.trials).

**--job-dir**:
Cloud Storage path in which to store training outputs and other data needed for
training.
This path will be passed to your TensorFlow program as the
`--job-dir` command-line arg. The benefit of specifying this field is
that AI Platform will validate the path for use in training. However, note that
your training program will need to parse the provided `--job-dir`
argument.
If packages must be uploaded and `--staging-bucket` is not provided,
this path will be used instead.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--master-accelerator**:
Hardware accelerator config for the master worker. Must specify both the
accelerator type (TYPE) for each server and the number of accelerators to attach
to each server (COUNT).

**`type`**:
Type of the accelerator. Choices are
nvidia-tesla-a100,nvidia-tesla-k80,nvidia-tesla-p100,nvidia-tesla-p4,nvidia-tesla-t4,nvidia-tesla-v100,tpu-v2,tpu-v2-pod,tpu-v3,tpu-v3-pod,tpu-v4-pod

**`count`**:
Number of accelerators to attach to each machine running the job. Must be
greater than 0.

**--master-image-uri**:
Docker image to run on each master worker. This image must be in Container
Registry. Only one of `--master-image-uri` and
`--runtime-version` must be specified.

**--master-machine-type**:
Specifies the type of virtual machine to use for training job's master worker.
You must set this value when `--scale-tier` is set to
`CUSTOM`.

**--module-name**:
Name of the module to run.

**--package-path**:
Path to a Python package to build. This should point to a `local`
directory containing the Python source for the job. It will be built using
`setuptools` (which must be installed) using its `parent`
directory as context. If the parent directory contains a `setup.py`
file, the build will use that; otherwise, it will use a simple built-in one.

**--packages**:
Path to Python archives used for training. These can be local paths (absolute or
relative), in which case they will be uploaded to the Cloud Storage bucket given
by `--staging-bucket`, or Cloud Storage URLs
('gs://bucket-name/path/to/package.tar.gz').

**--parameter-server-accelerator**:
Hardware accelerator config for the parameter servers. Must specify both the
accelerator type (TYPE) for each server and the number of accelerators to attach
to each server (COUNT).

**`type`**:
Type of the accelerator. Choices are
nvidia-tesla-a100,nvidia-tesla-k80,nvidia-tesla-p100,nvidia-tesla-p4,nvidia-tesla-t4,nvidia-tesla-v100,tpu-v2,tpu-v2-pod,tpu-v3,tpu-v3-pod,tpu-v4-pod

**`count`**:
Number of accelerators to attach to each machine running the job. Must be
greater than 0.

**--parameter-server-image-uri**:
Docker image to run on each parameter server. This image must be in Container
Registry. If not specified, the value of `--master-image-uri` is
used.

**--python-version**:
Version of Python used during training. Choices are 3.7, 3.5, and 2.7. However,
this value must be compatible with the chosen runtime version for the job.
Must be used with a compatible runtime version:

- 3.7 is compatible with runtime versions 1.15 and later.
- 3.5 is compatible with runtime versions 1.4 through 1.14.
- 2.7 is compatible with runtime versions 1.15 and earlier.

**--region**:
Region of the machine learning training job to submit. If not specified, you
might be prompted to select a region (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/region`` property:

```
gcloud config set compute/region REGION
```

A list of regions can be fetched by running:

```
gcloud compute regions list
```

To unset the property, run:

```
gcloud config unset compute/region
```

Alternatively, the region can be stored in the environment variable
``CLOUDSDK_COMPUTE_REGION``.

**--runtime-version**:
AI Platform runtime version for this job. Must be specified unless
--master-image-uri is specified instead. It is defined in documentation along
with the list of supported versions: [https://cloud.google.com/ai-platform/prediction/docs/runtime-version-list](https://cloud.google.com/ai-platform/prediction/docs/runtime-version-list)

**--scale-tier**:
Specify the machine types, the number of replicas for workers, and parameter
servers. `SCALE_TIER` must be one of:

**`basic`**:
Single worker instance. This tier is suitable for learning how to use AI
Platform, and for experimenting with new models using small datasets.

**`basic-gpu`**:
Single worker instance with a GPU.

**`basic-tpu`**:
Single worker instance with a Cloud TPU.

**`custom`**:
CUSTOM tier is not a set tier, but rather enables you to use your own cluster
specification. When you use this tier, set values to configure your processing
cluster according to these guidelines (using the `--config` flag):

- You `must` set `TrainingInput.masterType` to
specify the type of machine to use for your master node. This is the only
required setting.
- You `may` set `TrainingInput.workerCount` to
specify the number of workers to use. If you specify one or more workers, you
`must` also set `TrainingInput.workerType` to
specify the type of machine to use for your worker nodes.
- You `may` set
`TrainingInput.parameterServerCount` to specify the number of
parameter servers to use. If you specify one or more parameter servers, you
`must` also set
`TrainingInput.parameterServerType` to specify the type of machine to
use for your parameter servers. Note that all of your workers must use the same
machine type, which can be different from your parameter server type and master
type. Your parameter servers must likewise use the same machine type, which can
be different from your worker type and master type.

**`premium-1`**:
Large number of workers with many parameter servers.

**`standard-1`**:
Many workers and a few parameter servers.

**--service-account**:
The email address of a service account to use when running the training
appplication. You must have the `iam.serviceAccounts.actAs`
permission for the specified service account. In addition, the AI Platform
Training Google-managed service account must have the
`roles/iam.serviceAccountAdmin` role for the specified service
account. [Learn
more about configuring a service account.](https://cloud.google.com/ai-platform/training/docs/custom-service-account) If not specified, the AI Platform
Training Google-managed service account is used by default.

**--staging-bucket**:
Bucket in which to stage training archives.
Required only if a file upload is necessary (that is, other flags include local
paths) and no other flags implicitly specify an upload path.

**--use-chief-in-tf-config**:
Use "chief" role in the cluster instead of "master". This is required for
TensorFlow 2.0 and newer versions. Unlike "master" node, "chief" node does not
run evaluation.

**--worker-accelerator**:
Hardware accelerator config for the worker nodes. Must specify both the
accelerator type (TYPE) for each server and the number of accelerators to attach
to each server (COUNT).

**`type`**:
Type of the accelerator. Choices are
nvidia-tesla-a100,nvidia-tesla-k80,nvidia-tesla-p100,nvidia-tesla-p4,nvidia-tesla-t4,nvidia-tesla-v100,tpu-v2,tpu-v2-pod,tpu-v3,tpu-v3-pod,tpu-v4-pod

**`count`**:
Number of accelerators to attach to each machine running the job. Must be
greater than 0.

**--worker-image-uri**:
Docker image to run on each worker node. This image must be in Container
Registry. If not specified, the value of `--master-image-uri` is
used.

**--async**

**--kms-key**

**--parameter-server-count**

**--worker-count**

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
gcloud alpha ai-platform jobs submit training
```

```
gcloud beta ai-platform jobs submit training
```