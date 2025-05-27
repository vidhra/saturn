# gcloud container hub fleetobservability update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/fleetobservability/update](https://cloud.google.com/sdk/gcloud/reference/container/hub/fleetobservability/update)*

**NAME**

: **gcloud container hub fleetobservability update - updates the Fleet Observability Feature resource**

**SYNOPSIS**

: **`gcloud container hub fleetobservability update` [`[--logging-config](https://cloud.google.com/sdk/gcloud/reference/container/hub/fleetobservability/update#--logging-config)`=`LOGGING_CONFIG`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/fleetobservability/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command updates the Fleet Observability Feature in a fleet.

**EXAMPLES**

: To describe the Fleet Observability Feature, run:

```
gcloud container hub fleetobservability update --logging-config=LOGGING-CONFIG
```

**FLAGS**

: **--logging-config**:
Path of the YAML(or JSON) file that contains the logging configurations.
The JSON file is formatted as follows, with camelCase field naming:

```
{
    "loggingConfig": {
        "defaultConfig": {
            "mode": "COPY"
        },
        "fleetScopeLogsConfig": {
            "mode": "MOVE"
        }
    }
}
```

The YAML file is formatted as follows, with camelCase field naming:

```
---
loggingConfig:
  defaultConfig:
    mode: COPY
  fleetScopeLogsConfig:
    mode: MOVE
```

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
gcloud alpha container hub fleetobservability update
```

```
gcloud beta container hub fleetobservability update
```