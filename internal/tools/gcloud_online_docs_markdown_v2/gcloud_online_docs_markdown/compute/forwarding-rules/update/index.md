# gcloud compute forwarding-rules update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update)*

**NAME**

: **gcloud compute forwarding-rules update - update a Compute Engine forwarding rule**

**SYNOPSIS**

: **`gcloud compute forwarding-rules update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update#NAME)` [`[--allow-global-access](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update#--allow-global-access)`] [`[--allow-psc-global-access](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update#--allow-psc-global-access)`] [`[--external-managed-backend-bucket-migration-testing-percentage](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update#--external-managed-backend-bucket-migration-testing-percentage)`=`EXTERNAL_MANAGED_BACKEND_BUCKET_MIGRATION_TESTING_PERCENTAGE`] [`[--load-balancing-scheme](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update#--load-balancing-scheme)`=`LOAD_BALANCING_SCHEME`] [`[--source-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update#--source-ip-ranges)`=`SOURCE_IP_RANGE`,[…]] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-external-managed-backend-bucket-migration-state](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update#--clear-external-managed-backend-bucket-migration-state)`     | `[--external-managed-backend-bucket-migration-state](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update#--external-managed-backend-bucket-migration-state)`=`EXTERNAL_MANAGED_BACKEND_BUCKET_MIGRATION_STATE`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update#--remove-labels)`=[`KEY`,…]] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute forwarding-rules update` updates global access for a
Compute Engine forwarding rule.

**EXAMPLES**

: To update the forwarding rule to allow global access, run:

```
gcloud compute forwarding-rules update example-fr --allow-global-access --region=us-central1
```

To add/update labels ``k0`` and
``k1`` and remove labels with key
``k3``, run:

```
gcloud compute forwarding-rules update example-fr --region=us-central1 --update-labels=k0=value1,k1=value2 --remove-labels=k3
```

Labels can be used to identify the forwarding rule and to filter them as in

```
gcloud compute forwarding-rules list --filter='labels.k1:value2'
```

To list existing labels, run:

```
gcloud compute forwarding-rules describe example-fr --format="default(labels)"
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the forwarding rule to operate on.

**FLAGS**

: **--allow-global-access**:
If True, then clients from all regions can access this internal forwarding rule.
This can only be specified for forwarding rules with the LOAD_BALANCING_SCHEME
set to INTERNAL or INTERNAL_MANAGED. For forwarding rules of type INTERNAL, the
target must be either a backend service or a target instance.

**--allow-psc-global-access**:
If specified, clients from all regions can access this Private Service Connect
forwarding rule. This can only be specified if the forwarding rule's target is a
service attachment (--target-service-attachment).

**--external-managed-backend-bucket-migration-testing-percentage**:
Determines the fraction of requests that should be processed by the Global
external Application Load Balancer.
The value of this field must be in the range [0, 100].

**--load-balancing-scheme**:
Only for the Global external Application Load Balancer migration.
The value of this field must be EXTERNAL or EXTERNAL_MANAGED.
`LOAD_BALANCING_SCHEME` must be one of:
`EXTERNAL`, `EXTERNAL_MANAGED`.

**--source-ip-ranges**:
List of comma-separated IP addresses or IP ranges. If set, this forwarding rule
only forwards traffic when the packet's source IP address matches one of the IP
ranges set here.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-external-managed-backend-bucket-migration-state**

**--clear-labels**

**--global**

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
gcloud alpha compute forwarding-rules update
```

```
gcloud beta compute forwarding-rules update
```