# gcloud storage hmac update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/hmac/update](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/update)*

**NAME**

: **gcloud storage hmac update - change the status of a service account HMAC**

**SYNOPSIS**

: **`gcloud storage hmac update` `[ACCESS_ID](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/update#ACCESS_ID)` (`[--activate](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/update#--activate)`     | `[--deactivate](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/update#--deactivate)`) [`[--etag](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/update#--etag)`=`ETAG`, `[-e](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/update#-e)` `[ETAG](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/update#ETAG)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud storage hmac update` sets the state of the specified key.
Valid state arguments are ``ACTIVE`` and
``INACTIVE``. To set a key to state
``DELETED``, use `[gcloud storage hmac
delete](https://cloud.google.com/sdk/gcloud/reference/storage/hmac/delete)` on an ``INACTIVE`` key. If an
etag is set in the command, it will only succeed if the provided etag matches
the etag of the stored key.

**EXAMPLES**

: To activate an HMAC key:

```
gcloud storage hmac update GOOG56JBMFZX6PMPTQ62VD2 --activate
```

To set the state of an HMAC key to ``INACTIVE``
provided its etag is ``M42da=``:

```
gcloud storage hmac update GOOG56JBMFZX6PMPTQ62VD2 --deactivate --etag=M42da=
```

**POSITIONAL ARGUMENTS**

: **`ACCESS_ID`**:
Access ID for HMAC key to update.

**REQUIRED FLAGS**

: **--activate**

**OPTIONAL FLAGS**

: **--etag**:
If provided, the update will only be performed if the specified etag matches the
etag of the stored key.

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
gcloud alpha storage hmac update
```