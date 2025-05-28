# gcloud alpha compute health-checks  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks)*

**NAME**

: **gcloud alpha compute health-checks - read and manipulate health checks for load balanced instances**

**SYNOPSIS**

: **`gcloud alpha compute health-checks` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Read and manipulate health checks for load balanced
instances.
For more information about health checks, see the [health
checks documentation](https://cloud.google.com/load-balancing/docs/health-check-concepts).
See also: [Health
checks API](https://cloud.google.com/compute/docs/reference/rest/v1/healthChecks) and [Regional
health checks API](https://cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create)`**:
`(ALPHA)` Create (non-legacy) health checks for load balanced
instances.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/update)`**:
`(ALPHA)` Update health checks for load balanced instances.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/delete)`**:
`(ALPHA)` Delete health checks.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/describe)`**:
`(ALPHA)` Display detailed information about a health check.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/list)`**:
`(ALPHA)` List Google Compute Engine health checks.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute health-checks
```

```
gcloud beta compute health-checks
```