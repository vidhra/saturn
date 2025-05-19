# gcloud alpha ai models delete-version  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/delete-version](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/delete-version)*

**NAME**

: **gcloud alpha ai models delete-version - delete an existing Vertex AI model version**

**SYNOPSIS**

: **`gcloud alpha ai models delete-version` (`[MODEL_VERSION](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/delete-version#MODEL_VERSION)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/delete-version#--region)`=`REGION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/models/delete-version#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To delete a model `123` of version `1234` under project
`example` in region `us-central1`, run:

```
gcloud alpha ai models delete-version 123@1234 --project=example --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Model resource - Model version to delete. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `model_version` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`MODEL_VERSION`**:
ID of the model or fully qualified identifier for the model.
To set the `name` attribute:

- provide the argument `model_version` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Cloud region for the model.
To set the `region` attribute:

- provide the argument `model_version` on the command line with a fully
specified name;
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
gcloud ai models delete-version
```

```
gcloud beta ai models delete-version
```