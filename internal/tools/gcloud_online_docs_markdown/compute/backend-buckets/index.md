# gcloud compute backend-buckets  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets)*

**NAME**

: **gcloud compute backend-buckets - read and manipulate backend buckets**

**SYNOPSIS**

: **`gcloud compute backend-buckets` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Read and manipulate backend buckets. Backend buckets define Cloud Storage
buckets that can serve content. URL maps define which requests are sent to which
backend buckets.
For more information about backend buckets, see the [backend
buckets documentation](https://cloud.google.com/load-balancing/docs/https/ext-load-balancer-backend-buckets).
See also: [Backend
buckets API](https://cloud.google.com/compute/docs/reference/rest/v1/backendBuckets).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/add-iam-policy-binding)`**:
Add an IAM policy binding to a Compute Engine backend bucket.

**`[add-signed-url-key](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/add-signed-url-key)`**:
Add Cloud CDN Signed URL key to a backend bucket.

**`[create](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/create)`**:
Create a backend bucket.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/delete)`**:
Delete backend buckets.

**`[delete-signed-url-key](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/delete-signed-url-key)`**:
Delete Cloud CDN Signed URL key from a backend bucket.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/describe)`**:
Describe a backend bucket.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/get-iam-policy)`**:
Get the IAM policy for a Compute Engine backend bucket.

**`[list](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/list)`**:
List Google Compute Engine backend buckets.

**`[remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/remove-iam-policy-binding)`**:
Remove an IAM policy binding from a Compute Engine backend bucket.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/set-iam-policy)`**:
Set the IAM policy binding for a Compute Engine backend bucket.

**`[update](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update)`**:
Update a backend bucket.

**NOTES**

: These variants are also available:

```
gcloud alpha compute backend-buckets
```

```
gcloud beta compute backend-buckets
```