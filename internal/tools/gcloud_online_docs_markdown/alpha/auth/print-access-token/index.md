# gcloud alpha auth print-access-token  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/auth/print-access-token](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/print-access-token)*

**NAME**

: **gcloud alpha auth print-access-token - print an access token for the specified account**

**SYNOPSIS**

: **`gcloud alpha auth print-access-token` [`[ACCOUNT](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/print-access-token#ACCOUNT)`] [`[--lifetime](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/print-access-token#--lifetime)`=`LIFETIME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/print-access-token#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Print an access token for the specified account. See [RFC6749](https://tools.ietf.org/html/rfc6749) for more information
about access tokens.
Note that token itself may not be enough to access some services. If you use the
token with curl or similar tools, you may see permission errors similar to "API
has not been used in project 32555940559 before or it is disabled.". If it
happens, you may need to provide a quota project in the "X-Goog-User-Project"
header. For example,

```
curl -H "X-Goog-User-Project: your-project" -H "Authorization: Bearer $(gcloud auth print-access-token)" foo.googleapis.com
```

The identity that granted the token must have the serviceusage.services.use
permission on the provided project. See [https://cloud.google.com/apis/docs/system-parameters](https://cloud.google.com/apis/docs/system-parameters)
for more information.

**EXAMPLES**

: To print access tokens:

```
gcloud alpha auth print-access-token
```

**POSITIONAL ARGUMENTS**

: **[`ACCOUNT`]**:
Account to get the access token for. If not specified, the current active
account will be used.

**FLAGS**

: **--lifetime**:
Access token lifetime. The default access token lifetime is 3600 seconds, but
you can use this flag to reduce the lifetime or extend it up to 43200 seconds
(12 hours). The org policy constraint
`constraints/iam.allowServiceAccountCredentialLifetimeExtension` must
be set if you want to extend the lifetime beyond 3600 seconds. Note that this
flag is for service account impersonation only, so it must be used together with
the `--impersonate-service-account` flag.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud auth print-access-token
```

```
gcloud beta auth print-access-token
```