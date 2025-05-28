# gcloud gemini data-sharing-with-google-settings setting-bindings describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings/describe](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings/describe)*

**NAME**

: **gcloud gemini data-sharing-with-google-settings setting-bindings describe - describe settingBindings**

**SYNOPSIS**

: **`gcloud gemini data-sharing-with-google-settings setting-bindings describe` (`[SETTING_BINDING](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings/describe#SETTING_BINDING)` : `[--data-sharing-with-google-setting](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings/describe#--data-sharing-with-google-setting)`=`DATA_SHARING_WITH_GOOGLE_SETTING` `[--location](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a settingBinding

**EXAMPLES**

: To describe the settingBinding, run:
$ [gcloud
gemini data-sharing-with-google-settings setting-bindings](https://cloud.google.com/sdk/gcloud/reference/gemini/data-sharing-with-google-settings/setting-bindings) \
```
describe
```

**POSITIONAL ARGUMENTS**

: **SettingBinding resource - Name of the resource. The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `setting_binding` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SETTING_BINDING`**:
ID of the settingBinding or fully qualified identifier for the settingBinding.
To set the `setting_binding` attribute:

- provide the argument `setting_binding` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--data-sharing-with-google-setting**:
The dataSharingWithGoogleSetting id of the settingBinding resource.
To set the `data-sharing-with-google-setting` attribute:

- provide the argument `setting_binding` on the command line with a
fully specified name;
- provide the argument `--data-sharing-with-google-setting` on the
command line.

**--location**:
The location id of the settingBinding resource.
To set the `location` attribute:

- provide the argument `setting_binding` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.**

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