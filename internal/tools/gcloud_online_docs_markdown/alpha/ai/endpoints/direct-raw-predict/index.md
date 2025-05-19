# gcloud alpha ai endpoints direct-raw-predict  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/direct-raw-predict](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/direct-raw-predict)*

**NAME**

: **gcloud alpha ai endpoints direct-raw-predict - run Vertex AI online direct raw prediction**

**SYNOPSIS**

: **`gcloud alpha ai endpoints direct-raw-predict` (`[ENDPOINT](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/direct-raw-predict#ENDPOINT)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/direct-raw-predict#--region)`=`REGION`) `[--json-request](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/direct-raw-predict#--json-request)`=`JSON_REQUEST` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/direct-raw-predict#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha ai endpoints direct-raw-predict`
sends a direct raw prediction request to Vertex AI endpoint for the given input.
The request limit is 10MB.

**EXAMPLES**

: To direct raw predict against an endpoint
``123`` under project
``example`` in region
``us-central1``, run:

```
gcloud alpha ai endpoints direct-raw-predict 123 --project=example --region=us-central1 --json-request=input.json
```

**POSITIONAL ARGUMENTS**

: **Endpoint resource - The endpoint to do online direct raw prediction. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
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
  "method_name": "my.method.Predict",
  "input": "my request bytes"
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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud ai endpoints direct-raw-predict
```

```
gcloud beta ai endpoints direct-raw-predict
```