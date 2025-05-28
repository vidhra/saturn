# gcloud compute http-health-checks  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/http-health-checks](https://cloud.google.com/sdk/gcloud/reference/compute/http-health-checks)*

**NAME**

: **gcloud compute http-health-checks - read and manipulate HTTP health checks for load balanced instances**

**SYNOPSIS**

: **`gcloud compute http-health-checks` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/http-health-checks#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/http-health-checks#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Read and manipulate legacy health checks that use the HTTP protocol.
For more information about legacy health checks, see the [HTTP
health checks documentation](https://cloud.google.com/load-balancing/docs/health-checks#legacy-health-checks).
See also: [HTTP
health checks API](https://cloud.google.com/compute/docs/reference/rest/v1/httpHealthChecks).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/compute/http-health-checks/create)`**:
Create a legacy HTTP health check.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/compute/http-health-checks/delete)`**:
Delete HTTP health checks.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/http-health-checks/describe)`**:
Display detailed information about an HTTP health check.

**`[list](https://cloud.google.com/sdk/gcloud/reference/compute/http-health-checks/list)`**:
List Google Compute Engine health checks.

**`[update](https://cloud.google.com/sdk/gcloud/reference/compute/http-health-checks/update)`**:
Update a legacy HTTP health check.

**NOTES**

: These variants are also available:

```
gcloud alpha compute http-health-checks
```

```
gcloud beta compute http-health-checks
```