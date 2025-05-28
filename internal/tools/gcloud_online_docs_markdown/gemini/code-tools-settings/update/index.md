# gcloud gemini code-tools-settings update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/gemini/code-tools-settings/update](https://cloud.google.com/sdk/gcloud/reference/gemini/code-tools-settings/update)*

**NAME**

: **gcloud gemini code-tools-settings update - update codeToolsSettings**

**SYNOPSIS**

: **`gcloud gemini code-tools-settings update` (`[CODE_TOOLS_SETTING](https://cloud.google.com/sdk/gcloud/reference/gemini/code-tools-settings/update#CODE_TOOLS_SETTING)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/gemini/code-tools-settings/update#--location)`=`LOCATION`) [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/gemini/code-tools-settings/update#--request-id)`=`REQUEST_ID`] [`[--enabled-tool](https://cloud.google.com/sdk/gcloud/reference/gemini/code-tools-settings/update#--enabled-tool)`=[`accountConnector`=`ACCOUNTCONNECTOR`],[`config`=`CONFIG`],[`handle`=`HANDLE`],[`tool`=`TOOL`],[`uriOverride`=`URIOVERRIDE`]     | `[--add-enabled-tool](https://cloud.google.com/sdk/gcloud/reference/gemini/code-tools-settings/update#--add-enabled-tool)`=[`accountConnector`=`ACCOUNTCONNECTOR`],[`config`=`CONFIG`],[`handle`=`HANDLE`],[`tool`=`TOOL`],[`uriOverride`=`URIOVERRIDE`] `[--clear-enabled-tool](https://cloud.google.com/sdk/gcloud/reference/gemini/code-tools-settings/update#--clear-enabled-tool)`     | `[--remove-enabled-tool](https://cloud.google.com/sdk/gcloud/reference/gemini/code-tools-settings/update#--remove-enabled-tool)`=[`accountConnector`=`ACCOUNTCONNECTOR`],[`config`=`CONFIG`],[`handle`=`HANDLE`],[`tool`=`TOOL`],[`uriOverride`=`URIOVERRIDE`]] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/gemini/code-tools-settings/update#--labels)`=[`LABELS`,…]     | `[--update-labels](https://cloud.google.com/sdk/gcloud/reference/gemini/code-tools-settings/update#--update-labels)`=[`UPDATE_LABELS`,…] `[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/gemini/code-tools-settings/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/gemini/code-tools-settings/update#--remove-labels)`=[__REMOVE_LABELS,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/gemini/code-tools-settings/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a codeToolsSetting

**EXAMPLES**

: To update the codeToolsSetting, run:

```
gcloud gemini code-tools-settings update
```

**POSITIONAL ARGUMENTS**

: **CodeToolsSetting resource - Identifier. Name of the resource.
Format:projects/{project}/locations/{location}/codeToolsSettings/{codeToolsSetting}
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `code_tools_setting` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CODE_TOOLS_SETTING`**:
ID of the codeToolsSetting or fully qualified identifier for the
codeToolsSetting.
To set the `code_tools_setting` attribute:

- provide the argument `code_tools_setting` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location id of the codeToolsSetting resource.
To set the `location` attribute:

- provide the argument `code_tools_setting` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--request-id**:
An optional request ID to identify requests. Specify a unique request ID so that
if you must retry your request, the server will know to ignore the request if it
has already been completed. The server will guarantee that for at least 60
minutes since the first request.
For example, consider a situation where you make an initial request and the
request times out. If you make the request again with the same request ID, the
server can check if original operation with the same request ID was received,
and if so, will ignore the second request. This prevents clients from
accidentally creating duplicate commitments.
The request ID must be a valid UUID with the exception that zero UUID is not
supported (00000000-0000-0000-0000-000000000000).

**--enabled-tool**

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

: This command uses the `cloudaicompanion/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/gemini](https://cloud.google.com/gemini)