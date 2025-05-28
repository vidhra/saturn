# gcloud beta ai endpoints update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/update](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/update)*

**NAME**

: **gcloud beta ai endpoints update - update an existing Vertex AI endpoint**

**SYNOPSIS**

: **`gcloud beta ai endpoints update` (`[ENDPOINT](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/update#ENDPOINT)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/update#--region)`=`REGION`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/update#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/update#--display-name)`=`DISPLAY_NAME`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/update#--remove-labels)`=[`KEY`,…]] [`[--clear-traffic-split](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/update#--clear-traffic-split)`     | `[--traffic-split](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/update#--traffic-split)`=[`DEPLOYED_MODEL_ID`=`VALUE`,…]] [`[--disable-request-response-logging](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/update#--disable-request-response-logging)`     | `[--request-response-logging-rate](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/update#--request-response-logging-rate)`=`REQUEST_RESPONSE_LOGGING_RATE` `[--request-response-logging-table](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/update#--request-response-logging-table)`=`REQUEST_RESPONSE_LOGGING_TABLE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/update#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To update an endpoint ``123`` under project
``example`` in region
``us-central1``, run:

```
gcloud beta ai endpoints update 123 --project=example --region=us-central1 --display-name=new_name
```

**POSITIONAL ARGUMENTS**

: **Endpoint resource - The endpoint to update. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
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

**FLAGS**

: **--description**:
Description of the endpoint.

**--display-name**:
Display name of the endpoint.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

**--clear-traffic-split**

**--disable-request-response-logging**

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
gcloud ai endpoints update
```

```
gcloud alpha ai endpoints update
```