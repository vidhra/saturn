# gcloud preview config configurations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations/describe](https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations/describe)*

**NAME**

: **gcloud preview config configurations describe - describes a named configuration by listing its properties**

**SYNOPSIS**

: **`gcloud preview config configurations describe` `[CONFIGURATION_NAME](https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations/describe#CONFIGURATION_NAME)` [`[--all](https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations/describe#--all)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(PREVIEW)` Describes a named configuration by listing its
properties.
See `[gcloud topic
configurations](https://cloud.google.com/sdk/gcloud/reference/topic/configurations)` for an overview of named configurations.

**EXAMPLES**

: To describe an existing configuration named `my-config`, run:

```
gcloud preview config configurations describe my-config
```

This is similar to:

```
gcloud config configurations activate my-config
```

```
gcloud config list
```

**POSITIONAL ARGUMENTS**

: **`CONFIGURATION_NAME`**:
Name of the configuration to describe

**FLAGS**

: **--all**:
Include unset properties in output.

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
gcloud config configurations describe
```

```
gcloud alpha config configurations describe
```

```
gcloud beta config configurations describe
```