# gcloud network-connectivity policy-based-routes create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/create](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/create)*

**NAME**

: **gcloud network-connectivity policy-based-routes create - create a new policy-based route**

**SYNOPSIS**

: **`gcloud network-connectivity policy-based-routes create` `[POLICY_BASED_ROUTE](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/create#POLICY_BASED_ROUTE)` `[--network](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/create#--network)`=`NETWORK` [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/create#--description)`=`DESCRIPTION`] [`[--destination-range](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/create#--destination-range)`=`DESTINATION_RANGE`] [`[--ip-protocol](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/create#--ip-protocol)`=`IP_PROTOCOL`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--priority](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/create#--priority)`=`PRIORITY`] [`[--protocol-version](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/create#--protocol-version)`=`PROTOCOL_VERSION`; default="IPV4"] [`[--source-range](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/create#--source-range)`=`SOURCE_RANGE`] [`[--interconnect-attachment-region](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/create#--interconnect-attachment-region)`=`INTERCONNECT_ATTACHMENT_REGION`     | `[--tags](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/create#--tags)`=[`TAGS`,…]] [`[--next-hop-ilb-ip](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/create#--next-hop-ilb-ip)`=`NEXT_HOP_ILB_IP`     | `[--next-hop-other-routes](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/create#--next-hop-other-routes)`=`NEXT_HOP_OTHER_ROUTES`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new policy-based route with the given name.

**EXAMPLES**

: To create a policy-based route with the name
``my-pbr`` to route all traffic in
``default`` network to an internal load
balancer with IP 10.0.0.1, run:

```
gcloud network-connectivity policy-based-routes create my-pbr --network="projects/my-project/global/networks/default" --next-hop-ilb-ip=10.0.0.1
```

**POSITIONAL ARGUMENTS**

: **Policy based route resource - Name of the policy-based route to be created. This
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

**REQUIRED FLAGS**

: **--network**:
Fully-qualified URL of the network that this route applies to. E.g.
`projects/my-project/global/networks/my-network`

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Optional description of this resource. Provide this field when you create the
resource.

**--destination-range**:
Destination IP range of outgoing packets that this policy-based route applies
to.

**--ip-protocol**:
IP protocol that this policy-based route applies to. Valid values are
`TCP`, `UDP`, and `ALL`. Default is
`ALL`.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--priority**:
Priority of this policy-based route. Priority is used to break ties in cases
where there are more than one matching policy-based routes found. In cases where
multiple policy-based routes are matched, the one with the lowest-numbered
priority value wins. The default value is 1000. The priority value must be from
1 to 65535, inclusive. Note the priority of policy-based route is always higher
than other types of route (e.g. static routes/advanced routes)

**--protocol-version**:
Internet protocol versions that this policy-based route applies to. For this
version, only `IPV4` is supported.
`PROTOCOL_VERSION` must be one of: `ipv4`,
`protocol-version-unspecified`.

**--source-range**:
Source IP range of outgoing packets that this policy-based route applies to.

**--interconnect-attachment-region**

**--next-hop-ilb-ip**

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
gcloud alpha network-connectivity policy-based-routes create
```

```
gcloud beta network-connectivity policy-based-routes create
```