# gcloud app logs tail  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/logs/tail](https://cloud.google.com/sdk/gcloud/reference/app/logs/tail)*

**NAME**

: **gcloud app logs tail - streams logs for App Engine apps**

**SYNOPSIS**

: **`gcloud app logs tail` [`[--level](https://cloud.google.com/sdk/gcloud/reference/app/logs/tail#--level)`=`LEVEL`; default="any"] [`[--logs](https://cloud.google.com/sdk/gcloud/reference/app/logs/tail#--logs)`=`APP_LOG`,[`[APP_LOG](https://cloud.google.com/sdk/gcloud/reference/app/logs/tail#APP_LOG)`,…]; default=`"stderr,`stdout,crash.log,nginx.request,request_log"] [`[--service](https://cloud.google.com/sdk/gcloud/reference/app/logs/tail#--service)`=`SERVICE`, `[-s](https://cloud.google.com/sdk/gcloud/reference/app/logs/tail#-s)` `[SERVICE](https://cloud.google.com/sdk/gcloud/reference/app/logs/tail#SERVICE)`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/app/logs/tail#--version)`=`VERSION`, `[-v](https://cloud.google.com/sdk/gcloud/reference/app/logs/tail#-v)` `[VERSION](https://cloud.google.com/sdk/gcloud/reference/app/logs/tail#VERSION)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/logs/tail#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Streams logs for App Engine apps.

**EXAMPLES**

: To stream logs from a serving app, run:

```
gcloud app logs tail
```

To show only logs with a specific service, version, and level, run:

```
gcloud app logs tail --service=s1 --version=v1 --level=warning
```

To show only the logs from the request log for Standard apps, run:

```
gcloud app logs tail --logs=request_log
```

To show only the logs from the request log for Flex apps, run:

```
gcloud app logs tail --logs=nginx.request
```

**FLAGS**

: **--level**:
Filter entries with severity equal to or higher than a given level.
`LEVEL` must be one of: `critical`,
`error`, `warning`, `info`, `debug`,
`any`.

**--logs**:
Filter entries from a particular set of logs. Must be a comma-separated list of
log names (request_log, stdout, stderr, etc).

**--service**:
Limit to specific service.

**--version**:
Limit to specific version.

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

: This variant is also available:

```
gcloud beta app logs tail
```