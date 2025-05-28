# gcloud workstations configs create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create)*

**NAME**

: **gcloud workstations configs create - create a workstation configuration**

**SYNOPSIS**

: **`gcloud workstations configs create` (`[CONFIG](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#CONFIG)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--cluster)`=`CLUSTER` `[--region](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--region)`=`REGION`) [`[--allowed-ports](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--allowed-ports)`=[`ALLOWED_PORTS`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--async)`] [`[--boot-disk-size](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--boot-disk-size)`=`BOOT_DISK_SIZE`; default=50] [`[--container-args](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--container-args)`=[`CONTAINER_ARGS`,…]] [`[--container-command](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--container-command)`=[`CONTAINER_COMMAND`,…]] [`[--container-env](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--container-env)`=[`CONTAINER_ENV`,…]] [`[--container-run-as-user](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--container-run-as-user)`=`CONTAINER_RUN_AS_USER`] [`[--container-working-dir](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--container-working-dir)`=`CONTAINER_WORKING_DIR`] [`[--disable-public-ip-addresses](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--disable-public-ip-addresses)`] [`[--disable-ssh-to-vm](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--disable-ssh-to-vm)`] [`[--disable-tcp-connections](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--disable-tcp-connections)`] [`[--enable-audit-agent](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--enable-audit-agent)`] [`[--enable-confidential-compute](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--enable-confidential-compute)`] [`[--enable-nested-virtualization](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--enable-nested-virtualization)`] [`[--enable-ssh-to-vm](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--enable-ssh-to-vm)`] [`[--ephemeral-directory](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--ephemeral-directory)`=[`PROPERTY`=`VALUE`,…]] [`[--grant-workstation-admin-role-on-create](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--grant-workstation-admin-role-on-create)`] [`[--idle-timeout](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--idle-timeout)`=`IDLE_TIMEOUT`; default=7200] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--labels)`=[`LABELS`,…]] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--machine-type)`=`MACHINE_TYPE`; default="e2-standard-4"] [`[--max-usable-workstations-count](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--max-usable-workstations-count)`=`MAX_USABLE_WORKSTATIONS_COUNT`] [`[--network-tags](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--network-tags)`=[`NETWORK_TAGS`,…]] [`[--pd-disk-type](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--pd-disk-type)`=`PD_DISK_TYPE`; default="pd-standard"] [`[--pd-reclaim-policy](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--pd-reclaim-policy)`=`PD_RECLAIM_POLICY`; default="delete"] [`[--pool-size](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--pool-size)`=`POOL_SIZE`] [`[--replica-zones](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--replica-zones)`=[`REPLICA_ZONES`,…]] [`[--running-timeout](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--running-timeout)`=`RUNNING_TIMEOUT`; default=7200] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--service-account)`=`SERVICE_ACCOUNT`] [`[--service-account-scopes](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--service-account-scopes)`=[`SERVICE_ACCOUNT_SCOPES`,…]] [`[--shielded-integrity-monitoring](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--shielded-integrity-monitoring)`] [`[--shielded-secure-boot](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--shielded-secure-boot)`] [`[--shielded-vtpm](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--shielded-vtpm)`] [`[--vm-tags](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--vm-tags)`=[`VM_TAGS`,…]] [`[--accelerator-count](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--accelerator-count)`=`ACCELERATOR_COUNT` : `[--accelerator-type](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--accelerator-type)`=`ACCELERATOR_TYPE`] [`[--container-custom-image](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--container-custom-image)`=`CONTAINER_CUSTOM_IMAGE`     | `[--container-predefined-image](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--container-predefined-image)`=`CONTAINER_PREDEFINED_IMAGE`; default="codeoss"] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--kms-key)`=`KMS_KEY` : `[--kms-key-service-account](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--kms-key-service-account)`=`KMS_KEY_SERVICE_ACCOUNT`] [`[--pd-disk-size](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--pd-disk-size)`=`PD_DISK_SIZE`; default=200     | `[--pd-source-snapshot](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#--pd-source-snapshot)`=`PD_SOURCE_SNAPSHOT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a workstation configuration.

**EXAMPLES**

: To create a configuration with the 'e2-standard-8' machine type and a IntelliJ
image, run:

```
gcloud workstations configs create CONFIG --machine-type=e2-standard-8 --container-predefined-image=intellij
```

To create a configuration with a Shielded VM instance that enables Secure Boot,
virtual trusted platform module (vTPM) and integrity monitoring, run:

```
gcloud workstations configs create CONFIG --machine-type=e2-standard-4 --shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring
```

To create a configuration with a non-default persistent disk containing 10GB of
PD SSD storage, run:
```
gcloud workstations configs create CONFIG --machine-type=e2-standard-4 --pd-disk-type=pd-ssd --pd-disk-size=10
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
gcloud workstations configs create --allowed-ports=first=9000,last=9090
gcloud workstations configs create --allowed-ports=first=80,last=80
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
gcloud workstations configs create --container-args=arg_1,arg_2
```

**--container-command**:
If set, overrides the default ENTRYPOINT specified by the image.
Example:

```
gcloud workstations configs create --container-command=executable,parameter_1,parameter_2
```

**--container-env**:
Environment variables passed to the container.
Example:

```
gcloud workstations configs create --container-env=key1=value1,key2=value2
```

**--container-run-as-user**:
If set, overrides the USER specified in the image with the given uid.

**--container-working-dir**:
If set, overrides the default DIR specified by the image.

**--disable-public-ip-addresses**:
Default value is false. If set, instances will have no public IP address.

**--disable-ssh-to-vm**:
(DEPRECATED) Default value is False. If set, workstations disable SSH
connections to the root VM.
The --disable-ssh-to-vm option is deprecated; use --enable-ssh-to-vm instead.

**--disable-tcp-connections**:
Default value is false. If set, workstations don't allow plain TCP connections.

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

**--enable-ssh-to-vm**:
Default value is False. If set, workstations enable SSH connections to the root
VM.

**--ephemeral-directory**:
Ephemeral directory which won't persist across workstation sessions.

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
gcloud workstations configs create --labels=label1=value1,label2=value2
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
gcloud workstations configs create --network-tags=tag_1,tag_2
```

**--pd-disk-type**:
Type of the persistent directory. `PD_DISK_TYPE` must be
one of: `pd-standard`, `pd-balanced`, `pd-ssd`.

**--pd-reclaim-policy**:
What should happen to the disk after the Workstation is deleted.
`PD_RECLAIM_POLICY` must be one of:

**`delete`**:
The persistent disk will be deleted with the Workstation.

**`retain`**:
The persistent disk will be remain after the workstation is deleted and the
administrator must manually delete the disk.

**--pool-size**:
Number of instances to pool for faster Workstation startup.

**--replica-zones**:
Specifies the zones the VM and disk resources will be replicated within the
region. If set, exactly two zones within the workstation cluster's region must
be specified.
Example:

```
gcloud workstations configs create --replica-zones=us-central1-a,us-central1-f
```

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
gcloud workstations configs create --vm-tags=tagKeys/key1=tagValues/value1,tagKeys/key2=tagValues/value2
```

**--accelerator-count**

**--container-custom-image**

**--kms-key**

**--pd-disk-size**

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
gcloud alpha workstations configs create
```

```
gcloud beta workstations configs create
```