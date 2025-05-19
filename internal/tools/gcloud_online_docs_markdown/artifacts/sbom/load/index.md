# gcloud artifacts sbom load  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/load](https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/load)*

**NAME**

: **gcloud artifacts sbom load - upload an SBOM file and create a reference occurrence**

**SYNOPSIS**

: **`gcloud artifacts sbom load` `[--source](https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/load#--source)`=`SOURCE` `[--uri](https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/load#--uri)`=`ARTIFACT_URI` [`[--destination](https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/load#--destination)`=`DESTINATION`] [`[--kms-key-version](https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/load#--kms-key-version)`=`KMS_KEY_VERSION`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/load#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/load#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Upload an SBOM file and create a reference occurrence.

**EXAMPLES**

: To upload an SBOM file at /path/to/sbom.json for a Docker image in Artifact
Registry:

```
gcloud artifacts sbom load --source=/path/to/sbom.json --uri=us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz
```

To upload an SBOM file at /path/to/sbom.json for a Docker image with a KMS key
version to sign the created SBOM reference:

```
gcloud artifacts sbom load --source=/path/to/sbom.json --uri=us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz --kms-key-version=projects/my-project/locations/us-west1/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/1
```

To upload an SBOM file at /path/to/sbom.json for a Docker image from a Docker
registry:

```
gcloud artifacts sbom load --source=/path/to/sbom.json --uri=my-docker-registry/my-image@sha256:abcxyz --destination=gs://my-cloud-storage-bucket
```

**REQUIRED FLAGS**

: **--source**:
The SBOM file for uploading.

**--uri**:
The URI of the artifact the SBOM is generated from. The URI can be a Docker
image from any Docker registries. A URI provided with a tag (e.g.
`[IMAGE]:[TAG]`) will be resolved into a URI with a digest
(`[IMAGE]@sha256:[DIGEST]`). When passing an image which is not from
Artifact Registry or Container Registry with a tag, only public images can be
resolved. Also, when passing an image which is not from Artifact Registry or
Container Registry, the `--destination` flag is required.

**OPTIONAL FLAGS**

: **--destination**:
The storage path will be used to store the SBOM file. Currently only supports
Cloud Storage paths start with 'gs://'.

**--kms-key-version**:
Cloud KMS key version to sign the SBOM reference. The key version provided
should be the resource ID in the format of
`projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]/cryptoKeyVersions/[KEY_VERSION]`.

**--location**:
If specified, all requests to Artifact Analysis for occurrences will go to
location specified

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