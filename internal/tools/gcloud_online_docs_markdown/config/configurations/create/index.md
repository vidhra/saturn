# gcloud config configurations create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/config/configurations/create](https://cloud.google.com/sdk/gcloud/reference/config/configurations/create)*

**NAME**

: **gcloud config configurations create - creates a new named configuration**

**SYNOPSIS**

: **`gcloud config configurations create` `[CONFIGURATION_NAME](https://cloud.google.com/sdk/gcloud/reference/config/configurations/create#CONFIGURATION_NAME)` [`[--no-activate](https://cloud.google.com/sdk/gcloud/reference/config/configurations/create#--activate)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/config/configurations/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a new named configuration.
Except for special cases (NONE), configuration names start with a lower case
letter and contain only lower case letters a-z, digits 0-9, and hyphens '-'.
See `[gcloud topic
configurations](https://cloud.google.com/sdk/gcloud/reference/topic/configurations)` for an overview of named configurations.

**EXAMPLES**

: To create a new named configuration, run:

```
gcloud config configurations create my-config
```

**POSITIONAL ARGUMENTS**

: **`CONFIGURATION_NAME`**:
Name of the configuration to create

**FLAGS**

: **--activate**:
If true, activate this configuration upon create. Enabled by default, use
`--no-activate` to disable.

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

: These variants are also available:

```
gcloud alpha config configurations create
```

```
gcloud beta config configurations create
```

```
gcloud preview config configurations create
```