# gcloud alpha bigtable app-profiles update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/update](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/update)*

**NAME**

: **gcloud alpha bigtable app-profiles update - update a Bigtable app profile**

**SYNOPSIS**

: **`gcloud alpha bigtable app-profiles update` (`[APP_PROFILE](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/update#APP_PROFILE)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/update#--instance)`=`INSTANCE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/update#--description)`=`DESCRIPTION`] [`[--force](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/update#--force)`] [`[--data-boost](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/update#--data-boost)` `[--data-boost-compute-billing-owner](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/update#--data-boost-compute-billing-owner)`=`DATA_BOOST_COMPUTE_BILLING_OWNER`     | [`[--priority](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/update#--priority)`=`PRIORITY` : `[--standard](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/update#--standard)`]] [[`[--route-any](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/update#--route-any)` : `[--restrict-to](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/update#--restrict-to)`=[`RESTRICT_TO`,…] `[--row-affinity](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/update#--row-affinity)`]     | [`[--route-to](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/update#--route-to)`=`ROUTE_TO` : `[--transactional-writes](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/update#--transactional-writes)`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable/app-profiles/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update a Bigtable app profile.

**EXAMPLES**

: To update an app profile to use a multi-cluster routing policy, run:

```
gcloud alpha bigtable app-profiles update my-app-profile-id --instance=my-instance-id --route-any
```

To update an app profile to use a single-cluster routing policy that routes all
requests to `my-cluster-id` and allows transactional writes, run:

```
gcloud alpha bigtable app-profiles update my-app-profile-id --instance=my-instance-id --route-to=my-cluster-id --transactional-writes
```

To update the description for an app profile, run:

```
gcloud alpha bigtable app-profiles update my-app-profile-id --instance=my-instance-id --description="New description"
```

To update the request priority for an app profile to PRIORITY_LOW, run:

```
gcloud alpha bigtable app-profiles update my-app-profile-id --instance=my-instance-id --priority=PRIORITY_LOW
```

To update an app profile to enable Data Boost which bills usage to the host
project, run:

```
gcloud alpha bigtable app-profiles update my-app-profile-id --instance=my-instance-id --data-boost --data-boost-compute-billing-owner=HOST_PAYS
```

To update an app profile to enable row-affinity routing, run:

```
gcloud alpha bigtable app-profiles update my-app-profile-id --instance=my-instance-id --route-any --row-affinity
```

**POSITIONAL ARGUMENTS**

: **App profile resource - The app profile to update. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `app_profile` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`APP_PROFILE`**:
ID of the app profile or fully qualified identifier for the app profile.
To set the `name` attribute:

- provide the argument `app_profile` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--instance**:
Bigtable instance for the app profile.
To set the `instance` attribute:

- provide the argument `app_profile` on the command line with a fully
specified name;
- provide the argument `--instance` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Friendly name of the app profile.

**--force**:
Ignore warnings and force update.

**--data-boost**

**--route-any**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud bigtable app-profiles update
```

```
gcloud beta bigtable app-profiles update
```