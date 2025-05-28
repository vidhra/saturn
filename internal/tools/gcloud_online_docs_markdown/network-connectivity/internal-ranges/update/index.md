# gcloud network-connectivity internal-ranges update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/update](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/update)*

**NAME**

: **gcloud network-connectivity internal-ranges update - update an internal range**

**SYNOPSIS**

: **`gcloud network-connectivity internal-ranges update` (`[INTERNAL_RANGE](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/update#INTERNAL_RANGE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/update#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/update#--description)`=`DESCRIPTION`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/update#--clear-labels)`     | `[--labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/update#--labels)`=[`KEY`=`VALUE`,…]] [`[--clear-overlaps](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/update#--clear-overlaps)`     | `[--overlaps](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/update#--overlaps)`=[`OVERLAPS`,…]] [`[--ip-cidr-range](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/update#--ip-cidr-range)`=`IP_CIDR_RANGE`     | `[--prefix-length](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/update#--prefix-length)`=`PREFIX_LENGTH`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the details of an internal range.

**EXAMPLES**

: Update ip-cidr-range of an internal range named
``my-range``:

```
gcloud network-connectivity internal-ranges update my-range --ip-cidr-range="192.168.0.0/24"
```

Extend an internal range named ``my-range`` to
an address block of /24:

```
gcloud network-connectivity internal-ranges update my-range --prefix-length=24
```

**POSITIONAL ARGUMENTS**

: **Internal range resource - Name of the internal range to be created. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `internal_range` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INTERNAL_RANGE`**:
ID of the internal range or fully qualified identifier for the internal range.
To set the `internal_range` attribute:

- provide the argument `internal_range` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The location ID.
To set the `region` attribute:

- provide the argument `internal_range` on the command line with a
fully specified name;
- provide the argument `--region` on the command line;
- use default global location .**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Description of the Internal Range

**--clear-labels**

**--clear-overlaps**

**--ip-cidr-range**

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

: This command uses the `networkconnectivity/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest](https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest)

**NOTES**

: This variant is also available:

```
gcloud alpha network-connectivity internal-ranges update
```