# gcloud alpha ai index-endpoints create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/create](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/create)*

**NAME**

: **gcloud alpha ai index-endpoints create - create a new Vertex AI index endpoint**

**SYNOPSIS**

: **`gcloud alpha ai index-endpoints create` `[--display-name](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/create#--display-name)`=`DISPLAY_NAME` [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/create#--description)`=`DESCRIPTION`] [`[--enable-private-service-connect](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/create#--enable-private-service-connect)`] [`[--encryption-kms-key-name](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/create#--encryption-kms-key-name)`=`ENCRYPTION_KMS_KEY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--network](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/create#--network)`=`NETWORK`] [`[--project-allowlist](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/create#--project-allowlist)`=[`PROJECTS`,…]] [`[--public-endpoint-enabled](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/create#--public-endpoint-enabled)`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/create#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/create#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create an index endpoint under project `example` with network
`projects/123/global/networks/test-network` in region
`us-central1`, run:

```
gcloud alpha ai index-endpoints create --display-name=index-endpoint --description=test --network=projects/123/global/networks/test-network --project=example --region=us-central1
```

**REQUIRED FLAGS**

: **--display-name**:
Display name of the index endpoint.

**OPTIONAL FLAGS**

: **--description**:
Description of the index endpoint.

**--enable-private-service-connect**:
If true, expose the index endpoint via private service connect.

**--encryption-kms-key-name**:
The Cloud KMS resource identifier of the customer managed encryption key used to
protect a resource. Has the form:
projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key.
The key needs to be in the same region as where the compute resource is created.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--network**:
The Google Compute Engine network name to which the IndexEndpoint should be
peered.

**--project-allowlist**:
List of projects from which the forwarding rule will target the service
attachment.

**--public-endpoint-enabled**:
If true, the deployed index will be accessible through public endpoint.

**Region resource - Cloud region to create index endpoint. This represents a Cloud
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
gcloud ai index-endpoints create
```

```
gcloud beta ai index-endpoints create
```