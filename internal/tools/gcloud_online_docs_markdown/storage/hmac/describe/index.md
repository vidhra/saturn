# gcloud storage hmac describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/hmac/describe](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/describe)*

**NAME**

: **gcloud storage hmac describe - describes a service account HMAC key**

**SYNOPSIS**

: **`gcloud storage hmac describe` `[ACCESS_ID](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/describe#ACCESS_ID)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud storage hmac describe` retrieves the specified HMAC key's
metadata. Note that there is no option to retrieve a key's secret material after
it has been created.

**EXAMPLES**

: The following command retrieves the HMAC key's metadata:

```
gcloud storage hmac describe GOOG56JBMFZX6PMPTQ62VD2
```

Note `GOOG56JBMFZX6PMPTQ62VD2` is the `ACCESS_ID` of the
HMAC key.

**POSITIONAL ARGUMENTS**

: **`ACCESS_ID`**:
The [Access
ID](https://cloud.google.com/storage/docs/authentication/hmackeys#overview) of the HMAC key

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
gcloud alpha storage hmac describe
```