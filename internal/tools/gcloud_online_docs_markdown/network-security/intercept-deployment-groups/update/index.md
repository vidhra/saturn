# gcloud network-security intercept-deployment-groups update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/update](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/update)*

**NAME**

: **gcloud network-security intercept-deployment-groups update - update an Intercept Deployment Group**

**SYNOPSIS**

: **`gcloud network-security intercept-deployment-groups update` (`[INTERCEPT_DEPLOYMENT_GROUP](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/update#INTERCEPT_DEPLOYMENT_GROUP)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/update#--description)`=`DESCRIPTION`] [`[--max-wait](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/update#--max-wait)`=`MAX_WAIT`; default="20m"] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an intercept deployment group. Check the progress of deployment group
update by using `[gcloud
network-security intercept-deployment-groups list](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/list)`.
For examples refer to the EXAMPLES section below.

**EXAMPLES**

: To update labels k1 and k2, run:

```
gcloud network-security intercept-deployment-groups update my-deployment-group --project=my-project --location=global --update-labels=k1=v1,k2=v2
```

To remove labels k3 and k4, run:

```
gcloud network-security intercept-deployment-groups update my-deployment-group --project=my-project --location=global --remove-labels=k3,k4
```

To clear all labels from the intercept deployment group, run:

```
gcloud network-security intercept-deployment-groups update my-deployment-group --project=my-project --location=global --clear-labels
```

To update description to 'new description', run:

```
gcloud network-security intercept-deployment-groups update my-deployment-group --project=my-project --location=global --description='new description'
```

**POSITIONAL ARGUMENTS**

: **Intercept deployment group resource - Intercept Deployment Group. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `INTERCEPT_DEPLOYMENT_GROUP` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INTERCEPT_DEPLOYMENT_GROUP`**:
ID of the intercept deployment group or fully qualified identifier for the
intercept deployment group.
To set the `deployment-group-id` attribute:

- provide the argument `INTERCEPT_DEPLOYMENT_GROUP` on the command
line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the intercept deployment group.
To set the `location` attribute:

- provide the argument `INTERCEPT_DEPLOYMENT_GROUP` on the command line
with a fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--description**:
Description of the deployment group.

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
gcloud alpha network-security intercept-deployment-groups update
```

```
gcloud beta network-security intercept-deployment-groups update
```