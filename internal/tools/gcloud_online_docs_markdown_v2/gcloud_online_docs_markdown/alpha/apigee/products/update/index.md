# gcloud alpha apigee products update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update)*

**NAME**

: **gcloud alpha apigee products update - update an existing Apigee API product**

**SYNOPSIS**

: **`gcloud alpha apigee products update` (`[PRODUCT](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#PRODUCT)` : `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--organization)`=`ORGANIZATION`) [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--display-name)`=`SET_DISPLAYNAME`] [`[--all-apis](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--all-apis)`     | `[--add-api](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--add-api)`=[`API`,…] `[--remove-api](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--remove-api)`=[`API`,…]] [`[--all-environments](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--all-environments)`     | `[--add-environment](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--add-environment)`=[`ENVIRONMENT`,…] `[--remove-environment](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--remove-environment)`=[`ENVIRONMENT`,…]] [`[--all-resources](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--all-resources)`     | `[--add-resource](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--add-resource)`=[`RESOURCE`#…] `[--remove-resource](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--remove-resource)`=[`RESOURCE`#…]] [`[--automatic-approval](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--automatic-approval)`     | `[--manual-approval](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--manual-approval)`] [`[--clear-attributes](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--clear-attributes)`     | `[--add-attribute](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--add-attribute)`=[`NAME`=`VALUE`,…] `[--remove-attribute](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--remove-attribute)`=[`NAME`,…]] [`[--clear-description](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--clear-description)`     | `[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--description)`=`SET_DESCRIPTION`] [`[--clear-oauth-scopes](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--clear-oauth-scopes)`     | `[--add-oauth-scope](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--add-oauth-scope)`=[`OAUTH-SCOPE`,…] `[--remove-oauth-scope](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--remove-oauth-scope)`=[`OAUTH-SCOPE`,…]] [`[--clear-quota](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--clear-quota)`     | `[--quota](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--quota)`=`QUOTA` `[--quota-interval](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--quota-interval)`=`QUOTA_INTERVAL` `[--quota-unit](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--quota-unit)`=`QUOTA_UNIT`] [`[--internal-access](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--internal-access)`     | `[--private-access](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--private-access)`     | `[--public-access](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#--public-access)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update an existing Apigee API product.
`gcloud alpha apigee products update` applies a set of modifications
to an existing API product.
To create a new API product, run:

```
gcloud alpha apigee products create
```

**EXAMPLES**

: To update the display name of the API product with the internal name
``my-prod``, run:

```
gcloud alpha apigee products update my-prod --display-name="Example Project"
```

To update the description of the API product, run:

```
gcloud alpha apigee products update my-prod --description="This API is famous for appearing in a YouTube video."
```

To remove the API product's description, run:

```
gcloud alpha apigee products update my-prod --clear-description
```

To remove manual approval requirements from the API and change its access level
to public, run:

```
gcloud alpha apigee products update my-prod --public-access --automatic-approval
```

To impose a quota of 45 calls per minute per application on the API product,
run:

```
gcloud alpha apigee products update my-prod --quota=45 --quota-interval=1 --quota-unit=minute
```

To remove a quota on the API product and switch it to unlisted access with
manual approval, run:

```
gcloud alpha apigee products update my-prod --manual-approval --private-access --clear-quota
```

To set the API product's custom attribute
``foo`` to the value
``bar``, updating that attribute if it exists
and creating it if it doesn't, and remove the attribute
``baz`` if it exists, run:

```
gcloud alpha apigee products update my-prod --add-attribute="foo=bar" --remove-attribute=baz
```

To update the list of API proxies included in the API product, run:

```
gcloud alpha apigee products update my-prod --add-api=NEW_ONE,NEW_TWO --remove-api=OLD_ONE,OLD_TWO
```

To switch the API product to including all
``test`` environment APIs no matter what API
proxy or resource they expose, run:

```
gcloud alpha apigee products update my-prod --add-environment=test --all-apis --all-resources
```

To update the list of API resources included in the API product, and output the
updated API product as a JSON object, run:

```
gcloud alpha apigee products update my-prod --add-resource="NEW_ONE#NEW_TWO" --remove-resource="OLD_ONE#OLD_TWO" --format=json
```

**POSITIONAL ARGUMENTS**

: **API product resource - API product to be updated. To get a list of available API
products, run:

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

**FLAGS**

: **--display-name**:
Name to be displayed in the UI or developer portal to developers registering for
API access.

**--all-apis**

**--all-environments**

**--all-resources**

**--automatic-approval**

**--clear-attributes**

**--clear-description**

**--clear-oauth-scopes**

**--clear-quota**

**--internal-access**

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
gcloud apigee products update
```

```
gcloud beta apigee products update
```