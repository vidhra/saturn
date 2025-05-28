# gcloud compute routers nats rules list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/list](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/list)*

**NAME**

: **gcloud compute routers nats rules list - lists the NATs on a Compute Engine router**

**SYNOPSIS**

: **`gcloud compute routers nats rules list` `[--nat](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/list#--nat)`=`NAT` `[--router](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/list#--router)`=`ROUTER` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/list#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute routers nats rules list` is used to list the Rule on
a Compute Engine NAT.

**EXAMPLES**

: To list all Rules in Nat ``n1`` in router
``r1`` in region
``us-central1``, run:

```
gcloud compute routers nats rules list --nat=n1 --router=r1 --region=us-central1.
```

**REQUIRED FLAGS**

: **--nat**:
Name of the NAT that contains the Rule

**--router**:
The Router to use for NAT.

**OPTIONAL FLAGS**

: **--region**:
Region of the NAT containing the Rules to list. If not specified, you might be
prompted to select a region (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/region`` property:

```
gcloud config set compute/region REGION
```

A list of regions can be fetched by running:

```
gcloud compute regions list
```

To unset the property, run:

```
gcloud config unset compute/region
```

Alternatively, the region can be stored in the environment variable
``CLOUDSDK_COMPUTE_REGION``.

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
gcloud alpha compute routers nats rules list
```

```
gcloud beta compute routers nats rules list
```