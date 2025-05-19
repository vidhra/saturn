# gcloud alpha auth configure-docker  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/auth/configure-docker](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/configure-docker)*

**NAME**

: **gcloud alpha auth configure-docker - register `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` as a Docker credential helper**

**SYNOPSIS**

: **`gcloud alpha auth configure-docker` [`[REGISTRIES](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/configure-docker#REGISTRIES)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/configure-docker#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` gcloud alpha auth configure-docker adds the Docker
`credHelper` entry to Docker's configuration file, or creates the
file if it doesn't exist. This will register `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` as the credential helper for all
Google-supported Docker registries. If the Docker configuration already contains
a `credHelper` entry, it will be overwritten.
Note: `docker` and `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` need to be on the same system
`PATH` to work correctly.
Note: This command will not work for `docker` installed via Snap, as
the `docker` snap package does not currently provide an interface for
credential helpers.
For more details on Docker registries, see [https://docs.docker.com/registry/](https://docs.docker.com/registry/).
For more details on how to authenticate to Google Container Registry using this
command, see [https://cloud.google.com/container-registry/docs/advanced-authentication#gcloud-helper](https://cloud.google.com/container-registry/docs/advanced-authentication#gcloud-helper).
For more details on Google Container Registry's standalone credential helpers,
see [https://github.com/GoogleCloudPlatform/docker-credential-gcr](https://github.com/GoogleCloudPlatform/docker-credential-gcr).
For more details on Docker credential helpers, see [https://docs.docker.com/engine/reference/commandline/login/#credential-helpers](https://docs.docker.com/engine/reference/commandline/login/#credential-helpers).

**EXAMPLES**

: To configure docker authentication after logging into gcloud, run:

```
gcloud alpha auth configure-docker
```

To configure docker authentication with Container Registry, e.g.,
`gcr.io`, run:

```
gcloud alpha auth configure-docker gcr.io
```

**POSITIONAL ARGUMENTS**

: **[`REGISTRIES`]**:
The comma-separated list of registries to configure the credential helper for.
Container Registry is a service for storing private container images. For
available registries, see [https://cloud.google.com/container-registry/docs/pushing-and-pulling#add-registry](https://cloud.google.com/container-registry/docs/pushing-and-pulling#add-registry).

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
allowlist. These variants are also available:

```
gcloud auth configure-docker
```

```
gcloud beta auth configure-docker
```