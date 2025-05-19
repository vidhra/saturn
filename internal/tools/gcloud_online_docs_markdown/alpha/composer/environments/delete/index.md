# gcloud alpha composer environments delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/delete](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/delete)*

**NAME**

: **gcloud alpha composer environments delete - delete one or more Cloud Composer environments**

**SYNOPSIS**

: **`gcloud alpha composer environments delete` (`[ENVIRONMENTS](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/delete#ENVIRONMENTS)` [`[ENVIRONMENTS](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/delete#ENVIRONMENTS)` …] : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Environments cannot be deleted unless they are in one of
the RUNNING or ERROR states. If run asynchronously with `--async`,
exits after printing one or more operation names that can be used to poll the
status of the deletion(s) via:

```
gcloud composer operations describe
```

If any of the environments are already in the process of being deleted, the
original deletion operations are waited on (default) or printed
(`--async`).

**EXAMPLES**

: To delete the environment named
``environment-1``, run:

```
gcloud alpha composer environments delete environment-1
```

**POSITIONAL ARGUMENTS**

: **Environment resource - The environments to delete. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `environments` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ENVIRONMENTS` [`ENVIRONMENTS` …]**:
IDs of the environments or fully qualified identifiers for the environments.
To set the `environment` attribute:

- provide the argument `environments` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Region where Composer environment runs or in which to create the environment.
To set the `location` attribute:

- provide the argument `environments` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `composer/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud composer environments delete
```

```
gcloud beta composer environments delete
```