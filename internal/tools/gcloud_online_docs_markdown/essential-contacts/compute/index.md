# gcloud essential-contacts compute  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/essential-contacts/compute](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/compute)*

**NAME**

: **gcloud essential-contacts compute - compute the essential contacts that are subscribed to the specified notification categories for a resource**

**SYNOPSIS**

: **`gcloud essential-contacts compute` `[--notification-categories](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/compute#--notification-categories)`=[`NOTIFICATION_CATEGORIES`,…] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/compute#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/compute#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/compute#--project)`=`PROJECT`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/compute#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/compute#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/compute#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/compute#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/essential-contacts/compute#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command will return the contacts subscribed to any of the notification
categories that have been set on the requested resource or any of its ancestors.

**EXAMPLES**

: To compute contacts subscribed to the technical category for the current
project, run:

```
gcloud essential-contacts compute --notification-categories=technical
```

To compute contacts subscribed to the product-updates or billing categories for
the folder with id ``123``, run:

```
gcloud essential-contacts compute --notification-categories=product-updates,billing --folder=123
```

To compute contacts subscribed to the legal category for the organization with
id ``456``, run:

```
gcloud essential-contacts compute --notification-categories=legal --organization=456
```

**REQUIRED FLAGS**

: **--notification-categories**:
list of notification categories contact is subscribed to.
`NOTIFICATION_CATEGORIES` must be one of:
`all`, `billing`, `legal`,
`notification-category-unspecified`, `product-updates`,
`security`, `suspension`, `technical`,
`technical-incidents`.

**FLAGS**

: **--folder**

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates `True`, then that item is
listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--limit**:
Maximum number of resources to list. The default is `unlimited`. This
flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--page-size**:
Some services group resource list output into pages. This flag specifies the
maximum number of resources per page. The default is determined by the service
if it supports paging, otherwise it is `unlimited` (no paging).
Paging may be applied before or after `--filter` and
`--limit` depending on the service.

**--sort-by**:
Comma-separated list of resource field key names to sort by. The default order
is ascending. Prefix a field with ``~´´ for descending order on that
field. This flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

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
gcloud alpha essential-contacts compute
```

```
gcloud beta essential-contacts compute
```