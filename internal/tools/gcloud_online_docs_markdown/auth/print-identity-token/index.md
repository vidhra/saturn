# gcloud auth print-identity-token  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/auth/print-identity-token](https://cloud.google.com/sdk/gcloud/reference/auth/print-identity-token)*

**NAME**

: **gcloud auth print-identity-token - print an identity token for the specified account**

**SYNOPSIS**

: **`gcloud auth print-identity-token` [`[ACCOUNT](https://cloud.google.com/sdk/gcloud/reference/auth/print-identity-token#ACCOUNT)`] [`[--audiences](https://cloud.google.com/sdk/gcloud/reference/auth/print-identity-token#--audiences)`=`AUDIENCES`] [`[--include-email](https://cloud.google.com/sdk/gcloud/reference/auth/print-identity-token#--include-email)`] [`[--include-license](https://cloud.google.com/sdk/gcloud/reference/auth/print-identity-token#--include-license)` `[--token-format](https://cloud.google.com/sdk/gcloud/reference/auth/print-identity-token#--token-format)`=`TOKEN_FORMAT`; default="standard"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/auth/print-identity-token#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Print an identity token for the specified account.

**EXAMPLES**

: To print identity tokens:

```
gcloud auth print-identity-token
```

To print identity token for account 'foo@example.com' whose audience is
'https://service-hash-uc.a.run.app', run:

```
gcloud auth print-identity-token foo@example.com --audiences="https://service-hash-uc.a.run.app"
```

To print identity token for an impersonated service account
'my-account@example.iam.gserviceaccount.com' whose audience is
'https://service-hash-uc.a.run.app', run:

```
gcloud auth print-identity-token --impersonate-service-account="my-account@example.iam.gserviceaccount.com" --audiences="https://service-hash-uc.a.run.app"
```

To print identity token of a Compute Engine instance, which includes project and
instance details as well as license codes for images associated with the
instance, run:

```
gcloud auth print-identity-token --token-format=full --include-license
```

To print identity token for an impersonated service account
'my-account@example.iam.gserviceaccount.com', which includes the email address
of the service account, run:

```
gcloud auth print-identity-token --impersonate-service-account="my-account@example.iam.gserviceaccount.com" --include-email
```

**POSITIONAL ARGUMENTS**

: **[`ACCOUNT`]**:
Account to print the identity token for. If not specified, the current active
account will be used.

**FLAGS**

: **--audiences**:
Intended recipient of the token. Currently, only one audience can be specified.

**--include-email**:
Specify whether or not service account email is included in the identity token.
If specified, the token will contain 'email' and 'email_verified' claims. This
flag should only be used for impersonate service account.

**--include-license**

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
gcloud alpha auth print-identity-token
```

```
gcloud beta auth print-identity-token
```