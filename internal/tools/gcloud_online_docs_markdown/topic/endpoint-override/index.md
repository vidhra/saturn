# gcloud topic endpoint-override  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/topic/endpoint-override](https://cloud.google.com/sdk/gcloud/reference/topic/endpoint-override)*

**NAME**

: **gcloud topic endpoint-override - gcloud endpoint override supplementary help**

**DESCRIPTION**

: Use API endpoint overrides to override the API endpoints used by the `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` CLI. Applications such as Private
Google Access and Private Service Connect use API endpoint overrides.

**Setting API endpoint overrides**

: `gcloud` API endpoints are defined as `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` CLI properties and can be
overridden through `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` CLI
properties or environment variables. For example, to override the API endpoint
for the `[gcloud storage](https://cloud.google.com/sdk/gcloud/reference/storage)`
command to use the private `storage-vialink1.p.googleapis.com`
endpoint with either `http://` or `https://` prefix, you
can use one of the following commands:

```
# Override using a property:
gcloud config set api_endpoint_overrides/storage https://storage-vialink1.p.googleapis.com/
```

```
# Override using an environment variable
CLOUDSDK_API_ENDPOINT_OVERRIDES_STORAGE=https://\
storage-vialink1.p.googleapis.com/
gcloud storage objects list gs://my-bucket
```

**Default API endpoints**

: To get the default value for an API endpoint override, use `[gcloud config get](https://cloud.google.com/sdk/gcloud/reference/config/get)` to
determine the correct format for your API endpoint override:

```
gcloud config get api_endpoint_overrides/storage
```

**Unsetting API endpoint overrides**

: To unset an API endpoint override, use `[gcloud config unset](https://cloud.google.com/sdk/gcloud/reference/config/unset)`:

```
gcloud config unset api_endpoint_overrides/storage
```

**Configured API endpoint overrides**

: To see the APIs which have an endpoint override set, use `[gcloud config list](https://cloud.google.com/sdk/gcloud/reference/config/list)`:

```
gcloud config list api_endpoint_overrides/
```

To see all the set and unset API endpoint override properties, use the
`--all` flag:

```
gcloud config list api_endpoint_overrides/ --all
```

**NOTES**

: These variants are also available:

```
gcloud alpha topic endpoint-override
```

```
gcloud beta topic endpoint-override
```