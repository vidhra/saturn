# gcloud workstations configs update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update)*

**NAME**

: **gcloud workstations configs update - updates a workstation configuration**

**SYNOPSIS**

: **`gcloud workstations configs update` (`[CONFIG](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#CONFIG)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--cluster)`=`CLUSTER` `[--region](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--region)`=`REGION`) [`[--allowed-ports](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--allowed-ports)`=[`ALLOWED_PORTS`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--async)`] [`[--boot-disk-size](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--boot-disk-size)`=`BOOT_DISK_SIZE`] [`[--container-args](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--container-args)`=[`CONTAINER_ARGS`,…]] [`[--container-command](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--container-command)`=[`CONTAINER_COMMAND`,…]] [`[--container-env](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--container-env)`=[`CONTAINER_ENV`,…]] [`[--container-run-as-user](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--container-run-as-user)`=`CONTAINER_RUN_AS_USER`] [`[--container-working-dir](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--container-working-dir)`=`CONTAINER_WORKING_DIR`] [`[--disable-public-ip-addresses](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--disable-public-ip-addresses)`] [`[--enable-audit-agent](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--enable-audit-agent)`] [`[--enable-confidential-compute](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--enable-confidential-compute)`] [`[--enable-nested-virtualization](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--enable-nested-virtualization)`] [`[--grant-workstation-admin-role-on-create](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--grant-workstation-admin-role-on-create)`] [`[--idle-timeout](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--idle-timeout)`=`IDLE_TIMEOUT`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--labels)`=[`LABELS`,…]] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--machine-type)`=`MACHINE_TYPE`] [`[--max-usable-workstations-count](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--max-usable-workstations-count)`=`MAX_USABLE_WORKSTATIONS_COUNT`] [`[--network-tags](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--network-tags)`=[`NETWORK_TAGS`,…]] [`[--pool-size](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--pool-size)`=`POOL_SIZE`] [`[--running-timeout](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--running-timeout)`=`RUNNING_TIMEOUT`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--service-account)`=`SERVICE_ACCOUNT`] [`[--service-account-scopes](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--service-account-scopes)`=[`SERVICE_ACCOUNT_SCOPES`,…]] [`[--shielded-integrity-monitoring](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--shielded-integrity-monitoring)`] [`[--shielded-secure-boot](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--shielded-secure-boot)`] [`[--shielded-vtpm](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--shielded-vtpm)`] [`[--vm-tags](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--vm-tags)`=[`VM_TAGS`,…]] [`[--accelerator-count](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--accelerator-count)`=`ACCELERATOR_COUNT` : `[--accelerator-type](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--accelerator-type)`=`ACCELERATOR_TYPE`] [`[--container-custom-image](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--container-custom-image)`=`CONTAINER_CUSTOM_IMAGE`     | `[--container-predefined-image](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--container-predefined-image)`=`CONTAINER_PREDEFINED_IMAGE`] [`[--disable-ssh-to-vm](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--disable-ssh-to-vm)`     | `[--enable-ssh-to-vm](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--enable-ssh-to-vm)`] [`[--disable-tcp-connections](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--disable-tcp-connections)`     | `[--enable-tcp-connections](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--enable-tcp-connections)`] [`[--pd-source-snapshot](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--pd-source-snapshot)`=`PD_SOURCE_SNAPSHOT`     | `[--pd-disk-size](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--pd-disk-size)`=`PD_DISK_SIZE` `[--pd-disk-type](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#--pd-disk-type)`=`PD_DISK_TYPE`; default="pd-standard"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates a workstation configuration.

**EXAMPLES**

: To update a configuration with the 'e2-standard-8' machine type and a IntelliJ
image, run:

```
gcloud workstations configs update CONFIG --machine-type=e2-standard-8 --container-predefined-image=intellij
```

To update a configuration to disable Secure Boot, virtual trusted platform
module (vTPM) and integrity monitoring, run:

```
gcloud workstations configs update CONFIG --no-shielded-secure-boot --no-shielded-vtpm --no-shielded-integrity-monitoring
```

**POSITIONAL ARGUMENTS**

: **Config resource - The group of arguments defining a config The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `config` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CONFIG`**:
ID of the config or fully qualified identifier for the config.
To set the `config` attribute:

- provide the argument `config` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--cluster**:
The cluster for the config.
To set the `cluster` attribute:

- provide the argument `config` on the command line with a fully
specified name;
- provide the argument `--cluster` on the command line;
- set the property `workstations/cluster`.

**--region**:
The region for the config.
To set the `region` attribute:

- provide the argument `config` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `workstations/region`.**

**FLAGS**

: **--allowed-ports**:
A Single or Range of ports externally accessible in the workstation. If not
specified defaults to ports 22, 80 and ports 1024-65535.
To specify a single port, both first and last should be same.
Example:

```
gcloud workstations configs update --allowed-ports=first=9000,last=9090
gcloud workstations configs update --allowed-ports=first=80,last=80
```

Sets `allowed_ports` value.

**`first`**:
Required, sets `first` value.

**`last`**:
Required, sets `last` value.

`Shorthand Example:`

```
--allowed-ports=first=int,last=int
```

`JSON Example:`

```
--allowed-ports='{"first": int, "last": int}'
```

`File Example:`

```
--allowed-ports=path_to_file.(yaml|json)
```

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--boot-disk-size**:
Size of the boot disk in GB.

**--container-args**:
Arguments passed to the entrypoint.
Example:

```
gcloud workstations configs update --container-args=arg_1,arg_2
```

**--container-command**:
If set, overrides the default ENTRYPOINT specified by the image.
Example:

```
gcloud workstations configs update --container-command=executable,parameter_1,parameter_2
```

**--container-env**:
Environment variables passed to the container.
Example:

```
gcloud workstations configs update --container-env=key1=value1,key2=value2
```

**--container-run-as-user**:
If set, overrides the USER specified in the image with the given uid.

**--container-working-dir**:
If set, overrides the default DIR specified by the image.

**--disable-public-ip-addresses**:
Default value is false. If set, instances will have no public IP address.

**--enable-audit-agent**:
Whether to enable Linux `auditd` logging on the workstation. When
enabled, a service account must also be specified that has
`logging.buckets.write` permission on the project.

**--enable-confidential-compute**:
Default value is false. If set, instances will have confidential compute
enabled.

**--enable-nested-virtualization**:
Default value is false. If set, instances will have nested virtualization
enabled.

**--grant-workstation-admin-role-on-create**:
Default value is false. If set, creator of a workstation will get
`roles/workstations.policyAdmin` role along with
`roles/workstations.user` role on the workstation created by them.

**--idle-timeout**:
How long (in seconds) to wait before automatically stopping an instance that
hasn't received any user traffic. A value of 0 indicates that this instance
should never time out due to idleness.

**--labels**:
Labels that are applied to the configuration and propagated to the underlying
Compute Engine resources.
Example:

```
gcloud workstations configs update --labels=label1=value1,label2=value2
```

**--machine-type**:
Machine type determines the specifications of the Compute Engine machines that
the workstations created under this configuration will run on.

**--max-usable-workstations-count**:
Maximum number of workstations under this configuration a user can have
`workstations.workstation.use` permission on.
If not specified, defaults to `0`, which indicates a user can have
unlimited number of workstations under this configuration.

**--network-tags**:
Network tags to add to the Google Compute Engine machines backing the
Workstations.
Example:

```
gcloud workstations configs update --network-tags=tag_1,tag_2
```

**--pool-size**:
Number of instances to pool for faster Workstation startup.

**--running-timeout**:
How long (in seconds) to wait before automatically stopping a workstation after
it started. A value of 0 indicates that workstations using this config should
never time out.

**--service-account**:
Email address of the service account that will be used on VM instances used to
support this config. This service account must have permission to pull the
specified container image. If not set, VMs will run without a service account,
in which case the image must be publicly accessible.

**--service-account-scopes**:
Scopes to grant to the service_account. Various scopes are automatically added
based on feature usage. When specified, users of workstations under this
configuration must have iam.serviceAccounts.actAs`on the service account.`

**--shielded-integrity-monitoring**:
Default value is false. If set, instances will have integrity monitoring
enabled.

**--shielded-secure-boot**:
Default value is false. If set, instances will have Secure Boot enabled.

**--shielded-vtpm**:
Default value is false. If set, instances will have vTPM enabled.

**--vm-tags**:
Resource manager tags to be bound to the instance. Tag keys and values have the
same definition as [https://cloud.google.com/resource-manager/docs/tags/tags-overview](https://cloud.google.com/resource-manager/docs/tags/tags-overview)
Example:

```
gcloud workstations configs update --vm-tags=tagKeys/key1=tagValues/value1,tagKeys/key2=tagValues/value2
```

**--accelerator-count**

**--container-custom-image**

**--disable-ssh-to-vm**

**--disable-tcp-connections**

**--pd-source-snapshot**

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
gcloud alpha workstations configs update
```

```
gcloud beta workstations configs update
```