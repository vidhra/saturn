# gcloud monitoring dashboards create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/monitoring/dashboards/create](https://cloud.google.com/sdk/gcloud/reference/monitoring/dashboards/create)*

**NAME**

: **gcloud monitoring dashboards create - create a new Cloud Monitoring dashboard**

**SYNOPSIS**

: **`gcloud monitoring dashboards create` (`[--config](https://cloud.google.com/sdk/gcloud/reference/monitoring/dashboards/create#--config)`=`CONFIG`     | `[--config-from-file](https://cloud.google.com/sdk/gcloud/reference/monitoring/dashboards/create#--config-from-file)`=`PATH_TO_FILE`) [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/monitoring/dashboards/create#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/monitoring/dashboards/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Monitoring dashboard. A dashboard can be specified as a JSON/YAML
value passed in as a string through the `--config` flag or as a file
through the `--config-from-file` flag. Validate a dashboard config
without saving by setting the `--validate-only` flag.
For information about the format of a dashboard: [https://cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards](https://cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards)

**EXAMPLES**

: To create a dashboard with a YAML config, run:

```
gcloud monitoring dashboards create --config='''
  displayName: New Dashboard
  gridLayout:
    widgets:
    - text:
        content: Hello World
  '''
```

To validate a dashboard and not save it, run:

```
gcloud monitoring dashboards create --validate-only --config='''
  displayName: New Dashboard
  gridLayout:
    widgets:
    - text:
        content: Hello World
  '''
```

To create a dashboard with a JSON config, run:

```
gcloud monitoring dashboards create --config='''
  {
    "displayName": "New Dashboard",
    "gridLayout": {
      "widgets": [
        {
          "text": {
            "content": "Hello World",
          }
        }
      ]
    },
  }
  '''
```

To create a dashboard with a specific dashboard ID, run:

```
gcloud monitoring dashboards create --config='''
  name: projects/MY-PROJECT/dashboards/MY-DASHBOARD
  displayName: New Dashboard
  gridLayout:
    widgets:
    - text:
        content: Hello World
  '''
```

To create a dashboard within a specific project, run:

```
gcloud monitoring dashboards create --project=MY-PROJECT --config='''
  displayName: New Dashboard
  gridLayout:
    widgets:
    - text:
        content: Hello World
  '''
```

To create a dashboard with a file, run:

```
gcloud monitoring dashboards create --config-from-file=MY-FILE
```

Sample contents of MY-FILE:

```
displayName: New Dashboard
gridLayout:
  widgets:
  - text:
      content: Hello World
```

**REQUIRED FLAGS**

: **--config**

**OPTIONAL FLAGS**

: **--validate-only**:
When set, validate the dashboard but do not save it.

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

**API REFERENCE**

: This command uses the `monitoring/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/monitoring/api/](https://cloud.google.com/monitoring/api/)

**NOTES**

: These variants are also available:

```
gcloud alpha monitoring dashboards create
```

```
gcloud beta monitoring dashboards create
```