# gcloud network-security intercept-deployments update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/update](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/update)*

**NAME**

: **gcloud network-security intercept-deployments update - update an Intercept Deployment**

**SYNOPSIS**

: **`gcloud network-security intercept-deployments update` (`[INTERCEPT_DEPLOYMENT](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/update#INTERCEPT_DEPLOYMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/update#--description)`=`DESCRIPTION`] [`[--max-wait](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/update#--max-wait)`=`MAX_WAIT`; default="20m"] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an intercept deployment. Check the progress of deployment update by using
`[gcloud
network-security intercept-deployments list](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/list)`.
For examples refer to the EXAMPLES section below.

**EXAMPLES**

: To update labels k1 and k2, run:

```
gcloud network-security intercept-deployments update my-deployment --project=my-project --location=us-central1-a --update-labels=k1=v1,k2=v2
```

To remove labels k3 and k4, run:

```
gcloud network-security intercept-deployments update my-deployment --project=my-project --location=us-central1-a --remove-labels=k3,k4
```

To clear all labels from the intercept deployment, run:

```
gcloud network-security intercept-deployments update my-deploymen --project=my-project --location=us-central1-a --clear-labels
```

To update description to 'new description', run:

```
gcloud network-security intercept-deployments update my-deploymen --project=my-project --location=us-central1-a --description="new description"
```

**POSITIONAL ARGUMENTS**

: **Intercept deployment resource - Intercept Deployment. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `INTERCEPT_DEPLOYMENT` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INTERCEPT_DEPLOYMENT`**:
ID of the intercept deployment or fully qualified identifier for the intercept
deployment.
To set the `deployment-id` attribute:

- provide the argument `INTERCEPT_DEPLOYMENT` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the intercept deployment.
To set the `location` attribute:

- provide the argument `INTERCEPT_DEPLOYMENT` on the command line with
a fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--description**:
Description of the deployment.

**--max-wait**:
Time to synchronously wait for the operation to complete, after which the
operation continues asynchronously. Ignored if --no-async isn't specified. See $
[gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on time formats.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

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
gcloud alpha network-security intercept-deployments update
```

```
gcloud beta network-security intercept-deployments update
```