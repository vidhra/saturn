# gcloud model-armor templates sanitize-model-response  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/sanitize-model-response](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/sanitize-model-response)*

**NAME**

: **gcloud model-armor templates sanitize-model-response - sanitize Model Response**

**SYNOPSIS**

: **`gcloud model-armor templates sanitize-model-response` (`[TEMPLATE](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/sanitize-model-response#TEMPLATE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/sanitize-model-response#--location)`=`LOCATION`) [`[--user-prompt](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/sanitize-model-response#--user-prompt)`=`USER_PROMPT`] [`[--model-response-data-text](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/sanitize-model-response#--model-response-data-text)`=`MODEL_RESPONSE_DATA_TEXT`     | `[--model-response-data-byte-item-from-file](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/sanitize-model-response#--model-response-data-byte-item-from-file)`=`PATH_TO_FILE` `[--model-response-data-byte-item-type](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/sanitize-model-response#--model-response-data-byte-item-type)`=`MODEL_RESPONSE_DATA_BYTE_ITEM_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/sanitize-model-response#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Sanitizes a model response.

**EXAMPLES**

: To sanitize a model response, run:
```
gcloud model-armor templates sanitize-model-response my-template --location=us-central1 --model-response-data="test-model-response"
```

**POSITIONAL ARGUMENTS**

: **Template resource - Represents resource name of template e.g.
name=projects/sample-project/locations/us-central1/templates/templ01 The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `template` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TEMPLATE`**:
ID of the template or fully qualified identifier for the template.
To set the `template` attribute:

- provide the argument `template` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location id of the template resource.
To set the `location` attribute:

- provide the argument `template` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--user-prompt**:
User Prompt associated with Model response.

**--model-response-data-text**

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

**API REFERENCE**

: This command uses the `modelarmor/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/security-command-center/docs/model-armor-overview](https://cloud.google.com/security-command-center/docs/model-armor-overview)

**NOTES**

: This variant is also available:

```
gcloud alpha model-armor templates sanitize-model-response
```