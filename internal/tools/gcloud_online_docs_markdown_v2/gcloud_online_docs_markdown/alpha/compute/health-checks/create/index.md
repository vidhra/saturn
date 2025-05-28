# gcloud alpha compute health-checks create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create)*

**NAME**

: **gcloud alpha compute health-checks create - create (non-legacy) health checks for load balanced instances**

**SYNOPSIS**

: **`gcloud alpha compute health-checks create` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create (non-legacy) health checks for load balanced
instances.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[grpc](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/grpc)`**:
`(ALPHA)` Create a gRPC health check to monitor load balanced
instances.

**`[http](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/http)`**:
`(ALPHA)` Create a HTTP health check to monitor load balanced
instances.

**`[http2](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/http2)`**:
`(ALPHA)` Create a HTTP2 health check to monitor load balanced
instances.

**`[https](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/https)`**:
`(ALPHA)` Create a HTTPS health check to monitor load balanced
instances.

**`[ssl](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/ssl)`**:
`(ALPHA)` Create a SSL health check to monitor load balanced
instances.

**`[tcp](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/health-checks/create/tcp)`**:
`(ALPHA)` Create a TCP health check to monitor load balanced
instances.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute health-checks create
```

```
gcloud beta compute health-checks create
```