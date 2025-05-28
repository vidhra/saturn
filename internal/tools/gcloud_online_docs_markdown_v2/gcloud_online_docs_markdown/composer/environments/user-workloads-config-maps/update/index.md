# gcloud composer environments user-workloads-config-maps update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/composer/environments/user-workloads-config-maps/update](https://cloud.google.com/sdk/gcloud/reference/composer/environments/user-workloads-config-maps/update)*

**NAME**

: **gcloud composer environments user-workloads-config-maps update - update a user workloads ConfigMap**

**SYNOPSIS**

: **`gcloud composer environments user-workloads-config-maps update` `[--config-map-file-path](https://cloud.google.com/sdk/gcloud/reference/composer/environments/user-workloads-config-maps/update#--config-map-file-path)`=`CONFIG_MAP_FILE_PATH` (`[--environment](https://cloud.google.com/sdk/gcloud/reference/composer/environments/user-workloads-config-maps/update#--environment)`=`ENVIRONMENT` : `[--location](https://cloud.google.com/sdk/gcloud/reference/composer/environments/user-workloads-config-maps/update#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/composer/environments/user-workloads-config-maps/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a user workloads ConfigMap.

**EXAMPLES**

: To update a user workloads ConfigMap of the environment named env-1, run:

```
gcloud composer environments user-workloads-config-maps update --environment=env-1 --config-map-file-path=config_map.yaml
```

**REQUIRED FLAGS**

: **--config-map-file-path**:
Path to a local file with a single Kubernetes ConfigMap in YAML format.

**Environment resource - The environment where the user workloads ConfigMap must
be updated. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `--environment` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--environment**:
ID of the environment or fully qualified identifier for the environment.
To set the `environment` attribute:

- provide the argument `--environment` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--location**:
Region where Composer environment runs or in which to create the environment.
To set the `location` attribute:

- provide the argument `--environment` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `composer/location`.**

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
gcloud alpha composer environments user-workloads-config-maps update
```

```
gcloud beta composer environments user-workloads-config-maps update
```