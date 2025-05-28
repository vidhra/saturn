# gcloud network-connectivity policy-based-routes delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/delete](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/delete)*

**NAME**

: **gcloud network-connectivity policy-based-routes delete - delete a policy-based route**

**SYNOPSIS**

: **`gcloud network-connectivity policy-based-routes delete` `[POLICY_BASED_ROUTE](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/delete#POLICY_BASED_ROUTE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete the specified policy-based route.

**EXAMPLES**

: To delete a policy-based route named
``my-pbr``, run:

```
gcloud network-connectivity policy-based-routes delete my-pbr
```

**POSITIONAL ARGUMENTS**

: **Policy based route resource - Name of the policy-based route to be deleted. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `policy_based_route` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`POLICY_BASED_ROUTE`**:
ID of the policy based route or fully qualified identifier for the policy based
route.
To set the `policy_based_route` attribute:

- provide the argument `policy_based_route` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

**API REFERENCE**

: This command uses the `networkconnectivity/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest](https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest)

**NOTES**

: These variants are also available:

```
gcloud alpha network-connectivity policy-based-routes delete
```

```
gcloud beta network-connectivity policy-based-routes delete
```