# gcloud compute routers  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/routers](https://cloud.google.com/sdk/gcloud/reference/compute/routers)*

**NAME**

: **gcloud compute routers - list, create, and delete Compute Engine routers**

**SYNOPSIS**

: **`gcloud compute routers` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/compute/routers#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/routers#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/routers#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List, create, and delete Cloud Routers.
For more information about Cloud Routers, see the [Cloud
Router documentation](https://cloud.google.com//network-connectivity/docs/router/concepts/overview).
See also: [Routers
API](https://cloud.google.com/compute/docs/reference/rest/v1/routers).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[nats](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats)`**:
List, create, describe, and delete Cloud NAT.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-bgp-peer](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer)`**:
Add a BGP peer to a Compute Engine router.

**`[add-interface](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-interface)`**:
Add an interface to a Compute Engine router.

**`[add-route-policy](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-route-policy)`**:
Add an empty route policy to a Compute Engine router.

**`[add-route-policy-term](https://cloud.google.com/sdk/gcloud/reference/compute/routers/add-route-policy-term)`**:
Adds a new term to an existing route policy of a Comute Engine router.

**`[create](https://cloud.google.com/sdk/gcloud/reference/compute/routers/create)`**:
Create a Compute Engine router.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/compute/routers/delete)`**:
Delete Compute Engine routers.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/routers/describe)`**:
Describe a Compute Engine router.

**`[download-route-policy](https://cloud.google.com/sdk/gcloud/reference/compute/routers/download-route-policy)`**:
Download a route policy from a Compute Engine router.

**`[get-nat-ip-info](https://cloud.google.com/sdk/gcloud/reference/compute/routers/get-nat-ip-info)`**:
Display NAT IP information in a router.

**`[get-nat-mapping-info](https://cloud.google.com/sdk/gcloud/reference/compute/routers/get-nat-mapping-info)`**:
Display NAT Mapping information in a router.

**`[get-route-policy](https://cloud.google.com/sdk/gcloud/reference/compute/routers/get-route-policy)`**:
Get a route policy from a Compute Engine router.

**`[get-status](https://cloud.google.com/sdk/gcloud/reference/compute/routers/get-status)`**:
Get status of a Compute Engine router.

**`[list](https://cloud.google.com/sdk/gcloud/reference/compute/routers/list)`**:
List Google Compute Engine routers.

**`[list-bgp-routes](https://cloud.google.com/sdk/gcloud/reference/compute/routers/list-bgp-routes)`**:
List routes advertised and learned on individual BGP sessions, both pre- and
post-policy evaluation.

**`[list-route-policies](https://cloud.google.com/sdk/gcloud/reference/compute/routers/list-route-policies)`**:
List route policies from a Compute Engine router.

**`[remove-bgp-peer](https://cloud.google.com/sdk/gcloud/reference/compute/routers/remove-bgp-peer)`**:
Remove a BGP peer from a Compute Engine router.

**`[remove-interface](https://cloud.google.com/sdk/gcloud/reference/compute/routers/remove-interface)`**:
Remove an interface from a Compute Engine router.

**`[remove-route-policy](https://cloud.google.com/sdk/gcloud/reference/compute/routers/remove-route-policy)`**:
Remove a route policy from a Compute Engine router.

**`[remove-route-policy-term](https://cloud.google.com/sdk/gcloud/reference/compute/routers/remove-route-policy-term)`**:
Remove a route policy term of a Compute Engine router.

**`[update](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update)`**:
Update a Compute Engine router.

**`[update-bgp-peer](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-bgp-peer)`**:
Update a BGP peer on a Compute Engine router.

**`[update-interface](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-interface)`**:
Update an interface on a Compute Engine router.

**`[update-route-policy-term](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-route-policy-term)`**:
Updates a term of an existing route policy of a Comute Engine router.

**`[upload-route-policy](https://cloud.google.com/sdk/gcloud/reference/compute/routers/upload-route-policy)`**:
Upload a route policy into a Compute Engine router.

**NOTES**

: These variants are also available:

```
gcloud alpha compute routers
```

```
gcloud beta compute routers
```