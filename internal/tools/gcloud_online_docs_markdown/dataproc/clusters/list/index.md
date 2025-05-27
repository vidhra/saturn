# gcloud dataproc clusters list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/list](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/list)*

**NAME**

: **gcloud dataproc clusters list - view a list of clusters in a project**

**SYNOPSIS**

: **`gcloud dataproc clusters list` [`[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/list#--region)`=`REGION`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/list#--page-size)`=`PAGE_SIZE`; default=100] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/clusters/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: View a list of clusters in a project. An optional filter can be used to
constrain the clusters returned. Filters are case-sensitive and have the
following syntax:

```
field = value [AND [field = value]] …
```

where `field` is one of `status.state`,
`clusterName`, or `labels.[KEY]`, and `[KEY]`
is a label key. `value` can be `*` to match all values.
`status.state` can be one of the following: `ACTIVE`,
`INACTIVE`, `CREATING`, `RUNNING`,
`ERROR`, `DELETING`, or `UPDATING`.
`ACTIVE` contains the `CREATING`, `UPDATING`,
and `RUNNING` states. `INACTIVE` contains the
`DELETING` and `ERROR` states. `clusterName` is
the name of the cluster provided at creation time. Only the logical
`AND` operator is supported; space-separated items are treated as
having an implicit `AND` operator.

**EXAMPLES**

: To see the list of all clusters in Dataproc's 'us-central1' region, run:

```
gcloud dataproc clusters list --region='us-central1'
```

To show a cluster in Dataproc's 'global' region with the name 'mycluster', run:

```
gcloud dataproc clusters list --region='global' --filter='clusterName = mycluster'
```

To see the list of all clusters in Dataproc's 'global' region with specified
labels, run:

```
gcloud dataproc clusters list --region='global' --filter='labels.env = staging AND
  labels.starred = *'
```

To see a list of all active clusters in Dataproc's 'europe-west1' region with
specified labels, run:

```
gcloud dataproc clusters list --region='europe-west1' --filter='status.state = ACTIVE AND
  labels.env = staging AND labels.starred = *'
```

**FLAGS**

: **--region**:
Dataproc region to use. Each Dataproc region constitutes an independent resource
namespace constrained to deploying instances into Compute Engine zones inside
the region. Overrides the default `dataproc/region` property value
for this command invocation.

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
gcloud alpha dataproc clusters list
```

```
gcloud beta dataproc clusters list
```