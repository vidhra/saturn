# gcloud compute https-health-checks  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks](https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks)*

**NAME**

: **gcloud compute https-health-checks - read and manipulate HTTPS health checks for load balanced instances**

**SYNOPSIS**

: **`gcloud compute https-health-checks` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Read and manipulate legacy health checks that use the HTTPS protocol.
For more information about legacy health checks, see the [HTTPS
health checks documentation](https://cloud.google.com/load-balancing/docs/health-checks#legacy-health-checks)
See also: [HTTPS
health checks API](https://cloud.google.com/compute/docs/reference/rest/v1/httpsHealthChecks).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/create)`**:
Create a legacy HTTPS health check.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/delete)`**:
Delete HTTPS health checks.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/describe)`**:
Display detailed information about an HTTPS health check.

**`[list](https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/list)`**:
List Google Compute Engine HTTPS health checks.

**`[update](https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks/update)`**:
Update a legacy HTTPS health check.

**NOTES**

: These variants are also available:

```
gcloud alpha compute https-health-checks
```

```
gcloud beta compute https-health-checks
```