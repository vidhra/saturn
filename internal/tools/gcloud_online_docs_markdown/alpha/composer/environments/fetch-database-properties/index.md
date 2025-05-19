# gcloud alpha composer environments fetch-database-properties  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/fetch-database-properties](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/fetch-database-properties)*

**NAME**

: **gcloud alpha composer environments fetch-database-properties - fetch database properties**

**SYNOPSIS**

: **`gcloud alpha composer environments fetch-database-properties` (`[ENVIRONMENT](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/fetch-database-properties#ENVIRONMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/fetch-database-properties#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/fetch-database-properties#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Fetch database properties.

**EXAMPLES**

: To fetch database properties for the environment named
``environment-1``, run:
```
gcloud alpha composer environments fetch-database-properties environment-1
```

**POSITIONAL ARGUMENTS**

: **Environment resource - The environment for which to fetch database properties.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud composer environments fetch-database-properties
```

```
gcloud beta composer environments fetch-database-properties
```