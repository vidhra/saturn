# gcloud alpha auth enterprise-certificate-config  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/auth/enterprise-certificate-config](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/enterprise-certificate-config)*

**NAME**

: **gcloud alpha auth enterprise-certificate-config - manage enterprise certificate configurations**

**SYNOPSIS**

: **`gcloud alpha auth enterprise-certificate-config` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/enterprise-certificate-config#GROUP)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/enterprise-certificate-config#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Currently only create is implemented.
The gcloud alpha auth enterprise-certificate-config group lets you create
enterprise certificate configurations. This configuration will be used by gcloud
to communicate with the enterprise-certificate-proxy.
See more details at `[gcloud topic
client-certificate](https://cloud.google.com/sdk/gcloud/reference/topic/client-certificate)`.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/auth/enterprise-certificate-config/create)`**:
`(ALPHA)` Create enterprise certificate configurations.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud auth enterprise-certificate-config
```

```
gcloud beta auth enterprise-certificate-config
```