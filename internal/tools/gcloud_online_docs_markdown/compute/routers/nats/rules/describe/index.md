# gcloud compute routers nats rules describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/describe](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/describe)*

**NAME**

: **gcloud compute routers nats rules describe - describe a Rule in a Compute Engine NAT**

**SYNOPSIS**

: **`gcloud compute routers nats rules describe` `[RULE_NUMBER](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/describe#RULE_NUMBER)` `[--nat](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/describe#--nat)`=`NAT` `[--router](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/describe#--router)`=`ROUTER` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/describe#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute routers nats rules describe` is used to describe a
Rule on a Compute Engine NAT.

**EXAMPLES**

: To describe Rule 1 in NAT 'n1' in router 'r1', run:

```
gcloud compute routers nats rules describe 1 --nat=n1 --router=r1 --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`RULE_NUMBER`**:
Number that uniquely identifies the Rule to operate on

**REQUIRED FLAGS**

: **--nat**:
Name of the NAT that contains the Rule

**--router**:
The Router to use for NAT.

**OPTIONAL FLAGS**

: **--region**:
Region of the NAT containing the Rule to describe. If not specified, you might
be prompted to select a region (interactive mode only).
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
gcloud alpha compute routers nats rules describe
```

```
gcloud beta compute routers nats rules describe
```