# gcloud alpha ai-platform explain  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/explain](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/explain)*

**NAME**

: **gcloud alpha ai-platform explain - run AI Platform explanation**

**SYNOPSIS**

: **`gcloud alpha ai-platform explain` `[--model](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/explain#--model)`=`MODEL` (`[--json-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/explain#--json-instances)`=`JSON_INSTANCES`     | `[--json-request](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/explain#--json-request)`=`JSON_REQUEST`     | `[--text-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/explain#--text-instances)`=`TEXT_INSTANCES`) [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/explain#--region)`=`REGION`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/explain#--version)`=`VERSION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/explain#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha ai-platform explain` sends an
explain request to AI Platform for the given instances. This command will read
up to 100 instances, though the service itself will accept instances up to the
payload limit size (currently, 1.5MB).

**EXAMPLES**

: To get explanations for an AI Platform version model with the version 'version'
and with the name 'model-name', run:

```
gcloud alpha ai-platform explain explain --model=model-name --version=version --json-instances=instances.json
```

**REQUIRED FLAGS**

: **--model**:
Name of the model.

**--json-instances**

**OPTIONAL FLAGS**

: **--region**:
Google Cloud region of the regional endpoint to use for this command. For the
global endpoint, the region needs to be specified as `global`.
Learn more about regional endpoints and see a list of available regions: [https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints](https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints)
`REGION` must be one of: `global`,
`asia-east1`, `asia-northeast1`,
`asia-southeast1`, `australia-southeast1`,
`europe-west1`, `europe-west2`, `europe-west3`,
`europe-west4`, `northamerica-northeast1`,
`us-central1`, `us-east1`, `us-east4`,
`us-west1`.

**--version**:
Model version to be used.
If unspecified, the default version of the model will be used. To list model
versions run

```
gcloud alpha ai-platform versions list
```

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
gcloud beta ai-platform explain
```