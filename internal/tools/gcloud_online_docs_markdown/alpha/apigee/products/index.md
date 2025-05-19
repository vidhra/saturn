# gcloud alpha apigee products  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products)*

**NAME**

: **gcloud alpha apigee products - manage Apigee API products**

**SYNOPSIS**

: **`gcloud alpha apigee products` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Manage Apigee API products.
`gcloud alpha apigee products` manipulates API products. These are
collections of deployed API resources, combined with quota settings and
metadata, used to deliver customized and productized API bundles to the
developer community.

**EXAMPLES**

: To list all API products in the active Cloud Platform project, run:

```
gcloud alpha apigee products list
```

To create an API product named ``my-apis`` by
answering interactive prompts about its included proxies and access policies,
run:

```
gcloud alpha apigee products create my-apis
```

To create an API product named ``prod-apis``
that makes every API proxy deployed to the
``prod`` environment publicly available, run:

```
gcloud alpha apigee products create prod-apis --environments=prod --all-proxies --public-access
```

To get a JSON object describing an existing API product, run:

```
gcloud alpha apigee products describe PRODUCT_NAME --organization=ORG_NAME --format=json
```

To add another API proxy to an existing API product, run:

```
gcloud alpha apigee products update PRODUCT_NAME --add-api=API_NAME
```

To edit the publicly visible name and description of an API product, run:

```
gcloud alpha apigee products update PRODUCT_NAME --display-name="New Name" --description="A new description of this product."
```

To make an existing product publicly visible and automatically allow developers
access to it, run:

```
gcloud alpha apigee products update PRODUCT_NAME --public-access --automatic-approval
```

To delete an existing API product, run:

```
gcloud alpha apigee products delete PRODUCT_NAME
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create)`**:
`(ALPHA)` Create an Apigee API product.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/delete)`**:
`(ALPHA)` Delete an Apigee API product.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/describe)`**:
`(ALPHA)` Describe an Apigee API product.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/list)`**:
`(ALPHA)` List Apigee API products.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update)`**:
`(ALPHA)` Update an existing Apigee API product.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud apigee products
```

```
gcloud beta apigee products
```