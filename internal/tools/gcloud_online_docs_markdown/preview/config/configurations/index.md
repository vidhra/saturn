# gcloud preview config configurations  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations](https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations)*

**NAME**

: **gcloud preview config configurations - manage the set of gcloud named configurations**

**SYNOPSIS**

: **`gcloud preview config configurations` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(PREVIEW)` Manage the set of gcloud named configurations.
The current configuration can be managed via the CLOUDSDK_ACTIVE_CONFIG_NAME
environment variable or a configuration property. See `[gcloud topic
configurations](https://cloud.google.com/sdk/gcloud/reference/topic/configurations)` for an overview of named configurations.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[activate](https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations/activate)`**:
`(PREVIEW)` Activates an existing named configuration.

**`[create](https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations/create)`**:
`(PREVIEW)` Creates a new named configuration.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations/delete)`**:
`(PREVIEW)` Deletes a named configuration.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations/describe)`**:
`(PREVIEW)` Describes a named configuration by listing its
properties.

**`[list](https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations/list)`**:
`(PREVIEW)` Lists existing named configurations.

**`[rename](https://cloud.google.com/sdk/gcloud/reference/preview/config/configurations/rename)`**:
`(PREVIEW)` Renames a named configuration.

**NOTES**

: This command is currently in DEVELOPER PREVIEW and may change without notice. If
this command fails with API permission errors despite specifying the correct
project, you might be trying to access an API with an invitation-only early
access allowlist. These variants are also available:

```
gcloud config configurations
```

```
gcloud alpha config configurations
```

```
gcloud beta config configurations
```