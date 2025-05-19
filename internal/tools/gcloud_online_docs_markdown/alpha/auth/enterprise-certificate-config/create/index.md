# gcloud alpha auth enterprise-certificate-config create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/auth/enterprise-certificate-config/create](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/enterprise-certificate-config/create)*

**NAME**

: **gcloud alpha auth enterprise-certificate-config create - create enterprise certificate configurations**

**SYNOPSIS**

: **`gcloud alpha auth enterprise-certificate-config create` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/enterprise-certificate-config/create#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/enterprise-certificate-config/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` The gcloud alpha auth enterprise-certificate-config create
group lets you create enterprise certificate configurations. This configuration
will be used by gcloud to communicate with the enterprise-certificate-proxy.
See more details at `[gcloud topic
client-certificate](https://cloud.google.com/sdk/gcloud/reference/topic/client-certificate)`.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[linux](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/enterprise-certificate-config/create/linux)`**:
`(ALPHA)` Create an enterprise-certificate configuration file for
Linux.

**`[macos](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/enterprise-certificate-config/create/macos)`**:
`(ALPHA)` Create an enterprise-certificate configuration file for
MacOS.

**`[windows](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/enterprise-certificate-config/create/windows)`**:
`(ALPHA)` Create an enterprise-certificate configuration file for
Windows.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud auth enterprise-certificate-config create
```

```
gcloud beta auth enterprise-certificate-config create
```