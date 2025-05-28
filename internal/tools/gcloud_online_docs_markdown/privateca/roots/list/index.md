# gcloud privateca roots list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/privateca/roots/list](https://cloud.google.com/sdk/gcloud/reference/privateca/roots/list)*

**NAME**

: **gcloud privateca roots list - list root certificate authorities**

**SYNOPSIS**

: **`gcloud privateca roots list` [`[--location](https://cloud.google.com/sdk/gcloud/reference/privateca/roots/list#--location)`=`LOCATION`] [`[--pool](https://cloud.google.com/sdk/gcloud/reference/privateca/roots/list#--pool)`=`POOL`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/privateca/roots/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/privateca/roots/list#--page-size)`=`PAGE_SIZE`; default=100] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/privateca/roots/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/privateca/roots/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/privateca/roots/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List the root certificate authorities within a project.

**EXAMPLES**

: To list all root certificate authorities in a projects:

```
gcloud privateca roots list
```

To list all root certificate authorities within a project and location
'us-central1':

```
gcloud privateca roots list --location=us-central1
```

To list all root certificate authorities within a CA Pool in location
'us-central1':

```
gcloud privateca roots list --pool=my-pool --location=us-central1
```

**FLAGS**

: **--location**:
Location of the certificate authorities. If ommitted, root CAs across all
regions will be listed.

**--pool**:
ID of the CA Pool where the certificate authorities reside. If ommitted, root
CAs across all CA pools will be listed.

**LIST COMMAND FLAGS**

: **--limit**:
Maximum number of resources to list. The default is `unlimited`. This
flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--page-size**:
Some services group resource list output into pages. This flag specifies the
maximum number of resources per page. The default is `100`. Paging
may be applied before or after `--filter` and `--limit`
depending on the service.

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