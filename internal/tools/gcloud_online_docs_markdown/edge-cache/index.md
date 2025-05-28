# gcloud edge-cache  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cache](https://cloud.google.com/sdk/gcloud/reference/edge-cache)*

**NAME**

: **gcloud edge-cache - manage Media CDN resources**

**SYNOPSIS**

: **`gcloud edge-cache` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/edge-cache#GROUP)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cache#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage Media CDN resources.

**EXAMPLES**

: To list EdgeCacheService resources in the active Cloud Platform project, run:

```
gcloud edge-cache services list
```

To create an EdgeCacheOrigin resource named 'my-origin' that points to a Cloud
Storage bucket, run:

```
gcloud edge-cache origins create my-origin --origin-address="gs://bucket"
```

To import an EdgeCacheService resource configuration from a YAML definition,
run:

```
gcloud edge-cache services import my-service --source=config.yaml
```

To describe an EdgeCacheKeyset resource named 'my-keyset', run:

```
gcloud edge-cache keysets describe my-keyset
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[keysets](https://cloud.google.com/sdk/gcloud/reference/edge-cache/keysets)`**:
Interact with and manage EdgeCacheKeyset resources.

**`[operations](https://cloud.google.com/sdk/gcloud/reference/edge-cache/operations)`**:
Manage EdgeCache operations.

**`[origins](https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins)`**:
Interact with and manage EdgeCacheOrigin resources.

**`[services](https://cloud.google.com/sdk/gcloud/reference/edge-cache/services)`**:
Interact with and manage EdgeCacheService resources.

**NOTES**

: This variant is also available:

```
gcloud alpha edge-cache
```