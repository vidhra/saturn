# gcloud deployment-manager deployments  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments)*

**NAME**

: **gcloud deployment-manager deployments - commands for Deployment Manager deployments**

**SYNOPSIS**

: **`gcloud deployment-manager deployments` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Commands to create, update, delete, and examine deployments of resources.

**EXAMPLES**

: To create a deployment, run:

```
gcloud deployment-manager deployments create my-deployment --config config.yaml
```

To update a deployment, run:

```
gcloud deployment-manager deployments update my-deployment --config new_config.yaml
```

To stop a deployment create or update in progress, run:

```
gcloud deployment-manager deployments stop my-deployment
```

To cancel a previewed create or update, run:

```
gcloud deployment-manager deployments cancel-preview my-deployment
```

To delete a deployment, run:

```
gcloud deployment-manager deployments delete my-deployment
```

To view the details of a deployment, run:

```
gcloud deployment-manager deployments describe my-deployment
```

To see the list of all deployments, run:

```
gcloud deployment-manager deployments list
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[cancel-preview](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/cancel-preview)`**:
Cancel a pending or running deployment preview.

**`[create](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/create)`**:
Create a deployment.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/delete)`**:
Delete a deployment.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/describe)`**:
Provide information about a deployment.

**`[list](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/list)`**:
List deployments in a project.

**`[stop](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/stop)`**:
Stop a pending or running deployment update or creation.

**`[update](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/update)`**:
Update a deployment based on a provided config file.

**NOTES**

: These variants are also available:

```
gcloud alpha deployment-manager deployments
```

```
gcloud beta deployment-manager deployments
```