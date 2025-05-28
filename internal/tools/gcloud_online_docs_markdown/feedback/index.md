# gcloud feedback  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/feedback](https://cloud.google.com/sdk/gcloud/reference/feedback)*

**NAME**

: **gcloud feedback - provide feedback to the Google Cloud CLI team**

**SYNOPSIS**

: **`gcloud feedback` [`[--log-file](https://cloud.google.com/sdk/gcloud/reference/feedback#--log-file)`=`LOG_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/feedback#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The Google Cloud CLI team offers support through a number of channels:

- Google Cloud CLI Issue Tracker
- Stack Overflow "#gcloud" tag
- google-cloud-dev Google group

This command lists the available channels and facilitates getting help through
one of them by opening a web browser to the relevant page, possibly with
information relevant to the current install and configuration pre-populated in
form fields on that page.

**EXAMPLES**

: To send feedback, including the log file for the most recent command, run:

```
gcloud feedback
```

To send feedback with a previously generated log file named 'my-logfile', run:

```
gcloud feedback --log-file=my-logfile
```

**FLAGS**

: **--log-file**:
Path to the log file from a prior gcloud run.

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