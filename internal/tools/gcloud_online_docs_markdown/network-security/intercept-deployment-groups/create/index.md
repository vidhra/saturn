# gcloud network-security intercept-deployment-groups create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/create](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/create)*

**NAME**

: **gcloud network-security intercept-deployment-groups create - create an Intercept Deployment Group**

**SYNOPSIS**

: **`gcloud network-security intercept-deployment-groups create` (`[INTERCEPT_DEPLOYMENT_GROUP](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/create#INTERCEPT_DEPLOYMENT_GROUP)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/create#--location)`=`LOCATION`) `[--network](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/create#--network)`=`NETWORK` [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--max-wait](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/create#--max-wait)`=`MAX_WAIT`; default="20m"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create an intercept deployment group. Successful creation of a deployment group
results in a deployment group in ACTIVE state. Check the progress of deployment
group creation by using `[gcloud
network-security intercept-deployment-groups list](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/list)`.
For more examples, refer to the EXAMPLES section below.

**EXAMPLES**

: To create a intercept deployment group called `my-deployment-group`,
in project ID `my-project`, run:
```
gcloud network-security intercept-deployment-groups create my-deployment-group --project=my-project --location=global --network=my-network
```

OR

```
gcloud network-security intercept-deployment-groups create my-deployment-group --project=my-project --location=global --network=projects/my-project/global/networks/my-network
```

OR

```
gcloud network-security intercept-deployment-groups create projects/my-project/locations/global/interceptDeploymentGroups/my-deployment-group --network=projects/my-project/global/networks/my-network
```

OR

```
gcloud network-security intercept-deployment-groups create projects/my-project/locations/global/interceptDeploymentGroups/my-deployment-group --network=projects/my-project/global/networks/my-network --description='new description'
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

**REQUIRED FLAGS**

: **Network resource - Intercept Deployment Group. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `--network` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--network**:
ID of the network or fully qualified identifier for the network.
To set the `network-name` attribute:

- provide the argument `--network` on the command line.**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--description**:
Description of the deployment group.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--max-wait**:
Time to synchronously wait for the operation to complete, after which the
operation continues asynchronously. Ignored if --no-async isn't specified. See $
[gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on time formats.

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
gcloud alpha network-security intercept-deployment-groups create
```

```
gcloud beta network-security intercept-deployment-groups create
```