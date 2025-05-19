# gcloud compute backend-services export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/export](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/export)*

**NAME**

: **gcloud compute backend-services export - export a backend service**

**SYNOPSIS**

: **`gcloud compute backend-services export` `[BACKEND_SERVICE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/export#BACKEND_SERVICE_NAME)` [`[--destination](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/export#--destination)`=`DESTINATION`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/export#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/export#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Exports a backend service's configuration to a file. This configuration can be
imported at a later time.

**EXAMPLES**

: A backend service can be exported by running:

```
gcloud compute backend-services export NAME --destination=<path-to-file> --global
```

**POSITIONAL ARGUMENTS**

: **`BACKEND_SERVICE_NAME`**:
Name of the backend service to export.

**FLAGS**

: **--destination**:
Path to a YAML file where the configuration will be exported. Alternatively, you
may omit this flag to write to standard output. For a schema describing the
export/import format, see:
$CLOUDSDKROOT/lib/googlecloudsdk/schemas/compute/v1/BackendService.yaml.

**--global**

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
gcloud alpha compute backend-services export
```

```
gcloud beta compute backend-services export
```