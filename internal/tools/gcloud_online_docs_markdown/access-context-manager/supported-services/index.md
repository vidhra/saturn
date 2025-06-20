# gcloud access-context-manager supported-services  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/access-context-manager/supported-services](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/supported-services)*

**NAME**

: **gcloud access-context-manager supported-services - retrieve VPC Service Controls Supported Services**

**SYNOPSIS**

: **`gcloud access-context-manager supported-services` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/supported-services#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/supported-services#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud access-context-manager supported-services command group lets you list
VPC Service Controls supported services and its properties.

**EXAMPLES**

: To see all VPC Service Controls supported services:

```
gcloud access-context-manager supported-services list
```

To see support information about VPC Service Controls supported services:

```
gcloud access-context-manager supported-services describe SERVICE_NAME
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/supported-services/describe)`**:
Gets information about a VPC Service Controls Supported Service.

**`[list](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/supported-services/list)`**:
Lists all VPC Service Controls supported services.

**NOTES**

: These variants are also available:

```
gcloud alpha access-context-manager supported-services
```

```
gcloud beta access-context-manager supported-services
```