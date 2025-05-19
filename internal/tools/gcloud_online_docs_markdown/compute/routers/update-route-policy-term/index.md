# gcloud compute routers update-route-policy-term  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-route-policy-term](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-route-policy-term)*

**NAME**

: **gcloud compute routers update-route-policy-term - updates a term of an existing route policy of a Comute Engine router**

**SYNOPSIS**

: **`gcloud compute routers update-route-policy-term` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-route-policy-term#NAME)` `[--actions](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-route-policy-term#--actions)`=[`ACTION`;…] `[--match](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-route-policy-term#--match)`=`MATCH` `[--policy-name](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-route-policy-term#--policy-name)`=`POLICY_NAME` `[--priority](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-route-policy-term#--priority)`=`PRIORITY` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-route-policy-term#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/routers/update-route-policy-term#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute routers update-route-policy-term` updates a term of a
route policy.

**EXAMPLES**

: To update a term with priority 128 with match `destination ==
'192.168.0.0/24'` and actions
`med.set(12345);asPath.prependSequence([1, 2])` of a route policy
`example-policy-name` of a router `example-router` in
region `router-region`, run:

```
gcloud compute routers update-route-policy-term example-router --region=router-region --policy-name=example-policy-name --priority=128 --match="destination == '192.168.0.0/24'" --actions="med.set(12345);asPath.prependSequence([1, 2])"
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the router to update.

**REQUIRED FLAGS**

: **--actions**:
Semicolon separated CEL expressions for the actions to take when the rule
matches.

**--match**:
CEL expression for matching a route.

**--policy-name**:
Name of the route policy to which the term should be updated.

**--priority**:
Order of the term within the policy.

**OPTIONAL FLAGS**

: **--region**:
Region of the router to update. If not specified, you might be prompted to
select a region (interactive mode only).
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
gcloud alpha compute routers update-route-policy-term
```

```
gcloud beta compute routers update-route-policy-term
```