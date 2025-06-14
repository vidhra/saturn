# gcloud monitoring dashboards update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/monitoring/dashboards/update](https://cloud.google.com/sdk/gcloud/reference/monitoring/dashboards/update)*

**NAME**

: **gcloud monitoring dashboards update - update a Cloud Monitoring dashboard**

**SYNOPSIS**

: **`gcloud monitoring dashboards update` `[DASHBOARD](https://cloud.google.com/sdk/gcloud/reference/monitoring/dashboards/update#DASHBOARD)` (`[--config](https://cloud.google.com/sdk/gcloud/reference/monitoring/dashboards/update#--config)`=`CONFIG`     | `[--config-from-file](https://cloud.google.com/sdk/gcloud/reference/monitoring/dashboards/update#--config-from-file)`=`PATH_TO_FILE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/monitoring/dashboards/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Monitoring dashboard. The updated dashboard can be specified as a
JSON/YAML value passed in as a string through the `--config` flag or
as a file through the `--config-from-file` flag.
Note: Etags are used to prevent concurrent updates to the same dashboard. The
latest etag can be found in a `describe` or `list`
response.
For information about the format of a dashboard: [https://cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards](https://cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards)

**EXAMPLES**

: To update a dashboard with a YAML config, run:

```
gcloud monitoring dashboards update MY-DASHBOARD --config='''
  displayName: New Dashboard with New Display Name
  etag: 40d1040034db4e5a9dee931ec1b12c0d
  gridLayout:
    widgets:
    - text:
        content: Hello World
  '''
```

To update a dashboard with a JSON config, run:

```
gcloud monitoring dashboards update MY-DASHBOARD --config='''
  {
    "displayName": "New Dashboard with New Display Name",
    "etag": "40d1040034db4e5a9dee931ec1b12c0d",
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

To update a dashboard within a specific project, run:

```
gcloud monitoring dashboards update MY-DASHBOARD --project=MY-PROJECT --config='''
  displayName: New Dashboard with New Display Name
  etag: 40d1040034db4e5a9dee931ec1b12c0d
  gridLayout:
    widgets:
    - text:
        content: Hello World
  '''
```

To update a dashboard with a file, run:

```
gcloud monitoring dashboards update MY-DASHBOARD --config-from-file=MY-FILE
```

Sample contents of MY-FILE:

```
displayName: New Dashboard with new Display Name
etag: 40d1040034db4e5a9dee931ec1b12c0d
gridLayout:
  widgets:
  - text:
      content: Hello World
```

**POSITIONAL ARGUMENTS**

: **Dashboard resource - The dashboard to update. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `dashboard` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DASHBOARD`**:
ID of the dashboard or fully qualified identifier for the dashboard.
To set the `dashboard` attribute:

- provide the argument `dashboard` on the command line.**

**REQUIRED FLAGS**

: **--config**

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
gcloud alpha monitoring dashboards update
```

```
gcloud beta monitoring dashboards update
```