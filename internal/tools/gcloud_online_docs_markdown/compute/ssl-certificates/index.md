# gcloud compute ssl-certificates  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates)*

**NAME**

: **gcloud compute ssl-certificates - list, create, and delete Compute Engine SSL certificate resources**

**SYNOPSIS**

: **`gcloud compute ssl-certificates` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Read and manipulate SSL certificates that encrypt traffic between clients and a
load balancer. The relevant load balancer types are Application Load Balancers
and proxy Network Load Balancers.
For more information about SSL certificates, see the [SSL
certificates documentation](https://cloud.google.com/load-balancing/docs/ssl-certificates).
See also: [SSL
certificates API](https://cloud.google.com/compute/docs/reference/rest/v1/sslCertificates) and [regional
SSL certificates API](https://cloud.google.com/compute/docs/reference/rest/v1/regionSslCertificates).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create)`**:
Create a Compute Engine SSL certificate.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/delete)`**:
Delete Compute Engine SSL certificates.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/describe)`**:
Describe a Compute Engine SSL certificate.

**`[list](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/list)`**:
List Google Compute Engine SSL certificates.

**NOTES**

: These variants are also available:

```
gcloud alpha compute ssl-certificates
```

```
gcloud beta compute ssl-certificates
```