# gcloud privateca certificates list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/list](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/list)*

**NAME**

: **gcloud privateca certificates list - list certificates within a project**

**SYNOPSIS**

: **`gcloud privateca certificates list` [`[--issuer-pool](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/list#--issuer-pool)`=`ISSUER_POOL` `[--location](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/list#--location)`=`LOCATION`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/list#--page-size)`=`PAGE_SIZE`; default=100] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/privateca/certificates/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List certificates within a project. Note that listing certificates accross
locations is not supported.

**EXAMPLES**

: To list all Certificates issued by a given CA pool, run:

```
gcloud privateca certificates list --issuer-pool=my-pool --location=us-west1
```

To list all Certificates issued by all CA pools in a location, run:

```
gcloud privateca certificates list --location=us-west1
```

To list all Certificates issued directly under a CA, run:

```
gcloud privateca certificates list --issuer-pool=my-pool --location=us-west1 --filter="issuer_certificate_authority='projects/1234567890/locations/us-west1/caPools/my-pool/certificateAuthorities/my-ca'"
```

You can omit the `--location` flag in both of the above examples if
you've already set the ``privateca/location``
property. For example:

```
gcloud config set privateca/location us-west1
```

```
# The following is equivalent to the first example above.
gcloud privateca certificates list --issuer-pool=my-pool
```

```
# The following is equivalent to the second example above.
gcloud privateca certificates list
```

**FLAGS**

: **CA POOL resource - The issuing CA pool. If this is omitted, Certificates issued
by all CA pools in the given location will be listed. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--issuer-pool` on the command line with a fully
specified name;
- defaults to all CA pools in the given location with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--issuer-pool**:
ID of the CA_POOL or fully qualified identifier for the CA_POOL.
To set the `pool` attribute:

- provide the argument `--issuer-pool` on the command line;
- defaults to all CA pools in the given location.

**--location**:
The location of the CA_POOL.
To set the `location` attribute:

- provide the argument `--issuer-pool` on the command line with a fully
specified name;
- defaults to all CA pools in the given location with a fully specified name;
- provide the argument `--location` on the command line;
- set the property `privateca/location`.**

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