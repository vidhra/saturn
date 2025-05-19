# gcloud compute routers remove-route-policy-term  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/routers/remove-route-policy-term](https://cloud.google.com/sdk/gcloud/reference/compute/routers/remove-route-policy-term)*

**NAME**

: **gcloud compute routers remove-route-policy-term - remove a route policy term of a Compute Engine router**

**SYNOPSIS**

: **`gcloud compute routers remove-route-policy-term` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/routers/remove-route-policy-term#NAME)` `[--policy-name](https://cloud.google.com/sdk/gcloud/reference/compute/routers/remove-route-policy-term#--policy-name)`=`POLICY_NAME` `[--priority](https://cloud.google.com/sdk/gcloud/reference/compute/routers/remove-route-policy-term#--priority)`=`PRIORITY` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/routers/remove-route-policy-term#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/routers/remove-route-policy-term#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute routers remove-route-policy-term` removes a term of a
route policy.

**EXAMPLES**

: To remove a route policy term with priority 0 from a route policy
`my-policy` from a router `my-router` in region
`us-central1`, run:

```
gcloud compute routers remove-route-policy-term my-router --region=us-central1 --policy-name=my-policy --priority=0
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the router to remove a route policy term from.

**REQUIRED FLAGS**

: **--policy-name**:
Name of the route policy from which the term should be removed.

**--priority**:
Order of the term within the policy.

**OPTIONAL FLAGS**

: **--region**:
Region of the router to remove a route policy term from. If not specified, you
might be prompted to select a region (interactive mode only).
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
gcloud alpha compute routers remove-route-policy-term
```

```
gcloud beta compute routers remove-route-policy-term
```