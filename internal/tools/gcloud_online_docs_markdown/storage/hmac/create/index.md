# gcloud storage hmac create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/hmac/create](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/create)*

**NAME**

: **gcloud storage hmac create - add a service account HMAC**

**SYNOPSIS**

: **`gcloud storage hmac create` `[SERVICE_ACCOUNT](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/create#SERVICE_ACCOUNT)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud storage hmac create` command creates an HMAC key for the
specified service account. The secret key material is only available upon
creation, so be sure to store the returned secret along with the access_id.

**EXAMPLES**

: To create an HMAC key for
``test.service.account@test_project.iam.gserviceaccount.com``:

```
gcloud storage hmac create test.service.account@test_project.iam.gserviceaccount.com
```

**POSITIONAL ARGUMENTS**

: **`SERVICE_ACCOUNT`**:
The service account email.

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
gcloud alpha storage hmac create
```