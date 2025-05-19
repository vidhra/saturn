# gcloud access-approval settings get  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/access-approval/settings/get](https://cloud.google.com/sdk/gcloud/reference/access-approval/settings/get)*

**NAME**

: **gcloud access-approval settings get - get Access Approval settings**

**SYNOPSIS**

: **`gcloud access-approval settings get` [`[--folder](https://cloud.google.com/sdk/gcloud/reference/access-approval/settings/get#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/access-approval/settings/get#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/access-approval/settings/get#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/access-approval/settings/get#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get the Access Approval settings associated with a project, a folder, or
organization.

**EXAMPLES**

: To get the settings for the current project use

```
gcloud access-approval settings get
```

To get the settings for folder f1 use

```
gcloud access-approval settings get --folder=f1
```

**FLAGS**

: **--folder**

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
gcloud alpha access-approval settings get
```

```
gcloud beta access-approval settings get
```