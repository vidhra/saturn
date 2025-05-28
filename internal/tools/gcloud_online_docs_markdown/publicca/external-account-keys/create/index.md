# gcloud publicca external-account-keys create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/publicca/external-account-keys/create](https://cloud.google.com/sdk/gcloud/reference/publicca/external-account-keys/create)*

**NAME**

: **gcloud publicca external-account-keys create - create a new external account key**

**SYNOPSIS**

: **`gcloud publicca external-account-keys create` [`[--key-output-file](https://cloud.google.com/sdk/gcloud/reference/publicca/external-account-keys/create#--key-output-file)`=`KEY_OUTPUT_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/publicca/external-account-keys/create#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create an external account key:

```
gcloud publicca external-account-keys create
```

To create an external account key and save it to a file:

```
gcloud publicca external-account-keys create --key-output-file=./external_account_key.txt
```

**FLAGS**

: **--key-output-file**:
The path where the generated external account key is written.

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
gcloud alpha publicca external-account-keys create
```

```
gcloud beta publicca external-account-keys create
```