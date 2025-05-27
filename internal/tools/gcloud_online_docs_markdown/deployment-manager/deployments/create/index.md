# gcloud deployment-manager deployments create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/create](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/create)*

**NAME**

: **gcloud deployment-manager deployments create - create a deployment**

**SYNOPSIS**

: **`gcloud deployment-manager deployments create` `[DEPLOYMENT_NAME](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/create#DEPLOYMENT_NAME)` (`[--composite-type](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/create#--composite-type)`=`COMPOSITE_TYPE`     | `[--config](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/create#--config)`=`CONFIG`     | `[--template](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/create#--template)`=`TEMPLATE`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--preview](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/create#--preview)`] [`[--properties](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/create#--properties)`=[`PROPERTIES`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/create#--async)`     | `[--automatic-rollback-on-error](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/create#--automatic-rollback-on-error)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command inserts (creates) a new deployment based on a provided config file.

**EXAMPLES**

: To create a new deployment from a top-level YAML file, run:

```
gcloud deployment-manager deployments create my-deployment --config=config.yaml --description="My deployment"
```

To create a new deployment from a top-level template file, run:

```
gcloud deployment-manager deployments create my-deployment --template=template.{jinja|py} --properties="string-key:'string-value',integer-key:12345"
```

To create a new deployment directly from a composite type, run:

```
gcloud deployment-manager deployments create my-deployment --composite-type=<project-id>/composite:<type-name> --properties="string-key:'string-value',integer-key:12345"
```

To preview a deployment without actually creating resources, run:

```
gcloud deployment-manager deployments create my-new-deployment --config=config.yaml --preview
```

To instantiate a deployment that has been previewed, issue an update command for
that deployment without specifying a config file.
More information is available at [https://cloud.google.com/deployment-manager/docs/configuration/](https://cloud.google.com/deployment-manager/docs/configuration/).

**POSITIONAL ARGUMENTS**

: **`DEPLOYMENT_NAME`**:
Deployment name.

**REQUIRED FLAGS**

: **--composite-type**

**OPTIONAL FLAGS**

: **--description**:
Optional description of the deployment to insert.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--preview**:
Preview the requested create without actually instantiating the underlying
resources. (default=False)

**--properties**:
A comma separated, key:value, map to be used when deploying a template file or
composite type directly.

**--async**

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
gcloud alpha deployment-manager deployments create
```

```
gcloud beta deployment-manager deployments create
```