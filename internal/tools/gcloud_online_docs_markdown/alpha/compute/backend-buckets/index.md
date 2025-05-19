# gcloud alpha compute backend-buckets  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets)*

**NAME**

: **gcloud alpha compute backend-buckets - read and manipulate backend buckets**

**SYNOPSIS**

: **`gcloud alpha compute backend-buckets` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Read and manipulate backend buckets. Backend buckets define
Cloud Storage buckets that can serve content. URL maps define which requests are
sent to which backend buckets.
For more information about backend buckets, see the [backend
buckets documentation](https://cloud.google.com/load-balancing/docs/https/ext-load-balancer-backend-buckets).
See also: [Backend
buckets API](https://cloud.google.com/compute/docs/reference/rest/v1/backendBuckets).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[config](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/config)`**:
`(ALPHA)` Manage Compute Engine backend bucket configurations.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/add-iam-policy-binding)`**:
`(ALPHA)` Add an IAM policy binding to a Compute Engine backend
bucket.

**`[add-signed-url-key](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/add-signed-url-key)`**:
`(ALPHA)` Add Cloud CDN Signed URL key to a backend bucket.

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/create)`**:
`(ALPHA)` Create a backend bucket.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/delete)`**:
`(ALPHA)` Delete backend buckets.

**`[delete-signed-url-key](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/delete-signed-url-key)`**:
`(ALPHA)` Delete Cloud CDN Signed URL key from a backend bucket.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/describe)`**:
`(ALPHA)` Describe a backend bucket.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/get-iam-policy)`**:
`(ALPHA)` Get the IAM policy for a Compute Engine backend bucket.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/list)`**:
`(ALPHA)` List Google Compute Engine backend buckets.

**`[remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/remove-iam-policy-binding)`**:
`(ALPHA)` Remove an IAM policy binding from a Compute Engine backend
bucket.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/set-iam-policy)`**:
`(ALPHA)` Set the IAM policy binding for a Compute Engine backend
bucket.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-buckets/update)`**:
`(ALPHA)` Update a backend bucket.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute backend-buckets
```

```
gcloud beta compute backend-buckets
```