# gcloud model-armor templates update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update)*

**NAME**

: **gcloud model-armor templates update - update Model Armor Template**

**SYNOPSIS**

: **`gcloud model-armor templates update` (`[TEMPLATE](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#TEMPLATE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--location)`=`LOCATION`) [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--request-id)`=`REQUEST_ID`] [`[--clear-filter-config](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--clear-filter-config)` `[--malicious-uri-filter-settings-enforcement](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--malicious-uri-filter-settings-enforcement)`=`MALICIOUS_URI_FILTER_SETTINGS_ENFORCEMENT` `[--basic-config-filter-enforcement](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--basic-config-filter-enforcement)`=`BASIC_CONFIG_FILTER_ENFORCEMENT`     | `[--advanced-config-deidentify-template](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--advanced-config-deidentify-template)`=`ADVANCED_CONFIG_DEIDENTIFY_TEMPLATE` `[--advanced-config-inspect-template](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--advanced-config-inspect-template)`=`ADVANCED_CONFIG_INSPECT_TEMPLATE` `[--pi-and-jailbreak-filter-settings-confidence-level](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--pi-and-jailbreak-filter-settings-confidence-level)`=`PI_AND_JAILBREAK_FILTER_SETTINGS_CONFIDENCE_LEVEL` `[--pi-and-jailbreak-filter-settings-enforcement](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--pi-and-jailbreak-filter-settings-enforcement)`=`PI_AND_JAILBREAK_FILTER_SETTINGS_ENFORCEMENT` `[--rai-settings-filters](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--rai-settings-filters)`=[`confidenceLevel`=`CONFIDENCELEVEL`],[`filterType`=`FILTERTYPE`]     | `[--add-rai-settings-filters](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--add-rai-settings-filters)`=[`confidenceLevel`=`CONFIDENCELEVEL`],[`filterType`=`FILTERTYPE`] `[--clear-rai-settings-filters](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--clear-rai-settings-filters)`     | `[--remove-rai-settings-filters](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--remove-rai-settings-filters)`=[`confidenceLevel`=`CONFIDENCELEVEL`],[`filterType`=`FILTERTYPE`]] [`[--clear-template-metadata](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--clear-template-metadata)` `[--template-metadata-custom-llm-response-safety-error-code](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--template-metadata-custom-llm-response-safety-error-code)`=`TEMPLATE_METADATA_CUSTOM_LLM_RESPONSE_SAFETY_ERROR_CODE` `[--template-metadata-custom-llm-response-safety-error-message](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--template-metadata-custom-llm-response-safety-error-message)`=`TEMPLATE_METADATA_CUSTOM_LLM_RESPONSE_SAFETY_ERROR_MESSAGE` `[--template-metadata-custom-prompt-safety-error-code](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--template-metadata-custom-prompt-safety-error-code)`=`TEMPLATE_METADATA_CUSTOM_PROMPT_SAFETY_ERROR_CODE` `[--template-metadata-custom-prompt-safety-error-message](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--template-metadata-custom-prompt-safety-error-message)`=`TEMPLATE_METADATA_CUSTOM_PROMPT_SAFETY_ERROR_MESSAGE` `[--[no-]template-metadata-ignore-partial-invocation-failures](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--[no-]template-metadata-ignore-partial-invocation-failures)` `[--[no-]template-metadata-log-operations](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--[no-]template-metadata-log-operations)` `[--[no-]template-metadata-log-sanitize-operations](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--[no-]template-metadata-log-sanitize-operations)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--labels)`=[`LABELS`,…]     | `[--update-labels](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--update-labels)`=[`UPDATE_LABELS`,…] `[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#--remove-labels)`=[__REMOVE_LABELS,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates a Template.

**EXAMPLES**

: To update a Template, run:
```
gcloud model-armor templates update my-template --location=us-central1 --clear-labels
```

**POSITIONAL ARGUMENTS**

: **Template resource - Identifier. name of resource The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
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

: **--request-id**:
An optional request ID to identify requests. Specify a unique request ID so that
if you must retry your request, the server will know to ignore the request if it
has already been completed. The server stores the request ID for 60 minutes
after the first request.
For example, consider a situation where you make an initial request and the
request times out. If you make the request again with the same request ID, the
server can check if original operation with the same request ID was received,
and if so, will ignore the second request. This prevents clients from
accidentally creating duplicate commitments.
The request ID must be a valid UUID with the exception that zero UUID is not
supported (00000000-0000-0000-0000-000000000000).

**--clear-filter-config**

**--clear-template-metadata**

**--labels**

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
gcloud alpha model-armor templates update
```