# gcloud alpha apigee products describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/describe)*

**NAME**

: **gcloud alpha apigee products describe - describe an Apigee API product**

**SYNOPSIS**

: **`gcloud alpha apigee products describe` (`[PRODUCT](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/describe#PRODUCT)` : `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/describe#--organization)`=`ORGANIZATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Describe an Apigee API product.

**EXAMPLES**

: To describe an API product called
``product-name`` in the active Cloud Platform
project, run:

```
gcloud alpha apigee products describe product-name
```

To describe an API product called
``other-product`` in an Apigee organization
called ``org-name``, run:

```
gcloud alpha apigee products describe other-product --organization=org-name
```

To describe an API product called
``product-name`` as a JSON object, run:

```
gcloud alpha apigee products describe product-name --format=json
```

**POSITIONAL ARGUMENTS**

: **API product resource - API product to be described. To get a list of available
API products, run:

```
gcloud alpha apigee products list
```

```
The arguments in this group can be used to specify the attributes of this resource.
```

This must be specified.

**`PRODUCT`**:
ID of the API product or fully qualified identifier for the API product.
To set the `product` attribute:

- provide the argument `PRODUCT` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--organization**:
Apigee organization containing the API product. If unspecified, the Cloud
Platform project's associated organization will be used.
To set the `organization` attribute:

- provide the argument `PRODUCT` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line;
- set the property [project] or provide the argument [--project] on the command
line, using a Cloud Platform project with an associated Apigee organization.**

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud apigee products describe
```

```
gcloud beta apigee products describe
```