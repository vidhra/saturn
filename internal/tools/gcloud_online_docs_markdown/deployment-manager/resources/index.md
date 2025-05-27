# gcloud deployment-manager resources  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deployment-manager/resources](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/resources)*

**NAME**

: **gcloud deployment-manager resources - commands for Deployment Manager resources**

**SYNOPSIS**

: **`gcloud deployment-manager resources` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/resources#COMMAND)` [`[--deployment](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/resources#--deployment)`=`DEPLOYMENT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/resources#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Commands to list and examine resources within a deployment.

**EXAMPLES**

: To view all details about a resource, run:

```
gcloud deployment-manager resources describe my-resource --deployment my-deployment
```

To see the list of all resources in a deployment, run:

```
gcloud deployment-manager resources list --deployment my-deployment
```

**FLAGS**

: **--deployment**:
Deployment name

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/resources/describe)`**:
Provide information about a resource.

**`[list](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/resources/list)`**:
List resources in a deployment.

**NOTES**

: These variants are also available:

```
gcloud alpha deployment-manager resources
```

```
gcloud beta deployment-manager resources
```