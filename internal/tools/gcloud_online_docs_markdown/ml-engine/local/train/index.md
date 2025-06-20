# gcloud ml-engine local train  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ml-engine/local/train](https://cloud.google.com/sdk/gcloud/reference/ml-engine/local/train)*

**NAME**

: **gcloud ml-engine local train - run an AI Platform training job locally**

**SYNOPSIS**

: **`gcloud ml-engine local train` `[--module-name](https://cloud.google.com/sdk/gcloud/reference/ml-engine/local/train#--module-name)`=`MODULE_NAME` [`[--distributed](https://cloud.google.com/sdk/gcloud/reference/ml-engine/local/train#--distributed)`] [`[--evaluator-count](https://cloud.google.com/sdk/gcloud/reference/ml-engine/local/train#--evaluator-count)`=`EVALUATOR_COUNT`] [`[--job-dir](https://cloud.google.com/sdk/gcloud/reference/ml-engine/local/train#--job-dir)`=`JOB_DIR`] [`[--package-path](https://cloud.google.com/sdk/gcloud/reference/ml-engine/local/train#--package-path)`=`PACKAGE_PATH`] [`[--parameter-server-count](https://cloud.google.com/sdk/gcloud/reference/ml-engine/local/train#--parameter-server-count)`=`PARAMETER_SERVER_COUNT`] [`[--start-port](https://cloud.google.com/sdk/gcloud/reference/ml-engine/local/train#--start-port)`=`START_PORT`; default=27182] [`[--worker-count](https://cloud.google.com/sdk/gcloud/reference/ml-engine/local/train#--worker-count)`=`WORKER_COUNT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ml-engine/local/train#GCLOUD-WIDE-FLAGS) …`] [-- `[USER_ARGS](https://cloud.google.com/sdk/gcloud/reference/ml-engine/local/train#USER_ARGS)` …]**

**DESCRIPTION**

: This command runs the specified module in an environment similar to that of a
live AI Platform Training Job.
This is especially useful in the case of testing distributed models, as it
allows you to validate that you are properly interacting with the AI Platform
cluster configuration. If your model expects a specific number of parameter
servers or workers (i.e. you expect to use the CUSTOM machine type), use the
--parameter-server-count and --worker-count flags to further specify the desired
cluster configuration, just as you would in your cloud training job
configuration:

```
gcloud ml-engine local train --module-name trainer.task --package-path /path/to/my/code/trainer --distributed --parameter-server-count 4 --worker-count 8
```

Unlike submitting a training job, the --package-path parameter can be omitted,
and will use your current working directory.
AI Platform Training sets a TF_CONFIG environment variable on each VM in your
training job. You can use TF_CONFIG to access the cluster description and the
task description for each VM.
Learn more about TF_CONFIG: [https://cloud.google.com/ai-platform/training/docs/distributed-training-details](https://cloud.google.com/ai-platform/training/docs/distributed-training-details).

**POSITIONAL ARGUMENTS**

: **[-- `USER_ARGS` …]**:
Additional user arguments to be forwarded to user code. Any relative paths will
be relative to the `parent` directory of `--package-path`.
The '--' argument must be specified between gcloud specific args on the left and
USER_ARGS on the right.

**REQUIRED FLAGS**

: **--module-name**:
Name of the module to run.

**OPTIONAL FLAGS**

: **--distributed**:
Runs the provided code in distributed mode by providing cluster configurations
as environment variables to subprocesses

**--evaluator-count**:
Number of evaluators with which to run. Ignored if --distributed is not
specified. Default: 0

**--job-dir**:
Cloud Storage path or local_directory in which to store training outputs and
other data needed for training.
This path will be passed to your TensorFlow program as the
`--job-dir` command-line arg. The benefit of specifying this field is
that AI Platform will validate the path for use in training. However, note that
your training program will need to parse the provided `--job-dir`
argument.

**--package-path**:
Path to a Python package to build. This should point to a `local`
directory containing the Python source for the job. It will be built using
`setuptools` (which must be installed) using its `parent`
directory as context. If the parent directory contains a `setup.py`
file, the build will use that; otherwise, it will use a simple built-in one.

**--parameter-server-count**:
Number of parameter servers with which to run. Ignored if --distributed is not
specified. Default: 2

**--start-port**:
Start of the range of ports reserved by the local cluster. This command will use
a contiguous block of ports equal to parameter-server-count + worker-count + 1.
If --distributed is not specified, this flag is ignored.

**--worker-count**:
Number of workers with which to run. Ignored if --distributed is not specified.
Default: 2

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
gcloud alpha ml-engine local train
```

```
gcloud beta ml-engine local train
```