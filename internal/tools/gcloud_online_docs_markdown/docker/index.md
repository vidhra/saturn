# gcloud docker  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/docker](https://cloud.google.com/sdk/gcloud/reference/docker)*

**NAME**

: **gcloud docker - enable Docker CLI access to Google Container Registry**

**SYNOPSIS**

: **`gcloud docker` [`[--authorize-only](https://cloud.google.com/sdk/gcloud/reference/docker#--authorize-only)`, `[-a](https://cloud.google.com/sdk/gcloud/reference/docker#-a)`] [`[--docker-host](https://cloud.google.com/sdk/gcloud/reference/docker#--docker-host)`=`DOCKER_HOST`] [`[--server](https://cloud.google.com/sdk/gcloud/reference/docker#--server)`=`SERVER`,[`[SERVER](https://cloud.google.com/sdk/gcloud/reference/docker#SERVER)`,…], `[-s](https://cloud.google.com/sdk/gcloud/reference/docker#-s)` `[SERVER](https://cloud.google.com/sdk/gcloud/reference/docker#SERVER)`,[`[SERVER](https://cloud.google.com/sdk/gcloud/reference/docker#SERVER)`,…]; default="gcr.io,us.gcr.io,eu.gcr.io,asia.gcr.io,staging-k8s.gcr.io,marketplace.gcr.io"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/docker#GCLOUD-WIDE-FLAGS) …`] [-- `[DOCKER_ARGS](https://cloud.google.com/sdk/gcloud/reference/docker#DOCKER_ARGS)` …]**

**DESCRIPTION**

: `(DEPRECATED)` Enable Docker CLI access to Google Container Registry.
`gcloud docker` will not be supported for Docker client versions
above 18.03.
As an alternative, use `[gcloud auth
configure-docker](https://cloud.google.com/sdk/gcloud/reference/auth/configure-docker)` to configure `docker` to use `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` as a credential helper, then use
`docker` as you would for non-GCR registries, e.g. `docker pull
gcr.io/project-id/my-image`. Add `--verbosity=error` to silence
this warning: `gcloud docker --verbosity=error -- pull
gcr.io/project-id/my-image`.
See: [https://cloud.google.com/container-registry/docs/support/deprecation-notices#gcloud-docker](https://cloud.google.com/container-registry/docs/support/deprecation-notices#gcloud-docker)
gcloud docker wraps Docker commands so that `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` can inject the appropriate fresh
authentication token into requests that interact with the Docker registry.
All Docker-specific flags are passed through to the underlying
`docker` command. A full reference of Docker's command line options
available after `--` can be found here: [https://docs.docker.com/engine/reference/commandline/cli/](https://docs.docker.com/engine/reference/commandline/cli/).
You may also run `gcloud docker -- --help` to view the Docker CLI's
help directly.
Detailed documentation on Container Registry can be found here: [https://cloud.google.com/container-registry/docs/](https://cloud.google.com/container-registry/docs/)

**EXAMPLES**

: To pull the image 'gcr.io/google-containers/pause:1.0' from the docker registry,
run:

```
gcloud docker -- pull gcr.io/google-containers/pause:1.0
```

Push the image 'gcr.io/example-org/example-image:latest' to our private docker
registry.

```
gcloud docker -- push gcr.io/example-org/example-image:latest
```

Configure authentication, then simply use docker:

```
gcloud docker --authorize-only
docker push gcr.io/example-org/example-image:latest
```

**POSITIONAL ARGUMENTS**

: **[-- `DOCKER_ARGS` …]**:
Arguments to pass to Docker.
The '--' argument must be specified between gcloud specific args on the left and
DOCKER_ARGS on the right.

**FLAGS**

: **--authorize-only**:
Configure Docker authorization only; do not launch the Docker command-line.

**--docker-host**:
URL to connect to Docker Daemon. Format: tcp://host:port or
unix:///path/to/socket.

**--server**:
Address of the Google Cloud Registry.

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