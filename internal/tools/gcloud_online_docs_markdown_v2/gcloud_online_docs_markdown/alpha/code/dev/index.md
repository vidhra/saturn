# gcloud alpha code dev  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev)*

**NAME**

: **gcloud alpha code dev - run a Cloud Run service in a local development environment**

**SYNOPSIS**

: **`gcloud alpha code dev` [`[SERVICE_CONFIG](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#SERVICE_CONFIG)`] [`[--[no-]allow-secret-manager](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#--[no-]allow-secret-manager)`] [`[--cloudsql-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#--cloudsql-instances)`=[`CLOUDSQL_INSTANCE`,…]] [`[--cpu](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#--cpu)`=`CPU`] [`[--image](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#--image)`=`IMAGE`] [`[--local-port](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#--local-port)`=`LOCAL_PORT`] [`[--memory](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#--memory)`=`MEMORY`] [`[--minikube-vm-driver](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#--minikube-vm-driver)`=`MINIKUBE_VM_DRIVER`; default="docker"] [`[--namespace](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#--namespace)`=`NAMESPACE`] [`[--secrets](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#--secrets)`=[`KEY`=`VALUE`,…]] [`[--service-name](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#--service-name)`=`SERVICE_NAME`] [`[--source](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#--source)`=`SOURCE`] [`[--no-stop-cluster](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#--stop-cluster)`] [`[--application-default-credential](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#--application-default-credential)`     | `[--service-account](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#--service-account)`=`SERVICE_ACCOUNT`] [`[--builder](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#--builder)`=`BUILDER`     | `[--dockerfile](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#--dockerfile)`=`DOCKERFILE`; default="Dockerfile"] [`[--env-vars](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#--env-vars)`=[`KEY`=`VALUE`,…]     | `[--env-vars-file](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#--env-vars-file)`=`FILE_PATH`] [`[--kube-context](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#--kube-context)`=`KUBE_CONTEXT`     | `[--minikube-profile](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#--minikube-profile)`=`MINIKUBE_PROFILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/code/dev#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Run a Cloud Run service in a local development environment.
This command takes Cloud Run source, builds it, and runs it on the local
machine. This command also watches the relevant source files and updates the
container when they change.

**EXAMPLES**

: If building images using a Dockerfile:

```
gcloud alpha code dev --dockerfile=<path_to_dockerfile>
```

If the Dockerfile is named `Dockerfile` and is located in the current
directory, the `--dockerfile` flag may be omitted:

```
gcloud alpha code dev
```

To access Google Cloud Platform services with the current user's credentials,
login to obtain the application default credentials and invoke this command with
the `--application-default-credential` flag.

```
gcloud auth application-default login
gcloud alpha code dev --dockerfile=<path_to_dockerfile> --application-default-credential
```

**POSITIONAL ARGUMENTS**

: **[`SERVICE_CONFIG`]**:
service.yaml filename override. Defaults to the first file matching
`*service.dev.yaml` then `*service.yaml`, if any exist.
This path is relative to the --source dir. An App Engine config path (typically
`app.yaml`) may also be provided here, and we will build with a Cloud
Native Computing Foundation Buildpack builder selected from
gcr.io/gae-runtimes/buildpacks, according to the App Engine `runtime`
specified in app.yaml.

**FLAGS**

: **--[no-]allow-secret-manager**:
Suppress warnings if secrets need to be pulled from secret manager. Use
`--allow-secret-manager` to enable and
`--no-allow-secret-manager` to disable.

**--cloudsql-instances**:
Cloud SQL instance connection strings. Must be in the form
<project>:<region>:<instance>.

**--cpu**:
Container CPU limit. Limit is expressed as a number of CPUs. Fractional CPU
limits are allowed (e.g. 1.5).

**--image**:
Name for the built image.

**--local-port**:
Local port to which the service connection is forwarded. If this flag is not
set, then a random port is chosen.

**--memory**:
Container memory limit. Limit is expressed either as an integer representing the
number of bytes or an integer followed by a unit suffix. Valid unit suffixes are
"B", "KB", "MB", "GB", "TB", "KiB", "MiB", "GiB", "TiB", or "PiB".

**--minikube-vm-driver**:
If running on minikube, use this vm driver.

**--namespace**:
Kubernetes namespace for development kubernetes objects.

**--secrets**:
List of key-value pairs to set as secrets.

**--service-name**:
Name of the service.

**--source**:
The directory containing the source to build. If not specified, the current
directory is used.

**--stop-cluster**:
If running on minikube, stop the minkube profile at the end of the session.
Enabled by default, use `--no-stop-cluster` to disable.

**--application-default-credential**

**--builder**

**--env-vars**

**--kube-context**

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
allowlist. This variant is also available:

```
gcloud beta code dev
```