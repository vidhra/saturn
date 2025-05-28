# gcloud config configurations delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/config/configurations/delete](https://cloud.google.com/sdk/gcloud/reference/config/configurations/delete)*

**NAME**

: **gcloud config configurations delete - deletes a named configuration**

**SYNOPSIS**

: **`gcloud config configurations delete` `[CONFIGURATION_NAMES](https://cloud.google.com/sdk/gcloud/reference/config/configurations/delete#CONFIGURATION_NAMES)` [`[CONFIGURATION_NAMES](https://cloud.google.com/sdk/gcloud/reference/config/configurations/delete#CONFIGURATION_NAMES)` …] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/config/configurations/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Deletes a named configuration. You cannot delete a configuration that is active,
even when overridden with the --configuration flag. To delete the current active
configuration, first `[gcloud config
configurations activate](https://cloud.google.com/sdk/gcloud/reference/config/configurations/activate)` another one.
See `[gcloud topic
configurations](https://cloud.google.com/sdk/gcloud/reference/topic/configurations)` for an overview of named configurations.

**EXAMPLES**

: To delete an existing configuration named `my-config`, run:

```
gcloud config configurations delete my-config
```

To delete more than one configuration, run:

```
gcloud config configurations delete my-config1 my-config2
```

To list existing configurations, run:

```
gcloud config configurations list
```

**POSITIONAL ARGUMENTS**

: **`CONFIGURATION_NAMES` [`CONFIGURATION_NAMES` …]**:
Name of the configuration to delete. Cannot be currently active configuration.

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
gcloud alpha config configurations delete
```

```
gcloud beta config configurations delete
```

```
gcloud preview config configurations delete
```