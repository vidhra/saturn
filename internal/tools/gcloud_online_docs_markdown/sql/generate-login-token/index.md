# gcloud sql generate-login-token  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/generate-login-token](https://cloud.google.com/sdk/gcloud/reference/sql/generate-login-token)*

**NAME**

: **gcloud sql generate-login-token - generate an IAM login token for Cloud SQL**

**SYNOPSIS**

: **`gcloud sql generate-login-token` [`[--application-default-credential](https://cloud.google.com/sdk/gcloud/reference/sql/generate-login-token#--application-default-credential)`] [`[--instance](https://cloud.google.com/sdk/gcloud/reference/sql/generate-login-token#--instance)`=`INSTANCE`, `[-i](https://cloud.google.com/sdk/gcloud/reference/sql/generate-login-token#-i)` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/generate-login-token#INSTANCE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/generate-login-token#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud sql generate-login-token generates an IAM token to use for logging in to
Cloud SQL instances.

**EXAMPLES**

: To generate an IAM login token using gcloud credentials, run:

```
gcloud sql generate-login-token
```

To generate an IAM login token using application default credentials, run:

```
gcloud sql generate-login-token --application-default-credential
```

To generate an IAM login token using gcloud credentials for instance
`my-instance`, run:

```
gcloud sql generate-login-token --instance=my-instance
```

To generate an IAM login token using application default credentials for
instance `my-instance`, run:

```
gcloud sql generate-login-token --instance=my-instance --application-default-credential
```

**FLAGS**

: **--application-default-credential**:
Use application default credentials to generate the login token.

**--instance**:
Cloud SQL instance ID.

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
gcloud alpha sql generate-login-token
```

```
gcloud beta sql generate-login-token
```