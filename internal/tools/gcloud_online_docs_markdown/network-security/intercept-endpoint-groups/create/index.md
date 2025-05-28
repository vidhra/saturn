# gcloud network-security intercept-endpoint-groups create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-groups/create](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-groups/create)*

**NAME**

: **gcloud network-security intercept-endpoint-groups create - create a Intercept Endpoint Group**

**SYNOPSIS**

: **`gcloud network-security intercept-endpoint-groups create` (`[INTERCEPT_ENDPOINT_GROUP](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-groups/create#INTERCEPT_ENDPOINT_GROUP)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-groups/create#--location)`=`LOCATION`) (`[--intercept-deployment-group](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-groups/create#--intercept-deployment-group)`=`INTERCEPT_DEPLOYMENT_GROUP` : `[--intercept-deployment-group-location](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-groups/create#--intercept-deployment-group-location)`=`INTERCEPT_DEPLOYMENT_GROUP_LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-groups/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-groups/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-groups/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--max-wait](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-groups/create#--max-wait)`=`MAX_WAIT`; default="20m"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-groups/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a intercept endpoint group. Successful creation of an endpoint group
results in an endpoint group in ACTIVE state. Check the progress of endpoint
group creation by using `[gcloud
network-security intercept-endpoint-groups list](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-groups/list)`.
For more examples, refer to the EXAMPLES section below.

**EXAMPLES**

: To create a intercept endpoint group called `my-endpoint-group`, in
project ID `my-project`, run:
```
gcloud network-security intercept-endpoint-groups create my-endpoint-group --project=my-project --location=global --intercept-deployment-group=my-deployment-group
```

OR

```
gcloud network-security intercept-endpoint-groups create my-endpoint-group --project=my-project --location=global --intercept-deployment-group=projects/my-project/locations/global/interceptDeploymentGroups/my-deployment-group
```

OR

```
gcloud network-security intercept-endpoint-groups create projects/my-project/locations/global/interceptEndpointGroups/my-endpoint-group --intercept-deployment-group=projects/my-project/locations/global/interceptDeploymentGroups/my-deployment-group
```

OR

```
gcloud network-security intercept-endpoint-groups create my-endpoint-group --project=my-project --location=global --mirroring-deployment-group=projects/my-project/locations/global/interceptDeploymentGroups/my-deployment-group --description='new description'
```

**POSITIONAL ARGUMENTS**

: **Intercept endpoint group resource - Intercept Endpoint Group. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `INTERCEPT_ENDPOINT_GROUP` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INTERCEPT_ENDPOINT_GROUP`**:
ID of the intercept endpoint group or fully qualified identifier for the
intercept endpoint group.
To set the `endpoint-group-id` attribute:

- provide the argument `INTERCEPT_ENDPOINT_GROUP` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the intercept endpoint group.
To set the `location` attribute:

- provide the argument `INTERCEPT_ENDPOINT_GROUP` on the command line
with a fully specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **Intercept deployment group resource - Intercept Deployment Group. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `--intercept-deployment-group` on the command
line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--intercept-deployment-group**:
ID of the intercept deployment group or fully qualified identifier for the
intercept deployment group.
To set the `id` attribute:

- provide the argument `--intercept-deployment-group` on the command
line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--intercept-deployment-group-location**:
Location of the intercept deployment group.
To set the `location` attribute:

- provide the argument `--intercept-deployment-group` on the command
line with a fully specified name;
- provide the argument `--intercept-deployment-group-location` on the
command line;
- provide the argument `--location` on the command line;
- provide the argument `INTERCEPT_ENDPOINT_GROUP` on the command line
with a fully specified name.**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--description**:
Description of the endpoint

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
gcloud alpha network-security intercept-endpoint-groups create
```

```
gcloud beta network-security intercept-endpoint-groups create
```