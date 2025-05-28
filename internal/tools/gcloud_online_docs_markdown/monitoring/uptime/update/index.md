# gcloud monitoring uptime update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update)*

**NAME**

: **gcloud monitoring uptime update - update an existing uptime check or synthetic monitor**

**SYNOPSIS**

: **`gcloud monitoring uptime update` `[CHECK_ID](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#CHECK_ID)` [`[--body](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--body)`=`BODY` `[--content-type](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--content-type)`=`CONTENT_TYPE` `[--custom-content-type](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--custom-content-type)`=`CUSTOM_CONTENT_TYPE` `[--mask-headers](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--mask-headers)`=`MASK_HEADERS` `[--password](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--password)`=`PASSWORD` `[--path](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--path)`=`PATH` `[--pings-count](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--pings-count)`=`PINGS_COUNT` `[--port](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--port)`=`PORT` `[--request-method](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--request-method)`=`REQUEST_METHOD` `[--service-agent-auth](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--service-agent-auth)`=`SERVICE_AGENT_AUTH` `[--username](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--username)`=`USERNAME` `[--validate-ssl](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--validate-ssl)`=`VALIDATE_SSL` `[--add-status-classes](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--add-status-classes)`=[`status-class`,…]     | `[--clear-status-classes](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--clear-status-classes)`=`CLEAR_STATUS_CLASSES`     | `[--remove-status-classes](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--remove-status-classes)`=[`status-class`,…]     | `[--set-status-classes](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--set-status-classes)`=[`status-class`,…]     | `[--add-status-codes](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--add-status-codes)`=[`status-code`,…]     | `[--clear-status-codes](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--clear-status-codes)`=`CLEAR_STATUS_CODES`     | `[--remove-status-codes](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--remove-status-codes)`=[`status-code`,…]     | `[--set-status-codes](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--set-status-codes)`=[`status-code`,…] `[--update-headers](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--update-headers)`=[`KEY`=`VALUE`,…] `[--clear-headers](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--clear-headers)`=`CLEAR_HEADERS`     | `[--remove-headers](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--remove-headers)`=[`KEY`,…]] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--display-name)`=`DISPLAY_NAME` `[--period](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--period)`=`PERIOD` `[--timeout](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--timeout)`=`TIMEOUT` `[--add-regions](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--add-regions)`=[`region`,…]     | `[--clear-regions](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--clear-regions)`=`CLEAR_REGIONS`     | `[--remove-regions](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--remove-regions)`=[`region`,…]     | `[--set-regions](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--set-regions)`=[`region`,…] `[--update-user-labels](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--update-user-labels)`=[`KEY`=`VALUE`,…] `[--clear-user-labels](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--clear-user-labels)`     | `[--remove-user-labels](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--remove-user-labels)`=[`KEY`,…]] [`[--matcher-content](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--matcher-content)`=`MATCHER_CONTENT` : `[--matcher-type](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--matcher-type)`=`MATCHER_TYPE` [`[--json-path](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--json-path)`=`JSON_PATH` : `[--json-path-matcher-type](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#--json-path-matcher-type)`=`JSON_PATH_MATCHER_TYPE`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates an existing uptime check or synthetic monitor.
Flags only apply to uptime checks unless noted that they apply to synthetic
monitors.
For information about the JSON/YAML format of an uptime check: [https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs)

**EXAMPLES**

: To update an uptime check or synthetic monitor, run:

```
gcloud monitoring uptime update CHECK_ID --period=5 --timeout=30
```

**POSITIONAL ARGUMENTS**

: **Uptime check or synthetic monitor resource - Name of the uptime check or
synthetic monitor to be updated. This represents a Cloud resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `check_id` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CHECK_ID`**:
ID of the uptime check or synthetic monitor or fully qualified identifier for
the uptime check or synthetic monitor.
To set the `check_id` attribute:

- provide the argument `check_id` on the command line.**

**FLAGS**

: **--body**

**--display-name**

**--matcher-content**

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
gcloud alpha monitoring uptime update
```

```
gcloud beta monitoring uptime update
```