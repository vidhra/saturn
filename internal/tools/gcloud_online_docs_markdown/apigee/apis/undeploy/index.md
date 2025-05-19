# gcloud apigee apis undeploy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/apigee/apis/undeploy](https://cloud.google.com/sdk/gcloud/reference/apigee/apis/undeploy)*

**NAME**

: **gcloud apigee apis undeploy - undeploy an Apigee API proxy from an environment**

**SYNOPSIS**

: **`gcloud apigee apis undeploy` [[`[REVISION](https://cloud.google.com/sdk/gcloud/reference/apigee/apis/undeploy#REVISION)`] `[--api](https://cloud.google.com/sdk/gcloud/reference/apigee/apis/undeploy#--api)`=`API` `[--environment](https://cloud.google.com/sdk/gcloud/reference/apigee/apis/undeploy#--environment)`=`ENVIRONMENT` `[--organization](https://cloud.google.com/sdk/gcloud/reference/apigee/apis/undeploy#--organization)`=`ORGANIZATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/apigee/apis/undeploy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Undeploy an Apigee API proxy from an environment.

**EXAMPLES**

: To undeploy an API proxy called ``my-api`` from
the ``test`` environment of the active Cloud
Platform project, run:

```
gcloud apigee apis undeploy --environment=test --api=my-api
```

To undeploy revision 3 of an `my-api` from the `test`
environment of the organization named
``test-org``, run:

```
gcloud apigee apis undeploy 3 --organization=test-org --environment=test --api=my-api
```

**POSITIONAL ARGUMENTS**

: **Revision resource - API proxy revision to be undeployed and environment from
which it should be removed.
Revisions can either be a positive revision number, or the special value
``auto``, which will undeploy whatever revision
is currently deployed. If revision is unspecified, the default is
``auto``. The arguments in this group can be
used to specify the attributes of this resource.

**[`REVISION`]**:
ID of the revision or fully qualified identifier for the revision.
To set the `revision` attribute:

- provide the argument `REVISION` on the command line;
- leave the argument unspecified for it to be chosen automatically.

**--api**:
API proxy to be undeployed. Must currently be deployed. To get a list of
available deployed proxies, run `gcloud apigee deployments list
--environment=ENV`.
To set the `api` attribute:

- provide the argument `REVISION` on the command line with a fully
specified name;
- leave the argument unspecified for it to be chosen automatically with a fully
specified name;
- provide the argument `--api` on the command line.

**--environment**:
Environment from which to undeploy the API proxy. To get a list of available
environments, run `[gcloud apigee environments
list](https://cloud.google.com/sdk/gcloud/reference/apigee/environments/list)`.
To set the `environment` attribute:

- provide the argument `REVISION` on the command line with a fully
specified name;
- leave the argument unspecified for it to be chosen automatically with a fully
specified name;
- provide the argument `--environment` on the command line.

**--organization**:
Apigee organization of the proxy and environment.
To set the `organization` attribute:

- provide the argument `REVISION` on the command line with a fully
specified name;
- leave the argument unspecified for it to be chosen automatically with a fully
specified name;
- provide the argument `--organization` on the command line;
- set the property [project] or provide the argument [--project] on the command
line, using a Cloud Platform project with an associated Apigee organization.**

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
gcloud alpha apigee apis undeploy
```

```
gcloud beta apigee apis undeploy
```