# gcloud transfer authorize  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/transfer/authorize](https://cloud.google.com/sdk/gcloud/reference/transfer/authorize)*

**NAME**

: **gcloud transfer authorize - authorize an account for all Transfer Service features**

**SYNOPSIS**

: **`gcloud transfer authorize` [`[--add-missing](https://cloud.google.com/sdk/gcloud/reference/transfer/authorize#--add-missing)`] [`[--creds-file](https://cloud.google.com/sdk/gcloud/reference/transfer/authorize#--creds-file)`=`CREDS_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/transfer/authorize#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Authorize a Google account for all Transfer Service features.
This command provides admin and owner rights for simplicity. If that's too much
authority for your use case, see custom setups here: [https://cloud.google.com/storage-transfer/docs/on-prem-set-up](https://cloud.google.com/storage-transfer/docs/on-prem-set-up)

**EXAMPLES**

: To see what Transfer Service IAM roles the account logged into gcloud may be
missing, run:

```
gcloud transfer authorize
```

To add the missing IAM roles, run:

```
gcloud transfer authorize --add-missing
```

To check a custom service account for missing roles, run:

```
gcloud transfer authorize --creds-file=path/to/service-account-key.json
```

**FLAGS**

: **--add-missing**:
Add IAM roles necessary to use all Transfer Service features to the specified
account. By default, this command just prints missing roles.

**--creds-file**:
The path to the creds file for an account to authorize. The file should be in
JSON format and contain a "type" and "client_email", which are automatically
generated for most creds files downloaded from Google (e.g. service account
tokens). If this flag is not present, the command authorizes the user currently
logged into gcloud.

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
gcloud alpha transfer authorize
```