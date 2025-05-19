# gcloud alpha apigee archives deploy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/deploy](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/deploy)*

**NAME**

: **gcloud alpha apigee archives deploy - deploy an Apigee archive deployment to an environment**

**SYNOPSIS**

: **`gcloud alpha apigee archives deploy` (`[--environment](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/deploy#--environment)`=`ENVIRONMENT` : `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/deploy#--organization)`=`ORGANIZATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/deploy#--async)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/deploy#--labels)`=[`KEY`=`VALUE`,…]] [`[--bundle-file](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/deploy#--bundle-file)`=`BUNDLE_FILE`     | `[--source](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/deploy#--source)`=`SOURCE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/deploy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Deploy an Apigee archive deployment to an environment.
`gcloud alpha apigee archives deploy` installs an archive deployment
in an Apigee environment.
By default, the archive deployment will be deployed on the remote management
plane for the specified Apigee organization. To deploy on a locally running
Apigee emulator, use the `--local` flag.

**EXAMPLES**

: To deploy the contents of the current working directory as an archive deployment
to an environment named ``my-test``, given that
the Cloud Platform project has been set in gcloud settings, run:

```
gcloud alpha apigee archives deploy --environment=my-test
```

To deploy an archive deployment from a local directory other than the current
working directory, to an environment named
``my-demo`` in an organization belonging to a
Cloud Platform project other than the one set in gcloud settings, named
``my-org``, run:

```
gcloud alpha apigee archives deploy --organization=my-org --environment=my-demo --source=/apigee/dev
```

To deploy the contents of the current working directory as an archive
deployment, with the user-defined labels
``my-label1=foo`` and
``my-label2=bar``, to an environment named
``my-test``, given that the Cloud Platform
project has been set in gcloud settings, run:

```
gcloud alpha apigee archives deploy --environment=my-test --labels=my-label1=foo,my-label2=bar
```

**REQUIRED FLAGS**

: **--environment**

**OPTIONAL FLAGS**

: **--async**:
If set, returns immediately and outputs a description of the long running
operation that was launched. Else, `gcloud alpha apigee archives
deploy` will block until the archive deployment has been successfully
deployed to the specified environment.
To monitor the operation once it's been launched, run `gcloud alpha apigee
operations describe OPERATION_NAME`.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--bundle-file**

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
allowlist. This variant is also available:

```
gcloud beta apigee archives deploy
```