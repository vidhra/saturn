# gcloud ai endpoints direct-predict  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ai/endpoints/direct-predict](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints/direct-predict)*

**NAME**

: **gcloud ai endpoints direct-predict - run Vertex AI online direct prediction**

**SYNOPSIS**

: **`gcloud ai endpoints direct-predict` (`[ENDPOINT](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints/direct-predict#ENDPOINT)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints/direct-predict#--region)`=`REGION`) `[--json-request](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints/direct-predict#--json-request)`=`JSON_REQUEST` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ai/endpoints/direct-predict#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud ai endpoints direct-predict` sends a direct prediction
request to Vertex AI endpoint for the given instances. The request limit is
10MB.

**EXAMPLES**

: To direct predict against an endpoint ``123``
under project ``example`` in region
``us-central1``, run:

```
gcloud ai endpoints direct-predict 123 --project=example --region=us-central1 --json-request=input.json
```

**POSITIONAL ARGUMENTS**

: **Endpoint resource - The endpoint to do online direct prediction. The arguments
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
  "inputs": [
    {"dtype": "STRING", shape: [1], "string_val": ["hello world"]},
    {"dtype": "INT32", shape: [1], "int_val": [42]}
  ]
}
```

This flag accepts "-" for stdin.

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
gcloud alpha ai endpoints direct-predict
```

```
gcloud beta ai endpoints direct-predict
```