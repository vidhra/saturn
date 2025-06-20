# gcloud preview config configurations rename  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations/rename](https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations/rename)*

**NAME**

: **gcloud preview config configurations rename - renames a named configuration**

**SYNOPSIS**

: **`gcloud preview config configurations rename` `[CONFIGURATION_NAME](https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations/rename#CONFIGURATION_NAME)` `[--new-name](https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations/rename#--new-name)`=`NEW_NAME` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations/rename#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(PREVIEW)` Renames a named configuration.
See `[gcloud topic
configurations](https://cloud.google.com/sdk/gcloud/reference/topic/configurations)` for an overview of named configurations.

**EXAMPLES**

: To rename an existing configuration named `my-config`, run:

```
gcloud preview config configurations rename my-config --new-name=new-config
```

**POSITIONAL ARGUMENTS**

: **`CONFIGURATION_NAME`**:
Name of the configuration to rename

**REQUIRED FLAGS**

: **--new-name**:
Specifies the new name of the configuration.

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

: This command is currently in DEVELOPER PREVIEW and may change without notice. If
this command fails with API permission errors despite specifying the correct
project, you might be trying to access an API with an invitation-only early
access allowlist. These variants are also available:

```
gcloud config configurations rename
```

```
gcloud alpha config configurations rename
```

```
gcloud beta config configurations rename
```