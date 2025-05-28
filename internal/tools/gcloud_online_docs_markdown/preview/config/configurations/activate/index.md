# gcloud preview config configurations activate  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations/activate](https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations/activate)*

**NAME**

: **gcloud preview config configurations activate - activates an existing named configuration**

**SYNOPSIS**

: **`gcloud preview config configurations activate` `[CONFIGURATION_NAME](https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations/activate#CONFIGURATION_NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations/activate#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(PREVIEW)` Activates an existing named configuration.
See `[gcloud topic
configurations](https://cloud.google.com/sdk/gcloud/reference/topic/configurations)` for an overview of named configurations.

**EXAMPLES**

: To activate an existing configuration named `my-config`, run:

```
gcloud preview config configurations activate my-config
```

To list all properties in the activated configuration, run:

```
gcloud config list --all
```

**POSITIONAL ARGUMENTS**

: **`CONFIGURATION_NAME`**:
Name of the configuration to activate

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
gcloud config configurations activate
```

```
gcloud alpha config configurations activate
```

```
gcloud beta config configurations activate
```