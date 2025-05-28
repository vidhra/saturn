# gcloud alpha apigee applications list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/list](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/list)*

**NAME**

: **gcloud alpha apigee applications list - list Apigee applications**

**SYNOPSIS**

: **`gcloud alpha apigee applications list` [`[--developer](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/list#--developer)`=`DEVELOPER` `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/list#--organization)`=`ORGANIZATION`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` List Apigee applications.

**EXAMPLES**

: To list all Apigee applications in the active Cloud Platform project, run:

```
gcloud alpha apigee applications list
```

To list all Apigee applications belonging to the developer
``horse@example.com`` in an Apigee organization
called ``my-org``, formatted as JSON, run:

```
gcloud alpha apigee applications list --developer=horse@example.com --organization=my-org --format=json
```

**FLAGS**

: **Developer resource - Apigee organization, and optionally developer, whose
applications should be listed. If developer is not specified, all developers
will be listed.
To get a list of valid developers, run:

```
gcloud alpha apigee developers list
```

```
The arguments in this group can be used to specify the attributes of this resource.
```

**--developer**:
ID of the developer or fully qualified identifier for the developer.
To set the `developer` attribute:

- provide the argument `--developer` on the command line;
- leave the argument unspecified for it to be chosen automatically.

**--organization**:
Apigee organization containing the developer. If unspecified, the Cloud Platform
project's associated organization will be used.
To set the `organization` attribute:

- provide the argument `--developer` on the command line with a fully
specified name;
- leave the argument unspecified for it to be chosen automatically with a fully
specified name;
- provide the argument `--organization` on the command line;
- set the property [project] or provide the argument [--project] on the command
line, using a Cloud Platform project with an associated Apigee organization.**

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

**--uri**:
Print a list of resource URIs instead of the default output, and change the
command output to a list of URIs. If this flag is used with
`--format`, the formatting is applied on this URI list. To display
URIs alongside other keys instead, use the `uri()` transform.

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
gcloud apigee applications list
```

```
gcloud beta apigee applications list
```