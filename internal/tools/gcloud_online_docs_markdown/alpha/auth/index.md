# gcloud alpha auth  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/auth](https://cloud.google.com/sdk/gcloud/reference/alpha/auth)*

**NAME**

: **gcloud alpha auth - manage oauth2 credentials for the Google Cloud CLI**

**SYNOPSIS**

: **`gcloud alpha auth` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/auth#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/auth#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/auth#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` The `[gcloud
auth](https://cloud.google.com/sdk/gcloud/reference/auth)` command group lets you grant and revoke authorization to Google
Cloud CLI (`[gcloud](https://cloud.google.com/sdk/gcloud/reference)` CLI) to
access Google Cloud. Typically, when scripting Google Cloud CLI tools for use on
multiple machines, using `[gcloud auth
activate-service-account](https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account)` is recommended.
For information about authorization and credential types, see [Authorizing the gcloud
CLI](https://cloud.google.com/sdk/docs/authorizing). For information about authorizing a service account, see [Authorizing
with a service account](https://cloud.google.com/sdk/docs/authorizing#service-account).
After running `[gcloud auth](https://cloud.google.com/sdk/gcloud/reference/auth)`
commands, you can run other commands with
`--account`=``ACCOUNT`` to
authenticate the command with the credentials of the specified account. For
information about `--account` and other `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` CLI global flags, see the [gcloud CLI overview](https://cloud.google.com/sdk/gcloud/reference).
See `$ [gcloud
topic client-certificate](https://cloud.google.com/sdk/gcloud/reference/topic/client-certificate)` to learn how to use Mutual TLS when using
gcloud. Mutual TLS can be used for [certificate
based access](https://cloud.google.com/beyondcorp-enterprise/docs/securing-resources-with-certificate-based-access) with gcloud.

**EXAMPLES**

: To authenticate a user account with `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` and minimal user output, run:

```
gcloud auth login --brief
```

To list all credentialed accounts and identify the current active account, run:

```
gcloud auth list
```

To revoke credentials for a user account (like logging out), run:

```
gcloud auth revoke test@gmail.com
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[application-default](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/application-default)`**:
`(ALPHA)` Manage your active Application Default Credentials.

**`[enterprise-certificate-config](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/enterprise-certificate-config)`**:
`(ALPHA)` Manage enterprise certificate configurations.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[activate-service-account](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/activate-service-account)`**:
`(ALPHA)` Authorize access to Google Cloud with a service account.

**`[configure-docker](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/configure-docker)`**:
`(ALPHA)` Register `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` as a Docker credential helper.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/list)`**:
`(ALPHA)` Lists credentialed accounts.

**`[login](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/login)`**:
`(ALPHA)` Authorize gcloud to access the Cloud Platform with Google
user credentials.

**`[print-access-token](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/print-access-token)`**:
`(ALPHA)` Print an access token for the specified account.

**`[print-identity-token](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/print-identity-token)`**:
`(ALPHA)` Print an identity token for the specified account.

**`[revoke](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/revoke)`**:
`(ALPHA)` Revoke access credentials for an account.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud auth
```

```
gcloud beta auth
```