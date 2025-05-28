# gcloud app logs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/logs](https://cloud.google.com/sdk/gcloud/reference/app/logs)*

**NAME**

: **gcloud app logs - manage your App Engine logs**

**SYNOPSIS**

: **`gcloud app logs` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/app/logs#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/logs#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This set of commands can be used to view your existing App Engine logs.

**EXAMPLES**

: To read the logs for the current App Engine project, run:

```
gcloud app logs read
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[read](https://cloud.google.com/sdk/gcloud/reference/app/logs/read)`**:
Reads log entries for the current App Engine app.

**`[tail](https://cloud.google.com/sdk/gcloud/reference/app/logs/tail)`**:
Streams logs for App Engine apps.

**NOTES**

: This variant is also available:

```
gcloud beta app logs
```