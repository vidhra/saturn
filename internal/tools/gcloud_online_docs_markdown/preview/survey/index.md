# gcloud preview survey  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/preview/survey](https://cloud.google.com/sdk/gcloud/reference/preview/survey)*

**NAME**

: **gcloud preview survey - invoke a customer satisfaction survey for Google Cloud CLI**

**SYNOPSIS**

: **`gcloud preview survey` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/preview/survey#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(PREVIEW)` To permanently disable the survey prompt, run:

```
gcloud config set survey/disable_prompts True
```

**EXAMPLES**

: To launch the survey, run:

```
gcloud preview survey
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

: This command is currently in DEVELOPER PREVIEW and may change without notice. If
this command fails with API permission errors despite specifying the correct
project, you might be trying to access an API with an invitation-only early
access allowlist. These variants are also available:

```
gcloud survey
```

```
gcloud alpha survey
```

```
gcloud beta survey
```