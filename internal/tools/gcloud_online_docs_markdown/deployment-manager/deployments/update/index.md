# gcloud deployment-manager deployments update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/update](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/update)*

**NAME**

: **gcloud deployment-manager deployments update - update a deployment based on a provided config file**

**SYNOPSIS**

: **`gcloud deployment-manager deployments update` `[DEPLOYMENT_NAME](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/update#DEPLOYMENT_NAME)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/update#--async)`] [`[--create-policy](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/update#--create-policy)`=`CREATE_POLICY`; default="create-or-acquire"] [`[--delete-policy](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/update#--delete-policy)`=`DELETE_POLICY`; default="delete"] [`[--description](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/update#--description)`=`DESCRIPTION`] [`[--fingerprint](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/update#--fingerprint)`=`FINGERPRINT`] [`[--preview](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/update#--preview)`] [`[--properties](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/update#--properties)`=[`PROPERTIES`,…]] [`[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/update#--remove-labels)`=[`KEY`,…]] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--composite-type](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/update#--composite-type)`=`COMPOSITE_TYPE`     | `[--config](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/update#--config)`=`CONFIG`     | `[--template](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/update#--template)`=`TEMPLATE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command will update a deployment with the new config file provided.
Different policies for create, update, and delete policies can be specified.

**EXAMPLES**

: To update an existing deployment with a new config YAML file, run:

```
gcloud deployment-manager deployments update my-deployment --config=new_config.yaml
```

To update an existing deployment with a new config template file, run:

```
gcloud deployment-manager deployments update my-deployment --template=new_config.{jinja|py}
```

To update an existing deployment with a composite type as a new config, run:

```
gcloud deployment-manager deployments update my-deployment --composite-type=<project-id>/composite:<new-config>
```

To preview an update to an existing deployment without actually modifying the
resources, run:

```
gcloud deployment-manager deployments update my-deployment --config=new_config.yaml --preview
```

To apply an update that has been previewed, provide the name of the previewed
deployment, and no config file:

```
gcloud deployment-manager deployments update my-deployment
```

To specify different create, update, or delete policies, include any subset of
the following flags:

```
gcloud deployment-manager deployments update my-deployment --config=new_config.yaml --create-policy=acquire --delete-policy=abandon
```

To perform an update without waiting for the operation to complete, run:

```
gcloud deployment-manager deployments update my-deployment --config=new_config.yaml --async
```

To update an existing deployment with a new config file and a fingerprint, run:

```
gcloud deployment-manager deployments update my-deployment --config=new_config.yaml --fingerprint=deployment-fingerprint
```

Either the `--config`, `--template`, or
`--composite-type` flag is required unless launching an
already-previewed update to a deployment. If you want to update a deployment's
metadata, such as the labels or description, you must run a separate command
with `--update-labels`, `--remove-labels`, or
`--description`, as applicable.
More information is available at [https://cloud.google.com/deployment-manager/docs/deployments/updating-deployments](https://cloud.google.com/deployment-manager/docs/deployments/updating-deployments).

**POSITIONAL ARGUMENTS**

: **`DEPLOYMENT_NAME`**:
Deployment name.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--create-policy**:
Create policy for resources that have changed in the update.
`CREATE_POLICY` must be one of: `acquire`,
`create-or-acquire`.

**--delete-policy**:
Delete policy for resources that will change as part of an update or delete.
`delete` deletes the resource while `abandon` just removes
the resource reference from the deployment.
`DELETE_POLICY` must be one of: `abandon`,
`delete`.

**--description**:
The new description of the deployment.

**--fingerprint**:
The fingerprint to use in requests to modify a deployment. If not specified, a
get deployment request will be made to fetch the latest fingerprint. A
fingerprint is a randomly generated value that is part of the update, stop, and
cancel-preview request to perform optimistic locking. It is initially generated
by Deployment Manager and changes after every request to modify data. The latest
fingerprint is printed when deployment data is modified.

**--preview**:
Preview the requested update without making any changes to the underlying
resources. (default=False)

**--properties**:
A comma separated, key:value, map to be used when deploying a template file or
composite type directly.

**--remove-labels**:
List of label keys to remove. If a label does not exist it is silently ignored.
If `--update-labels` is also specified then
`--update-labels` is applied first.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--composite-type**

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

: These variants are also available:

```
gcloud alpha deployment-manager deployments update
```

```
gcloud beta deployment-manager deployments update
```