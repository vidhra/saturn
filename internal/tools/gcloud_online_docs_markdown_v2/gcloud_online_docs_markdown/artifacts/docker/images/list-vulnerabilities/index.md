# gcloud artifacts docker images list-vulnerabilities  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/list-vulnerabilities](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/list-vulnerabilities)*

**NAME**

: **gcloud artifacts docker images list-vulnerabilities - list On-Demand Scanning vulnerabilities**

**SYNOPSIS**

: **`gcloud artifacts docker images list-vulnerabilities` (`[SCAN](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/list-vulnerabilities#SCAN)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/list-vulnerabilities#--location)`=`LOCATION`) [`[--limit](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/list-vulnerabilities#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/list-vulnerabilities#--page-size)`=`PAGE_SIZE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/list-vulnerabilities#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List On-Demand Scanning vulnerabilities from a completed scan.

**EXAMPLES**

: The following command lists vulnerabilities from a completed On-Demand Scanning
scan.

```
gcloud artifacts docker images list-vulnerabilities projects/my-project/locations/europe/scans/fff66882-0z55-4333-l619-z1z00df6040c
```

**POSITIONAL ARGUMENTS**

: **Scan resource - The scan resource to list vulnerabilites for. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `scan` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SCAN`**:
ID of the scan or fully qualified identifier for the scan.
To set the `scan` attribute:

- provide the argument `scan` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Cloud multi-region.
To set the `location` attribute:

- provide the argument `scan` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**LIST COMMAND FLAGS**

: **--limit**:
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

: This command uses the `ondemandscanning/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/container-analysis/docs/on-demand-scanning/](https://cloud.google.com/container-analysis/docs/on-demand-scanning/)

**NOTES**

: This variant is also available:

```
gcloud beta artifacts docker images list-vulnerabilities
```