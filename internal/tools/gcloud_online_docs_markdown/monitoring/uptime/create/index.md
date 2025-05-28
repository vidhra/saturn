# gcloud monitoring uptime create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create)*

**NAME**

: **gcloud monitoring uptime create - create a new uptime check or synthetic monitor**

**SYNOPSIS**

: **`gcloud monitoring uptime create` `[DISPLAY_NAME](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#DISPLAY_NAME)` (`[--synthetic-target](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--synthetic-target)`=`SYNTHETIC_TARGET`     | [`[--group-id](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--group-id)`=`GROUP_ID` : `[--group-type](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--group-type)`=`GROUP_TYPE`]     | [`[--resource-labels](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--resource-labels)`=[`KEY`=`VALUE`,…] : `[--resource-type](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--resource-type)`=`RESOURCE_TYPE`]) [`[--body](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--body)`=`BODY` `[--content-type](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--content-type)`=`CONTENT_TYPE` `[--custom-content-type](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--custom-content-type)`=`CUSTOM_CONTENT_TYPE` `[--headers](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--headers)`=[`KEY`=`VALUE`,…] `[--mask-headers](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--mask-headers)`=`MASK_HEADERS` `[--password](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--password)`=`PASSWORD` `[--path](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--path)`=`PATH` `[--pings-count](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--pings-count)`=`PINGS_COUNT` `[--port](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--port)`=`PORT` `[--protocol](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--protocol)`=`PROTOCOL` `[--request-method](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--request-method)`=`REQUEST_METHOD` `[--service-agent-auth](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--service-agent-auth)`=`SERVICE_AGENT_AUTH` `[--username](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--username)`=`USERNAME` `[--validate-ssl](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--validate-ssl)`=`VALIDATE_SSL` `[--status-classes](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--status-classes)`=[`status-class`,…]     | `[--status-codes](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--status-codes)`=[`status-code`,…]] [`[--matcher-content](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--matcher-content)`=`MATCHER_CONTENT` : `[--matcher-type](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--matcher-type)`=`MATCHER_TYPE` [`[--json-path](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--json-path)`=`JSON_PATH` : `[--json-path-matcher-type](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--json-path-matcher-type)`=`JSON_PATH_MATCHER_TYPE`]] [`[--period](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--period)`=`PERIOD` `[--regions](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--regions)`=[`field`,…] `[--timeout](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--timeout)`=`TIMEOUT` `[--user-labels](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#--user-labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new uptime check or synthetic monitor.
Flags only apply to uptime checks unless noted that they apply to synthetic
monitors.
For information about the JSON/YAML format of an uptime check: [https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs)

**EXAMPLES**

: To create an uptime check against a URL, run:

```
gcloud monitoring uptime create DISPLAY_NAME --resource-type=uptime-url --resource-labels=host=google.com,project_id=PROJECT_ID
```

To create a synthetic monitor, run:

```
gcloud monitoring uptime create SYNTHETIC_MONITOR_NAME --synthetic-target=projects/PROJECT_ID/locations/REGION/functions/FUNCTION_NAME
```

**POSITIONAL ARGUMENTS**

: **`DISPLAY_NAME`**:
Display name for the uptime check or synthetic monitor.

**REQUIRED FLAGS**

: **--synthetic-target**

**OPTIONAL FLAGS**

: **--body**

**--matcher-content**

**--period**

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
gcloud alpha monitoring uptime create
```

```
gcloud beta monitoring uptime create
```