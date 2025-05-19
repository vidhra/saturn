# gcloud composer environments list-packages  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/composer/environments/list-packages](https://cloud.google.com/sdk/gcloud/reference/composer/environments/list-packages)*

**NAME**

: **gcloud composer environments list-packages - list all PyPI modules installed in an Airflow worker**

**SYNOPSIS**

: **`gcloud composer environments list-packages` (`[ENVIRONMENT](https://cloud.google.com/sdk/gcloud/reference/composer/environments/list-packages#ENVIRONMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/composer/environments/list-packages#--location)`=`LOCATION`) [`[--tree](https://cloud.google.com/sdk/gcloud/reference/composer/environments/list-packages#--tree)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/composer/environments/list-packages#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List all PyPI modules installed in an Airflow worker.

**EXAMPLES**

: The following command:

```
gcloud composer environments list-packages myenv
```

runs the "python -m pip list" command on a worker and returns the output.
The following command:

```
gcloud composer environments list-packages myenv --tree
```

runs the "python -m pipdeptree --warn" command on a worker and returns the
output.

**POSITIONAL ARGUMENTS**

: **Environment resource - The environment in which to list PyPI modules. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `environment` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ENVIRONMENT`**:
ID of the environment or fully qualified identifier for the environment.
To set the `environment` attribute:

- provide the argument `environment` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Region where Composer environment runs or in which to create the environment.
To set the `location` attribute:

- provide the argument `environment` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `composer/location`.**

**FLAGS**

: **--tree**:
List PyPI packages, their versions and a dependency tree, as displayed by the
"python -m pipdeptree --warn" command.

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
gcloud alpha composer environments list-packages
```

```
gcloud beta composer environments list-packages
```