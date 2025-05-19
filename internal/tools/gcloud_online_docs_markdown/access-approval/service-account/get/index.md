# gcloud access-approval service-account get  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/access-approval/service-account/get](https://cloud.google.com/sdk/gcloud/reference/access-approval/service-account/get)*

**NAME**

: **gcloud access-approval service-account get - get Access Approval service account**

**SYNOPSIS**

: **`gcloud access-approval service-account get` [`[--folder](https://cloud.google.com/sdk/gcloud/reference/access-approval/service-account/get#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/access-approval/service-account/get#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/access-approval/service-account/get#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/access-approval/service-account/get#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Retrieves the service account that is used by Access Approval to access KMS keys
for signing approved approval requests.

**EXAMPLES**

: To get the service account for the current project use

```
gcloud access-approval service-account get
```

To get the service account for folder f1 use

```
gcloud access-approval service-account get --folder=f1
```

To get the service account for organization org1 use

```
gcloud access-approval service-account get --organization=org1
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