# gcloud alpha compute backend-services  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services)*

**NAME**

: **gcloud alpha compute backend-services - list, create, and delete backend services**

**SYNOPSIS**

: **`gcloud alpha compute backend-services` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` List, create, and delete backend services.
For more information about backend services, see the [backend
services documentation](https://cloud.google.com/load-balancing/docs/backend-service).
See also: [Global
backend services API](https://cloud.google.com/compute/docs/reference/rest/v1/backendServices) and [Regional
backend services API](https://cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-backend](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/add-backend)`**:
`(ALPHA)` Add a backend to a backend service.

**`[add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/add-iam-policy-binding)`**:
`(ALPHA)` Add an IAM policy binding to a Compute Engine backend
service.

**`[add-service-bindings](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/add-service-bindings)`**:
`(ALPHA)` Add service bindings to a backend service.

**`[add-signed-url-key](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/add-signed-url-key)`**:
`(ALPHA)` Add Cloud CDN Signed URL key to a backend service.

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/create)`**:
`(ALPHA)` Create a backend service.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/delete)`**:
`(ALPHA)` Delete backend services.

**`[delete-signed-url-key](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/delete-signed-url-key)`**:
`(ALPHA)` Delete Cloud CDN Signed URL key from a backend service.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/describe)`**:
`(ALPHA)` Display detailed information about a backend service.

**`[edit](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/edit)`**:
`(ALPHA)` Modify a backend service.

**`[export](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/export)`**:
`(ALPHA)` Export a backend service.

**`[get-effective-security-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/get-effective-security-policies)`**:
`(ALPHA)` Get the effective security policies of a Compute Engine
backend service.

**`[get-health](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/get-health)`**:
`(ALPHA)` Get backend health statuses from a backend service.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/get-iam-policy)`**:
`(ALPHA)` Get the IAM policy for a Compute Engine backend service.

**`[import](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/import)`**:
`(ALPHA)` Import a backend service.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/list)`**:
`(ALPHA)` List Google Compute Engine backend services.

**`[list-usable](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/list-usable)`**:
`(ALPHA)` List usable backend services.

**`[remove-backend](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/remove-backend)`**:
`(ALPHA)` Remove a backend from a backend service.

**`[remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/remove-iam-policy-binding)`**:
`(ALPHA)` Remove an IAM policy binding from a Compute Engine backend
service.

**`[remove-service-bindings](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/remove-service-bindings)`**:
`(ALPHA)` Remove service bindings from a backend service.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/set-iam-policy)`**:
`(ALPHA)` Set the IAM policy binding for a Compute Engine backend
service.

**`[set-security-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/set-security-policy)`**:
`(ALPHA)` `(DEPRECATED)` Set the security policy for a
backend service.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update)`**:
`(ALPHA)` Update a backend service.

**`[update-backend](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend)`**:
`(ALPHA)` Update an existing backend in a backend service.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute backend-services
```

```
gcloud beta compute backend-services
```