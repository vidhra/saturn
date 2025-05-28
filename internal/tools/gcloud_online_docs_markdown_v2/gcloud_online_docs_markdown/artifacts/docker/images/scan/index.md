# gcloud artifacts docker images scan  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/scan](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/scan)*

**NAME**

: **gcloud artifacts docker images scan - perform a vulnerability scan on a container image**

**SYNOPSIS**

: **`gcloud artifacts docker images scan` `[RESOURCE_URI](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/scan#RESOURCE_URI)` [`[--additional-package-types](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/scan#--additional-package-types)`=[`ADDITIONAL_PACKAGE_TYPES`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/scan#--async)`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/scan#--location)`=`LOCATION`; default="us"] [`[--remote](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/scan#--remote)`] [`[--skip-package-types](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/scan#--skip-package-types)`=[`SKIP_PACKAGE_TYPES`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/scan#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: You can scan a container image in a Google Cloud registry (Artifact Registry or
Container Registry), or a local container image.
Reference an image by tag or digest using any of the formats:

```
Artifact Registry:
  LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE[:tag]
  LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE@sha256:digest
```

```
Container Registry:
  [LOCATION.]gcr.io/PROJECT-ID/REPOSITORY-ID/IMAGE[:tag]
  [LOCATION.]gcr.io/PROJECT-ID/REPOSITORY-ID/IMAGE@sha256:digest
```

```
Local:
  IMAGE[:tag]
```

**EXAMPLES**

: Start a scan of a container image stored in Artifact Registry:

```
gcloud artifacts docker images scan us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz --remote
```

Start a scan of a container image stored in the Container Registry, and perform
the analysis in Europe:

```
gcloud artifacts docker images scan eu.gcr.io/my-project/my-repository/my-image:latest --remote --location=europe
```

Start a scan of a container image stored locally, and perform the analysis in
Asia:

```
gcloud artifacts docker images scan ubuntu:latest --location=asia
```

**POSITIONAL ARGUMENTS**

: **`RESOURCE_URI`**:
A container image in a Google Cloud registry (Artifact Registry or Container
Registry), or a local container image.

**FLAGS**

: **--additional-package-types**:
(DEPRECATED) A comma-separated list of package types to scan in addition to OS
packages.
This flag is deprecated as scanning for all package types is now the default. To
skip scanning for specific package types, use --skip-package-types.
`ADDITIONAL_PACKAGE_TYPES` must be one of:

**`COMPOSER`**:
PHP Composer package.

**`GO`**:
Go standard library and third party packages.

**`MAVEN`**:
Maven package.

**`NPM`**:
NPM package.

**`NUGET`**:
NuGet package.

**`PYTHON`**:
Python package.

**`RUBYGEMS`**:
RubyGems package.

**`RUST`**:
Rust package.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--location**:
The API location in which to perform package analysis. Consider choosing a
location closest to where you are located. Proximity to the container image does
not affect response time. `LOCATION` must be one of:

**`asia`**:
Perform analysis in Asia

**`europe`**:
Perform analysis in Europe

**`us`**:
Perform analysis in the US

**--remote**:
Whether the container image is located remotely or on your local machine.

**--skip-package-types**:
A comma-separated list of package types to skip when scanning.
`SKIP_PACKAGE_TYPES` must be one of:

**`COMPOSER`**:
PHP Composer package.

**`GO`**:
Go standard library and third party packages.

**`MAVEN`**:
Maven package.

**`NPM`**:
NPM package.

**`NUGET`**:
NuGet package.

**`PYTHON`**:
Python package.

**`RUBYGEMS`**:
RubyGems package.

**`RUST`**:
Rust package.

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

: This variant is also available:

```
gcloud beta artifacts docker images scan
```