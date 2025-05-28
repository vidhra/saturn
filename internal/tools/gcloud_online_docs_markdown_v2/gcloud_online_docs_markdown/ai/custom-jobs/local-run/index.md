# gcloud ai custom-jobs local-run  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/local-run](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/local-run)*

**NAME**

: **gcloud ai custom-jobs local-run - run a custom training locally**

**SYNOPSIS**

: **`gcloud ai custom-jobs local-run` `[--executor-image-uri](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/local-run#--executor-image-uri)`=`IMAGE_URI` [`[--extra-dirs](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/local-run#--extra-dirs)`=[`EXTRA_DIR`,…]] [`[--extra-packages](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/local-run#--extra-packages)`=[`PACKAGE`,…]] [`[--gpu](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/local-run#--gpu)`] [`[--local-package-path](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/local-run#--local-package-path)`=`LOCAL_PATH`] [`[--output-image-uri](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/local-run#--output-image-uri)`=`OUTPUT_IMAGE`] [`[--requirements](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/local-run#--requirements)`=[`REQUIREMENTS`,…]] [`[--service-account-key-file](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/local-run#--service-account-key-file)`=`ACCOUNT_KEY_FILE`] [`[--python-module](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/local-run#--python-module)`=`PYTHON_MODULE`     | `[--script](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/local-run#--script)`=`SCRIPT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/local-run#GCLOUD-WIDE-FLAGS) …`] [-- `[ARGS](https://cloud.google.com/sdk/gcloud/reference/ai/custom-jobs/local-run#ARGS)` …]**

**DESCRIPTION**

: Packages your training code into a Docker image and executes it locally.
You should execute this command in the top folder which includes all the code
and resources you want to pack and run, or specify the 'work-dir' flag to point
to it. Any other path you specified via flags should be a relative path to the
work-dir and under it; otherwise it will be unaccessible.
Supposing your directories are like the following structures:

```
/root
  - my_project
      - my_training
          - task.py
          - util.py
          - setup.py
      - other_modules
          - some_module.py
      - dataset
          - small.dat
          - large.dat
      - config
      - dep
          - foo.tar.gz
      - bar.whl
      - requirements.txt
  - another_project
      - something
```

If you set 'my_project' as the package, then you should execute the task.py by
specifying "--script=my_training/task.py" or "--python-module=my_training.task",
the 'requirements.txt' will be processed. And you will also be able to install
extra packages by, e.g. specifying "--extra-packages=dep/foo.tar.gz,bar.whl" or
include extra directories, e.g. specifying "--extra-dirs=dataset,config".
If you set 'my_training' as the package, then you should execute the task.py by
specifying "--script=task.py" or "--python-module=task", the 'setup.py' will be
processed. However, you won't be able to access any other files or directories
that are not in 'my_training' folder.
See more details in the HELP info of the corresponding flags.

**EXAMPLES**

: To execute an python module with required dependencies, run:

```
gcloud ai custom-jobs local-run --python-module=my_training.task --executor-image-uri=gcr.io/my/image --requirements=pandas,scipy>=1.3.0
```

To execute a python script using local GPU, run:

```
gcloud ai custom-jobs local-run --script=my_training/task.py --executor-image-uri=gcr.io/my/image --gpu
```

To execute an arbitrary script with custom arguments, run:

```
gcloud ai custom-jobs local-run --script=my_run.sh --executor-image-uri=gcr.io/my/image -- --my-arg bar --enable_foo
```

To run an existing container training without building new image, run:

```
gcloud ai custom-jobs local-run --executor-image-uri=gcr.io/my/custom-training-image
```

**POSITIONAL ARGUMENTS**

: **[-- `ARGS` …]**:
Additional user arguments to be forwarded to your application.
The '--' argument must be specified between gcloud specific args on the left and
ARGS on the right. Example:

```
gcloud ai custom-jobs local-run --script=my_run.sh --base-image=gcr.io/my/image -- --my-arg bar --enable_foo
```

**REQUIRED FLAGS**

: **--executor-image-uri**:
URI or ID of the container image in either the Container Registry or local that
will run the application. See [https://cloud.google.com/vertex-ai/docs/training/pre-built-containers](https://cloud.google.com/vertex-ai/docs/training/pre-built-containers)
for available pre-built container images provided by Vertex AI for training.

**OPTIONAL FLAGS**

: **--extra-dirs**:
Extra directories under the working directory to include, besides the one that
contains the main executable.
By default, only the parent directory of the main script or python module is
copied to the container. For example, if the module is "training.task" or the
script is "training/task.py", the whole "training" directory, including its
sub-directories, will always be copied to the container. You may specify this
flag to also copy other directories if necessary.
Note: if no parent is specified in 'python_module' or 'scirpt', the whole
working directory is copied, then you don't need to specify this flag.

**--extra-packages**:
Local paths to Python archives used as training dependencies in the image
container. These can be absolute or relative paths. However, they have to be
under the work_dir; Otherwise, this tool will not be able to access it.
Example: 'dep1.tar.gz, ./downloads/dep2.whl'

**--gpu**:
Enable to use GPU.

**--local-package-path**:
local path of the directory where the python-module or script exists. If not
specified, it use the directory where you run the this command.
Only the contents of this directory will be accessible to the built container
image.

**--output-image-uri**:
Uri of the custom container image to be built with the your application packed
in.

**--requirements**:
Python dependencies from PyPI to be used when running the application. If this
is not specified, and there is no "setup.py" or "requirements.txt" in the
working directory, your application will only have access to what exists in the
base image with on other dependencies.
Example: 'tensorflow-cpu, pandas==1.2.0, matplotlib>=3.0.2'

**--service-account-key-file**:
The JSON file of a Google Cloud service account private key. When specified, the
corresponding service account will be used to authenticate the local container
to access Google Cloud services. Note that the key file won't be copied to the
container, it will be mounted during running time.

**--python-module**

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
gcloud alpha ai custom-jobs local-run
```

```
gcloud beta ai custom-jobs local-run
```