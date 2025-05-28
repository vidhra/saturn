# gcloud beta ai endpoints undeploy-model  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/undeploy-model](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/undeploy-model)*

**NAME**

: **gcloud beta ai endpoints undeploy-model - undeploy a model from an existing Vertex AI endpoint**

**SYNOPSIS**

: **`gcloud beta ai endpoints undeploy-model` (`[ENDPOINT](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/undeploy-model#ENDPOINT)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/undeploy-model#--region)`=`REGION`) `[--deployed-model-id](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/undeploy-model#--deployed-model-id)`=`DEPLOYED_MODEL_ID` [`[--traffic-split](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/undeploy-model#--traffic-split)`=[`DEPLOYED_MODEL_ID`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/undeploy-model#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To undeploy a model ``456`` from an endpoint
``123`` under project
``example`` in region
``us-central1``, run:

```
gcloud beta ai endpoints undeploy-model 123 --project=example --region=us-central1 --deployed-model-id=456
```

**POSITIONAL ARGUMENTS**

: **Endpoint resource - The endpoint to undeploy a model from. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `endpoint` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ENDPOINT`**:
ID of the endpoint or fully qualified identifier for the endpoint.
To set the `name` attribute:

- provide the argument `endpoint` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Cloud region for the endpoint.
To set the `region` attribute:

- provide the argument `endpoint` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `ai/region`;
- choose one from the prompted list of available regions.**

**REQUIRED FLAGS**

: **--deployed-model-id**:
Id of the deployed model.

**OPTIONAL FLAGS**

: **--traffic-split**:
List of pairs of deployed model id and value to set as traffic split.

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

: This command is currently in beta and might change without notice. These
variants are also available:

```
gcloud ai endpoints undeploy-model
```

```
gcloud alpha ai endpoints undeploy-model
```