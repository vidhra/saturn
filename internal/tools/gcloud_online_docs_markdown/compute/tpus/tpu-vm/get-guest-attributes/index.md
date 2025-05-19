# gcloud compute tpus tpu-vm get-guest-attributes  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/get-guest-attributes](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/get-guest-attributes)*

**NAME**

: **gcloud compute tpus tpu-vm get-guest-attributes - retrieve the Guest Attributes for a Cloud TPU VM**

**SYNOPSIS**

: **`gcloud compute tpus tpu-vm get-guest-attributes` (`[TPU](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/get-guest-attributes#TPU)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/get-guest-attributes#--zone)`=`ZONE`) [`[--query-path](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/get-guest-attributes#--query-path)`=`QUERY_PATH`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/get-guest-attributes#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/get-guest-attributes#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/get-guest-attributes#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/get-guest-attributes#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/get-guest-attributes#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Retrieve the Guest Attributes for a Cloud TPU VM.

**EXAMPLES**

: To retrieve the guest attributes, run:

```
gcloud compute tpus tpu-vm get-guest-attributes my-tpu --zone=us-central1-b
```

To select only a specific query path, use the --query-path flag:

```
gcloud compute tpus tpu-vm get-guest-attributes my-tpu --zone=us-central1-b --query-path=lifecycle/event
```

To only display the guest attributes for one of the workers in a TPU pod, use
the --filter flag:

```
gcloud compute tpus tpu-vm get-guest-attributes my-tpu --zone=us-central1-b --filter="worker_id:3"
```

where 3 is an example of the worker ID (0-indexed).

**POSITIONAL ARGUMENTS**

: **Tpu resource - Name of the Cloud TPU VM. The arguments in this group can be used
to specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `tpu` on the command line with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TPU`**:
ID of the tpu or fully qualified identifier for the tpu.
To set the `tpu` attribute:

- provide the argument `tpu` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--zone**:
Zone of the Cloud TPU.
If not specified, will use `default` compute/zone.
To set the `zone` attribute:

- provide the argument `tpu` on the command line with a fully specified
name;
- provide the argument `--zone` on the command line;
- set the property `compute/zone`.**

**FLAGS**

: **--query-path**:
Attribute path to query. Can be empty string or of the form
`<namespace>/` or `<namespace>/<key>`.
Default is the empty string.

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

**API REFERENCE**

: This command uses the `tpu/v2` API. The full documentation for this
API can be found at: [https://cloud.google.com/tpu/](https://cloud.google.com/tpu/)

**NOTES**

: This variant is also available:

```
gcloud alpha compute tpus tpu-vm get-guest-attributes
```