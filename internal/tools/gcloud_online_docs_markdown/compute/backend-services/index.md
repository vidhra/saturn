# gcloud compute backend-services  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/backend-services](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services)*

**NAME**

: **gcloud compute backend-services - list, create, and delete backend services**

**SYNOPSIS**

: **`gcloud compute backend-services` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List, create, and delete backend services.
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

**`[add-backend](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend)`**:
Add a backend to a backend service.

**`[add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-iam-policy-binding)`**:
Add an IAM policy binding to a Compute Engine backend service.

**`[add-service-bindings](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-service-bindings)`**:
Add service bindings to a backend service.

**`[add-signed-url-key](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-signed-url-key)`**:
Add Cloud CDN Signed URL key to a backend service.

**`[create](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/create)`**:
Create a backend service.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/delete)`**:
Delete backend services.

**`[delete-signed-url-key](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/delete-signed-url-key)`**:
Delete Cloud CDN Signed URL key from a backend service.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/describe)`**:
Display detailed information about a backend service.

**`[edit](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/edit)`**:
Modify a backend service.

**`[export](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/export)`**:
Export a backend service.

**`[get-health](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/get-health)`**:
Get backend health statuses from a backend service.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/get-iam-policy)`**:
Get the IAM policy for a Compute Engine backend service.

**`[import](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/import)`**:
Import a backend service.

**`[list](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/list)`**:
List Google Compute Engine backend services.

**`[list-usable](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/list-usable)`**:
List usable backend services.

**`[remove-backend](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/remove-backend)`**:
Remove a backend from a backend service.

**`[remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/remove-iam-policy-binding)`**:
Remove an IAM policy binding from a Compute Engine backend service.

**`[remove-service-bindings](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/remove-service-bindings)`**:
Remove service bindings from a backend service.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/set-iam-policy)`**:
Set the IAM policy binding for a Compute Engine backend service.

**`[update](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update)`**:
Update a backend service.

**`[update-backend](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/update-backend)`**:
Update an existing backend of a load balancer or Traffic Director.

**NOTES**

: These variants are also available:

```
gcloud alpha compute backend-services
```

```
gcloud beta compute backend-services
```