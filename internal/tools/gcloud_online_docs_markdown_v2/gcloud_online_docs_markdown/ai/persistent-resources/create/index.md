# gcloud ai persistent-resources create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ai/persistent-resources/create](https://cloud.google.com/sdk/gcloud/reference/ai/persistent-resources/create)*

**NAME**

: **gcloud ai persistent-resources create - create a new persistent resource**

**SYNOPSIS**

: **`gcloud ai persistent-resources create` `[--persistent-resource-id](https://cloud.google.com/sdk/gcloud/reference/ai/persistent-resources/create#--persistent-resource-id)`=`PERSISTENT_RESOURCE_ID` (`[--config](https://cloud.google.com/sdk/gcloud/reference/ai/persistent-resources/create#--config)`=`CONFIG` `[--resource-pool-spec](https://cloud.google.com/sdk/gcloud/reference/ai/persistent-resources/create#--resource-pool-spec)`=[`RESOURCE_POOL_SPEC`,…]) [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/ai/persistent-resources/create#--display-name)`=`DISPLAY_NAME`] [`[--enable-custom-service-account](https://cloud.google.com/sdk/gcloud/reference/ai/persistent-resources/create#--enable-custom-service-account)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/ai/persistent-resources/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--network](https://cloud.google.com/sdk/gcloud/reference/ai/persistent-resources/create#--network)`=`NETWORK`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/ai/persistent-resources/create#--region)`=`REGION`] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/ai/persistent-resources/create#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/ai/persistent-resources/create#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/ai/persistent-resources/create#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/ai/persistent-resources/create#--kms-project)`=`KMS_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ai/persistent-resources/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command will create a persistent resource on the users project to use with
Vertex AI custom training jobs. Persistent resources remain active until they
are deleted by the user.

**EXAMPLES**

: To create a PersistentResource under project
``example`` in region
``us-central1``, run:

```
gcloud ai persistent-resources create --region=us-central1 --project=example --resource-pool-spec=replica-count=1,machine-type='n1-standard-4' --display-name=example-resource
```

**REQUIRED FLAGS**

: **--persistent-resource-id**:
User-specified ID of the Persistent Resource.

**--config**

**OPTIONAL FLAGS**

: **--display-name**:
Display name of the Persistent Resource.

**--enable-custom-service-account**:
Whether or not to use a custom user-managed service account with this Persistent
Resource.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--network**:
Full name of the Google Compute Engine network to which the Job is peered with.
Private services access must already have been configured. If unspecified, the
Job is not peered with any network.

**Region resource - Cloud region to create a Persistent Resource. This represents
a Cloud resource. (NOTE) Some attributes are not given arguments in this group
but can be set in other ways.
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

**--kms-key**

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
gcloud alpha ai persistent-resources create
```

```
gcloud beta ai persistent-resources create
```