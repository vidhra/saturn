# gcloud config configurations  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/config/configurations](https://cloud.google.com/sdk/gcloud/reference/config/configurations)*

**NAME**

: **gcloud config configurations - manage the set of gcloud named configurations**

**SYNOPSIS**

: **`gcloud config configurations` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/config/configurations#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/config/configurations#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage the set of gcloud named configurations.
The current configuration can be managed via the CLOUDSDK_ACTIVE_CONFIG_NAME
environment variable or a configuration property. See `[gcloud topic
configurations](https://cloud.google.com/sdk/gcloud/reference/topic/configurations)` for an overview of named configurations.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[activate](https://cloud.google.com/sdk/gcloud/reference/config/configurations/activate)`**:
Activates an existing named configuration.

**`[create](https://cloud.google.com/sdk/gcloud/reference/config/configurations/create)`**:
Creates a new named configuration.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/config/configurations/delete)`**:
Deletes a named configuration.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/config/configurations/describe)`**:
Describes a named configuration by listing its properties.

**`[list](https://cloud.google.com/sdk/gcloud/reference/config/configurations/list)`**:
Lists existing named configurations.

**`[rename](https://cloud.google.com/sdk/gcloud/reference/config/configurations/rename)`**:
Renames a named configuration.

**NOTES**

: These variants are also available:

```
gcloud alpha config configurations
```

```
gcloud beta config configurations
```

```
gcloud preview config configurations
```