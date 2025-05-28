# gcloud iap oauth-brands create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iap/oauth-brands/create](https://cloud.google.com/sdk/gcloud/reference/iap/oauth-brands/create)*

**NAME**

: **gcloud iap oauth-brands create - create a Cloud OAuth brand for the project**

**SYNOPSIS**

: **`gcloud iap oauth-brands create` `--application_title`=`APPLICATION_TITLE` `--support_email`=`SUPPORT_EMAIL` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iap/oauth-brands/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud iap oauth-brands create` is used to create a Cloud OAuth
brand for the project. The brand is 'internal only', meaning OAuth clients
created under it only accept requests from users who belong to the same G Suite
account as the project. The brand is created in unreviewed status. Your domain
will not appear on the OAuth consent screen until it is reviewed after you
manually start a review process in Google Cloud Platform Console. Note that the
'internal only' setting can be manually changed in Google Cloud Platform Console
(https://console.cloud.google.com/apis/credentials/consent). A project can only
have one brand.

**EXAMPLES**

: To create a Cloud OAuth brand for the current project, run:

```
gcloud iap oauth-brands create --application_title=APPLICATION_TITLE --support_email=SUPPORT_EMAIL
```

To create a Cloud OAuth brand for the project PROJECT_ID, run:

```
gcloud iap oauth-brands create --application_title=APPLICATION_TITLE --support_email=SUPPORT_EMAIL --project=PROJECT_ID
```

**REQUIRED FLAGS**

: **--application_title**:
Application name displayed on the OAuth consent screen.

**--support_email**:
Support email displayed on the OAuth consent screen.

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

**API REFERENCE**

: This command uses the `iap/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/iap](https://cloud.google.com/iap)

**NOTES**

: These variants are also available:

```
gcloud alpha iap oauth-brands create
```

```
gcloud beta iap oauth-brands create
```