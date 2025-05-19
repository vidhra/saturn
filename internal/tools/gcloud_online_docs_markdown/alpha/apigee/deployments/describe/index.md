# gcloud alpha apigee deployments describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/describe)*

**NAME**

: **gcloud alpha apigee deployments describe - describe an Apigee API proxy deployment**

**SYNOPSIS**

: **`gcloud alpha apigee deployments describe` [[`[REVISION](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/describe#REVISION)`] `[--api](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/describe#--api)`=`API` `[--environment](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/describe#--environment)`=`ENVIRONMENT` `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/describe#--organization)`=`ORGANIZATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Describe an Apigee API proxy deployment.
`gcloud alpha apigee deployments describe` retrieves the status of a
specific API proxy's deployment to a specific environment.

**EXAMPLES**

: To get the status of a deployment in the active Cloud Platform project, which
deploys ``my-proxy`` into the
``prod`` environment, run:

```
gcloud alpha apigee deployments describe --api=my-proxy --environment=prod
```

To get the status of that deployment as a JSON object, run:

```
gcloud alpha apigee deployments describe --api=my-proxy --environment=prod --format=json
```

To get the status of a deployment in an organization called
``my-org``, which deploys version 3 of the
proxy ``my-proxy`` into the
``test`` environment, run:

```
gcloud alpha apigee deployments describe 3 --organization=my-org --environment=test --api=my-proxy
```

**POSITIONAL ARGUMENTS**

: **Revision resource - API proxy revision and environment of the deployment to be
described.
To get a list of deployed proxies and their environments, run:

```
gcloud alpha apigee deployments list
```

REVISION can either be a positive revision number, or the special value
``auto``, which will choose whichever revision
of API is currently deployed in ENVIRONMENT, or return an error if more than one
revision is deployed.**

If REVISION is unspecified, the default is
``auto``.

```
The arguments in this group can be used to specify the attributes of this resource.
```

**[`REVISION`]**:
ID of the revision or fully qualified identifier for the revision.
To set the `revision` attribute:

- provide the argument `REVISION` on the command line;

- leave the argument unspecified for it to be chosen automatically.

**--api**:
Deployed API proxy.
To set the `api` attribute:

- provide the argument `REVISION` on the command line with a fully
specified name;
- leave the argument unspecified for it to be chosen automatically with a fully
specified name;
- provide the argument `--api` on the command line.

**--environment**:
Environment in which the proxy was deployed.
To set the `environment` attribute:

- provide the argument `REVISION` on the command line with a fully
specified name;
- leave the argument unspecified for it to be chosen automatically with a fully
specified name;
- provide the argument `--environment` on the command line.

**--organization**:
Apigee Organization of the proxy and environment. If unspecified, the Cloud
Platform project's associated organization will be used.
To set the `organization` attribute:

- provide the argument `REVISION` on the command line with a fully
specified name;
- leave the argument unspecified for it to be chosen automatically with a fully
specified name;
- provide the argument `--organization` on the command line;
- set the property [project] or provide the argument [--project] on the command
line, using a Cloud Platform project with an associated Apigee organization.

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
gcloud apigee deployments describe
```

```
gcloud beta apigee deployments describe
```