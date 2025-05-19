# gcloud alpha auth revoke  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/auth/revoke](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/revoke)*

**NAME**

: **gcloud alpha auth revoke - revoke access credentials for an account**

**SYNOPSIS**

: **`gcloud alpha auth revoke` [`[ACCOUNTS](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/revoke#ACCOUNTS)` …] [`[--all](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/revoke#--all)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/revoke#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Revokes credentials for the specified user accounts,
service accounts or external accounts (workload identity pools).
When given a user account, this command revokes the user account token on the
server. If the revocation is successful, or if the token has already been
revoked, this command removes the credential from the local machine.
When given a service account, this command does not revoke the service account
token on the server because service account tokens are not revocable. Instead,
it will print a warning and remove the credential from the local machine. When
used with a service account, this command has only a local effect and the key
associated with the service account is not deleted. This can be done by
executing `[gcloud iam
service-accounts keys delete](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/delete)` after `revoke`.
When given an external account (workload identity pool), whether impersonated or
not, the command does not revoke the corresponding token on the server because
these tokens are not revocable. The underlying external credentials (OIDC, AWS,
etc.) used to generate these access tokens have to be revoked too, but gcloud
has no control over that. Instead, it will print a warning and remove the
credential from the local machine.
If no account is specified, this command revokes credentials for the currently
active account, effectively logging out of that account. If --all is given, the
behaviors described above apply individually to each account in the list.
You can revoke credentials when you want to prevent gcloud and other Google
Cloud CLI tools from using the specified account. You do not need to revoke
credentials to switch between accounts.

**POSITIONAL ARGUMENTS**

: **[`ACCOUNTS` …]**:
Accounts whose credentials are to be revoked.

**FLAGS**

: **--all**:
Revoke credentials for all accounts.

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
gcloud auth revoke
```

```
gcloud beta auth revoke
```