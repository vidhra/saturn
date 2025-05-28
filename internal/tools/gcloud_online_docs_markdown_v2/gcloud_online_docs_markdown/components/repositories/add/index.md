# gcloud components repositories add  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/components/repositories/add](https://cloud.google.com/sdk/gcloud/reference/components/repositories/add)*

**NAME**

: **gcloud components repositories add - add a new Trusted Tester component repository**

**SYNOPSIS**

: **`gcloud components repositories add` `[URL](https://cloud.google.com/sdk/gcloud/reference/components/repositories/add#URL)` [`[URL](https://cloud.google.com/sdk/gcloud/reference/components/repositories/add#URL)` …] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/components/repositories/add#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Add a new Trusted Tester component repository to the list of repositories used
by the component manager. This will allow you to install and update components
found in this repository.
If you are participating in a Trusted Tester program, you will be instructed on
the location of repositories with additional versions of one or more Google
Cloud CLI components.

**EXAMPLES**

: To add the Trusted Tester component repository [http://repo.location.com](http://repo.location.com) run:

```
gcloud components repositories add http://repo.location.com
```

**POSITIONAL ARGUMENTS**

: **`URL` [`URL` …]**:
One or more URLs for the component repositories you want to add.

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