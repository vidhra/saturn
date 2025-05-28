# gcloud network-security mirroring-deployments create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/create](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/create)*

**NAME**

: **gcloud network-security mirroring-deployments create - create a Mirroring Deployment**

**SYNOPSIS**

: **`gcloud network-security mirroring-deployments create` (`[MIRRORING_DEPLOYMENT](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/create#MIRRORING_DEPLOYMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/create#--location)`=`LOCATION`) (`[--forwarding-rule](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/create#--forwarding-rule)`=`FORWARDING_RULE` : `[--forwarding-rule-location](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/create#--forwarding-rule-location)`=`FORWARDING_RULE_LOCATION`) (`[--mirroring-deployment-group](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/create#--mirroring-deployment-group)`=`MIRRORING_DEPLOYMENT_GROUP` : `[--mirroring-deployment-group-location](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/create#--mirroring-deployment-group-location)`=`MIRRORING_DEPLOYMENT_GROUP_LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--max-wait](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/create#--max-wait)`=`MAX_WAIT`; default="20m"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a mirroring deployment. Successful creation of a deployment results in a
deployment in ACTIVE state. Check the progress of deployment creation by using
`[gcloud
network-security mirroring-deployments list](https://cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/list)`.
For more examples, refer to the EXAMPLES section below.

**EXAMPLES**

: To create a mirroring deployment called `my-deployment`, in project
ID `my-project` and zone `us-central1-a`, run:
```
gcloud network-security mirroring-deployments create my-deployment --project=my-project --location=us-central1-a --deployment-group-location=global --forwarding-rule=my-forwarding-rule --forwarding-rule-location=us-central1 --mirroring-deployment-group=my-deployment-group
```

OR

```
gcloud network-security mirroring-deployments create my-deployment --project=my-project --location=us-central1-a --forwarding-rule=projects/my-project/regions/us-central1/forwardingRules/my-forwarding-rule --mirroring-deployment-group=projects/my-project/locations/global/mirroringDeploymentGroups/my-deployment-group
```

OR

```
gcloud network-security mirroring-deployments create projects/my-project/locations/us-central1/mirroringDeployments/my-deployment --forwarding-rule=projects/my-project/regions/us-central1/forwardingRules/my-forwarding-rule --mirroring-deployment-group=projects/my-project/locations/global/mirroringDeploymentGroups/my-deployment-group
```

OR

```
gcloud network-security mirroring-deployments create projects/my-project/locations/us-central1/mirroringDeployments/my-deployment --forwarding-rule=projects/my-project/regions/us-central1/forwardingRules/my-forwarding-rule --mirroring-deployment-group=projects/my-project/locations/global/mirroringDeploymentGroups/my-deployment-group --description="my-description"
```

**POSITIONAL ARGUMENTS**

: **Mirroring deployment resource - Mirroring Deployment. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `MIRRORING_DEPLOYMENT` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`MIRRORING_DEPLOYMENT`**:
ID of the mirroring deployment or fully qualified identifier for the mirroring
deployment.
To set the `deployment-id` attribute:

- provide the argument `MIRRORING_DEPLOYMENT` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the mirroring deployment.
To set the `location` attribute:

- provide the argument `MIRRORING_DEPLOYMENT` on the command line with
a fully specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **ForwardingRule resource - Mirroring Deployment Forwarding Rule. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--forwarding-rule` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--forwarding-rule**:
ID of the forwardingRule or fully qualified identifier for the forwardingRule.
To set the `forwarding-rule-id` attribute:

- provide the argument `--forwarding-rule` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--forwarding-rule-location**:
The Cloud region for the forwardingRule.
To set the `forwarding-rule-location` attribute:

- provide the argument `--forwarding-rule` on the command line with a
fully specified name;
- provide the argument `--forwarding-rule-location` on the command
line.**

**Mirroring deployment group resource - Mirroring Deployment Group. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `--mirroring-deployment-group` on the command
line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--mirroring-deployment-group**:
ID of the mirroring deployment group or fully qualified identifier for the
mirroring deployment group.
To set the `id` attribute:

- provide the argument `--mirroring-deployment-group` on the command
line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--mirroring-deployment-group-location**:
Location of the mirroring deployment group.
To set the `location` attribute:

- provide the argument `--mirroring-deployment-group` on the command
line with a fully specified name;
- provide the argument `--mirroring-deployment-group-location` on the
command line;
- provide the argument `--location` on the command line;
- provide the argument
`networksecurity.projects.locations.mirroringDeployments` on the
command line with a fully specified name.**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--description**:
Description of the mirroring deployment

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
gcloud alpha network-security mirroring-deployments create
```

```
gcloud beta network-security mirroring-deployments create
```