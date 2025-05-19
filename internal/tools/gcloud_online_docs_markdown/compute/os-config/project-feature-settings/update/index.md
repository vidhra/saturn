# gcloud compute os-config project-feature-settings update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/os-config/project-feature-settings/update](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/project-feature-settings/update)*

**NAME**

: **gcloud compute os-config project-feature-settings update - update VM Manager project feature settings**

**SYNOPSIS**

: **`gcloud compute os-config project-feature-settings update` `[--patch-and-config-feature-set](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/project-feature-settings/update#--patch-and-config-feature-set)`=`PATCH_AND_CONFIG_FEATURE_SET` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/project-feature-settings/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update VM Manager project feature settings.

**EXAMPLES**

: To update project feature settings for project `my-project`:

```
gcloud compute os-config project-feature-settings update --project=my-project --patch-and-config-feature-set=full
```

**REQUIRED FLAGS**

: **--patch-and-config-feature-set**:
Specifies the feature set for VM Manager.
`PATCH_AND_CONFIG_FEATURE_SET` must be one of:

**`full`**:
Full set of VM Manager functionality (alias for osconfig-c).

**`limited`**:
Limited feature set. Enables only the basic set of features (alias for
osconfig-b).

**`osconfig-b`**:
Limited feature set. Enables only the basic set of features.

**`osconfig-c`**:
Full set of VM Manager functionality.

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

: This command uses the `osconfig/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/compute/docs/osconfig/rest](https://cloud.google.com/compute/docs/osconfig/rest)