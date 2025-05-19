# gcloud apigee  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/apigee](https://cloud.google.com/sdk/gcloud/reference/apigee)*

**NAME**

: **gcloud apigee - manage Apigee resources**

**SYNOPSIS**

: **`gcloud apigee` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/apigee#GROUP)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/apigee#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage Apigee resources.

**EXAMPLES**

: To list API proxies in the active Cloud Platform project, run:

```
gcloud apigee apis list
```

To deploy an API proxy named ``hello-world`` to
the ``test`` environment, run:

```
gcloud apigee apis deploy --environment=test --api=hello-world
```

To get the status of that deployment, run:

```
gcloud apigee deployments describe --environment=test --api=hello-world
```

To undeploy that API proxy, run:

```
gcloud apigee apis undeploy --environment=test --api=hello-world
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[apis](https://cloud.google.com/sdk/gcloud/reference/apigee/apis)`**:
Manage Apigee API proxies.

**`[applications](https://cloud.google.com/sdk/gcloud/reference/apigee/applications)`**:
Manage third-party applications which call Apigee API proxies.

**`[deployments](https://cloud.google.com/sdk/gcloud/reference/apigee/deployments)`**:
Manage deployments of Apigee API proxies in runtime environments.

**`[developers](https://cloud.google.com/sdk/gcloud/reference/apigee/developers)`**:
Manage Apigee developers.

**`[environments](https://cloud.google.com/sdk/gcloud/reference/apigee/environments)`**:
Manage Apigee environments.

**`[organizations](https://cloud.google.com/sdk/gcloud/reference/apigee/organizations)`**:
Manage Apigee organizations.

**`[products](https://cloud.google.com/sdk/gcloud/reference/apigee/products)`**:
Manage Apigee API products.

**NOTES**

: These variants are also available:

```
gcloud alpha apigee
```

```
gcloud beta apigee
```