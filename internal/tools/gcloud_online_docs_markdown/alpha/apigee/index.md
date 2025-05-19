# gcloud alpha apigee  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/apigee](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee)*

**NAME**

: **gcloud alpha apigee - manage Apigee resources**

**SYNOPSIS**

: **`gcloud alpha apigee` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee#GROUP)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Manage Apigee resources.

**EXAMPLES**

: To list API proxies in the active Cloud Platform project, run:

```
gcloud alpha apigee apis list
```

To deploy an API proxy named ``hello-world`` to
the ``test`` environment, run:

```
gcloud alpha apigee apis deploy --environment=test --api=hello-world
```

To get the status of that deployment, run:

```
gcloud alpha apigee deployments describe --environment=test --api=hello-world
```

To undeploy that API proxy, run:

```
gcloud alpha apigee apis undeploy --environment=test --api=hello-world
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[apis](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/apis)`**:
`(ALPHA)` Manage Apigee API proxies.

**`[applications](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications)`**:
`(ALPHA)` Manage third-party applications which call Apigee API
proxies.

**`[archives](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives)`**:
`(ALPHA)` Manage Apigee archive deployments.

**`[deployments](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments)`**:
`(ALPHA)` Manage deployments of Apigee API proxies in runtime
environments.

**`[developers](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/developers)`**:
`(ALPHA)` Manage Apigee developers.

**`[environments](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/environments)`**:
`(ALPHA)` Manage Apigee environments.

**`[operations](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/operations)`**:
`(ALPHA)` Manage Apigee long running operations.

**`[organizations](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations)`**:
`(ALPHA)` Manage Apigee organizations.

**`[products](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/products)`**:
`(ALPHA)` Manage Apigee API products.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud apigee
```

```
gcloud beta apigee
```