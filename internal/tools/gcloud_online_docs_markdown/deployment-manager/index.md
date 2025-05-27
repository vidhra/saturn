# gcloud deployment-manager  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deployment-manager](https://cloud.google.com/sdk/gcloud/reference/deployment-manager)*

**NAME**

: **gcloud deployment-manager - manage deployments of cloud resources**

**SYNOPSIS**

: **`gcloud deployment-manager` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/deployment-manager#GROUP)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deployment-manager#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud deployment-manager command group lets you manage the deployment of
Google Cloud Platform resources using Google Cloud Deployment Manager.
Google Cloud Deployment Manager allows you to specify all the resources needed
for your application in a declarative format using YAML. You can also use Python
or Jinja2 templates to parameterize the configuration and allow reuse of common
deployment paradigms such as a load balanced, auto-scaled instance group.
More information on Cloud Deployment Manager can be found here: [https://cloud.google.com/deployment-manager](https://cloud.google.com/deployment-manager)
and detailed documentation can be found here: [https://cloud.google.com/deployment-manager/docs/](https://cloud.google.com/deployment-manager/docs/)

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[deployments](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments)`**:
Commands for Deployment Manager deployments.

**`[manifests](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/manifests)`**:
Commands for Deployment Manager manifests.

**`[operations](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/operations)`**:
Commands for Deployment Manager operations.

**`[resources](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/resources)`**:
Commands for Deployment Manager resources.

**`[types](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/types)`**:
Commands for Deployment Manager types.

**NOTES**

: These variants are also available:

```
gcloud alpha deployment-manager
```

```
gcloud beta deployment-manager
```