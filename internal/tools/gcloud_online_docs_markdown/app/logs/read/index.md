# gcloud app logs read  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/logs/read](https://cloud.google.com/sdk/gcloud/reference/app/logs/read)*

**NAME**

: **gcloud app logs read - reads log entries for the current App Engine app**

**SYNOPSIS**

: **`gcloud app logs read` [`[--level](https://cloud.google.com/sdk/gcloud/reference/app/logs/read#--level)`=`LEVEL`; default="any"] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/app/logs/read#--limit)`=`LIMIT`; default=200] [`[--logs](https://cloud.google.com/sdk/gcloud/reference/app/logs/read#--logs)`=`APP_LOG`,[`[APP_LOG](https://cloud.google.com/sdk/gcloud/reference/app/logs/read#APP_LOG)`,…]; default=`"stderr,`stdout,crash.log,nginx.request,request_log"] [`[--service](https://cloud.google.com/sdk/gcloud/reference/app/logs/read#--service)`=`SERVICE`, `[-s](https://cloud.google.com/sdk/gcloud/reference/app/logs/read#-s)` `[SERVICE](https://cloud.google.com/sdk/gcloud/reference/app/logs/read#SERVICE)`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/app/logs/read#--version)`=`VERSION`, `[-v](https://cloud.google.com/sdk/gcloud/reference/app/logs/read#-v)` `[VERSION](https://cloud.google.com/sdk/gcloud/reference/app/logs/read#VERSION)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/logs/read#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Display the latest log entries from stdout, stderr and crash log for the current
Google App Engine app in a human readable format. This command requires that the
caller have the logging.logEntries.list permission.

**EXAMPLES**

: To display the latest entries for the current app, run:

```
gcloud app logs read
```

To show only the entries with severity at `warning` or higher, run:

```
gcloud app logs read --level=warning
```

To show only the entries with a specific version, run:

```
gcloud app logs read --version=v1
```

To show only the 10 latest log entries for the default service, run:

```
gcloud app logs read --limit=10 --service=default
```

To show only the logs from the request log for standard apps, run:

```
gcloud app logs read --logs=request_log
```

To show only the logs from the request log for Flex apps, run:

```
gcloud app logs read --logs=nginx.request
```

**FLAGS**

: **--level**:
Filter entries with severity equal to or higher than a given level.
`LEVEL` must be one of: `critical`,
`error`, `warning`, `info`, `debug`,
`any`.

**--limit**:
Number of log entries to show.

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
gcloud beta app logs read
```