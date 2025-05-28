# gcloud storage hmac delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/hmac/delete](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/delete)*

**NAME**

: **gcloud storage hmac delete - remove a service account HMAC**

**SYNOPSIS**

: **`gcloud storage hmac delete` `[ACCESS_ID](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/delete#ACCESS_ID)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud storage hmac delete` permanently deletes the specified HMAC
key. Note that keys must be updated to be in the
``INACTIVE`` state before they can be deleted.

**EXAMPLES**

: To delete a specific HMAC key:

```
gcloud storage hmac delete GOOG56JBMFZX6PMPTQ62VD2
```

To be prompted for HMAC keys to delete:

```
gcloud storage hmac delete
```

**POSITIONAL ARGUMENTS**

: **`ACCESS_ID`**:
Access ID for HMAC key to delete.

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
gcloud alpha storage hmac delete
```