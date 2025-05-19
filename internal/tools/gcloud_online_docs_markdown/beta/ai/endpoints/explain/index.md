# gcloud beta ai endpoints explain  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/explain](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/explain)*

**NAME**

: **gcloud beta ai endpoints explain - request an online explanation from an Vertex AI endpoint**

**SYNOPSIS**

: **`gcloud beta ai endpoints explain` (`[ENDPOINT](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/explain#ENDPOINT)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/explain#--region)`=`REGION`) `[--json-request](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/explain#--json-request)`=`JSON_REQUEST` [`[--deployed-model-id](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/explain#--deployed-model-id)`=`DEPLOYED_MODEL_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/explain#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(BETA)` `gcloud beta ai endpoints explain` sends an
explanation request to the Vertex AI endpoint for the given instances. This
command reads up to 100 instances, though the service itself accepts instances
up to the payload limit size (currently, 1.5MB).

**EXAMPLES**

: To send an explanation request to the endpoint for the json file, input.json,
run:

```
gcloud beta ai endpoints explain ENDPOINT_ID --region=us-central1 --json-request=input.json
```

**POSITIONAL ARGUMENTS**

: **Endpoint resource - The endpoint to request an online explanation. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
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

: **--json-request**:
Path to a local file containing the body of a JSON request.
An example of a JSON request:

```
{
  "instances": [
    {"x": [1, 2], "y": [3, 4]},
    {"x": [-1, -2], "y": [-3, -4]}
  ]
}
```

This flag accepts "-" for stdin.

**OPTIONAL FLAGS**

: **--deployed-model-id**:
Id of the deployed model.

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
gcloud ai endpoints explain
```

```
gcloud alpha ai endpoints explain
```