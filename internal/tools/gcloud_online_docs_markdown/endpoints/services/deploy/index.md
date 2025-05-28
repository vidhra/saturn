# gcloud endpoints services deploy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy)*

**NAME**

: **gcloud endpoints services deploy - deploys a service configuration for the given service name**

**SYNOPSIS**

: **`gcloud endpoints services deploy` `[SERVICE_CONFIG_FILE](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy#SERVICE_CONFIG_FILE)` [`[SERVICE_CONFIG_FILE](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy#SERVICE_CONFIG_FILE)` …] [`[--async](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy#--async)`] [`[--force](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy#--force)`, `[-f](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy#-f)`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command is used to deploy a service configuration for a service to Google
Service Management. As input, it takes one or more paths to service
configurations that should be uploaded. These configuration files can be Proto
Descriptors, Open API (Swagger) specifications, or Google Service Configuration
files in JSON or YAML formats.
If a service name is present in multiple configuration files (given in the
`host` field in OpenAPI specifications or the `name` field
in Google Service Configuration files), the first one will take precedence.
This command will block until deployment is complete unless the
`--async` flag is passed.

**EXAMPLES**

: To deploy a single Open API service configuration, run:

```
gcloud endpoints services deploy ~/my_app/openapi.json
```

To run the deployment asynchronously (non-blocking), run:

```
gcloud endpoints services deploy ~/my_app/openapi.json --async
```

To deploy a service config with a Proto, run:

```
gcloud endpoints services deploy ~/my_app/service-config.yaml ~/my_app/service-protos.pb
```

**POSITIONAL ARGUMENTS**

: **`SERVICE_CONFIG_FILE` [`SERVICE_CONFIG_FILE` …]**:
The service configuration file (or files) containing the API specification to
upload. Proto Descriptors, Open API (Swagger) specifications, and Google Service
Configuration files in JSON and YAML formats are acceptable.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--force**:
Force the deployment even if any hazardous changes to the service configuration
are detected.

**--validate-only**:
If included, the command validates the service configuration(s), but does not
deploy them. The service must exist in order to validate the configuration(s).

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
gcloud alpha endpoints services deploy
```

```
gcloud beta endpoints services deploy
```