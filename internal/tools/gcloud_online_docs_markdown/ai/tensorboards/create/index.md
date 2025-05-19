# gcloud ai tensorboards create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ai/tensorboards/create](https://cloud.google.com/sdk/gcloud/reference/ai/tensorboards/create)*

**NAME**

: **gcloud ai tensorboards create - create a new Vertex AI Tensorboard**

**SYNOPSIS**

: **`gcloud ai tensorboards create` `[--display-name](https://cloud.google.com/sdk/gcloud/reference/ai/tensorboards/create#--display-name)`=`DISPLAY_NAME` [`[--description](https://cloud.google.com/sdk/gcloud/reference/ai/tensorboards/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/ai/tensorboards/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/ai/tensorboards/create#--region)`=`REGION`] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/ai/tensorboards/create#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/ai/tensorboards/create#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/ai/tensorboards/create#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/ai/tensorboards/create#--kms-project)`=`KMS_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ai/tensorboards/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Vertex AI Tensorboard.

**EXAMPLES**

: To create a Tensorboard with the display name `my tensorboard`:

```
gcloud ai tensorboards create --display-name="my tensorboard"
```

You may also provide a description:

```
gcloud ai tensorboards create --description="my description"
```

You may also provide labels:

```
gcloud ai tensorboards create --labels="label1=value1" --labels="label2=value2"
```

**REQUIRED FLAGS**

: **--display-name**:
Display name of the tensorboard.

**OPTIONAL FLAGS**

: **--description**:
Description of the tensorboard.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**Region resource - Cloud region to create a Tensorboard. This represents a Cloud
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
gcloud alpha ai tensorboards create
```

```
gcloud beta ai tensorboards create
```