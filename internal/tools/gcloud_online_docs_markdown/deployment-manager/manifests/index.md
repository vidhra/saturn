# gcloud deployment-manager manifests  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deployment-manager/manifests](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/manifests)*

**NAME**

: **gcloud deployment-manager manifests - commands for Deployment Manager manifests**

**SYNOPSIS**

: **`gcloud deployment-manager manifests` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/manifests#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/manifests#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Commands to list and examine manifests within a deployment.

**EXAMPLES**

: To view all details about a manifest, run:

```
gcloud deployment-manager manifests describe manifest-name --deployment my-deployment
```

To see the list of all manifests in a deployment, run:

```
gcloud deployment-manager manifests list --deployment my-deployment
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/manifests/describe)`**:
Provide information about a manifest.

**`[list](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/manifests/list)`**:
List manifests in a deployment.

**NOTES**

: These variants are also available:

```
gcloud alpha deployment-manager manifests
```

```
gcloud beta deployment-manager manifests
```