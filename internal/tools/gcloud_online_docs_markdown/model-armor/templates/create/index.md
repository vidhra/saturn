# gcloud model-armor templates create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/create](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/create)*

**NAME**

: **gcloud model-armor templates create - create Model Armor Template**

**SYNOPSIS**

: **`gcloud model-armor templates create` (`[TEMPLATE](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/create#TEMPLATE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/create#--location)`=`LOCATION`) (`[--malicious-uri-filter-settings-enforcement](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/create#--malicious-uri-filter-settings-enforcement)`=`MALICIOUS_URI_FILTER_SETTINGS_ENFORCEMENT` `[--rai-settings-filters](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/create#--rai-settings-filters)`=[`confidenceLevel`=`CONFIDENCELEVEL`],[`filterType`=`FILTERTYPE`] `[--basic-config-filter-enforcement](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/create#--basic-config-filter-enforcement)`=`BASIC_CONFIG_FILTER_ENFORCEMENT`     | `[--advanced-config-deidentify-template](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/create#--advanced-config-deidentify-template)`=`ADVANCED_CONFIG_DEIDENTIFY_TEMPLATE` `[--advanced-config-inspect-template](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/create#--advanced-config-inspect-template)`=`ADVANCED_CONFIG_INSPECT_TEMPLATE` `[--pi-and-jailbreak-filter-settings-confidence-level](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/create#--pi-and-jailbreak-filter-settings-confidence-level)`=`PI_AND_JAILBREAK_FILTER_SETTINGS_CONFIDENCE_LEVEL` `[--pi-and-jailbreak-filter-settings-enforcement](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/create#--pi-and-jailbreak-filter-settings-enforcement)`=`PI_AND_JAILBREAK_FILTER_SETTINGS_ENFORCEMENT`) [`[--labels](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/create#--labels)`=[`LABELS`,…]] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/create#--request-id)`=`REQUEST_ID`] [`[--template-metadata-custom-llm-response-safety-error-code](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/create#--template-metadata-custom-llm-response-safety-error-code)`=`TEMPLATE_METADATA_CUSTOM_LLM_RESPONSE_SAFETY_ERROR_CODE` `[--template-metadata-custom-llm-response-safety-error-message](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/create#--template-metadata-custom-llm-response-safety-error-message)`=`TEMPLATE_METADATA_CUSTOM_LLM_RESPONSE_SAFETY_ERROR_MESSAGE` `[--template-metadata-custom-prompt-safety-error-code](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/create#--template-metadata-custom-prompt-safety-error-code)`=`TEMPLATE_METADATA_CUSTOM_PROMPT_SAFETY_ERROR_CODE` `[--template-metadata-custom-prompt-safety-error-message](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/create#--template-metadata-custom-prompt-safety-error-message)`=`TEMPLATE_METADATA_CUSTOM_PROMPT_SAFETY_ERROR_MESSAGE` `[--template-metadata-ignore-partial-invocation-failures](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/create#--template-metadata-ignore-partial-invocation-failures)` `[--template-metadata-log-operations](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/create#--template-metadata-log-operations)` `[--template-metadata-log-sanitize-operations](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/create#--template-metadata-log-sanitize-operations)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/model-armor/templates/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a new Template in a given project and location.

**EXAMPLES**

: To create a Template, run:
```
gcloud model-armor templates create my-template --location=us-central1 --malicious-uri-filter-settings-enforcement=enabled
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

**REQUIRED FLAGS**

: **--malicious-uri-filter-settings-enforcement**

**OPTIONAL FLAGS**

: **--labels**:
Labels as key value pairs.

**`KEY`**:
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers.

**`VALUE`**:
Values must contain only hyphens (`-`), underscores (`_`),
lowercase characters, and numbers.

`Shorthand Example:`

```
--labels=string=string
```

`JSON Example:`

```
--labels='{"string": "string"}'
```

`File Example:`

```
--labels=path_to_file.(yaml|json)
```

**--request-id**:
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

**--template-metadata-custom-llm-response-safety-error-code**

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
gcloud alpha model-armor templates create
```