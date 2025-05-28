# gcloud alpha access-context-manager supported-services  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/supported-services](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/supported-services)*

**NAME**

: **gcloud alpha access-context-manager supported-services - retrieve VPC Service Controls Supported Services**

**SYNOPSIS**

: **`gcloud alpha access-context-manager supported-services` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/supported-services#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/supported-services#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` The gcloud alpha access-context-manager supported-services
command group lets you list VPC Service Controls supported services and its
properties.

**EXAMPLES**

: To see all VPC Service Controls supported services:

```
gcloud alpha access-context-manager supported-services list
```

To see support information about VPC Service Controls supported services:

```
gcloud alpha access-context-manager supported-services describe SERVICE_NAME
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/supported-services/describe)`**:
`(ALPHA)` Gets information about a VPC Service Controls Supported
Service.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/supported-services/list)`**:
`(ALPHA)` Lists all VPC Service Controls supported services.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud access-context-manager supported-services
```

```
gcloud beta access-context-manager supported-services
```