# gcloud alpha artifacts docker images describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/describe)*

**NAME**

: **gcloud alpha artifacts docker images describe - describe an Artifact Registry container image**

**SYNOPSIS**

: **`gcloud alpha artifacts docker images describe` `[IMAGE](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/describe#IMAGE)` [`[--metadata-filter](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/describe#--metadata-filter)`=`METADATA_FILTER`] [`[--show-all-metadata](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/describe#--show-all-metadata)`] [`[--show-build-details](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/describe#--show-build-details)`] [`[--show-deployment](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/describe#--show-deployment)`] [`[--show-image-basis](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/describe#--show-image-basis)`] [`[--show-package-vulnerability](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/describe#--show-package-vulnerability)`] [`[--show-provenance](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/describe#--show-provenance)`] [`[--show-sbom-references](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/describe#--show-sbom-references)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Reference an image by tag or digest using the format:

```
LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE:tag
LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE@sha256:digest
```

This command can fail for the following reasons:

- The repository format is invalid.
- The specified image does not exist.
- The active account does not have permission to run the command
(`roles/artifactregistry.reader`,
`roles/containeranalysis.admin` and
`roles/serviceusage.serviceUsageViewer`).

**EXAMPLES**

: To describe an image digest `abcxyz` under image
`busy-box`:

```
gcloud alpha artifacts docker images describe us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz
```

To describe an image `busy-box` with tag `my-tag`:

```
gcloud alpha artifacts docker images describe us-west1-docker.pkg.dev/my-project/my-repository/busy-box:my-tag
```

**POSITIONAL ARGUMENTS**

: **`IMAGE`**:
A container image.
A valid container image has the format of
LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE
A valid container image that can be referenced by tag or digest, has the format
of LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE:tag
LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE@sha256:digest

**FLAGS**

: **--metadata-filter**:
Additional filter to fetch metadata for a given qualified image reference.

**--show-all-metadata**:
Include all metadata in the output. Metadata will be grouped by Grafeas kind,
with an additional section for intoto provenance metadata.

**--show-build-details**:
Include build metadata in the output.

**--show-deployment**:
Include deployment metadata in the output.

**--show-image-basis**:
Include base image metadata in the output.

**--show-package-vulnerability**:
Include vulnerability metadata in the output.

**--show-provenance**:
Include intoto provenance metadata in the output, in the provenance_summary
section. To see all build metadata in the output, use --show-all-metadata or
--show-build-details.

**--show-sbom-references**:
Include SBOM metadata in the output.

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
gcloud artifacts docker images describe
```

```
gcloud beta artifacts docker images describe
```