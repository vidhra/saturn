# gcloud alpha apigee products create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create)*

**NAME**

: **gcloud alpha apigee products create - create an Apigee API product**

**SYNOPSIS**

: **`gcloud alpha apigee products create` [`[INTERNAL_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create#INTERNAL_NAME)` : `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create#--organization)`=`ORGANIZATION`] [`[--attributes](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create#--attributes)`=[`NAME`=`VALUE`,…]] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create#--display-name)`=`DISPLAY_NAME`] [`[--manual-approval](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create#--manual-approval)`] [`[--oauth-scopes](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create#--oauth-scopes)`=[`SCOPE`,…]] [`[--all-environments](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create#--all-environments)`     | `[--environments](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create#--environments)`=`ENVIRONMENT`,[`[ENVIRONMENT](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create#ENVIRONMENT)`,…]] [`[--all-proxies](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create#--all-proxies)`     | `[--apis](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create#--apis)`=[`API`,…] `[--resources](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create#--resources)`=`RESOURCE`#[`[RESOURCE](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create#RESOURCE)`#…]] [`[--internal-access](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create#--internal-access)`     | `[--private-access](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create#--private-access)`     | `[--public-access](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create#--public-access)`] [`[--quota](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create#--quota)`=`QUOTA` `[--quota-interval](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create#--quota-interval)`=`QUOTA_INTERVAL` `[--quota-unit](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create#--quota-unit)`=`QUOTA_UNIT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create an Apigee API product.
`gcloud alpha apigee products create` publishes a collection of API
proxy resources as an API product.
API products combine their underlying API proxies with quota settings and
metadata, to deliver customized and productized API bundles to the developer
community.
API products enable the repackaging of APIs on-the-fly, without having to do any
additional coding or configuration. Apigee recommends starting with a simple API
product including only required elements, and then provisioning credentials to
apps to enable them to start testing those APIs.
At minimum, a new API product requires an internal name, access policy, and
declaration of what environments and API proxies to include in the product. If
these aren't provided, interactive calls will prompt for the missing values, and
non-interactive calls will fail.

**EXAMPLES**

: To create a basic API product in the active Cloud Platform project by answering
interactive prompts, run:

```
gcloud alpha apigee products create
```

To create an API product that publicly exposes all API proxies deployed to the
``prod`` environment, run:

```
gcloud alpha apigee products create kitchen-sink --environments=prod --all-proxies --public-access
```

To require manual approval of developers before they can access the new API
product, run:

```
gcloud alpha apigee products create kitchen-sink --environments=prod --all-proxies --public-access --manual-approval
```

To hide the new API product while still making it accessible to developers, run:

```
gcloud alpha apigee products create kitchen-sink --environments=prod --all-proxies --private-access
```

To restrict the new API product to internal users only, run:

```
gcloud alpha apigee products create kitchen-sink --environments=prod --all-proxies --internal-access
```

To expose all API proxies that are deployed to a URI fragment beginning with
``/v1`` or
``/v0``, run:

```
gcloud alpha apigee products create legacy --all-environments --resources="/v0/**#/v1/**" --public-access
```

To expose a few specific API proxies on all URI paths where they're deployed,
run:

```
gcloud alpha apigee products create consumer --environments=prod --apis=menu,cart,delivery-tracker --public-access
```

To expose only those API calls that match both a set of API proxies and a set of
API resources, run:

```
gcloud alpha apigee products create legacy-consumer --environments=prod --apis=menu,cart,delivery-tracker --resources="/v0/**#/v1/**" --public-access
```

To impose a quota of 50 calls per half-hour on a new all-inclusive API product,
and output the new API product as a JSON object, run:

```
gcloud alpha apigee products create kitchen-sink --environments=prod --all-proxies --public-access --quota=50 --quota-interval=30 --quota-unit=minute --format=json
```

To specify a human-friendly display name and description for the product, run:

```
gcloud alpha apigee products create consumer --environments=prod --apis=menu,cart,delivery-tracker --public-access --display-name="Consumer APIs" --description="APIs for the consumer side of the delivery network: ordering food and tracking deliveries."
```

**POSITIONAL ARGUMENTS**

: **API product resource - API product to be created. Characters in a product's
internal name are restricted to: `A-Za-z0-9._-$ %`. The arguments in
this group can be used to specify the attributes of this resource.

**`INTERNAL_NAME`**:
ID of the API product or fully qualified identifier for the API product.
To set the `product` attribute:

- provide the argument `INTERNAL_NAME` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--organization**:
Apigee organization containing the API product. If unspecified, the Cloud
Platform project's associated organization will be used.
To set the `organization` attribute:

- provide the argument `INTERNAL_NAME` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line.**

**FLAGS**

: **--attributes**:
Key-value attribute pairs that may be used to extend the default API product
profile with customer-specific metadata. Up to 17 attributes can be specified.

**--description**:
Overview of the API product. Include key information about the API product that
is not captured by other fields.

**--display-name**:
Name to be displayed in the UI or developer portal to developers registering for
API access.

**--manual-approval**:
Require manual approval of developer requests to access this API product before
their consumer keys can be used. If unset, the consumer key is generated in an
"approved" state and can be used immediately.

**--oauth-scopes**:
Comma-separated list of OAuth scopes that are validated at runtime. Apigee
validates that the scopes in any access token presented match the scopes defined
in the OAuth policy assoicated with the API product.

**--all-environments**

**--all-proxies**

**--internal-access**

**--quota**

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
gcloud apigee products create
```

```
gcloud beta apigee products create
```